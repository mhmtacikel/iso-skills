#!/usr/bin/env python3
"""
ai-governance-legal envanteri (ai-systems.yaml) <-> YZYS-LS-04 YZ Sistem Envanteri (Excel)
iki yonlu eslestirme.

Sahiplik kurali (iki yonlu senkronun temeli):
  * ai-systems.yaml HUKUKI alanlarin sahibidir: id, name, owner, status, eu_nexus,
    role, role_basis, tier, tier_basis, next_review. Bu alanlar Excel'e YAZILIR,
    Excel'den YAML'a asla geri yazilmaz.
  * Excel 42001 alanlarinin sahibidir: amac disi kullanim, yasak kullanim, karar
    ozerkligi, etkilenen kisi grubu, risk/etki kayit no vb. Bu alanlar YAML'a
    tasinmaz; Excel yeniden uretilirken MEVCUT Excel'den korunur.
  * Ortak anahtar: YAML `id` (sys-NNN) == Excel "Sistem No".

Alt komutlar:
  aktar   YAML'i Excel'e aktarir. --mevcut verilirse 42001 alanlari oradan korunur.
  fark    YAML ile Excel'i karsilastirir; farklari Markdown rapor olarak yazar.
  oneri   Excel'de olup YAML'da olmayan sistemler icin YAML taslagi yazar
          (role/tier BOS - siniflandirma bu betigin isi degildir). ai-systems.yaml'a
          dokunmaz; kullanici onayiyla /ai-governance-legal:ai-inventory add ile eklenir.
  zincir  Her sistem icin risk kaydi + etki degerlendirmesi + (AB baglantisi varsa)
          hukuki siniflandirma kapaliligini kontrol eder.

Ornek:
  python3 envanter_senkron.py aktar --yaml ai-systems.yaml --kurulus "Ornek A.S." \
      --cikti "03_Envanterler/YZYS-LS-04 YZ Sistem Envanteri.xlsx" --mevcut eski.xlsx
  python3 envanter_senkron.py fark --yaml ai-systems.yaml --xlsx envanter.xlsx --rapor fark.md
"""
import argparse
import datetime as dt
import os
import sys

import yaml
from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kayitlar_42001 as K  # noqa: E402

SAYFA = "YZ Sistem Envanteri"

# Envanter sutunlari. kayitlar_42001.py'nin eski surumlerinde ENVANTER_BASLIKLAR
# olmadigi icin liste burada da tanimlidir; betik tek basina calisir.
BASLIKLAR = getattr(K, "ENVANTER_BASLIKLAR", None) or [
    "Sistem No", "Sistem Adı", "Sağlayıcı", "Kuruluşun YZ Rolü",
    "Önemli Değişiklik Yapıldı mı?", "Model Tipi", "Teknik Yaklaşım",
    "Uygulama Alanı", "Amaçlanan Kullanım", "Öngörülebilir Amaç Dışı Kullanım",
    "Yasak Kullanım", "Kullanıcı Grubu", "Etkilenen Kişi Grubu", "Karar Özerkliği",
    "İşlenen Veri Tipleri", "Kişisel Veri", "Özel Nitelikli Veri",
    "Yaşam Döngüsü Aşaması", "Sistem Sahibi", "Teknik Sahip", "Kritiklik",
    "Risk Kaydı No", "Etki Değerlendirmesi No", "AB Bağlantısı", "AB YZ Yasası Rolü",
    "AB YZ Yasası Risk Seviyesi", "Yasal Uyum Matrisi Ref", "Devreye Alma Tarihi",
    "Son Gözden Geçirme", "Sonraki Gözden Geçirme", "Durum"]


