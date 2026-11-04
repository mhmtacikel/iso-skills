---
name: "iso-27001-dokuman-seti"
description: "ISO/IEC 27001:2022 (TS EN ISO/IEC 27001:2023) Bilgi Güvenliği Yönetim Sistemi için belgelendirme denetiminden geçebilecek kapsamlı doküman seti üretir — kapsam, politikalar, prosedürler, risk envanteri, Uygulanabilirlik Bildirgesi (SoA), formlar, planlar; hepsi kurumsal Word/Excel stilleriyle. Kullanıcı \"ISO 27001 dokümanları hazırla\", \"BGYS kur\", \"bilgi güvenliği politikası yaz\", \"SoA oluştur\", \"risk envanteri hazırla\", \"27001 belgelendirmeye hazırlan\", \"bilgi güvenliği prosedürü\", \"BGYS doküman seti\" dediğinde ya da 27001 denetimine hazırlık, boşluk analizi, eksik doküman tamamlama işi geçtiğinde mutlaka kullan. Kullanıcı standardı açıkça anmasa bile bilgi güvenliği yönetim sistemi dokümantasyonu, ISMS kurulumu veya bilgi güvenliği sertifikasyonu bağlamı varsa bu skill devreye girmeli."
---

# ISO/IEC 27001:2022 Doküman Seti Üretimi

Bu skill, bir kuruluşun BGYS'sini sıfırdan kurabilecek ya da mevcut sistemindeki
boşlukları kapatabilecek doküman setini üretir. Hedef, dosya sayısı değil:
**belgelendirme denetçisinin masaya koyduğunda uygunsuzluk yazamayacağı bir set.**

Bu ikisi arasındaki fark şudur: denetçi dokümanın varlığına değil, dokümanın
kuruluşu anlatıp anlatmadığına ve uygulama kanıtına bağlanıp bağlanmadığına
bakar. Bu yüzden bu skill önce kuruluşu tanır, sonra yazar.

## Çalışma akışı

### 1 — Kuruluşu tanı (üretimden önce, her zaman)

`references/gorusme-rehberi.md` dosyasındaki **altı soruluk açılış anketini**
sor. `AskUserQuestion` aracı varsa onunla sor; çoktan seçmeli seçenekler
kullanıcının yazma yükünü kaldırır ve cevap kalitesini yükseltir.

27001'e özgü olarak şu ikisini de sor:

- **Bilgi varlıklarınızın ağırlığı nerede?** (müşteri verisi / fikri mülkiyet /
  finansal veri / sağlık verisi / operasyonel teknoloji) — risk senaryolarını ve
  hangi Ek A kontrollerinin ağırlık kazanacağını bu belirler.
- **Yazılım geliştiriyor musunuz, veri merkeziniz kendinizin mi?** — A.8.25–8.34
  geliştirme kontrolleri ve A.7 fiziksel kontrollerin uygulanabilirliği buna bağlı.
  Tamamı bulutta çalışan bir SaaS şirketiyle kendi veri merkezi olan bir bankanın
  Uygulanabilirlik Bildirgesi aynı olamaz.

Kullanıcı kurumsal şablonunu yüklediyse önce onu tanı:

```bash
python3 scripts/sablon_analiz.py "<şablon.docx>"
```

Çıktıdaki yazı tipi, renk, antet ve doküman kodu kalıbını üretimde kullan.
Şablon yoksa `ys_docx.py` içindeki varsayılan kurumsal kimlik devreye girer;
bunu kullanıcıya söyle ve sonradan şablona geçilebileceğini belirt.

### 2 — Kapsamı ve plan taslağını onaylat

Üretime başlamadan önce tek ekranlık planı sun: kapsam beyanı cümlesi, üretilecek
doküman sayısı, kodlama kuralı, hangi Ek A kontrollerinin hariç tutulacağı,
hangi dosyaların kodsuz yol gösterici olacağı.
Kullanıcı kapsam cümlesini burada düzeltirse kırk dosya yerine bir satır
düzeltmiş olursun. Bu adımı atlama.

