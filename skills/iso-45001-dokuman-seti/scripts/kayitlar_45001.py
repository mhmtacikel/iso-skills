#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_45001.py — İSG Yönetim Sistemi'nin tekrar eden Excel kayıtlarını üretir.

Neden var: risk değerlendirme tablosu, yasal şartlar listesi, periyodik kontrol
planı, olay istatistiği gibi kayıtlar her kurulumda aynı iskeleti taşır ve elle
kurulduğunda en sık hata buralarda çıkar (elle yazılmış risk seviyesi, #VALUE!
formülü, 106'ya toplanan ağırlıklar, mülga mevzuat). Bu script iskeleti formülleri
ve açılır listeleriyle kurar; kuruluşa özgü satırları sen doldurursun.

Kullanım:
    python3 kayitlar_45001.py --kurulus "ÖRNEK GIDA A.Ş." --cikti "<klasör>" \\
        --tarih 2026-10-02 --hazirlayan "İş Güvenliği Uzmanı" --onaylayan "Genel Müdür" \\
        [--yontem l-matris|fine-kinney] [--tehlike-sinifi "çok tehlikeli"] \\
        [--onek İSGYS] [--hangi risk,yasal,...] [--sade]

Varsayılan kod öneki "İSGYS" (iso-*-dokuman-seti ailesi: [SİSTEM]-[TİP]-[SIRA]; PN=plan, LS=liste). Kuruluşun kendi kodlama kuralı varsa
--kodlar ile JSON verip kodları ezebilirsin: --kodlar '{"risk":"1000-11-FR-022"}'

Örnek satırlar "ÖRNEK —" ile başlar; kuruluş doğrulamadan gerçek kayıt sayılmaz.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

STANDART = "TS EN ISO 45001:2018 (+ Amd 1:2024)"

# anahtar: (tür, sıra, ad) — tip kodları aile standardıdır (PN plan, LS liste, FR form)  — references/dokuman-listesi.md ile aynı tutulmalı
KAYITLAR = {
    "risk":       ("LS", "01", "Tehlike Belirleme ve Risk Değerlendirme Tablosu"),
    "riskfirsat": ("LS", "02", "İSG Yönetim Sistemi Risk ve Fırsat Listesi"),
    "baglam":     ("LS", "03", "İç-Dış Hususlar ve İlgili Taraflar Listesi"),
    "yasal":      ("LS", "04", "Yasal ve Diğer Şartlar Listesi ve Uygunluk Değerlendirmesi"),
    "hedef":      ("PN", "05", "İSG Hedefleri ve Programı"),
    "periyodik":  ("PN", "04", "İzleme, Ölçme ve Periyodik Kontrol Planı"),
    "egitim":     ("PN", "03", "Yıllık Eğitim Planı ve Eğitim Matrisi"),
    "kkd":        ("LS", "05", "KKD Standart Listesi (Bölüm-KKD Matrisi)"),
    "olay":       ("LS", "06", "Olay, Kaza ve Ramak Kala Kayıt ve İstatistik Tablosu"),
    "dof":        ("LS", "07", "Uygunsuzluk ve Düzeltici Faaliyet Takip Listesi"),
    "tetkik":     ("PN", "06", "İç Tetkik Programı"),
    "dokuman":    ("LS", "08", "Doküman Ana Listesi"),
    "degisiklik": ("LS", "09", "Değişiklik Yönetimi Kayıt Listesi"),
    "yuklenici":  ("LS", "10", "Yüklenici ve Tedarikçi İSG Değerlendirme Listesi"),
    "katilim":    ("LS", "11", "Çalışan Danışma ve Katılım Kayıt Listesi"),
    "acil":       ("LS", "12", "Acil Durum Ekipleri ve Tatbikat Takip Listesi"),
    "kimyasal":   ("LS", "13", "Tehlikeli Kimyasallar Envanteri"),
    "ekipman":    ("LS", "14", "Periyodik Kontrole Tabi İş Ekipmanları Envanteri"),
}

# Sade sette birleştirilen kayıtlar başka bir dosyanın sayfası olur.
SADE_DISI = {"katilim", "degisiklik", "kimyasal", "ekipman"}


def _kod(bilgi, anahtar):
    ozel = bilgi.get("kodlar", {})
    if anahtar in ozel:
        return ozel[anahtar]
    tur, sira, _ = KAYITLAR[anahtar]
    return f"{bilgi.get('onek', 'İSGYS')}-{tur}-{sira}"


def _kayit(bilgi, anahtar):
    _, _, ad = KAYITLAR[anahtar]
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=_kod(bilgi, anahtar),
                   standart=STANDART, sistem="İSG Yönetim Sistemi",
                   revizyon=bilgi.get("revizyon", "00"), tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""), onaylayan=bilgi.get("onaylayan", ""))


def _dosya(bilgi, anahtar, cikti):
    return os.path.join(cikti, f"{_kod(bilgi, anahtar)} {KAYITLAR[anahtar][2]}.xlsx")


EVET_HAYIR = ["Evet", "Hayır"]
DURUM = ["Açık", "Devam", "Kapalı", "Gecikti"]
HIYERARSI = ["1-Ortadan kaldırma", "2-İkame", "3-Mühendislik kontrolü",
             "4-İdari kontrol / eğitim", "5-KKD"]
MARUZ = ["Çalışan", "Yüklenici", "Ziyaretçi", "Özel politika grubu", "Çevre/Komşu"]

# ---------------------------------------------------------------- risk
L_SEVIYE = ('=IF([{s}]{{r}}="","",IF([{s}]{{r}}>=25,"Tolere Edilemez",IF([{s}]{{r}}>=15,"Önemli",'
            'IF([{s}]{{r}}>=8,"Orta",IF([{s}]{{r}}>=2,"Kabul Edilebilir","Önemsiz")))))')
FK_SEVIYE = ('=IF([{s}]{{r}}="","",IF([{s}]{{r}}>400,"Tolere Edilemez",IF([{s}]{{r}}>200,"Esaslı",'
             'IF([{s}]{{r}}>70,"Önemli",IF([{s}]{{r}}>20,"Olası","Katlanılabilir")))))')