def _envanter_yaz(bilgi: dict, satirlar: list, cikti: str) -> str:
    """kayitlar_42001'in surumunden bagimsiz envanter yazici."""
    k = K._kayit(bilgi, "YZ Sistem Envanteri", bilgi.get("kod_env", "YZYS-LS-04"))
    k.bilgi_sayfasi(
        aciklama=("YZYS'nin merkez kaydı. Hem risk değerlendirmesinin hem etki "
                  "değerlendirmesinin girdisidir. Hukuki sütunlar ai-governance-legal "
                  "envanterinden (ai-systems.yaml) aktarılır."),
        kullanim_notu=("Hukuki alanlar YAML'dan gelir, burada değiştirilmez; "
                       "42001 alanları bu dosyanın sahipliğindedir."))
    k.sayfa(SAYFA, BASLIKLAR, satirlar,
            listeler={"Kuruluşun YZ Rolü": K.ROLLER, "Karar Özerkliği": K.OZERKLIK,
                      "Yaşam Döngüsü Aşaması": K.ASAMALAR, "Teknik Yaklaşım": K.YAKLASIMLAR,
                      "Kişisel Veri": ["Yok", "Var", "Özel nitelikli var"],
                      "Özel Nitelikli Veri": ["Yok", "Var", "Belirlenmedi"],
                      "Kritiklik": ["Kritik", "Yüksek", "Orta", "Düşük"],
                      "Durum": ["Aktif", "Pilot", "Planlanan", "Emekli"]},
            durum_sutunu="Durum", bos_satir=40,
            notlar={"AB YZ Yasası Rolü": "ai-inventory classify ile belirlenir. "
                                          "42001 rolüyle AYNI EKSEN DEĞİLDİR."})
    k.ozet_sayfasi("Özet", SAYFA, "Kritiklik", ["Kritik", "Yüksek", "Orta", "Düşük"])
    return k.kaydet(cikti)

# --- AB YZ Yasasi rol/seviye etiketleri (eklenti degeri -> Turkce etiket) --------
ROL_TR = {
    "provider": "Sağlayıcı (provider)",
    "deployer": "Uygulayıcı (deployer)",
    "importer": "İthalatçı (importer)",
    "distributor": "Dağıtıcı (distributor)",
    "authorized_rep": "Yetkili temsilci (authorized representative)",
    "product_manufacturer": "Ürün imalatçısı (product manufacturer)",
}
SEVIYE_TR = {
    "prohibited": "Yasak uygulama",
    "high_risk": "Yüksek riskli",
    "limited": "Sınırlı risk (şeffaflık)",
    "minimal": "Asgari risk",
    "gpai": "Genel amaçlı YZ modeli",
    "gpai_systemic": "Sistemik riskli genel amaçlı YZ modeli",
}
DURUM_TR = {
    "planned": "Planlanan",
    "in_development": "Planlanan",
    "in_production": "Aktif",
    "deprecated": "Emekli",
}
ASAMA_TR = {
    "planned": "Fikir/İnceleme",
    "in_development": "Geliştirme",
    "in_production": "İşletim",
    "deprecated": "Emekliye ayırma",
}
# Karsilastirmada kaba kategori: Pilot ve Aktif ayni "canli" kovasina duser.
DURUM_KOVA = {"Planlanan": "plan", "Pilot": "canli", "Aktif": "canli", "Emekli": "emekli"}

TEYIT = " [teyit — AB YZ Yasası güncel metni]"
BEKLIYOR = "[DOLDURULACAK — /ai-governance-legal:ai-inventory classify ile sınıflandırılacak]"


def yaml_oku(yol: str) -> list[dict]:
    with open(yol, encoding="utf-8") as f:
        veri = yaml.safe_load(f) or {}
    return list(veri.get("systems") or [])


def xlsx_oku(yol: str) -> dict[str, dict]:
    wb = load_workbook(yol, data_only=True)
    if SAYFA not in wb.sheetnames:
        raise SystemExit(f"'{SAYFA}' sayfası bulunamadı: {yol}")
    ws = wb[SAYFA]
    basliklar = [c.value for c in ws[1]]
    kayitlar = {}
    for satir in ws.iter_rows(min_row=2, values_only=True):
        d = {b: ("" if v is None else str(v).strip()) for b, v in zip(basliklar, satir) if b}
        no = d.get("Sistem No", "")
        if no:
            kayitlar[no] = d
    return kayitlar


