#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tutarlilik_tarama.py — Uretilen doküman setinin teslim oncesi tutarlilik taramasi.

Neden var: denetci iki dokumani yan yana koydugunda farkli rol adi, farkli
siklik, "BILGI" gibi bozuk buyuk harf veya var olmayan bir koda atif gorur ve
"yasamayan sistem" bulgusu yazar. Bu hatalar elle okumayla yakalanmaz.

Kullanim:
    python tutarlilik_tarama.py <set_klasoru> [--sozluk terimler.json] [--md rapor.md]

--sozluk (istege bagli) JSON:
    {"unvan": "ACME Bilisim A.S.",
     "unvan_varyantlari": ["ACME A.S.", "Acme Bilisim"],
     "roller": {"Bilgi İşlem Şefi": "BT Müdürü"},        # yanlis -> dogru
     "yayin_tarihi": "2026-11-04"}

Yapilan 10 kontrol (iso-entegre-yonetim-sistemi Adim 6):
  1 unvan varyantlari        6 kirik dokuman kodu atiflari
  2 sozluk disi rol adlari   7 yol gostericilere kodla atif (K2)
  3 yasakli klisheler        8 [DOLDURULACAK]/[ÖRNEK]/[DOĞRULANACAK] sayimi
  4 olculemez ifadeler       9 yayin tarihi tutarliligi
  5 hatali buyuk harf (K1)  10 kalan Ingilizce kisaltmalar (K3)
Cikis kodu: bulgu yoksa 0, varsa 1 (etiket sayimi bulgu sayilmaz).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import zipfile
from collections import Counter, defaultdict

KOD_RE = re.compile(r"\b([A-ZÇĞİÖŞÜ]{2,5}-[A-Z]{2,3}-\d{2}(?:-\d{2})?)\b")
K1_HATALI = ["YÖNETIM", "BILGI", "POLITIKA", "ILGILI", "SISTEM", "TETKIK", "DEĞIŞIKLIK",
             "GÜVENLIĞI", "ERIŞIM", "EĞITIM", "KIMLIK", "IHLAL", "TEKNIK", "KRITIK",
             "HIZMET", "IŞ ", "GIZLILIK", "SÜREKLILIK", "IZLEME", "IYILEŞTIRME"]
KLISELER = ["kapsamlı bir şekilde", "titizlikle", "önemli ölçüde", "sağlam bir temel",
            "detaylı bir analiz sonucunda", "genel olarak değerlendirildiğinde",
            "ayrıca belirtmek gerekir ki", "büyük önem", "en üst düzeyde",
            "son derece", "etkin ve verimli bir şekilde"]
OLCULEMEZ = ["düzenli olarak", "gerektiğinde", "en kısa sürede", "periyodik olarak",
             "yeterli düzeyde", "zamanında", "uygun aralıklarla", "makul sürede"]
KISALTMALAR = ["SoA", "DPIA", "PII", "BIA", "SLA", "OLA", "CMDB", "RTO", "RPO", "MTPD",
               "AIMS", "DLP", "SIEM", "CCTV", "IVR", "MFA", "SOC", "ISMS", "BCMS", "SMS",
               "PIMS", "OFI", "KPI"]
ETIKETLER = ["[DOLDURULACAK", "[ÖRNEK", "ÖRNEK —", "[DOĞRULANACAK"]
TARIH_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2}|\d{2}\.\d{2}\.20\d{2})\b")


def docx_metin(yol: str) -> str:
    with zipfile.ZipFile(yol) as z:
        parcalar = [n for n in z.namelist()
                    if n.startswith("word/") and n.endswith(".xml")
                    and any(k in n for k in ("document", "header", "footer"))]
        xml = " ".join(z.read(n).decode("utf-8", "ignore") for n in parcalar)
    xml = re.sub(r"</w:p>", "\n", xml)
    return re.sub(r"<[^>]+>", "", xml)


def xlsx_metin(yol: str) -> str:
    from openpyxl import load_workbook
    wb = load_workbook(yol, read_only=True, data_only=True)
    satirlar = []
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            satirlar.append(" | ".join(str(c) for c in row if c is not None))
    return "\n".join(satirlar)


def dosyalari_oku(kok: str) -> dict:
    metinler = {}
    for d, _, dosyalar in os.walk(kok):
        if "_to_delete" in d:
            continue
        for f in dosyalar:
            if f.startswith(("~$", ".")):
                continue
            yol = os.path.join(d, f)
            rel = os.path.relpath(yol, kok)
            try:
                if f.lower().endswith(".docx"):
                    metinler[rel] = docx_metin(yol)
                elif f.lower().endswith((".xlsx", ".xlsm")):
                    metinler[rel] = xlsx_metin(yol)
            except Exception as e:  # bozuk dosya da bir bulgudur
                metinler[rel] = ""
                print(f"UYARI: {rel} okunamadi: {e}", file=sys.stderr)
    return metinler