def risk(bilgi, yol):
    k = _kayit(bilgi, "risk")
    fk = bilgi.get("yontem") == "fine-kinney"
    sinif = bilgi.get("tehlike_sinifi", "[DOLDURULACAK]")
    yenileme = {"çok tehlikeli": "2 yıl", "tehlikeli": "4 yıl", "az tehlikeli": "6 yıl"}.get(
        sinif.lower(), "tehlike sınıfına göre (2/4/6 yıl)")
    k.bilgi_sayfasi(
        aciklama=("ISO 45001 Madde 6.1.2, 8.1.2 ve 6331 sayılı Kanun m.10 ile İSG Risk "
                  "Değerlendirmesi Yönetmeliği kapsamındaki tehlike belirleme ve risk "
                  f"değerlendirme kaydı. Yöntem: {'Fine-Kinney (O×F×Ş)' if fk else '5×5 L tipi matris (O×Ş)'}."),
        kullanim_notu=(f"İşyeri tehlike sınıfı: {sinif}. Yasal yenileme periyodu: en geç {yenileme}; "
                       "ayrıca iş kazası, meslek hastalığı, ramak kala, yeni makine/kimyasal/proses, "
                       "yerleşim değişikliği ve mevzuat değişikliğinde güncellenir. Risk seviyesi "
                       "sütunu formüldür — elle yazma; yöntem değişirse yalnız eşikler değişir."))
    if fk:
        bas = ["Sıra No", "Bölüm / Süreç", "Faaliyet", "Rutin / Rutin Dışı", "Tehlike",
               "Risk (olası zarar)", "Maruz Kalanlar", "Mevcut Önlemler",
               "Olasılık", "Frekans", "Şiddet", "Risk Skoru", "Risk Seviyesi",
               "İlgili Yasal Şart", "Kontrol Hiyerarşisi", "Alınacak Ek Önlemler", "Sorumlu",
               "Termin", "Kalan Olasılık", "Kalan Frekans", "Kalan Şiddet", "Kalan Skor",
               "Kalan Seviye", "Durum"]
        formul = {"Risk Skoru": '=IF(AND([Olasılık]{r}<>"",[Frekans]{r}<>"",[Şiddet]{r}<>""),[Olasılık]{r}*[Frekans]{r}*[Şiddet]{r},"")',
                  "Risk Seviyesi": FK_SEVIYE.format(s="Risk Skoru"),
                  "Kalan Skor": '=IF(AND([Kalan Olasılık]{r}<>"",[Kalan Frekans]{r}<>"",[Kalan Şiddet]{r}<>""),[Kalan Olasılık]{r}*[Kalan Frekans]{r}*[Kalan Şiddet]{r},"")',
                  "Kalan Seviye": FK_SEVIYE.format(s="Kalan Skor")}
        liste = {"Olasılık": [0.2, 0.5, 1, 3, 6, 10], "Frekans": [0.5, 1, 2, 3, 6, 10],
                 "Şiddet": [1, 3, 7, 15, 40, 100], "Kalan Olasılık": [0.2, 0.5, 1, 3, 6, 10],
                 "Kalan Frekans": [0.5, 1, 2, 3, 6, 10], "Kalan Şiddet": [1, 3, 7, 15, 40, 100]}
    else:
        bas = ["Sıra No", "Bölüm / Süreç", "Faaliyet", "Rutin / Rutin Dışı", "Tehlike",
               "Risk (olası zarar)", "Maruz Kalanlar", "Mevcut Önlemler",
               "Olasılık", "Şiddet", "Risk Skoru", "Risk Seviyesi",
               "İlgili Yasal Şart", "Kontrol Hiyerarşisi", "Alınacak Ek Önlemler", "Sorumlu",
               "Termin", "Kalan Olasılık", "Kalan Şiddet", "Kalan Skor", "Kalan Seviye", "Durum"]
        formul = {"Risk Skoru": '=IF(AND([Olasılık]{r}<>"",[Şiddet]{r}<>""),[Olasılık]{r}*[Şiddet]{r},"")',
                  "Risk Seviyesi": L_SEVIYE.format(s="Risk Skoru"),
                  "Kalan Skor": '=IF(AND([Kalan Olasılık]{r}<>"",[Kalan Şiddet]{r}<>""),[Kalan Olasılık]{r}*[Kalan Şiddet]{r},"")',
                  "Kalan Seviye": L_SEVIYE.format(s="Kalan Skor")}
        liste = {"Olasılık": [1, 2, 3, 4, 5], "Şiddet": [1, 2, 3, 4, 5],
                 "Kalan Olasılık": [1, 2, 3, 4, 5], "Kalan Şiddet": [1, 2, 3, 4, 5]}
    liste.update({"Rutin / Rutin Dışı": ["Rutin", "Rutin dışı", "Acil durum"],
                  "Kontrol Hiyerarşisi": HIYERARSI, "Durum": DURUM})
    ornek = [["1", "ÖRNEK — Üretim / Dolum hattı", "Bant temizliği", "Rutin",
              "Hareketli makine aksamı", "El/parmak sıkışması, uzuv kaybı", "Çalışan",
              "Sabit koruyucu, acil stop"] + ([""] * (len(bas) - 8))]
    k.sayfa("Risk Değerlendirme", bas, ornek, listeler=liste, formuller=formul,
            isi_haritasi=["Risk Skoru", "Kalan Skor"], durum_sutunu="Durum", bos_satir=80,
            notlar={"Kontrol Hiyerarşisi": "ISO 45001 8.1.2: önce ortadan kaldırma, en son KKD. "
                    "KKD tek önlemse gerekçesini Ek Önlemler sütununa yaz.",
                    "Maruz Kalanlar": "Gebe/emziren, genç, engelli, yaşlı, yabancı uyruklu, "
                    "kronik hastalığı olan çalışanlar 'Özel politika grubu'dur (RD Yön. m.6)."})
    if fk:
        k.sayfa("Yöntem", ["Parametre", "Değer", "Tanım"], [
            ["Olasılık", 0.2, "Pratik olarak imkânsız"], ["Olasılık", 0.5, "Zayıf ihtimal"],
            ["Olasılık", 1, "Oldukça düşük ihtimal"], ["Olasılık", 3, "Nadir fakat olabilir"],
            ["Olasılık", 6, "Kuvvetle muhtemel"], ["Olasılık", 10, "Çok kuvvetli ihtimal"],
            ["Frekans", 0.5, "Çok seyrek (yılda bir veya daha az)"], ["Frekans", 1, "Oldukça seyrek (yılda birkaç)"],
            ["Frekans", 2, "Seyrek (ayda bir)"], ["Frekans", 3, "Ara sıra (haftada bir)"],
            ["Frekans", 6, "Sıklıkla (günde bir)"], ["Frekans", 10, "Hemen hemen sürekli"],
            ["Şiddet", 1, "Hasarsız / ilk yardım"], ["Şiddet", 3, "Küçük hasar, iş günü kaybı yok"],
            ["Şiddet", 7, "Önemli hasar, iş günü kaybı"], ["Şiddet", 15, "Ciddi yaralanma, uzuv kaybı"],
            ["Şiddet", 40, "Ölüm"], ["Şiddet", 100, "Birden fazla ölüm"],
            ["Seviye", "<=20", "Katlanılabilir — ek önlem gerekmez, izlenir"],
            ["Seviye", "21-70", "Olası — 1 yıl içinde önlem"],
            ["Seviye", "71-200", "Önemli — kısa dönemde (≤3 ay) önlem"],
            ["Seviye", "201-400", "Esaslı — kısa sürede (≤1 ay) önlem"],
            ["Seviye", ">400", "Tolere edilemez — iş durdurulur"]], genislikler=[14, 10, 60])
    else:
        k.sayfa("Yöntem", ["Parametre", "Değer", "Tanım"], [
            ["Olasılık", 1, "Çok küçük — hemen hemen hiç (yılda bir veya daha seyrek)"],
            ["Olasılık", 2, "Küçük — çok az (yılda birkaç kez)"],
            ["Olasılık", 3, "Orta — az (ayda bir)"], ["Olasılık", 4, "Yüksek — sıklıkla (haftada bir)"],
            ["Olasılık", 5, "Çok yüksek — her zaman (her gün)"],
            ["Şiddet", 1, "Çok hafif — iş saati kaybı yok, ilk yardım"],
            ["Şiddet", 2, "Hafif — iş günü kaybı yok, ayakta tedavi"],
            ["Şiddet", 3, "Orta — hafif yaralanma, yataklı tedavi, iş günü kaybı"],
            ["Şiddet", 4, "Ciddi — ciddi yaralanma, uzuv kaybı, meslek hastalığı"],
            ["Şiddet", 5, "Çok ciddi — ölüm, sürekli iş göremezlik"],
            ["Seviye", "1", "Önemsiz — ek önlem gerekmez"],
            ["Seviye", "2-6", "Kabul edilebilir — mevcut önlemler izlenir, uzun vadede iyileştirilir"],
            ["Seviye", "8-12", "Orta — önlem planlanır (≤3 ay)"],
            ["Seviye", "15-20", "Önemli — önlem alınmadan işe başlanmaz / kısa sürede (≤1 ay)"],
            ["Seviye", "25", "Tolere edilemez — iş derhal durdurulur"]], genislikler=[14, 10, 70])
    k.ozet_sayfasi("Özet", "Risk Değerlendirme", "Risk Seviyesi",
                   ["Tolere Edilemez", "Esaslı", "Önemli", "Orta", "Olası",
                    "Kabul Edilebilir", "Katlanılabilir", "Önemsiz"])
    return k.kaydet(yol)


