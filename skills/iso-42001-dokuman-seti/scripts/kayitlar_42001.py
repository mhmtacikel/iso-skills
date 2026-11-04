#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_42001.py — YZYS'nin tekrar eden Excel kayitlarini uretir.

En degerli ucu: YZ sistem envanteri (iki zincirin de girdisi), Ek A kontrollerini
hazir iceren SoA, ve etki degerlendirmesi tablosu. Bu ucu elle kurulunca hem
yavas hem eksik cikar.

Kullanim:
    python3 kayitlar_42001.py --kurulus "ACME A.S." --cikti "/yol/03_Envanter" \\
        --tarih 2026-08-11 --hangi envanter,soa,risk,etki,veri,hedef,saglayici,\\
olay,endise,dof,zincir,dokuman,yetkinlik,politika,soru_bankasi,yasal,raci

Denetim hazirlik ucusu ayri uretilebilir:
    python3 kayitlar_42001.py --kurulus "ACME A.S." --cikti "/yol/07_Denetim_Hazirlik" \\
        --hangi soru_bankasi,yasal,raci

--hangi verilmezse TUM ureticiler calisir.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

BURASI = os.path.dirname(os.path.abspath(__file__))
ANNEX = os.path.join(BURASI, "..", "assets", "annex_a_42001.json")
SORULAR = os.path.join(BURASI, "..", "assets", "denetim_sorulari_42001.json")
STANDART = "TS ISO/IEC 42001 (ISO/IEC 42001:2023)"

# ISO/IEC 22989 rol taksonomisi. YZ suje ve ilgili otorite kurulus rolu degil,
# ilgili taraftir; bu nedenle listede yok (bkz. references/roller-ve-yetkinlik.md).
ROLLER = ["YZ sağlayıcı", "YZ üreticisi", "YZ müşterisi", "YZ ortağı",
          "YZ üreticisi + sağlayıcı", "YZ sağlayıcı + müşteri"]
OZERKLIK = ["Destekleyici (YZ önerir, insan karar verir)",
            "Tamamlayıcı (paylaşımlı kontrol, insan onaylar)",
            "Otonom (korkuluklarla otomatik hareket eder)"]
ASAMALAR = ["Fikir/İnceleme", "Tasarım", "Geliştirme", "Doğrulama/Geçerleme",
            "Devreye alma", "İşletim", "Emekliye ayırma"]
YAKLASIMLAR = ["Makine öğrenmesi", "Derin öğrenme", "Doğal dil işleme",
               "Bilgisayarlı görü", "Pekiştirmeli öğrenme",
               "Üretken YZ (büyük dil modeli)", "Üretken YZ (görüntü/ses)",
               "Kural / uzman sistemi", "Karma"]
CEVAP = ["E", "H", "U/D"]


def _kayit(bilgi: dict, ad: str, kod: str) -> YSKayit:
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=kod,
                   standart=STANDART, sistem="YZYS",
                   revizyon=bilgi.get("revizyon", "00"), tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""), onaylayan=bilgi.get("onaylayan", ""))


def _annex() -> list:
    with open(ANNEX, encoding="utf-8") as fh:
        return json.load(fh)


def _sorular() -> dict:
    with open(SORULAR, encoding="utf-8") as fh:
        return json.load(fh)


