---
name: iso-20000-1-dokuman-seti
description: "ISO/IEC 20000-1:2018 Hizmet Yönetim Sistemi (HYYS/SMS) için belgelendirme denetiminden geçebilecek kapsamlı doküman seti üretir — hizmet kataloğu, SLA/OLA, olay ve talep yönetimi, problem yönetimi, değişiklik ve sürüm yönetimi, konfigürasyon yönetimi (CMDB), kapasite ve süreklilik, tedarikçi yönetimi, raporlama; hepsi kurumsal Word/Excel stilleriyle. Kullanıcı \"ISO 20000 dokümanları hazırla\", \"hizmet yönetim sistemi kur\", \"HYYS\", \"SMS\", \"ITSM dokümantasyonu\", \"hizmet kataloğu oluştur\", \"SLA yaz\", \"olay yönetimi prosedürü\", \"problem yönetimi\", \"değişiklik yönetimi prosedürü\", \"CMDB kur\", \"20000 belgelendirmeye hazırlan\" dediğinde mutlaka kullan. Standart açıkça anılmasa bile BT hizmet yönetimi, servis masası, ITIL süreçleri veya hizmet seviyesi yönetimi dokümantasyonu bağlamı varsa bu skill devreye girmeli."
metadata:
  surum: "2.0.0"
---

# ISO/IEC 20000-1:2018 Hizmet Yönetimi Doküman Seti Üretimi

Bu skill bir kuruluşun HYYS'sini kurabilecek doküman setini üretir. Hedef dosya
sayısı değil: **denetçinin masaya koyduğunda uygunsuzluk yazamayacağı bir set.**

20000-1'in ayırt edici yanı şudur: standart hem bir yönetim sistemi (Madde 4–10,
Annex SL gövdesi) hem de **operasyonel süreçler** (Madde 8'in altındaki hizmet
yönetimi süreçleri) ister. Diğer standartlarda Madde 8 incedir; burada standardın
yarısıdır. Bu yüzden bu skill'in ağırlık merkezi Madde 8'dir.

> **Not:** Elinizde ISO/IEC 20000-6 varsa, o **belgelendirme kuruluşları için**
> gerekliliklerdir (ISO/IEC 17021-1 tamamlayıcısı) — kuruluşun uygulayacağı
> gereklilikler **20000-1**'dedir. Kullanıcı 20000-6'yı kaynak olarak sunarsa
> bu ayrımı nazikçe belirt; 20000-6 denetimin nasıl yapılacağını anlatır ve
> denetime hazırlanırken yararlıdır, ama doküman setinin temeli 20000-1'dir.

## Çalışma akışı

### 1 — Kuruluşu tanı (üretimden önce, her zaman)

`references/gorusme-rehberi.md` dosyasındaki altı soruluk açılış anketini sor.
`AskUserQuestion` varsa onunla sor.

20000-1'e özgü olarak şu dördünü mutlaka sor — hizmet kataloğu ve kapsam bunlara
dayanır:

- **Hangi hizmetleri, kimlere sunuyorsunuz?** İç müşteri mi, dış müşteri mi, ikisi
  de mi? Kapsam beyanının ve hizmet kataloğunun temeli budur. Kamu kurumunda BT
  birimi diğer hizmet birimlerine hizmet veriyorsa müşteri "iç müşteri"dir ve
  Hizmet Düzeyi Anlaşması sözleşme yerine iç yazışma/onaylı form ile kurulur.
- **Hizmet masanız var mı, hangi araçla?** (Jira Service Management, ServiceNow,
  GLPI, OTRS, e-posta…) Olay/talep süreçleri araca göre yazılır.
- **Hizmetin hangi parçalarını başkası sağlıyor?** 20000-1'de bu kritik: standart
  **diğer taraflarca işletilen prosesler** için özel gereklilik getirir (8.2.3) ve
  bu prosesler üzerinde yönetişim gösterilemiyorsa kapsam sorunlu olur.
