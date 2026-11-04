#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ys_docx.py — Yonetim sistemi dokumanlari icin Word uretim motoru.

Neden var: her politika/prosedur/plan ayni kurumsal kiyafeti giymeli. Denetci
bir dokumani acip kapak, antet, dokuman kodu, revizyon tablosu ve onay blogunu
ayni yerde bulamazsa "dokuman kontrolu" (7.5.3) maddesinden bulgu yazar. Bu
motor o iskeleti tek yerden uretir; iceriÄŸi sen yazarsin.

Kullanim:
    from ys_docx import YSBelge, Kimlik

    k = Kimlik(kurulus="ACME A.S.", sistem="BGYS", standart="ISO/IEC 27001:2022",
               ad="Bilgi Guvenligi Politikasi", kod="BGYS-PL-01", revizyon="00",
               tarih="2026-08-11", hazirlayan="BG Yoneticisi",
               kontrol_eden="Kalite Yoneticisi", onaylayan="Genel Mudur",
               gizlilik="Ic Kullanim")

    d = YSBelge(k, sablon="/yol/kurumsal.docx", logo="/yol/logo.png")
    d.kapak()
    d.revizyon_tablosu([("00", "2026-08-11", "Ilk yayin", "BG Yoneticisi")])
    d.icindekiler()
    d.h1("1. Amac"); d.p("...")
    d.tablo(["Rol", "Sorumluluk"], [["Genel Mudur", "Kaynak saglar"]])
    d.onay_blogu()
    d.kaydet("/cikti/BGYS-PL-01.docx")

Sablon davranisi: `sablon` verilirse o dosya taban alinir, yani kurumsal
stiller/antet/renkler korunur ve eksik stiller uzerine eklenir. Verilmezse
asagidaki varsayilan kurumsal kimlik uygulanir.
"""

from __future__ import annotations

import copy
import os
from dataclasses import dataclass, field
from typing import Iterable, Sequence

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

# --------------------------------------------------------------------------
# Kurumsal varsayilanlar. Kullanicinin sablonu yoksa devreye girer.
# --------------------------------------------------------------------------
VARSAYILAN_TEMA = {
    "govde_font": "Calibri",
    "baslik_font": "Calibri",
    "govde_punto": 10.5,
    "ana_renk": "1F4E79",     # koyu lacivert - basliklar ve tablo basligi
    "vurgu_renk": "2E74B5",   # orta mavi - alt basliklar
    "gri": "595959",
    "acik_gri": "D9D9D9",
    "tablo_seritli": True,
}


@dataclass
class Kimlik:
    """Her dokumanin kapaginda, antetinde ve onay blogunda tekrar eden kimlik."""

    kurulus: str
    ad: str
    kod: str
    sistem: str = ""              # BGYS / ISYS / HYYS / YZYS
    standart: str = ""            # ISO/IEC 27001:2022 vb.
    revizyon: str = "00"
    tarih: str = ""
    hazirlayan: str = ""
    kontrol_eden: str = ""
    onaylayan: str = ""
    gizlilik: str = "Ic Kullanim"
    kapsam_notu: str = ""
    ek_alanlar: dict = field(default_factory=dict)


def _hex(v: str) -> RGBColor:
    return RGBColor.from_string(v.upper().lstrip("#"))


def _shade(cell, renk: str) -> None:
    """Hucreye dolgu rengi verir (python-docx'te dogrudan API yok)."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), renk.upper().lstrip("#"))
    tcPr.append(shd)


def _kenarlik(tablo, renk: str = "BFBFBF", kalinlik: int = 6) -> None:
    tbl = tablo._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for kenar in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{kenar}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(kalinlik))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), renk.upper().lstrip("#"))
        borders.append(el)
    tblPr.append(borders)


def _alan(paragraf, kod: str) -> None:
    """Word alan kodu ekler (SAYFA, NUMSAYFA, TOC ...)."""
    r = paragraf.add_run()
    b = OxmlElement("w:fldChar"); b.set(qn("w:fldCharType"), "begin")
    t = OxmlElement("w:instrText"); t.set(qn("xml:space"), "preserve"); t.text = kod
    s = OxmlElement("w:fldChar"); s.set(qn("w:fldCharType"), "separate")
    e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), "end")
    for el in (b, t, s, e):
        r._r.append(el)