def riskfirsat(bilgi, yol):
    k = _kayit(bilgi, "riskfirsat")
    k.bilgi_sayfasi(
        aciklama=("Madde 6.1.1 ve 6.1.2.3: İSG yönetim sisteminin kendisine yönelik riskler "
                  "(ör. yetkin İSG profesyoneli kaybı, yüklenici yoğunluğu, mevzuat değişikliği) ve "
                  "İSG fırsatları (ör. otomasyonla elle taşımanın kaldırılması). Tehlike kaynaklı "
                  "İSG riskleri bu listede değil, Risk Değerlendirme Tablosu'ndadır."),
        kullanim_notu="Girdi: İç-Dış Hususlar ve İlgili Taraflar Listesi. YGG öncesi gözden geçirilir.")
    bas = ["No", "Tarih", "Kaynak (İç/Dış husus veya İlgili taraf)", "Tür", "Kategori", "Tanım",
           "Olasılık (1-5)", "Yasal Etki (1-3)", "Operasyonel Etki (1-3)", "Finansal Etki (1-3)",
           "İtibar Etkisi (1-3)", "Toplam Etki", "Skor", "Öncelik", "Aksiyon", "Sorumlu",
           "Termin", "Etkinlik Değerlendirmesi", "Durum"]
    k.sayfa("Risk ve Fırsatlar", bas, [["RF-01", "", "ÖRNEK — Dış: İklim / aşırı sıcak (Amd 1:2024)",
            "Risk", "Operasyonel", "Yaz aylarında üretim alanında ısı stresi", "", "", "", "", ""]],
            listeler={"Tür": ["Risk", "Fırsat"], "Olasılık (1-5)": [1, 2, 3, 4, 5],
                      "Yasal Etki (1-3)": [1, 2, 3], "Operasyonel Etki (1-3)": [1, 2, 3],
                      "Finansal Etki (1-3)": [1, 2, 3], "İtibar Etkisi (1-3)": [1, 2, 3],
                      "Kategori": ["Stratejik", "Operasyonel", "Yasal", "Finansal", "İnsan kaynağı",
                                   "Yüklenici/Tedarik", "İklim", "Teknoloji"], "Durum": DURUM},
            formuller={"Toplam Etki": '=IF([Yasal Etki (1-3)]{r}="","",[Yasal Etki (1-3)]{r}+[Operasyonel Etki (1-3)]{r}+[Finansal Etki (1-3)]{r}+[İtibar Etkisi (1-3)]{r})',
                       "Skor": '=IF(OR([Olasılık (1-5)]{r}="",[Toplam Etki]{r}=""),"",[Olasılık (1-5)]{r}*[Toplam Etki]{r})',
                       "Öncelik": '=IF([Skor]{r}="","",IF([Skor]{r}>=36,"Yüksek",IF([Skor]{r}>=16,"Orta","Düşük")))'},
            isi_haritasi=["Skor"], durum_sutunu="Durum", bos_satir=40)
    return k.kaydet(yol)


def baglam(bilgi, yol):
    k = _kayit(bilgi, "baglam")
    k.bilgi_sayfasi(aciklama="Madde 4.1 ve 4.2 (Amd 1:2024: iklim değişikliğinin ilgili olup olmadığı "
                             "4.1'de değerlendirilir; ilgili taraflar iklim beklentisi taşıyabilir).",
                    kullanim_notu="Yılda bir ve YGG öncesi gözden geçirilir.")
    k.sayfa("İç-Dış Hususlar", ["No", "İç / Dış", "Başlık (PESTLE / iç kaynak)", "Husus",
            "İSG'ye Etkisi", "İlgili Risk/Fırsat No", "Son Gözden Geçirme"],
            [["H-01", "Dış", "Çevresel / İklim", "ÖRNEK — Sıcak hava dalgalarının sıklaşması",
              "Isı stresi, soğutma yükü, acil durum", "RF-01", ""]],
            listeler={"İç / Dış": ["İç", "Dış"]}, bos_satir=30)
    k.sayfa("İlgili Taraflar", ["No", "İlgili Taraf", "İç / Dış", "İhtiyaç ve Beklentiler",
            "Yasal Şart mı? (6.1.3'e aktarılır)", "Karşılama Yöntemi", "İletişim Kanalı"],
            [["T-01", "Çalışanlar ve çalışan temsilcileri", "İç",
              "Güvenli işyeri, bilgilendirme, katılım, çalışmaktan kaçınma hakkı",
              "Evet", "Risk değerlendirmesi, kurul, eğitim", "Kurul, panolar"],
             ["T-02", "Çalışma ve Sosyal Güvenlik Bakanlığı / İş Müfettişleri", "Dış",
              "6331 ve alt mevzuata uyum", "Evet", "Yasal şart takibi", "İSG-KATİP, resmi yazı"],
             ["T-03", "Yükleniciler / alt işverenler", "Dış", "Risklerin paylaşılması, koordinasyon",
              "Evet (6331 m.23)", "Yüklenici prosedürü", "Giriş eğitimi, iş izni"]],
            listeler={"İç / Dış": ["İç", "Dış"], "Yasal Şart mı? (6.1.3'e aktarılır)": ["Evet", "Hayır"]},
            bos_satir=25)
    return k.kaydet(yol)


