#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ys_xlsx.py — Yonetim sistemi kayit/envanter/liste uretim motoru.

Neden var: risk envanteri, Uygulanabilirlik Bildirgesi, varlik envanteri, hedef
takibi gibi kayitlar Word tablosunda yasamaz - filtrelenmesi, siralanmasi ve
guncellenmesi gerekir. Denetci de bu kayitlarda "canli" izler arar: bos birakilmis
sutun, hicbir zaman guncellenmemis tarih, formulsuz risk skoru bulgu uretir.

Bu motor: kimlik sayfasi (Bilgi), stilli baslik satiri, dondurulmus bolme,
otomatik filtre, acilir liste (veri dogrulama), kosullu bicimlendirme ve
formul destegi verir.

Kullanim:
    from ys_xlsx import YSKayit, SUTUN

    k = YSKayit("ACME A.S.", "Bilgi Guvenligi Risk Envanteri", "BGYS-FR-03",
                standart="TS EN ISO/IEC 27001:2022", revizyon="00", tarih="2026-08-11")
    k.bilgi_sayfasi()
    k.sayfa("Risk Envanteri",
            basliklar=["Risk No", "Varlik", "Tehdit", "Aciklik", "Olasilik", "Etki",
                       "Risk Skoru", "Risk Sahibi", "Isleme Secenegi", "Kontroller"],
            satirlar=[...],
            genislikler=[9, 22, 24, 24, 10, 8, 11, 18, 16, 30],
            listeler={"Olasilik": [1,2,3,4,5], "Isleme Secenegi": ["Azalt","Kabul et","Aktar","Kacin"]},
            formuller={"Risk Skoru": "=E{r}*F{r}"},
            isi_haritasi=["Risk Skoru"])
    k.kaydet("/cikti/BGYS-FR-03.xlsx")