class YSBelge:
    """Tek bir yonetim sistemi dokumani."""

    def __init__(self, kimlik: Kimlik, sablon: str | None = None,
                 logo: str | None = None, tema: dict | None = None):
        self.k = kimlik
        self.logo = logo if (logo and os.path.exists(logo)) else None
        self.tema = {**VARSAYILAN_TEMA, **(tema or {})}
        self.sablon_kullanildi = bool(sablon and os.path.exists(sablon))

        if self.sablon_kullanildi:
            self.doc = Document(sablon)
            self._sablonu_temizle()
        else:
            self.doc = Document()
            self._sayfa_duzeni()

        self._stilleri_kur()
        self._antet_altbilgi()

    # ---------------------------------------------------------------- kurulum
    def _sablonu_temizle(self) -> None:
        """Sablondaki ornek govde metnini siler, stilleri ve bolum ayarlarini birakir."""
        body = self.doc.element.body
        for child in list(body):
            if child.tag == qn("w:sectPr"):
                continue
            body.remove(child)

    def _sayfa_duzeni(self) -> None:
        for s in self.doc.sections:
            s.top_margin = Cm(2.5)
            s.bottom_margin = Cm(2.0)
            s.left_margin = Cm(2.5)
            s.right_margin = Cm(2.0)
            s.header_distance = Cm(1.0)
            s.footer_distance = Cm(0.8)

    def _stil(self, ad: str, temel: str = "Normal"):
        """Stili bulur, yoksa olusturur. Sablondaki ayni adli stili EZMEZ."""
        try:
            return self.doc.styles[ad], False
        except KeyError:
            from docx.enum.style import WD_STYLE_TYPE
            st = self.doc.styles.add_style(ad, WD_STYLE_TYPE.PARAGRAPH)
            st.base_style = self.doc.styles[temel]
            return st, True

    def _stilleri_kur(self) -> None:
        t = self.tema

        normal = self.doc.styles["Normal"]
        if not self.sablon_kullanildi:
            normal.font.name = t["govde_font"]
            normal.font.size = Pt(t["govde_punto"])
            normal.element.rPr.rFonts.set(qn("w:eastAsia"), t["govde_font"])
        normal.paragraph_format.space_after = Pt(6)
        normal.paragraph_format.line_spacing = 1.15

        # Baslik seviyeleri - sablonda varsa dokunmuyoruz, yoksa kuruyoruz.
        seviyeler = [
            ("Heading 1", 15, True, t["ana_renk"], 14, 6),
            ("Heading 2", 12.5, True, t["vurgu_renk"], 10, 4),
            ("Heading 3", 11, True, t["gri"], 8, 3),
        ]
        for ad, punto, kalin, renk, once, sonra in seviyeler:
            try:
                st = self.doc.styles[ad]
            except KeyError:
                continue
            if self.sablon_kullanildi:
                continue
            st.font.name = t["baslik_font"]
            st.font.size = Pt(punto)
            st.font.bold = kalin
            st.font.color.rgb = _hex(renk)
            st.paragraph_format.space_before = Pt(once)
            st.paragraph_format.space_after = Pt(sonra)
            st.paragraph_format.keep_with_next = True

        ozel = {
            "YS Kapak Kurum": dict(size=13, bold=False, color=t["gri"], align="center", after=2),
            "YS Kapak Baslik": dict(size=26, bold=True, color=t["ana_renk"], align="center", after=6, before=24),
            "YS Kapak Alt": dict(size=12, bold=False, color=t["gri"], align="center", after=24),
            "YS Govde": dict(size=t["govde_punto"], bold=False, color="000000", align="justify", after=6),
            "YS Not": dict(size=9.5, bold=False, color=t["gri"], align="left", after=6, italic=True),
            "YS Tablo Basligi": dict(size=9.5, bold=True, color="FFFFFF", align="center", after=0),
            "YS Tablo Govde": dict(size=9.5, bold=False, color="000000", align="left", after=0),
            "YS Sekil Yazisi": dict(size=9, bold=False, color=t["gri"], align="center", after=8, italic=True),
        }
        for ad, cfg in ozel.items():
            st, yeni = self._stil(ad)
            if not yeni:
                continue
            st.font.name = t["govde_font"]
            st.font.size = Pt(cfg["size"])
            st.font.bold = cfg["bold"]
            st.font.italic = cfg.get("italic", False)
            st.font.color.rgb = _hex(cfg["color"])
            pf = st.paragraph_format
            pf.space_after = Pt(cfg["after"])
            pf.space_before = Pt(cfg.get("before", 0))
            pf.alignment = {
                "center": WD_ALIGN_PARAGRAPH.CENTER,
                "left": WD_ALIGN_PARAGRAPH.LEFT,
                "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
            }[cfg["align"]]

    def _antet_altbilgi(self) -> None:
        if self.sablon_kullanildi:
            # Kurumsal sablonun kendi anteti varsa ona dokunma.
            hdr = self.doc.sections[0].header
            if any(p.text.strip() for p in hdr.paragraphs) or hdr.tables:
                return

        for s in self.doc.sections:
            hdr = s.header
            for p in list(hdr.paragraphs):
                p.text = ""
            tbl = hdr.add_table(rows=2, cols=3, width=Cm(16.5))
            tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl.autofit = True

            if self.logo:
                cell = tbl.cell(0, 0).merge(tbl.cell(1, 0))
                run = cell.paragraphs[0].add_run()
                run.add_picture(self.logo, height=Cm(1.1))
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                cell = tbl.cell(0, 0).merge(tbl.cell(1, 0))
                r = cell.paragraphs[0].add_run(self.k.kurulus)
                r.bold = True
                r.font.size = Pt(10)
                r.font.color.rgb = _hex(self.tema["ana_renk"])

            orta = tbl.cell(0, 1).merge(tbl.cell(1, 1))
            r = orta.paragraphs[0].add_run(self.k.ad)
            r.bold = True
            r.font.size = Pt(9.5)
            orta.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

            sag_ust, sag_alt = tbl.cell(0, 2), tbl.cell(1, 2)
            for hucre, metin in ((sag_ust, f"Dok. No: {self.k.kod}"),
                                 (sag_alt, f"Rev. {self.k.revizyon} / {self.k.tarih}")):
                r = hucre.paragraphs[0].add_run(metin)
                r.font.size = Pt(8.5)
                r.font.color.rgb = _hex(self.tema["gri"])
                hucre.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
            _kenarlik(tbl, self.tema["acik_gri"], 4)

            ftr = s.footer
            p = ftr.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(f"{self.k.gizlilik}  |  Sayfa ")
            r.font.size = Pt(8)
            r.font.color.rgb = _hex(self.tema["gri"])
            _alan(p, "PAGE")
            r = p.add_run(" / ")
            r.font.size = Pt(8)
            _alan(p, "NUMPAGES")

    # ----------------------------------------------------------------- icerik
    def kapak(self, alt_baslik: str | None = None) -> "YSBelge":
        if self.logo:
            p = self.doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.add_run().add_picture(self.logo, height=Cm(2.2))
        self.doc.add_paragraph(self.k.kurulus, style="YS Kapak Kurum")
        if self.k.sistem:
            self.doc.add_paragraph(self.k.sistem, style="YS Kapak Kurum")
        self.doc.add_paragraph(self.k.ad, style="YS Kapak Baslik")
        if alt_baslik:
            self.doc.add_paragraph(alt_baslik, style="YS Kapak Alt")
        elif self.k.standart:
            self.doc.add_paragraph(self.k.standart, style="YS Kapak Alt")

        satirlar = [
            ("Dokuman No", self.k.kod),
            ("Revizyon No", self.k.revizyon),
            ("Yayin / Revizyon Tarihi", self.k.tarih),
            ("Gizlilik Derecesi", self.k.gizlilik),
        ]
        satirlar += [(a, b) for a, b in self.k.ek_alanlar.items()]
        t = self.doc.add_table(rows=len(satirlar), cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, (etiket, deger) in enumerate(satirlar):
            sol, sag = t.cell(i, 0), t.cell(i, 1)
            sol.paragraphs[0].style = self.doc.styles["YS Tablo Govde"]
            sol.paragraphs[0].add_run(etiket).bold = True
            sag.paragraphs[0].style = self.doc.styles["YS Tablo Govde"]
            sag.paragraphs[0].add_run(str(deger))
            sol.width = Cm(6.0); sag.width = Cm(8.0)
        _kenarlik(t, self.tema["acik_gri"])
        self.sayfa_sonu()
        return self

    def revizyon_tablosu(self, kayitlar: Sequence[Sequence[str]] | None = None) -> "YSBelge":
        """kayitlar: (rev_no, tarih, degisiklik, yapan) dortlusu."""
        self.h1("Revizyon Gecmisi")
        kayitlar = kayitlar or [(self.k.revizyon, self.k.tarih, "Ilk yayin", self.k.hazirlayan)]
        self.tablo(["Rev. No", "Tarih", "Degisiklik Aciklamasi", "Yapan"],
                   [list(x) for x in kayitlar], genislikler=[2.0, 2.6, 8.4, 3.0])
        return self

    def icindekiler(self, derinlik: int = 3) -> "YSBelge":
        self.h1("Icindekiler")
        p = self.doc.add_paragraph()
        _alan(p, f'TOC \\o "1-{derinlik}" \\h \\z \\u')
        self.not_kutusu(
            "Icindekiler alanini guncellemek icin Word'de tumunu secip F9 tusuna basin "
            "(veya Basvurular > Tabloyu Guncelle)."
        )
        self.sayfa_sonu()
        return self

    def h1(self, metin: str) -> "YSBelge":
        self.doc.add_paragraph(metin, style="Heading 1")
        return self

    def h2(self, metin: str) -> "YSBelge":
        self.doc.add_paragraph(metin, style="Heading 2")
        return self

    def h3(self, metin: str) -> "YSBelge":
        self.doc.add_paragraph(metin, style="Heading 3")
        return self

    def p(self, metin: str, stil: str = "YS Govde") -> "YSBelge":
        self.doc.add_paragraph(metin, style=stil)
        return self

    def madde(self, ogeler: Iterable[str], numarali: bool = False) -> "YSBelge":
        stil = "List Number" if numarali else "List Bullet"
        for o in ogeler:
            self.doc.add_paragraph(o, style=stil)
        return self

    def not_kutusu(self, metin: str) -> "YSBelge":
        self.doc.add_paragraph(f"NOT: {metin}", style="YS Not")
        return self

    def doldurulacak(self, metin: str) -> "YSBelge":
        """Kuruluştan bilgi bekleyen alanlari gorunur birakir - denetim oncesi
        bunlarin hepsinin kapatilmis olmasi gerekir."""
        p = self.doc.add_paragraph(style="YS Govde")
        r = p.add_run(f"[DOLDURULACAK] {metin}")
        r.bold = True
        r.font.color.rgb = _hex("C00000")
        return self

    def tablo(self, basliklar: Sequence[str], satirlar: Sequence[Sequence],
              genislikler: Sequence[float] | None = None,
              baslik_rengi: str | None = None) -> "YSBelge":
        t = self.doc.add_table(rows=1, cols=len(basliklar))
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        renk = baslik_rengi or self.tema["ana_renk"]
        for i, b in enumerate(basliklar):
            c = t.cell(0, i)
            c.paragraphs[0].style = self.doc.styles["YS Tablo Basligi"]
            c.paragraphs[0].add_run(str(b))
            _shade(c, renk)
        for j, satir in enumerate(satirlar):
            hucreler = t.add_row().cells
            for i, deger in enumerate(satir[:len(basliklar)]):
                hucreler[i].paragraphs[0].style = self.doc.styles["YS Tablo Govde"]
                hucreler[i].paragraphs[0].add_run("" if deger is None else str(deger))
            if self.tema["tablo_seritli"] and j % 2 == 1:
                for c in hucreler:
                    _shade(c, "F2F6FA")
        if genislikler:
            for i, g in enumerate(genislikler[:len(basliklar)]):
                for row in t.rows:
                    row.cells[i].width = Cm(g)
        _kenarlik(t, self.tema["acik_gri"])
        self.doc.add_paragraph("", style="YS Govde")
        return self

    def onay_blogu(self) -> "YSBelge":
        self.h1("Hazirlayan / Kontrol Eden / Onaylayan")
        t = self.doc.add_table(rows=4, cols=4)
        basliklar = ["", "Hazirlayan", "Kontrol Eden", "Onaylayan"]
        satirlar = [
            ["Ad Soyad / Unvan", self.k.hazirlayan, self.k.kontrol_eden, self.k.onaylayan],
            ["Tarih", self.k.tarih, self.k.tarih, self.k.tarih],
            ["Imza", "", "", ""],
        ]
        for i, b in enumerate(basliklar):
            c = t.cell(0, i)
            c.paragraphs[0].style = self.doc.styles["YS Tablo Basligi"]
            c.paragraphs[0].add_run(b)
            _shade(c, self.tema["ana_renk"])
        for r, satir in enumerate(satirlar, start=1):
            for i, deger in enumerate(satir):
                c = t.cell(r, i)
                c.paragraphs[0].style = self.doc.styles["YS Tablo Govde"]
                run = c.paragraphs[0].add_run(str(deger))
                if i == 0:
                    run.bold = True
            if satir[0] == "Imza":
                for i in range(1, 4):
                    t.cell(r, i).height = Cm(1.6)
        _kenarlik(t, self.tema["acik_gri"])
        return self

    def sayfa_sonu(self) -> "YSBelge":
        self.doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
        return self

    def kaydet(self, yol: str) -> str:
        os.makedirs(os.path.dirname(os.path.abspath(yol)), exist_ok=True)
        self.doc.save(yol)
        return yol


# ------------------------------------------------------------------ kalip
def standart_belge(kimlik: Kimlik, bolumler: Sequence[tuple], **kw) -> YSBelge:
    """Kapak + revizyon + icindekiler + bolumler + onay iskeletini tek cagriyla kurar.

    bolumler: [("h1"|"h2"|"h3"|"p"|"madde"|"tablo"|"not"|"doldurulacak", veri), ...]
    tablo verisi: (basliklar, satirlar) veya (basliklar, satirlar, genislikler)
    """
    d = YSBelge(kimlik, **kw)
    d.kapak().revizyon_tablosu().icindekiler()
    for tip, veri in bolumler:
        if tip == "h1":
            d.h1(veri)
        elif tip == "h2":
            d.h2(veri)
        elif tip == "h3":
            d.h3(veri)
        elif tip == "p":
            d.p(veri)
        elif tip == "madde":
            d.madde(veri)
        elif tip == "numara":
            d.madde(veri, numarali=True)
        elif tip == "not":
            d.not_kutusu(veri)
        elif tip == "doldurulacak":
            d.doldurulacak(veri)
        elif tip == "tablo":
            d.tablo(*veri)
        elif tip == "sayfa":
            d.sayfa_sonu()
    d.onay_blogu()
    return d


if __name__ == "__main__":
    k = Kimlik(kurulus="ORNEK A.S.", ad="Bilgi Guvenligi Politikasi", kod="BGYS-PL-01",
               sistem="Bilgi Guvenligi Yonetim Sistemi", standart="TS EN ISO/IEC 27001:2022",
               tarih="2026-08-11", hazirlayan="BGYS Yoneticisi",
               kontrol_eden="Kalite Yoneticisi", onaylayan="Genel Mudur")
    d = standart_belge(k, [
        ("h1", "1. Amac"),
        ("p", "Bu politikanin amaci ..."),
        ("h1", "2. Kapsam"),
        ("p", "..."),
        ("h1", "3. Sorumluluklar"),
        ("tablo", (["Rol", "Sorumluluk"], [["Ust Yonetim", "Kaynak saglar"],
                                            ["BGYS Yoneticisi", "Sistemi isletir"]], [5.0, 10.0])),
    ])
    print(d.kaydet("/tmp/ornek_politika.docx"))
