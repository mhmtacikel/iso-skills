#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
envanter.py — Mevcut bir İSG doküman klasörünün envanterini ve doküman kontrolü
bulgularını tek Excel'de çıkarır.

Neden var: gerçek kuruluş klasörleri yıllar içinde birikir — aynı dokümanın üç
revizyonu yan yana, iki farklı kodlama düzeni, "Kopya ..." dosyaları, Word geçici
dosyaları (~$), Thumbs.db, ARŞİV klasörleri, adında yıl geçen formlar. Yüzlerce
dosyayı tek tek açmak yerine bu script dosya adlarından ve (docx/xlsx için)
antet tablolarından kod/revizyon/tarih toplar, bulguları sınıflandırır.

Kullanıcının bilgisayarında (device_bash) çalıştırılmak üzere yazıldı; yalnız
python-docx, openpyxl ve (varsa) xlrd gerekir. .doc/.xls antetleri okunmaz,
yalnız dosya adı analiz edilir — gerekirse önce soffice ile dönüştür.

Kullanım:
    python3 envanter.py "<klasör>" "<çıktı.xlsx>"
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict

COP = re.compile(r"(^~\$|^thumbs\.db$|\.tmp$|^debug\.log$|^plot\.log$|^desktop\.ini$|\.bak$)", re.I)
ARSIV = re.compile(r"(ar[sş][iı]v|eski|old|iptal|orijinal)", re.I)
KOPYA = re.compile(r"(^kopya|\bcopy\b|\(\d\)|_?filigran)", re.I)
TUR = r"(PO|PR|TA|PL|LS|FR|SM|ŞM|TN|ŞR|ŞT|ST|GT|KK|EK|YSEK|TD|SZ|MSDS)"
# 1000-11-PR-014 | 01-PR-004 | 11-ŞT-002 | İSG-PR-01 | 1000-11-04-TA-020
KOD = re.compile(rf"\b((?:\d{{2,4}}-){{1,3}}{TUR}-[0-9X]{{2,4}}x*|[A-ZÇĞİÖŞÜ]{{2,5}}-{TUR}-\d{{2,3}})", re.I)
REV = re.compile(r"(?:rev(?:izyon)?\.?\s*|r\.)(\d{1,2}(?:\.\d)?)", re.I)
YIL = re.compile(r"\b(19|20)\d{2}\b")


def _kod_duzeni(kod: str) -> str:
    parca = kod.split("-")
    if parca[0].isdigit() and len(parca[0]) == 4:
        return "FFFF-BB-TT-SSS (firma kodlu)"
    if parca[0].isdigit():
        return "BB-TT-SSS (birim kodlu, eski)"
    return "ÖNEK-TT-SS"


def _antet(yol: str) -> dict:
    """docx: antet/gövde ilk tablolarından; xlsx: ilk 8 satırdan kod/rev/tarih arar."""
    sonuc = {}
    etiketler = {"kod": ("doküman kodu", "döküman kodu", "doküman no", "döküman no", "dokuman no"),
                 "rev": ("revizyon no",), "yururluk": ("yürürlük", "yürürlülük"),
                 "revtarih": ("revizyon tarihi",)}

    def bak(hucreler):
        for i, h in enumerate(hucreler):
            t = (h or "").strip().lower()
            for anahtar, kaliplar in etiketler.items():
                if anahtar not in sonuc and any(t.startswith(k) for k in kaliplar):
                    for sonraki in hucreler[i + 1:]:
                        if sonraki and sonraki.strip() and sonraki.strip().lower() != t:
                            sonuc[anahtar] = sonraki.strip().lstrip(":").strip()
                            break
    try:
        if yol.lower().endswith(".docx"):
            import docx
            d = docx.Document(yol)
            tablolar = []
            for s in d.sections[:1]:
                tablolar += s.header.tables + s.first_page_header.tables
            tablolar += d.tables[:1]
            for t in tablolar:
                for r in t.rows:
                    bak([c.text for c in r.cells])
            for s in d.sections[:1]:
                for p in s.footer.paragraphs:
                    m = re.search(r"(\S+-\S+)/(\d+)/(\d{2}\.\d{2}\.\d{4})", p.text)
                    if m:
                        sonuc.setdefault("kod", m.group(1)); sonuc.setdefault("rev", m.group(2))
                        sonuc.setdefault("revtarih", m.group(3))
        elif yol.lower().endswith((".xlsx", ".xlsm")):
            import openpyxl
            wb = openpyxl.load_workbook(yol, read_only=True, data_only=True)
            ws = wb.worksheets[0]
            for row in ws.iter_rows(max_row=8, values_only=True):
                bak([str(v) if v is not None else "" for v in row])
                for v in row:
                    if isinstance(v, str) and v.startswith("#"):
                        sonuc["formul_hatasi"] = v
            wb.close()
    except Exception as e:  # bozuk / şifreli dosya
        sonuc["okuma_hatasi"] = type(e).__name__
    return sonuc


