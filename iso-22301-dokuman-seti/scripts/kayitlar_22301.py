#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_22301.py — ISYS'nin tekrar eden Excel kayitlarini uretir.

En degerlisi BIA: zaman dilimlerine gore etki, MTPD/RTO/RPO/MBCO, bagimliliklar
ve RTO<MTPD tutarlilik kontrolu formulle kurulu gelir. Bu kontrol elle yapildiginda
en sik atlanan seydir ve denetimde ilk yakalanandir.

Kullanim:
    python3 kayitlar_22301.py --kurulus "ACME A.S." --cikti "/yol/03_Analiz" \\
        --tarih 2026-08-11 --hangi bia,risk,strateji,kaynak,tatbikat,iletisim,hedef,dof,dokuman,yetkinlik,zincir
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

STANDART = "TS EN ISO 22301 (ISO 22301:2019)"

KAYNAK_BASLIKLARI = [
    "İnsan (personel, yetkinlik)",
    "Bilgi ve veri",
    "Fiziksel altyapı (bina, alan)",
    "Ekipman ve sarf malzemeleri",
    "Bilgi ve iletişim teknolojisi sistemleri",
    "Ulaşım ve lojistik",
    "Finans",
    "Ortaklar ve tedarikçiler",
]

ZAMAN_DILIMLERI = ["0-4 saat", "4-24 saat", "1-3 gün", "3-7 gün", "7+ gün"]
ETKI_SEVIYELERI = ["Önemsiz", "Düşük", "Orta", "Yüksek", "Kritik"]


def _kayit(bilgi: dict, ad: str, kod: str) -> YSKayit:
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=kod,
                   standart=STANDART, sistem="İSYS",
                   revizyon=bilgi.get("revizyon", "00"), tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""), onaylayan=bilgi.get("onaylayan", ""))