**Kapsam beyanı** sertifikanın üstünde yazacak metindir. Şu üçünü içermeli:
tüzel kişilik + faaliyet/hizmet tanımı + lokasyon. Örnek kalıp:

> "[Unvan] tarafından [lokasyon] adresinde yürütülen [hizmet/ürün] faaliyetlerinin
> geliştirilmesi, işletilmesi ve destek süreçlerini kapsayan bilgi güvenliği
> yönetim sistemi. Uygulanabilirlik Bildirgesi Rev. [nn] geçerlidir."

### 3 — Üret

Sırayı koru; sonraki doküman öncekine referans verir:

1. **Kapsam + El Kitabı** → sistemin çerçevesi
2. **Bağlam ve ilgili taraf analizleri** → 4.1/4.2 girdileri
3. **Politikalar** → ana politika + konuya özgü politikalar
4. **Risk metodolojisi → risk envanteri → Uygulanabilirlik Bildirgesi → risk
   işleme planı** (bu zincir sırayla kurulmalı; bildirge risk işlemenin
   çıktısıdır, bağımsız bir liste değil)
5. **Prosedürler** → doküman kontrolünden başla, diğerleri ona atıf verir
6. **Formlar, listeler, planlar**
7. **OKUBENI.md** → her zaman, en son
8. **Denetim hazırlık yol göstericileri** (kodsuz): boşluk raporu, kontrol-kanıt
   matrisi ve öz değerlendirme — aşağıdaki bölüm

Word için `scripts/ys_docx.py`, Excel için `scripts/ys_xlsx.py` kullan. Bu
scriptler kapak, antet, revizyon tablosu, içindekiler, onay bloğu, stiller,
donmuş bölme, açılır liste ve koşullu biçimlendirmeyi hazır verir — bunları
elle yeniden yazma, motorun üstüne içerik koy.

Tekrar eden Excel kayıtları (93 kontrollü bildirge, risk envanteri, varlık
envanteri, hedefler, doküman listesi, yetkinlik matrisi, DÖF, tetkik programı)
tek komutla:

```bash
python3 scripts/kayitlar_27001.py --kurulus "..." --cikti "<klasör>" \
  --tarih 2026-08-11 --hazirlayan "..." --onaylayan "..." [--sade]
```

**`--sade` bayrağını sadeleştirilmiş set üretirken mutlaka kullan.** Bildirgedeki
doküman kodları tam sete göredir; sade sette birleştirilmiş dokümanların
kodlarını olduğu gibi bırakırsan var olmayan dosyalara atıf veren bir bildirge
çıkar ve bu denetimde bulgu üretir.

Bildirgenin "Dahil Etme Gerekçesi" sütunu varsayılan olarak `[DOLDURULACAK]`
gelir — bilerek. Jenerik gerekçe ("standart gereği") bulgu üretir; gerçek
gerekçeleri risk numaralarıyla birlikte `gerekce=` ve `risk_eslesme=`
parametreleriyle ver.

Hangi dokümanların üretileceği: `references/dokuman-listesi.md`
Madde bazlı zorunlu dokümante bilgi: `references/madde-4-10.md`
Ek A kontrol → doküman → kanıt eşlemesi: `references/annex-a-kontroller.md`

### 4 — Öz denetim yap ve raporla

Ürettiğin seti kendi kontrol listenle geç: `references/denetim-oz-kontrol.md`.
`[DOLDURULACAK]` etiketlerini say, çapraz referansların doğruluğunu doğrula,
kapsam beyanının her dokümanda aynı olduğunu kontrol et, kalan İngilizce
kısaltmaları ve yol gösterici dosyalara kodla verilmiş atıfları tara. Bulguları
`OKUBENI.md` içinde "denetim öncesi kapatılması gerekenler" başlığı altında ver.

## Kırılma noktaları

Bu skill'in üreteceği setin denetimde başarısız olmasına yol açan en yaygın
hatalar bunlar. Üretim sırasında her birine karşı uyanık ol:

