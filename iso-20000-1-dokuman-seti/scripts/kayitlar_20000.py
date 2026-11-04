#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_20000.py — HYYS'nin tekrar eden Excel kayitlarini uretir.

Bu standartta en degerli iki cikti: hizmet katalogu (zincirin basi) ve
SLA-OLA-UC hizalama tablosu (celiskileri gorunur kilar). Ikisi de elle
kuruldugunda tutarsiz cikar; burada iskelet ve kontrol formulleri hazir gelir.

Kullanim:
    python3 kayitlar_20000.py --kurulus "ACME A.S." --cikti "/yol/03_Katalog" \\
        --tarih 2026-08-11 --hangi katalog,sla,hizalama,cmdb,olay,problem,degisiklik,\\
surum,kapasite,tedarikci,hedef,iyilestirme,dof,zincir,dokuman,yetkinlik
"""

from __future__ import annotations

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

STANDART = "TS ISO/IEC 20000-1 (ISO/IEC 20000-1:2018)"
ONCELIKLER = ["P1", "P2", "P3", "P4"]


def _kayit(bilgi: dict, ad: str, kod: str) -> YSKayit:
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=kod,
                   standart=STANDART, sistem="HYYS",
                   revizyon=bilgi.get("revizyon", "00"), tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""), onaylayan=bilgi.get("onaylayan", ""))


# -------------------------------------------------------------------- katalog
def katalog(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Hizmet Kataloğu", bilgi.get("kod_kat", "HYYS-LS-01"))
    k.bilgi_sayfasi(
        aciklama=("Madde 8.2.4 gereği hizmet kataloğu. HYYS'nin zincir başlangıcıdır: "
                  "katalogdaki her hizmetin bir SLA'sı, her SLA hedefinin bir ölçüm "
                  "kaynağı olmalıdır."),
        kullanim_notu=("Açıklama sütunu MÜŞTERİNİN anlayacağı dilde yazılır — teknik "
                       "bileşen adı değil, hizmet adı. Altı ayda bir gözden geçirilir."))
    k.sayfa("Hizmet Kataloğu",
            ["Hizmet Kodu", "Hizmet Adı", "Kategori", "Açıklama (müşteri dili)",
             "Hedef Kullanıcı Grubu", "Hizmet Sahibi", "Teknik Sahip",
             "Bağımlı KÖ'ler", "Bağımlı Hizmetler", "Tedarikçi Bağımlılığı",
             "Hizmet Saatleri", "Destek Saatleri", "İlgili SLA", "Kritiklik",
             "Ücretlendirme", "Devreye Alma Tarihi", "Durum", "Son Gözden Geçirme"],
            [], genislikler=[12, 30, 18, 46, 24, 20, 20, 28, 24, 26, 18, 18, 16, 12, 20, 16, 12, 16],
            listeler={"Kritiklik": ["Kritik", "Yüksek", "Orta", "Düşük"],
                      "Durum": ["Aktif", "Planlanan", "Emekliye ayrılıyor", "Kapalı"],
                      "Kategori": ["Altyapı", "Uygulama", "İletişim", "Son kullanıcı desteği",
                                    "Güvenlik", "Veri/Raporlama", "Diğer"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Açıklama (müşteri dili)": "'Exchange Server kümesi' bir hizmet değildir; "
                                                "'Kurumsal E-posta ve Takvim' hizmettir.",
                    "Kritiklik": "SLA seviyesini ve süreklilik önceliğini belirler. Boş bırakılamaz."})
    k.ozet_sayfasi("Özet", "Hizmet Kataloğu", "Kritiklik", ["Kritik", "Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)


# ------------------------------------------------------------------------ SLA
def sla(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "SLA Kayıt Listesi ve Hedef Tablosu", bilgi.get("kod_sla", "HYYS-LS-04"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.3.3 gereği hizmet seviyesi anlaşmaları ve hedefleri.",
        kullanim_notu=("Her hedef beş bileşeni taşımalıdır: metrik, eşik, ölçüm dönemi, "
                       "ölçüm kaynağı, istisna. Biri eksikse hedef ölçülemez ve bulgu üretir."))
    k.sayfa("SLA Listesi",
            ["SLA No", "SLA Adı", "Müşteri / Taraf", "Kapsanan Hizmetler",
             "Hizmet Saatleri", "Yürürlük Başlangıcı", "Yürürlük Bitişi",
             "Gözden Geçirme Sıklığı", "Son Gözden Geçirme", "İmza Durumu",
             "SLA Sahibi", "Yükseltme (Escalation) Yolu", "Durum"],
            [], genislikler=[10, 30, 24, 34, 18, 17, 15, 18, 16, 14, 18, 34, 12],
            listeler={"İmza Durumu": ["İmzalı", "Taslak", "Yenilenecek"],
                      "Gözden Geçirme Sıklığı": ["Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Aktif", "Taslak", "Sona erdi"]},
            durum_sutunu="Durum", bos_satir=20)
    k.sayfa("Hedefler",
            ["Hedef No", "SLA No", "Hizmet Kodu", "Hedef Adı", "Metrik", "Eşik",
             "Ölçüm Dönemi", "Ölçüm Kaynağı", "İstisnalar", "Sorumlu",
             "Raporlama Sıklığı", "İlgili OLA/UC", "Son Dönem Gerçekleşen",
             "Uyum Durumu", "İhlal Nedeni / Aksiyon"],
            [], genislikler=[10, 10, 12, 30, 26, 14, 15, 30, 34, 18, 16, 20, 18, 14, 40],
            listeler={"Ölçüm Dönemi": ["Günlük", "Haftalık", "Aylık", "Üç aylık"],
                      "Uyum Durumu": ["Uygun", "İhlal", "Ölçülmedi"]},
            durum_sutunu="Uyum Durumu", bos_satir=50,
            notlar={"Eşik": "Sayısal olmalı: '≥ %99,5', '≤ 4 saat'. 'Yüksek' bir eşik değildir.",
                    "Ölçüm Kaynağı": "Hangi sistemden, hangi raporla ölçüldüğü yazılmalı — "
                                      "denetçi kanıtı buradan ister.",
                    "İstisnalar": "Planlı bakım pencereleri gibi hariç tutulan durumlar."})
    k.sayfa("Öncelik Matrisi",
            ["Etki \\ Aciliyet", "Yüksek", "Orta", "Düşük"],
            [["Yüksek (tüm kullanıcılar / kritik hizmet)", "P1", "P2", "P3"],
             ["Orta (birim / önemli hizmet)", "P2", "P3", "P4"],
             ["Düşük (tek kullanıcı / yardımcı hizmet)", "P3", "P4", "P4"]],
            genislikler=[44, 14, 14, 14])
    k.sayfa("Öncelik Hedefleri",
            ["Öncelik", "İlk Müdahale Hedefi", "Çözüm Hedefi", "Bilgilendirme Sıklığı",
             "Yükseltme Süresi", "Kapsanan Saatler"],
            [[p, "[DOLDURULACAK]", "[DOLDURULACAK]", "[DOLDURULACAK]",
              "[DOLDURULACAK]", "[DOLDURULACAK]"] for p in ONCELIKLER],
            genislikler=[12, 24, 20, 24, 20, 22],
            notlar={"Öncelik": "Bu tablodaki hedefler SLA'daki hedeflerle AYNI olmalıdır."})
    return k.kaydet(cikti)


# ------------------------------------------------------------------- hizalama
def hizalama(bilgi: dict, cikti: str) -> str:
    """SLA-OLA-UC celiski taramasi. Bu standarda ozgu, denetimde cok ise yarar."""
    k = _kayit(bilgi, "SLA / OLA / UC Hizalama Tablosu", bilgi.get("kod_hiz", "HYYS-LS-08"))
    k.bilgi_sayfasi(
        aciklama=("Müşteriye verilen söz (SLA) ile iç birim anlaşmaları (OLA) ve "
                  "tedarikçi sözleşmeleri (UC) arasındaki tutarlılığı gösterir."),
        kullanim_notu=("'Hizalama Kontrolü' otomatiktir: OLA veya UC süresi SLA "
                       "süresinden büyükse ÇELİŞKİ yazar. Çelişki, denetçinin severek "
                       "yakaladığı bulgudur — SLA imzalanmadan önce kapatılmalıdır."))
    k.sayfa("Hizalama",
            ["Sıra", "Hizmet Kodu", "Hedef", "Öncelik", "SLA Süresi (saat)",
             "OLA Sahibi (iç birim)", "OLA Süresi (saat)", "UC / Tedarikçi",
             "UC Süresi (saat)", "Toplam İç+Dış (saat)", "Hizalama Kontrolü",
             "Tampon (saat)", "Not / Aksiyon"],
            [], genislikler=[7, 12, 30, 10, 16, 24, 17, 26, 15, 19, 18, 13, 40],
            listeler={"Öncelik": ONCELIKLER},
            formuller={
                "Toplam İç+Dış (saat)":
                    '=IF(AND([OLA Süresi (saat)]{r}="",[UC Süresi (saat)]{r}=""),"",'
                    'N([OLA Süresi (saat)]{r})+N([UC Süresi (saat)]{r}))',
                "Hizalama Kontrolü":
                    '=IF(OR([SLA Süresi (saat)]{r}="",[Toplam İç+Dış (saat)]{r}=""),"",'
                    'IF([Toplam İç+Dış (saat)]{r}<=[SLA Süresi (saat)]{r},"OK","ÇELİŞKİ"))',
                "Tampon (saat)":
                    '=IF(OR([SLA Süresi (saat)]{r}="",[Toplam İç+Dış (saat)]{r}=""),"",'
                    '[SLA Süresi (saat)]{r}-[Toplam İç+Dış (saat)]{r})',
            },
            bos_satir=40,
            notlar={"Hizalama Kontrolü": "OK = iç ve dış süreler SLA'ya sığıyor. "
                                          "ÇELİŞKİ = SLA tutulamaz, sözleşme veya hedef düzeltilmeli."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- CMDB
def cmdb(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Konfigürasyon Öğeleri (CMDB)", bilgi.get("kod_cmdb", "HYYS-LS-03"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.2.6 gereği konfigürasyon bilgisi.",
        kullanim_notu=("'Son Doğrulama Tarihi' ve 'Doğrulayan' sütunları 8.2.6'nın "
                       "doğrulama gerekliliğinin tek kanıtıdır — hiç doğrulanmamış bir "
                       "CMDB bulgu üretir. Kritik KÖ'ler üç ayda bir doğrulanır."))
    k.sayfa("CMDB",
            ["KÖ No", "KÖ Adı", "Tip", "Kategori", "Sahip", "Durum", "Sürüm",
             "Lokasyon / Ortam", "İlişkili Hizmet(ler)", "Üst KÖ", "Alt KÖ'ler",
             "Bağımlılıklar", "Tedarikçi", "Garanti / Destek Bitiş",
             "Son Değişiklik No", "Son Doğrulama Tarihi", "Doğrulayan", "Doğrulama Sonucu"],
            [], genislikler=[11, 30, 16, 18, 18, 12, 12, 22, 28, 14, 22, 28, 20, 18, 16, 17, 16, 18],
            listeler={"Tip": ["Donanım", "Yazılım", "Ağ", "Veritabanı", "Bulut hizmeti",
                              "Dokümantasyon", "Lisans", "Hizmet", "Diğer"],
                      "Durum": ["Aktif", "Stokta", "Bakımda", "Emekli", "Planlanan"],
                      "Doğrulama Sonucu": ["Doğru", "Düzeltildi", "Doğrulanmadı"]},
            durum_sutunu="Durum", bos_satir=60)
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- olay
def olay(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Olay ve Hizmet Talebi Kayıt Defteri", bilgi.get("kod_olay", "HYYS-FR-02"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.6.1 (olay) ve 8.6.2 (hizmet talebi) kayıtları.",
        kullanim_notu=("Olay ile talep AYRI kayıt tipidir; 'Kayıt Tipi' sütunuyla "
                       "ayrılır ve metrikleri ayrı raporlanır. Büyük olaylar ayrıca "
                       "işaretlenir ve olay sonrası inceleme gerektirir."))
    k.sayfa("Olay ve Talep",
            ["Kayıt No", "Kayıt Tipi", "Açılış Tarihi/Saati", "Kanal", "Bildiren",
             "Etkilenen Hizmet", "Etkilenen KÖ", "Özet", "Etki", "Aciliyet",
             "Öncelik", "Büyük Olay mı", "Atanan Grup", "Atanan Kişi",
             "İlk Müdahale Zamanı", "İlk Müdahale SLA", "Geçici Çözüm",
             "Çözüm Açıklaması", "Kapanış Tarihi/Saati", "Çözüm Süresi (saat)",
             "Çözüm SLA", "İlgili Problem No", "İlgili Değişiklik No",
             "Kullanıcı Memnuniyeti", "Durum"],
            [], genislikler=[11, 14, 18, 14, 20, 24, 20, 44, 10, 11, 10, 13, 18, 18,
                             18, 15, 34, 44, 18, 16, 13, 16, 18, 17, 12],
            listeler={"Kayıt Tipi": ["Olay", "Hizmet Talebi"],
                      "Kanal": ["Servis masası", "E-posta", "Telefon", "Portal", "İzleme sistemi", "Otomatik"],
                      "Etki": ["Yüksek", "Orta", "Düşük"], "Aciliyet": ["Yüksek", "Orta", "Düşük"],
                      "Öncelik": ONCELIKLER, "Büyük Olay mı": ["Evet", "Hayır"],
                      "İlk Müdahale SLA": ["Uygun", "İhlal"], "Çözüm SLA": ["Uygun", "İhlal"],
                      "Durum": ["Açık", "Devam", "Beklemede", "Çözüldü", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=80,
            notlar={"Kayıt Tipi": "Olay = planlanmamış kesinti/kalite düşüşü. "
                                   "Talep = standart, önceden onaylı istek. Metrikleri ayrıdır.",
                    "Büyük Olay mı": "Evet ise olay sonrası inceleme ve problem kaydı açılması beklenir."})
    k.ozet_sayfasi("Özet", "Olay ve Talep", "Öncelik", ONCELIKLER)
    return k.kaydet(cikti)


# -------------------------------------------------------------------- problem
def problem(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Problem Kayıt Defteri ve Bilinen Hatalar",
               bilgi.get("kod_prob", "HYYS-FR-03"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.6.3 gereği problem yönetimi kayıtları.",
        kullanim_notu=("Problem, olayın kök nedenidir — olay kaydıyla karıştırılmamalıdır. "
                       "Kök nedeni bulunmuş ama kalıcı çözümü uygulanmamış problemler "
                       "'Bilinen Hata' sayfasına geçer ve hizmet masası oradan yararlanır."))
    k.sayfa("Problemler",
            ["Problem No", "Açılış Tarihi", "Kaynak", "İlgili Olay No(ları)",
             "Etkilenen Hizmet", "Problem Tanımı", "Öncelik", "Atanan",
             "Analiz Yöntemi", "Kök Neden", "Geçici Çözüm (workaround)",
             "Kalıcı Çözüm", "İlgili Değişiklik No", "Bilinen Hata mı",
             "Kapanış Tarihi", "Tekrar Etti mi", "Durum"],
            [], genislikler=[11, 13, 22, 22, 24, 44, 10, 18, 22, 44, 40, 40, 18, 15, 14, 14, 12],
            listeler={"Kaynak": ["Tekrarlayan olay", "Büyük olay", "Proaktif analiz",
                                  "Trend analizi", "Tedarikçi bildirimi"],
                      "Öncelik": ONCELIKLER,
                      "Analiz Yöntemi": ["5 Neden", "Balık kılçığı (Ishikawa)",
                                          "Hata ağacı", "Kronoloji analizi", "Diğer"],
                      "Bilinen Hata mı": ["Evet", "Hayır"],
                      "Tekrar Etti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Analizde", "Çözüm bekliyor", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Analiz Yöntemi": "Yöntem adı boş bırakılamaz — 'araştırıldı' bir yöntem değildir.",
                    "Tekrar Etti mi": "Kapatılan problemin tekrarlaması, kök nedenin "
                                       "yanlış tespit edildiğini gösterir ve DÖF gerektirir."})
    k.sayfa("Bilinen Hatalar",
            ["BH No", "İlgili Problem No", "Etkilenen Hizmet", "Belirti (kullanıcı ne görür)",
             "Kök Neden", "Geçici Çözüm Adımları", "Kalıcı Çözüm Planı",
             "Beklenen Kapanış", "Yayımlandığı Yer", "Son Güncelleme", "Durum"],
            [], genislikler=[10, 16, 24, 44, 40, 50, 40, 16, 24, 15, 12],
            listeler={"Durum": ["Aktif", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=30,
            notlar={"Belirti (kullanıcı ne görür)": "Hizmet masası bu sütundan arama yapar — "
                                                     "kullanıcının tarif edeceği dille yazın."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------- degisiklik
def degisiklik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Değişiklik Talep ve CAB Kayıt Defteri", bilgi.get("kod_deg", "HYYS-FR-05"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.5.1 gereği değişiklik yönetimi kayıtları.",
        kullanim_notu=("Acil değişiklikler için ayrı onay mekanizması standardın açık "
                       "gereğidir. Acil değişiklik oranının yüksekliği (>%10) denetimde "
                       "'plansız çalışma' sorusuna yol açar."))
    k.sayfa("Değişiklikler",
            ["Değişiklik No", "Talep Tarihi", "Talep Eden", "Değişiklik Tipi",
             "Etkilenen Hizmet(ler)", "Etkilenen KÖ'ler", "Değişiklik Özeti",
             "Gerekçe", "Risk Değerlendirmesi", "Etki Değerlendirmesi",
             "Kaynak İhtiyacı", "Test Planı", "Geri Alma (Rollback) Planı",
             "Onay Mercii", "Onay Tarihi", "Planlanan Uygulama",
             "Gerçekleşen Uygulama", "İlgili Sürüm No", "Sonuç",
             "Uygulama Sonrası Gözden Geçirme", "Başarısızlık Nedeni", "Durum"],
            [], genislikler=[13, 13, 18, 15, 26, 24, 44, 34, 34, 30, 22, 30, 34,
                             18, 14, 17, 17, 15, 14, 34, 34, 12],
            listeler={"Değişiklik Tipi": ["Standart (önceden onaylı)", "Normal", "Acil"],
                      "Onay Mercii": ["CAB", "Süreç sahibi", "Acil CAB", "Otomatik (standart)"],
                      "Sonuç": ["Başarılı", "Kısmen başarılı", "Başarısız", "Geri alındı"],
                      "Durum": ["Talep", "Değerlendirmede", "Onaylandı", "Reddedildi",
                                 "Uygulandı", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=50,
            notlar={"Geri Alma (Rollback) Planı": "Boş bırakılamaz. 'Geri alınamaz' yazılacaksa "
                                                   "gerekçesi ve alternatif kurtarma yolu belirtilmeli.",
                    "Değişiklik Tipi": "Acil değişiklik ayrı onay mekanizmasıyla yönetilir (8.5.1)."})
    k.ozet_sayfasi("Özet", "Değişiklikler", "Sonuç",
                   ["Başarılı", "Kısmen başarılı", "Başarısız", "Geri alındı"])
    return k.kaydet(cikti)


def surum(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Sürüm ve Dağıtım Kayıt Defteri", bilgi.get("kod_sur", "HYYS-FR-12"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.5.3 gereği sürüm ve dağıtım kayıtları.",
        kullanim_notu="Değişiklik kaydından ayrıdır: değişiklik NEYİN onaylandığını, "
                      "sürüm NASIL canlıya alındığını yönetir.")
    k.sayfa("Sürümler",
            ["Sürüm No", "Sürüm Adı", "Tip", "İçerdiği Değişiklik No(ları)",
             "Etkilenen Hizmet(ler)", "Paket İçeriği", "Test Ortamı Sonucu",
             "Kabul Kriterleri", "Kabul Eden", "Dağıtım Planı", "Geri Alma Planı",
             "Planlanan Tarih", "Gerçekleşen Tarih", "Dağıtım Sonrası Doğrulama",
             "Sonuç", "Oluşan Olay No(ları)", "Durum"],
            [], genislikler=[11, 26, 14, 24, 26, 40, 30, 34, 18, 34, 34, 15, 15, 34, 14, 20, 12],
            listeler={"Tip": ["Büyük (major)", "Küçük (minor)", "Acil düzeltme (hotfix)"],
                      "Sonuç": ["Başarılı", "Kısmen başarılı", "Geri alındı", "Başarısız"],
                      "Durum": ["Planlanan", "Testte", "Onaylandı", "Dağıtıldı", "Geri alındı"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Oluşan Olay No(ları)": "Dağıtım sonrası oluşan olaylar burada izlenir — "
                                             "sürüm kalitesinin en doğrudan göstergesidir."})
    return k.kaydet(cikti)


# -------------------------------------------------------------------- kapasite
def kapasite(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Kapasite Planı ve Trend Tablosu", bilgi.get("kod_kap", "HYYS-FR-10"))
    k.bilgi_sayfasi(
        aciklama="Madde 8.4.3 gereği kapasite yönetimi kayıtları.",
        kullanim_notu="Kapasite yönetimi insan, teknik ve bilgi kaynaklarını kapsar — "
                      "sadece disk/CPU değil.")
    k.sayfa("Kapasite İzleme",
            ["Sıra", "Kaynak / Bileşen", "Kaynak Tipi", "İlgili Hizmet", "Metrik",
             "Birim", "Mevcut Kullanım", "Toplam Kapasite", "Kullanım Oranı",
             "Uyarı Eşiği", "Kritik Eşik", "Eşik Durumu", "Trend (aylık %)",
             "Doluluk Tahmini (ay)", "Planlanan Aksiyon", "Sorumlu", "Termin", "Durum"],
            [], genislikler=[7, 28, 16, 24, 24, 12, 16, 17, 15, 13, 13, 14, 15, 19, 34, 18, 12, 12],
            listeler={"Kaynak Tipi": ["İnsan", "Teknik (donanım)", "Teknik (yazılım/lisans)",
                                       "Ağ/bant genişliği", "Depolama", "Bilgi/veri", "Finansal"],
                      "Durum": ["İzleniyor", "Aksiyon gerekli", "Aksiyon alındı"]},
            formuller={"Kullanım Oranı":
                       '=IF(OR([Mevcut Kullanım]{r}="",[Toplam Kapasite]{r}=""),"",'
                       '[Mevcut Kullanım]{r}/[Toplam Kapasite]{r})',
                       "Eşik Durumu":
                       '=IF([Kullanım Oranı]{r}="","",IF([Kullanım Oranı]{r}>=[Kritik Eşik]{r},'
                       '"KRİTİK",IF([Kullanım Oranı]{r}>=[Uyarı Eşiği]{r},"UYARI","Normal")))'},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Uyarı Eşiği": "Ondalık girin (0,75 = %75).",
                    "Doluluk Tahmini (ay)": "Trend sürerse kapasitenin ne zaman dolacağı — "
                                             "8.4.3 tahminleme gerekliliğinin kanıtıdır."})
    return k.kaydet(cikti)


# ------------------------------------------------------------------ tedarikci
def tedarikci(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Tedarikçi ve Dış Proses Envanteri", bilgi.get("kod_ted", "HYYS-LS-05"))
    k.bilgi_sayfasi(
        aciklama=("Madde 8.3.4 (tedarikçi yönetimi) ve 8.2.3 (diğer taraflarca işletilen "
                  "prosesler) kayıtları."),
        kullanim_notu=("8.2.3 sayfası kapsam kararını doğrudan etkiler: bir proses üzerinde "
                       "yönetişim gösterilemiyorsa ilgili hizmet kapsama alınmamalıdır."))
    k.sayfa("Tedarikçiler",
            ["Sıra", "Tedarikçi", "Sağlanan Hizmet/Ürün", "Kritiklik",
             "İlgili Hizmet Kodu", "Sözleşme No", "Sözleşme Başlangıç", "Bitiş",
             "UC Hedefleri (özet)", "Performans Ölçüm Yöntemi", "Ölçüm Sıklığı",
             "Son Dönem Performansı", "Yaptırım / Teşvik Maddesi",
             "İlişki Sahibi", "Son Gözden Geçirme", "Durum"],
            [], genislikler=[7, 26, 34, 12, 18, 16, 17, 14, 40, 30, 15, 20, 30, 18, 16, 12],
            listeler={"Kritiklik": ["Kritik", "Yüksek", "Orta", "Düşük"],
                      "Ölçüm Sıklığı": ["Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Aktif", "Yenilenecek", "Sona erdi"]},
            durum_sutunu="Durum", bos_satir=30)
    k.sayfa("Diğer Taraf Prosesleri (8.2.3)",
            ["Sıra", "HYYS Prosesi", "İşleten Taraf", "Sözleşme / Anlaşma",
             "Arayüz Tanımı (sorumluluk sınırı)", "İzleme Yöntemi", "Ölçüm Sıklığı",
             "Performans Hedefi", "Müdahale Mekanizması", "Yönetişim Kanıtı",
             "Sorumlu", "Son Gözden Geçirme"],
            [], genislikler=[7, 28, 24, 24, 44, 30, 15, 30, 34, 30, 18, 16],
            bos_satir=20,
            notlar={"Yönetişim Kanıtı": "Kuruluş HYYS'nin bütününün yönetişiminden sorumludur "
                                         "ve bunu devredemez. Kanıt gösterilemiyorsa hizmet "
                                         "kapsam dışında bırakılmalıdır."})
    return k.kaydet(cikti)


# ----------------------------------------------------------------- ortak set
def hedefler(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Hizmet Yönetimi Hedefleri ve İzleme Tablosu",
               bilgi.get("kod_hedef", "HYYS-FR-04"))
    k.bilgi_sayfasi(aciklama="Madde 6.2 ve 9.1 kapsamındaki kayıt.")
    k.sayfa("Hedefler",
            ["Hedef No", "Hedef", "Politika İlkesiyle İlişkisi", "İlgili Hizmet/Süreç",
             "Gösterge (KPI)", "Ölçüm Yöntemi", "Başlangıç Değeri", "Hedef Değer",
             "Ölçüm Sıklığı", "Sorumlu", "Kaynak", "Termin",
             "Q1", "Q2", "Q3", "Q4", "Yıl Sonu", "Değerlendirme", "Durum"],
            [], genislikler=[10, 38, 24, 24, 26, 26, 14, 12, 14, 18, 18, 12, 8, 8, 8, 8, 13, 34, 12],
            listeler={"Ölçüm Sıklığı": ["Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Açık", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=20)
    return k.kaydet(cikti)


def iyilestirme(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "İyileştirme Kayıt Defteri (CSI Register)",
               bilgi.get("kod_csi", "HYYS-FR-09"))
    k.bilgi_sayfasi(
        aciklama="Madde 10.2 sürekli iyileştirme kaydı.",
        kullanim_notu="Kaynaklar: tetkik bulguları, problem analizleri, müşteri geri "
                      "bildirimi, SLA ihlalleri, çalışan önerileri.")
    k.sayfa("İyileştirmeler",
            ["Sıra", "Kayıt Tarihi", "Kaynak", "İyileştirme Fikri", "İlgili Hizmet/Süreç",
             "Beklenen Fayda", "Tahmini Efor", "Öncelik Puanı", "Karar",
             "Sahibi", "Termin", "Uygulanma Tarihi", "Ölçülen Sonuç", "Durum"],
            [], genislikler=[7, 13, 24, 44, 24, 34, 15, 14, 14, 18, 12, 15, 34, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "Problem analizi",
                                  "Müşteri geri bildirimi", "SLA ihlali", "YGG",
                                  "Çalışan önerisi", "Trend analizi"],
                      "Karar": ["Kabul", "Ertelendi", "Reddedildi"],
                      "Durum": ["Yeni", "Değerlendirmede", "Planlandı", "Uygulanıyor",
                                 "Tamamlandı", "İptal"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Ölçülen Sonuç": "Beklenen fayda gerçekleşti mi? Ölçülmemiş iyileştirme "
                                      "tamamlanmış sayılmaz."})
    return k.kaydet(cikti)


def dof(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Uygunsuzluk ve Düzeltici Faaliyet Takip Formu",
               bilgi.get("kod_dof", "HYYS-FR-07"))
    k.bilgi_sayfasi(aciklama="Madde 10.1 kapsamındaki kayıt.")
    k.sayfa("DÖF Takip",
            ["DÖF No", "Tespit Tarihi", "Kaynak", "Uygunsuzluk Tanımı", "İlgili Madde",
             "Sınıf", "Acil Düzeltme", "Kök Neden Analizi (yöntem + sonuç)",
             "Benzer Uygunsuzluk Taraması", "Düzeltici Faaliyet", "Sorumlu", "Termin",
             "Tamamlanma", "Etkinlik Doğrulama Yöntemi", "Doğrulama Tarihi",
             "Doğrulayan", "HYYS Değişikliği Gerekti mi", "Durum"],
            [], genislikler=[10, 13, 22, 44, 14, 12, 34, 44, 30, 44, 16, 12, 14, 34, 16, 16, 24, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "SLA ihlali", "Büyük olay",
                                  "Müşteri şikâyeti", "YGG", "İzleme/ölçme", "Diğer"],
                      "Sınıf": ["Majör", "Minör", "Gözlem"],
                      "HYYS Değişikliği Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40)
    k.ozet_sayfasi("Özet", "DÖF Takip", "Durum", ["Açık", "Devam", "Kapalı"])
    return k.kaydet(cikti)


def zincir(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Hizmet Zincir Kontrolü", bilgi.get("kod_zin", "HYYS-FR-15"))
    k.bilgi_sayfasi(
        aciklama=("Denetçi bir hizmet seçip 'hedefi ne, geçen ay tutturdunuz mu, kanıtı "
                  "nerede?' diye sorar. Bu tablo o testi önceden yapar."),
        kullanim_notu="Altı halkanın tamamı 'Evet' olmalıdır.")
    k.sayfa("Zincir Kontrolü",
            ["Hizmet Kodu", "Hizmet Adı", "Katalogda var mı", "SLA tanımlı mı",
             "OLA/UC hizalı mı", "Ölçüm kaynağı tanımlı mı", "Raporlanıyor mu",
             "CMDB'de KÖ ilişkisi var mı", "Zincir Durumu", "Eksik Halka", "Aksiyon"],
            [], genislikler=[12, 30, 16, 15, 17, 22, 17, 24, 14, 26, 40],
            listeler={x: ["Evet", "Hayır", "Kısmen"] for x in
                      ["Katalogda var mı", "SLA tanımlı mı", "OLA/UC hizalı mı",
                       "Ölçüm kaynağı tanımlı mı", "Raporlanıyor mu",
                       "CMDB'de KÖ ilişkisi var mı"]},
            formuller={"Zincir Durumu":
                       '=IF(COUNTIF([Katalogda var mı]{r}:[CMDB\'de KÖ ilişkisi var mı]{r},'
                       '"Evet")=6,"OK",IF(COUNTBLANK([Katalogda var mı]{r}:'
                       '[CMDB\'de KÖ ilişkisi var mı]{r})=6,"","EKSİK"))'},
            bos_satir=40)
    return k.kaydet(cikti)


def dokuman_listesi(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Doküman Ana Listesi", bilgi.get("kod_dok", "HYYS-LS-10"))
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
    k.sayfa("Bilgi Varlıkları (7.5.4)",
            ["Sıra", "Bilgi Varlığı", "Tip", "Konum / Sistem", "Sahibi",
             "Hedef Kitle", "Oluşturma Tarihi", "Gözden Geçirme Sıklığı",
             "Son Gözden Geçirme", "Durum"],
            [["1", "Hizmet masası bilgi bankası", "Bilgi bankası", "", "", "", "", "", "", ""],
             ["2", "Bilinen hata veritabanı", "Veritabanı", "", "", "", "", "", "", ""],
             ["3", "Çözüm makaleleri / SSS", "Makale", "", "", "", "", "", "", ""]],
            genislikler=[7, 34, 18, 26, 18, 22, 16, 20, 17, 12],
            listeler={"Durum": ["Güncel", "Gözden geçirilecek", "Eski"]},
            bos_satir=20,
            notlar={"Bilgi Varlığı": "Madde 7.5.4 (HYYS bilgisi) 20000-1'e özgüdür — "
                                      "oluşturma/gözden geçirme mekanizması tanımlı olmalıdır."})
    return k.kaydet(cikti)


def yetkinlik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yetkinlik ve Eğitim Matrisi", bilgi.get("kod_yet", "HYYS-LS-07"))
    k.bilgi_sayfasi(aciklama="Madde 7.2 ve 7.3 kapsamındaki kayıt.")
    k.sayfa("Yetkinlik Matrisi",
            ["Sıra", "Rol / Unvan", "Kişi", "Hizmet Sahipliği", "Süreç Sahipliği",
             "Gerekli Yetkinlik", "Yetkinlik Kanıtı", "Mevcut Durum", "Boşluk",
             "Planlanan Eğitim", "Termin", "Tamamlanma", "Etkinlik Değerlendirmesi",
             "Sonraki Tazeleme"],
            [], genislikler=[7, 22, 20, 26, 26, 30, 34, 14, 24, 28, 12, 14, 30, 16],
            listeler={"Mevcut Durum": ["Yeterli", "Kısmen", "Yetersiz"]},
            bos_satir=40,
            notlar={"Hizmet Sahipliği": "Bir hizmetin uçtan uca performansından sorumluluk.",
                    "Süreç Sahipliği": "Bir sürecin tüm hizmetler genelinde işleyişinden sorumluluk."})
    return k.kaydet(cikti)


URETICILER = {
    "katalog": (katalog, "HYYS-LS-01 Hizmet Katalogu.xlsx"),
    "sla": (sla, "HYYS-LS-04 SLA Kayit Listesi ve Hedefler.xlsx"),
    "hizalama": (hizalama, "HYYS-LS-08 SLA-OLA-UC Hizalama.xlsx"),
    "cmdb": (cmdb, "HYYS-LS-03 Konfigurasyon Ogeleri (CMDB).xlsx"),
    "olay": (olay, "HYYS-FR-02 Olay ve Talep Kayit Defteri.xlsx"),
    "problem": (problem, "HYYS-FR-03 Problem ve Bilinen Hatalar.xlsx"),
    "degisiklik": (degisiklik, "HYYS-FR-05 Degisiklik ve CAB Kayit Defteri.xlsx"),
    "surum": (surum, "HYYS-FR-12 Surum ve Dagitim Kayit Defteri.xlsx"),
    "kapasite": (kapasite, "HYYS-FR-10 Kapasite Plani ve Trend.xlsx"),
    "tedarikci": (tedarikci, "HYYS-LS-05 Tedarikci ve Dis Proses Envanteri.xlsx"),
    "hedef": (hedefler, "HYYS-FR-04 Hizmet Yonetimi Hedefleri.xlsx"),
    "iyilestirme": (iyilestirme, "HYYS-FR-09 Iyilestirme Kayit Defteri.xlsx"),
    "dof": (dof, "HYYS-FR-07 DOF Takip Formu.xlsx"),
    "zincir": (zincir, "HYYS-FR-15 Hizmet Zincir Kontrolu.xlsx"),
    "dokuman": (dokuman_listesi, "HYYS-LS-10 Dokuman Ana Listesi.xlsx"),
    "yetkinlik": (yetkinlik, "HYYS-LS-07 Yetkinlik ve Egitim Matrisi.xlsx"),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="HYYS Excel kayitlarini uretir.")
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
