#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kayitlar_27001.py — BGYS'nin tekrar eden Excel kayitlarini uretir.

Neden var: SoA'daki 93 kontrolu her seferinde elle yazmak hem yavas hem hataya
acik. Risk envanteri, varlik envanteri, hedef tablosu, dokuman ana listesi ve
yetkinlik matrisi de her kurulumda ayni iskeleti tasir. Bu script iskeleti
kurar; sen kurulusa ozgu satirlari doldurursun.

Kullanim:
    python3 kayitlar_27001.py --kurulus "ACME A.S." --cikti "/yol/04_Formlar" \\
        --tarih 2026-08-11 --hazirlayan "BG Yoneticisi" --onaylayan "Genel Mudur" \\
        --hangi soa,risk,varlik,hedef,dokuman,yetkinlik,dof,tetkik

Ya da Python'dan:
    from kayitlar_27001 import soa, risk_envanteri
    soa(bilgi, "/yol/BGYS-LS-02 Uygulanabilirlik Bildirgesi.xlsx",
        uygulanmayan={"7.9": "Kuruluş dışına cihaz çıkarılmamaktadır. İlgili risk "
                             "A.8.1 uç nokta kontrolleriyle karşılanmaktadır."},
        risk_eslesme={"5.15": "R-003, R-012"},
        gerekce={"5.15": "R-003 ve R-012 numaralı riskler ile 6698 sayılı KVKK "
                         "m.12 kapsamındaki veri güvenliği yükümlülüğü gereği."},
        sorumlu={"5.15": "BT Müdürü"},
        sade=True)   # sade set uretiyorsan kod eslemesi otomatik yapilir

SoA notu: standart, TUM Ek A kontrollerinin listelenmesini ve hariç tutulanlarin
gerekcesinin yazilmasini ister (6.1.3 d). Bu yuzden 93 satirin hepsi her zaman
uretilir; hicbiri silinmez, sadece "Uygulanabilir" sutunu H yapilir.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ys_xlsx import YSKayit  # noqa: E402

BURASI = os.path.dirname(os.path.abspath(__file__))
ANNEX = os.path.join(BURASI, "..", "assets", "annex_a_93.json")
STANDART = "TS EN ISO/IEC 27001:2023 (ISO/IEC 27001:2022)"


def _kayit(bilgi: dict, ad: str, kod: str) -> YSKayit:
    return YSKayit(kurulus=bilgi.get("kurulus", "[KURULUŞ]"), ad=ad, kod=kod,
                   standart=STANDART, sistem="BGYS",
                   revizyon=bilgi.get("revizyon", "00"),
                   tarih=bilgi.get("tarih", ""),
                   gizlilik=bilgi.get("gizlilik", "İç Kullanım"),
                   hazirlayan=bilgi.get("hazirlayan", ""),
                   onaylayan=bilgi.get("onaylayan", ""))


def _annex() -> list:
    with open(ANNEX, encoding="utf-8") as fh:
        return json.load(fh)


# Sade sette birlestirilen dokumanlarin kod esleme tablosu.
# Neden var: annex_a_93.json TAM set kodlarina atif verir. Sade sette PL-05,
# PL-08, PL-10, PL-11, PR-06, PR-11, PR-13, PR-14, PR-17, PR-22 uretilmez;
# bu kodlarla dolu bir SoA "var olmayan dokumana atif" bulgusu uretir.
SADE_ESLEME = {
    "BGYS-PL-05": "BGYS-PL-02", "BGYS-PL-08": "BGYS-PL-03",
    "BGYS-PL-10": "BGYS-PL-03", "BGYS-PL-11": "BGYS-PL-14",
    "BGYS-PL-12": "BGYS-PL-04", "BGYS-PL-13": "BGYS-PL-14",
    "BGYS-PR-06": "BGYS-PL-09", "BGYS-PR-11": "BGYS-PL-04",
    "BGYS-PR-12": "BGYS-PR-20", "BGYS-PR-13": "BGYS-PR-10",
    "BGYS-PR-14": "BGYS-PR-16", "BGYS-PR-15": "BGYS-PR-19",
    "BGYS-PR-17": "BGYS-PR-21", "BGYS-PR-22": "BGYS-PR-10",
}


def sade_kod(metin: str) -> str:
    """Tam set kodlarini sade set karsiliklariyla degistirir."""
    for tam, sade in SADE_ESLEME.items():
        metin = metin.replace(tam, sade)
    return metin


