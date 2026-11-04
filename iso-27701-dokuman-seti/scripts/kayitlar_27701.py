#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_27701.py — KVYS'nin tekrar eden Excel kayitlarini uretir.

Iki surumu de destekler. En degerli ucu:
  * SoA  — surum (2019/2025) ve role (sorumlu/isleyen/her-ikisi) gore dogru
           kontrol setini ve DOGRU NUMARALANDIRMAYI uretir. Elle yapildiginda
           en sik hata numaralandirmayi karistirmaktir.
  * envanter — VERBIS alan yapisina hizali kisisel veri isleme envanteri;
           zincirin basi.
  * gecis — 2019 -> 2025 esleme ve bosluk analizi tablosu.

Kullanim:
    python3 kayitlar_27701.py --kurulus "ACME A.S." --cikti "/yol/03_Kayitlar" \\
        --surum 2025 --rol her-ikisi --tarih 2026-08-11 \\
        --hangi envanter,soa,risk,dpia,basvuru,saklama,aktarim,ihlal,riza,\\
ifsa,altyuklenici,hedef,dof,yetkinlik,dokuman,zincir,gecis,kvkk

Surum/rol bayraklari:
    --surum 2019 | 2025
    --rol   sorumlu | isleyen | her-ikisi
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

BURASI = os.path.dirname(os.path.abspath(__file__))
KONTROLLER = os.path.join(BURASI, "..", "assets", "kontroller_27701.json")

STANDART = {
    "2019": "TS ISO/IEC 27701:2019 (ISO/IEC 27701:2019) — ISO/IEC 27001 eklentisi",
    "2025": "ISO/IEC 27701:2025 — Bağımsız Kişisel Veri Yönetim Sistemi",
}

VERI_KATEGORILERI = ["Kimlik", "İletişim", "Özlük", "Finans", "Hukuki İşlem",
                     "Müşteri İşlem", "İşlem Güvenliği", "Fiziksel Mekân Güvenliği",
                     "Pazarlama", "Görsel/İşitsel Kayıt", "Mesleki Deneyim",
                     "Özel Nitelikli"]
ILGILI_KISI = ["Çalışan", "Çalışan adayı", "Eski çalışan", "Stajyer",
               "Müşteri", "Potansiyel müşteri", "Ziyaretçi", "Tedarikçi çalışanı",
               "Hissedar/ortak", "Müşteri çalışanı (işleyen rolü)", "Diğer"]
HUKUKI_SEBEP = [
    "m.5/1 Açık rıza",
    "m.5/2-a Kanunlarda açıkça öngörülme",
    "m.5/2-b Fiili imkânsızlık",
    "m.5/2-c Sözleşmenin kurulması/ifası",
    "m.5/2-ç Hukuki yükümlülük",
    "m.5/2-d İlgili kişinin alenileştirmesi",
    "m.5/2-e Hakkın tesisi/kullanılması/korunması",
    "m.5/2-f Meşru menfaat",
    "m.6/2 Açık rıza (özel nitelikli)",
    "m.6/3 Kanunda öngörülen hâller (özel nitelikli)",
]


def _kayit(bilgi: dict, ad: str, kod: str) -> YSKayit:
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=kod,
                   standart=STANDART[bilgi.get("surum", "2025")], sistem="KVYS",
                   revizyon=bilgi.get("revizyon", "00"), tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""), onaylayan=bilgi.get("onaylayan", ""))


def _kontroller() -> dict:
    with open(KONTROLLER, encoding="utf-8") as fh:
        return json.load(fh)


# ---------------------------------------------------------------------- SoA
def soa(bilgi: dict, cikti: str, uygulanmayan: dict | None = None,
        gerekce: dict | None = None, sorumlu: dict | None = None) -> str:
    """Uygulanabilirlik Bildirgesi — surum ve role gore dogru kontrol seti.

    Rol geregi uygulanmayan kontroller SILINMEZ; 'Uygulanabilir' = H yapilir ve
    'rol gereği uygulanabilir değil' gerekcesi yazilir. Denetci tam listeyi
    gormek ister.
    """
    uygulanmayan = uygulanmayan or {}
    gerekce = gerekce or {}
    sorumlu = sorumlu or {}
    surum = bilgi.get("surum", "2025")
    rol = bilgi.get("rol", "her-ikisi")
    k27 = _kontroller()

    satirlar = []
    gruplar = [("controller", "Veri sorumlusu", rol in ("sorumlu", "her-ikisi")),
               ("processor", "Veri işleyen", rol in ("isleyen", "her-ikisi"))]
    if surum == "2025":
        gruplar.append(("security", "Bilgi güvenliği (A.3)", True))

    for anahtar, grup_adi, rol_uygun in gruplar:
        for c in k27[anahtar]:
            no = c["v2019"] if (surum == "2019" and "v2019" in c) else c["v2025"]
            if surum == "2019":
                on = "A." if anahtar == "controller" else "B."
                no = on + c["v2019"]
            haric = uygulanmayan.get(no)
            if not rol_uygun:
                haric = haric or ("Kuruluş bu işleme faaliyetlerinde bu rolde "
                                  "bulunmadığından uygulanabilir değildir.")
            if haric:
                g = ""
            elif no in gerekce:
                g = gerekce[no]
            else:
                g = "[DOLDURULACAK: ilgili işleme faaliyeti no ve/veya mevzuat dayanağı]"
            satirlar.append([
                no, grup_adi, c["baslik"], "H" if haric else "E", g,
                "", "" if haric else "Planlandı",
                "" if haric else c["dokuman"], sorumlu.get(no, ""),
                "" if haric else c["kanit"], haric or "", bilgi.get("tarih", ""),
            ])

    k = _kayit(bilgi, f"Uygulanabilirlik Bildirgesi (SoA) — {surum}",
               bilgi.get("kod_soa", "KVYS-LS-11"))
    k.bilgi_sayfasi(
        aciklama=(f"ISO/IEC 27701:{surum} kapsamındaki Uygulanabilirlik Bildirgesi. "
                  f"Kuruluşun rolü: {rol}. Kontrollerin tamamı listelenmiştir; "
                  "rol gereği veya başka sebeple uygulanmayanlar silinmez, "
                  "gerekçesiyle işaretlenir."
                  + (" 2019 sürümünde bu bildirge, BGYS Uygulanabilirlik "
                     "Bildirgesi'nin eki veya genişletilmiş hâlidir."
                     if surum == "2019" else "")),
        kullanim_notu=("Risk değerlendirmesi ve işleme envanteri her güncellendiğinde "
                       "gözden geçirilir. Kontrol numaralandırması sürüme özgüdür — "
                       "2019 ve 2025 numaraları KARIŞTIRILMAMALIDIR."))
    k.sayfa("SoA",
            ["Kontrol No", "Kontrol Grubu", "Kontrol Başlığı", "Uygulanabilir (E/H)",
             "Dahil Etme Gerekçesi", "İlgili İşleme Faaliyeti No", "Uygulama Durumu",
             "Uygulayan Doküman", "Sorumlu", "Doğrulama / Kanıt",
             "Hariç Tutma Gerekçesi", "Son Gözden Geçirme"],
            satirlar,
            genislikler=[13, 20, 46, 13, 40, 20, 15, 40, 16, 44, 44, 15],
            listeler={"Uygulanabilir (E/H)": ["E", "H"],
                      "Uygulama Durumu": ["Planlandı", "Uygulanıyor", "Uygulandı",
                                          "Kısmen", "Uygulanmıyor"]},
            durum_sutunu="Uygulama Durumu",
            notlar={"Hariç Tutma Gerekçesi":
                    "Boş bırakılamaz. Rol gereği uygulanmayanlar da gerekçelendirilir.",
                    "İlgili İşleme Faaliyeti No":
                    "KVYS-LS-01 envanterindeki faaliyet numarası — zincirin kanıtı."})
    k.ozet_sayfasi("Özet", "SoA", "Uygulama Durumu",
                   ["Planlandı", "Uygulanıyor", "Uygulandı", "Kısmen", "Uygulanmıyor"])
    return k.kaydet(cikti)


