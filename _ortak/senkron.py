#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
senkron.py — Ortak motoru (_ortak/scripts) tum iso-*-dokuman-seti skill'lerine kopyalar
ve sapma olup olmadigini dogrular. Bu dosya skill paketine girmez; bakim aracidir.

    python _ortak/senkron.py           # kopyala
    python _ortak/senkron.py --kontrol  # yalniz dogrula (sapma varsa cikis kodu 1)

Neden: claude.ai'deki her skill ayri plugin olarak yuklenir ve dosya paylasamaz;
motor her skill'de kopya olarak durmak zorunda. Kopyalar elle duzenlenirse
ayrisir (2.0.0 oncesinde 45001'in motoru digerlerinden farkliydi). Tek kaynak
burasidir; motoru yalniz _ortak/scripts icinde degistir, sonra bunu calistir.
"""
import filecmp
import glob
import os
import shutil
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "_ortak", "scripts")
ORTAK = ["ys_docx.py", "ys_xlsx.py", "sablon_analiz.py", "tutarlilik_tarama.py"]


def main() -> int:
    kontrol = "--kontrol" in sys.argv
    hedefler = sorted(glob.glob(os.path.join(KOK, "iso-*-dokuman-seti", "scripts")))
    sapma = 0
    for h in hedefler:
        for f in ORTAK:
            src, dst = os.path.join(KAYNAK, f), os.path.join(h, f)
            ayni = os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False)
            if kontrol:
                if not ayni:
                    sapma += 1
                    print(f"SAPMA: {os.path.relpath(dst, KOK)}")
            elif not ayni:
                shutil.copy2(src, dst)
                print(f"guncellendi: {os.path.relpath(dst, KOK)}")
    print(f"{len(hedefler)} skill, {len(ORTAK)} ortak dosya; sapma: {sapma}" if kontrol
          else f"{len(hedefler)} skill senkron.")
    return 1 if sapma else 0


if __name__ == "__main__":
    raise SystemExit(main())
