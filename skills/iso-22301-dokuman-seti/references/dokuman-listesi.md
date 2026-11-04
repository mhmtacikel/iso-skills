# ISO 22301:2019 — Üretilecek Doküman Listesi

## İçindekiler

- 00 — Kapsam ve El Kitabı
- 01 — Politikalar
- 02 — Prosedürler
- 03 — Analiz ve Değerlendirme (Excel)
  - BIA'nın zorunlu sütunları
- 04 — Planlar
- 05 — Formlar
- 07 — Denetim Hazırlık
- Sayısal beklenti

`Z` = standardın açıkça dokümante edilmiş bilgi olarak istediği. `U` = uygulamada
denetçinin beklediği. Sade set: < 50 çalışan, tek lokasyon, düşük karmaşıklık.

---

## 00 — Kapsam ve El Kitabı

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSYS-EK-01 | İSYS El Kitabı | Word | 4.4 | U | U |
| İSYS-PL-00 | İSYS Kapsam Dokümanı | Word | **4.3.1 Z**, 4.3.2 | Z | Z |
| İSYS-FR-01 | Bağlam Analizi | Word | 4.1 | U | birleşir→İSYS-LS-06 (tek Word: "Bağlam ve İlgili Taraflar Analizi"; taraf tablosu içinde) |
| İSYS-LS-06 | İlgili Taraflar Analizi | Excel | 4.2.1 | U | U |
| İSYS-LS-03 | Yasal ve Düzenleyici Yükümlülükler Matrisi | Excel | **4.2.2 Z** | Z | Z |

---

## 01 — Politikalar

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSYS-PL-01 | İş Sürekliliği Politikası | Word | **5.2.1 Z**, 5.2.2 | Z | Z |
| İSYS-PL-02 | Risk İştahı ve Kabul Kriterleri Beyanı | Word | 4.3.2, 6.1 | U | birleşir→PL-01 |

---

## 02 — Prosedürler

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSYS-PR-01 | Doküman ve Kayıt Kontrol Prosedürü | Word | **7.5 Z** | Z | Z |
| İSYS-PR-02 | Risk ve Fırsat Yönetimi Prosedürü | Word | 6.1 | U | birleşir→PR-03 |
| İSYS-PR-03 | BIA ve Risk Değerlendirme Metodolojisi | Word | **8.2.1 Z** | Z | Z |
| İSYS-PR-04 | Uygunsuzluk ve Düzeltici Faaliyet Prosedürü | Word | **10.1 Z** | Z | Z |
| İSYS-PR-05 | İç Tetkik Prosedürü | Word | **9.2 Z** | Z | Z |
| İSYS-PR-06 | Yönetimin Gözden Geçirmesi Prosedürü | Word | **9.3 Z** | Z | birleşir→PR-05 |
| İSYS-PR-07 | Tatbikat (Alıştırma) Prosedürü | Word | **8.5 Z** | Z | Z |
| İSYS-PR-08 | Değişiklik Yönetimi Prosedürü | Word | 6.3, 8.1 | U | birleşir→PR-01 |
| İSYS-PR-09 | Tedarikçi Süreklilik Yönetimi Prosedürü | Word | 8.1, 8.3.4 | U | U |
| İSYS-PR-10 | Dokümantasyon ve Yetenek Değerlendirme Prosedürü | Word | **8.6 Z** | Z | birleşir→PR-07 |

---

## 03 — Analiz ve Değerlendirme (Excel)

| Kod | Doküman | Madde | Tam | Sade |
|---|---|---|---|---|
| İSYS-FR-02 | **İş Etki Analizi (BIA)** | **8.2.2 Z** | Z | Z |
| İSYS-FR-03 | Süreklilik Risk Değerlendirmesi | **8.2.3 Z** | Z | Z |
| İSYS-FR-05 | Strateji Seçimi ve Boşluk Analizi | **8.3.2, 8.3.3 Z** | Z | Z |
| İSYS-FR-06 | Kaynak Gereksinimleri Tablosu | **8.3.4 Z** | Z | Z |
| İSYS-LS-01 | Kritik Kaynak ve Sistem Envanteri | 8.3.4 | U | U |
| İSYS-LS-02 | Tedarikçi Kritiklik ve Süreklilik Envanteri | 8.3.4 | U | U |

### BIA'nın zorunlu sütunları
Ayrıntı için `bia-ve-strateji.md` §2. Özetle: faaliyet, sahip, zaman dilimlerine
göre etki, MTPD, RTO, RPO, MBCO, bağımlılıklar (personel/sistem/veri/tedarikçi/
lokasyon/diğer faaliyet), zirve dönem, mevcut yetenek, boşluk.