def _hukuki_alanlar(s: dict) -> dict:
    """YAML kaydindan Excel'e yazilacak hukuki/ortak alanlar."""
    eu = s.get("eu_nexus")
    rol = s.get("role")
    seviye = s.get("tier")
    return {
        "Sistem No": s.get("id", ""),
        "Sistem Adı": s.get("name", ""),
        "Sistem Sahibi": s.get("owner", ""),
        "Durum": DURUM_TR.get(s.get("status", ""), ""),
        "Sonraki Gözden Geçirme": str(s.get("next_review") or ""),
        "AB Bağlantısı": ("Var — [türünü belirtin]" if eu is True else
                          "Yok" if eu is False else "Belirlenmedi"),
        "AB YZ Yasası Rolü": (ROL_TR.get(rol, rol) + TEYIT) if rol else BEKLIYOR,
        "AB YZ Yasası Risk Seviyesi": (SEVIYE_TR.get(seviye, seviye) + TEYIT) if seviye else BEKLIYOR,
    }


def aktar(a) -> None:
    sistemler = yaml_oku(a.yaml)
    mevcut = xlsx_oku(a.mevcut) if a.mevcut else {}
    satirlar = []
    for s in sistemler:
        eski = mevcut.pop(s.get("id", ""), {})
        satir = {b: eski.get(b, "") for b in BASLIKLAR}
        satir.update(_hukuki_alanlar(s))
        # YAML'daki "AB Bağlantısı = Var" ise ve Excel'de turu zaten yaziliysa koru.
        if s.get("eu_nexus") is True and eski.get("AB Bağlantısı", "").startswith("Var"):
            satir["AB Bağlantısı"] = eski["AB Bağlantısı"]
        # Bos 42001 alanlarini YAML'dan tohumla (uzerine yazmadan).
        if not satir["Amaçlanan Kullanım"] and s.get("description"):
            satir["Amaçlanan Kullanım"] = s["description"] + " [YAML açıklamasından — gözden geçirin]"
        if not satir["Yaşam Döngüsü Aşaması"]:
            satir["Yaşam Döngüsü Aşaması"] = ASAMA_TR.get(s.get("status", ""), "")
        if not satir["Yasal Uyum Matrisi Ref"] and s.get("id"):
            satir["Yasal Uyum Matrisi Ref"] = f"YZYS-LS-10 / {s['id']}"
        satirlar.append([satir[b] for b in BASLIKLAR])
    # YAML'da olmayan ama eski Excel'de olan sistemler kaybolmasin: sona ekle.
    for no, eski in mevcut.items():
        satirlar.append([eski.get(b, "") for b in BASLIKLAR])
        print(f"  ! {no} yalnızca Excel'de — korundu; 'oneri' ile YAML taslağı üretin.")
    bilgi = {"kurulus": a.kurulus, "tarih": a.tarih, "revizyon": a.revizyon}
    yol = _envanter_yaz(bilgi, satirlar, a.cikti)
    print(f" -> {yol}  ({len(satirlar)} sistem)")