- **Mevcut Hizmet Düzeyi Anlaşmalarınız var mı?** Varsa yükletin — sıfırdan yazmak
  yerine standarda uyumlu hâle getirmek hem hızlı hem doğru olur.

Ayrıca sor: kişi adı mı unvan mı kullanılacak, Revizyon 0 yayın tarihi, kurumsal
şablon birebir mi kullanılacak, mevcut dokümanlar yeniden mi yazılacak yoksa
revizyon rehberiyle mi ele alınacak.

Kurumsal şablon yüklendiyse önce tanı:

```bash
python scripts/sablon_analiz.py "<şablon.docx>"
```

### 2 — Kapsamı ve plan taslağını onaylat

**20000-1 kapsamı en hassas olanıdır.** Standart, kuruluşun hizmet yönetimi
üzerinde **yönetişim (governance) gösteremediği** hizmetleri kapsama alamayacağını
söyler. Tamamen dış kaynaklı bir hizmeti "bizim hizmetimiz" diye kapsama koymak
denetimde reddedilir. Kapsam belirlerken şunu netleştir: kuruluş hizmeti
sunuyor mu, yoksa sadece aracılık mı ediyor?

Planda ayrıca hangi dosyaların kodsuz yol gösterici olacağını göster.

Kapsam cümlesi kalıbı:

> "[Unvan] tarafından [lokasyon] üzerinden [müşteri grubu]'na sunulan [hizmet
> listesi] hizmetlerinin planlanması, sunulması ve iyileştirilmesini kapsayan
> hizmet yönetim sistemi."

### 3 — Üret

Sıra önemlidir; Madde 8 süreçleri birbirini besler:

1. **Kapsam + El Kitabı + Hizmet Yönetim Planı** (4.3, 4.4, 5.3)
2. **Bağlam, ilgili taraflar, politika, hedefler** (4.1, 4.2, 5.2, 6.2)
3. **Hizmet kataloğu → Hizmet Düzeyi Anlaşması → Operasyonel Düzey Anlaşması /
   Dayanak Sözleşme** (8.2.4, 8.3.3) — bu üçlü zincirdir
4. **Konfigürasyon yönetimi** (8.2.6) — diğer süreçler buna dayanır
5. **Olay ve hizmet talebi → problem → değişiklik → sürüm ve dağıtım** (8.6, 8.5)
6. **Kapasite, süreklilik ve erişilebilirlik, bilgi güvenliği** (8.4.3, 8.7.1–8.7.2)
7. **Tedarikçi ve müşteri ilişkileri** (8.3.4, 8.6.1)
8. **Raporlama, ölçme, iç tetkik, YGG, DÖF** (8.4.2, 9–10)
9. **OKUBENI.md**
10. **Denetim hazırlık yol göstericileri** (kodsuz): boşluk raporu, kontrol-kanıt
    matrisi ve öz değerlendirme

**Zincir kuralı:** Katalogdaki her hizmetin bir Hizmet Düzeyi Anlaşması, her
hedefin bir ölçüm kaynağı, her ölçümün bir rapor satırı olmalı. Denetçi bir
hizmet seçip "bunun hedefi ne, geçen ay tutturdunuz mu, kanıtı nerede?" diye sorar.

Word için `scripts/ys_docx.py`, Excel için `scripts/ys_xlsx.py`, standarda özgü
kayıtlar için `scripts/kayitlar_20000.py` kullan.

### 4 — Öz denetim yap ve raporla

`references/denetim-oz-kontrol.md` listesini geç, ayrıca hizmet zinciri kontrolünü
(katalog → Hizmet Düzeyi Anlaşması → ölçüm → rapor) yap. Bir betikle kalan
İngilizce kısaltmaları, kırık doküman kodu atıflarını, yol gösterici dosyalara
kodla verilmiş atıfları ve etiket sayılarını tara. Bulguları `OKUBENI.md`'de
"Denetim öncesi kapatılması gerekenler" tablosunda raporla.

Teslimden önce tutarlılık taramasını çalıştır (K1 büyük harf, K2 kodlu
yol gösterici, K3 kısaltma, kırık kod atıfları, klişe ve ölçülemez ifade,
etiket sayımı, yayın tarihi):

