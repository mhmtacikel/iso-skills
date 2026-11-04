---
name: iso-22301-dokuman-seti
description: "ISO 22301:2019 (TS EN ISO 22301) İş Sürekliliği Yönetim Sistemi için belgelendirme denetiminden geçebilecek kapsamlı doküman seti üretir — kapsam, iş sürekliliği politikası, İş Etki Analizi (BIA), RTO/RPO/MTPD tanımları, süreklilik stratejileri, olay müdahale yapısı, iş sürekliliği planları, tatbikat programı, formlar; hepsi kurumsal Word/Excel stilleriyle. Kullanıcı \"ISO 22301 dokümanları hazırla\", \"iş sürekliliği yönetim sistemi kur\", \"İSYS\", \"BIA yap\", \"iş etki analizi\", \"iş sürekliliği planı yaz\", \"RTO RPO belirle\", \"felaket kurtarma planı\", \"tatbikat planı\", \"22301 belgelendirmeye hazırlan\" dediğinde mutlaka kullan. Standart açıkça anılmasa bile iş sürekliliği, kriz yönetimi, olağanüstü durum planlaması veya iş kesintisine hazırlık dokümantasyonu bağlamı varsa bu skill devreye girmeli."
metadata:
  surum: "2.0.0"
---

# ISO 22301:2019 İş Sürekliliği Doküman Seti Üretimi

Bu skill bir kuruluşun İSYS'sini kurabilecek doküman setini üretir. Hedef dosya
sayısı değil: **denetçinin masaya koyduğunda uygunsuzluk yazamayacağı bir set.**

22301'in diğer yönetim sistemlerinden farkı şudur: burada dokümanın kendisi
yeterli değil, **çalıştığının kanıtlanması** gerekir. Tatbikat yapılmamış bir
iş sürekliliği planı denetimde plan sayılmaz. Bu yüzden bu skill her plan için
tatbikat ve değerlendirme mekanizmasını da üretir.

## Çalışma akışı

### 1 — Kuruluşu tanı (üretimden önce, her zaman)

`references/gorusme-rehberi.md` dosyasındaki altı soruluk açılış anketini sor.
`AskUserQuestion` varsa onunla sor.

22301'e özgü olarak şu üçünü mutlaka sor — bunlar olmadan İş Etki Analizi
yazılamaz:

- **Kesintiye en tahammülsüz faaliyetiniz hangisi ve ne kadar süre durabilir?**
  Azami tolere edilebilir kesinti süresi / kurtarma süresi hedefi tartışmasının
  başlangıç noktası budur.
- **Geçmişte yaşadığınız kesintiler neler?** (elektrik, siber olay, tedarikçi
  iflası, pandemi, yangın, deprem, kilit personel kaybı) Gerçek geçmiş, uydurma
  senaryodan çok daha inandırıcı bir risk değerlendirmesi verir.
- **Alternatif çalışma imkânınız var mı?** (yedek lokasyon / felaket kurtarma
  merkezi, uzaktan çalışma altyapısı, yedek tedarikçi, bulut yedekliliği) Strateji
  bölümü buna dayanır.

Ayrıca sor: kişi adı mı unvan mı kullanılacak, Revizyon 0 yayın tarihi, kurumsal
şablon birebir mi kullanılacak, mevcut planlar yeniden mi yazılacak yoksa
revizyon rehberiyle mi ele alınacak.

Kurumsal şablon yüklendiyse önce tanı:

```bash
python scripts/sablon_analiz.py "<şablon.docx>"
```

### 2 — Kapsamı ve plan taslağını onaylat

Üretime başlamadan tek ekranlık planı sun: kapsam beyanı, üretilecek doküman
sayısı, kodlama kuralı, İş Etki Analizi'nde ele alınacak faaliyet sayısı, hangi
dosyaların kodsuz yol gösterici olacağı.

**22301 kapsamı özel dikkat ister.** Standart 4.3.2'de kapsam belirlenirken
kuruluşun misyonu, hedefleri, iç/dış yükümlülükleri, risk iştahı ve ilgili taraf
gerekliliklerinin dikkate alınmasını ister; kapsam dışı bırakılan her şeyin
gerekçelendirilmesi gerekir. Kapsam cümlesi kalıbı:

