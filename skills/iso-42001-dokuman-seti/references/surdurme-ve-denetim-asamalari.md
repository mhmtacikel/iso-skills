# Sürdürme modu ve denetim aşamaları

## İçindekiler

- 1. Çalışma modunu belirle
- 2. Sürdürme modu — olay güdümlü akışlar
  - 2a. Yeni YZ kullanım talebi
  - 2b. Mevcut sistemde değişiklik
  - 2c. Yeni düzenleme veya yürürlük tarihi değişikliği
  - 2d. YZ olayı veya endişe bildirimi
  - 2e. Sistemin emekliye ayrılması
- 3. Sürdürme modu — periyodik takvim
- 4. Denetim aşaması paketleri
  - Aşama 1 — doküman ve hazırlık değerlendirmesi
  - Aşama 2 — uygulama ve etkinlik
  - Gözetim denetimi (yıllık)
  - Yeniden belgelendirme (üç yıllık)
- 5. ISO/IEC 42006 — denetçinin bakış açısı
- 6. Kanıt klasörü yapısı
Doküman setini üretmek işin başıdır. Belgelendirme denetçisi Aşama 2'de ve
gözetim denetimlerinde **sistemin yaşadığını** görmek ister: yeni YZ talepleri
nasıl karşılandı, envanter güncel mi, etki değerlendirmeleri yeniden yapıldı mı,
YGG politika sapmalarını gördü mü. Bu bölüm o yaşam döngüsünü tanımlar.

## 1. Çalışma modunu belirle

Kullanıcının isteğinden modu çıkar; belirsizse tek soruyla sor.

| Mod | Sinyal | Ne üretilir |
|---|---|---|
| **Kurulum** | "42001 dokümanları hazırla", set yok | Tam veya sadeleştirilmiş set (Çalışma akışı §3) |
| **Sürdürme** | Set var; "yeni YZ aracı alıyoruz", "envanteri güncelle", "YGG hazırlığı", "iç tetkik zamanı" | Mevcut kayıtlarda revizyon + değişiklik kaydı; yeni doküman değil |
| **Denetim hazırlığı** | "Aşama 1/2 denetimi geliyor", "gözetim denetimi", tarih verilmiş | §4'teki aşamaya özgü paket |
| **Boşluk analizi** | Kullanıcı mevcut dokümanları verdi | Mevcut Doküman Değerlendirme ve Boşluk Raporu |

Sürdürme modunda **yeni doküman kodu açma eğilimine direnin.** Yeni bir YZ
sistemi yeni bir doküman değil; envantere satır, risk kaydına satır, etki
değerlendirmesine kayıt ve gerekiyorsa SoA'da revizyondur.

## 2. Sürdürme modu — olay güdümlü akışlar

Her akışın sonunda: etkilenen kayıtların revizyon numarası ve tarihi artar,
Doküman Ana Listesi (LS-09) güncellenir, değişiklik 6.3 kapsamında kayda
geçer.

### 2a. Yeni YZ kullanım talebi

```
Talep → /ai-governance-legal:use-case-triage
   🔴 → Talep reddi kayda geçer (YZ Kullanım Onay Kaydı); gerekçe yasaklı
        kullanımlar listesinde yoksa YZ politikasına eklenmesi önerilir
   🟡/🟢 → ai-inventory add (+ classify, AB bağlantısı varsa)
        → envanter_senkron.py aktar --mevcut (LS-04 güncellenir)
        → Risk kaydına satır (FR-03), şartlar → risk işleme kontrolü
        → Etki değerlendirmesi gerekli mi? (etki-degerlendirmesi.md §4)
             evet → aia-generation (hukuki) + FR-04 kaydı (42001)
        → Yeni üçüncü taraf varsa vendor-ai-review → LS-06
        → SoA etkileniyor mu? (yeni kontrol uygulanabilir hâle geldi mi)
        → envanter_senkron.py zincir → açık zincir kalmadı mı
```

**Eklenti yoksa** aynı akış elle yürür; kayıtlar aynıdır, yalnız hukuki
adımlar hukuk birimine devredilir:

| Eklenti adımı | Eklentisiz karşılığı |
|---|---|
| `use-case-triage` | YZ Kullanım Onay Kaydı'na talep satırı; YZ politikasındaki yasaklı kullanımlarla karşılaştır; karar sahibi ve tarih yaz |
| `ai-inventory add/classify` | YZYS-LS-04'e satırı doğrudan gir; AB YZ Yasası rolü/seviyesi sütununa `[Hukuk teyidi]` |
| `envanter_senkron.py aktar` | Atla (YAML yok) |
| `aia-generation` | Yalnız FR-04 YZ Sistemi Etki Değerlendirmesi; hukuki AIA gerekip gerekmediğini hukuka sor |
| `vendor-ai-review` | LS-06 satırı + sözleşmenin YZ maddeleri (veriyle eğitim, saklama, veri yeri, model değişikliği bildirimi) için hukuk incelemesi talebi |
| `envanter_senkron.py zincir` | Elle kontrol: LS-04 satırının risk no (FR-03) ve etki değerlendirmesi no (FR-04) sütunları dolu mu |