# Ad listesi kasıtlı olarak tarih/sayı içermez: Resmî Gazete künyesi mevzuat.gov.tr'den
# teyit edilerek yazılır. Uydurma künye denetimde güveni tümden bitirir.
MEVZUAT = [
    ("Kanun", "6331 sayılı İş Sağlığı ve Güvenliği Kanunu", "Tümü"),
    ("Kanun", "4857 sayılı İş Kanunu", "İSG, çalışma süreleri, gece çalışması"),
    ("Kanun", "5510 sayılı Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu", "m.13-14 iş kazası/meslek hastalığı bildirimi"),
    ("Yönetmelik", "İş Sağlığı ve Güvenliği Risk Değerlendirmesi Yönetmeliği", ""),
    ("Yönetmelik", "İş Sağlığı ve Güvenliği Hizmetleri Yönetmeliği", ""),
    ("Yönetmelik", "İş Sağlığı ve Güvenliği Kurulları Hakkında Yönetmelik", ""),
    ("Yönetmelik", "İşyerlerinde Acil Durumlar Hakkında Yönetmelik", ""),
    ("Yönetmelik", "Çalışanların İş Sağlığı ve Güvenliği Eğitimlerinin Usul ve Esasları Hakkında Yönetmelik", "2 Nisan 2026 değişikliği"),
    ("Yönetmelik", "İş Ekipmanlarının Kullanımında Sağlık ve Güvenlik Şartları Yönetmeliği", "Ek-III periyodik kontroller"),
    ("Yönetmelik", "Kişisel Koruyucu Donanımların İşyerlerinde Kullanılması Hakkında Yönetmelik", ""),
    ("Yönetmelik", "Güvenlik ve Sağlık İşaretleri Yönetmeliği", ""),
    ("Yönetmelik", "İşyeri Bina ve Eklentilerinde Alınacak Sağlık ve Güvenlik Önlemlerine İlişkin Yönetmelik", ""),
    ("Yönetmelik", "Kimyasal Maddelerle Çalışmalarda Sağlık ve Güvenlik Önlemleri Hakkında Yönetmelik", ""),
    ("Yönetmelik", "Çalışanların Gürültü ile İlgili Risklerden Korunmalarına Dair Yönetmelik", ""),
    ("Yönetmelik", "Çalışanların Titreşimle İlgili Risklerden Korunmalarına Dair Yönetmelik", ""),
    ("Yönetmelik", "Tozla Mücadele Yönetmeliği", ""),
    ("Yönetmelik", "Elle Taşıma İşleri Yönetmeliği", ""),
    ("Yönetmelik", "Ekranlı Araçlarla Çalışmalarda Sağlık ve Güvenlik Önlemleri Hakkında Yönetmelik", ""),
    ("Yönetmelik", "Çalışanların Patlayıcı Ortamların Tehlikelerinden Korunması Hakkında Yönetmelik", "Toz/gaz patlama riski varsa"),
    ("Yönetmelik", "Binaların Yangından Korunması Hakkında Yönetmelik", ""),
    ("Yönetmelik", "İş Sağlığı ve Güvenliği ile İlgili Çalışan Temsilcisinin Nitelikleri ve Seçilme Usul ve Esaslarına İlişkin Tebliğ", ""),
    ("Yönetmelik", "Gebe veya Emziren Kadınların Çalıştırılma Şartlarıyla Emzirme Odaları ve Çocuk Bakım Yurtlarına Dair Yönetmelik", ""),
    ("Yönetmelik", "Çocuk ve Genç İşçilerin Çalıştırılma Usul ve Esasları Hakkında Yönetmelik", ""),
    ("Yönetmelik", "Yapı İşlerinde İş Sağlığı ve Güvenliği Yönetmeliği", "Bina içi inşaat/tadilat işleri varsa"),
    ("Yönetmelik", "Tehlikeli ve Çok Tehlikeli Sınıfta Yer Alan İşlerde Çalıştırılacakların Mesleki Eğitimlerine Dair Yönetmelik", "Tehlikeli/çok tehlikeli sınıf"),
    ("Yönetmelik", "Sağlık ve Güvenlik Önlemlerinin Alınmasında Bölünemeyen Yükümlülükler / İşin Durdurulmasına Dair Yönetmelik", "Temmuz 2026 değişikliği"),
    ("Tebliğ", "İş Sağlığı ve Güvenliğine İlişkin İşyeri Tehlike Sınıfları Tebliği", "NACE koduna göre tehlike sınıfı"),
    ("Diğer şart", "Müşteri / grup şirketi İSG şartları", ""),
    ("Diğer şart", "TS EN ISO 45001:2018 + Amd 1:2024", ""),
]


def yasal(bilgi, yol):
    k = _kayit(bilgi, "yasal")
    k.bilgi_sayfasi(aciklama=("Madde 6.1.3 ve 9.1.2. Liste bir başlangıç önerisidir; kuruluşa "
                              "uygulanabilirlik ve Resmî Gazete künyesi (ilk yayın + son değişiklik) "
                              "mevzuat.gov.tr'den teyit edilmeden kesinleşmiş sayılmaz. Mülga tüzükleri "
                              "(ör. İşçi Sağlığı ve İş Güvenliği Tüzüğü) listeye almayın."),
                    kullanim_notu="Uygunluk değerlendirmesi en az yılda bir; önemli değişiklikte o mevzuat için derhal.")
    satir = [[i + 1, t, ad, "[TEYİT: RG tarih/sayı]", "[TEYİT]", ilgili or "[DOLDURULACAK: ilgili maddeler]",
              "Evet", "", "", "", "", "", ""] for i, (t, ad, ilgili) in enumerate(MEVZUAT)]
    k.sayfa("Mevzuat Listesi", ["No", "Tür", "Mevzuat / Şart", "İlk Yayın RG Tarih-Sayı",
            "Son Değişiklik RG Tarih-Sayı", "İlgili Maddeler / Yükümlülük", "Uygulanabilir mi?",
            "Gerekçe (uygulanmıyorsa)", "Sorumlu", "Uygunluk Değerlendirme Tarihi",
            "Uygunluk Durumu", "Kanıt / Kayıt", "Aksiyon (DÖF No)"],
            satir, genislikler=[5, 11, 48, 18, 18, 34, 12, 24, 16, 14, 14, 26, 14],
            listeler={"Uygulanabilir mi?": EVET_HAYIR,
                      "Uygunluk Durumu": ["Uygun", "Kısmen Uygun", "Uygun Değil"]},
            durum_sutunu="Uygunluk Durumu", bos_satir=20)
    return k.kaydet(yol)