# ---------------------------------------------------------------------- SoA
def soa(bilgi: dict, cikti: str, uygulanmayan: dict | None = None,
        risk_eslesme: dict | None = None, gerekce: dict | None = None,
        sorumlu: dict | None = None, dokuman_ezme: dict | None = None,
        sade: bool = False) -> str:
    """Uygulanabilirlik Bildirgesi — 93 kontrolun tamami.

    uygulanmayan  : {"7.9": "hariç tutma gerekçesi"}  -> Uygulanabilir = H
    risk_eslesme  : {"5.15": "R-003, R-012"}           -> İlgili Risk No sütunu
    gerekce       : {"5.15": "R-003 ve KVKK m.12 ..."} -> Dahil Etme Gerekçesi
    sorumlu       : {"5.15": "BT Müdürü"}              -> Sorumlu sütunu
    dokuman_ezme  : {"5.15": "BGYS-PL-02 §4"}          -> Uygulayan Doküman
    sade          : True ise dokuman kodlari sade set karsiliklarina cevrilir

    Gerekce sutunu bilerek BOS BIRAKILMAZ ama jenerik de doldurulmaz:
    `gerekce` verilmeyen kontrollerde `[DOLDURULACAK: ...]` yazilir. Sebebi
    icerik-rehberi.md §6'da: "Gerekli" / "Standart geregi" gibi jenerik
    gerekce denetimde bulgu uretir. Bos gorunen alan, yanlis dolu alandan
    daha durusttur ve kapatilmasi gerektigi belli olur.
    """
    uygulanmayan = uygulanmayan or {}
    risk_eslesme = risk_eslesme or {}
    gerekce = gerekce or {}
    sorumlu = sorumlu or {}
    dokuman_ezme = dokuman_ezme or {}
    basliklar = ["Kontrol No", "Kontrol Başlığı", "Uygulanabilir (E/H)",
                 "Dahil Etme Gerekçesi", "İlgili Risk No", "Uygulama Durumu",
                 "Uygulayan Doküman", "Sorumlu", "Doğrulama / Kanıt",
                 "Hariç Tutma Gerekçesi", "Son Gözden Geçirme"]
    satirlar = []
    for no, baslik, dokuman, kanit in _annex():
        haric = uygulanmayan.get(no)
        dok = dokuman_ezme.get(no, dokuman)
        if sade:
            dok = sade_kod(dok)
        if haric:
            g = ""
        elif no in gerekce:
            g = gerekce[no]
        elif risk_eslesme.get(no):
            g = f"{risk_eslesme[no]} numaralı risk(ler)in işlenmesi kapsamında gereklidir."
        else:
            g = ("[DOLDURULACAK: ilgili risk no ve/veya yasal/sözleşmesel dayanak]")
        satirlar.append([
            f"A.{no}", baslik, "H" if haric else "E", g,
            risk_eslesme.get(no, ""),
            "" if haric else "Planlandı",
            "" if haric else dok,
            sorumlu.get(no, ""), "" if haric else kanit,
            haric or "", bilgi.get("tarih", ""),
        ])
    k = _kayit(bilgi, "Uygulanabilirlik Bildirgesi (SoA)", bilgi.get("kod_soa", "BGYS-LS-02"))
    k.bilgi_sayfasi(
        aciklama=("ISO/IEC 27001:2022 Madde 6.1.3 d) gereği hazırlanan Uygulanabilirlik "
                  "Bildirgesi. Ek A'daki 93 kontrolün tamamı listelenmiştir; hariç "
                  "tutulanlar için gerekçe zorunludur."),
        kullanim_notu=("Risk değerlendirmesi her güncellendiğinde bu bildirge gözden "
                       "geçirilir. Belgelendirme kuruluşuna sunulan sertifika kapsamı "
                       "bu bildirgenin revizyon numarasına atıf yapar."))
    k.sayfa("SoA", basliklar, satirlar,
            genislikler=[11, 42, 13, 30, 14, 15, 34, 16, 40, 34, 15],
            listeler={"Uygulanabilir (E/H)": ["E", "H"],
                      "Uygulama Durumu": ["Planlandı", "Uygulanıyor", "Uygulandı",
                                          "Kısmen", "Uygulanmıyor"]},
            durum_sutunu="Uygulama Durumu",
            notlar={"Dahil Etme Gerekçesi":
                    "Neden gerekli: risk değerlendirmesi / yasal gereklilik / sözleşme / iyi uygulama",
                    "Hariç Tutma Gerekçesi":
                    "Boş bırakılamaz — 'Uygulanabilir' H ise gerekçe zorunludur."})
    k.ozet_sayfasi("Özet", "SoA", "Uygulama Durumu",
                   ["Planlandı", "Uygulanıyor", "Uygulandı", "Kısmen", "Uygulanmıyor"])
    return k.kaydet(cikti)