def tara(kok: str):
    kayitlar, bulgular = [], []
    for dizin, _, dosyalar in os.walk(kok):
        goreli_dizin = os.path.relpath(dizin, kok)
        for ad in sorted(dosyalar):
            yol = os.path.join(dizin, ad)
            goreli = os.path.normpath(os.path.join(goreli_dizin, ad))
            if COP.search(ad):
                bulgular.append(["Çöp / geçici dosya", goreli, "Doküman değildir; envantere alınmaz, temizlenir."])
                continue
            kok_ad, uzanti = os.path.splitext(ad)
            m = KOD.search(kok_ad)
            kod = m.group(1).upper().replace("ŞM", "ŞM") if m else ""
            rv = REV.search(kok_ad)
            arsivde = bool(ARSIV.search(goreli_dizin)) or bool(re.search(r"\biptal\b", kok_ad, re.I))
            kayit = {
                "Klasör": goreli_dizin, "Dosya": ad, "Uzantı": uzanti.lower(),
                "Koddan Kod": kod, "Kod Düzeni": _kod_duzeni(kod) if kod else "KODSUZ",
                "Addan Rev": rv.group(1) if rv else "", "Arşiv/İptal": "Evet" if arsivde else "",
                "Boyut (KB)": round(os.path.getsize(yol) / 1024, 1),
            }
            a = _antet(yol) if uzanti.lower() in (".docx", ".xlsx", ".xlsm") else {}
            kayit.update({"Antet Kod": a.get("kod", ""), "Antet Rev": a.get("rev", ""),
                          "Yürürlük": a.get("yururluk", ""), "Rev Tarihi": a.get("revtarih", "")})
            kayitlar.append(kayit)

            if not kod and not arsivde and uzanti.lower() in (".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf"):
                bulgular.append(["Kodsuz doküman", goreli, "Kod verilmeli ya da dış kaynaklı/yol gösterici olarak sınıflandırılmalı."])
            if kod and a.get("kod") and a["kod"].replace(" ", "").upper() != kod:
                bulgular.append(["Dosya adı ↔ antet kod farkı", goreli, f"Ad: {kod} / Antet: {a['kod']}"])
            if KOPYA.search(kok_ad):
                bulgular.append(["Kopya / varyant dosya", goreli, "Kontrolsüz kopya; tek yürürlükteki sürüm kalmalı."])
            if YIL.search(kok_ad) and "FR" in kod.upper():
                bulgular.append(["Adında yıl geçen form", goreli, "Form şablonu yıl taşımaz; doldurulmuş kayıt ayrı saklanır."])
            if uzanti.lower() in (".doc", ".xls", ".ppt"):
                bulgular.append(["Eski dosya biçimi", goreli, "docx/xlsx'e dönüştürülmesi önerilir (izlenebilirlik, antet okuma)."])
            if a.get("formul_hatasi"):
                bulgular.append(["Formül hatası", goreli, a["formul_hatasi"]])
            if a.get("okuma_hatasi"):
                bulgular.append(["Okunamayan dosya", goreli, a["okuma_hatasi"]])
            if kod and not (rv or a.get("rev")):
                bulgular.append(["Revizyon bilgisi yok", goreli, "Ne dosya adında ne antette revizyon no bulundu."])

    # aynı koddan birden çok aktif dosya
    gruplar = defaultdict(list)
    for k in kayitlar:
        if k["Koddan Kod"] and not k["Arşiv/İptal"]:
            gruplar[k["Koddan Kod"]].append(k)
    cakisma = []
    for kod, liste in gruplar.items():
        adlar = {re.sub(r"[^a-zçğıöşü]", "", k["Dosya"].lower().split(kod.lower())[-1])[:25] for k in liste}
        if len(liste) > 1:
            tur = "Aynı kod, farklı adlar (kod çakışması)" if len(adlar) > 1 else "Aynı doküman, birden çok sürüm aktif klasörde"
            for k in liste:
                cakisma.append([kod, tur, os.path.join(k["Klasör"], k["Dosya"]), k["Addan Rev"] or k["Antet Rev"]])
    duzenler = defaultdict(int)
    for k in kayitlar:
        duzenler[k["Kod Düzeni"]] += 1
    return kayitlar, bulgular, cakisma, duzenler


def yaz(kayitlar, bulgular, cakisma, duzenler, cikti):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ys_xlsx import YSKayit
    k = YSKayit("[KURULUŞ]", "Mevcut Doküman Envanteri ve Doküman Kontrolü Bulguları", "YOL GÖSTERİCİ",
                standart="ISO 45001:2018 Madde 7.5")
    ozet = "; ".join(f"{a}: {b}" for a, b in sorted(duzenler.items()))
    k.bilgi_sayfasi(aciklama=f"Toplam {len(kayitlar)} doküman dosyası, {len(bulgular)} bulgu, "
                             f"{len(cakisma)} çakışma satırı. Kod düzenleri — {ozet}.",
                    kullanim_notu="Bu dosya yönetim sistemi dokümanı değildir; boşluk analizinin girdisidir.")
    if kayitlar:
        bas = list(kayitlar[0].keys())
        k.sayfa("Envanter", bas, [[r[b] for b in bas] for r in kayitlar])
    k.sayfa("Bulgular", ["Bulgu Türü", "Dosya", "Açıklama"], bulgular, genislikler=[30, 80, 60])
    k.sayfa("Kod Çakışmaları", ["Kod", "Tür", "Dosya", "Rev"], cakisma, genislikler=[18, 40, 80, 8])
    k.ozet_sayfasi("Özet", "Bulgular", "Bulgu Türü",
                   ["Çöp / geçici dosya", "Kodsuz doküman", "Dosya adı ↔ antet kod farkı",
                    "Kopya / varyant dosya", "Adında yıl geçen form", "Eski dosya biçimi",
                    "Formül hatası", "Okunamayan dosya", "Revizyon bilgisi yok"])
    return k.kaydet(cikti)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    r = tara(sys.argv[1])
    print(yaz(*r, sys.argv[2]))
    print(f"{len(r[0])} dosya, {len(r[1])} bulgu, {len(r[2])} çakışma satırı")
    for a, b in sorted(r[3].items()):
        print(f"  {a}: {b}")