def _fark_listesi(sistemler: list[dict], excel: dict[str, dict]):
    yalniz_yaml, yalniz_excel, celiski = [], [], []
    ids = set()
    for s in sistemler:
        sid = s.get("id", "")
        ids.add(sid)
        x = excel.get(sid)
        if not x:
            yalniz_yaml.append(s)
            continue
        h = _hukuki_alanlar(s)
        for alan in ("Sistem Adı", "Sistem Sahibi"):
            if h[alan] and x.get(alan) and h[alan] != x[alan]:
                celiski.append((sid, alan, h[alan], x[alan]))
        if DURUM_KOVA.get(h["Durum"]) != DURUM_KOVA.get(x.get("Durum", ""), DURUM_KOVA.get(h["Durum"])):
            celiski.append((sid, "Durum", h["Durum"], x.get("Durum", "")))
        xe = x.get("AB Bağlantısı", "")
        if s.get("eu_nexus") is True and xe.startswith("Yok"):
            celiski.append((sid, "AB Bağlantısı", "Var", xe))
        if s.get("eu_nexus") is False and xe.startswith("Var"):
            celiski.append((sid, "AB Bağlantısı", "Yok", xe))
        for alan, anahtar, sozluk in (("AB YZ Yasası Rolü", "role", ROL_TR),
                                      ("AB YZ Yasası Risk Seviyesi", "tier", SEVIYE_TR)):
            deger = s.get(anahtar)
            if deger and sozluk.get(deger, deger) not in x.get(alan, ""):
                celiski.append((sid, alan, sozluk.get(deger, deger), x.get(alan, "")))
    for no, x in excel.items():
        if no not in ids:
            yalniz_excel.append(x)
    return yalniz_yaml, yalniz_excel, celiski


def fark(a) -> None:
    sistemler = yaml_oku(a.yaml)
    excel = xlsx_oku(a.xlsx)
    yy, ye, cel = _fark_listesi(sistemler, excel)
    r = [f"# Envanter Fark Raporu — {dt.date.today().isoformat()}", "",
         f"- YAML: `{os.path.basename(a.yaml)}` ({len(sistemler)} sistem)",
         f"- Excel: `{os.path.basename(a.xlsx)}` ({len(excel)} sistem)", "",
         "Sahiplik: hukuki alanlarda YAML, 42001 alanlarında Excel esastır. "
         "Çelişkide YAML değeri doğru kabul edilir ve Excel `aktar` ile güncellenir; "
         "YAML değeri yanlışsa önce `/ai-governance-legal:ai-inventory edit <id>` çalıştırılır.", ""]
    r += ["## Yalnızca YAML'da (Excel'e aktarılmamış)", ""]
    r += [f"- {s.get('id')} — {s.get('name')}" for s in yy] or ["- yok"]
    r += ["", "## Yalnızca Excel'de (hukuki envantere girmemiş)", ""]
    r += [f"- {x.get('Sistem No')} — {x.get('Sistem Adı')} → `oneri` ile taslak üretin, "
          f"ardından ai-inventory add + classify" for x in ye] or ["- yok"]
    r += ["", "## Alan çelişkileri", ""]
    if cel:
        r += ["| Sistem | Alan | YAML | Excel |", "|---|---|---|---|"]
        r += [f"| {a_} | {b} | {c} | {d} |" for a_, b, c, d in cel]
    else:
        r += ["- yok"]
    metin = "\n".join(r) + "\n"
    if a.rapor:
        with open(a.rapor, "w", encoding="utf-8") as f:
            f.write(metin)
        print(f" -> {a.rapor}")
    else:
        print(metin)
    print(f"Özet: yalnız YAML={len(yy)}, yalnız Excel={len(ye)}, çelişki={len(cel)}")


def oneri(a) -> None:
    sistemler = yaml_oku(a.yaml) if a.yaml and os.path.exists(a.yaml) else []
    excel = xlsx_oku(a.xlsx)
    ids = {s.get("id") for s in sistemler}
    bugun = dt.date.today().isoformat()
    taslak = []
    for no, x in excel.items():
        if no in ids:
            continue
        durum = {"Aktif": "in_production", "Pilot": "in_production",
                 "Planlanan": "planned", "Emekli": "deprecated"}.get(x.get("Durum", ""), "planned")
        ab = x.get("AB Bağlantısı", "")
        taslak.append({
            "id": no if no.startswith("sys-") else f"[ATANACAK — Excel no: {no}]",
            "name": x.get("Sistem Adı", ""),
            "owner": x.get("Sistem Sahibi", ""),
            "description": x.get("Amaçlanan Kullanım", ""),
            "status": durum,
            "eu_nexus": True if ab.startswith("Var") else False if ab.startswith("Yok") else None,
            "role": None, "role_basis": None, "tier": None, "tier_basis": None,
            "obligations_assessed": False,
            "obligations_note": "Sınıflandırılmadı — /ai-governance-legal:ai-inventory classify",
            "created": bugun, "updated": bugun,
        })
    with open(a.cikti, "w", encoding="utf-8") as f:
        f.write("# TASLAK — ai-systems.yaml'a OTOMATİK EKLENMEZ.\n"
                "# Her kayıt kullanıcı onayıyla /ai-governance-legal:ai-inventory add ile eklenir;\n"
                "# role/tier alanları bilerek boştur (sınıflandırma görünür walk-through ister).\n")
        yaml.safe_dump({"systems": taslak}, f, allow_unicode=True, sort_keys=False)
    print(f" -> {a.cikti}  ({len(taslak)} öneri)")