```bash
python scripts/tutarlilik_tarama.py "<set klasörü>" --md "<set klasörü>/_tarama.md"
```

Çıkış kodu 1 ise bulgular vardır; kapat veya `OKUBENI.md`'de gerekçesiyle listele.

## Kırılma noktaları

**Hizmet Düzeyi Anlaşmasının ölçülemez olması.** "Yüksek erişilebilirlik
sağlanır" bir hedef değildir. Her hedef: metrik + eşik + ölçüm dönemi + ölçüm
kaynağı + istisna tanımı içermeli. "Aylık erişilebilirlik ≥ %99,5; planlı bakım
pencereleri hariç; kaynak: izleme sistemi aylık raporu" bir hedeftir.

**Operasyonel Düzey Anlaşması / Dayanak Sözleşme katmanının atlanması.** Hizmet
Düzeyi Anlaşması müşteriye verilen sözdür. O sözü tutmak için iç birimlerle
operasyonel düzey anlaşması ve tedarikçilerle dayanak sözleşme gerekir. Müşteriye
4 saat çözüm vaat edilirken tedarikçi sözleşmesi 8 saat diyorsa bu bir
**tutarsızlıktır** ve denetçinin severek yakaladığı bir şeydir.

**Olay ile problemin karıştırılması.** Olay: hizmetin kesintisi veya kalite
düşüşü; hedef mümkün olan en hızlı normale dönüş. Problem: bir veya daha fazla
olayın **kök nedeni**; hedef nedeni ortadan kaldırmak. Aynı prosedürde
birleştirilmiş olay/problem yönetimi 8.6.1 ve 8.6.2'yi karşılamaz. İki ayrı
süreç, iki ayrı kayıt tipi, iki ayrı metrik.

**Değişiklik ile sürümün karıştırılması.** Değişiklik yönetimi (8.5.1) *neyin
onaylandığını*, sürüm ve dağıtım yönetimi (8.5.3) *nasıl canlıya alındığını*
yönetir. Ayrı süreçlerdir; standart 8.5.1'de acil değişiklikler için ayrı
mekanizma da ister.

**Konfigürasyon yönetim veri tabanının süs olması.** 8.2.6, konfigürasyon
öğelerinin tanımlanmasını, kaydedilmesini, **kontrol edilmesini** ve doğruluğunun
periyodik olarak doğrulanmasını ister. Hiç doğrulanmamış bir veri tabanı bulgu
üretir. Şablona "son doğrulama tarihi" ve "doğrulayan" sütunlarını mutlaka koy.

**Diğer taraflarca işletilen prosesler (8.2.3).** Standart burada nettir: bir
proses başkası tarafından işletiliyorsa kuruluş bunun üzerinde kontrolü
göstermeli — sorumluluk, arayüz, performans izleme ve müdahale hakkı yazılı olmalı.
"Tedarikçi hallediyor" cevabı yeterli değildir.

**Hizmet raporlamasının atlanması.** 8.4.2 hizmet raporlaması ayrı bir
gerekliliktir: raporun tanımı, amacı, alıcısı, sıklığı, veri kaynağı belirlenmeli.
"Ara sıra Excel gönderiyoruz" bir raporlama süreci değildir.

**Yeni/değişen hizmetlerin planlanması (8.5.2).** En sık atlanan maddedir.
Yeni bir hizmet devreye alınırken planlama, kabul kriterleri ve devreye alma
sonrası gözden geçirme gerekir. Kuruluş yeni hizmet devreye almıyorsa bile
prosedürü olmalı.

**Uydurulmuş kayıt.** Örnek katalog satırı, örnek hedef üretilebilir; gerçekleşmiş
hizmet raporu, ölçülmüş erişilebilirlik oranı, kapanmış olay kaydı uydurulamaz.
`[ÖRNEK — doğrulanacak]` etiketle.

## Mevcut doküman analizi