# ------------------------------------------------------------------- riskler
def risk_envanteri(bilgi: dict, cikti: str, ornek_satirlar: list | None = None) -> str:
    basliklar = ["Risk No", "Varlık / Süreç", "Varlık Sahibi", "Tehdit", "Açıklık",
                 "Mevcut Kontroller", "Olasılık (1-5)", "Etki (1-5)", "Risk Skoru",
                 "Risk Seviyesi", "Risk Sahibi", "İşleme Seçeneği",
                 "Planlanan Kontroller (Ek A)", "Aksiyon Sorumlusu", "Termin",
                 "Artık Olasılık", "Artık Etki", "Artık Risk", "Risk Sahibi Onayı",
                 "Değerlendirme Tarihi", "Sonraki Gözden Geçirme", "Durum"]
    k = _kayit(bilgi, "Bilgi Güvenliği Risk Envanteri ve Risk İşleme Planı",
               bilgi.get("kod_risk", "BGYS-FR-03"))
    k.bilgi_sayfasi(
        aciklama=("Madde 6.1.2 (risk değerlendirmesi), 6.1.3 (risk işleme), 8.2 ve 8.3 "
                  "kapsamındaki ana kayıt. Risk kriterleri BGYS-PR-02 Risk Yönetimi "
                  "Prosedürü'nde tanımlıdır."),
        kullanim_notu=("Yılda en az bir kez, ayrıca önemli değişiklik ve ciddi ihlal "
                       "olayı sonrasında güncellenir. 'Risk Sahibi Onayı' sütunu "
                       "6.1.3 f) gereğidir ve boş bırakılamaz."))
    k.sayfa("Risk Envanteri", basliklar, ornek_satirlar or [],
            genislikler=[9, 26, 16, 26, 26, 30, 12, 11, 11, 13, 16, 14, 28, 16, 12,
                         13, 12, 11, 16, 15, 16, 11],
            listeler={"Olasılık (1-5)": [1, 2, 3, 4, 5], "Etki (1-5)": [1, 2, 3, 4, 5],
                      "Artık Olasılık": [1, 2, 3, 4, 5], "Artık Etki": [1, 2, 3, 4, 5],
                      "İşleme Seçeneği": ["Azalt", "Kabul et", "Aktar", "Kaçın"],
                      "Risk Sahibi Onayı": ["Onaylandı", "Beklemede", "Reddedildi"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            formuller={
                "Risk Skoru": '=IF(AND([Olasılık (1-5)]{r}<>"",[Etki (1-5)]{r}<>""),'
                              '[Olasılık (1-5)]{r}*[Etki (1-5)]{r},"")',
                "Risk Seviyesi": '=IF([Risk Skoru]{r}="","",IF([Risk Skoru]{r}>=15,"Yüksek",'
                                 'IF([Risk Skoru]{r}>=8,"Orta","Düşük")))',
                "Artık Risk": '=IF(AND([Artık Olasılık]{r}<>"",[Artık Etki]{r}<>""),'
                              '[Artık Olasılık]{r}*[Artık Etki]{r},"")'},
            isi_haritasi=["Risk Skoru", "Artık Risk"], durum_sutunu="Durum",
            bos_satir=60,
            notlar={"Risk Skoru": "Otomatik: Olasılık × Etki",
                    "Risk Seviyesi": "≥15 Yüksek, 8–14 Orta, <8 Düşük (BGYS-PR-02'ye göre ayarlanır)",
                    "Risk Sahibi Onayı": "Madde 6.1.3 f) — risk sahibi işleme planını onaylar ve artık riski kabul eder."})
    k.sayfa("Risk Kriterleri",
            ["Parametre", "Değer / Tanım", "Açıklama"],
            [["Olasılık 1", "Çok düşük", "5 yılda birden az beklenir"],
             ["Olasılık 2", "Düşük", "2-5 yılda bir beklenir"],
             ["Olasılık 3", "Orta", "Yılda bir beklenir"],
             ["Olasılık 4", "Yüksek", "Çeyrekte bir beklenir"],
             ["Olasılık 5", "Çok yüksek", "Ayda bir veya daha sık beklenir"],
             ["Etki 1", "Önemsiz", "Operasyon etkilenmez, maddi kayıp yok"],
             ["Etki 2", "Düşük", "Kısa süreli aksama, sınırlı maddi kayıp"],
             ["Etki 3", "Orta", "Hizmet aksaması, müşteri şikâyeti, orta düzey kayıp"],
             ["Etki 4", "Yüksek", "Yasal yaptırım riski, ciddi itibar kaybı"],
             ["Etki 5", "Kritik", "Faaliyetin durması, ağır yaptırım, ciddi veri ihlali"],
             ["Risk kabul eşiği", "[DOLDURULACAK]", "Bu skorun altındaki riskler kabul edilir"],
             ["Değerlendirme sıklığı", "Yılda 1 kez", "Ayrıca önemli değişiklik ve ihlal sonrası"]],
            genislikler=[22, 24, 56])
    k.ozet_sayfasi("Özet", "Risk Envanteri", "Risk Seviyesi", ["Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)


# ------------------------------------------------------------------ varliklar
def varlik_envanteri(bilgi: dict, cikti: str, ornek_satirlar: list | None = None) -> str:
    k = _kayit(bilgi, "Bilgi Varlıkları Envanteri", bilgi.get("kod_varlik", "BGYS-LS-01"))
    k.bilgi_sayfasi(
        aciklama="Ek A.5.9 gereği bilgi ve ilgili varlıkların envanteri; sahipleri dahil.",
        kullanim_notu="Yeni varlık edinildiğinde eklenir, altı ayda bir gözden geçirilir.")
    k.sayfa("Varlık Envanteri",
            ["Varlık No", "Varlık Adı", "Varlık Tipi", "Açıklama", "Lokasyon / Ortam",
             "Varlık Sahibi", "Sorumlu Birim", "Gizlilik", "Bütünlük", "Erişilebilirlik",
             "Sınıflandırma", "Kişisel Veri İçeriyor mu", "Yasal Dayanak",
             "Saklama Süresi", "İlgili Riskler", "Son Güncelleme"],
            ornek_satirlar or [],
            genislikler=[10, 28, 16, 34, 22, 18, 18, 11, 11, 15, 15, 20, 22, 14, 16, 15],
            listeler={"Varlık Tipi": ["Bilgi/Veri", "Yazılım", "Donanım", "Hizmet",
                                       "Personel", "Fiziksel ortam", "Bulut hizmeti",
                                       "Maddi olmayan"],
                      "Gizlilik": [1, 2, 3], "Bütünlük": [1, 2, 3], "Erişilebilirlik": [1, 2, 3],
                      "Sınıflandırma": ["Açık", "İç Kullanım", "Gizli", "Çok Gizli"],
                      "Kişisel Veri İçeriyor mu": ["Evet", "Hayır", "Özel Nitelikli"]},
            bos_satir=60,
            notlar={"Sınıflandırma": "BGYS-PL-04 Bilgi Sınıflandırma Politikası'ndaki şemaya göre.",
                    "Varlık Sahibi": "Unvan yazın, kişi adı değil — personel değişiminde envanter bozulmaz."})
    k.ozet_sayfasi("Özet", "Varlık Envanteri", "Sınıflandırma",
                   ["Açık", "İç Kullanım", "Gizli", "Çok Gizli"])
    return k.kaydet(cikti)


# -------------------------------------------------------------------- hedefler
def hedefler(bilgi: dict, cikti: str, ornek_satirlar: list | None = None) -> str:
    k = _kayit(bilgi, "Bilgi Güvenliği Hedefleri ve İzleme Tablosu",
               bilgi.get("kod_hedef", "BGYS-FR-04"))
    k.bilgi_sayfasi(
        aciklama=("Madde 6.2 (hedefler) ve 9.1 (izleme, ölçme, analiz, değerlendirme) "
                  "kapsamındaki kayıt."),
        kullanim_notu=("Ölçüm sıklığı sütununa göre güncellenir; sonuçlar Yönetimin "
                       "Gözden Geçirmesi girdisidir (9.3.2)."))
    k.sayfa("Hedefler",
            ["Hedef No", "Bilgi Güvenliği Hedefi", "Politika İlkesiyle İlişkisi",
             "Gösterge (KPI)", "Ölçüm Yöntemi", "Başlangıç Değeri", "Hedef Değer",
             "Ölçüm Sıklığı", "Sorumlu", "Gerekli Kaynak", "Termin",
             "Q1", "Q2", "Q3", "Q4", "Yıl Sonu Durumu", "Değerlendirme", "Durum"],
            ornek_satirlar or [],
            genislikler=[10, 38, 26, 26, 26, 14, 12, 14, 18, 20, 12, 8, 8, 8, 8, 15, 34, 12],
            listeler={"Ölçüm Sıklığı": ["Aylık", "Üç aylık", "Altı aylık", "Yıllık"],
                      "Durum": ["Açık", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=20,
            notlar={"Gösterge (KPI)": "Sayısal olmalı. 'Farkındalığı artırmak' hedef değildir; "
                                       "'oltalama tatbikatı tıklama oranı ≤ %5' hedeftir.",
                    "Başlangıç Değeri": "Mevcut durum ölçülmeden hedef konamaz."})
    return k.kaydet(cikti)


# ------------------------------------------------------------- dokuman listesi
def dokuman_listesi(bilgi: dict, cikti: str, dokumanlar: list | None = None) -> str:
    k = _kayit(bilgi, "Doküman Ana Listesi", bilgi.get("kod_dok", "BGYS-LS-04"))
    k.bilgi_sayfasi(
        aciklama="Madde 7.5.3 gereği yürürlükteki dokümante bilgilerin kontrol listesi.",
        kullanim_notu="Her yeni doküman ve revizyon burada kayıt altına alınır.")
    k.sayfa("İç Dokümanlar",
            ["Doküman No", "Doküman Adı", "Tip", "Revizyon", "Yayın Tarihi",
             "Son Revizyon Tarihi", "Hazırlayan", "Onaylayan", "Dağıtım / Erişim",
             "Gizlilik", "Saklama Süresi", "Ortam", "İlgili Madde/Kontrol", "Durum"],
            dokumanlar or [],
            genislikler=[13, 44, 10, 10, 13, 16, 18, 18, 24, 13, 14, 12, 26, 12],
            listeler={"Tip": ["El Kitabı", "Politika", "Prosedür", "Talimat", "Plan",
                              "Form", "Liste", "Rapor"],
                      "Gizlilik": ["Açık", "İç Kullanım", "Gizli", "Çok Gizli"],
                      "Ortam": ["Elektronik", "Basılı", "Her ikisi"],
                      "Durum": ["Yürürlükte", "Taslak", "Yürürlükten kalktı"]},
            durum_sutunu="Durum", bos_satir=40)
    k.sayfa("Dış Kaynaklı Dokümanlar",
            ["Sıra", "Doküman Adı", "Kaynak / Yayımlayan", "Sürüm / Tarih",
             "Neden Gerekli", "Erişim Yeri", "Sorumlu", "Güncellik Kontrolü"],
            [["1", "TS EN ISO/IEC 27001:2023", "TSE", "2023", "Yönetim sistemi gerekliliği",
              "[DOLDURULACAK]", "BGYS Yöneticisi", "Yıllık"],
             ["2", "6698 sayılı KVKK ve ikincil mevzuat", "Resmî Gazete / KVKK",
              "[DOLDURULACAK]", "Yasal yükümlülük", "mevzuat.gov.tr", "Hukuk", "Altı aylık"]],
            genislikler=[7, 40, 26, 16, 30, 26, 18, 18], bos_satir=20)
    return k.kaydet(cikti)


# ------------------------------------------------------------------ yetkinlik
def yetkinlik(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yetkinlik ve Eğitim Matrisi", bilgi.get("kod_yet", "BGYS-LS-07"))
    k.bilgi_sayfasi(
        aciklama="Madde 7.2 (yetkinlik) ve 7.3 (farkındalık) kapsamındaki kayıt.",
        kullanim_notu="İşe giriş, görev değişikliği ve yıllık eğitim planı sonrası güncellenir.")
    k.sayfa("Yetkinlik Matrisi",
            ["Sıra", "Rol / Unvan", "Kişi", "BGYS'deki Görevi",
             "Gerekli Yetkinlik", "Yetkinlik Kanıtı (eğitim/deneyim/sertifika)",
             "Mevcut Durum", "Boşluk", "Planlanan Eğitim", "Termin", "Tamamlanma",
             "Etkinlik Değerlendirmesi", "Sonraki Tazeleme"],
            [], genislikler=[7, 22, 20, 26, 30, 38, 14, 24, 28, 12, 14, 30, 16],
            listeler={"Mevcut Durum": ["Yeterli", "Kısmen", "Yetersiz"]},
            bos_satir=40,
            notlar={"Etkinlik Değerlendirmesi":
                    "7.2 d) alınan faaliyetlerin etkinliğinin değerlendirilmesini ister — "
                    "eğitim katılım kaydı tek başına yeterli değildir."})
    k.sayfa("Farkındalık Kayıtları",
            ["Tarih", "Faaliyet", "Konu", "Hedef Kitle", "Katılımcı Sayısı",
             "Katılım Oranı", "Ölçüm Yöntemi", "Sonuç", "Sorumlu", "Kanıt Dosyası"],
            [], genislikler=[13, 26, 32, 22, 15, 14, 24, 24, 18, 26], bos_satir=30)
    return k.kaydet(cikti)


# ----------------------------------------------------------------------- DOF
def dof(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Uygunsuzluk ve Düzeltici Faaliyet Takip Formu",
               bilgi.get("kod_dof", "BGYS-FR-12"))
    k.bilgi_sayfasi(
        aciklama="Madde 10.2 kapsamındaki uygunsuzluk ve düzeltici faaliyet kaydı.",
        kullanim_notu=("Kök neden analizi, benzer uygunsuzluk taraması ve etkinlik "
                       "doğrulaması sütunları boş bırakılamaz — denetimde en sık "
                       "eksik çıkan üç alandır."))
    k.sayfa("DÖF Takip",
            ["DÖF No", "Tespit Tarihi", "Kaynak", "Uygunsuzluk Tanımı",
             "İlgili Madde/Kontrol", "Sınıf", "Acil Düzeltme (tepki)",
             "Kök Neden Analizi (yöntem + sonuç)", "Benzer Uygunsuzluk Taraması",
             "Düzeltici Faaliyet", "Sorumlu", "Termin", "Tamamlanma Tarihi",
             "Etkinlik Doğrulama Yöntemi", "Etkinlik Doğrulama Tarihi",
             "Doğrulayan", "BGYS Değişikliği Gerekti mi", "Durum"],
            [], genislikler=[10, 13, 20, 44, 20, 12, 34, 44, 30, 44, 16, 12, 15, 34, 17, 16, 22, 12],
            listeler={"Kaynak": ["İç tetkik", "Dış tetkik", "İhlal olayı", "Müşteri şikâyeti",
                                  "YGG", "İzleme/ölçme", "Çalışan bildirimi", "Diğer"],
                      "Sınıf": ["Majör", "Minör", "Gözlem"],
                      "BGYS Değişikliği Gerekti mi": ["Evet", "Hayır"],
                      "Durum": ["Açık", "Devam", "Kapalı"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"Kök Neden Analizi (yöntem + sonuç)":
                    "Yöntem adı geçmeli (5 Neden, balık kılçığı, hata ağacı) ve sonucu yazılmalı.",
                    "Etkinlik Doğrulama Tarihi":
                    "Kapatma tarihinden SONRA ayrı bir kontrol olmalı; aynı gün doğrulama inandırıcı değildir."})
    k.ozet_sayfasi("Özet", "DÖF Takip", "Durum", ["Açık", "Devam", "Kapalı"])
    return k.kaydet(cikti)


# ---------------------------------------------------------------------- tetkik
def tetkik_programi(bilgi: dict, cikti: str) -> str:
    k = _kayit(bilgi, "Yıllık İç Tetkik Programı", bilgi.get("kod_tetkik", "BGYS-PN-03"))
    k.bilgi_sayfasi(
        aciklama="Madde 9.2.2 gereği tetkik programı: sıklık, yöntem, sorumluluk, raporlama.",
        kullanim_notu=("Tetkikçinin kendi sorumluluk alanını tetkik etmemesi (tarafsızlık) "
                       "denetimde özellikle kontrol edilir."))
    k.sayfa("Tetkik Programı",
            ["Tetkik No", "Dönem", "Tetkik Edilen Süreç / Birim", "Tetkik Kriteri",
             "Kapsam", "Yöntem", "Baş Tetkikçi", "Tetkikçi(ler)",
             "Tarafsızlık Beyanı", "Planlanan Tarih", "Gerçekleşen Tarih",
             "Bulgu Sayısı (Majör/Minör/Gözlem)", "Rapor No", "Raporlandığı Merci", "Durum"],
            [], genislikler=[10, 12, 32, 30, 26, 16, 18, 24, 17, 15, 15, 26, 12, 22, 12],
            listeler={"Yöntem": ["Yerinde", "Uzaktan", "Karma", "Doküman incelemesi"],
                      "Tarafsızlık Beyanı": ["Alındı", "Beklemede"],
                      "Durum": ["Planlandı", "Devam", "Tamamlandı", "Gecikti"]},
            durum_sutunu="Durum", bos_satir=20)
    k.sayfa("Kapsam Matrisi",
            ["Standart Maddesi / Kontrol", "Q1", "Q2", "Q3", "Q4", "Not"],
            [[f"Madde {m}", "", "", "", "", ""] for m in
             ["4.1", "4.2", "4.3", "4.4", "5.1", "5.2", "5.3", "6.1.1", "6.1.2", "6.1.3",
              "6.2", "6.3", "7.1", "7.2", "7.3", "7.4", "7.5", "8.1", "8.2", "8.3",
              "9.1", "9.2", "9.3", "10.1", "10.2"]] +
            [[f"Ek A.{g}", "", "", "", "", ""] for g in ["5", "6", "7", "8"]],
            genislikler=[30, 8, 8, 8, 8, 40],
            notlar={"Standart Maddesi / Kontrol":
                    "Tetkik programı bir yıl içinde tüm maddeleri kapsamalıdır — boş satır kalmamalı."})
    return k.kaydet(cikti)


URETICILER = {
    "soa": (soa, "BGYS-LS-02 Uygulanabilirlik Bildirgesi.xlsx"),
    "risk": (risk_envanteri, "BGYS-FR-03 Risk Envanteri ve Risk Isleme Plani.xlsx"),
    "varlik": (varlik_envanteri, "BGYS-LS-01 Varlik Envanteri.xlsx"),
    "hedef": (hedefler, "BGYS-FR-04 Bilgi Guvenligi Hedefleri.xlsx"),
    "dokuman": (dokuman_listesi, "BGYS-LS-04 Dokuman Ana Listesi.xlsx"),
    "yetkinlik": (yetkinlik, "BGYS-LS-07 Yetkinlik ve Egitim Matrisi.xlsx"),
    "dof": (dof, "BGYS-FR-12 DOF Takip Formu.xlsx"),
    "tetkik": (tetkik_programi, "BGYS-PN-03 Yillik Ic Tetkik Programi.xlsx"),
}


def main() -> None:
    ap = argparse.ArgumentParser(description="BGYS Excel kayitlarini uretir.")
    ap.add_argument("--kurulus", required=True)
    ap.add_argument("--cikti", required=True)
    ap.add_argument("--tarih", default="")
    ap.add_argument("--revizyon", default="00")
    ap.add_argument("--hazirlayan", default="")
    ap.add_argument("--onaylayan", default="")
    ap.add_argument("--gizlilik", default="İç Kullanım")
    ap.add_argument("--hangi", default="soa,risk,varlik,hedef,dokuman,yetkinlik,dof,tetkik")
    ap.add_argument("--sade", action="store_true",
                    help="Sadelestirilmis set: SoA'daki dokuman kodlari birlestirilmis "
                         "karsiliklarina cevrilir (var olmayan dokumana atif olmaz).")
    a = ap.parse_args()

    bilgi = dict(kurulus=a.kurulus, tarih=a.tarih, revizyon=a.revizyon,
                 hazirlayan=a.hazirlayan, onaylayan=a.onaylayan, gizlilik=a.gizlilik)
    os.makedirs(a.cikti, exist_ok=True)
    for ad in [x.strip() for x in a.hangi.split(",") if x.strip()]:
        if ad not in URETICILER:
            print(f"  ! bilinmeyen: {ad}")
            continue
        fn, dosya = URETICILER[ad]
        ek = {"sade": True} if (ad == "soa" and a.sade) else {}
        print(" ->", fn(bilgi, os.path.join(a.cikti, dosya), **ek))


if __name__ == "__main__":
    main()