"""

from __future__ import annotations

MOTOR_SURUM = "2.0.0"   # _ortak/scripts kaynagindan senkronlanir; elle degistirme

import re as _re


def sayfa_adi(ad: str) -> str:
    """Excel sayfa adi kurali: ters bolu, / ? * [ ] : yasak, en fazla 31 karakter.
    'Tedarikçi / Alt Yüklenici' -> 'Tedarikçi - Alt Yüklenici'."""
    return _re.sub(r"\s*[\/?*\[\]:]\s*", " - ", str(ad)).strip()[:31]

import os
import re
from typing import Sequence

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, ColorScaleRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ANA = "1F4E79"
VURGU = "2E74B5"
ACIK = "F2F6FA"
CIZGI = "BFBFBF"

_ince = Side(style="thin", color=CIZGI)
KENAR = Border(left=_ince, right=_ince, top=_ince, bottom=_ince)


class YSKayit:
    def __init__(self, kurulus: str, ad: str, kod: str, standart: str = "",
                 sistem: str = "", revizyon: str = "00", tarih: str = "",
                 gizlilik: str = "İç Kullanım", hazirlayan: str = "", onaylayan: str = ""):
        self.meta = dict(kurulus=kurulus, ad=ad, kod=kod, standart=standart, sistem=sistem,
                         revizyon=revizyon, tarih=tarih, gizlilik=gizlilik,
                         hazirlayan=hazirlayan, onaylayan=onaylayan)
        self.wb = Workbook()
        self.wb.remove(self.wb.active)

    # ------------------------------------------------------------------ bilgi
    def bilgi_sayfasi(self, aciklama: str = "", kullanim_notu: str = "") -> "YSKayit":
        """Her kaydin kimlik kartI. Dokuman kontrolu (7.5.3) icin gerekli."""
        ws = self.wb.create_sheet("Bilgi", 0)
        ws.sheet_view.showGridLines = False
        m = self.meta
        ws["B2"] = m["kurulus"]
        ws["B2"].font = Font(size=14, bold=True, color=ANA)
        ws["B3"] = m["ad"]
        ws["B3"].font = Font(size=18, bold=True, color=ANA)
        if m["standart"]:
            ws["B4"] = m["standart"]
            ws["B4"].font = Font(size=11, color="595959")

        alanlar = [
            (("Doküman Türü", "Yol Gösterici") if m["kod"] in ("", "Yol Gösterici")
             else ("Doküman No", m["kod"])),
            ("Yönetim Sistemi", m["sistem"]),
            ("Revizyon No", m["revizyon"]),
            ("Yayın / Revizyon Tarihi", m["tarih"]),
            ("Gizlilik Derecesi", m["gizlilik"]),
            ("Hazırlayan", m["hazirlayan"]),
            ("Onaylayan", m["onaylayan"]),
        ]
        r = 6
        for etiket, deger in alanlar:
            ws.cell(r, 2, etiket).font = Font(bold=True, size=10)
            ws.cell(r, 2).fill = PatternFill("solid", fgColor=ACIK)
            ws.cell(r, 2).border = KENAR
            ws.cell(r, 3, deger or "").font = Font(size=10)
            ws.cell(r, 3).border = KENAR
            r += 1

        if aciklama:
            r += 1
            ws.cell(r, 2, "Amaç").font = Font(bold=True, size=10, color=ANA)
            ws.cell(r + 1, 2, aciklama).alignment = Alignment(wrap_text=True, vertical="top")
            ws.merge_cells(start_row=r + 1, start_column=2, end_row=r + 4, end_column=7)
            r += 6
        if kullanim_notu:
            ws.cell(r, 2, "Kullanım / Güncelleme").font = Font(bold=True, size=10, color=ANA)
            ws.cell(r + 1, 2, kullanim_notu).alignment = Alignment(wrap_text=True, vertical="top")
            ws.merge_cells(start_row=r + 1, start_column=2, end_row=r + 4, end_column=7)

        ws.column_dimensions["A"].width = 2
        ws.column_dimensions["B"].width = 28
        for c in "CDEFG":
            ws.column_dimensions[c].width = 20
        return self

    # ------------------------------------------------------------------ sayfa
    def sayfa(self, ad: str, basliklar: Sequence[str], satirlar: Sequence[Sequence] = (),
              genislikler: Sequence[float] | None = None,
              listeler: dict | None = None,
              formuller: dict | None = None,
              isi_haritasi: Sequence[str] = (),
              durum_sutunu: str | None = None,
              bos_satir: int = 0,
              notlar: dict | None = None) -> "YSKayit":
        """
        listeler   : {"Sutun adi": [secenekler]}   -> acilir liste
        formuller  : {"Sutun adi": "=[Olasilik]{r}*[Etki]{r}"}
                     {r} satir numarasi, [Baslik Adi] o sutunun harfi ile degisir.
                     Harf yerine baslik adi kullanmak, sutun sirasi degisince
                     formulun bozulmasini onler.
        isi_haritasi: sayisal sutunlarda yesil-sari-kirmizi renk skalasi
        durum_sutunu: "Acik/Kapali/Devam" tarzi sutuna renk kodu
        bos_satir  : kullanicinin dolduracagi bos satir sayisi
        notlar     : {"Sutun adi": "hucre aciklamasi"}
        """
        ws = self.wb.create_sheet(sayfa_adi(ad))
        idx = {b: i + 1 for i, b in enumerate(basliklar)}

        for i, b in enumerate(basliklar, start=1):
            c = ws.cell(1, i, b)
            c.font = Font(bold=True, color="FFFFFF", size=10)
            c.fill = PatternFill("solid", fgColor=ANA)
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            c.border = KENAR
        ws.row_dimensions[1].height = 32

        toplam = list(satirlar) + [[""] * len(basliklar) for _ in range(bos_satir)]
        for ri, satir in enumerate(toplam, start=2):
            for ci in range(1, len(basliklar) + 1):
                deger = satir[ci - 1] if ci - 1 < len(satir) else ""
                c = ws.cell(ri, ci, deger)
                c.border = KENAR
                c.alignment = Alignment(vertical="top", wrap_text=True)
                c.font = Font(size=9.5)
                if ri % 2 == 1:
                    c.fill = PatternFill("solid", fgColor=ACIK)

        son = max(2, len(toplam) + 1)

        if formuller:
            # Formullerde sutun harfi yerine BASLIK ADI kullanilabilir: [Risk Skoru]{r}
            # Boylece sutun sirasi degistiginde formul bozulmaz - elle harf saymak
            # bu dosyalarda en sik yapilan hatadir.
            def _cevir(kalip: str) -> str:
                def repl(m):
                    ad = m.group(1)
                    if ad not in idx:
                        raise KeyError(f"Formulde bilinmeyen sutun: {ad}")
                    return get_column_letter(idx[ad])
                return re.sub(r"\[([^\]]+)\]", repl, kalip)

            for sutun, kalip in formuller.items():
                if sutun not in idx:
                    continue
                ci = idx[sutun]
                cevrilmis = _cevir(kalip)
                for ri in range(2, son + 1):
                    ws.cell(ri, ci).value = cevrilmis.format(r=ri)

        if listeler:
            for sutun, secenekler in listeler.items():
                if sutun not in idx:
                    continue
                harf = get_column_letter(idx[sutun])
                dv = DataValidation(
                    type="list",
                    formula1='"' + ",".join(str(s) for s in secenekler) + '"',
                    allow_blank=True, showDropDown=False)
                dv.error = "Lütfen listeden bir değer seçin."
                dv.errorTitle = "Geçersiz değer"
                ws.add_data_validation(dv)
                dv.add(f"{harf}2:{harf}{max(son, 500)}")

        for sutun in isi_haritasi:
            if sutun not in idx:
                continue
            harf = get_column_letter(idx[sutun])
            ws.conditional_formatting.add(
                f"{harf}2:{harf}{max(son, 500)}",
                ColorScaleRule(start_type="min", start_color="63BE7B",
                               mid_type="percentile", mid_value=50, mid_color="FFEB84",
                               end_type="max", end_color="F8696B"))

        if durum_sutunu and durum_sutunu in idx:
            harf = get_column_letter(idx[durum_sutunu])
            alan = f"{harf}2:{harf}{max(son, 500)}"
            for kelime, renk in (("Kapalı", "C6EFCE"), ("Tamamlandı", "C6EFCE"),
                                 ("Uygun", "C6EFCE"), ("Devam", "FFEB9C"),
                                 ("Kısmen Uygun", "FFEB9C"), ("Açık", "FFC7CE"),
                                 ("Aktif", "C6EFCE"), ("Pilot", "FFEB9C"),
                                 ("Emekli", "D9D9D9"),
                                 ("Gecikti", "FFC7CE"), ("Uygun Değil", "FFC7CE")):
                ws.conditional_formatting.add(alan, CellIsRule(
                    operator="equal", formula=[f'"{kelime}"'],
                    fill=PatternFill("solid", fgColor=renk)))

        if notlar:
            from openpyxl.comments import Comment
            for sutun, metin in notlar.items():
                if sutun in idx:
                    ws.cell(1, idx[sutun]).comment = Comment(metin, "Yönetim Sistemi")

        if genislikler:
            for i, g in enumerate(genislikler[:len(basliklar)], start=1):
                ws.column_dimensions[get_column_letter(i)].width = g
        else:
            for i, b in enumerate(basliklar, start=1):
                ws.column_dimensions[get_column_letter(i)].width = max(12, min(40, len(b) + 6))

        ws.freeze_panes = "A2"
        ws.auto_filter.ref = f"A1:{get_column_letter(len(basliklar))}{max(son, 2)}"
        ws.sheet_view.zoomScale = 100
        return self

    def ozet_sayfasi(self, ad: str, kaynak_sayfa: str, sutun: str,
                     basliklar: Sequence[str]) -> "YSKayit":
        """Basit sayim ozeti - denetimde 'bu kayittan ne cikiyor' sorusunun cevabi."""
        ws = self.wb.create_sheet(sayfa_adi(ad))
        kaynak_sayfa = sayfa_adi(kaynak_sayfa)
        kws = self.wb[kaynak_sayfa]
        idx = {c.value: c.column for c in kws[1] if c.value}
        if sutun not in idx:
            return self
        harf = get_column_letter(idx[sutun])
        ws.cell(1, 1, sutun).font = Font(bold=True, color="FFFFFF")
        ws.cell(1, 1).fill = PatternFill("solid", fgColor=ANA)
        ws.cell(1, 2, "Adet").font = Font(bold=True, color="FFFFFF")
        ws.cell(1, 2).fill = PatternFill("solid", fgColor=ANA)
        for i, b in enumerate(basliklar, start=2):
            ws.cell(i, 1, b)
            ws.cell(i, 2, f"=COUNTIF('{kaynak_sayfa}'!{harf}:{harf},A{i})")
        ws.column_dimensions["A"].width = 28
        ws.column_dimensions["B"].width = 10
        return self

    def kaydet(self, yol: str) -> str:
        os.makedirs(os.path.dirname(os.path.abspath(yol)), exist_ok=True)
        self.wb.save(yol)
        return yol


if __name__ == "__main__":
    k = YSKayit("ORNEK A.S.", "Bilgi Guvenligi Risk Envanteri", "BGYS-FR-03",
                standart="TS EN ISO/IEC 27001:2022", sistem="BGYS", tarih="2026-08-11")
    k.bilgi_sayfasi(aciklama="ISO/IEC 27001 Madde 6.1.2 ve 8.2 kapsaminda risk kaydi.",
                    kullanim_notu="Yilda en az bir kez ve onemli degisiklik sonrasi guncellenir.")
    k.sayfa("Risk Envanteri",
            ["Risk No", "Varlik", "Tehdit", "Aciklik", "Olasilik", "Etki", "Risk Skoru",
             "Risk Sahibi", "Isleme Secenegi", "Ilgili Kontroller", "Artik Risk", "Durum"],
            [["R-001", "Musteri veritabani", "Yetkisiz erisim", "Zayif parola politikasi",
              4, 5, "", "BT Muduru", "Azalt", "A.5.15, A.5.17, A.8.5", 6, "Devam"]],
            genislikler=[9, 22, 24, 26, 10, 8, 11, 18, 16, 26, 11, 12],
            listeler={"Olasilik": [1, 2, 3, 4, 5], "Etki": [1, 2, 3, 4, 5],
                      "Isleme Secenegi": ["Azalt", "Kabul et", "Aktar", "Kacin"],
                      "Durum": ["Acik", "Devam", "Kapali"]},
            formuller={"Risk Skoru": '=IF(AND([Olasilik]{r}<>"",[Etki]{r}<>""),[Olasilik]{r}*[Etki]{r},"")'},
            isi_haritasi=["Risk Skoru"], durum_sutunu="Durum", bos_satir=30)
    k.ozet_sayfasi("Ozet", "Risk Envanteri", "Durum", ["Acik", "Devam", "Kapali"])
    import os, tempfile
    print(k.kaydet(os.path.join(tempfile.gettempdir(), "ornek_risk.xlsx")))