def hedef(bilgi, yol):
    k = _kayit(bilgi, "hedef")
    k.bilgi_sayfasi(aciklama="Madde 6.2.1–6.2.2: ölçülebilir İSG hedefleri ve bunlara ulaşma planı.",
                    kullanim_notu="Hedef; politika taahhüdüne, risk değerlendirmesine ve yasal şarta bağlanır.")
    k.sayfa("Hedefler", ["No", "İlgili Politika Taahhüdü", "Hedef", "Gösterge (KPI)", "Başlangıç Değeri",
            "Hedef Değer", "Faaliyetler", "Kaynak", "Sorumlu", "Termin", "İzleme Sıklığı",
            "Gerçekleşen", "Durum"],
            [["H-01", "İş kazalarının önlenmesi", "ÖRNEK — Kaza sıklık oranını düşürmek",
              "KSO = kayıp günlü kaza × 1.000.000 / toplam çalışma saati", "", "", "", "", "",
              "", "Aylık", "", "Açık"]],
            listeler={"Durum": DURUM, "İzleme Sıklığı": ["Aylık", "3 aylık", "6 aylık", "Yıllık"]},
            durum_sutunu="Durum", bos_satir=15)
    return k.kaydet(yol)


def periyodik(bilgi, yol):
    k = _kayit(bilgi, "periyodik")
    k.bilgi_sayfasi(aciklama="Madde 9.1.1: izleme-ölçme planı; iş ekipmanı periyodik kontrolleri, "
                             "ortam ölçümleri, sağlık gözetimi ve tatbikatlar.",
                    kullanim_notu="Periyotlar ilgili mevzuattan/üretici talimatından teyit edilir. "
                                  "Sonraki tarih formüldür.")
    satir = [
        ["İş ekipmanı", "ÖRNEK — Forklift / istif makineleri", "İş Ekipmanları Yön. Ek-III", 12, "", "", "Yetkili kişi/kuruluş", ""],
        ["İş ekipmanı", "Kaldırma ve iletme ekipmanları (vinç, caraskal)", "İş Ekipmanları Yön. Ek-III", 12, "", "", "", ""],
        ["İş ekipmanı", "Basınçlı kaplar, kompresör tankları", "İş Ekipmanları Yön. Ek-III", 12, "", "", "", ""],
        ["İş ekipmanı", "Buhar kazanları", "İş Ekipmanları Yön. Ek-III", 12, "", "", "", ""],
        ["Elektrik", "Topraklama ve iç tesisat uygunluk", "İlgili elektrik mevzuatı", 12, "", "", "", ""],
        ["Elektrik", "Paratoner (yıldırımdan korunma)", "", 12, "", "", "", ""],
        ["Yangın", "Yangın söndürücüler", "Binaların Yangından Korunması Yön.", 6, "", "", "", ""],
        ["Yangın", "Yangın dolapları / hidrantlar", "", 3, "", "", "", ""],
        ["Acil durum", "Acil aydınlatma ve yönlendirme", "", 1, "", "", "", ""],
        ["Acil durum", "Tahliye tatbikatı", "Acil Durumlar Yön.", 12, "", "", "", ""],
        ["Ortam ölçümü", "Gürültü", "Gürültü Yön.", "", "", "", "Akredite laboratuvar", ""],
        ["Ortam ölçümü", "Toz / kimyasal maruziyet", "Tozla Mücadele / Kimyasal Yön.", "", "", "", "", ""],
        ["Ortam ölçümü", "Termal konfor / aydınlatma", "", "", "", "", "", ""],
        ["Sağlık gözetimi", "Periyodik muayeneler", "İSG Hizmetleri Yön.", "", "", "", "İşyeri hekimi", ""],
    ]
    k.sayfa("Plan", ["Konu", "Ekipman / Parametre", "Dayanak", "Periyot (ay)", "Son Kontrol Tarihi",
            "Sonraki Kontrol", "Yapan Kişi / Kuruluş", "Rapor No / Sonuç", "Uygunsuzluk", "Durum"],
            satir, genislikler=[14, 40, 30, 11, 15, 15, 22, 20, 18, 12],
            formuller={"Sonraki Kontrol": '=IF(OR([Son Kontrol Tarihi]{r}="",[Periyot (ay)]{r}=""),"",EDATE([Son Kontrol Tarihi]{r},[Periyot (ay)]{r}))'},
            listeler={"Durum": ["Uygun", "Uygun Değil", "Gecikti"]}, durum_sutunu="Durum", bos_satir=40)
    return k.kaydet(yol)


