# ISO/IEC 20000-1:2018 Madde 8 — Hizmet Yönetimi Süreçleri

## İçindekiler

- Madde 8 haritası
- 8.2.4 Hizmet kataloğu — zincirin başlangıcı
- 8.3.3 SLA — ölçülebilirlik testi
  - SLA–OLA–UC hizalaması
- 8.6.1 / 8.6.2 / 8.6.3 — Olay, Talep, Problem ayrımı
  - Önceliklendirme matrisi
- 8.5.1 / 8.5.3 — Değişiklik ve Sürüm ayrımı
- 8.5.2 Yeni veya değiştirilen hizmetlerin tasarımı ve geçişi
- 8.2.6 Konfigürasyon yönetimi (CMDB)
- 8.4.2 Hizmet raporlaması
- 8.2.3 Diğer taraflarca işletilen prosesler

Bu standardın ağırlık merkezi. Diğer Annex SL standartlarında Madde 8 birkaç
paragraftır; burada standardın yarısıdır ve denetimin de yarısıdır.

## Madde 8 haritası

| Madde | Süreç / Konu | Üretilecek doküman |
|---|---|---|
| 8.1 | İşletim planlama ve kontrol | HYYS-PR-00 |
| 8.2.1 | Hizmet sunum modeli | HYYS-EK-01 §Hizmet Modeli |
| 8.2.2 | Hizmet yaşam döngüsünün planlanması | HYYS-PN-01 Hizmet Yönetim Planı |
| 8.2.3 | **Diğer taraflarca işletilen prosesler** | HYYS-PR-11 + HYYS-LS-05 |
| 8.2.4 | **Hizmet kataloğu yönetimi** | HYYS-LS-01 Hizmet Kataloğu |
| 8.2.5 | Varlık yönetimi | HYYS-LS-02 Hizmet Varlık Envanteri |
| 8.2.6 | **Konfigürasyon yönetimi (CMDB)** | HYYS-PR-08 + HYYS-LS-03 |
| 8.3.1 | İş ilişkileri yönetimi | HYYS-PR-10 |
| 8.3.2 | Hizmet gereksinimleri yönetimi | HYYS-PR-10 §Gereksinim |
| 8.3.3 | **Hizmet seviyesi yönetimi (SLA)** | HYYS-PR-02 + HYYS-LS-04 |
| 8.3.4 | **Tedarikçi yönetimi** | HYYS-PR-11 |
| 8.4.1 | Bütçeleme ve muhasebeleştirme | HYYS-PR-12 |
| 8.4.2 | **Hizmet raporlaması** | HYYS-PR-13 + HYYS-FR-06 |
| 8.4.3 | **Kapasite yönetimi** | HYYS-PR-06 |
| 8.5.1 | **Değişiklik yönetimi** | HYYS-PR-04 |
| 8.5.2 | **Yeni veya değiştirilen hizmetlerin tasarımı ve geçişi** | HYYS-PR-09 |
| 8.5.3 | **Sürüm ve dağıtım yönetimi** | HYYS-PR-05 |
| 8.6.1 | **Olay yönetimi** | HYYS-PR-01 |
| 8.6.2 | **Hizmet talebi yönetimi** | HYYS-PR-01 §Talep (veya ayrı) |
| 8.6.3 | **Problem yönetimi** | HYYS-PR-03 |
| 8.7.1 | Hizmet erişilebilirliği yönetimi | HYYS-PR-07 |
| 8.7.2 | Hizmet sürekliliği yönetimi | HYYS-PN-04 |
| 8.7.3 | Bilgi güvenliği yönetimi | HYYS-PL-03 (veya 27001 setine atıf) |

---

## 8.2.4 Hizmet kataloğu — zincirin başlangıcı

Katalog olmadan SLA yazılamaz. Her hizmet kaydı şunları içermeli:

`Hizmet Kodu | Hizmet Adı | Kategori | Açıklama (müşterinin anlayacağı dilde) |
Hedef Kullanıcı Grubu | Hizmet Sahibi | Teknik Sahip | Bağımlı KÖ'ler |
Bağımlı Diğer Hizmetler | Tedarikçi Bağımlılığı | Hizmet Saatleri |
Destek Saatleri | İlgili SLA | Kritiklik | Maliyet/Ücretlendirme |
Devreye Alma Tarihi | Durum | Son Gözden Geçirme`

**"Müşterinin anlayacağı dil"** vurgusu önemli: katalog teknik envanter değildir.
"Exchange Server 2019 kümesi" bir hizmet değil; "Kurumsal E-posta ve Takvim"
bir hizmettir.