> "[Unvan]'ın [lokasyon] adresinde yürüttüğü [faaliyet] faaliyetlerinin
> kesintiye uğraması hâlinde önceden tanımlanmış seviyede sürdürülmesini
> sağlayan iş sürekliliği yönetim sistemi."

### 3 — Üret

Sıra kritiktir; 22301'de zincirin kopması en sık bulgu kaynağıdır:

1. **Kapsam + El Kitabı**
2. **Bağlam, ilgili taraflar, yasal yükümlülükler** (4.1, 4.2.1, 4.2.2)
3. **İş sürekliliği politikası** (5.2)
4. **İş Etki Analizi metodolojisi → İş Etki Analizi → risk değerlendirmesi** (8.2)
5. **Süreklilik stratejileri ve çözümleri → kaynak gereksinimleri** (8.3)
6. **Müdahale yapısı → uyarı ve iletişim → iş sürekliliği planları → geri dönüş** (8.4)
7. **Tatbikat programı** (8.5) ve **değerlendirme** (8.6)
8. **Performans, iç tetkik, YGG, DÖF** (9–10)
9. **OKUBENI.md**
10. **Denetim hazırlık yol göstericileri** (kodsuz): boşluk raporu, kontrol-kanıt
    matrisi ve öz değerlendirme

**Zincir kuralı:** İş Etki Analizi'nde belirlenen her önceliklendirilmiş
faaliyetin bir kurtarma süresi hedefi, her hedefin bir stratejisi, her
stratejinin kaynak gereksinimi, her kaynağın plan içinde bir karşılığı olmalı.
Denetçi rastgele bir faaliyet seçip bu zinciri ucundan ucuna takip eder. Kopuk
halka = bulgu.

Word için `scripts/ys_docx.py`, Excel için `scripts/ys_xlsx.py`, standarda özgü
kayıtlar için `scripts/kayitlar_22301.py` kullan.

### 4 — Öz denetim yap ve raporla

`references/denetim-oz-kontrol.md` listesini geç, ayrıca 22301'e özgü zincir
kontrolünü yap (İş Etki Analizi → hedef süre → strateji → kaynak → plan). Bir
betikle kurtarma süresi hedefinin azami tolere edilebilir kesinti süresinden kısa
olduğunu satır satır doğrula; kalan İngilizce kısaltmaları, kırık kod atıflarını,
yol gösterici dosyalara kodla verilmiş atıfları ve etiket sayılarını tara.
Bulguları `OKUBENI.md`'de "Denetim öncesi kapatılması gerekenler" tablosunda
raporla.

Teslimden önce tutarlılık taramasını çalıştır (K1 büyük harf, K2 kodlu
yol gösterici, K3 kısaltma, kırık kod atıfları, klişe ve ölçülemez ifade,
etiket sayımı, yayın tarihi):

```bash
python scripts/tutarlilik_tarama.py "<set klasörü>" --md "<set klasörü>/_tarama.md"
```

Çıkış kodu 1 ise bulgular vardır; kapat veya `OKUBENI.md`'de gerekçesiyle listele.

## Kırılma noktaları

**Kurtarma süresi hedefi ile azami tolere edilebilir kesinti süresinin
karıştırılması.** Azami tolere edilebilir kesinti süresi (MTPD) faaliyetin
durmasının kabul edilemez hâle geldiği eşiktir — iş tarafının kararıdır. Kurtarma
süresi hedefi (RTO) faaliyetin yeniden başlatılması için konan hedeftir ve
**azami süreden kısa olmalıdır.** RTO ≥ MTPD olan bir analiz iç tutarsızlıktır ve
denetçinin ilk yakaladığı şeydir. Kurtarma noktası hedefi (RPO) ise kabul
edilebilir veri kaybı miktarıdır; süreyle ölçülür ama RTO'dan bağımsızdır.

**Tatbikatsız plan.** 8.5 tatbikat programını, 8.6 dokümantasyon ve yeteneklerin
değerlendirilmesini zorunlu kılar. Plan üretirken tatbikat senaryosu, tatbikat
kayıt formu ve tatbikat sonrası iyileştirme mekanizmasını birlikte üret.

**Kaynak gereksiniminin atlanması.** 8.3.4 kaynakları açıkça sayar: insan, bilgi
ve veri, fiziksel altyapı, ekipman ve sarf malzemeleri, bilgi ve iletişim
teknolojileri sistemleri, ulaşım ve lojistik, finans, ortaklar ve tedarikçiler.
Strateji dokümanında bu başlıkların her birine karşılık bir satır olmalı; boş
geçilen başlık "eksik değerlendirme" bulgusu üretir.