def egitim(bilgi, yol):
    k = _kayit(bilgi, "egitim")
    k.bilgi_sayfasi(
        aciklama=("Madde 7.2/7.3 ve Çalışanların İSG Eğitimlerinin Usul ve Esasları Yön. "
                  "(2 Nisan 2026 değişikliği): temel eğitim işe girişten itibaren en geç 3 ay içinde; "
                  "1 ders saati = 45 dk eğitim + 15 dk ara; tehlikeli/çok tehlikeli sınıfta "
                  "'işe ve işyerine özgü riskler' başlığı yalnız yüz yüze; 4. başlık asgari "
                  "süre az/tehlikeli/çok tehlikeli için 2/3/4 ders saati. Tekrar periyotları ve "
                  "toplam süreleri güncel metinden teyit edin."),
        kullanim_notu="Uzaktan eğitimde giriş-çıkış, tamamlama oranı ve sınav sonucu kaydı saklanır.")
    k.sayfa("Eğitim Planı", ["No", "Eğitim Konusu", "Hedef Grup", "Tür", "Yöntem", "Süre (ders saati)",
            "Eğitici", "Planlanan Ay", "Gerçekleşen Tarih", "Katılım (%)", "Etkinlik Değerlendirmesi", "Durum"],
            [["E-01", "Temel İSG eğitimi — genel, sağlık, teknik konular", "Tüm çalışanlar", "Temel",
              "Yüz yüze / uzaktan", "", "İGU + İH", "", "", "", "", "Açık"],
             ["E-02", "Temel İSG eğitimi — işe ve işyerine özgü riskler", "Tüm çalışanlar", "Temel",
              "Yüz yüze", "", "İGU", "", "", "", "", "Açık"],
             ["E-03", "Acil durum ekipleri eğitimi", "Ekip üyeleri", "Mevzuat", "Yüz yüze", "", "", "", "", "", "", "Açık"],
             ["E-04", "Çalışan temsilcisi eğitimi", "Çalışan temsilcileri", "Mevzuat", "Yüz yüze", "", "", "", "", "", "", "Açık"],
             ["E-05", "ISO 45001 farkındalık ve iç tetkikçi", "Yönetim / tetkikçiler", "Sistem", "", "", "", "", "", "", "", "Açık"]],
            listeler={"Tür": ["Temel", "Tekrar", "İşe başlama", "İş değişikliği", "Mevzuat", "Sistem", "Mesleki"],
                      "Yöntem": ["Yüz yüze", "Uzaktan", "Karma", "Yüz yüze / uzaktan"], "Durum": DURUM},
            durum_sutunu="Durum", bos_satir=30)
    k.sayfa("Eğitim Matrisi", ["Ad Soyad", "Bölüm", "Görev", "İşe Giriş", "Temel Eğitim Son Tarih (3 ay)",
            "Temel Eğitim Tarihi", "Tekrar Eğitimi Tarihi", "Özel Eğitimler / Belgeler (MYK vb.)", "Not"],
            [], formuller={"Temel Eğitim Son Tarih (3 ay)": '=IF([İşe Giriş]{r}="","",EDATE([İşe Giriş]{r},3))'},
            bos_satir=60)
    return k.kaydet(yol)


def kkd(bilgi, yol):
    k = _kayit(bilgi, "kkd")
    k.bilgi_sayfasi(aciklama="KKD Kullanımı Yönetmeliği ve risk değerlendirmesine dayalı bölüm-KKD matrisi. "
                             "'Z' zorunlu, 'G' gerektiğinde. KKD, kontrol hiyerarşisinde son kademedir.",
                    kullanim_notu="Her satır bir risk değerlendirmesi satırına bağlanmalı (RD No).")
    kkdler = ["Baret / bone", "Koruyucu gözlük / yüz siperi", "Kulak koruyucu", "Toz maskesi (FFP2/3)",
              "Gaz maskesi", "Kesilmeye dayanıklı eldiven", "Kimyasal eldiven", "Isıya dayanıklı eldiven",
              "İş ayakkabısı (S2/S3)", "Reflektörlü yelek", "Emniyet kemeri (tam vücut)", "Soğuk ortam giysisi"]
    k.sayfa("Matris", ["Bölüm / Görev", "RD No"] + kkdler + ["Standart / Not"],
            [["ÖRNEK — Üretim", ""] + [""] * len(kkdler) + [""]],
            listeler={x: ["Z", "G", ""] for x in kkdler}, bos_satir=25)
    k.sayfa("Zimmet", ["Tarih", "Ad Soyad", "Bölüm", "KKD", "Adet", "Standart / Kategori",
                       "Değişim Nedeni", "İmza"], [], bos_satir=60)
    return k.kaydet(yol)


def olay(bilgi, yol):
    k = _kayit(bilgi, "olay")
    k.bilgi_sayfasi(aciklama=("Madde 10.2: olay (iş kazası, ramak kala, tehlikeli durum, meslek hastalığı) "
                              "kaydı. İş kazası SGK'ya en geç 3 iş günü içinde bildirilir (5510 m.13; "
                              "6331 m.14). Sağlık bilgisi özel nitelikli kişisel veridir (KVKK m.6): bu "
                              "tabloda tanı yazılmaz, yalnız yaralanma türü ve kayıp gün."),
                    kullanim_notu="KSO ve KAO 'İstatistik' sayfasında formülle hesaplanır.")
    k.sayfa("Olaylar", ["Olay No", "Tarih", "Saat", "Vardiya", "Bölüm", "Olay Türü", "Kısa Tanım",
            "Etkilenen (Çalışan/Yüklenici/Ziyaretçi)", "Yaralanma Türü / Vücut Bölgesi", "Kayıp İş Günü",
            "SGK Bildirim Tarihi", "Kök Neden", "DÖF No", "Risk Değerlendirmesi Güncellendi mi?", "Durum"],
            [], listeler={"Olay Türü": ["İş kazası (kayıp günlü)", "İş kazası (kayıp günsüz)", "İlk yardım",
                                         "Ramak kala", "Tehlikeli durum", "Meslek hastalığı", "Maddi hasarlı olay"],
                          "Vardiya": ["Gündüz", "Akşam", "Gece"],
                          "Risk Değerlendirmesi Güncellendi mi?": EVET_HAYIR, "Durum": DURUM},
            durum_sutunu="Durum", bos_satir=80)
    k.sayfa("İstatistik", ["Ay", "Ortalama Çalışan", "Toplam Çalışma Saati", "Kayıp Günlü Kaza",
            "Kayıp Gün", "Ramak Kala", "KSO (×1.000.000)", "KAO (×1.000)"],
            [[a, "", "", "", "", "", "", ""] for a in ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran",
             "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]],
            formuller={"KSO (×1.000.000)": '=IF(N([Toplam Çalışma Saati]{r})=0,"",[Kayıp Günlü Kaza]{r}*1000000/[Toplam Çalışma Saati]{r})',
                       "KAO (×1.000)": '=IF(N([Toplam Çalışma Saati]{r})=0,"",[Kayıp Gün]{r}*1000/[Toplam Çalışma Saati]{r})'})
    return k.kaydet(yol)


def dof(bilgi, yol):
    k = _kayit(bilgi, "dof")
    k.bilgi_sayfasi(aciklama="Madde 10.2: uygunsuzluk ve düzeltici faaliyet. 45001'de 'önleyici faaliyet' "
                             "kavramı yoktur; potansiyel durumlar risk ve fırsat sürecinde ele alınır.",
                    kullanim_notu="Etkinlik doğrulaması kapanıştan en az 1-3 ay sonra yapılır.")
    k.sayfa("DÖF", ["DÖF No", "Açılış Tarihi", "Kaynak", "Uygunsuzluk Tanımı", "Düzeltme (anlık)",
            "Kök Neden (5 Neden / Balık Kılçığı)", "Düzeltici Faaliyet", "Çalışan / Temsilci Katılımı",
            "Sorumlu", "Termin", "Kapanış Tarihi", "Etkinlik Doğrulama", "RD/Doküman Güncellendi mi?", "Durum"],
            [], listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "Olay/kaza", "Saha denetimi", "Yasal uygunluk",
                                      "Çalışan bildirimi", "Müfettiş", "YGG", "Tatbikat"],
                          "Etkinlik Doğrulama": ["Etkin", "Etkin değil", "Bekliyor"],
                          "RD/Doküman Güncellendi mi?": EVET_HAYIR, "Durum": DURUM},
            durum_sutunu="Durum", bos_satir=60)
    return k.kaydet(yol)