def zincir(a) -> None:
    excel = xlsx_oku(a.xlsx)
    sistemler = {s.get("id"): s for s in yaml_oku(a.yaml)} if a.yaml else {}
    r = ["# Çift Zincir + Hukuki Sınıflandırma Kontrolü", "",
         "| Sistem | Ad | Risk kaydı | Etki değ. | AB bağlantısı | Hukuki sınıflandırma | Sonuç |",
         "|---|---|---|---|---|---|---|"]
    acik = 0
    for no, x in excel.items():
        risk = x.get("Risk Kaydı No", "")
        etki = x.get("Etki Değerlendirmesi No", "")
        ab = x.get("AB Bağlantısı", "")
        s = sistemler.get(no, {})
        sinif = "var" if (s.get("role") and s.get("tier")) else (
            "gerekmez" if ab.startswith("Yok") else "EKSİK")
        # Taslak/onay bekleyen kayit kapali sayilmaz; "Gerekmedi" gerekceliyse kapalidir.
        def _acik(v: str) -> bool:
            v = v.lower()
            return (not v or "doldurulacak" in v or "taslak" in v or "onay bekl" in v
                    or v.startswith("yok"))
        eksik = [e for e, v in (("risk", risk), ("etki", etki)) if _acik(v)]
        if sinif == "EKSİK":
            eksik.append("sınıflandırma")
        sonuc = "kapalı" if not eksik else "AÇIK: " + ", ".join(eksik)
        acik += bool(eksik)
        r.append(f"| {no} | {x.get('Sistem Adı','')} | {risk or '—'} | {etki or '—'} | "
                 f"{ab or '—'} | {sinif} | {sonuc} |")
    r += ["", f"{acik} / {len(excel)} sistemde zincir açık."]
    metin = "\n".join(r) + "\n"
    if a.rapor:
        with open(a.rapor, "w", encoding="utf-8") as f:
            f.write(metin)
        print(f" -> {a.rapor}")
    else:
        print(metin)


def main() -> None:
    ap = argparse.ArgumentParser(description="ai-systems.yaml <-> YZ Sistem Envanteri senkronu")
    alt = ap.add_subparsers(dest="komut", required=True)

    p = alt.add_parser("aktar")
    p.add_argument("--yaml", required=True)
    p.add_argument("--kurulus", required=True)
    p.add_argument("--cikti", required=True)
    p.add_argument("--mevcut", default="")
    p.add_argument("--tarih", default="")
    p.add_argument("--revizyon", default="00")
    p.set_defaults(f=aktar)

    p = alt.add_parser("fark")
    p.add_argument("--yaml", required=True)
    p.add_argument("--xlsx", required=True)
    p.add_argument("--rapor", default="")
    p.set_defaults(f=fark)

    p = alt.add_parser("oneri")
    p.add_argument("--xlsx", required=True)
    p.add_argument("--yaml", default="")
    p.add_argument("--cikti", required=True)
    p.set_defaults(f=oneri)

    p = alt.add_parser("zincir")
    p.add_argument("--xlsx", required=True)
    p.add_argument("--yaml", default="")
    p.add_argument("--rapor", default="")
    p.set_defaults(f=zincir)

    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