### 2b. Mevcut sistemde değişiklik

Tetikleyiciler: model sürümü değişti, ince ayar yapıldı, amaçlanan kullanım
genişledi, karar özerkliği arttı, yeni kullanıcı/etkilenen grup, yeni veri
kaynağı, tedarikçi şartlarını değiştirdi.

- Envanterde "Önemli Değişiklik" sütunu → Evet ise rol iki eksende yeniden
  değerlendirilir (eklenti-entegrasyonu.md §5).
- Etki değerlendirmesi yeniden yapılır veya "değişiklik etkiyi değiştirmiyor"
  gerekçesi kayda geçer.
- Tedarikçi model değişikliği → `vendor-ai-review` sözleşmedeki bildirim
  maddesini kontrol eder.

### 2c. Yeni düzenleme veya yürürlük tarihi değişikliği

guncellik-izleme.md veya `regulatory-legal` izleme ajanı bir değişiklik
gösterdiğinde → `reg-gap-analysis` → LS-10 satırları güncellenir → 4.1/4.2
bağlam ve ilgili taraf kayıtları gözden geçirilir → 6.3 değişiklik planı.

### 2d. YZ olayı veya endişe bildirimi

olay-bildirim-ve-okuryazarlik.md §1 akışı. Olay kaydı (YZYS olay formu) →
DÖF (10.2) → etki değerlendirmesi ve risk kaydı güncellemesi.

### 2e. Sistemin emekliye ayrılması

Envanterde Durum = Emekli, yaşam döngüsü aşaması = Emekliye ayırma;
`ai-inventory edit <id>` ile `status: deprecated`. Veri saklama/imha ve
kullanıcı bildirimi (A.8) kanıtı istenir. Kaydı silme — denetçi geçmişi görür.

## 3. Sürdürme modu — periyodik takvim

Takvimi kuruluşa öner; kullanıcı isterse zamanlanmış görev olarak kur
(`create_trigger`; yerel cron araçları değil). Zamanlanmış görev isteminin
tek başına anlaşılır olması gerekir — matter slug'ı, klasör yolu ve hangi
yeteneklerin çalışacağı yazılmalıdır.

| Sıklık | İş | Eklenti yeteneği | 42001 kanıtı |
|---|---|---|---|
| Haftalık / aylık | Politika sapması taraması | `policy-monitor --sweep` | 9.1 izleme, A.2.4 |
| Aylık | Envanter fark raporu ve çift zincir kontrolü | `envanter_senkron.py fark` + `zincir` | 8.1, 6.1.4 |
| Çeyreklik | Güncellik listesi kontrolü; değişen satırlar için boşluk analizi | `reg-gap-analysis` | 4.1, 4.2, 6.3 |
| Çeyreklik | YZ hedefleri ve adillik metrikleri ölçümü (değerleri kuruluş girer) | — | 6.2, 9.1 |
| Yıllık (veya plan) | İç tetkik — soru bankası ile; tetkikçi bağımsızlığı | — | 9.2 |
| Yıllık | YGG — girdiler aşağıda | `policy-monitor` raporu, `reg-gap-analysis` özeti | 9.3 |
| Yıllık | YZ okuryazarlığı/yetkinlik eğitimi tekrarı | — | 7.2, 7.3 |
| `next_review` tarihi geldiğinde | Sistem bazlı yeniden sınıflandırma ve etki değerlendirmesi | `ai-inventory classify` | 8.4 |

**YGG girdi paketi (9.3).** Sürdürme modunda YGG hazırlığı istendiğinde şu
paketi bir yol gösterici olarak hazırla: önceki YGG aksiyonları; iç/dış konu
değişiklikleri (güncellik listesinden); ilgili taraf gereklilik değişiklikleri
(LS-10); politika sapma taraması (REQUIRED/ADVISABLE sayıları — `policy-monitor`
çıktısının **sonucu**, hukuki gerekçesi değil); envanter değişimleri ve açık
zincirler; olaylar ve DÖF durumu; hedef gerçekleşmeleri (kuruluşun girdiği
değerler — uydurma yok); iç tetkik bulguları; iyileştirme fırsatları.

`policy-monitor` kuralı: tarama tarihi ve bulgu sayısı ancak kullanıcı sonucu
gözden geçirdiğini söyledikten sonra profile işlenir. YGG paketine de yalnız
onaylanmış tarama girer.

## 4. Denetim aşaması paketleri

Kullanıcı denetim aşamasını ve tarihini söylediğinde o aşamanın paketini
üret. Hepsi `07_Denetim_Hazirlik` altında **kodsuz yol gösterici**dir (K2).

### Aşama 1 — doküman ve hazırlık değerlendirmesi

Denetçi şunu sorar: sistem tasarlanmış mı, Aşama 2'ye hazır mı?