def tetkik(bilgi, yol):
    k = _kayit(bilgi, "tetkik")
    k.bilgi_sayfasi(aciklama="Madde 9.2: iç tetkik programı. Tetkikçi kendi işini tetkik etmez.",
                    kullanim_notu="Önem ve önceki sonuçlara göre sıklık artırılır; tüm maddeler yılda en az bir kez.")
    aylar = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"]
    maddeler = ["4 Bağlam", "5.1-5.3 Liderlik", "5.4 Danışma ve katılım", "6.1 Risk/fırsat, yasal şart",
                "6.2 Hedefler", "7 Destek", "8.1 Operasyonel kontrol", "8.1.3 Değişiklik yönetimi",
                "8.1.4 Satın alma/yükleniciler", "8.2 Acil durum", "9.1 İzleme-ölçme", "9.3 YGG",
                "10 İyileştirme"]
    k.sayfa("Program", ["Madde / Süreç", "Bölüm", "Tetkikçi"] + aylar + ["Rapor No", "Bulgu Sayısı"],
            [[m, "", ""] + [""] * 14 for m in maddeler],
            listeler={a: ["P", "G", ""] for a in aylar}, bos_satir=5)
    return k.kaydet(yol)


def dokuman(bilgi, yol):
    k = _kayit(bilgi, "dokuman")
    k.bilgi_sayfasi(aciklama="Madde 7.5: iç ve dış kaynaklı dokümanların ana listesi.",
                    kullanim_notu="Yol gösterici (kodsuz) dosyalar bu listeye girmez — bilinçli tercihtir.")
    k.sayfa("İç Kaynaklı", ["Doküman Kodu", "Doküman Adı", "Tür", "Sahibi", "Yürürlük Tarihi",
            "Revizyon No", "Revizyon Tarihi", "Son Gözden Geçirme", "Dağıtım", "Saklama Süresi", "Durum"],
            [], listeler={"Durum": ["Yürürlükte", "Revizyonda", "İptal"]}, bos_satir=80)
    k.sayfa("Dış Kaynaklı", ["No", "Doküman / Standart / Mevzuat", "Kaynak", "Sürüm / Tarih",
            "Güncellik Kontrolü", "Bulunduğu Yer"], [], bos_satir=30)
    return k.kaydet(yol)


def degisiklik(bilgi, yol):
    k = _kayit(bilgi, "degisiklik")
    k.bilgi_sayfasi(aciklama="Madde 8.1.3: planlı geçici/kalıcı değişiklikler (yeni makine, proses, kimyasal, "
                             "yerleşim, organizasyon, mevzuat, bilgi/teknoloji).",
                    kullanim_notu="Değişiklik uygulanmadan önce risk değerlendirmesi ve İSG onayı alınır.")
    k.sayfa("Değişiklikler", ["Değişiklik No", "Talep Tarihi", "Talep Eden", "Değişiklik Türü", "Tanım",
            "Geçici / Kalıcı", "Etkilenen Alan ve Kişiler", "RD Yapıldı mı? (No)", "Gerekli Önlemler",
            "Eğitim / Bilgilendirme", "Doküman Güncellemesi", "İSG Onayı", "Devreye Alma Tarihi",
            "Sonrası Gözden Geçirme", "Durum"], [],
            listeler={"Değişiklik Türü": ["Makine/ekipman", "Proses", "Kimyasal", "Yerleşim/bina",
                                          "Organizasyon/personel", "Mevzuat", "Yazılım/otomasyon"],
                      "Geçici / Kalıcı": ["Geçici", "Kalıcı"], "İSG Onayı": ["Onaylandı", "Reddedildi", "Bekliyor"],
                      "Durum": DURUM}, durum_sutunu="Durum", bos_satir=40)
    return k.kaydet(yol)


def yuklenici(bilgi, yol):
    k = _kayit(bilgi, "yuklenici")
    k.bilgi_sayfasi(aciklama=("Madde 8.1.4: yüklenici/tedarikçi seçimi ve izlenmesi; 6331 m.23 koordinasyon. "
                              "Ağırlıklar 'Kriterler' sayfasında; toplam formülle 100 kontrol edilir."),
                    kullanim_notu="Yeni yüklenici işe başlamadan önce; sürekli yükleniciler yılda bir değerlendirilir.")
    kriter = [["İSG organizasyonu (İGU/İH, OSGB sözleşmesi)", 15], ["Çalışan SGK kaydı ve özlük", 15],
              ["İSG eğitimleri ve mesleki yeterlilik belgeleri", 15], ["Risk değerlendirmesi / iş güvenliği planı", 15],
              ["KKD ve ekipman uygunluğu (periyodik kontroller)", 15], ["Geçmiş kaza ve ihlal performansı", 15],
              ["Çevre kurallarına uyum (atık, kimyasal)", 10]]
    k.sayfa("Kriterler", ["Kriter", "Ağırlık (%)"], kriter + [["TOPLAM (100 olmalı)", "=SUM(B2:B8)"]],
            genislikler=[60, 14])
    k.sayfa("Değerlendirme", ["Firma", "Hizmet / İş", "Değerlendirme Tarihi"] + [c[0] for c in kriter] +
            ["Ağırlıklı Puan", "Sonuç", "Değerlendiren"], [],
            listeler={c[0]: [0, 1, 2, 3, 4, 5] for c in kriter},
            formuller={"Ağırlıklı Puan": "=IF(COUNT(D{r}:J{r})<7,\"\",(" + "+".join(
                f"{h}{{r}}*Kriterler!$B${i}" for i, h in enumerate("DEFGHIJ", start=2)) + ")/5)",
                       "Sonuç": '=IF([Ağırlıklı Puan]{r}="","",IF([Ağırlıklı Puan]{r}>=70,"Onaylı",IF([Ağırlıklı Puan]{r}>=50,"Şartlı","Red")))'},
            bos_satir=30,
            notlar={"Ağırlıklı Puan": "Her kriter 0-5 puan; ağırlıklarla 0-100 ölçeğine çevrilir."})
    return k.kaydet(yol)