**Kritiklik** sütunu SLA seviyesini ve sürekliliği belirler; boş bırakılamaz.

---

## 8.3.3 SLA — ölçülebilirlik testi

Her SLA hedefi beş bileşeni taşımalı, biri eksikse hedef değildir:

| Bileşen | Örnek |
|---|---|
| Metrik | Aylık hizmet erişilebilirliği |
| Eşik | ≥ %99,5 |
| Ölçüm dönemi | Takvim ayı |
| Ölçüm kaynağı | Zabbix izleme sistemi, aylık erişilebilirlik raporu |
| İstisna | Duyurulmuş planlı bakım pencereleri (ayda azami 4 saat, en az 5 iş günü önce duyurulur) hariç tutulur |

SLA'nın içermesi gerekenler: taraflar, kapsanan hizmetler, hizmet saatleri,
hedefler tablosu, önceliklendirme matrisi, yükseltme (escalation) yolu,
raporlama sıklığı ve formatı, gözden geçirme sıklığı, istisnalar, değişiklik
prosedürü, geçerlilik süresi.

### SLA–OLA–UC hizalaması

Bu üçünün **matematiksel olarak tutarlı** olması gerekir:

```
Müşteriye SLA: P1 çözüm süresi 4 saat
  ├─ İç ekip OLA: BT Operasyon ilk müdahale 30 dk, çözüm 3 saat
  └─ Tedarikçi UC: Donanım sağlayıcı yerinde müdahale ≤ 2 saat
```

SLA 4 saat vaat ederken tedarikçi sözleşmesi 8 saat diyorsa bu tutarsızlıktır.
Üretim sonunda hizalama tablosunu çıkar ve çelişkileri `OKUBENI.md`'de raporla.

---

## 8.6.1 / 8.6.2 / 8.6.3 — Olay, Talep, Problem ayrımı

En sık karıştırılan üçlü. Ayrı süreç, ayrı kayıt, ayrı metrik olmalı:

| | Olay (8.6.1) | Hizmet Talebi (8.6.2) | Problem (8.6.3) |
|---|---|---|---|
| Tanım | Hizmetin planlanmamış kesintisi veya kalite düşüşü | Standart, önceden onaylanmış istek | Bir/daha fazla olayın kök nedeni |
| Hedef | En hızlı normale dönüş | Standart sürede karşılama | Nedeni ortadan kaldırma |
| Tetikleyici | Arıza, uyarı, kullanıcı bildirimi | Kullanıcı isteği | Tekrarlayan olay, büyük olay, proaktif analiz |
| Ana metrik | Çözüm süresi, SLA uyumu | Karşılama süresi | Kök neden bulma süresi, tekrar oranı |
| Kapanış kriteri | Hizmet normale döndü | İstek karşılandı | Kök neden giderildi veya bilinen hata kaydedildi |

**Büyük olay (major incident)** için ayrı bir yol tanımlanmalı: eşik, bildirim
zinciri, kriz iletişimi, olay sonrası inceleme. Standart olay yönetiminin içinde
ama ayrı tetikleyicilerle.

**Bilinen hata (known error)** kaydı problem yönetiminin çıktısıdır: kök neden
bulunmuş ama henüz kalıcı çözüm uygulanmamış durumlar. Geçici çözüm (workaround)
ile birlikte kaydedilir ve hizmet masası bunu kullanır. Bilinen hata veritabanı
olmayan bir problem yönetimi eksiktir.

### Önceliklendirme matrisi

Olay önceliği **etki × aciliyet** ile belirlenir. Matris dokümanda olmalı:

| Etki ↓ / Aciliyet → | Yüksek | Orta | Düşük |
|---|---|---|---|
| **Yüksek** (tüm kullanıcılar / kritik hizmet) | P1 | P2 | P3 |
| **Orta** (birim / önemli hizmet) | P2 | P3 | P4 |
| **Düşük** (tek kullanıcı / yardımcı hizmet) | P3 | P4 | P4 |

Her önceliğe ilk müdahale ve çözüm hedefi bağlanır; bu hedefler SLA'daki
hedeflerle aynı olmalıdır.

---

## 8.5.1 / 8.5.3 — Değişiklik ve Sürüm ayrımı

**Değişiklik yönetimi (8.5.1)** neyin onaylandığını yönetir:
- Değişiklik tipleri: standart (önceden onaylı), normal, acil
- Değerlendirme: risk, etki, kaynak, geri alma planı
- Onay yetkisi: tipine göre kim onaylar (CAB, süreç sahibi, otomatik)
- **Acil değişiklik için ayrı mekanizma** — standart bunu açıkça ister
- Değişiklik sonrası gözden geçirme
- Başarısız değişikliklerin analizi

