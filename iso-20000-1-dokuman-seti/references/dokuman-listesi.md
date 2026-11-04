# ISO/IEC 20000-1:2018 — Üretilecek Doküman Listesi

## İçindekiler

- 00 — Kapsam ve Planlama
- 01 — Politikalar
- 02 — Prosedürler (Madde 8'in gövdesi)
- 03 — Kataloglar ve Envanterler (Excel)
  - Hizmet kataloğunun zorunlu sütunları
  - CMDB'nin zorunlu sütunları
- 04 — Formlar ve Kayıtlar
- 07 — Denetim Hazırlık
- Sayısal beklenti

`Z` = zorunlu dokümante bilgi. `U` = denetimde beklenen.
Sade set: tek hizmet grubu, < 30 kişilik BT ekibi, dış müşteri yok veya az.

---

## 00 — Kapsam ve Planlama

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| HYYS-EK-01 | HYYS El Kitabı | Word | 4.4 | U | U |
| HYYS-PL-00 | HYYS Kapsam Dokümanı | Word | **4.3 Z** | Z | Z |
| HYYS-PN-01 | **Hizmet Yönetim Planı** | Word | **6.3 Z** | Z | Z |
| HYYS-FR-01 | Bağlam Analizi | Word | 4.1 | U | birleşir |
| HYYS-LS-06 | İlgili Taraflar Analizi | Excel | 4.2 | U | U |

---

## 01 — Politikalar

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| HYYS-PL-01 | Hizmet Yönetimi Politikası | Word | **5.2 Z** | Z | Z |
| HYYS-PL-02 | Değişiklik ve Sürüm Politikası | Word | 8.5.1, 8.5.3 | U | birleşir→PR-04 |
| HYYS-PL-03 | Hizmet Bilgi Güvenliği Politikası | Word | 8.7.3 | U | 27001 varsa atıf |

---

## 02 — Prosedürler (Madde 8'in gövdesi)

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| HYYS-PR-00 | İşletim Planlama ve Kontrol Prosedürü | Word | 8.1 | U | birleşir→PN-01 |
| HYYS-PR-01 | Olay ve Hizmet Talebi Yönetimi Prosedürü | Word | **8.6.1, 8.6.2** | Z | Z |
| HYYS-PR-02 | Hizmet Seviyesi Yönetimi Prosedürü | Word | **8.3.3** | Z | Z |
| HYYS-PR-03 | Problem Yönetimi Prosedürü | Word | **8.6.3** | Z | Z |
| HYYS-PR-04 | Değişiklik Yönetimi Prosedürü | Word | **8.5.1** | Z | Z |
| HYYS-PR-05 | Sürüm ve Dağıtım Yönetimi Prosedürü | Word | **8.5.3** | Z | birleşir→PR-04 |
| HYYS-PR-06 | Kapasite Yönetimi Prosedürü | Word | **8.4.3** | Z | Z |
| HYYS-PR-07 | Hizmet Erişilebilirliği Yönetimi Prosedürü | Word | 8.7.1 | U | birleşir→PR-02 |
| HYYS-PR-08 | Konfigürasyon Yönetimi Prosedürü | Word | **8.2.6** | Z | Z |
| HYYS-PR-09 | Yeni/Değiştirilen Hizmetlerin Tasarımı ve Geçişi | Word | **8.5.2** | Z | Z |
| HYYS-PR-10 | İş İlişkileri ve Müşteri Yönetimi Prosedürü | Word | 8.3.1, 8.3.2 | U | U |
| HYYS-PR-11 | Tedarikçi Yönetimi Prosedürü | Word | **8.3.4, 8.2.3** | Z | Z |
| HYYS-PR-12 | Bütçeleme ve Muhasebeleştirme Prosedürü | Word | 8.4.1 | U | — |
| HYYS-PR-13 | Hizmet Raporlama Prosedürü | Word | **8.4.2** | Z | Z |
| HYYS-PR-14 | Risk ve Fırsat Yönetimi Prosedürü | Word | 6.1 | U | birleşir→PN-01 |
| HYYS-PR-15 | Doküman ve Bilgi Yönetimi Prosedürü | Word | **7.5 Z**, 7.5.4 | Z | Z |
| HYYS-PR-16 | İç Tetkik ve YGG Prosedürü | Word | **9.2, 9.3 Z** | Z | Z |
| HYYS-PR-17 | Uygunsuzluk ve Düzeltici Faaliyet Prosedürü | Word | **10.1 Z** | Z | Z |
| HYYS-PN-04 | Hizmet Sürekliliği Planı | Word | 8.7.2 | U | U |

Sade sette 19 prosedür 11'e iner. Birleştirme yaparken **olay/problem ayrımını
asla birleştirme** — bu ikisi ayrı süreç kalmalı.

---

## 03 — Kataloglar ve Envanterler (Excel)

| Kod | Doküman | Madde | Tam | Sade |
|---|---|---|---|---|
| HYYS-LS-01 | **Hizmet Kataloğu** | **8.2.4 Z** | Z | Z |
| HYYS-LS-04 | **SLA Kayıt Listesi ve Hedef Tablosu** | **8.3.3 Z** | Z | Z |
| HYYS-LS-08 | OLA / UC Hizalama Tablosu | 8.3.3, 8.3.4 | U | U |
| HYYS-LS-03 | **Konfigürasyon Öğeleri (CMDB)** | **8.2.6 Z** | Z | Z |
| HYYS-LS-02 | Hizmet Varlık Envanteri | 8.2.5 | U | birleşir→LS-03 |
| HYYS-LS-05 | Tedarikçi ve Dış Proses Envanteri | **8.2.3, 8.3.4 Z** | Z | Z |
| HYYS-LS-09 | Bilinen Hata Veritabanı | 8.6.3 | U | U |
| HYYS-LS-07 | Yetkinlik ve Eğitim Matrisi | **7.2 Z** | Z | Z |
| HYYS-LS-10 | Doküman Ana Listesi | 7.5.3 | U | U |

### Hizmet kataloğunun zorunlu sütunları
`Hizmet Kodu | Hizmet Adı | Kategori | Müşteri diliyle açıklama | Hedef kullanıcı |
Hizmet Sahibi | Teknik Sahip | Bağımlı KÖ'ler | Bağımlı hizmetler | Tedarikçi
bağımlılığı | Hizmet saatleri | Destek saatleri | İlgili SLA | Kritiklik |
Ücretlendirme | Devreye alma | Durum | Son gözden geçirme`

### CMDB'nin zorunlu sütunları
Ayrıntı `madde-8-surecler.md` §8.2.6. **"Son doğrulama tarihi" ve "doğrulayan"
sütunlarını atlama** — 8.2.6'nın doğrulama gerekliliğinin tek kanıtıdır.

---

## 04 — Formlar ve Kayıtlar

| Kod | Doküman | Format | Madde |
|---|---|---|---|
| HYYS-FR-02 | Olay ve Talep Kayıt Formu / Kayıt Defteri | Excel | 8.6.1, 8.6.2 |
| HYYS-FR-03 | Problem Kayıt ve Kök Neden Analizi Formu | Excel | 8.6.3 |
| HYYS-FR-04 | Hizmet Yönetimi Hedefleri ve İzleme Tablosu | Excel | **6.2, 9.1 Z** |
| HYYS-FR-05 | Değişiklik Talep Formu ve CAB Kayıt Defteri | Excel | **8.5.1 Z** |
| HYYS-FR-06 | Hizmet Raporu Şablonu (SLA performans) | Word + Excel | **8.4.2 Z** |
| HYYS-FR-07 | Uygunsuzluk ve Düzeltici Faaliyet Takip Formu | Excel | **10.1 Z** |
| HYYS-FR-08 | Yönetimin Gözden Geçirmesi Formu | Word | **9.3 Z** |
| HYYS-FR-09 | İyileştirme Kayıt Defteri (CSI Register) | Excel | 10.2 |
| HYYS-FR-10 | Kapasite Planı ve Trend Tablosu | Excel | **8.4.3 Z** |
| HYYS-FR-11 | Müşteri Memnuniyeti ve Şikâyet Kayıt Formu | Excel | 8.3.1, 9.3.2 |
| HYYS-FR-12 | Sürüm ve Dağıtım Kayıt Defteri | Excel | **8.5.3 Z** |
| HYYS-FR-13 | İç Tetkik Soru Listesi ve Bulgu Formu | Excel | 9.2 |
| HYYS-FR-14 | Hizmet Geçiş (Transition) Kontrol Listesi | Excel | **8.5.2 Z** |
| HYYS-PN-03 | Yıllık İç Tetkik Programı | Excel | **9.2 Z** |
| HYYS-PN-02 | Farkındalık ve Eğitim Planı | Word + Excel | 7.3 |
| HYYS-PN-05 | İletişim Planı | Word | 7.4 |

Şablonlarda **öncelik matrisi** (etki × aciliyet) ve **SLA hedef tablosu**
mutlaka yer almalı; bu iki tablo olmadan olay yönetimi denetlenemez.

---

## 07 — Denetim Hazırlık

| Dosya | İçerik |
|---|---|
| `Madde-Kanit-Matrisi.xlsx` | Madde → doküman → kanıt → sorumlu → durum |
| `Hizmet-Zincir-Kontrolu.xlsx` | Katalog → SLA → OLA/UC → ölçüm → rapor bağlantı kontrolü |
| `SLA-OLA-UC-Hizalama.xlsx` | Hedef çelişkisi taraması |
| `Oz-Degerlendirme.xlsx` | Madde bazlı uygunluk durumu |
| `OKUBENI.md` | Ne üretildi, ne eksik, sonraki adımlar |

`SLA-OLA-UC-Hizalama.xlsx` bu standarda özgü ve çok işe yarar: müşteriye verilen
sözle iç/dış anlaşmalar arasındaki her çelişkiyi görünür kılar.

---

## Sayısal beklenti

| Ölçek | Word | Excel | Toplam |
|---|---|---|---|
| Sadeleştirilmiş | ~16 | ~13 | ~29 |
| Tam set | ~27 | ~20 | ~47 |