# ----------------------------------------------------------------- envanter
def envanter(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Kişisel Veri İşleme Envanteri", bilgi.get("kod_env", "KVYS-LS-01"))
    k.bilgi_sayfasi(
        aciklama=("KVYS'nin merkez kaydı ve zincirin başı. Alan yapısı VERBİS "
                  "bildirimiyle hizalıdır; envanter ile VERBİS kaydı arasındaki "
                  "çelişki hem 27701 hem KVKK açısından bulgu üretir."),
        kullanim_notu=("'Kuruluşun Rolü' her faaliyet için TEKİLDİR — 'her ikisi' "
                       "yazılmaz, faaliyet bazında netleşir. 'Hukuki Sebep' boş "
                       "bırakılamaz. Yılda en az bir kez ve yeni işleme faaliyeti "
                       "başladığında güncellenir."))
    k.sayfa("İşleme Envanteri",
            ["Faaliyet No", "Faaliyet Adı", "Süreç Sahibi Birim", "Kuruluşun Rolü",
             "İlgili Kişi Grubu", "Veri Kategorileri", "Özel Nitelikli Var mı",
             "İşleme Amacı", "Hukuki Sebep", "Meşru Menfaat Testi No",
             "Toplama Yöntemi", "Aktarılan Taraflar (yurt içi)",
             "Yurt Dışına Aktarım", "Aktarım No", "Saklama Süresi",
             "Sürenin Başlangıcı", "Saklama Dayanağı", "İmha Yöntemi",
             "Teknik Tedbirler", "İdari Tedbirler", "Aydınlatma Metni Ref.",
             "Rıza Gerekiyor mu", "DPIA Gerekli mi", "DPIA No",
             "Sistem / Ortam", "Kayıt Sayısı (yaklaşık)", "Son Güncelleme", "Durum"],
            [], genislikler=[11, 36, 20, 18, 24, 30, 17, 44, 34, 17, 26, 30, 17, 13,
                             16, 24, 34, 24, 34, 30, 22, 15, 15, 12, 26, 17, 15, 12],
            listeler={"Kuruluşun Rolü": ["Veri sorumlusu", "Veri işleyen",
                                          "Ortak veri sorumlusu"],
                      "Özel Nitelikli Var mı": ["Yok", "Var"],
                      "Hukuki Sebep": HUKUKI_SEBEP,
                      "Yurt Dışına Aktarım": ["Yok", "Var"],
                      "Rıza Gerekiyor mu": ["Hayır", "Evet", "Kısmen"],
                      "DPIA Gerekli mi": ["Hayır", "Evet", "Değerlendirilmedi"],
                      "Durum": ["Aktif", "Planlanan", "Sonlandırıldı"]},
            durum_sutunu="Durum", bos_satir=60,
            notlar={"Kuruluşun Rolü": "Faaliyet bazında TEKİL. Kuruluş genelinde iki "
                                       "rolde olabilir ama tek faaliyette bir roldedir.",
                    "Hukuki Sebep": "Açık rıza SON çare. Sözleşme ifası veya kanuni "
                                     "yükümlülük varken rıza almak rızayı geçersiz kılar.",
                    "Meşru Menfaat Testi No": "m.5/2-f seçildiyse yazılı dengeleme testi zorunlu.",
                    "Saklama Dayanağı": "Mevzuat maddesi / zamanaşımı / sözleşme. "
                                         "'10 yıl' tek başına savunulamaz.",
                    "Sürenin Başlangıcı": "Tetikleyici olay: sözleşme sonu, son işlem, "
                                           "hesap dönemi kapanışı..."})
    k.ozet_sayfasi("Özet — Rol", "İşleme Envanteri", "Kuruluşun Rolü",
                   ["Veri sorumlusu", "Veri işleyen", "Ortak veri sorumlusu"])
    return k.kaydet(cikti)


# --------------------------------------------------------------------- risk
def risk(bilgi: dict, cikti: str) -> str:
    """27701'e ozgu: KURULUSA etki ve ILGILI KISIYE etki AYRI degerlendirilir."""
    k = _kayit(bilgi, "Kişisel Veri Risk Envanteri", bilgi.get("kod_risk", "KVYS-FR-05"))
    k.bilgi_sayfasi(
        aciklama=("Risk değerlendirmesi iki boyutludur: riskin KURULUŞA etkisi ve "
                  "riskin İLGİLİ KİŞİYE etkisi. İkisi farklı sorulardır ve farklı "
                  "önlemler doğurur; tek skorda birleştirilemez."),
        kullanim_notu=("İlgili kişi etkisi yüksek olan riskler, kuruluş etkisi düşük "
                       "olsa bile önceliklidir — 27701'in ayırt edici beklentisi budur."))
    k.sayfa("Risk Envanteri",
            ["Risk No", "İlgili Faaliyet No", "Risk Kategorisi", "Risk Tanımı",
             "Tehdit", "Açıklık", "Mevcut Kontroller",
             "Olasılık (1-5)",
             "Kuruluşa Etki (1-5)", "Kuruluş Risk Skoru",
             "İlgili Kişiye Etki (1-5)", "İlgili Kişi Risk Skoru",
             "Kırılgan Grup mu", "Genel Risk Seviyesi", "Risk Sahibi",
             "İşleme Seçeneği", "Planlanan Kontroller", "Sorumlu", "Termin",
             "Artık Risk", "Risk Sahibi Onayı", "Değerlendirme Tarihi",
             "Sonraki Gözden Geçirme", "Durum"],
            [], genislikler=[9, 15, 22, 44, 30, 30, 30, 12, 14, 15, 16, 16, 14, 16,
                             18, 14, 34, 16, 12, 11, 16, 15, 16, 11],
            listeler={"Risk Kategorisi": ["Yetkisiz erişim/ifşa", "Aşırı veri toplama",
                                           "Amaç dışı kullanım", "Saklama süresi aşımı",
                                           "Hatalı/güncel olmayan veri", "Hukuki sebep eksikliği",
                                           "Aktarım riski", "Veri kaybı",
                                           "İlgili kişi hakkının kullanılamaması",
                                           "Otomatik karar/profilleme", "Tedarikçi riski"],
                      "Olasılık (1-5)": [1, 2, 3, 4, 5],
                      "Kuruluşa Etki (1-5)": [1, 2, 3, 4, 5],
                      "İlgili Kişiye Etki (1-5)": [1, 2, 3, 4, 5],
                      "Kırılgan Grup mu": ["Hayır", "Evet"],
                      "İşleme Seçeneği": ["Azalt", "Kabul et", "Aktar", "Kaçın"],
                      "Risk Sahibi Onayı": ["Onaylandı", "Beklemede"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            formuller={
                "Kuruluş Risk Skoru":
                    '=IF(AND([Olasılık (1-5)]{r}<>"",[Kuruluşa Etki (1-5)]{r}<>""),'
                    '[Olasılık (1-5)]{r}*[Kuruluşa Etki (1-5)]{r},"")',
                "İlgili Kişi Risk Skoru":
                    '=IF(AND([Olasılık (1-5)]{r}<>"",[İlgili Kişiye Etki (1-5)]{r}<>""),'
                    '[Olasılık (1-5)]{r}*[İlgili Kişiye Etki (1-5)]{r},"")',
                "Genel Risk Seviyesi":
                    '=IF([Kuruluş Risk Skoru]{r}="","",'
                    'IF(OR(MAX([Kuruluş Risk Skoru]{r},[İlgili Kişi Risk Skoru]{r})>=15,'
                    'AND([Kırılgan Grup mu]{r}="Evet",[İlgili Kişi Risk Skoru]{r}>=8)),'
                    '"Yüksek",IF(MAX([Kuruluş Risk Skoru]{r},'
                    '[İlgili Kişi Risk Skoru]{r})>=8,"Orta","Düşük")))',
            },
            isi_haritasi=["Kuruluş Risk Skoru", "İlgili Kişi Risk Skoru"],
            durum_sutunu="Durum", bos_satir=50,
            notlar={"İlgili Kişiye Etki (1-5)": "Mahremiyet ihlali, ayrımcılık, maddi kayıp, "
                                                 "itibar zedelenmesi, veri üzerinde kontrol kaybı.",
                    "Genel Risk Seviyesi": "Otomatik: iki skorun yükseği; kırılgan grup önceliği yükseltir.",
                    "Kırılgan Grup mu": "Çocuk, hasta, engelli, çalışan (bağımlılık ilişkisi), sığınmacı vb."})
    k.ozet_sayfasi("Özet", "Risk Envanteri", "Genel Risk Seviyesi",
                   ["Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)


# --------------------------------------------------------------------- DPIA
def dpia(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Gizlilik Etki Değerlendirmesi (DPIA) Kayıtları",
               bilgi.get("kod_dpia", "KVYS-FR-03"))
    esik = ["Özel nitelikli kişisel veri işleniyor (KVKK m.6)",
            "Otomatik karar verme veya profilleme var",
            "Sistematik izleme (kamera, konum, aktivite izleme)",
            "Çocuklara ait veri işleniyor",
            "Büyük ölçekli işleme (eşik: [DOLDURULACAK])",
            "Yeni teknoloji kullanımı (biyometrik, YZ tabanlı analiz)",
            "Yeterlilik kararı bulunmayan ülkeye aktarım",
            "İki veya daha fazla veri setinin eşleştirilmesi"]
    k.bilgi_sayfasi(
        aciklama="Gizlilik etki değerlendirmesi kayıtları (2019: 7.2.5 / 2025: A.1.2.6).",
        kullanim_notu=("Eşik kriterlerinden en az biri karşılanıyorsa DPIA zorunludur "
                       "ve işleme BAŞLAMADAN ÖNCE tamamlanır. Kriter karşılanmıyorsa "
                       "gerekçe envantere yazılır — boş bırakılmaz."))
    k.sayfa("Eşik Kriterleri",
            ["Sıra", "Kriter", "Bu kuruluşta uygulanır mı", "Eşik/Tanım", "Not"],
            [[i + 1, e, "", "", ""] for i, e in enumerate(esik)],
            genislikler=[7, 56, 22, 30, 40],
            listeler={"Bu kuruluşta uygulanır mı": ["Evet", "Hayır"]},
            notlar={"Eşik/Tanım": "'Büyük ölçekli' gibi ifadeler sayısallaştırılmalı."})
    k.sayfa("DPIA Kayıtları",
            ["DPIA No", "İlgili Faaliyet No", "Faaliyet Adı", "Tetikleyen Kriter",
             "Değerlendirme Tarihi", "Değerlendiren", "İşlemenin Tanımı",
             "Gereklilik ve Ölçülülük Değerlendirmesi", "Etkilenen İlgili Kişi Grubu",
             "Tahmini Kişi Sayısı", "Tespit Edilen Riskler (Risk No)",
             "En Yüksek İlgili Kişi Etkisi", "Azaltıcı Önlemler", "Kalan Risk",
             "İlgili Kişi Görüşü Alındı mı", "Sonuç",
             "Kurul Görüşü Gerekli mi", "Onaylayan", "Onay Tarihi",
             "Sonraki Gözden Geçirme", "Durum"],
            [], genislikler=[11, 15, 30, 30, 16, 18, 44, 44, 26, 15, 22, 18, 44, 26,
                             20, 20, 20, 18, 14, 17, 12],
            listeler={"İlgili Kişi Görüşü Alındı mı": ["Evet", "Hayır", "Uygulanabilir değil"],
                      "Sonuç": ["Kabul edilebilir", "Ek önlemle kabul edilebilir",
                                 "Kabul edilemez — işleme yapılmayacak"],
                      "Kurul Görüşü Gerekli mi": ["Hayır", "Evet", "Değerlendirilecek"],
                      "Durum": ["Taslak", "Tamamlandı", "Gözden geçirilecek"]},
            durum_sutunu="Durum", bos_satir=30,
            notlar={"Gereklilik ve Ölçülülük Değerlendirmesi":
                    "Amaç daha az veriyle gerçekleşebilir mi? Alternatifler değerlendirildi mi?",
                    "Sonraki Gözden Geçirme":
                    "Amaç/veri/teknoloji değişiminde ve en geç iki yılda bir."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------- basvuru
def basvuru(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "İlgili Kişi Başvuru Kayıt Defteri",
               bilgi.get("kod_bsv", "KVYS-LS-06"))
    k.bilgi_sayfasi(
        aciklama="İlgili kişi (veri sahibi) taleplerinin kaydı. KVKK m.13: en geç 30 gün.",
        kullanim_notu=("'Kalan Gün' ve 'Süre Uyumu' otomatik hesaplanır. Süre aşımı "
                       "denetimde en somut bulgudur; 20. günde sorumluya, 25. günde "
                       "yöneticiye uyarı mekanizması kurulmalıdır."))
    k.sayfa("Başvurular",
            ["Başvuru No", "Geliş Tarihi", "Kanal", "Başvuran (ilgili kişi)",
             "Kimlik Doğrulama", "Vekâleten mi", "Talep Tipi",
             "İlgili Faaliyet No", "Talep Özeti", "Sorumlu",
             "Son Tarih (30 gün)", "Kalan Gün", "Yapılan İşlem",
             "Sonuç", "Ret Gerekçesi", "Ücret Talep Edildi mi",
             "Yanıt Tarihi", "Süre Uyumu", "Üçüncü Taraflara Bildirim",
             "Kurul'a Şikâyet Oldu mu", "Durum"],
            [], genislikler=[12, 13, 22, 24, 17, 13, 26, 15, 44, 18, 16, 12, 40,
                             16, 34, 18, 14, 14, 22, 20, 12],
            listeler={"Kanal": ["Yazılı (ıslak imza)", "KEP", "Güvenli elektronik imza",
                                 "Mobil imza", "Kayıtlı e-posta adresi", "Sistemde kayıtlı e-posta",
                                 "Başvuru formu (web)"],
                      "Kimlik Doğrulama": ["Yapıldı", "Ek bilgi istendi", "Yapılamadı"],
                      "Vekâleten mi": ["Hayır", "Evet"],
                      "Talep Tipi": ["Bilgi talebi (m.11/1-a)", "Erişim (m.11/1-b)",
                                      "Amaca uygun kullanım (m.11/1-c)",
                                      "Yurt içi/dışı aktarım bilgisi (m.11/1-ç)",
                                      "Düzeltme (m.11/1-d)", "Silme/yok etme (m.11/1-e)",
                                      "Üçüncü tarafa bildirim (m.11/1-f)",
                                      "Otomatik karara itiraz (m.11/1-g)",
                                      "Zararın giderilmesi (m.11/1-ğ)", "Rıza geri çekme"],
                      "Sonuç": ["Kabul", "Kısmen kabul", "Ret", "Konusuz kalma"],
                      "Ücret Talep Edildi mi": ["Hayır", "Evet"],
                      "Üçüncü Taraflara Bildirim": ["Gerekmedi", "Yapıldı", "Bekliyor"],
                      "Kurul'a Şikâyet Oldu mu": ["Hayır", "Evet"],
                      "Durum": ["Açık", "İşlemde", "Kapalı"]},
            formuller={
                "Son Tarih (30 gün)": '=IF([Geliş Tarihi]{r}="","",[Geliş Tarihi]{r}+30)',
                "Kalan Gün": '=IF(OR([Geliş Tarihi]{r}="",[Yanıt Tarihi]{r}<>""),"",'
                             '[Son Tarih (30 gün)]{r}-TODAY())',
                "Süre Uyumu": '=IF(OR([Yanıt Tarihi]{r}="",[Geliş Tarihi]{r}=""),"",'
                              'IF([Yanıt Tarihi]{r}<=[Son Tarih (30 gün)]{r},"Uygun","AŞILDI"))',
            },
            durum_sutunu="Durum", bos_satir=50,
            notlar={"Kalan Gün": "Bugüne göre otomatik. Negatifse süre aşılmış demektir.",
                    "Ret Gerekçesi": "Ret de yazılı ve gerekçeli olmalı; hukuki dayanak belirtilmeli.",
                    "Talep Tipi": "KVKK m.11 bentlerine göre; her bent ayrı iş akışı gerektirebilir."})
    k.ozet_sayfasi("Özet", "Başvurular", "Süre Uyumu", ["Uygun", "AŞILDI"])
    return k.kaydet(cikti)


# ---------------------------------------------------------------- saklama
def saklama(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Saklama ve İmha Tablosu", bilgi.get("kod_sak", "KVYS-LS-02"))
    k.bilgi_sayfasi(
        aciklama="Kişisel Veri Saklama ve İmha Politikası'nın veri tablosu.",
        kullanim_notu=("'Sürenin Başlangıcı' ve 'Saklama Dayanağı' boş bırakılamaz. "
                       "Yedeklerdeki kopyanın ne zaman düşeceği ayrı sütundadır — "
                       "silme talebi karşılandı denip yedekte kopya kalması en sık "
                       "gözden kaçan noktadır."))
    k.sayfa("Saklama ve İmha",
            ["Sıra", "Veri Kategorisi", "İlgili Faaliyet No", "Saklama Ortamı",
             "Saklama Süresi", "Birim", "Sürenin Başlangıcı (tetikleyici olay)",
             "Saklama Dayanağı (mevzuat/zamanaşımı/sözleşme)", "İmha Yöntemi",
             "Yedekten Düşme Süresi", "İmha Sorumlusu", "Periyodik İmha Dönemi",
             "Son İmha Tarihi", "Sonraki İmha Tarihi", "Not"],
            [], genislikler=[7, 30, 15, 24, 14, 12, 34, 44, 26, 20, 18, 20, 15, 16, 34],
            listeler={"Birim": ["Gün", "Ay", "Yıl"],
                      "İmha Yöntemi": ["Silme", "Yok etme", "Anonim hâle getirme"],
                      "Periyodik İmha Dönemi": ["3 ayda bir", "6 ayda bir", "Yıllık"],
                      "Saklama Ortamı": ["Elektronik (uygulama)", "Elektronik (dosya sunucu)",
                                          "Bulut", "Fiziksel arşiv", "Yedek ortam", "Karma"]},
            bos_satir=50,
            notlar={"Saklama Dayanağı": "Mevzuat maddesi numarasıyla. '10 yıl' tek başına "
                                         "savunulamaz; dayanağı yazılmalı.",
                    "Yedekten Düşme Süresi": "Yedek rotasyonu nedeniyle verinin yedekten "
                                              "ne kadar sürede tamamen çıkacağı.",
                    "Periyodik İmha Dönemi": "İmha Yönetmeliği periyodik imha öngörür; "
                                              "kuruluşun belirlediği periyot yazılır."})
    return k.kaydet(cikti)


# ---------------------------------------------------------------- aktarim
def aktarim(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yurt Dışı Aktarım Envanteri", bilgi.get("kod_akt", "KVYS-LS-04"))
    k.bilgi_sayfasi(
        aciklama="Yurt dışına kişisel veri aktarımlarının kaydı (KVKK m.9).",
        kullanim_notu=("Bulut hizmetleri en sık gözden kaçan aktarımdır: sunucu yurt "
                       "dışındaysa aktarım vardır. Kullanılan tüm SaaS/bulut "
                       "hizmetlerinin veri barındırma bölgesi sorgulanmalıdır."))
    k.sayfa("Yurt Dışı Aktarım",
            ["Aktarım No", "İlgili Faaliyet No", "Alıcı (unvan)", "Alıcı Ülke",
             "Alıcının Rolü", "Aktarılan Veri Kategorileri", "Özel Nitelikli Var mı",
             "Aktarım Amacı", "Aktarım Sıklığı", "Hukuki Dayanak (m.9)",
             "Dayanak Belgesi / Referansı", "Kurul Bildirim/İzin Durumu",
             "Aktarım Kanalı ve Güvenlik Önlemi", "Sözleşme Referansı",
             "Başlangıç Tarihi", "Gözden Geçirme Tarihi", "Durum"],
            [], genislikler=[11, 15, 26, 16, 18, 30, 17, 34, 16, 34, 30, 22, 34, 20,
                             16, 17, 12],
            listeler={"Alıcının Rolü": ["Veri sorumlusu", "Veri işleyen", "Alt yüklenici"],
                      "Özel Nitelikli Var mı": ["Yok", "Var"],
                      "Aktarım Sıklığı": ["Sürekli", "Periyodik", "Tek seferlik", "Talep üzerine"],
                      "Hukuki Dayanak (m.9)": ["Yeterlilik kararı bulunan ülke",
                                                "Standart sözleşme",
                                                "Bağlayıcı şirket kuralları",
                                                "Taahhütname (Kurul izinli)",
                                                "İstisnai hâl",
                                                "[DOLDURULACAK: teyit edilecek]"],
                      "Kurul Bildirim/İzin Durumu": ["Gerekmedi", "Bildirildi", "İzin alındı",
                                                      "Beklemede", "[DOLDURULACAK]"],
                      "Durum": ["Aktif", "Sonlandırıldı", "Planlanan"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Hukuki Dayanak (m.9)": "Dayanak türleri ve bildirim/izin gereklilikleri "
                                             "Kurul düzenlemelerine göre değişir — güncel "
                                             "durumu teyit ettirin.",
                    "Alıcı Ülke": "Bulut hizmetlerinde veri barındırma bölgesi yazılır."})
    return k.kaydet(cikti)


# ------------------------------------------------------------------- ihlal
def ihlal(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Veri İhlali Kayıt Defteri", bilgi.get("kod_ihl", "KVYS-LS-10"))
    k.bilgi_sayfasi(
        aciklama="Kişisel veri ihlallerinin kaydı (KVKK m.12/5).",
        kullanim_notu=("Süreler SAAT bazında izlenir — 72 saat gün üzerinden "
                       "hesaplanmaz. '72 Saat Uyumu' otomatik hesaplanır."))
    k.sayfa("İhlal Kayıtları",
            ["İhlal No", "Tespit Tarihi/Saati", "Öğrenme Tarihi/Saati", "Kaynak",
             "İhlal Tipi", "Ne Oldu (özet)", "Etkilenen Veri Kategorileri",
             "Özel Nitelikli Var mı", "Etkilenen Kişi Sayısı",
             "Etkilenen İlgili Kişi Grubu", "İlgili Faaliyet No", "Olası Sonuçlar",
             "Acil Müdahale", "Kurul'a Bildirim Gerekli mi", "Bildirim Karar Gerekçesi",
             "Kurul Bildirim Tarihi/Saati", "Geçen Saat", "72 Saat Uyumu",
             "İlgili Kişiye Bildirim", "Bildirim Yöntemi", "Kök Neden",
             "DÖF No", "Kapanış Tarihi", "Durum"],
            [], genislikler=[11, 18, 18, 22, 24, 44, 30, 17, 16, 26, 15, 34, 40, 22,
                             40, 20, 13, 15, 20, 22, 40, 12, 14, 12],
            listeler={"Kaynak": ["Çalışan bildirimi", "İzleme sistemi", "İlgili kişi şikâyeti",
                                  "Tedarikçi bildirimi", "Denetim", "Üçüncü taraf uyarısı"],
                      "İhlal Tipi": ["Gizlilik (yetkisiz erişim/ifşa)",
                                      "Bütünlük (yetkisiz değişiklik)",
                                      "Erişilebilirlik (kayıp/erişilemezlik)", "Karma"],
                      "Özel Nitelikli Var mı": ["Yok", "Var"],
                      "Kurul'a Bildirim Gerekli mi": ["Evet", "Hayır", "Değerlendiriliyor"],
                      "İlgili Kişiye Bildirim": ["Yapıldı", "Gerekmedi", "Bekliyor"],
                      "Durum": ["Açık", "İncelemede", "Kapalı"]},
            formuller={
                "Geçen Saat": '=IF(OR([Öğrenme Tarihi/Saati]{r}="",'
                              '[Kurul Bildirim Tarihi/Saati]{r}=""),"",'
                              'ROUND(([Kurul Bildirim Tarihi/Saati]{r}-'
                              '[Öğrenme Tarihi/Saati]{r})*24,1))',
                "72 Saat Uyumu": '=IF([Geçen Saat]{r}="","",'
                                 'IF([Geçen Saat]{r}<=72,"Uygun","AŞILDI"))',
            },
            durum_sutunu="72 Saat Uyumu", bos_satir=40,
            notlar={"Öğrenme Tarihi/Saati": "72 saatlik sürenin başlangıcı budur — tespit "
                                             "değil, ihlal olduğunun anlaşıldığı an.",
                    "Geçen Saat": "Otomatik. Tarih hücrelerini tarih-saat biçiminde girin.",
                    "Bildirim Karar Gerekçesi": "Bildirim yapılmadıysa NEDEN yapılmadığı "
                                                 "yazılmalı — karar kaydı denetlenir."})
    k.ozet_sayfasi("Özet", "İhlal Kayıtları", "72 Saat Uyumu", ["Uygun", "AŞILDI"])
    return k.kaydet(cikti)


# --------------------------------------------------------- diger kayitlar
def riza(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Açık Rıza Kayıt Defteri", bilgi.get("kod_riz", "KVYS-LS-05"))
    k.bilgi_sayfasi(
        aciklama="Açık rıza kayıtları (2019: 7.2.4 / 2025: A.1.2.5).",
        kullanim_notu=("Rıza, hukuki sebep olarak SON çaredir. Sözleşme ifası veya "
                       "kanuni yükümlülük varken rıza almak rızayı geçersiz kılar. "
                       "Her rıza kaydı geri çekilebilir olmalıdır."))
    k.sayfa("Rıza Kayıtları",
            ["Kayıt No", "İlgili Kişi (kimlik/ref)", "İlgili Faaliyet No", "Rıza Konusu",
             "Rıza Metni Sürümü", "Alınma Tarihi/Saati", "Alınma Kanalı",
             "Bilgilendirme Yapıldı mı", "Ayrı ve Özgür İrade Teyidi",
             "Geçerlilik Süresi", "Geri Çekildi mi", "Geri Çekilme Tarihi",
             "Geri Çekilme Sonrası İşlem", "Kanıt Referansı", "Durum"],
            [], genislikler=[11, 26, 15, 34, 18, 18, 22, 20, 24, 16, 15, 17, 34, 22, 12],
            listeler={"Alınma Kanalı": ["Web formu", "Mobil uygulama", "Islak imza",
                                         "Elektronik imza", "Çağrı merkezi (kayıtlı)", "Diğer"],
                      "Bilgilendirme Yapıldı mı": ["Evet", "Hayır"],
                      "Ayrı ve Özgür İrade Teyidi": ["Evet", "Hayır"],
                      "Geri Çekildi mi": ["Hayır", "Evet"],
                      "Durum": ["Geçerli", "Geri çekildi", "Süresi doldu"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Ayrı ve Özgür İrade Teyidi": "Rıza, aydınlatmayla veya hizmet şartıyla "
                                                   "aynı kutucuğa bağlanmışsa 'Hayır' işaretlenmeli "
                                                   "ve düzeltilmelidir."})
    return k.kaydet(cikti)


def ifsa(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "İfşa ve Paylaşım Kayıt Defteri", bilgi.get("kod_ifs", "KVYS-LS-07"))
    k.bilgi_sayfasi(aciklama="Üçüncü taraflara yapılan kişisel veri ifşalarının kaydı.")
    k.sayfa("İfşa Kayıtları",
            ["Kayıt No", "Tarih", "İlgili Faaliyet No", "İfşa Edilen Taraf",
             "Taraf Tipi", "İfşa Edilen Veri", "Etkilenen Kişi Sayısı", "İfşa Amacı",
             "Hukuki Dayanak", "Talep Eden Makam (varsa)", "Talep Belgesi Ref.",
             "Hukuki İnceleme Yapıldı mı", "Müşteriye/İlgili Kişiye Bildirim",
             "Bildirim Yapılmadıysa Gerekçe", "Sorumlu", "Durum"],
            [], genislikler=[11, 13, 15, 26, 20, 34, 16, 34, 30, 26, 20, 22, 26, 34, 18, 12],
            listeler={"Taraf Tipi": ["Kamu kurumu", "Kolluk", "Yargı", "Tedarikçi",
                                      "İş ortağı", "Denetim kuruluşu", "Diğer"],
                      "Hukuki İnceleme Yapıldı mı": ["Evet", "Hayır"],
                      "Müşteriye/İlgili Kişiye Bildirim": ["Yapıldı", "Yasal engel var",
                                                            "Gerekmedi", "Bekliyor"],
                      "Durum": ["Tamamlandı", "İşlemde"]},
            bos_satir=40,
            notlar={"Müşteriye/İlgili Kişiye Bildirim": "Veri işleyen rolündeyseniz yasal "
                                                         "talepleri müşteriye bildirmeniz "
                                                         "beklenir (yasal engel yoksa)."})
    return k.kaydet(cikti)


def altyuklenici(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Tedarikçi ve Alt Yüklenici Envanteri",
               bilgi.get("kod_alt", "KVYS-LS-09"))
    k.bilgi_sayfasi(
        aciklama="Veri işleyen ve alt yüklenici envanteri (2019: 8.5.6–8.5.8 / 2025: A.2.5.7–A.2.5.9).",
        kullanim_notu="Alt yüklenici değişikliğinin müşteriye ÖNCEDEN bildirimi zorunludur.")
    k.sayfa("Tedarikçi / Alt Yüklenici",
            ["Sıra", "Unvan", "Tip", "Sağlanan Hizmet", "İlgili Faaliyet No",
             "İşlenen Veri Kategorileri", "Özel Nitelikli Var mı", "Lokasyon / Ülke",
             "Yurt Dışı Aktarım Var mı", "Sözleşme No", "Veri İşleme Eki Var mı",
             "Gizlilik Taahhüdü", "Değerlendirme Tarihi", "Değerlendirme Sonucu",
             "Müşteri Onayı Alındı mı", "Değişiklik Bildirim Yükümlülüğü",
             "Denetim Hakkı", "Son Denetim", "Sözleşme Bitiş", "Çıkış/İmha Planı", "Durum"],
            [], genislikler=[7, 26, 18, 30, 15, 30, 17, 20, 20, 14, 20, 16, 16, 20,
                             20, 24, 15, 14, 14, 30, 12],
            listeler={"Tip": ["Veri işleyen", "Alt yüklenici", "Ortak veri sorumlusu",
                               "Bağımsız veri sorumlusu"],
                      "Özel Nitelikli Var mı": ["Yok", "Var"],
                      "Yurt Dışı Aktarım Var mı": ["Yok", "Var"],
                      "Veri İşleme Eki Var mı": ["Var", "Yok", "Hazırlanıyor"],
                      "Gizlilik Taahhüdü": ["Var", "Yok"],
                      "Değerlendirme Sonucu": ["Uygun", "Şartlı uygun", "Uygun değil"],
                      "Müşteri Onayı Alındı mı": ["Evet", "Hayır", "Gerekmedi"],
                      "Denetim Hakkı": ["Var", "Yok"],
                      "Durum": ["Aktif", "Değerlendirmede", "Sonlandırıldı"]},
            durum_sutunu="Durum", bos_satir=40)
    return k.kaydet(cikti)


def hedefler(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "KVYS Hedefleri ve İzleme Tablosu", bilgi.get("kod_hedef", "KVYS-FR-04"))
    k.bilgi_sayfasi(
        aciklama="Kişisel veri koruma hedefleri ve performans izleme.",
        kullanim_notu=("KVYS'ye özgü göstergeler: başvuru süre uyumu, ihlal sayısı ve "
                       "72 saat uyumu, envanter güncelliği, eğitim tamamlanma, "
                       "DPIA tamamlanma, saklama süresi aşımı."))
    k.sayfa("Hedefler",
            ["Hedef No", "Hedef", "Kategori", "Politika İlkesiyle İlişkisi",
             "Gösterge (KPI)", "Ölçüm Yöntemi", "Başlangıç Değeri", "Hedef Değer",
             "Ölçüm Sıklığı", "Sorumlu", "Kaynak", "Termin",
             "Q1", "Q2", "Q3", "Q4", "Yıl Sonu", "Değerlendirme", "Durum"],
            [], genislikler=[10, 38, 22, 24, 30, 26, 14, 12, 14, 18, 18, 12,
                             8, 8, 8, 8, 13, 34, 12],
            listeler={"Kategori": ["İlgili kişi hakları", "Veri minimizasyonu",
                                    "İhlal yönetimi", "Farkındalık", "Envanter kalitesi",
                                    "Saklama ve imha", "Tedarikçi yönetimi", "Uyum"],
                      "Ölçüm Sıklığı": ["Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Açık", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=20,
            notlar={"Gösterge (KPI)": "Örnek: 'ilgili kişi başvurularında 30 gün süre uyumu = %100'."})
    return k.kaydet(cikti)


def dof(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Uygunsuzluk ve Düzeltici Faaliyet Takip Formu",
               bilgi.get("kod_dof", "KVYS-FR-07"))
    k.bilgi_sayfasi(aciklama="Uygunsuzluk ve düzeltici faaliyet kayıtları.")
    k.sayfa("DÖF Takip",
            ["DÖF No", "Tespit Tarihi", "Kaynak", "Uygunsuzluk Tanımı",
             "İlgili Madde/Kontrol", "Sınıf", "Acil Düzeltme",
             "Kök Neden Analizi (yöntem + sonuç)", "Benzer Uygunsuzluk Taraması",
             "Düzeltici Faaliyet", "Sorumlu", "Termin", "Tamamlanma",
             "Etkinlik Doğrulama Yöntemi", "Doğrulama Tarihi", "Doğrulayan",
             "KVYS Değişikliği Gerekti mi", "Durum"],
            [], genislikler=[10, 13, 24, 44, 20, 12, 34, 44, 30, 44, 16, 12, 14,
                             34, 16, 16, 24, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "Veri ihlali",
                                  "İlgili kişi şikâyeti", "Kurul kararı/incelemesi",
                                  "DPIA sonucu", "İzleme/ölçme", "YGG", "Diğer"],
                      "Sınıf": ["Majör", "Minör", "Gözlem"],
                      "KVYS Değişikliği Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40)
    k.ozet_sayfasi("Özet", "DÖF Takip", "Durum", ["Açık", "Devam", "Kapalı"])
    return k.kaydet(cikti)


def yetkinlik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yetkinlik ve Eğitim Matrisi", bilgi.get("kod_yet", "KVYS-LS-12"))
    k.bilgi_sayfasi(aciklama="Yetkinlik ve farkındalık kayıtları.",
                    kullanim_notu="Kişisel veri yetkinliği hukuki + teknik + süreç boyutludur.")
    k.sayfa("Yetkinlik Matrisi",
            ["Sıra", "Rol / Unvan", "Kişi", "KVYS'deki Görevi",
             "Hukuki Yetkinlik (KVKK)", "Teknik Yetkinlik", "Süreç Yetkinliği",
             "Yetkinlik Kanıtı", "Mevcut Durum", "Boşluk", "Planlanan Eğitim",
             "Termin", "Tamamlanma", "Etkinlik Değerlendirmesi", "Sonraki Tazeleme"],
            [], genislikler=[7, 22, 20, 26, 24, 22, 22, 34, 14, 24, 28, 12, 14, 30, 16],
            listeler={x: ["Yeterli", "Kısmen", "Yetersiz", "Gerekli değil"] for x in
                      ["Hukuki Yetkinlik (KVKK)", "Teknik Yetkinlik", "Süreç Yetkinliği"]},
            bos_satir=40)
    k.sayfa("Farkındalık Kayıtları",
            ["Tarih", "Faaliyet", "Konu", "Hedef Kitle", "Katılımcı Sayısı",
             "Katılım Oranı", "Ölçüm Yöntemi", "Sonuç", "Sorumlu", "Kanıt Dosyası"],
            [], genislikler=[13, 26, 32, 22, 15, 14, 24, 24, 18, 26], bos_satir=30)
    return k.kaydet(cikti)


def dokuman_listesi(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Doküman Ana Listesi", bilgi.get("kod_dok", "KVYS-LS-13"))
    k.bilgi_sayfasi(aciklama="Dokümante bilgilerin kontrol listesi.")
    k.sayfa("İç Dokümanlar",
            ["Doküman No", "Doküman Adı", "Tip", "Revizyon", "Yayın Tarihi",
             "Son Revizyon", "Hazırlayan", "Onaylayan", "Dağıtım / Erişim",
             "Gizlilik", "Saklama Süresi", "Ortam", "İlgili Madde/Kontrol", "Durum"],
            [], genislikler=[13, 44, 10, 10, 13, 14, 18, 18, 24, 13, 14, 12, 24, 12],
            listeler={"Tip": ["El Kitabı", "Politika", "Prosedür", "Talimat", "Plan",
                              "Form", "Liste", "Rapor"],
                      "Gizlilik": ["Açık", "İç Kullanım", "Gizli"],
                      "Ortam": ["Elektronik", "Basılı", "Her ikisi"],
                      "Durum": ["Yürürlükte", "Taslak", "Yürürlükten kalktı"]},
            durum_sutunu="Durum", bos_satir=50)
    k.sayfa("Yayımlanan Metinler",
            ["Sıra", "Metin", "Hedef Grup", "Sürüm", "Yayım Tarihi", "Yayım Yeri",
             "Önceki Sürüm Arşivi", "Son Gözden Geçirme", "Sorumlu"],
            [["1", "Aydınlatma Metni — Çalışan", "Çalışan", "", "", "", "", "", ""],
             ["2", "Aydınlatma Metni — Çalışan Adayı", "Aday", "", "", "", "", "", ""],
             ["3", "Aydınlatma Metni — Müşteri", "Müşteri", "", "", "", "", "", ""],
             ["4", "Aydınlatma Metni — Ziyaretçi", "Ziyaretçi", "", "", "", "", "", ""],
             ["5", "Açık Rıza Metni", "Değişken", "", "", "", "", "", ""],
             ["6", "Çerez Aydınlatma Metni", "Web ziyaretçisi", "", "", "", "", "", ""]],
            genislikler=[7, 40, 22, 12, 14, 30, 24, 17, 18], bos_satir=15,
            notlar={"Önceki Sürüm Arşivi": "Bir ilgili kişiye hangi sürümün sunulduğunu "
                                            "kanıtlamak için eski sürümler saklanmalıdır."})
    return k.kaydet(cikti)


def zincir(bilgi: dict, cikti: str) -> str:
    """Envanter zincir kontrolu — denetcinin yapacagi testi onceden yapar."""
    k = _kayit(bilgi, "Envanter Zincir Kontrolü", bilgi.get("kod_zin", "KVYS-RP-03"))
    k.bilgi_sayfasi(
        aciklama=("Denetçi envanterden rastgele bir faaliyet seçip zinciri takip eder: "
                  "hukuki sebep → aydınlatma → saklama → aktarım → DPIA → SoA."),
        kullanim_notu="Altı halkanın tamamı 'Evet' olmalıdır.")
    k.sayfa("Zincir Kontrolü",
            ["Faaliyet No", "Faaliyet Adı", "Hukuki sebep yazılı mı",
             "Aydınlatma metni var mı", "Saklama süresi + dayanak var mı",
             "Aktarım envanterinde var mı (gerekiyorsa)", "DPIA yapıldı mı (gerekiyorsa)",
             "SoA'ya bağlı mı", "Zincir Durumu", "Eksik Halka", "Aksiyon", "Sorumlu"],
            [], genislikler=[11, 34, 20, 20, 24, 28, 24, 15, 14, 26, 40, 18],
            listeler={x: ["Evet", "Hayır", "Gerekmiyor"] for x in
                      ["Hukuki sebep yazılı mı", "Aydınlatma metni var mı",
                       "Saklama süresi + dayanak var mı",
                       "Aktarım envanterinde var mı (gerekiyorsa)",
                       "DPIA yapıldı mı (gerekiyorsa)", "SoA'ya bağlı mı"]},
            formuller={"Zincir Durumu":
                       '=IF(COUNTBLANK([Hukuki sebep yazılı mı]{r}:[SoA\'ya bağlı mı]{r})=6,"",'
                       'IF(COUNTIF([Hukuki sebep yazılı mı]{r}:[SoA\'ya bağlı mı]{r},"Hayır")=0,'
                       '"OK","EKSİK"))'},
            bos_satir=50)
    return k.kaydet(cikti)


def kvkk(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "KVKK Uyum Matrisi", bilgi.get("kod_kvkk", "KVYS-LS-03"))
    k.bilgi_sayfasi(
        aciklama=("27701 kontrolleri ile 6698 sayılı KVKK ve ikincil mevzuat "
                  "yükümlülüklerinin eşlemesi."),
        kullanim_notu=("27701 belgesi KVKK uyumunu garanti etmez; bu matris iki "
                       "çerçevenin kesişimini görünür kılar. Hukuki yorum gerektiren "
                       "satırlarda hukuk birimi görüşü alınmalıdır."))
    satirlar = [
        ["m.4", "Genel ilkeler (hukuka uygunluk, doğruluk, amaçla sınırlılık, ölçülülük, süre)", "", "", "", "", ""],
        ["m.5", "Kişisel verilerin işlenme şartları", "", "", "", "", ""],
        ["m.6", "Özel nitelikli kişisel verilerin işlenme şartları", "", "", "", "", ""],
        ["m.7", "Silme, yok etme, anonim hâle getirme", "", "", "", "", ""],
        ["m.8", "Yurt içi aktarım", "", "", "", "", ""],
        ["m.9", "Yurt dışına aktarım", "", "", "", "", ""],
        ["m.10", "Aydınlatma yükümlülüğü", "", "", "", "", ""],
        ["m.11", "İlgili kişinin hakları", "", "", "", "", ""],
        ["m.12", "Veri güvenliğine ilişkin yükümlülükler", "", "", "", "", ""],
        ["m.12/5", "Veri ihlali bildirimi (Kurul ve ilgili kişi)", "", "", "", "", ""],
        ["m.13", "İlgili kişinin başvurusu (30 gün)", "", "", "", "", ""],
        ["m.14", "Kurula şikâyet", "", "", "", "", ""],
        ["m.16", "Veri Sorumluları Sicili (VERBİS)", "", "", "", "", ""],
        ["m.28", "İstisnalar", "", "", "", "", ""],
        ["İkincil", "Aydınlatma Yükümlülüğünün Yerine Getirilmesi Tebliği", "", "", "", "", ""],
        ["İkincil", "Başvuru Usul ve Esasları Tebliği", "", "", "", "", ""],
        ["İkincil", "Silme, Yok Etme veya Anonim Hâle Getirme Yönetmeliği", "", "", "", "", ""],
        ["İkincil", "Veri Sorumluları Sicili Hakkında Yönetmelik", "", "", "", "", ""],
        ["Rehber", "Kurul Veri Güvenliği Rehberi", "", "", "", "", ""],
        ["Sektörel", "[DOLDURULACAK: tabi olunan sektörel düzenleme]", "", "", "", "", ""],
    ]
    k.sayfa("KVKK Uyum Matrisi",
            ["Mevzuat Referansı", "Yükümlülük", "İlgili 27701 Kontrolü",
             "Karşılayan Doküman", "Kanıt", "Uyum Durumu", "Boşluk / Aksiyon",
             "Sorumlu", "Termin", "Son Değerlendirme"],
            [s + ["", "", ""] for s in satirlar],
            genislikler=[18, 50, 26, 34, 40, 15, 40, 18, 12, 17],
            listeler={"Uyum Durumu": ["Uygun", "Kısmen", "Uygun değil", "Değerlendirilmedi"]},
            durum_sutunu="Uyum Durumu", bos_satir=20,
            notlar={"İlgili 27701 Kontrolü": "Sürüme göre doğru numaralandırmayı kullanın.",
                    "Yükümlülük": "İkincil mevzuatın güncel içeriği doğrulanmadan yazılmamalıdır."})
    k.sayfa("VERBİS Karşılaştırma",
            ["Sıra", "VERBİS Alanı", "Envanterdeki Karşılığı", "Tutarlı mı",
             "Fark Açıklaması", "Aksiyon", "Sorumlu", "Son Kontrol"],
            [[i + 1, a, b, "", "", "", "", ""] for i, (a, b) in enumerate([
                ("Veri kategorileri", "Veri Kategorileri"),
                ("Veri konusu kişi grubu", "İlgili Kişi Grubu"),
                ("Veri işleme amaçları", "İşleme Amacı"),
                ("Alıcı / alıcı grupları", "Aktarılan Taraflar"),
                ("Yabancı ülkelere aktarım", "Yurt Dışına Aktarım"),
                ("Azami saklama süresi", "Saklama Süresi"),
                ("Veri güvenliği tedbirleri", "Teknik ve İdari Tedbirler"),
            ])],
            genislikler=[7, 34, 34, 14, 40, 34, 18, 15],
            listeler={"Tutarlı mı": ["Evet", "Hayır", "Kısmen"]},
            notlar={"Tutarlı mı": "Envanter ile VERBİS bildirimi arasındaki çelişki hem "
                                   "27701 hem KVKK açısından bulgu üretir."})
    return k.kaydet(cikti)


def gecis(bilgi: dict, cikti: str) -> str:
    """2019 -> 2025 esleme ve bosluk analizi."""
    k27 = _kontroller()
    k = _kayit(bilgi, "2019 → 2025 Geçiş Boşluk Analizi",
               bilgi.get("kod_gec", "KVYS-RP-04"))
    k.bilgi_sayfasi(
        aciklama=("ISO/IEC 27701:2019'dan 2025'e geçiş için kontrol eşlemesi ve "
                  "boşluk analizi. Kontrollerin büyük kısmı yalnızca yeniden "
                  "numaralandırılır; asıl yeni iş A.3 ve bağımsız yönetim sistemi "
                  "gövdesidir."),
        kullanim_notu=("Geçiş son tarihini belgelendirme kuruluşunuzdan yazılı olarak "
                       "teyit edin — bu tablo tarih üretmez."))
    satirlar = []
    for c in k27["controller"]:
        satirlar.append(["Kontrol", "A." + c["v2019"], c["v2025"], "Veri sorumlusu",
                         c["baslik"], "", "", "", "", "Yalnız numara değişimi",
                         "", "", "", "", ""])
    for c in k27["processor"]:
        satirlar.append(["Kontrol", "B." + c["v2019"], c["v2025"], "Veri işleyen",
                         c["baslik"], "", "", "", "", "Yalnız numara değişimi",
                         "", "", "", "", ""])
    for c in k27["security"]:
        satirlar.append(["Kontrol", "— (Madde 6 / 27002)", c["v2025"],
                         f"Bilgi güvenliği (27002 {c['iso27002']})", c["baslik"],
                         "", "", "", "", "Yeni tablo — 27001 varsa kanıt eşlemesi",
                         "", "", "", "", ""])
    for m, konu in [("5.2.1", "Rol belirleme → 2025 Madde 4.1"),
                    ("5.2.2", "İlgili taraflar → 4.2"),
                    ("5.2.3", "Kapsam → 4.3 (bağımsız yazılır)"),
                    ("5.2.4", "Yönetim sistemi → 4.4"),
                    ("5.3.1", "Liderlik → 5.1"),
                    ("5.3.2", "Politika → 5.2 (ayrı politika gerekir)"),
                    ("5.3.3", "Roller → 5.3"),
                    ("5.4.1", "Risk ve fırsatlar → 6.1"),
                    ("5.4.2", "Hedefler → 6.2"),
                    ("5.5.x", "Destek → 7.1–7.5"),
                    ("5.6.x", "İşletim → 8"),
                    ("5.7.x", "Performans → 9.1–9.3"),
                    ("5.8.x", "İyileştirme → 10")]:
        satirlar.append(["Yönetim sistemi", m, konu.split("→")[1].strip(), "—", konu,
                         "", "", "", "", "Yeni — bağımsız madde kurulacak",
                         "", "", "", "", ""])
    k.sayfa("Geçiş Boşluk Analizi",
            ["Kategori", "2019 Referansı", "2025 Referansı", "Grup", "Konu",
             "Mevcut Doküman", "Mevcut Kanıt", "Durum", "Boşluk Açıklaması",
             "Yapılacak İş", "Efor (gün)", "Sorumlu", "Termin", "Tamamlanma", "Durum2"],
            satirlar,
            genislikler=[16, 20, 15, 30, 50, 30, 34, 16, 40, 34, 12, 16, 12, 14, 12],
            listeler={"Durum": ["Karşılanıyor", "Kısmen", "Yok", "Rol gereği uygulanmaz"],
                      "Yapılacak İş": ["Yalnız numara değişimi", "Revizyon",
                                        "Yeni üretim", "Yeni — bağımsız madde kurulacak",
                                        "Yeni tablo — 27001 varsa kanıt eşlemesi",
                                        "Aksiyon gerekmiyor"],
                      "Durum2": ["Açık", "Devam", "Tamamlandı"]},
            durum_sutunu="Durum2", bos_satir=15,
            notlar={"Yapılacak İş": "27001 belgesi olan kuruluşta tipik dağılım: "
                                     "~%60 yalnız numara, ~%25 revizyon, ~%15 yeni üretim.",
                    "2019 Referansı": "'—' işaretli satırlar 2025'te YENİ olan gerekliliklerdir."})
    k.ozet_sayfasi("Özet", "Geçiş Boşluk Analizi", "Yapılacak İş",
                   ["Yalnız numara değişimi", "Revizyon", "Yeni üretim",
                    "Yeni — bağımsız madde kurulacak",
                    "Yeni tablo — 27001 varsa kanıt eşlemesi"])
    return k.kaydet(cikti)


URETICILER = {
    "envanter": (envanter, "KVYS-LS-01 Kisisel Veri Isleme Envanteri.xlsx"),
    "soa": (soa, "KVYS-LS-11 Uygulanabilirlik Bildirgesi.xlsx"),
    "risk": (risk, "KVYS-FR-05 Kisisel Veri Risk Envanteri.xlsx"),
    "dpia": (dpia, "KVYS-FR-03 Gizlilik Etki Degerlendirmesi (DPIA).xlsx"),
    "basvuru": (basvuru, "KVYS-LS-06 Ilgili Kisi Basvuru Kayit Defteri.xlsx"),
    "saklama": (saklama, "KVYS-LS-02 Saklama ve Imha Tablosu.xlsx"),
    "aktarim": (aktarim, "KVYS-LS-04 Yurt Disi Aktarim Envanteri.xlsx"),
    "ihlal": (ihlal, "KVYS-LS-10 Veri Ihlali Kayit Defteri.xlsx"),
    "riza": (riza, "KVYS-LS-05 Acik Riza Kayit Defteri.xlsx"),
    "ifsa": (ifsa, "KVYS-LS-07 Ifsa ve Paylasim Kayit Defteri.xlsx"),
    "altyuklenici": (altyuklenici, "KVYS-LS-09 Tedarikci ve Alt Yuklenici Envanteri.xlsx"),
    "hedef": (hedefler, "KVYS-FR-04 KVYS Hedefleri.xlsx"),
    "dof": (dof, "KVYS-FR-07 DOF Takip Formu.xlsx"),
    "yetkinlik": (yetkinlik, "KVYS-LS-12 Yetkinlik ve Egitim Matrisi.xlsx"),
    "dokuman": (dokuman_listesi, "KVYS-LS-13 Dokuman Ana Listesi.xlsx"),
    "zincir": (zincir, "KVYS-RP-03 Envanter Zincir Kontrolu.xlsx"),
    "kvkk": (kvkk, "KVYS-LS-03 KVKK Uyum Matrisi.xlsx"),
    "gecis": (gecis, "KVYS-RP-04 Gecis Bosluk Analizi.xlsx"),
}

VARSAYILAN = ("envanter,soa,risk,dpia,basvuru,saklama,aktarim,ihlal,riza,ifsa,"
              "altyuklenici,hedef,dof,yetkinlik,dokuman,zincir,kvkk")


def main() -> None:
    ap = argparse.ArgumentParser(description="KVYS Excel kayitlarini uretir.")
    ap.add_argument("--kurulus", required=True)
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--surum", choices=["2019", "2025"], default="2025",
                    help="27701 surumu. SoA numaralandirmasini ve kontrol setini belirler.")
    ap.add_argument("--rol", choices=["sorumlu", "isleyen", "her-ikisi"],
                    default="her-ikisi", help="Kurulusun rolu.")
    ap.add_argument("--tarih", default="")
    ap.add_argument("--revizyon", default="00")
    ap.add_argument("--hazirlayan", default="")
    ap.add_argument("--onaylayan", default="")
    ap.add_argument("--hangi", default=VARSAYILAN,
                    help="Uretilecek kayitlar. Gecis analizi icin 'gecis' ekleyin.")
    a = ap.parse_args()

    bilgi = dict(kurulus=a.kurulus, tarih=a.tarih, revizyon=a.revizyon,
                 hazirlayan=a.hazirlayan, onaylayan=a.onaylayan,
                 surum=a.surum, rol=a.rol)
    os.makedirs(a.cikti, exist_ok=True)
    print(f"Sürüm: {a.surum} | Rol: {a.rol}")
    for ad in [x.strip() for x in a.hangi.split(",") if x.strip()]:
        if ad not in URETICILER:
            print(f"  ! bilinmeyen: {ad}")
            continue
        fn, dosya = URETICILER[ad]
        print(" ->", fn(bilgi, os.path.join(a.cikti, dosya)))


if __name__ == "__main__":
    main()