**Sürüm ve dağıtım yönetimi (8.5.3)** nasıl canlıya alındığını yönetir:
- Sürüm politikası (sıklık, pencere, paketleme)
- Test ve kabul kriterleri
- Dağıtım planı ve geri alma (rollback) planı
- Canlıya alma sonrası doğrulama
- Başarısız dağıtımda izlenecek yol

Değişiklik kaydı ile sürüm kaydı ayrı numaralandırılmalı ve birbirine
referans vermeli.

---

## 8.5.2 Yeni veya değiştirilen hizmetlerin tasarımı ve geçişi

En sık atlanan maddedir. Gerekenler: hizmetin planlanması, gereksinimlerin
belirlenmesi, kabul kriterleri, test, geçiş planı, devreye alma sonrası gözden
geçirme, katalog ve SLA'nın güncellenmesi.

Kuruluş "yeni hizmet çıkarmıyoruz" dese bile prosedür olmalı — mevcut hizmette
önemli değişiklik de bu maddeye girer.

---

## 8.2.6 Konfigürasyon yönetimi (CMDB)

Gereklilikler: KÖ tipi ve ilişkilerinin tanımlanması, KÖ'lerin kaydedilmesi,
değişikliklerin kontrol edilmesi, bilginin doğruluğunun **periyodik olarak
doğrulanması** ve düzeltilmesi.

CMDB kaydı: `KÖ No | KÖ Adı | Tip | Kategori | Sahip | Durum | Sürüm |
Lokasyon/Ortam | İlişkili Hizmet(ler) | Üst KÖ | Alt KÖ'ler | Bağımlılıklar |
Tedarikçi | Garanti/Destek Bitiş | Son Değişiklik No | Son Doğrulama Tarihi |
Doğrulayan`

Son iki sütun 8.2.6'nın doğrulama gerekliliğinin kanıtıdır ve en sık boş kalan
alanlardır. Doğrulama sıklığını prosedürde belirt (tipik: kritik KÖ'ler üç ayda
bir, diğerleri yılda bir).

---

## 8.4.2 Hizmet raporlaması

Her rapor için tanımlanmalı: rapor adı, amacı, hedef kitlesi, içeriği, veri
kaynağı, sıklığı, formatı, sorumlusu, dağıtım yolu.

Asgari rapor seti:

| Rapor | Sıklık | Alıcı | İçerik |
|---|---|---|---|
| SLA performans raporu | Aylık | Müşteri, hizmet sahibi | Hedef vs. gerçekleşen, ihlaller, nedenler |
| Olay ve talep raporu | Aylık | HYYS yöneticisi, BT müdürü | Hacim, öncelik dağılımı, çözüm süreleri, tekrar edenler |
| Problem raporu | Aylık | HYYS yöneticisi | Açık problemler, bilinen hatalar, kapatılanlar |
| Değişiklik raporu | Aylık | CAB, BT müdürü | Sayı, başarı oranı, acil değişiklik oranı, başarısızlık nedenleri |
| Kapasite ve trend raporu | Üç aylık | BT müdürü | Kullanım trendi, tahmin, eşik aşımları |
| Tedarikçi performans raporu | Üç aylık | Satın alma, HYYS yöneticisi | UC hedeflerine uyum |
| HYYS yönetim raporu | Altı aylık | Üst yönetim | Hedefler, tetkik, DÖF, iyileştirme |

---

## 8.2.3 Diğer taraflarca işletilen prosesler

Standart burada nettir ve kapsam kararını doğrudan etkiler. Bir hizmet yönetimi
prosesi başka bir tarafça işletiliyorsa kuruluş şunları göstermeli:

- Prosesin hangi tarafça işletildiği ve kapsamı
- Sorumluluk ve yetki dağılımı (arayüz tanımı)
- Prosesin performansının nasıl izlendiği ve ölçüldüğü
- Performans yetersizse müdahale hakkı ve mekanizması
- Sözleşme veya anlaşmadaki karşılığı

**Kuruluş, HYYS'nin bütününün yönetişiminden sorumludur ve bunu devredemez.**
Tamamen dış kaynaklı bir hizmet üzerinde yönetişim gösterilemiyorsa o hizmet
kapsama alınmamalıdır. Bunu kullanıcıya net söyle — kapsam hatası belgelendirme
sürecinin en pahalı hatasıdır.

Kayıt tablosu: `Proses | İşleten taraf | Sözleşme/Anlaşma | Arayüz tanımı |
İzleme yöntemi | Ölçüm sıklığı | Performans hedefi | Müdahale mekanizması |
Sorumlu | Son gözden geçirme`