**RTO < MTPD** kuralını tabloya formülle koy; ihlal edilirse hücre kırmızıya dönsün.

---

## 04 — Planlar

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSYS-PN-01 | Olay Müdahale Yapısı ve Kriz Yönetim Planı | Word | **8.4.2 Z** | Z | Z |
| İSYS-PN-03 | İş Sürekliliği Planları (faaliyet/senaryo bazlı) | Word | **8.4.1, 8.4.4, 8.4.5 Z** | Z | Z |
| İSYS-PN-05 | BİT Süreklilik / Felaket Kurtarma Planı | Word | 8.3.4, 8.4.4 | U | U |
| İSYS-PN-06 | Uyarı ve İletişim Planı | Word | **8.4.3 Z**, 7.4 | Z | Z |
| İSYS-PN-04 | Yıllık Tatbikat Programı | Excel | **8.5 Z** | Z | Z |
| İSYS-PN-07 | Yıllık İç Tetkik Programı | Excel | **9.2.2 Z** | Z | Z |
| İSYS-PN-02 | Farkındalık ve Eğitim Planı | Word + Excel | 7.3 | U | U |

**İş sürekliliği planı kaç tane olmalı?** Tek bir dev plan yerine, öncelikli
faaliyet gruplarına göre 3–6 plan üretmek denetimde ve gerçekte daha iyi çalışır.
Tipik ayrım: (1) BT/sistem kesintisi, (2) lokasyon erişilemezliği, (3) kilit
personel kaybı, (4) tedarikçi kesintisi. Kullanıcının BIA'sına göre belirle.

---

## 05 — Formlar

| Kod | Doküman | Format | Madde |
|---|---|---|---|
| İSYS-FR-04 | İş Sürekliliği Hedefleri ve İzleme Tablosu | Excel | **6.2.2, 9.1 Z** |
| İSYS-FR-07 | Tatbikat Planlama ve Sonuç Raporu Formu | Word | **8.5 Z** |
| İSYS-FR-08 | Olay Kayıt ve Müdahale Formu | Excel | 8.4.2 |
| İSYS-FR-09 | Acil Durum İletişim Listesi (çağrı ağacı) | Excel | **8.4.3 Z** |
| İSYS-FR-10 | İletişim Şablonları (çalışan/müşteri/medya/yetkili) | Word | 8.4.3 |
| İSYS-FR-11 | Dokümantasyon ve Yetenek Değerlendirme Formu | Excel | **8.6 Z** |
| İSYS-FR-12 | Uygunsuzluk ve Düzeltici Faaliyet Takip Formu | Excel | **10.1 Z** |
| İSYS-FR-13 | Yönetimin Gözden Geçirmesi Formu | Word | **9.3 Z** |
| İSYS-FR-14 | İç Tetkik Soru Listesi ve Bulgu Formu | Excel | 9.2 |
| İSYS-LS-04 | Doküman Ana Listesi | Excel | 7.5.3 |
| İSYS-LS-07 | Yetkinlik ve Eğitim Matrisi | Excel | **7.2 Z** |
| İSYS-FR-15 | Rol Kartı (kesinti anında kim ne yapar — cep kartı) | Word | 7.3 |

İletişim listesi (FR-09) en hızlı bayatlayan dokümandır. Formda "son doğrulama
tarihi" sütunu ve üç aylık doğrulama notu bulunsun.

Rol kartı (FR-15) standartta adı geçmez ama 7.3 farkındalığının en güçlü
kanıtıdır: denetçi çalışana "kesinti olsa ne yaparsınız?" diye sorduğunda
cebinden kart çıkması sistemin yaşadığını gösterir.

---

## 07 — Denetim Hazırlık

| Dosya | İçerik |
|---|---|
| `Madde-Kanit-Matrisi.xlsx` | Madde → doküman → kanıt → sorumlu → durum |
| `BIA-Zincir-Kontrolu.xlsx` | Faaliyet → RTO → strateji → kaynak → plan bağlantı kontrolü |
| `Oz-Degerlendirme.xlsx` | Madde bazlı uygunluk durumu |
| `OKUBENI.md` | Ne üretildi, ne eksik, sonraki adımlar |

`BIA-Zincir-Kontrolu.xlsx` bu standarda özgü ve çok değerli: her öncelikli
faaliyetin zincirin sonuna kadar takip edilebildiğini gösterir. Denetçinin
yapacağı testi kullanıcı önceden kendisi yapmış olur.

---

## Sayısal beklenti

| Ölçek | Word | Excel | Toplam |
|---|---|---|---|
| Sadeleştirilmiş | ~14 | ~11 | ~25 |
| Tam set | ~24 | ~16 | ~40 |