**Jenerik metin.** "Kuruluşumuz bilgi güvenliğine önem vermektedir" cümlesi
hiçbir şey söylemez. Gerçek birim adları, gerçek sistem adları, gerçek sayılar
kullan. Bilgi yoksa `[DOLDURULACAK: BT departmanının resmi adı]` yaz — boş
bırakmak yerine görünür bir boşluk bırakmak dürüst ve işlevseldir.

**Bildirgenin risk değerlendirmesinden kopması.** Denetçi bildirgedeki bir
kontrolü seçip "bu neden gerekli?" diye sorar. Cevap risk envanterindeki bir
risk numarası olmalı. "Gerekçe" sütununu risk numaralarıyla doldur.

**Hariç tutma hatası.** Madde 4–10 hariç tutulamaz — standardın kendi ifadesiyle
"kabul edilemez". Ek A kontrolleri gerekçeyle hariç tutulabilir. Kullanıcı bir
maddeyi kapsam dışı bırakmak isterse bu ayrımı net söyle.

**Ölçülemez ifadeler.** "Düzenli olarak", "yeterli", "gerektiğinde" — bunlar
bulgu mıknatısıdır. Her birini sayı ve sıklıkla değiştir: "üç ayda bir",
"en az 12 karakter", "24 saat içinde".

**Uydurulmuş kayıt.** Örnek risk, örnek varlık, örnek olay üretebilirsin ama
her birini "ÖRNEK — kuruluş tarafından doğrulanacak" diye işaretle. Gerçekmiş
gibi sunulan sahte kayıt hem etik değil hem de denetimde sistemin güvenilirliğini
tümden yok eder.

**Ölçek uyumsuzluğu.** 15 kişilik bir şirkete 45 dokümanlık set vermek zarar
verir: kimse okumaz, uygulamaz, denetimde "yaşamayan sistem" bulgusu gelir.
50 kişi altındaysa `references/dokuman-listesi.md` içindeki sadeleştirilmiş
seti kullan — prosedürler birleştirilir, sayı düşer, sistem yaşar.

**Doküman listesinin kendisindeki tutarsızlıklar.** Mevcut BGYS doküman listesi
verildiyse şunları tara ve raporla: aynı adı taşıyan farklı kodlar, adında tarih
geçen formlar, boş revizyon alanları, "son gözden geçirme" tarihinin revizyon
tarihinden önce olması, dış kaynaklı listede eski standart sürümü (ör. 27001
2013 tarihli) veya eksik mevzuat.

## Denetim hazırlık yol göstericileri

Boşluk raporu, revizyon rehberleri, kontrol-kanıt matrisi ve öz değerlendirme
yönetim sisteminin parçası değildir; denetim öncesinde üst yönetime neyin, kim
tarafından, hangi sırayla yapılacağını gösteren yol göstericilerdir.
`iso-entegre-yonetim-sistemi` K2 kuralı uygulanır: doküman kodu yok, dosya adı
yalnız ad; kapakta "YOL GÖSTERİCİ", antette "Doküman Türü | Yol Gösterici";
onay yönetim sistemi komitesi başkanı; Doküman Listesi'ne girmez ve listenin not
alanında bu açıklanır; setin geri kalanı bu dosyalara adıyla atıf verir.
`07_Denetim_Hazirlik` klasöründe durur.

## Kullanıcı bir doküman istediğinde

Kullanıcı tüm seti değil tek bir doküman istiyorsa (örn. "bana sadece erişim
kontrol prosedürü lazım") aynı kaliteyi koru ama süreci kısalt: kuruluş adı,
kapsam ve varsa şablonu sor, üret, ilgili maddeleri ve kanıt beklentisini
dokümanın sonunda belirt. Tüm seti dayatma; ihtiyaç duyulan parçayı ver ve
setin geri kalanını isterse üretebileceğini bir cümleyle belirt.

## Entegre sistem

Kullanıcının ISO 9001, 22301, 20000-1 veya 42001 sistemi varsa ortak dokümanları
(doküman kontrol, iç tetkik, YGG, düzeltici faaliyet, yetkinlik/farkındalık)
birleştir — `EYS-` önekiyle tek doküman üret, kapsam bölümünde her iki standardın
maddesine atıf ver. Aynı prosedürü iki kez yazmak hem kullanıcıyı hem denetçiyi
yorar ve tutarsızlık riski doğurur.

**27701:2019 eklenecekse** BGYS dokümanlarını yeniden yazma; `iso-27701-dokuman-seti`
ile KVYS katmanını üret ve BGYS dokümanlarına eklenecek kişisel veri içeriğini
doküman bazında **BGYS Dokümanları KVYS Revizyon Rehberi** (kodsuz yol
gösterici) ile ver. BGYS 27002:2022'de ise 27701:2019 Madde 6 (27002:2013
numaraları) için eşleme tablosu gerekir.