def katilim(bilgi, yol):
    k = _kayit(bilgi, "katilim")
    k.bilgi_sayfasi(aciklama=("Madde 5.4: yönetici olmayan çalışanların danışılması (5.4 d) ve katılımı (5.4 e) "
                              "kanıtı. İSG Kurulu kararları tek başına yeterli kanıt değildir."),
                    kullanim_notu="Her konu için kimlerin, hangi kanalla danışıldığı yazılır.")
    k.sayfa("Kayıtlar", ["No", "Tarih", "Konu (5.4 d/e maddesi)", "Danışma / Katılım", "Kanal",
            "Katılanlar (yönetici olmayan çalışanlar)", "Alınan Görüş / Öneri", "Sonuç / Geri Bildirim", "İlgili Kayıt"],
            [], listeler={"Danışma / Katılım": ["Danışma", "Katılım"],
                          "Kanal": ["İSG Kurulu", "Çalışan temsilcisi", "Saha toplantısı", "Öneri kutusu",
                                    "Anket", "Risk değerlendirme ekibi", "Kaza inceleme ekibi"],
                          "Konu (5.4 d/e maddesi)": ["d1 İhtiyaç-beklenti", "d2 Politika", "d3 Roller",
                                                       "d4 Yasal şartlar", "d5 Hedefler", "d6 Dış kaynak/yüklenici kontrolü",
                                                       "d7 İzleme-ölçme", "d8 Tetkik programı", "d9 Sürekli iyileştirme",
                                                       "e1 Katılım mekanizması", "e2 Tehlike/risk belirleme",
                                                       "e3 Önlem belirleme", "e4 Yetkinlik/eğitim", "e5 İletişim",
                                                       "e6 Kontrol önlemleri", "e7 Olay/uygunsuzluk araştırması"]},
            bos_satir=50)
    return k.kaydet(yol)


def acil(bilgi, yol):
    k = _kayit(bilgi, "acil")
    k.bilgi_sayfasi(aciklama="Madde 8.2 ve İşyerlerinde Acil Durumlar Hakkında Yönetmelik: destek elemanları "
                             "(söndürme, kurtarma, koruma, ilk yardım) ve tatbikat takibi.",
                    kullanim_notu="Ekip sayıları tehlike sınıfına göre yönetmelikten teyit edilir; tatbikat en az yılda bir.")
    k.sayfa("Ekipler", ["Ekip", "Vardiya", "Ad Soyad", "Görev", "Telefon", "Eğitim Tarihi", "Sertifika (ilk yardım vb.)"],
            [], listeler={"Ekip": ["Söndürme", "Kurtarma", "Koruma", "İlk yardım", "Haberleşme / Koordinasyon"]},
            bos_satir=40)
    k.sayfa("Tatbikatlar", ["Tarih", "Senaryo", "Katılımcı Sayısı", "Tahliye Süresi", "Tespitler",
            "DÖF No", "Plan Güncellendi mi?"], [], listeler={"Plan Güncellendi mi?": EVET_HAYIR}, bos_satir=12)
    return k.kaydet(yol)


def kimyasal(bilgi, yol):
    k = _kayit(bilgi, "kimyasal")
    k.bilgi_sayfasi(aciklama="Kimyasal Maddelerle Çalışmalarda Sağlık ve Güvenlik Önlemleri Yön.: envanter + SDS takibi.",
                    kullanim_notu="Türkçe güvenlik bilgi formu (SDS) güncel olmalı; yeni kimyasal değişiklik yönetimine girer.")
    k.sayfa("Envanter", ["Ticari Ad", "Tedarikçi", "Kullanım Yeri", "Kullanım Amacı", "Zararlılık (H ifadeleri)",
            "SDS Var mı?", "SDS Tarihi", "Maksimum Stok", "Depolama Yeri / Uyumluluk", "Gerekli KKD", "RD No"],
            [], listeler={"SDS Var mı?": EVET_HAYIR}, bos_satir=50)
    return k.kaydet(yol)


def ekipman(bilgi, yol):
    k = _kayit(bilgi, "ekipman")
    k.bilgi_sayfasi(aciklama="Periyodik kontrole tabi iş ekipmanları envanteri (kaldırma, basınçlı kap, iletme vb.).",
                    kullanim_notu="Plan (İzleme-Ölçme ve Periyodik Kontrol Planı) bu envantere dayanır.")
    k.sayfa("Envanter", ["Envanter No", "Ekipman", "Tür", "Marka / Model", "Seri No", "Konum",
            "Kapasite", "Kullanıcı Yetki Belgesi Gerekli mi?", "Son Periyodik Kontrol", "Sonuç"], [],
            listeler={"Kullanıcı Yetki Belgesi Gerekli mi?": EVET_HAYIR,
                      "Sonuç": ["Uygun", "Uygun Değil"]}, durum_sutunu="Sonuç", bos_satir=50)
    return k.kaydet(yol)


URETICI = {"risk": risk, "riskfirsat": riskfirsat, "baglam": baglam, "yasal": yasal, "hedef": hedef,
           "periyodik": periyodik, "egitim": egitim, "kkd": kkd, "olay": olay, "dof": dof,
           "tetkik": tetkik, "dokuman": dokuman, "degisiklik": degisiklik, "yuklenici": yuklenici,
           "katilim": katilim, "acil": acil, "kimyasal": kimyasal, "ekipman": ekipman}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kurulus", required=True)
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--tarih", default="")
    ap.add_argument("--hazirlayan", default="")
    ap.add_argument("--onaylayan", default="")
    ap.add_argument("--yontem", default="l-matris", choices=["l-matris", "fine-kinney"])
    ap.add_argument("--tehlike-sinifi", default="[DOLDURULACAK]")
    ap.add_argument("--onek", default="İSGYS")
    ap.add_argument("--kodlar", default="{}", help='JSON: {"risk": "1000-11-FR-022", ...}')
    ap.add_argument("--hangi", default="", help="virgüllü anahtar listesi; boşsa hepsi")
    ap.add_argument("--sade", action="store_true", help="küçük kuruluş: yardımcı kayıtları atla")
    a = ap.parse_args()
    bilgi = dict(kurulus=a.kurulus, tarih=a.tarih, hazirlayan=a.hazirlayan, onaylayan=a.onaylayan,
                 yontem=a.yontem, tehlike_sinifi=a.tehlike_sinifi, onek=a.onek,
                 kodlar=json.loads(a.kodlar))
    secim = [x.strip() for x in a.hangi.split(",") if x.strip()] or list(URETICI)
    if a.sade:
        secim = [x for x in secim if x not in SADE_DISI]
    for anahtar in secim:
        print(URETICI[anahtar](bilgi, _dosya(bilgi, anahtar, a.cikti)))


if __name__ == "__main__":
    main()