- Zorunlu dokümante bilgi kontrol listesi (`madde-4-10.md` sonu) → eksik yok
- Kapsam beyanı + YZ rolleri + SoA tutarlılığı (hariç tutulan her kontrolün gerekçesi)
- Envanter ↔ risk ↔ etki çift zincir raporu (`zincir`)
- En az bir tam iç tetkik ve bir YGG kaydı **planlanmış veya yapılmış** olmalı
- LS-10'da açık `[teyit-madde]` sayısı ve hukuk biriminin doğrulama planı
- Çıktı: `Asama1-Hazirlik-Kontrolu.xlsx` + OKUBENI'de "Aşama 1 öncesi kapatılacaklar"

### Aşama 2 — uygulama ve etkinlik

Denetçi şunu sorar: yazılan uygulanıyor mu? Örnekleme yapar.

- Her kritik/yüksek sistem için örneklem dosyası: envanter satırı, risk kaydı,
  etki değerlendirmesi, insan gözetimi kanıtı (müdahale kayıtları dahil),
  olay günlüğü örneği, tedarikçi incelemesi, şeffaflık bildirimi örneği
- Doldurulmuş iç tetkik ve YGG tutanakları, DÖF kapanış kanıtları
- Personel görüşmesine hazırlık: rol başına 3-5 soru (soru bankasından süz)
- Ölçülen hedef ve adillik metrikleri (değerler kuruluştan)
- Çıktı: `Asama2-Orneklem-Dosyasi.xlsx` (sistem × kanıt matrisi) + görüşme kartları

### Gözetim denetimi (yıllık)

- Son denetimden bu yana değişiklik özeti: yeni/emekli sistemler, rol
  değişimleri, yeni düzenlemeler, olaylar
- Önceki bulguların kapanış kanıtları
- Sürdürme takviminin işlediğinin kanıtı (§3 tablosundaki kayıtlar)
- Çıktı: `Gozetim-Degisiklik-Ozeti.docx`

### Yeniden belgelendirme (üç yıllık)

Gözetim paketine ek olarak: üç yıllık performans eğilimi, kapsam değişikliği
değerlendirmesi, SoA'nın baştan gözden geçirilmesi, standart revizyonu veya
yeni tamamlayıcı standart (ör. 42005) uygulamaya alındıysa geçiş kanıtı.

## 5. ISO/IEC 42006 — denetçinin bakış açısı

ISO/IEC 42006:2025, YZYS denetimi ve belgelendirmesi yapan kuruluşlara yönelik
gereklilikleri koyar `[teyit]`. Doküman seti için pratik sonuçları:

- **Denetçinin YZ yetkinliği artar.** Genel yönetim sistemi sorularının
  ötesinde teknik sorular beklenmeli: model doğrulama yöntemi, veri kökeni,
  sapma (drift) izleme, yanlılık testi metodolojisi. Soru bankasındaki teknik
  sorulara teknik sahibin cevap hazırlaması önerilir.
- **YZ sistemleri örneklenir.** Kapsamdaki sistem sayısı ve kritikliği denetim
  süresini ve örneklemi etkiler `[teyit]`. Envanterdeki "Kritiklik" sütununun
  dürüst doldurulması bu yüzden önemlidir.
- **Etki değerlendirmesi derinlemesine incelenir.** Biçimsel değil, sistemin
  gerçek kullanımını yansıtan değerlendirme aranır — 42005 hizalaması
  (42005-hizalama.md) burada değer kazanır.
- **Kapsam beyanı ve roller** denetim planlamasının girdisidir; belirsiz rol
  tanımı denetim süresinin ve tartışmanın uzamasına yol açar.

Bu bölümdeki ayrıntılar standardın metnine erişilerek doğrulanmalıdır; skill
42006'nın madde numaralarını atıf olarak yazmaz.

## 6. Kanıt klasörü yapısı

Doküman setinin yanına, denetim sırasında hızlı erişim için:

```
08_Kanitlar/
├── 01_Envanter_ve_Siniflandirma/   (LS-04 sürümleri, fark raporları, zincir raporları)
├── 02_Risk_ve_Etki/                (sistem bazlı alt klasörler: sys-001/ ...)
├── 03_Kullanim_Onaylari/           (triyaj sonuçlarının YZYS kaydı — hukuki gerekçe değil)
├── 04_Tedarikci/                   (LS-06, sözleşme inceleme sonuç özetleri)
├── 05_Izleme_ve_Olcum/             (hedef ölçümleri, gözetim müdahale kayıtları, günlük örnekleri)
├── 06_Olay_ve_DOF/
├── 07_Egitim_ve_Okuryazarlik/      (LS-07, katılım kayıtları)
├── 08_Ic_Tetkik_ve_YGG/
└── 09_Yasal_Uyum/                  (LS-10, doğrulama günlüğü özeti)
```

Hukuki notlar bu klasöre girmez (eklenti-entegrasyonu.md §4). Kanıt
klasörü Doküman Ana Listesi'ne girmez; kayıtların saklama yeri olarak 7.5.3
prosedüründe tanımlanır.