## Kurumsal şablonu birebir kullanma

Kullanıcı mevcut bir kurumsal dokümanı "şablon olarak bire bir kullan" diye
verirse `ys_docx.py`'nin varsayılan kimliği yerine şablonu klonla: kapak kodu ve
antet hücrelerini değiştir (antet adını `tr_upper()` ile büyüt), şablonun başlık/
gövde/liste paragraflarını rPr dahil prototip olarak çoğalt, İçindekiler'i
bookmark + `PAGEREF` ile yeniden kur ve sayfa numaralarını LibreOffice
render'ıyla hesapla, sabit toplam sayfa metnini `SECTIONPAGES` alanıyla değiştir.
Excel için kuruluşun mevcut liste dosyasının "Doküman Bilgisi" sayfasını ve
logosunu koru. Her dosyayı PDF'e çevirip görsel kontrol et.

## Türkçe terim kuralı

Kullanıcı aksini istemedikçe başlık ve doküman adlarında İngilizce kısaltma
kullanma (SoA → Uygulanabilirlik Bildirgesi, DLP → Veri Sızıntısı Önleme sistemi,
SIEM → Güvenlik Olay ve Kayıt Yönetim sistemi, CCTV → kapalı devre kamera, MFA →
çok faktörlü kimlik doğrulama, SOC → Güvenlik Operasyon Merkezi). İngilizce
karşılığı yalnız Tanımlar tablosunda parantez içinde ver; ürün adları olduğu
gibi kalır. Motorda sözlük + `tr()` fonksiyonuyla tüm metinlere uygula.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Girdi | Cihaz köprüsü (`device_list_dir`, `device_bash`, `device_stage_files`) | Bağlı klasördeki mevcut dokümanları yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa |
| Mevzuat teyidi | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher`, `regulatory-legal:policy-diff` | 5651, 7545, BİG Rehberi, sektörel düzenlemelerin güncelliği |
| Tedarikçi | `commercial-legal:vendor-agreement-review`, `commercial-legal:saas-msa-review` | A.5.19–5.23 tedarikçi ve bulut sözleşmeleri |
| Kişisel veri | `iso-27701-dokuman-seti`, `privacy-legal:*` | KVKK katmanı |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf` | Üretim ve doğrulama |
| Görsel kontrol | `soffice` → `pdftoppm` → Read | Şablon birebirliği |
| Entegrasyon | `iso-entegre-yonetim-sistemi` | Çoklu standart, K1–K4 kuralları |
| Teslim | `device_commit_files` (bağlı klasörde yeni alt klasör) | Kullanıcının dosyalarını değiştirmeden teslim |

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/gorusme-rehberi.md` | Her çalışmanın başında — soru stratejisi |
| `references/dokuman-listesi.md` | Plan aşamasında — ne üretilecek |
| `references/madde-4-10.md` | Yönetim sistemi dokümanlarını yazarken |
| `references/annex-a-kontroller.md` | Bildirge ve kontrol dokümanlarını yazarken |
| `references/icerik-rehberi.md` | Her dokümanın gövdesini yazarken |
| `references/dokuman-mimarisi.md` | Kodlama, hiyerarşi, ortak bölümler |
| `references/denetim-oz-kontrol.md` | Üretim bitince — teslim öncesi kontrol |

## Bağımlılıklar

`python-docx` ve `openpyxl` gerekir:

```bash
pip install python-docx openpyxl --break-system-packages
```