def tara(kok: str, sozluk: dict) -> dict:
    metinler = dosyalari_oku(kok)
    bulgular = defaultdict(list)
    sayim = {}

    dosya_kodlari = set()
    yol_gostericiler = []
    for rel, metin in metinler.items():
        ad = os.path.splitext(os.path.basename(rel))[0]
        m = KOD_RE.match(ad)
        if m:
            dosya_kodlari.add(m.group(1))
        elif "Yol Gösterici" in metin or "YOL GÖSTERİCİ" in metin:
            yol_gostericiler.append(ad)

    tarihler = Counter()
    for rel, metin in metinler.items():
        kucuk = metin.lower()
        # 1 unvan varyantlari
        for v in sozluk.get("unvan_varyantlari", []):
            if v in metin:
                bulgular["1 Unvan varyanti"].append(f"{rel}: '{v}' -> '{sozluk.get('unvan', '?')}'")
        # 2 rol adlari
        for yanlis, dogru in sozluk.get("roller", {}).items():
            if yanlis in metin:
                bulgular["2 Sozluk disi rol"].append(f"{rel}: '{yanlis}' -> '{dogru}'")
        # 3 klisheler / 4 olculemez
        for k in KLISELER:
            if k in kucuk:
                bulgular["3 Yasakli klishe"].append(f"{rel}: '{k}'")
        for k in OLCULEMEZ:
            if k in kucuk:
                bulgular["4 Olculemez ifade"].append(f"{rel}: '{k}' (sayi/siklik ver)")
        # 5 K1
        for k in K1_HATALI:
            if re.search(r"(?<![A-ZÇĞİÖŞÜa-zçğıöşü])" + re.escape(k), metin):
                bulgular["5 Hatali buyuk harf (K1)"].append(f"{rel}: '{k.strip()}'")
        # 6 kirik kod atiflari
        for kod in sorted(set(KOD_RE.findall(metin))):
            if dosya_kodlari and kod not in dosya_kodlari and not rel.startswith(kod):
                bulgular["6 Kirik dokuman kodu atfi"].append(f"{rel}: {kod} sette yok")
        # 7 yol gostericiye kodla atif: 'XX-RP-..' gibi kodlar 07_ klasorunde dosya olarak yoksa
        if any(p.startswith("07") for p in rel.split(os.sep)) and KOD_RE.match(os.path.basename(rel)):
            bulgular["7 Yol gosterici kodlu (K2)"].append(f"{rel}: denetim hazirlik dosyasi kodsuz olmali")
        # 8 etiket sayimi
        sayim[rel] = {e.strip("[ —"): metin.count(e) for e in ETIKETLER if metin.count(e)}
        # 9 tarih
        for t in TARIH_RE.findall(metin):
            tarihler[t] += 1
        # 10 kisaltmalar (Tanimlar tablosundaki parantez ici kullanim haric)
        for k in KISALTMALAR:
            for m in re.finditer(r"(?<![\w(])" + re.escape(k) + r"(?![\w)])", metin):
                bulgular["10 Kalan Ingilizce kisaltma (K3)"].append(f"{rel}: '{k}'")
                break

    beklenen = sozluk.get("yayin_tarihi")
    if beklenen and tarihler:
        digerleri = {t: n for t, n in tarihler.items() if t != beklenen}
        if digerleri:
            bulgular["9 Yayin tarihi farkli"].append(
                f"beklenen {beklenen}; ayrica gecen: " + ", ".join(f"{t} (x{n})" for t, n in digerleri.items()))
    return {"dosya_sayisi": len(metinler), "kodlu": len(dosya_kodlari),
            "yol_gosterici": len(yol_gostericiler), "bulgular": bulgular,
            "etiketler": {k: v for k, v in sayim.items() if v}}


def markdown(sonuc: dict) -> str:
    s = [f"## Tutarlılık taraması\n",
         f"Taranan dosya: {sonuc['dosya_sayisi']} (kodlu {sonuc['kodlu']}, yol gösterici {sonuc['yol_gosterici']})\n"]
    if not sonuc["bulgular"]:
        s.append("Bulgu yok.\n")
    for baslik in sorted(sonuc["bulgular"], key=lambda x: int(x.split()[0])):
        satirlar = sonuc["bulgular"][baslik]
        s.append(f"\n### {baslik} — {len(satirlar)}\n")
        s += [f"- {x}" for x in satirlar[:200]]
    if sonuc["etiketler"]:
        s.append("\n### 8 Etiket sayımı (kapatılması gerekenler)\n")
        s.append("| Dosya | Etiketler |\n|---|---|")
        for rel, d in sorted(sonuc["etiketler"].items()):
            s.append(f"| {rel} | " + ", ".join(f"{k}: {v}" for k, v in d.items()) + " |")
    return "\n".join(s) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("klasor")
    ap.add_argument("--sozluk", help="unvan/rol/tarih sozlugu (JSON)")
    ap.add_argument("--md", help="raporu bu Markdown dosyasina da yaz")
    a = ap.parse_args()
    sozluk = json.load(open(a.sozluk, encoding="utf-8")) if a.sozluk else {}
    sonuc = tara(a.klasor, sozluk)
    rapor = markdown(sonuc)
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(rapor)
    sys.stdout.reconfigure(encoding="utf-8")
    print(rapor)
    return 1 if sonuc["bulgular"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