**Genel plan, özel senaryo yok.** "Kriz olursa kriz masası toplanır" plan değildir.
Plan; tetikleyici eşiği, kimin ne zaman nasıl haberdar edileceğini, ilk 1 saat /
ilk 24 saat / sonrası adımlarını, karar yetkilerini ve yedek karar vericileri
içermeli. 8.4.2 müdahale yapısının **yetki ve yedek atamalarını** açıkça ister.

**İletişim planının tek yönlü olması.** 8.4.3 uyarı ve iletişim; sadece
çalışanlara duyuru değil — ilgili taraflar, yetkili merciler, medya, müşteriler
ve tedarikçilerle iletişimi, ayrıca **alternatif iletişim kanallarını** kapsar.
Ana iletişim kanalı çalışmıyorken kullanılacak yedek kanal tanımlı olmalı.

**Geri dönüşün unutulması.** 8.4.5 "eski hâline geri dönme" ayrı bir gerekliliktir.
Çoğu doküman seti kurtarmayı anlatır, normale dönüşü anlatmaz. Her planda
"normal operasyona dönüş" bölümü ve kriterleri olmalı.

**Uydurulmuş tatbikat kaydı.** Tatbikat senaryosu ve boş kayıt formu üretilebilir;
gerçekleşmiş gibi doldurulmuş tatbikat raporu üretilemez. Bunu `[ÖRNEK]` olarak
işaretle ve kullanıcıya gerçek tatbikat yapması gerektiğini söyle. İletişim
listesindeki kişi adı ve telefon numarası da uydurulmaz; unvan yaz, numarayı
`[DOLDURULACAK]` bırak.

## Mevcut doküman analizi

Kullanıcı hazır dokümanlar verdiğinde önce **Mevcut Doküman Değerlendirme ve
Boşluk Raporu**'nu (kodsuz yol gösterici) üret. Tara ve raporla: kurtarma süresi
hedefi azami süreden uzun olan satırlar, stratejisi veya kaynağı olmayan
faaliyetler, formülsüz/#N/A etki skorları, tatbikat kaydı olmayan planlar, yedek
karar verici tanımlanmamış müdahale yapısı, normale dönüş bölümü olmayan planlar,
sütun kayması (başka birimin/şablonun içeriği), doküman listesinde aynı adlı farklı
kodlar. Kullanıcı mevcut planların yeniden yazılmasını istemiyorsa her biri için
"eklenecek içerik + öncelik + kabul kriteri" veren bir **revizyon rehberi** (kodsuz
yol gösterici) üret.

## Denetim hazırlık yol göstericileri (07_Denetim_Hazirlik)

Boşluk raporu, revizyon rehberleri, kontrol-kanıt matrisi, öz değerlendirme ve
tatbikat hazırlık takvimi yönetim sistemi dokümanı değildir; denetim öncesinde üst
yönetime neyin, kim tarafından, hangi sırayla yapılacağını gösteren yol
göstericilerdir. `iso-entegre-yonetim-sistemi` K2 kuralı uygulanır: doküman kodu
yok, dosya adı yalnız ad; kapakta "YOL GÖSTERİCİ", antette "Doküman Türü | Yol
Gösterici"; onay İSYS komitesi başkanı; metnin başında "yönetim sistemi dokümanı
değildir" notu; Doküman Listesi'ne girmez ve listenin not alanında bu açıklanır;
setin geri kalanı bu dosyalara adıyla atıf verir.
Motorda: `Kimlik(..., tur="yol_gosterici")` ver ve dosyayı `k.dosya_adi()` ile kaydet; kapak, antet etiketi, giriş notu ve kodsuz dosya adı otomatik gelir.

## Türkçe terim kuralı

Kullanıcı aksini istemedikçe başlık ve doküman adlarında İngilizce kısaltma
kullanma: BIA → İş Etki Analizi, RTO → Kurtarma Süresi Hedefi, RPO → Kurtarma
Noktası Hedefi, MTPD → Azami Tolere Edilebilir Kesinti Süresi, MBCO → Asgari İş
Sürekliliği Hedefi, BCP → İş Sürekliliği Planı, DRP → Felaket Kurtarma Planı,
DR site → felaket kurtarma merkezi. Tablo sütunlarında yer darsa kısaltma
kullanılabilir; ilk geçtiği yerde ve Tanımlar tablosunda açılımı verilir. Motorda
sözlük + `tr()` fonksiyonuyla tüm metinlere uygula; büyük harf dönüşümünde
`tr_upper()` kullan.

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