Kullanıcı hazır dokümanlar verdiğinde önce **Mevcut Doküman Değerlendirme ve
Boşluk Raporu**'nu (kodsuz yol gösterici) üret. Tara ve raporla: hizmet
kataloğunda Hizmet Düzeyi Anlaşması olmayan hizmetler, hedefi ölçüm kaynağı
olmayan anlaşmalar, tedarikçi sözleşme süreleri ile müşteri vaatleri arasındaki
çelişkiler, doğrulama tarihi olmayan konfigürasyon kayıtları, olay/problem
ayrımı yapılmamış kayıt tipleri, doküman listesinde aynı adlı farklı kodlar ve
boş revizyon alanları. Kullanıcı mevcut dokümanların yeniden yazılmasını
istemiyorsa her biri için "eklenecek içerik + öncelik + kabul kriteri" veren bir
**revizyon rehberi** (kodsuz yol gösterici) üret.

## Denetim hazırlık yol göstericileri (07_Denetim_Hazirlik)

Boşluk raporu, revizyon rehberleri, kontrol-kanıt matrisi, öz değerlendirme ve
denetim günü kontrol listesi yönetim sistemi dokümanı değildir; denetim öncesinde
üst yönetime neyin, kim tarafından, hangi sırayla yapılacağını gösteren yol
göstericilerdir. `iso-entegre-yonetim-sistemi` K2 kuralı uygulanır: doküman kodu
yok, dosya adı yalnız ad; kapakta "YOL GÖSTERİCİ", antette "Doküman Türü | Yol
Gösterici"; onay HYYS komitesi başkanı; metnin başında "yönetim sistemi dokümanı
değildir" notu; Doküman Listesi'ne girmez ve listenin not alanında bu açıklanır;
setin geri kalanı bu dosyalara adıyla atıf verir.
Motorda: `Kimlik(..., tur="yol_gosterici")` ver ve dosyayı `k.dosya_adi()` ile kaydet; kapak, antet etiketi, giriş notu ve kodsuz dosya adı otomatik gelir.

## Türkçe terim kuralı

Kullanıcı aksini istemedikçe başlık ve doküman adlarında İngilizce kısaltma
kullanma: SLA → Hizmet Düzeyi Anlaşması, OLA → Operasyonel Düzey Anlaşması, UC →
Dayanak Sözleşme, CMDB → Konfigürasyon Yönetim Veri Tabanı, CI → konfigürasyon
öğesi, ITSM → BT hizmet yönetimi, KPI → performans göstergesi, RFC → değişiklik
talebi, CAB → Değişiklik Danışma Kurulu, service desk → hizmet masası. İngilizce
karşılık yalnız Tanımlar tablosunda parantez içinde bir kez verilir; ürün adları
(Jira, ServiceNow, GLPI) olduğu gibi kalır. Motor (`ys_docx.py` 2.0.0)
Word metinlerine `tr()` sözlüğünü otomatik uygular; Excel'de ve kendi kodunda
`tr()` ve `tr_upper()` çağır.

## Kurumsal şablonu birebir kullanma

Kullanıcı bir kurumsal dokümanı "şablon olarak bire bir kullan" derse
`ys_docx.py` yerine şablonu klonla (`iso-entegre-yonetim-sistemi` K4): kapak kodu
ve antet hücrelerini değiştir, başlık/gövde/liste paragraflarını rPr dahil
prototip olarak çoğalt, İçindekiler'i bookmark + `PAGEREF` ile kurup sayfa
numaralarını LibreOffice render + `pdftotext` ile hesapla, sabit toplam sayfa
metnini `SECTIONPAGES` alanıyla değiştir. Excel'de kuruluşun mevcut liste
dosyasının bilgi sayfasını ve logosunu koru. Her dosyayı PDF'e çevirip görsel
kontrol et.

## Kullanıcı tek doküman istediğinde

Süreci kısalt, kaliteyi koru: kuruluş, hizmet, kapsam ve varsa şablonu sor; üret;
ilgili maddeleri ve kanıt beklentisini dokümanın sonunda belirt. Hizmet Düzeyi
Anlaşması veya katalog istenirse zincirin diğer halkalarını bir cümleyle hatırlat.