# ----------------------------------------------------------------------- BIA
def bia(bilgi: dict, cikti: str, ornek_satirlar: list | None = None) -> str:
    basliklar = (["Faaliyet No", "Faaliyet", "Sahip Birim", "Süreç Sahibi"] +
                 [f"Etki {z}" for z in ZAMAN_DILIMLERI] +
                 ["Baskın Etki Türü", "MTPD (saat)", "RTO (saat)", "RTO Kontrolü",
                  "RPO (saat)", "MBCO / Asgari Çıktı", "Bağımlı Personel/Rol",
                  "Bağımlı Sistemler", "Bağımlı Veri", "Bağımlı Tedarikçiler",
                  "Lokasyon", "Bağımlı Diğer Faaliyetler", "Zirve Dönem",
                  "Mevcut Kurtarma Yeteneği (saat)", "Boşluk (saat)",
                  "Öncelik", "Değerlendirme Tarihi", "Sonraki Gözden Geçirme"])
    k = _kayit(bilgi, "İş Etki Analizi (BIA)", bilgi.get("kod_bia", "İSYS-FR-02"))
    k.bilgi_sayfasi(
        aciklama=("ISO 22301 Madde 8.2.2 gereği iş etki analizi. Kesinti etkisinin "
                  "zaman içindeki değişimi, öncelikli faaliyetler, zaman çerçeveleri "
                  "(MTPD/RTO/RPO/MBCO) ve bağımlılıklar bu tabloda toplanır."),
        kullanim_notu=("Yılda en az bir kez ve organizasyon/sistem/tedarikçi "
                       "değişikliklerinde güncellenir. 'RTO Kontrolü' sütunu "
                       "otomatiktir: RTO, MTPD'den küçük olmalıdır."))
    # sutun harfleri: MTPD=M(13), RTO=N(14), RTO Kontrolu=O(15), Mevcut=X, Bosluk=Y
    k.sayfa("BIA", basliklar, ornek_satirlar or [],
            genislikler=([11, 40, 18, 20] + [12] * 5 +
                         [18, 13, 12, 14, 12, 34, 26, 28, 24, 26, 16, 30, 18, 22, 14, 11, 16, 18]),
            listeler={**{f"Etki {z}": ETKI_SEVIYELERI for z in ZAMAN_DILIMLERI},
                      "Baskın Etki Türü": ["Finansal", "Operasyonel", "Yasal/Düzenleyici",
                                            "İtibar", "Müşteri/Hizmet", "Personel güvenliği"],
                      "Öncelik": ["Kritik", "Yüksek", "Orta", "Düşük"]},
            formuller={
                "RTO Kontrolü": '=IF(OR([MTPD (saat)]{r}="",[RTO (saat)]{r}=""),"",'
                                'IF([RTO (saat)]{r}<[MTPD (saat)]{r},"OK","HATA: RTO ≥ MTPD"))',
                "Boşluk (saat)": '=IF(OR([RTO (saat)]{r}="",'
                                 '[Mevcut Kurtarma Yeteneği (saat)]{r}=""),"",'
                                 'MAX(0,[Mevcut Kurtarma Yeteneği (saat)]{r}-[RTO (saat)]{r}))',
            },
            durum_sutunu="RTO Kontrolü", bos_satir=60,
            notlar={"MTPD (saat)": "Faaliyetin durmasının kabul edilemez hâle geldiği süre. İş tarafı belirler.",
                    "RTO (saat)": "Kurtarma hedefi. MTPD'den KISA olmalıdır.",
                    "RPO (saat)": "Kabul edilebilir azami veri kaybı. RTO'dan bağımsızdır.",
                    "MBCO / Asgari Çıktı": "Kesinti sırasında sürdürülmesi gereken asgari hizmet seviyesi.",
                    "Zirve Dönem": "Kesintinin en pahalıya patlayacağı dönem (ay sonu, sezon, kampanya).",
                    "Bağımlı Diğer Faaliyetler": "Bağımlı olunan faaliyetin RTO'su bu faaliyetinkinden kısa olmalıdır."})
    k.sayfa("Etki Kriterleri",
            ["Etki Seviyesi", "Finansal", "Operasyonel", "Yasal/Düzenleyici", "İtibar", "Müşteri/Hizmet"],
            [[s, "[DOLDURULACAK]", "[DOLDURULACAK]", "[DOLDURULACAK]",
              "[DOLDURULACAK]", "[DOLDURULACAK]"] for s in ETKI_SEVIYELERI],
            genislikler=[16, 30, 30, 30, 30, 30],
            notlar={"Etki Seviyesi": "Kuruluşa özgü eşikler girilmeli — 'Kritik' bir KOBİ ile holding için aynı tutar değildir."})
    k.ozet_sayfasi("Özet", "BIA", "Öncelik", ["Kritik", "Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- risk
def risk(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Süreklilik Risk Değerlendirmesi", bilgi.get("kod_risk", "İSYS-FR-03"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.2.3 gereği öncelikli faaliyetlerin kesintiye uğrama riskinin değerlendirilmesi.",
        kullanim_notu="BIA ile birlikte güncellenir. Her öncelikli faaliyet en az bir risk satırına bağlanmalıdır.")
    k.sayfa("Risk Değerlendirmesi",
            ["Risk No", "İlgili Faaliyet No", "Kesinti Senaryosu", "Tehdit Kaynağı",
             "Açıklık / Zayıflık", "Mevcut Önlemler", "Olasılık (1-5)", "Etki (1-5)",
             "Risk Skoru", "Risk Seviyesi", "Risk Sahibi", "İşleme Kararı",
             "Planlanan Önlem", "İlgili Strateji No", "Sorumlu", "Termin",
             "Artık Risk", "Onay", "Durum"],
            [], genislikler=[9, 15, 34, 22, 30, 30, 12, 11, 11, 13, 18, 14, 34, 16, 16, 12, 11, 13, 11],
            listeler={"Olasılık (1-5)": [1, 2, 3, 4, 5], "Etki (1-5)": [1, 2, 3, 4, 5],
                      "İşleme Kararı": ["Azalt", "Kabul et", "Aktar", "Kaçın"],
                      "Onay": ["Onaylandı", "Beklemede"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            formuller={
                "Risk Skoru": '=IF(AND([Olasılık (1-5)]{r}<>"",[Etki (1-5)]{r}<>""),'
                              '[Olasılık (1-5)]{r}*[Etki (1-5)]{r},"")',
                "Risk Seviyesi": '=IF([Risk Skoru]{r}="","",IF([Risk Skoru]{r}>=15,"Yüksek",'
                                 'IF([Risk Skoru]{r}>=8,"Orta","Düşük")))'},
            isi_haritasi=["Risk Skoru"], durum_sutunu="Durum", bos_satir=50,
            notlar={"Kesinti Senaryosu": "Somut olmalı: 'siber saldırı' değil, "
                                          "'fidye yazılımı nedeniyle üretim veritabanının 48 saat erişilemez olması'."})
    return k.kaydet(cikti)


# -------------------------------------------------------------------- strateji
def strateji(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Süreklilik Stratejisi ve Boşluk Analizi", bilgi.get("kod_str", "İSYS-FR-05"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.3.2 ve 8.3.3 gereği strateji belirleme ve seçimi.",
        kullanim_notu="Her öncelikli faaliyet için en az bir strateji satırı bulunmalıdır.")
    k.sayfa("Strateji ve Boşluk",
            ["Strateji No", "İlgili Faaliyet No", "Faaliyet", "RTO Hedefi (saat)",
             "Mevcut Yetenek (saat)", "Boşluk (saat)", "Strateji Kategorisi",
             "Değerlendirilen Seçenekler", "Seçilen Strateji", "Seçim Gerekçesi",
             "Tahmini Maliyet", "Uygulama Sorumlusu", "Termin",
             "Uygulama Durumu", "Doğrulama Yöntemi", "İlgili Plan"],
            [], genislikler=[11, 15, 34, 15, 16, 13, 22, 40, 34, 40, 15, 18, 12, 15, 30, 24],
            listeler={"Strateji Kategorisi": ["Personel", "Lokasyon", "Teknoloji", "Veri",
                                               "Tedarikçi", "Finans", "Süreç"],
                      "Uygulama Durumu": ["Planlandı", "Devam", "Uygulandı", "Ertelendi"]},
            formuller={"Boşluk (saat)": '=IF(OR([RTO Hedefi (saat)]{r}="",'
                                        '[Mevcut Yetenek (saat)]{r}=""),"",'
                                        'MAX(0,[Mevcut Yetenek (saat)]{r}-[RTO Hedefi (saat)]{r}))'},
            durum_sutunu="Uygulama Durumu", bos_satir=40,
            notlar={"Değerlendirilen Seçenekler": "Sadece seçileni değil, elenenleri de yazın — "
                                                    "8.3.2 seçeneklerin belirlenmesini ister.",
                    "Boşluk (saat)": "Otomatik: Mevcut yetenek − RTO hedefi. Pozitifse strateji zorunludur."})
    return k.kaydet(cikti)


# --------------------------------------------------------------------- kaynak
def kaynak(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Kaynak Gereksinimleri Tablosu", bilgi.get("kod_kay", "İSYS-FR-06"))
    k.bilgi_sayfasi(
        aciklama=("Madde 8.3.4 gereği kaynak gereksinimleri. Standart sekiz kaynak "
                  "başlığını açıkça sayar; her başlık için satır bulunmalıdır."),
        kullanim_notu="Boş bırakılan başlık için 'uygulanabilir değil' ve gerekçe yazılmalıdır.")
    satirlar = [[b, "", "", "", "", "", "", ""] for b in KAYNAK_BASLIKLARI]
    k.sayfa("Kaynak Gereksinimleri",
            ["Kaynak Başlığı (8.3.4)", "İlgili Faaliyet No", "Normal İhtiyaç",
             "Kesinti Sırasında İhtiyaç", "Mevcut Durum", "Boşluk", "Aksiyon",
             "Sorumlu", "Termin", "Durum"],
            [r + ["", ""] for r in satirlar],
            genislikler=[36, 15, 30, 32, 28, 26, 34, 18, 12, 12],
            listeler={"Durum": ["Açık", "Devam", "Tamamlandı"]},
            durum_sutunu="Durum", bos_satir=30,
            notlar={"Kaynak Başlığı (8.3.4)": "Sekiz başlığın tamamı ele alınmalıdır: insan; bilgi ve veri; "
                                               "fiziksel altyapı; ekipman ve sarf; BİT sistemleri; ulaşım ve "
                                               "lojistik; finans; ortaklar ve tedarikçiler."})
    return k.kaydet(cikti)


# ------------------------------------------------------------------- tatbikat
def tatbikat(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yıllık Tatbikat (Alıştırma) Programı", bilgi.get("kod_tat", "İSYS-PN-04"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.5 gereği tatbikat programı ve sonuçları.",
        kullanim_notu=("'Başarı Kriteri' sütunu boş bırakılamaz — 'tatbikat yapıldı' "
                       "bir sonuç değildir, ölçülebilir kriter gerekir."))
    k.sayfa("Tatbikat Programı",
            ["Tatbikat No", "Tür", "Senaryo", "Kapsanan Plan / Faaliyet",
             "Doğrulanacak Hedef", "Başarı Kriteri", "Katılımcılar", "Gözlemci",
             "Planlanan Tarih", "Gerçekleşen Tarih", "Sonuç (kritere göre)",
             "Tespit Edilen Boşluklar", "Açılan DÖF No", "Rapor No", "Durum"],
            [], genislikler=[11, 20, 40, 30, 34, 34, 26, 18, 15, 15, 26, 40, 14, 12, 12],
            listeler={"Tür": ["Masa başı (tabletop)", "Çağrı ağacı testi",
                              "Teknik kurtarma testi", "Simülasyon", "Tam ölçekli"],
                      "Sonuç (kritere göre)": ["Başarılı", "Kısmen başarılı", "Başarısız"],
                      "Durum": ["Planlandı", "Devam", "Tamamlandı", "Ertelendi"]},
            durum_sutunu="Durum", bos_satir=25,
            notlar={"Başarı Kriteri": "Ölçülebilir olmalı: 'RTO 4 saat hedefine ulaşıldı' gibi.",
                    "Tür": "Yıl içinde en az iki farklı tür uygulanması beklenir."})
    k.sayfa("Değerlendirme (8.6)",
            ["Sıra", "Değerlendirme Konusu", "Tarih", "Yöntem", "Bulgular",
             "Güncelleme Gerekti mi", "Aksiyon", "Sorumlu", "Termin", "Durum"],
            [[i + 1, konu, "", "", "", "", "", "", "", ""] for i, konu in enumerate([
                "Planların güncelliği (organizasyon/sistem/tedarikçi değişiklikleri)",
                "İletişim listelerinin güncelliği",
                "BIA'daki MTPD/RTO/RPO değerlerinin geçerliliği",
                "Tatbikat bulgularının kapatılma durumu",
                "Gerçek kesinti yaşandıysa planların performansı",
                "Kaynak gereksinimlerinin karşılanma durumu",
            ])],
            genislikler=[7, 52, 13, 22, 40, 20, 34, 18, 12, 12],
            listeler={"Güncelleme Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Tamamlandı"]},
            durum_sutunu="Durum", bos_satir=10)
    return k.kaydet(cikti)


# -------------------------------------------------------------------- iletisim
def iletisim(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Acil Durum İletişim Listesi ve Çağrı Ağacı",
               bilgi.get("kod_ilt", "İSYS-FR-09"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.4.3 gereği uyarı ve iletişim kayıtları.",
        kullanim_notu=("En hızlı bayatlayan dokümandır. Üç ayda bir doğrulanmalı ve "
                       "'Son Doğrulama' sütunu güncellenmelidir. Alternatif iletişim "
                       "kanalı sütunu boş bırakılamaz — ana kanal çalışmadığında ne olacak?"))
    k.sayfa("Çağrı Ağacı",
            ["Sıra", "Rol / Görev", "Ad Soyad", "Birim", "Birincil Telefon",
             "Alternatif Telefon", "E-posta", "Alternatif İletişim Kanalı",
             "Kimi Arayacak", "Kim Tarafından Aranacak", "Yedek Kişi",
             "Yedeğin Telefonu", "Son Doğrulama Tarihi"],
            [], genislikler=[7, 26, 22, 18, 17, 17, 26, 26, 26, 26, 22, 17, 17],
            bos_satir=40)
    k.sayfa("Dış İlgili Taraflar",
            ["Sıra", "Taraf", "Kategori", "İlgili Kişi", "Telefon", "E-posta",
             "Hangi Durumda İletişim", "Kim İletişim Kuracak", "Bildirim Süresi",
             "Kullanılacak Şablon", "Son Doğrulama"],
            [["", "", "Yetkili merci", "", "", "", "", "", "", "", ""],
             ["", "", "Müşteri", "", "", "", "", "", "", "", ""],
             ["", "", "Tedarikçi", "", "", "", "", "", "", "", ""],
             ["", "", "Medya", "", "", "", "", "", "", "", ""],
             ["", "", "Sigorta", "", "", "", "", "", "", "", ""]],
            genislikler=[7, 28, 18, 22, 17, 26, 34, 22, 15, 26, 15],
            listeler={"Kategori": ["Yetkili merci", "Müşteri", "Tedarikçi", "Medya",
                                    "Sigorta", "Hissedar", "Kamu", "Diğer"]},
            bos_satir=30)
    return k.kaydet(cikti)


# --------------------------------------------------------------------- hedefler
def hedefler(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "İş Sürekliliği Hedefleri ve İzleme Tablosu",
               bilgi.get("kod_hedef", "İSYS-FR-04"))
    k.bilgi_sayfasi(
        aciklama="Madde 6.2.2 (hedefler) ve 9.1 (izleme ve ölçme) kapsamındaki kayıt.",
        kullanim_notu="Sonuçlar Yönetimin Gözden Geçirmesi girdisidir (9.3.2).")
    k.sayfa("Hedefler",
            ["Hedef No", "İş Sürekliliği Hedefi", "Politika İlkesiyle İlişkisi",
             "İlgili Faaliyet / Plan", "Gösterge (KPI)", "Ölçüm Yöntemi",
             "Başlangıç Değeri", "Hedef Değer", "Ölçüm Sıklığı", "Sorumlu",
             "Gerekli Kaynak", "Termin", "Q1", "Q2", "Q3", "Q4",
             "Yıl Sonu Durumu", "Değerlendirme", "Durum"],
            [], genislikler=[10, 38, 24, 24, 26, 26, 14, 12, 14, 18, 20, 12, 8, 8, 8, 8, 15, 34, 12],
            listeler={"Ölçüm Sıklığı": ["Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Açık", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=20,
            notlar={"Gösterge (KPI)": "Örnek: 'kritik faaliyet A için RTO hedefine tatbikatta ulaşma oranı ≥ %90'."})
    return k.kaydet(cikti)


# ------------------------------------------------------------------- ortak set
def dof(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Uygunsuzluk ve Düzeltici Faaliyet Takip Formu",
               bilgi.get("kod_dof", "İSYS-FR-12"))
    k.bilgi_sayfasi(aciklama="Madde 10.1 kapsamındaki kayıt.",
                    kullanim_notu="Kök neden, benzer uygunsuzluk taraması ve etkinlik doğrulaması zorunludur.")
    k.sayfa("DÖF Takip",
            ["DÖF No", "Tespit Tarihi", "Kaynak", "Uygunsuzluk Tanımı", "İlgili Madde",
             "Sınıf", "Acil Düzeltme", "Kök Neden Analizi (yöntem + sonuç)",
             "Benzer Uygunsuzluk Taraması", "Düzeltici Faaliyet", "Sorumlu", "Termin",
             "Tamamlanma", "Etkinlik Doğrulama Yöntemi", "Doğrulama Tarihi",
             "Doğrulayan", "İSYS Değişikliği Gerekti mi", "Durum"],
            [], genislikler=[10, 13, 22, 44, 14, 12, 34, 44, 30, 44, 16, 12, 14, 34, 16, 16, 24, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "Tatbikat", "Gerçek kesinti",
                                  "YGG", "İzleme/ölçme", "8.6 değerlendirmesi", "Diğer"],
                      "Sınıf": ["Majör", "Minör", "Gözlem"],
                      "İSYS Değişikliği Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40)
    k.ozet_sayfasi("Özet", "DÖF Takip", "Durum", ["Açık", "Devam", "Kapalı"])
    return k.kaydet(cikti)


def dokuman_listesi(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Doküman Ana Listesi", bilgi.get("kod_dok", "İSYS-LS-04"))
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
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Ortam": "İş sürekliliği planlarının BASILI bir kopyasının olması beklenir — "
                             "sistemler çöktüğünde elektronik plan okunamaz."})
    k.sayfa("Dış Kaynaklı Dokümanlar",
            ["Sıra", "Doküman Adı", "Kaynak", "Sürüm / Tarih", "Neden Gerekli",
             "Erişim Yeri", "Sorumlu", "Güncellik Kontrolü"],
            [["1", "TS EN ISO 22301", "TSE", "2019", "Yönetim sistemi gerekliliği",
              "[DOLDURULACAK]", "İSYS Yöneticisi", "Yıllık"]],
            genislikler=[7, 40, 24, 16, 30, 26, 18, 18], bos_satir=20)
    return k.kaydet(cikti)


def yetkinlik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yetkinlik ve Eğitim Matrisi", bilgi.get("kod_yet", "İSYS-LS-07"))
    k.bilgi_sayfasi(aciklama="Madde 7.2 ve 7.3 kapsamındaki kayıt.",
                    kullanim_notu="Kesinti anındaki rol bilgisi ayrı sütunda izlenir (7.3).")
    k.sayfa("Yetkinlik Matrisi",
            ["Sıra", "Rol / Unvan", "Kişi", "İSYS'deki Görevi", "Kesinti Anındaki Rolü",
             "Gerekli Yetkinlik", "Yetkinlik Kanıtı", "Mevcut Durum", "Boşluk",
             "Planlanan Eğitim", "Termin", "Tamamlanma", "Etkinlik Değerlendirmesi",
             "Rol Kartı Teslim", "Sonraki Tazeleme"],
            [], genislikler=[7, 22, 20, 26, 30, 30, 34, 14, 24, 28, 12, 14, 30, 15, 16],
            listeler={"Mevcut Durum": ["Yeterli", "Kısmen", "Yetersiz"],
                      "Rol Kartı Teslim": ["Evet", "Hayır"]},
            bos_satir=40)
    return k.kaydet(cikti)


def zincir_kontrolu(bilgi: dict, cikti: str) -> str:
    """22301'e ozgu: BIA -> RTO -> strateji -> kaynak -> plan zincirinin kapali olup
    olmadigini gosterir. Denetcinin yapacagi testi kullanici onceden yapmis olur."""
    k = _kayit(bilgi, "BIA-Strateji-Plan Zincir Kontrolü",
               bilgi.get("kod_zin", "İSYS-FR-16"))
    k.bilgi_sayfasi(
        aciklama=("Denetçi rastgele bir öncelikli faaliyet seçip BIA'dan plana kadar "
                  "zinciri takip eder. Bu tablo o testi önceden yapar."),
        kullanim_notu="Her satırda 'Zincir Durumu' OK olmalıdır. Boş halka = bulgu.")
    k.sayfa("Zincir Kontrolü",
            ["Faaliyet No", "Faaliyet", "MTPD", "RTO", "BIA'da var mı",
             "Risk değerlendirmesinde var mı", "Strateji tanımlı mı", "Kaynak planlanmış mı",
             "Plan içinde ele alınmış mı", "Tatbikat edilmiş mi", "Zincir Durumu", "Eksik Halka", "Aksiyon"],
            [], genislikler=[11, 36, 10, 10, 15, 26, 18, 20, 24, 18, 14, 26, 34],
            listeler={x: ["Evet", "Hayır", "Kısmen"] for x in
                      ["BIA'da var mı", "Risk değerlendirmesinde var mı", "Strateji tanımlı mı",
                       "Kaynak planlanmış mı", "Plan içinde ele alınmış mı", "Tatbikat edilmiş mi"]},
            formuller={"Zincir Durumu":
                       '=IF(COUNTIF([BIA\'da var mı]{r}:[Tatbikat edilmiş mi]{r},"Evet")=6,"OK",'
                       'IF(COUNTBLANK([BIA\'da var mı]{r}:[Tatbikat edilmiş mi]{r})=6,"","EKSİK"))'},
            bos_satir=50,
            notlar={"Zincir Durumu": "Altı halkanın tamamı 'Evet' ise OK. Aksi hâlde eksik halkayı yazın."})
    return k.kaydet(cikti)


URETICILER = {
    "bia": (bia, "ISYS-FR-02 Is Etki Analizi (BIA).xlsx"),
    "risk": (risk, "ISYS-FR-03 Sureklilik Risk Degerlendirmesi.xlsx"),
    "strateji": (strateji, "ISYS-FR-05 Strateji ve Bosluk Analizi.xlsx"),
    "kaynak": (kaynak, "ISYS-FR-06 Kaynak Gereksinimleri.xlsx"),
    "tatbikat": (tatbikat, "ISYS-PN-04 Yillik Tatbikat Programi.xlsx"),
    "iletisim": (iletisim, "ISYS-FR-09 Acil Durum Iletisim Listesi.xlsx"),
    "hedef": (hedefler, "ISYS-FR-04 Is Surekliligi Hedefleri.xlsx"),
    "dof": (dof, "ISYS-FR-12 DOF Takip Formu.xlsx"),
    "dokuman": (dokuman_listesi, "ISYS-LS-04 Dokuman Ana Listesi.xlsx"),
    "yetkinlik": (yetkinlik, "ISYS-LS-07 Yetkinlik ve Egitim Matrisi.xlsx"),
    "zincir": (zincir_kontrolu, "ISYS-FR-16 Zincir Kontrolu.xlsx"),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="ISYS Excel kayitlarini uretir.")
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
