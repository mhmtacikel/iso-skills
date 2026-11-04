#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dogrula.py — iso-* skill'lerini yayinlamadan once dogrular, istenirse paketler.

    python _ortak/dogrula.py            # yalniz dogrula
    python _ortak/dogrula.py --paketle  # dogrula + dist/<skill>.zip uret

Kontroller (Agent Skills spesifikasyonu + Anthropic en iyi uygulamalari):
  - frontmatter yalniz name/description/license/compatibility/metadata/allowed-tools
  - name = klasor adi, kucuk harf-rakam-tire, <=64
  - description 1..1024 karakter, XML etiketi yok
  - SKILL.md govdesi <= 500 satir
  - 100 satiri asan references dosyalarinda "## İçindekiler"
  - SKILL.md'de atif verilen references/scripts/assets dosyalari mevcut
  - Python betikleri derleniyor; ortak motor kopyalari senkron
"""
import glob
import os
import py_compile
import re
import subprocess
import sys
import zipfile

import yaml

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IZINLI = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def dogrula(d: str) -> list:
    hatalar = []
    ad = os.path.basename(d)
    s = open(os.path.join(d, "SKILL.md"), encoding="utf-8").read()
    if not s.startswith("---\n"):
        return [f"{ad}: frontmatter ilk satirda degil"]
    _, fm_txt, govde = s.split("---", 2)
    fm = yaml.safe_load(fm_txt)
    fazla = set(fm) - IZINLI
    if fazla:
        hatalar.append(f"{ad}: izinsiz alan {fazla}")
    if fm.get("name") != ad or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", ad) or len(ad) > 64:
        hatalar.append(f"{ad}: name gecersiz ({fm.get('name')})")
    desc = fm.get("description", "")
    if not (1 <= len(desc) <= 1024) or re.search(r"<[a-zA-Z/]", desc):
        hatalar.append(f"{ad}: description {len(desc)} karakter / XML")
    if len(govde.strip("\n").split("\n")) > 500:
        hatalar.append(f"{ad}: SKILL.md govdesi 500 satiri asiyor")
    for ref in sorted(set(re.findall(r"`((?:references|scripts|assets)/[\w\-./]+)`", s))):
        if "<" in ref or not os.path.exists(os.path.join(d, ref)):
            hatalar.append(f"{ad}: atif verilen dosya yok: {ref}")
    for r in glob.glob(os.path.join(d, "references", "*.md")):
        t = open(r, encoding="utf-8").read()
        if len(t.split("\n")) > 100 and "## İçindekiler" not in t:
            hatalar.append(f"{ad}: icindekiler yok: {os.path.basename(r)}")
    for py in glob.glob(os.path.join(d, "scripts", "*.py")):
        try:
            py_compile.compile(py, doraise=True)
        except py_compile.PyCompileError as e:
            hatalar.append(f"{ad}: derlenmiyor {os.path.basename(py)}: {e.msg[:80]}")
    return hatalar


def paketle(d: str) -> str:
    os.makedirs(os.path.join(KOK, "dist"), exist_ok=True)
    hedef = os.path.join(KOK, "dist", os.path.basename(d) + ".zip")
    with zipfile.ZipFile(hedef, "w", zipfile.ZIP_DEFLATED) as z:
        for kok, dizinler, dosyalar in os.walk(d):
            dizinler[:] = [x for x in dizinler if x not in ("__pycache__", ".git")]
            for f in dosyalar:
                if f.endswith(".pyc"):
                    continue
                yol = os.path.join(kok, f)
                z.write(yol, os.path.relpath(yol, os.path.dirname(d)).replace(os.sep, "/"))
    return hedef


def main() -> int:
    skilller = sorted(x for x in glob.glob(os.path.join(KOK, "skills", "iso-*")) if os.path.isdir(x))
    hatalar = []
    for d in skilller:
        hatalar += dogrula(d)
    r = subprocess.run([sys.executable, os.path.join(KOK, "_ortak", "senkron.py"), "--kontrol"],
                       capture_output=True, text=True)
    if r.returncode:
        hatalar.append("ortak motor senkron degil:\n" + r.stdout)
    for h in hatalar:
        print("HATA", h)
    print(f"{len(skilller)} skill, {len(hatalar)} hata")
    if hatalar:
        return 1
    if "--paketle" in sys.argv:
        for d in skilller:
            print("paket:", os.path.relpath(paketle(d), KOK))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