# ------------------------------------------------------------------ envanter
def envanter(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "YZ Sistem Envanteri", bilgi.get("kod_env", "YZYS-LS-04"))
    k.bilgi_sayfasi(
        aciklama=("YZYS'nin merkez kaydı. Hem risk değerlendirmesinin hem etki "
                  "değerlendirmesinin girdisidir; envanterdeki her sistemin iki "
                  "zincirde de karşılığı olmalıdır."),
        kullanim_notu=("'Kullanıcı Grubu' ile 'Etkilenen Kişi Grubu' AYRI sütunlardır. "
                       "İşe alım eleme modelinde kullanıcı İK uzmanı, etkilenen adaydır. "
                       "Bu ayrım yapılmazsa etki değerlendirmesi beslenemez."))
    k.sayfa("YZ Sistem Envanteri",
            ["Sistem No", "Sistem Adı", "Sağlayıcı", "Kuruluşun YZ Rolü",
             "Önemli Değişiklik Yapıldı mı?", "Model Tipi", "Teknik Yaklaşım",
             "Uygulama Alanı", "Amaçlanan Kullanım",
             "Öngörülebilir Amaç Dışı Kullanım", "Yasak Kullanım", "Kullanıcı Grubu",
             "Etkilenen Kişi Grubu", "Karar Özerkliği", "İşlenen Veri Tipleri",
             "Kişisel Veri", "Yaşam Döngüsü Aşaması", "Sistem Sahibi", "Teknik Sahip",
             "Kritiklik", "Risk Kaydı No", "Etki Değerlendirmesi No",
             "AB Bağlantısı", "AB YZ Yasası Rolü", "AB YZ Yasası Risk Seviyesi",
             "Yasal Uyum Matrisi Ref", "Devreye Alma Tarihi", "Son Gözden Geçirme",
             "Durum"],
            [], genislikler=[11, 30, 24, 22, 16, 20, 22, 22, 44, 40, 34, 24, 26, 30, 30,
                             16, 20, 18, 18, 12, 15, 20, 14, 20, 22, 18, 17, 16, 12],
            listeler={"Kuruluşun YZ Rolü": ROLLER, "Karar Özerkliği": OZERKLIK,
                      "Yaşam Döngüsü Aşaması": ASAMALAR,
                      "Teknik Yaklaşım": YAKLASIMLAR,
                      "Önemli Değişiklik Yapıldı mı?": ["Hayır", "Evet — ince ayar",
                                                        "Evet — amaç değişikliği",
                                                        "Evet — kendi markası altında"],
                      "Kişisel Veri": ["Yok", "Var", "Özel nitelikli var"],
                      "AB Bağlantısı": ["Yok", "Var — AB'de sunuluyor",
                                        "Var — AB'deki kişileri etkiliyor",
                                        "Belirlenmedi"],
                      "Kritiklik": ["Kritik", "Yüksek", "Orta", "Düşük"],
                      "Durum": ["Aktif", "Pilot", "Planlanan", "Emekli"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Kuruluşun YZ Rolü": "ISO/IEC 22989 taksonomisi. Yükümlülükler role "
                                          "göre değişir; aynı kuruluş farklı sistemlerde "
                                          "farklı rolde olabilir.",
                    "Önemli Değişiklik Yapıldı mı?": "Üçüncü taraf modelin ince ayarı, amaç "
                                                      "değişikliği veya kendi markası altında "
                                                      "sunulması rolü değiştirebilir ve hariç "
                                                      "tutulan kontrolleri geri getirebilir.",
                    "Öngörülebilir Amaç Dışı Kullanım": "A.5.3 gereği. 'Yasak kullanım'dan "
                                                         "farklıdır: yasaklanmamış ama beklenen sapma.",
                    "Yasak Kullanım": "A.9.4 gereği amaçlanan kullanımın tanımı, "
                                      "yasak kullanımın da tanımlanmasını gerektirir.",
                    "Karar Özerkliği": "Özerklik düzeyinin değişmesi, etki değerlendirmesinin "
                                       "yeniden yapılmasını gerektiren bir tetikleyicidir.",
                    "Etkilenen Kişi Grubu": "Sistemin kararına maruz kalanlar. "
                                             "Kullanıcıdan farklıdır ve etki değerlendirmesinin odağıdır.",
                    "AB YZ Yasası Rolü": "[DOLDURULACAK — hukuk birimince sınıflandırılacak] "
                                          "42001 rolüyle AYNI EKSEN DEĞİLDİR.",
                    "AB YZ Yasası Risk Seviyesi": "[DOLDURULACAK — hukuk birimince "
                                                   "sınıflandırılacak] Bu skill sınıflandırma yapmaz."})
    k.ozet_sayfasi("Özet", "YZ Sistem Envanteri", "Kritiklik",
                   ["Kritik", "Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- SoA
def soa(bilgi: dict, cikti: str, uygulanmayan: dict | None = None) -> str:
    uygulanmayan = uygulanmayan or {}
    basliklar = ["Kontrol No", "Kontrol Başlığı", "Uygulanabilir (E/H)",
                 "Dahil Etme Gerekçesi", "İlgili Risk / Etki No", "Uygulama Durumu",
                 "Uygulayan Doküman", "Sorumlu", "Doğrulama / Kanıt",
                 "Hariç Tutma Gerekçesi", "Son Gözden Geçirme"]
    satirlar = []
    for no, baslik, dokuman, kanit in _annex():
        haric = uygulanmayan.get(no)
        satirlar.append([f"A.{no}", baslik, "H" if haric else "E",
                         "" if haric else "Risk ve etki değerlendirmesi sonucu",
                         "", "" if haric else "Planlandı",
                         "" if haric else dokuman, "",
                         "" if haric else kanit, haric or "", bilgi.get("tarih", "")])
    k = _kayit(bilgi, "Uygulanabilirlik Bildirgesi (SoA)", bilgi.get("kod_soa", "YZYS-LS-01"))
    k.bilgi_sayfasi(
        aciklama=("ISO/IEC 42001 Madde 6.1.3 gereği Uygulanabilirlik Bildirgesi. "
                  "Ek A kontrollerinin tamamı listelenmiştir; hariç tutulanlar için "
                  "gerekçe zorunludur."),
        kullanim_notu=("Hariç tutma gerekçesi iki soruyu yanıtlamalı: neden uygulanabilir "
                       "değil, ve ilgili risk başka hangi kontrolle karşılanıyor. "
                       "Kuruluş yalnızca YZ kullanıcısıysa geliştirme kontrolleri (A.6) "
                       "hariç tutulabilir — ama gerekçesiyle."))
    k.sayfa("SoA", basliklar, satirlar,
            genislikler=[11, 44, 13, 34, 18, 15, 40, 16, 44, 40, 15],
            listeler={"Uygulanabilir (E/H)": ["E", "H"],
                      "Uygulama Durumu": ["Planlandı", "Uygulanıyor", "Uygulandı",
                                          "Kısmen", "Uygulanmıyor"]},
            durum_sutunu="Uygulama Durumu",
            notlar={"Hariç Tutma Gerekçesi": "Boş bırakılamaz — 'Uygulanabilir' H ise zorunludur."})
    k.ozet_sayfasi("Özet", "SoA", "Uygulama Durumu",
                   ["Planlandı", "Uygulanıyor", "Uygulandı", "Kısmen", "Uygulanmıyor"])
    return k.kaydet(cikti)


# ---------------------------------------------------------------------- risk
def risk(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "YZ Risk Envanteri ve Risk İşleme Planı",
               bilgi.get("kod_risk", "YZYS-FR-03"))
    k.bilgi_sayfasi(
        aciklama=("Madde 6.1.2, 6.1.3, 8.2 ve 8.3 kapsamındaki kayıt. Riskin KURULUŞA "
                  "etkisini değerlendirir — kişilere etkisi ayrı bir kayıttır "
                  "(YZYS-FR-04 Etki Değerlendirmesi)."),
        kullanim_notu="Yılda en az bir kez, model güncellemesi ve olay sonrası güncellenir.")
    k.sayfa("Risk Envanteri",
            ["Risk No", "İlgili Sistem No", "Risk Kategorisi", "Risk Tanımı",
             "Tetikleyici / Senaryo", "Mevcut Kontroller", "Olasılık (1-5)",
             "Etki (1-5)", "Risk Skoru", "Risk Seviyesi", "Risk Sahibi",
             "İşleme Seçeneği", "Planlanan Kontroller (Ek A)", "Sorumlu", "Termin",
             "Artık Olasılık", "Artık Etki", "Artık Risk", "Risk Sahibi Onayı",
             "Değerlendirme Tarihi", "Sonraki Gözden Geçirme", "Durum"],
            [], genislikler=[9, 15, 22, 44, 40, 30, 12, 11, 11, 13, 18, 14, 28, 16, 12,
                             13, 12, 11, 16, 15, 16, 11],
            listeler={"Risk Kategorisi": ["Model davranışı", "Veri", "Güvenlik",
                                           "Şeffaflık", "Bağımlılık", "Yönetişim",
                                           "Uyum", "Kaynak"],
                      "Olasılık (1-5)": [1, 2, 3, 4, 5], "Etki (1-5)": [1, 2, 3, 4, 5],
                      "Artık Olasılık": [1, 2, 3, 4, 5], "Artık Etki": [1, 2, 3, 4, 5],
                      "İşleme Seçeneği": ["Azalt", "Kabul et", "Aktar", "Kaçın"],
                      "Risk Sahibi Onayı": ["Onaylandı", "Beklemede"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            formuller={
                "Risk Skoru": '=IF(AND([Olasılık (1-5)]{r}<>"",[Etki (1-5)]{r}<>""),'
                              '[Olasılık (1-5)]{r}*[Etki (1-5)]{r},"")',
                "Risk Seviyesi": '=IF([Risk Skoru]{r}="","",IF([Risk Skoru]{r}>=15,"Yüksek",'
                                 'IF([Risk Skoru]{r}>=8,"Orta","Düşük")))',
                "Artık Risk": '=IF(AND([Artık Olasılık]{r}<>"",[Artık Etki]{r}<>""),'
                              '[Artık Olasılık]{r}*[Artık Etki]{r},"")'},
            isi_haritasi=["Risk Skoru", "Artık Risk"], durum_sutunu="Durum", bos_satir=50,
            notlar={"Risk Kategorisi": "Ek C potansiyel YZ risk kaynaklarını listeler.",
                    "Risk Tanımı": "Kuruluşa etki odaklı. Kişilere etki YZYS-FR-04'e yazılır."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- etki
def etki(bilgi: dict, cikti: str) -> str:
    """42001'in imzasi olan kayit. Risk envanteriyle KARISTIRILMAMALI."""
    k = _kayit(bilgi, "YZ Sistemi Etki Değerlendirmesi", bilgi.get("kod_etki", "YZYS-FR-04"))
    k.bilgi_sayfasi(
        aciklama=("Madde 6.1.4 ve 8.4 ile Ek A.5 kapsamındaki kayıt. YZ sisteminin "
                  "KİŞİLER, KİŞİ GRUPLARI ve TOPLUM üzerindeki potansiyel etkilerini "
                  "değerlendirir. Risk değerlendirmesinden ayrıdır: bir sistem kusursuz "
                  "çalışırken bile burada tespit edilen zararı üretebilir."),
        kullanim_notu=("Her YZ sistemi için ayrı yapılır. Tasarım aşamasında başlar, "
                       "yaşam döngüsü boyunca güncellenir. Tetikleyiciler: model "
                       "güncellemesi, yeni kullanım alanı, yeni kullanıcı grubu, olay, "
                       "mevzuat değişikliği, yıllık periyot."))
    k.sayfa("Etki Değerlendirmesi",
            ["Değerlendirme No", "İlgili Sistem No", "Sistem Adı", "Değerlendirme Tarihi",
             "Değerlendiren", "Etki Alanı", "Etkilenen Taraf", "Kırılgan Grup mu",
             "Potansiyel Olumsuz Etki", "Nasıl Ortaya Çıkar", "Şiddet (1-5)",
             "Olasılık (1-5)", "Etkilenen Kitle Büyüklüğü", "Tersine Çevrilebilir mi",
             "Etki Puanı", "Öncelik", "Azaltıcı Önlem", "Sorumlu", "Termin",
             "Kalan Etki", "Kabul Kararı", "Onaylayan", "İzleme Metriği",
             "İzleme Sıklığı", "Sonraki Gözden Geçirme", "Durum"],
            [], genislikler=[13, 15, 26, 16, 18, 22, 26, 15, 44, 40, 12, 13, 20, 18,
                             12, 12, 44, 18, 12, 30, 15, 18, 30, 15, 17, 12],
            listeler={"Etki Alanı": ["Adillik ve ayrımcılık", "Mahremiyet",
                                      "Güvenlik ve emniyet", "İnsan özerkliği",
                                      "Şeffaflık ve açıklanabilirlik", "Ekonomik etki",
                                      "Çevresel etki", "Bilgi bütünlüğü", "Toplumsal etki"],
                      "Kırılgan Grup mu": ["Evet", "Hayır"],
                      "Şiddet (1-5)": [1, 2, 3, 4, 5], "Olasılık (1-5)": [1, 2, 3, 4, 5],
                      "Etkilenen Kitle Büyüklüğü": ["Bireysel", "Küçük grup",
                                                     "Büyük grup", "Toplum geneli"],
                      "Tersine Çevrilebilir mi": ["Evet", "Kısmen", "Hayır"],
                      "Kabul Kararı": ["Kabul edildi", "Ek önlem gerekli", "Sistem durduruldu"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            formuller={"Etki Puanı":
                       '=IF(AND([Şiddet (1-5)]{r}<>"",[Olasılık (1-5)]{r}<>""),'
                       '[Şiddet (1-5)]{r}*[Olasılık (1-5)]{r},"")',
                       "Öncelik":
                       '=IF([Etki Puanı]{r}="","",IF(OR([Etki Puanı]{r}>=15,'
                       'AND([Tersine Çevrilebilir mi]{r}="Hayır",[Etki Puanı]{r}>=6),'
                       '[Kırılgan Grup mu]{r}="Evet"),"Yüksek",'
                       'IF([Etki Puanı]{r}>=8,"Orta","Düşük")))'},
            isi_haritasi=["Etki Puanı"], durum_sutunu="Durum", bos_satir=60,
            notlar={"Etkilenen Taraf": "Kullanıcı değil, kararın muhatabı olan kişi/grup.",
                    "Tersine Çevrilebilir mi": "Geri alınamayan zarar (haksız iş reddi, "
                                                "yanlış tıbbi tanı) düşük olasılıkta bile yüksek önceliklidir.",
                    "Öncelik": "Otomatik: tersine çevrilemezlik ve kırılgan grup varlığı "
                               "önceliği yükseltir.",
                    "İzleme Metriği": "Adillik metrikleri teknik performanstan AYRI izlenmelidir."})
    k.sayfa("İnsan Gözetimi",
            ["Sıra", "İlgili Sistem No", "Gözetim Rolü", "Gözeten Kişi/Birim",
             "Hangi Eşikte Devreye Girer", "Karara Müdahale Yetkisi",
             "İhtiyaç Duyulan Bilgi", "Müdahale Süresi", "Sistemi Durdurma Yetkisi",
             "Eğitim Durumu", "Müdahale Oranı (izleme)", "Son Gözden Geçirme"],
            [], genislikler=[7, 15, 24, 24, 40, 34, 34, 17, 22, 16, 22, 17],
            listeler={"Sistemi Durdurma Yetkisi": ["Var", "Yok", "Üst onayla"],
                      "Eğitim Durumu": ["Tamamlandı", "Planlandı", "Yok"]},
            bos_satir=25,
            notlar={"İhtiyaç Duyulan Bilgi": "Gözeten kişi çıktıyı sorgulayacak bilgiye "
                                              "sahip değilse gözetim biçimseldir — denetçi bunu sorar.",
                    "Müdahale Oranı (izleme)": "Hiç müdahale edilmeyen bir gözetim mekanizması "
                                                "çalışmıyor olabilir; oran izlenmelidir."})
    k.sayfa("Adillik Metrikleri",
            ["Sıra", "İlgili Sistem No", "Seçilen Metrik", "Seçim Gerekçesi",
             "Kabul Edilen Ödünleşim", "Karşılaştırılan Gruplar", "Ölçüm Yöntemi",
             "Hedef Eşik", "Son Ölçüm Değeri", "Ölçüm Tarihi", "Sonuç", "Aksiyon"],
            [], genislikler=[7, 15, 26, 40, 40, 30, 30, 14, 17, 14, 14, 34],
            listeler={"Seçilen Metrik": ["Demografik parite", "Eşit fırsat",
                                          "Eşitlenmiş olasılıklar", "Kalibrasyon", "Diğer"],
                      "Sonuç": ["Uygun", "Sapma var", "Ölçülmedi"]},
            durum_sutunu="Sonuç", bos_satir=25,
            notlar={"Seçim Gerekçesi": "Tek bir 'adil' metrik yoktur ve bazı tanımlar aynı "
                                        "anda sağlanamaz. Seçim bir değer yargısıdır; "
                                        "gerekçelendirmek gizlemekten güçlüdür.",
                    "Son Ölçüm Değeri": "UYDURULMAZ. Ölçümü kuruluş yapar."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- veri
def veri(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Veri Kaynakları ve Köken Envanteri", bilgi.get("kod_veri", "YZYS-LS-03"))
    k.bilgi_sayfasi(
        aciklama="Ek A.4.3, A.7.3, A.7.5 ve A.7.6 kapsamındaki kayıt.",
        kullanim_notu=("'Köken' ve 'Kullanım İzni / Lisans' sütunları A.7.5'in kanıtıdır. "
                       "Telifli, kazınmış veya belirsiz kaynaklı veri bu tabloda açığa çıkar."))
    k.sayfa("Veri Kaynakları",
            ["Veri Seti No", "Veri Seti Adı", "İlgili Sistem No", "Kullanım Amacı",
             "Kaynak Türü", "Köken (nereden, nasıl elde edildi)", "Kullanım İzni / Lisans",
             "Kişisel Veri", "Hukuki Dayanak", "Hacim", "Zaman Aralığı",
             "Temsil Edicilik Değerlendirmesi", "Bilinen Yanlılık",
             "Ön İşleme / Hazırlama Adımları", "Etiketleme Yöntemi", "Kalite Puanı",
             "Saklama Süresi", "Veri Sahibi", "Son Doğrulama", "Durum"],
            [], genislikler=[12, 30, 15, 30, 20, 44, 26, 16, 24, 14, 16, 34, 34, 40, 26,
                             13, 15, 18, 15, 12],
            listeler={"Kaynak Türü": ["Kurum içi üretim", "Müşteri verisi", "Satın alınan",
                                       "Açık kaynak / kamu", "Web'den toplanan", "Sentetik",
                                       "Üçüncü taraf sağlayıcı"],
                      "Kişisel Veri": ["Yok", "Var", "Özel nitelikli var"],
                      "Durum": ["Aktif", "Arşiv", "İmha edildi"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Köken (nereden, nasıl elde edildi)":
                    "A.7.5 veri kökenini ister: verinin nereden geldiği, hangi izinle "
                    "kullanıldığı, yaşam döngüsü boyunca nasıl izlendiği.",
                    "Bilinen Yanlılık": "Temsil eksikliği, tarihsel yanlılık, örnekleme "
                                         "yanlılığı — bilinmiyorsa 'değerlendirilmedi' yazın, boş bırakmayın."})
    k.sayfa("Veri Kalitesi (A.7.4)",
            ["Sıra", "Veri Seti No", "Kalite Boyutu", "Kriter", "Ölçüm Yöntemi",
             "Hedef", "Ölçülen Değer", "Ölçüm Tarihi", "Sonuç", "Aksiyon"],
            [[i + 1, "", b, "", "", "", "", "", "", ""] for i, b in enumerate([
                "Doğruluk", "Tamlık", "Tutarlılık", "Güncellik", "Temsil edicilik",
                "Dengelilik", "Etiket kalitesi", "Tekrarsızlık"])],
            genislikler=[7, 15, 22, 34, 30, 14, 15, 14, 14, 34],
            listeler={"Sonuç": ["Uygun", "Sapma var", "Ölçülmedi"]},
            durum_sutunu="Sonuç", bos_satir=20)
    return k.kaydet(cikti)


# ------------------------------------------------------------------- ortak set
def hedefler(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "YZ Hedefleri ve İzleme Tablosu", bilgi.get("kod_hedef", "YZYS-FR-02"))
    k.bilgi_sayfasi(
        aciklama="Madde 6.2 ve 9.1 kapsamındaki kayıt.",
        kullanim_notu=("YZ'ye özgü metrikler ayrılmalı: model performansı, ADİLLİK "
                       "metrikleri, model kayması, olay sayısı, insan müdahale oranı. "
                       "Sadece teknik performans izlemek 42001'in beklentisini karşılamaz."))
    k.sayfa("Hedefler",
            ["Hedef No", "YZ Hedefi", "Metrik Kategorisi", "İlgili Sistem No",
             "Politika İlkesiyle İlişkisi", "Gösterge (KPI)", "Ölçüm Yöntemi",
             "Başlangıç Değeri", "Hedef Değer", "Ölçüm Sıklığı", "Sorumlu",
             "Kaynak", "Termin", "Q1", "Q2", "Q3", "Q4", "Yıl Sonu",
             "Değerlendirme", "Durum"],
            [], genislikler=[10, 38, 20, 15, 24, 26, 26, 14, 12, 14, 18, 18, 12,
                             8, 8, 8, 8, 13, 34, 12],
            listeler={"Metrik Kategorisi": ["Model performansı", "Adillik", "Şeffaflık",
                                             "Güvenlik", "Model kayması", "Olay/Şikâyet",
                                             "İnsan gözetimi", "Yönetişim", "Çevresel"],
                      "Ölçüm Sıklığı": ["Sürekli", "Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Açık", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=25)
    return k.kaydet(cikti)


def saglayici(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Üçüncü Taraf ve Model Sağlayıcı Envanteri",
               bilgi.get("kod_sag", "YZYS-LS-06"))
    k.bilgi_sayfasi(aciklama="Ek A.10.2–A.10.4 kapsamındaki kayıt.",
                    kullanim_notu="Yaşam döngüsü boyunca sorumluluk paylaşımı açıkça "
                                  "tanımlanmalıdır (A.10.2).")
    k.sayfa("Sağlayıcılar",
            ["Sıra", "Sağlayıcı", "Sağlanan YZ Bileşeni", "İlgili Sistem No",
             "Sözleşme No", "Sorumluluk Paylaşımı (A.10.2)", "Sağlayıcının Beyanları",
             "Model Kartı / Teknik Doküman Var mı", "Veri Kullanım Şartları",
             "Sürüm Değişikliği Bildirimi", "Değerlendirme Tarihi",
             "Değerlendirme Sonucu", "Çıkış Stratejisi", "Sorumlu", "Durum"],
            [], genislikler=[7, 26, 30, 15, 14, 44, 34, 24, 34, 26, 16, 20, 34, 18, 12],
            listeler={"Model Kartı / Teknik Doküman Var mı": ["Var", "Kısmen", "Yok"],
                      "Değerlendirme Sonucu": ["Uygun", "Şartlı uygun", "Uygun değil"],
                      "Durum": ["Aktif", "Değerlendirmede", "Sonlandırıldı"]},
            durum_sutunu="Durum", bos_satir=25,
            notlar={"Çıkış Stratejisi": "Sağlayıcı hizmeti sonlandırırsa veya modeli "
                                         "değiştirirse ne olacak? Bağımlılık riski buradan yönetilir."})
    return k.kaydet(cikti)


def olay(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "YZ Olay Kayıt Defteri", bilgi.get("kod_olay", "YZYS-FR-12"))
    k.bilgi_sayfasi(aciklama="Ek A.8.4 kapsamındaki kayıt.",
                    kullanim_notu="Kök neden katmanı (veri/model/süreç/insan/ortam) "
                                  "ayrımı YZ olaylarında ayırt edicidir.")
    k.sayfa("YZ Olayları",
            ["Olay No", "Tarih", "İlgili Sistem No", "Olay Tipi", "Bildiren",
             "Olay Tanımı", "Etkilenen Taraf", "Etki Şiddeti", "Acil Müdahale",
             "Kök Neden Katmanı", "Kök Neden Analizi", "Kalıcı Çözüm",
             "Kullanıcılara Bildirim (A.8.4)", "Dış Bildirim Gerekti mi",
             "İlgili DÖF No", "Etki Değerlendirmesi Güncellendi mi",
             "Kapanış Tarihi", "Durum"],
            [], genislikler=[10, 13, 15, 24, 20, 44, 26, 14, 34, 20, 44, 40, 30, 20,
                             14, 26, 14, 12],
            listeler={"Olay Tipi": ["Hatalı çıktı", "Yanlılık tespiti", "Halüsinasyon",
                                     "Veri sızıntısı", "Güvenlik ihlali", "Model kayması",
                                     "Amaç dışı kullanım", "Erişilebilirlik", "Diğer"],
                      "Etki Şiddeti": ["Kritik", "Yüksek", "Orta", "Düşük"],
                      "Kök Neden Katmanı": ["Veri", "Model", "Süreç", "İnsan", "Ortam", "Karma"],
                      "Dış Bildirim Gerekti mi": ["Evet", "Hayır"],
                      "Etki Değerlendirmesi Güncellendi mi": ["Evet", "Hayır", "Gerekmedi"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40)
    return k.kaydet(cikti)


def endise(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Endişe Bildirim Kayıt Formu", bilgi.get("kod_end", "YZYS-FR-13"))
    k.bilgi_sayfasi(
        aciklama="Ek A.3.3 gereği: çalışanların YZ sistemleriyle ilgili endişelerini "
                 "bildirebileceği mekanizmanın kaydı.",
        kullanim_notu=("Bildirim kanalı misilleme korkusu olmadan kullanılabilmelidir. "
                       "Gizlilik seçeneği ve geri bildirim süresi tanımlı olmalı."))
    k.sayfa("Endişe Bildirimleri",
            ["Bildirim No", "Tarih", "Kanal", "Gizlilik Talebi", "İlgili Sistem No",
             "Endişe Konusu", "Endişe Tanımı", "İlk Değerlendirme", "Sorumlu",
             "İncelemenin Sonucu", "Alınan Aksiyon", "Bildirene Geri Dönüş Tarihi",
             "İlgili DÖF / Etki Değerlendirmesi", "Kapanış", "Durum"],
            [], genislikler=[12, 13, 20, 16, 15, 24, 50, 34, 18, 40, 40, 20, 30, 14, 12],
            listeler={"Kanal": ["Yüz yüze", "E-posta", "Anonim form", "Yönetici", "Etik hattı"],
                      "Gizlilik Talebi": ["Evet", "Hayır"],
                      "Endişe Konusu": ["Adillik", "Mahremiyet", "Güvenlik", "Şeffaflık",
                                         "Amaç dışı kullanım", "Veri kalitesi", "Diğer"],
                      "Durum": ["Açık", "İncelemede", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=25)
    return k.kaydet(cikti)


def dof(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Uygunsuzluk ve Düzeltici Faaliyet Takip Formu",
               bilgi.get("kod_dof", "YZYS-FR-05"))
    k.bilgi_sayfasi(aciklama="Madde 10.2 kapsamındaki kayıt.")
    k.sayfa("DÖF Takip",
            ["DÖF No", "Tespit Tarihi", "Kaynak", "Uygunsuzluk Tanımı", "İlgili Madde",
             "Sınıf", "Acil Düzeltme", "Kök Neden Katmanı",
             "Kök Neden Analizi (yöntem + sonuç)", "Benzer Uygunsuzluk Taraması",
             "Düzeltici Faaliyet", "Sorumlu", "Termin", "Tamamlanma",
             "Etkinlik Doğrulama Yöntemi", "Doğrulama Tarihi", "Doğrulayan",
             "YZYS Değişikliği Gerekti mi", "Durum"],
            [], genislikler=[10, 13, 22, 44, 14, 12, 34, 20, 44, 30, 44, 16, 12, 14,
                             34, 16, 16, 24, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "YZ olayı", "Endişe bildirimi",
                                  "Etki değerlendirmesi", "İzleme/ölçme", "YGG", "Diğer"],
                      "Sınıf": ["Majör", "Minör", "Gözlem"],
                      "Kök Neden Katmanı": ["Veri", "Model", "Süreç", "İnsan", "Ortam", "Karma"],
                      "YZYS Değişikliği Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40)
    k.ozet_sayfasi("Özet", "DÖF Takip", "Durum", ["Açık", "Devam", "Kapalı"])
    return k.kaydet(cikti)


def zincir(bilgi: dict, cikti: str) -> str:
    """42001'e ozgu cift zincir kontrolu: her sistem hem risk hem etki zincirinde olmali."""
    k = _kayit(bilgi, "Çift Zincir Kontrolü", bilgi.get("kod_zin", "YZYS-FR-15"))
    k.bilgi_sayfasi(
        aciklama=("Envanterdeki her YZ sisteminin HEM risk HEM etki zincirinde "
                  "karşılığı olmalıdır. Denetçi envanterden bir sistem seçip iki "
                  "zinciri de takip eder."),
        kullanim_notu="Her iki zincir de OK olmalıdır.")
    k.sayfa("Çift Zincir",
            ["Sistem No", "Sistem Adı", "Envanterde var mı",
             "Risk kaydı var mı", "Risk işleme kararı var mı", "SoA'ya bağlı mı",
             "Risk Zinciri",
             "Etki değerlendirmesi var mı", "Azaltıcı önlem tanımlı mı",
             "İzleme metriği var mı", "Şeffaflık taahhüdü var mı", "Etki Zinciri",
             "Eksik Halka", "Aksiyon"],
            [], genislikler=[11, 30, 16, 15, 20, 15, 14, 22, 22, 18, 20, 14, 26, 40],
            listeler={x: ["Evet", "Hayır", "Kısmen"] for x in
                      ["Envanterde var mı", "Risk kaydı var mı", "Risk işleme kararı var mı",
                       "SoA'ya bağlı mı", "Etki değerlendirmesi var mı",
                       "Azaltıcı önlem tanımlı mı", "İzleme metriği var mı",
                       "Şeffaflık taahhüdü var mı"]},
            formuller={
                "Risk Zinciri": '=IF(COUNTIF([Envanterde var mı]{r}:[SoA\'ya bağlı mı]{r},'
                                '"Evet")=4,"OK",IF(COUNTBLANK([Envanterde var mı]{r}:'
                                '[SoA\'ya bağlı mı]{r})=4,"","EKSİK"))',
                "Etki Zinciri": '=IF(COUNTIF([Etki değerlendirmesi var mı]{r}:'
                                '[Şeffaflık taahhüdü var mı]{r},"Evet")=4,"OK",'
                                'IF(COUNTBLANK([Etki değerlendirmesi var mı]{r}:'
                                '[Şeffaflık taahhüdü var mı]{r})=4,"","EKSİK"))'},
            bos_satir=40)
    return k.kaydet(cikti)


def politika_uyum(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Politika Uyum Matrisi", bilgi.get("kod_pol", "YZYS-LS-08"))
    k.bilgi_sayfasi(
        aciklama="Ek A.2.3 gereği YZ politikasının diğer kurumsal politikalarla uyumu.",
        kullanim_notu="Çelişki tespit edilirse hangi politikanın güncelleneceği karara bağlanır.")
    k.sayfa("Politika Uyumu",
            ["Sıra", "İlgili Kurumsal Politika", "Sahibi", "Kesişim Konusu",
             "YZ Politikasındaki İlke", "Diğer Politikadaki Hüküm", "Uyum Durumu",
             "Çelişki Açıklaması", "Karar", "Sorumlu", "Termin", "Durum"],
            [["1", "Bilgi Güvenliği Politikası", "", "", "", "", "", "", "", "", "", ""],
             ["2", "Kişisel Verilerin Korunması Politikası", "", "", "", "", "", "", "", "", "", ""],
             ["3", "Etik Kurallar / Davranış Kuralları", "", "", "", "", "", "", "", "", "", ""],
             ["4", "Kalite Politikası", "", "", "", "", "", "", "", "", "", ""],
             ["5", "Satın Alma / Tedarikçi Politikası", "", "", "", "", "", "", "", "", "", ""],
             ["6", "İnsan Kaynakları Politikası", "", "", "", "", "", "", "", "", "", ""]],
            genislikler=[7, 34, 18, 30, 40, 40, 14, 40, 30, 18, 12, 12],
            listeler={"Uyum Durumu": ["Uyumlu", "Çelişki var", "Boşluk var", "Değerlendirilmedi"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=15)
    return k.kaydet(cikti)


def dokuman_listesi(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Doküman Ana Listesi", bilgi.get("kod_dok", "YZYS-LS-09"))
    k.bilgi_sayfasi(aciklama="Madde 7.5.3 gereği dokümante bilgilerin kontrol listesi.")
    k.sayfa("İç Dokümanlar",
            ["Doküman No", "Doküman Adı", "Tip", "Revizyon", "Yayın Tarihi",
             "Son Revizyon", "Hazırlayan", "Onaylayan", "Dağıtım / Erişim",
             "Gizlilik", "Saklama Süresi", "Ortam", "İlgili Madde", "Durum"],
            [], genislikler=[13, 44, 10, 10, 13, 14, 18, 18, 24, 13, 14, 12, 20, 12],
            listeler={"Tip": ["El Kitabı", "Politika", "Prosedür", "Plan", "Form", "Liste", "Rapor"],
                      "Gizlilik": ["Açık", "İç Kullanım", "Gizli"],
                      "Ortam": ["Elektronik", "Basılı", "Her ikisi"],
                      "Durum": ["Yürürlükte", "Taslak", "Yürürlükten kalktı"]},
            durum_sutunu="Durum", bos_satir=50)
    return k.kaydet(cikti)


def yetkinlik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yetkinlik ve Eğitim Matrisi", bilgi.get("kod_yet", "YZYS-LS-07"))
    k.bilgi_sayfasi(
        aciklama="Madde 7.2, 7.3 ve Ek A.4.6 kapsamındaki kayıt.",
        kullanim_notu=("YZ yetkinliği yalnızca teknik değildir. Etki değerlendirmesi "
                       "yapacak kişinin etik, hukuk ve alan bilgisine de ihtiyacı vardır."))
    k.sayfa("Yetkinlik Matrisi",
            ["Sıra", "Rol / Unvan", "Kişi", "YZYS'deki Görevi", "Teknik Yetkinlik",
             "Etik Yetkinlik", "Hukuki Yetkinlik", "Alan Bilgisi", "Yetkinlik Kanıtı",
             "Mevcut Durum", "Boşluk", "Planlanan Eğitim", "Termin", "Tamamlanma",
             "Etkinlik Değerlendirmesi", "Sonraki Tazeleme"],
            [], genislikler=[7, 22, 20, 26, 26, 22, 22, 22, 34, 14, 24, 28, 12, 14, 30, 16],
            listeler={x: ["Yeterli", "Kısmen", "Yetersiz", "Gerekli değil"] for x in
                      ["Teknik Yetkinlik", "Etik Yetkinlik", "Hukuki Yetkinlik", "Alan Bilgisi"]},
            bos_satir=40)
    return k.kaydet(cikti)


# ------------------------------------------------------- denetim soru bankasi
def soru_bankasi(bilgi: dict, cikti: str) -> str:
    """Belgelendirme kuruluşu kontrol listesinden türetilmiş denetçi soru bankası.

    İki işi birden görür: iç tetkik soru listesi (9.2) ve belgelendirme öncesi
    öz değerlendirme. 'Kanıt' sütunu sahada istenecek kanıt tipini gösterir.
    """
    veri = _sorular()
    basliklar = ["Sıra", "Tip", "Ref", "Başlık", "Denetçi Sorusu", "Cevap (E/H/U-D)",
                 "İlgili Doküman", "Kanıt Yeri / Dosya", "Sorumlu", "Bulgu / Not",
                 "Aksiyon Gerekli mi?", "Termin", "Durum"]
    satirlar = []
    sira = 0
    for b in veri["bolumler"]:
        tip = "Madde" if b["tip"] == "madde" else "Kontrol"
        for soru in b["sorular"]:
            sira += 1
            satirlar.append([sira, tip, b["ref"], b["baslik"], soru, "", "", "", "",
                             "", "", "", "Açık"])
        # Her bölümün sonuna kanıt hatırlatma satırı
        sira += 1
        satirlar.append([sira, tip, b["ref"], b["baslik"],
                         f"KANIT — sahada istenecekler: {b['kanit']}",
                         "", "", "", "", "", "", "", "Açık"])

    k = _kayit(bilgi, "Denetim Soru Bankası ve Öz Değerlendirme",
               bilgi.get("kod_soru", "YZYS-FR-14"))
    k.bilgi_sayfasi(
        aciklama=("Belgelendirme kuruluşu tetkik kontrol listesinden uyarlanmış "
                  f"{sum(len(b['sorular']) for b in veri['bolumler'])} denetçi sorusu. "
                  "Madde 4-10 ve Ek A kontrollerinin tamamını kapsar. Hem iç tetkik "
                  "soru listesi (9.2) hem belgelendirme öncesi öz değerlendirme "
                  "olarak kullanılır."),
        kullanim_notu=("'U/D' yalnızca Ek A kontrolleri için kullanılabilir — Madde 4-10 "
                       "hariç tutulamaz. 'H' işaretlenen her satır bir açık demektir ve "
                       "OKUBENI.md'ye taşınmalıdır. Referans doküman girilmemiş bölüm, "
                       "karşılığı henüz üretilmemiş gereklilik demektir."))
    k.sayfa("Soru Bankası", basliklar, satirlar,
            genislikler=[6, 9, 10, 34, 96, 14, 30, 30, 16, 44, 14, 12, 12],
            listeler={"Cevap (E/H/U-D)": CEVAP,
                      "Aksiyon Gerekli mi?": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum",
            notlar={"Cevap (E/H/U-D)": "U/D (uygulanabilir değil) yalnızca Ek A "
                                        "kontrolleri için geçerlidir; Madde 4-10 hariç tutulamaz.",
                    "Kanıt Yeri / Dosya": "Dokümanın adı yetmez — kanıtın hangi dosyada, "
                                           "hangi bölümde olduğunu yaz."})
    k.ozet_sayfasi("Özet", "Soru Bankası", "Cevap (E/H/U-D)", CEVAP)
    return k.kaydet(cikti)


# ------------------------------------------------------- yasal uyum matrisi
def yasal_uyum(bilgi: dict, cikti: str) -> str:
    """YZYS-LS-10 Yasal Uyum ve Yükümlülük Matrisi.

    42001 yasal uyumu garanti etmez; bu matris yasal yükümlülükleri 42001
    dokümanlarından AYRI izler. Her satır hukuk birimince doğrulanmalıdır.
    """
    k = _kayit(bilgi, "Yasal Uyum ve Yükümlülük Matrisi",
               bilgi.get("kod_yasal", "YZYS-LS-10"))
    k.bilgi_sayfasi(
        aciklama=("Tabi olunan mevzuattan doğan yükümlülüklerin, ilgili YZ sistemleri "
                  "ve 42001 dokümanlarıyla eşlendiği matris. Madde 4.1/4.2 ve Ek A.2.3 "
                  "ile bağlanır."),
        kullanim_notu=("BU BİR HUKUKİ GÖRÜŞ DEĞİLDİR. Her satırın hukuk birimince "
                       "doğrulanması gerekir; 'Doğrulayan (Hukuk)' sütunu boş "
                       "bırakılamaz. Madde/fıkra numarası içeren her atıf "
                       "[teyit-madde] etiketlidir ve birincil kaynaktan doğrulanmadan "
                       "kullanılamaz. Bu matriste uydurma madde numarası, uydurma "
                       "yürürlük tarihi, 'uyumludur' beyanı ve ceza tutarı bulunamaz."))
    k.sayfa("Yasal Uyum Matrisi",
            ["Sıra", "Düzenleme / Mevzuat", "Dayanak (madde/karar)", "Kaynak Etiketi",
             "İlgili YZ Sistemi", "Yükümlülük Özeti", "İlgili 42001 Maddesi/Kontrolü",
             "Bunu Karşılayan Doküman", "Mevcut Durum", "Boşluk Tanımı", "Sorumlu",
             "Termin", "Doğrulayan (Hukuk)", "Doğrulama Tarihi", "Durum"],
            [], genislikler=[6, 30, 26, 16, 24, 54, 26, 32, 18, 44, 16, 12, 20, 15, 12],
            listeler={"Kaynak Etiketi": ["[yerleşik]", "[teyit]", "[teyit-madde]"],
                      "Mevcut Durum": ["Karşılanıyor", "Kısmen", "Karşılanmıyor",
                                       "Uygulanabilir değil", "Belirlenmedi"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Kaynak Etiketi": "[yerleşik] uzun süredir yürürlükte · [teyit] "
                                       "güncelliği doğrulanmalı · [teyit-madde] madde "
                                       "numarası içeriyor, birincil kaynaktan doğrulanmalı.",
                    "Doğrulayan (Hukuk)": "BOŞ BIRAKILAMAZ. Doğrulanmamış satır, "
                                           "karşılandığı iddia edilemeyen satırdır.",
                    "Mevcut Durum": "'Karşılanıyor' işareti hukuk doğrulaması olmadan "
                                     "konulamaz."})
    k.ozet_sayfasi("Özet", "Yasal Uyum Matrisi", "Mevcut Durum",
                   ["Karşılanıyor", "Kısmen", "Karşılanmıyor", "Uygulanabilir değil",
                    "Belirlenmedi"])
    return k.kaydet(cikti)


# --------------------------------------------------------------- RACI matrisi
RACI_FAALIYETLER = [
    ("YZ politikasının geliştirilmesi ve gözden geçirilmesi", "5.2, A.2.2, A.2.4"),
    ("YZ risk değerlendirmesi ve risk işleme", "6.1.2, 6.1.3, 8.2, 8.3"),
    ("YZ sistemi etki değerlendirmesi", "6.1.4, 8.4, A.5.2-A.5.5"),
    ("YZ sistem envanterinin sürdürülmesi", "4.3, 8.1"),
    ("Veri yönetişimi ve veri kalitesi", "A.7.2-A.7.6"),
    ("Veri kökeni kaydı", "A.7.5"),
    ("Sorumlu tasarım ve geliştirme", "A.6.1.3, A.6.2.2, A.6.2.3"),
    ("Doğrulama ve geçerleme (TEVV), yanlılık testi", "A.6.2.4"),
    ("Devreye alma ve geri alma", "A.6.2.5, 6.3"),
    ("İşletim, izleme, kayma ve adillik takibi", "A.6.2.6, 9.1"),
    ("Olay günlüklerinin tasarımı ve korunması", "A.6.2.8"),
    ("Teknik dokümantasyon / model kartı", "A.6.2.7"),
    ("İnsan gözetiminin tasarımı ve etkinliğinin izlenmesi", "A.9.3, A.5.4"),
    ("Şeffaflık, harici raporlama ve olay bildirimi", "A.8.3, A.8.4, A.8.5"),
    ("Endişe bildirimlerinin alınması ve eskalasyonu", "A.3.3"),
    ("Tedarikçi ve model sağlayıcı yönetimi", "A.10.2, A.10.3"),
    ("Müşteri bilgilendirmesi", "A.10.4"),
    ("Yetkinlik yönetimi ve farkındalık", "7.2, 7.3, A.4.6"),
    ("Yasal uyum matrisinin sürdürülmesi", "4.1, 4.2, A.2.3"),
    ("İç tetkik", "9.2"),
    ("Yönetimin gözden geçirmesi", "9.3"),
    ("Uygunsuzluk ve düzeltici faaliyet", "10.2"),
    ("Sürekli iyileştirme", "10.1"),
]


def raci(bilgi: dict, cikti: str) -> str:
    """YZYS rol ve sorumluluk (RACI) matrisi — A.3.2 kanıtı.

    A.3.2 rol ve sorumlulukların on alanı birden kapsamasını ister. Bu matris
    her faaliyet icin tam olarak bir 'A' bulunmasini zorunlu kilar.
    """
    roller = ["Üst Yönetim Sponsoru", "YZ Yönetişim ve Uyum Sorumlusu",
              "YZ Etik Sorumlusu", "Hukuk ve Politika Danışmanı", "Veri Sahibi",
              "Veri Bilimci / ML Mühendisi", "YZ Mühendisi", "MLOps / İşletim",
              "Siber Güvenlik ve Mahremiyet", "Tedarik Sorumlusu",
              "İç Tetkikçi", "İK / Eğitim"]
    basliklar = ["Sıra", "Faaliyet", "İlgili Madde/Kontrol"] + roller + ["Not"]
    satirlar = [[i, ad, ref] + [""] * len(roller) + [""]
                for i, (ad, ref) in enumerate(RACI_FAALIYETLER, start=1)]

    k = _kayit(bilgi, "YZYS Rol ve Sorumluluk (RACI) Matrisi",
               bilgi.get("kod_raci", "YZYS-LS-11"))
    k.bilgi_sayfasi(
        aciklama=("Madde 5.3 ve Ek A.3.2 kapsamındaki rol ve sorumluluk kaydı. "
                  "A.3.2 rol tanımlarının şu on alanı kapsamasını ister: risk yönetimi, "
                  "mahremiyet, güvenlik, emniyet, YZ sistemi etki değerlendirmesi, "
                  "performans, insan gözetimi, tedarikçi ilişkileri, uyum, veri "
                  "kalitesi yönetimi."),
        kullanim_notu=("R = yürüten · A = hesap veren · C = danışılan · I = bilgilendirilen. "
                       "HER SATIRDA TAM OLARAK BİR 'A' BULUNMALIDIR — birden fazla 'A' "
                       "sorumluluk boşluğu demektir, sıfır 'A' sahipsiz faaliyet demektir. "
                       "Rol sütunlarını kuruluşun gerçek unvanlarıyla değiştirin; küçük "
                       "kuruluşta bir kişi birden çok rolü üstlenebilir, sorun bu değildir — "
                       "sorun bir alanın isimsiz kalmasıdır. İç tetkikçi, tetkik ettiği "
                       "faaliyette 'R' veya 'A' olamaz (9.2 bağımsızlık)."))
    k.sayfa("RACI", basliklar, satirlar,
            genislikler=[6, 52, 24] + [18] * len(roller) + [40],
            listeler={r: ["R", "A", "C", "I", "-"] for r in roller})
    return k.kaydet(cikti)


URETICILER = {
    "envanter": (envanter, "YZYS-LS-04 YZ Sistem Envanteri.xlsx"),
    "soa": (soa, "YZYS-LS-01 Uygulanabilirlik Bildirgesi.xlsx"),
    "risk": (risk, "YZYS-FR-03 YZ Risk Envanteri.xlsx"),
    "etki": (etki, "YZYS-FR-04 YZ Sistemi Etki Degerlendirmesi.xlsx"),
    "veri": (veri, "YZYS-LS-03 Veri Kaynaklari ve Koken Envanteri.xlsx"),
    "hedef": (hedefler, "YZYS-FR-02 YZ Hedefleri ve Izleme.xlsx"),
    "saglayici": (saglayici, "YZYS-LS-06 Ucuncu Taraf ve Model Saglayici Envanteri.xlsx"),
    "olay": (olay, "YZYS-FR-12 YZ Olay Kayit Defteri.xlsx"),
    "endise": (endise, "YZYS-FR-13 Endise Bildirim Kayit Formu.xlsx"),
    "dof": (dof, "YZYS-FR-05 DOF Takip Formu.xlsx"),
    "zincir": (zincir, "YZYS-FR-15 Cift Zincir Kontrolu.xlsx"),
    "politika": (politika_uyum, "YZYS-LS-08 Politika Uyum Matrisi.xlsx"),
    "dokuman": (dokuman_listesi, "YZYS-LS-09 Dokuman Ana Listesi.xlsx"),
    "yetkinlik": (yetkinlik, "YZYS-LS-07 Yetkinlik ve Egitim Matrisi.xlsx"),
    "soru_bankasi": (soru_bankasi, "Denetim-Soru-Bankasi.xlsx"),
    "yasal": (yasal_uyum, "YZYS-LS-10 Yasal Uyum ve Yukumluluk Matrisi.xlsx"),
    "raci": (raci, "YZYS-LS-11 Rol ve Sorumluluk RACI Matrisi.xlsx"),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="YZYS Excel kayitlarini uretir.")
    ap.add_argument("--kurulus", required=True)
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--tarih", default="")
    ap.add_argument("--revizyon", default="00")
    ap.add_argument("--hazirlayan", default="")
    ap.add_argument("--onaylayan", default="")
    ap.add_argument("--hangi", default=",".join(URETICILER))
    a = ap.parse_args()
    bilgi = dict(kurulus=a.kurulus, tarih=a.tarih, revizyon=a.revizyon,
                 hazirlayan=a.hazirlayan, onaylayan=a.onaylayan)
    os.makedirs(a.cikti, exist_ok=True)
    for ad in [x.strip() for x in a.hangi.split(",") if x.strip()]:
        if ad not in URETICILER:
            print(f"  ! bilinmeyen: {ad}"); continue
        fn, dosya = URETICILER[ad]
        print(" ->", fn(bilgi, os.path.join(a.cikti, dosya)))


if __name__ == "__main__":
    main()
