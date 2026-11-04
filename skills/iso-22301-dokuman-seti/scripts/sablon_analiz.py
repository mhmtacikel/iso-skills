#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sablon_analiz.py — Kullanicinin kurumsal Word sablonunu (.docx/.dotx) okur ve
uretilecek dokumanlarin ona benzemesi icin gereken bilgiyi cikarir.

Neden var: kullanici "sablonum var" dediginde ona uymayan bir dokuman uretmek,
her dosyayi elle yeniden bicimlendirmesi demektir. Once sablonu tani, sonra uret.

Kullanim:
    python3 sablon_analiz.py /yol/sablon.docx
    python3 sablon_analiz.py /yol/sablon.docx --json

Cikti: stil adlari, yazi tipleri, renkler, antet/altbilgi metni, tespit edilen
dokuman kodu kalibi ve logo olup olmadigi.
"""

from __future__ import annotations

import json
import re
import sys
import zipfile

from docx import Document
from docx.shared import RGBColor

KOD_KALIPLARI = [
    (r"\b([A-ZÇĞİÖŞÜ]{2,5})-([A-ZÇĞİÖŞÜ]{2,3})-(\d{2,3})(?:-(\d{2,3}))?\b", "HARF-TIP-NO"),
    (r"\b([A-ZÇĞİÖŞÜ]{2,5})\.([A-ZÇĞİÖŞÜ]{2,3})\.(\d{2,3})\b", "HARF.TIP.NO"),
    (r"\b(FR|PR|PL|TL|LS|FORM|PROS)[-_ ]?(\d{2,3})\b", "TIP-NO"),
]


def _renk(font) -> str | None:
    try:
        if font.color and font.color.rgb and isinstance(font.color.rgb, RGBColor):
            return str(font.color.rgb)
    except Exception:
        pass
    return None


def analiz(yol: str) -> dict:
    doc = Document(yol)
    s = {"dosya": yol, "stiller": [], "antet": [], "altbilgi": [],
         "logo_var": False, "resim_sayisi": 0, "sayfa_duzeni": {},
         "kod_ornekleri": [], "kod_kalibi": None, "tablo_sayisi": len(doc.tables),
         "notlar": []}

    normal = doc.styles["Normal"]
    s["normal_font"] = normal.font.name
    s["normal_punto"] = normal.font.size.pt if normal.font.size else None

    for st in doc.styles:
        try:
            if st.type is None or not st.name:
                continue
            kayit = {"ad": st.name, "tip": str(st.type).split(".")[-1].split(" ")[0]}
            f = getattr(st, "font", None)
            if f is not None:
                kayit.update({"font": f.name, "punto": f.size.pt if f.size else None,
                              "kalin": f.bold, "renk": _renk(f)})
            if any(kayit.get(x) for x in ("font", "punto", "renk")) or \
               st.name.lower().startswith(("heading", "başlık", "baslik", "title", "liste", "list")):
                s["stiller"].append(kayit)
        except Exception:
            continue

    sec = doc.sections[0]
    s["sayfa_duzeni"] = {
        "ust_cm": round(sec.top_margin.cm, 2), "alt_cm": round(sec.bottom_margin.cm, 2),
        "sol_cm": round(sec.left_margin.cm, 2), "sag_cm": round(sec.right_margin.cm, 2),
        "yonlendirme": "yatay" if sec.page_width > sec.page_height else "dikey",
    }

    metinler = []
    for bolum in doc.sections:
        for hedef, anahtar in ((bolum.header, "antet"), (bolum.footer, "altbilgi")):
            for p in hedef.paragraphs:
                if p.text.strip():
                    s[anahtar].append(p.text.strip())
                    metinler.append(p.text)
            for t in hedef.tables:
                for row in t.rows:
                    for c in row.cells:
                        if c.text.strip():
                            s[anahtar].append(c.text.strip())
                            metinler.append(c.text)

    for p in doc.paragraphs[:80]:
        if p.text.strip():
            metinler.append(p.text)
    for t in doc.tables[:5]:
        for row in t.rows:
            for c in row.cells:
                metinler.append(c.text)

    havuz = "\n".join(metinler)
    for kalip, ad in KOD_KALIPLARI:
        bulunan = re.findall(kalip, havuz)
        if bulunan:
            s["kod_kalibi"] = ad
            s["kod_ornekleri"] = sorted({"".join(x) if isinstance(x, str) else
                                          "-".join(y for y in x if y) for x in bulunan})[:10]
            break

    with zipfile.ZipFile(yol) as z:
        medya = [n for n in z.namelist() if n.startswith("word/media/")]
    s["resim_sayisi"] = len(medya)
    s["logo_var"] = len(medya) > 0
    s["medya"] = medya[:10]

    if not s["antet"]:
        s["notlar"].append("Sablonda antet yok - ys_docx.py kendi antetini kuracak.")
    if not s["logo_var"]:
        s["notlar"].append("Sablonda gomulu resim yok - logo dosyasini ayrica iste.")
    if not s["kod_kalibi"]:
        s["notlar"].append("Dokuman kodu kalibi tespit edilemedi - kullaniciya sor.")
    return s


def temaya_cevir(s: dict) -> dict:
    """Analiz sonucunu ys_docx.YSBelge(tema=...) sozlugune cevirir.

    Neden var: analiz ciktisini gozle okuyup elle tema yazmak hem yavas hem
    hataya acik. Sablonu YSBelge'ye `sablon=` ile verdiginde stiller zaten
    miras alinir; bu fonksiyon, sablonu taban almadan sadece RENK ve YAZI
    TIPINI tasimak istedigin durumlar icin (or. Excel kayitlarini ayni
    kurumsal renkle uretmek).

    Kullanim:
        s = analiz("kurumsal.docx")
        tema = temaya_cevir(s)
        d = YSBelge(kimlik, tema=tema)          # renk/font sablondan
        # ya da tam miras icin:
        d = YSBelge(kimlik, sablon="kurumsal.docx")
    """
    tema = {}
    if s.get("normal_font"):
        tema["govde_font"] = s["normal_font"]
    if s.get("normal_punto"):
        tema["govde_punto"] = s["normal_punto"]

    def _stil(ad_parcalari):
        for st in s.get("stiller", []):
            ad = (st.get("ad") or "").lower()
            if any(p in ad for p in ad_parcalari):
                return st
        return None

    h1 = _stil(["heading 1", "başlık 1", "baslik 1"])
    h2 = _stil(["heading 2", "başlık 2", "baslik 2"])
    if h1:
        if h1.get("font"):
            tema["baslik_font"] = h1["font"]
        if h1.get("renk") and h1["renk"] not in ("000000", "auto"):
            tema["ana_renk"] = h1["renk"]
    if h2 and h2.get("renk") and h2["renk"] not in ("000000", "auto"):
        tema["vurgu_renk"] = h2["renk"]
    return tema


def yazdir(s: dict) -> None:
    print(f"\n=== SABLON ANALIZI: {s['dosya']}")
    print(f"Govde yazi tipi : {s.get('normal_font')} {s.get('normal_punto')}pt")
    print(f"Sayfa duzeni    : {s['sayfa_duzeni']}")
    print(f"Logo/resim      : {'VAR (' + str(s['resim_sayisi']) + ' adet)' if s['logo_var'] else 'YOK'}")
    print(f"Dokuman kodu    : {s['kod_kalibi'] or 'tespit edilemedi'} {s['kod_ornekleri']}")
    if s["antet"]:
        print("Antet           : " + " | ".join(dict.fromkeys(s["antet"]))[:200])
    if s["altbilgi"]:
        print("Altbilgi        : " + " | ".join(dict.fromkeys(s["altbilgi"]))[:200])
    print("\nBaslik/govde stilleri:")
    for st in s["stiller"]:
        if st["ad"].lower().startswith(("heading", "başlık", "baslik", "normal", "title", "liste", "list")):
            print(f"  - {st['ad']:<28} font={st.get('font')} punto={st.get('punto')} "
                  f"kalin={st.get('kalin')} renk={st.get('renk')}")
    if s["notlar"]:
        print("\nDikkat:")
        for n in s["notlar"]:
            print(f"  ! {n}")
    print("\nys_docx tema sozlugu (tema= parametresine verilebilir):")
    print(f"  {temaya_cevir(s)}")
    print("Tam stil mirasi icin: YSBelge(kimlik, sablon=\"%s\")" % s["dosya"])
    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    sonuc = analiz(sys.argv[1])
    if "--json" in sys.argv:
        print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    else:
        yazdir(sonuc)