## Entegre sistem

ISO 27001 ile çok sık birlikte kurulur. 20000-1'in 8.7.3 bilgi güvenliği
yönetimi maddesi 27001'in tamamıyla karşılanır; 8.7.2 hizmet sürekliliği ise
22301 ile örtüşür. Ortak dokümanları (doküman kontrol, iç tetkik, YGG, DÖF,
yetkinlik, değişiklik yönetimi) `EYS-` önekiyle tek doküman üret ve her iki
standardın maddesine atıf ver. Birden fazla standart kapsamdaysa
`iso-entegre-yonetim-sistemi` ile çalış.

## Çalışma ortamı

Bu skill hem Cowork'te hem Claude Code'da çalışır. Aracı ortama göre seç:

| İş | Cowork (bağlı klasör) | Claude Code / yerel |
|---|---|---|
| Mevcut dosyaları okuma | `device_list_dir`, `device_bash` ile yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları `device_stage_files` ile al | `Read`, `Glob`, `Bash`/`PowerShell` ile doğrudan |
| Script çalıştırma | `python3 scripts/<betik>.py …` | `python scripts/<betik>.py …` (Windows'ta `py -3` de olur). `scripts/` yolu skill'in taban dizinine göredir; Claude Code bu dizini skill yüklenirken "Base directory" satırında verir |
| Teslim | `device_commit_files` ile bağlı klasörde **yeni alt klasör** | Kullanıcının gösterdiği klasörde, yoksa çalışma dizininde **yeni alt klasör** |
| Dosyaları sunma | `mcp__cowork__present_files` | Tam dosya yollarını listele |

Her iki ortamda: kullanıcının mevcut dosyalarını değiştirme ve silme. Yeniden
üretimde adı değişen eski dosyaları `_to_delete/` alt klasörüne taşı
(`mv -n`) ve söyle.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Girdi | Bağlı klasör / yerel dosya sistemi (bkz. Çalışma ortamı) | Bağlı klasördeki mevcut katalog, anlaşma ve kayıtları yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa |
| Hizmet masası verisi | Jira / ServiceNow connector'ı (varsa `SearchMcpRegistry` ile ara) | Gerçek kategori, öncelik ve hedef değerlerini okumak — kayıt uydurmamak |
| Sözleşmeler | `commercial-legal:vendor-agreement-review`, `commercial-legal:saas-msa-review` | Dayanak sözleşme ile müşteri vaadi tutarlılığı, bulut hizmetleri |
| Mevzuat | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher` | Sektörel BT düzenlemeleri, kamu için BİG Rehberi |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf` | Üretim ve doğrulama |
| Görsel kontrol | `soffice` → `pdftoppm` → Read | Şablon birebirliği, tablo taşmaları |
| Entegrasyon | `iso-entegre-yonetim-sistemi`, `iso-27001-dokuman-seti`, `iso-22301-dokuman-seti` | 8.7.2 / 8.7.3 kesişimleri, K1–K4 kuralları |
| Teslim | Yeni alt klasöre teslim (bkz. Çalışma ortamı) | Kullanıcının dosyalarını değiştirmeden teslim |

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/gorusme-rehberi.md` | Her çalışmanın başında |
| `references/dokuman-listesi.md` | Plan aşamasında |
| `references/madde-4-10.md` | Yönetim sistemi maddeleri (4–7, 9–10) |
| `references/madde-8-surecler.md` | Hizmet yönetimi süreçleri — bu standardın kalbi |
| `references/icerik-rehberi.md` | Metin kalitesi — örnek zayıf/güçlü metinler |
| `references/dokuman-mimarisi.md` | Kodlama, hiyerarşi, ortak bölümler |
| `references/denetim-oz-kontrol.md` | Teslim öncesi |

## Bağımlılıklar

`python-docx` ve `openpyxl` gerekir:

```bash
pip install python-docx openpyxl
```

Linux'ta "externally-managed-environment" hatası alırsan komuta
`--break-system-packages` ekle; Windows ve macOS'ta gerekmez.