Süreci kısalt ama kaliteyi koru: kuruluş, kapsam, varsa şablonu sor; üret; ilgili
maddeleri ve kanıt beklentisini dokümanın sonunda belirt. İş Etki Analizi veya
plan istenirse, zincirin kalan halkalarının eksik olacağını bir cümleyle hatırlat.

## Entegre sistem

ISO 27001 ile birlikte kuruluyorsa: 27001'in A.5.29 ve A.5.30 kontrolleri
(kesinti sırasında bilgi güvenliği, iş sürekliliği için BİT hazırlığı) 22301'in
8.3/8.4 çıktılarıyla karşılanır. 20000-1 varsa 8.7.2 hizmet sürekliliği bu setle
karşılanır. Ortak dokümanları (doküman kontrol, iç tetkik, YGG, DÖF, yetkinlik)
`EYS-` önekiyle tek doküman olarak üret ve her iki standardın maddesine atıf ver.
Birden fazla standart kapsamdaysa `iso-entegre-yonetim-sistemi` ile çalış.

## Çalışma ortamı

Bu skill hem Cowork'te hem Claude Code'da çalışır. Aracı ortama göre seç:

| İş | Cowork (bağlı klasör) | Claude Code / yerel |
|---|---|---|
| Mevcut dosyaları okuma | `device_list_dir`, `device_bash` ile yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları `device_stage_files` ile al | `Read`, `Glob`, `Bash`/`PowerShell` ile doğrudan |
| Script çalıştırma | `python3 scripts/<betik>.py …` | `python scripts/<betik>.py …` (Windows'ta `py -3` de olur). `scripts/` yolu skill'in taban dizinine (bu SKILL.md'nin bulunduğu klasör) göredir; Claude Code skill yüklenirken bunu "Base directory" satırında verir, dosya doğrudan okunduysa SKILL.md'nin klasörünü kullan |
| Teslim | `device_commit_files` ile bağlı klasörde **yeni alt klasör** | Kullanıcının gösterdiği klasörde **yeni alt klasör**; klasör belirtilmediyse üretimden önce sor |
| Dosyaları sunma | `mcp__cowork__present_files` | Tam dosya yollarını listele |

Her iki ortamda: kullanıcının mevcut dosyalarını değiştirme ve silme. Yeniden
üretimde adı değişen eski dosyaları `_to_delete/` alt klasörüne taşı
(`mv -n`) ve söyle.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Girdi | Bağlı klasör / yerel dosya sistemi (bkz. Çalışma ortamı) | Bağlı klasördeki mevcut analiz ve planları yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa |
| Mevzuat | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher`, `regulatory-legal:policy-diff` | AFAD, sektörel süreklilik düzenlemeleri, kamu için BİG Rehberi; tarih/süre uydurma |
| Tedarikçi | `commercial-legal:vendor-agreement-review`, `commercial-legal:saas-msa-review` | Tedarikçi süreklilik taahhütleri, bulut yedekliliği |
| İK | `employment-legal:policy-drafting` | Kilit personel, uzaktan çalışma, vekâlet düzenlemeleri |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf`, `anthropic-skills:pptx` (tatbikat brifingi, YGG sunumu) | Üretim ve doğrulama |
| Görsel kontrol | `soffice` → `pdftoppm` → Read | Şablon birebirliği, tablo taşmaları |
| Entegrasyon | `iso-entegre-yonetim-sistemi`, `iso-27001-dokuman-seti`, `iso-20000-1-dokuman-seti` | A.5.29/5.30 ve 8.7.2 kesişimleri, K1–K4 kuralları |
| Teslim | Yeni alt klasöre teslim (bkz. Çalışma ortamı) | Kullanıcının dosyalarını değiştirmeden teslim |

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/gorusme-rehberi.md` | Her çalışmanın başında |
| `references/dokuman-listesi.md` | Plan aşamasında |
| `references/madde-4-10.md` | Yönetim sistemi dokümanlarını yazarken |
| `references/bia-ve-strateji.md` | İş Etki Analizi, hedef süreler, strateji ve plan yazarken |
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
