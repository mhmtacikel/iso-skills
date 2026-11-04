---
name: "iso-27701-dokuman-seti"
description: "ISO/IEC 27701 Kişisel Veri Yönetim Sistemi (KVYS/PIMS) için belgelendirme denetiminden geçebilecek doküman seti üretir — hem 2019 (27001 eklentisi) hem 2025 (bağımsız sistem) sürümü, ayrıca 2019→2025 geçiş ve boşluk analizi. Veri işleme envanteri, aydınlatma metni, açık rıza, DPIA, ilgili kişi başvuru süreci, saklama-imha, yurt dışı aktarım, veri ihlali yönetimi, Uygulanabilirlik Bildirgesi ve KVKK eşleme matrisi dahil; kurumsal Word/Excel stilleriyle. Kullanıcı \"ISO 27701 dokümanları hazırla\", \"KVYS kur\", \"PIMS\", \"kişisel veri yönetim sistemi\", \"27701 belgelendirmeye hazırlan\", \"27701:2025 geçiş\", \"veri işleme envanteri\", \"DPIA yap\", \"aydınlatma metni yaz\", \"VERBİS\", \"ilgili kişi başvuru prosedürü\", \"saklama imha politikası\", \"veri ihlali prosedürü\" dediğinde mutlaka kullan. Standart anılmasa bile kişisel veri koruma yönetim sistemi, KVKK/GDPR uyum dokümantasyonu veya gizlilik sertifikasyonu bağlamı varsa devreye girmeli."
---

# ISO/IEC 27701 Kişisel Veri Yönetim Sistemi Doküman Seti Üretimi

Bu skill bir kuruluşun KVYS'sini kurabilecek doküman setini üretir. Hedef dosya
sayısı değil: **denetçinin masaya koyduğunda uygunsuzluk yazamayacağı bir set.**

27701'in özel yanı: **iki sürümü yapısal olarak farklı standartlardır.**

| | **2019** | **2025** |
|---|---|---|
| Niteliği | ISO/IEC 27001 + 27002'ye **eklenti** | **Bağımsız** yönetim sistemi standardı |
| 27001 şartı | **Zorunlu** — 27001 belgesi olmadan 27701 alınamaz | Gerekli değil; tek başına belgelendirilebilir |
| Yapı | Madde 5 (27001 eklemeleri), 6 (27002 eklemeleri), 7 (veri sorumlusu), 8 (veri işleyen) | Annex SL: Madde 4–10 + Ek A/B/C/D/E/F |
| Kontroller | Ek A: 31 (veri sorumlusu) + Ek B: 18 (veri işleyen) = **49** | A.1: 31 + A.2: 18 + A.3: 29 = **78** |
| A.3 | Yok | **Yeni** — 27002:2022'den seçilmiş 29 bilgi güvenliği kontrolü |
| Yayım | Aralık 2019 (TS ISO/IEC 27701:2019) | Ekim 2025 |

Bu farkı kavramadan üretilen doküman seti yanlış sürümü hedefler ve boşa gider.
İlk iş sürümü netleştirmektir.

## Çalışma akışı

### 1 — Sürümü ve rolü belirle (her zaman, ilk adım)

Üç soru, üretimin tamamını belirler. `AskUserQuestion` varsa onunla sor.

**Soru 1 — Hangi sürüm?**

- **2019** → Kuruluşun ISO/IEC 27001 belgesi var mı? Yoksa önce onu kurmak
  gerekir; 27701:2019 tek başına belgelendirilemez. Bunu açıkça söyle.
- **2025** → Bağımsız kurulabilir. 27001 varsa entegre edilir, yoksa gerekmez.
- **Geçiş (2019 → 2025)** → Mevcut 2019 dokümantasyonunu iste, boşluk analizi
  yap, farkları kapat. Belgelendirme kuruluşları geçiş için süre tanır;
  kullanıcı süreyi kendi belgelendirme kuruluşundan teyit etmeli — bu tarihi
  sen uydurma.
- **Emin değil** → Yeni kurulumsa 2025'i öner (2019 yeni belgelendirmeler için
  kapanmaya doğru gider ve zaten 27001 zorunluluğu getirir). Mevcut 2019
  belgesi varsa geçiş planı öner.

**Soru 2 — Kuruluşun rolü ne?** Veri sorumlusu mu, veri işleyen mi, ikisi de mi?
Bu, hangi kontrol setinin uygulanacağını belirler:

| Rol | 2019 | 2025 |
|---|---|---|
| Yalnız veri sorumlusu | Ek A (31) | A.1 (31) + A.3 (29) |
| Yalnız veri işleyen | Ek B (18) | A.2 (18) + A.3 (29) |
| İkisi de | Ek A + Ek B (49) | A.1 + A.2 + A.3 (78) |

Çoğu kuruluş **ikisidir**: kendi çalışanlarının verisi için sorumlu, müşteri
verisi için işleyen. Bunu varsayma, sor — ama iki rolün aynı anda olabileceğini
hatırlat. Hangi işleme faaliyetinde hangi rolde olduğu envanterde sütun olmalı.

**Soru 3 — Mevcut 27001 durumu?** Belgeli / kuruluyor / yok. Entegre doküman
seti mi, bağımsız mı üretileceğini bu belirler.

Ardından `references/gorusme-rehberi.md`'deki altı soruluk genel açılış
anketini sor (kuruluş, kapsam, ölçek, dış kaynak, mevcut dokümanlar, hedef).

27701'e özgü olarak şu üçünü de sor — envanter ve etki değerlendirmesi bunlara dayanır:

- **Hangi kişisel veri kategorilerini işliyorsunuz?** Özel nitelikli veri
  (sağlık, biyometrik, din, ceza mahkûmiyeti, sendika) var mı? KVKK m.6 ayrı
  bir rejim getirir ve etki değerlendirmesi eşiğini düşürür.
- **Yurt dışına veri aktarıyor musunuz?** (bulut, grup şirketi, tedarikçi,
  uluslararası protokol) KVKK m.9 dayanağı — yeterlilik kararı, standart
  sözleşme, taahhütname veya bağlayıcı şirket kuralları — belirlenmeli. Şu an
  aktarım yoksa bunu tarihli beyan olarak kaydet ve gelecekteki aktarım için
  önleyici akışı prosedürde bırak.
- **Otomatik karar veren bir sisteminiz var mı?** (kredi skoru, işe alım eleme,
  fiyatlandırma, içerik moderasyonu) Varsa A.1.3.11 / 7.3.10 devreye girer ve
  ISO 42001 ile kesişme oluşur. Yoksa kontrolü "uygulanabilir — faaliyet yok,
  önleyici kontrol" olarak bırakmayı öner.

Kurumsal şablon yüklendiyse önce tanı:

```bash
python3 scripts/sablon_analiz.py "<şablon.docx>"
```

### 2 — Kapsamı ve plan taslağını onaylat

Üretime başlamadan tek ekranlık planı sun: sürüm, rol, kapsam beyanı, doküman
sayısı, kodlama kuralı, hariç tutulacak kontroller, hangi dosyaların kodsuz
yol gösterici olacağı.

**2019 kapsamı** BGYS kapsamının içinde veya ona eşit olmalıdır — KVYS, BGYS'nin
bir uzantısıdır ve onun dışına taşamaz. Kapsam cümlesinde bu ilişki görünmeli.

**2025 kapsamı** bağımsız tanımlanır ama kişisel veri işleme faaliyetleriyle
sınırlıdır.

Kapsam cümlesi kalıbı:

> "[Unvan]'ın [lokasyon] adresinde, [veri sorumlusu / veri işleyen / her iki]
> sıfatıyla yürüttüğü [faaliyet] kapsamındaki kişisel veri işleme faaliyetlerini
> kapsayan kişisel veri yönetim sistemi. [2019 için: Bu KVYS, [BGYS kapsam
> referansı] kapsamındaki bilgi güvenliği yönetim sistemine dayanmaktadır.]
> Uygulanabilirlik Bildirgesi [kod] Rev. [nn] geçerlidir."

### 3 — Üret

Sıra kritiktir; zincirin başı envanterdir:

1. **Kapsam + El Kitabı** (2019: BGYS'ye bağlanarak)
2. **Bağlam, ilgili taraflar** — ilgili taraflar listesinde **ilgili kişi**
   (veri sahibi) mutlaka yer almalı
3. **Kişisel veri işleme envanteri** — VERBİS ile hizalı; zincirin başı
4. **KVYS politikası** ve konuya özgü politikalar
5. **Risk değerlendirmesi → gizlilik etki değerlendirmesi → Uygulanabilirlik Bildirgesi**
6. **İlgili kişi hakları süreci** (aydınlatma, rıza, başvuru, itiraz)
7. **Saklama-imha, aktarım, ihlal yönetimi**
8. **Performans, iç tetkik, YGG, DÖF**
9. **KVKK eşleme matrisi + OKUBENI.md**
10. **Denetim hazırlık yol göstericileri** (kodsuz — aşağıdaki bölüm): boşluk
    raporu, revizyon rehberleri, kontrol-kanıt matrisi ve öz değerlendirme

**Zincir kuralı:** Envanterdeki her işleme faaliyetinin bir hukuki sebebi, bir
saklama süresi, bir aydınlatma metni referansı ve (gerekiyorsa) bir gizlilik etki
değerlendirmesi olmalı. Denetçi envanterden rastgele bir satır seçip bunları sorar.

Word için `scripts/ys_docx.py`, Excel için `scripts/ys_xlsx.py`, kayıtlar için:

```bash
python3 scripts/kayitlar_27701.py --kurulus "..." --cikti "<klasör>" \
  --surum 2025 --rol her-ikisi --tarih 2026-08-11
```

`--surum 2019|2025` ve `--rol sorumlu|isleyen|her-ikisi` bayrakları
Uygulanabilirlik Bildirgesi'nin hangi kontrolleri içereceğini belirler. Yanlış
sürüm bayrağı yanlış numaralı bir bildirge üretir; bunu kontrol et.

### 4 — Öz denetim yap ve raporla

`references/denetim-oz-kontrol.md` listesini geç, ayrıca 27701'e özgü envanter
zincirini doğrula. Bir denetim betiğiyle şunları tara: kalan İngilizce
kısaltmalar, kırık doküman kodu atıfları, yol gösterici dosyalara kodla verilmiş
atıf, `[DOLDURULACAK]` / `[ÖRNEK]` / `[DOĞRULANACAK]` / Hukuk teyidi etiket
sayıları (dosya bazında). Bulguları `OKUBENI.md`'de "Denetim öncesi kapatılması
gerekenler" tablosunda (öncelik, konu, dosya, yapılacak) raporla.

## Kırılma noktaları

**Sürüm karışıklığı.** 2019 kontrolü `A.7.2.1`, 2025 karşılığı `A.1.2.2`.
Numaralar birbirine benziyor ama farklı. Tek bir dokümanda iki numaralandırmayı
karıştırmak denetçide "hangi standarda göre kurdunuz?" sorusunu doğurur.
`references/kontroller.md` iki sürümün karşılıklı tablosunu içerir; atıf
verirken oradan doğrula.

**2019'da 27001 zemininin unutulması.** 2019 sürümü, 27001 Madde 4–10 ve
27002 kontrollerine **eklemeler** yapar. KVYS dokümanı BGYS dokümanına atıf
vermiyorsa sistem havada kalır. Madde 5.2.1'den itibaren her ekleme, ilgili
27001 maddesine bağlanmalı.

**Veri sorumlusu / veri işleyen rolünün belirsizliği.** Bir kuruluş aynı anda
her iki rolde olabilir ama **her işleme faaliyeti için rol tekildir**. Envanterde
"rol" sütunu boşsa ya da "her ikisi" yazıyorsa bu bir eksikliktir; faaliyet
bazında netleşmeli.

**Envanterin VERBİS'ten kopması.** Türkiye'de denetçi büyük olasılıkla VERBİS
kaydınıza bakacaktır. İşleme envanteri ile VERBİS bildirimi çelişiyorsa bu hem
27701 hem KVKK açısından bulgu üretir. Envanteri VERBİS alan yapısına hizalı
üret — `references/kvkk-eslesme.md` bu alanları listeler.

**Etki değerlendirmesi eşiğinin tanımsız olması.** "Gerektiğinde gizlilik etki
değerlendirmesi yapılır" bir kriter değildir. Hangi durumlarda zorunlu olduğu
yazılı olmalı: özel nitelikli veri, büyük ölçekli işleme, sistematik izleme,
otomatik karar, yeni teknoloji, çocuk verisi. Kurul'un yayımladığı kriterler
varsa onlara atıf ver.

**Aydınlatma ile açık rızanın karıştırılması.** Aydınlatma bir **yükümlülüktür**
ve her işlemede yapılır (KVKK m.10). Açık rıza bir **hukuki sebeptir** ve
yalnızca başka bir sebep yoksa alınır (m.5/1). İkisini tek metinde birleştirmek
ve "rıza veriyorum" kutucuğuna aydınlatmayı gömmek yaygın ve yanlış bir
uygulamadır; ayrı metin, ayrı kayıt üret.

**Saklama süresinin gerekçesiz olması.** Her veri kategorisi için saklama
süresi **ve dayanağı** (mevzuat maddesi, zamanaşımı, sözleşme) yazılmalı.
"10 yıl" tek başına savunulamaz; "TTK m.82 uyarınca 10 yıl" savunulabilir.
Kesinleşmemiş süreleri "Önerilen" sütununda ver ve `[Hukuk Müşavirliğince
teyit edilecek]` etiketle.

**İhlal bildirim süresinin atlanması.** Kurul'a "en kısa sürede ve 72 saat
içinde" bildirim yükümlülüğü var. Prosedürde saat bazlı akış, karar verici ve
yedek karar verici tanımlı olmalı — ihlal gece yarısı olur ve o an kimin karar
vereceği belli değilse süre kaçar.

**Uydurulmuş kayıt.** Örnek envanter satırı, örnek etki değerlendirmesi
üretebilirsin; ama gerçekleşmiş ilgili kişi başvurusu, gerçek ihlal kaydı,
imzalı rıza uydurulamaz. `[ÖRNEK — doğrulanacak]` etiketle. Kişisel veri
alanında sahte kayıt yalnızca denetimi değil, ilgili kişilerin haklarını da etkiler.

## Mevcut doküman analizi (kullanıcı hazır dokümanlar verdiğinde)

Kullanıcı "hazırlanmış dokümanlar ektedir, bunları baz al" dediğinde önce
**Mevcut Doküman Değerlendirme ve Boşluk Raporu**'nu (kodsuz yol gösterici)
üret, sonra seti bu bulguları kapatacak şekilde kur. Sık görülen ve mutlaka
taranması gereken hatalar:

- **Etki değerlendirmesi dosyasında sütun kayması:** "Yapılacak işlem / sorumlu"
  sütunları başka birimin/şablonun içeriğini taşıyor olabilir. Satır–faaliyet
  eşleşmesini tek tek kontrol et; kopuksa dosyayı yeniden kur, eskisini düzeltme.
- **Formülsüz veya #N/A risk skorları**, numarasız satırlar, taslak notları.
- **"Süresiz" / boş / anlamsız saklama süreleri** ("101 yıl", "2 ay;; 5 gün") —
  sayıp listele; her biri için süre + başlangıç olayı + dayanak öner ve
  `[Hukuk Müşavirliğince teyit edilecek]` etiketle.
- **m.6/3-b (özel nitelikli dayanak) özel nitelikli olmayan veride**, **m.5/2-c
  sözleşmenin tarafı olmayan firma çalışanları için**, **kamu işvereninde sağlık
  verisine açık rıza** (2024 değişikliği sonrası m.6/3'te istihdam yükümlülüğü
  dayanağı var) — faaliyet numaralarıyla raporla.
- **Uygulanabilirlik Bildirgesi'nde gerekçe / uygulama durumu sütunu yok, Ek B'de
  doküman atfı yok, "uygulanabilir" + "faaliyet yok" çelişkisi** — gerekçeli
  yeniden üret; faaliyet olmayan kontrolleri "önleyici kontrol" olarak
  uygulanabilir bırakmayı öner.
- **27701:2019 + 27002:2022 uyumsuzluğu** — bildirgeye "Madde 6 → 27002:2013 →
  2022" eşleme sayfası ekle.
- **Kamu kurumunda birim ≠ veri sorumlusu.** Bakanlık/kurum tüzel kişiliği veri
  sorumlusudur; bir genel müdürlük "veri sorumlusu adına işleyen birim" ve diğer
  birimlerin sistemlerini barındırıyorsa "iç hizmet sağlayıcı (veri işleyen)"
  rolündedir. Aynı tüzel kişilikte sözleşme yerine **Veri İşleme Talimatı Formu**
  üret. Kurul'a bildirimi kurum irtibat kişisi yapar; ihlal prosedüründe bu
  arayüzü saat bazlı akışa koy. Birimde kişisel veri organizasyonu yoksa
  (komite, KVYS yöneticisi) birim içinde kur ve atamaları `[DOLDURULACAK]` bırak.
- **Uyum yazılımında (ör. JUS., VERBİS portalı) tutulan kurum düzeyi dokümanlar**
  (aydınlatma/rıza metinleri, başvuru prosedürü, aktarım prosedürü) kullanıcı
  aksini söylemedikçe **yeniden yazılmaz**; her biri için "nasıl olmalı"
  içeriğini, kabul kriterlerini ve birime özgü eksikleri veren bir **revizyon
  rehberi** (kodsuz yol gösterici) üret. 2019'da BGYS dokümanları için de aynı
  mantıkla **BGYS Dokümanları KVYS Revizyon Rehberi** (doküman bazında eklenecek
  içerik + öncelik) üret.
- Süreç listesinde **kişi adları** varsa dokümanlarda unvan kullan; adları yalnız
  envanterin "süreç sorumlusu" sütununda tut.

## Denetim hazırlık yol göstericileri (07_Denetim_Hazirlik)

Boşluk raporu, BGYS ve uyum yazılımı revizyon rehberleri, kontrol-kanıt matrisi
ve öz değerlendirme **yönetim sistemi dokümanı değildir**. Bunlar belgelendirme
denetiminden önce üst yönetime ve KVYS Komitesine neyin, kim tarafından, hangi
sırayla yapılacağını gösteren **yol göstericilerdir**.
`iso-entegre-yonetim-sistemi` K2 kuralını uygula:

- **Doküman kodu verilmez.** Dosya adı yalnız addır: `Mevcut Doküman
  Değerlendirme ve Boşluk Raporu.docx`, `Kontrol-Kanıt Matrisi ve Öz
  Değerlendirme.xlsx`.
- Kapakta kod yerine **"YOL GÖSTERİCİ"**; antette "Doküman No" yerine
  **"Doküman Türü | Yol Gösterici"**. Antetteki toplam sayfa alanını güncelleyen
  kod her iki etiketi de tanımalı, yoksa "n/1" kalır. Excel'de "Doküman
  Bilgisi" sayfasındaki kod hücresi de aynı biçimde değişir.
- Onay satırı **KVYS Komitesi Başkanı**; üst yönetim onayı gerekmez.
- Metnin başına kısa bir not: "Bu dosya yönetim sistemi dokümanı değildir,
  doküman kontrolüne tabi değildir; iş ilerledikçe güncellenir."
- **Doküman Listesi'ne girmez.** Listenin not alanına bunun bilinçli tercih
  olduğunu yaz; yoksa denetçi "eksik doküman" sanar. OKUBENI'de sayıyı "n kodlu
  doküman + m yol gösterici" diye ayrı ver.
- Setin geri kalanında bu dosyalara **adıyla** atıf verilir. Üretimde iç kısa
  kod kullandıysan `tr()` içindeki bir regex ile kodu (Türkçe ekleriyle: 'de,
  'te, 'ye, 'dedir) dosya adına çevir ve teslimden önce setin tamamında eski kod
  kalmadığını tara.
- Kullanıcı sonradan kodsuza geçilmesini isterse bağlı klasördeki eski kodlu
  dosyaları silme; `_to_delete/` alt klasörüne `mv -n` ile taşı ve kullanıcıya
  söyle.

## Türkçe terim kuralı

Kullanıcı aksini istemedikçe başlıklarda ve doküman adlarında İngilizce kısaltma
kullanma: DPIA/GEA → "Gizlilik Etki Değerlendirmesi" (kayıt no `ED-nn`), SoA →
"Uygulanabilirlik Bildirgesi", PII → "kişisel veri", PII principal → "ilgili
kişi", DLP → "Veri Sızıntısı Önleme sistemi", SIEM → "Güvenlik Olay ve Kayıt
Yönetim sistemi", CCTV → "kapalı devre kamera", IVR → "sesli yanıt sistemi",
MFA → "çok faktörlü kimlik doğrulama", taşeron → "alt yüklenici". İngilizce
karşılık yalnızca Tanımlar tablosunda parantez içinde bir kez verilir; ürün adları
(QRadar, Azure DevOps, EBYS, MERSİS) olduğu gibi kalır. Bunu motorda bir sözlük +
`tr()` fonksiyonuyla tüm Word/Excel metinlerine uygula; kullanıcının mevcut
bildirge çevirisindeki "PII'nin", "PII ilgilileri" gibi ekli biçimleri de
sözlüğe koy. Ekli biçimlerde yeni ek üretirken ünlü uyumunu kontrol et
("Alt yükleniciun" gibi hatalar sıralama hatasından çıkar; uzun ifadeleri önce
değiştir).

## Kurumsal şablonu birebir kullanma

Kullanıcı "bu dokümanı şablon olarak bire bir kullan" derse `ys_docx.py` yerine
**şablonu klonla**:

- Şablonu `python-docx` ile aç; kapaktaki kod metnini, antet tablosundaki doküman
  adı / no / yayın tarihi / revizyon hücrelerini değiştir. Antetteki adı
  **`tr_upper()`** ile büyüt (Python `.upper()` "i"yi "I" yapar).
- Mevcut Heading 1 / Heading 2 / gövde / liste paragraflarını **prototip** olarak
  kopyala (rPr dahil; yoksa başlıklar varsayılan mavi/Cambria'ya düşer); şablon
  başlıklarını (Amaç, Kapsam, Revizyon, Tanımlar, Uygulama, İlgili Dokümanlar)
  koru, ek bölümleri "Uygulama" altına H2 olarak ekle. Tüm başlıkları tek bir
  numaralandırma listesine bağla.
- İçindekiler'i başlıklara eklenen bookmark'lar + `PAGEREF` alanlarıyla yeniden
  kur (ikinci düzey satırlara sol sekme ekle); sayfa numaralarını LibreOffice
  ile PDF'e çevirip `pdftotext` ile hesapla ve alan önbelleğine yaz.
- Antetteki toplam sayfa sayısı şablonda sabit metin olabilir — `SECTIONPAGES`
  alanıyla değiştir.
- Excel için kuruluşun mevcut liste dosyasını (ör. BGYS-LS-14) aç, "Doküman
  Bilgisi" sayfasını ve logosunu koru, diğer sayfaları silip veri sayfalarını aynı
  antetle ekle.
- Revizyon 0 yayın tarihini kullanıcı aksini söylemedikçe boş bırak; onay
  bloğunu şablondaki gibi koru; kişi adı yerine unvan yaz.
- Her dosyayı PDF'e çevirip en az bir sayfasını görsel olarak kontrol et.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Girdi | Cihaz köprüsü (`device_list_dir`, `device_bash`, `device_stage_files`) | Bağlı klasördeki mevcut Excel/PDF'leri yerinde oku (`python3 + openpyxl`, `pdftotext`); yalnız şablon .docx ve görsel kontrol gereken dosyaları buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa arama ve okuma |
| Mevzuat teyidi | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher`, `regulatory-legal:policy-diff` | KVKK değişiklikleri, Kurul kararları, yönetmelik güncelliği; tarih/süre uydurma |
| Hukuki içerik | `privacy-legal:pia-generation`, `privacy-legal:dsar-response`, `privacy-legal:dpa-review`, `privacy-legal:reg-gap-analysis` | Etki değerlendirmesi, başvuru yanıtı, veri işleyen sözleşmesi, mevzuat boşluk analizi |
| Sözleşmeler | `commercial-legal:vendor-agreement-review`, `commercial-legal:saas-msa-review` | Tedarikçi veri işleme şartları, bulut/SaaS aktarımı |
| İK verisi | `employment-legal:policy-drafting` | Çalışan verisi, izin/rapor, kamera politikaları |
| Otomatik karar | `ai-governance-legal:aia-generation`, `iso-42001-dokuman-seti` | 7.3.10 / A.1.3.11 kesişimi |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf` | Word/Excel/PDF üretim ve doğrulama |
| Görsel kontrol | `soffice --headless --convert-to pdf` → `pdftoppm` → Read | Şablon birebirliği, tablo taşmaları |
| Entegrasyon | `iso-entegre-yonetim-sistemi`, `iso-27001-dokuman-seti` | 2019'da BGYS zemini, çoklu standart, K1–K4 kuralları |
| Teslim | `device_commit_files` (bağlı klasöre alt klasör olarak), gerekirse Artifact | Kullanıcının dosyalarını değiştirmeden yeni klasöre yaz |

## 2019 → 2025 geçişi

Kullanıcı geçiş istiyorsa `references/gecis-2019-2025.md` dosyasını oku. Özet
mantık: 2019'daki 49 kontrol 2025'te birebir karşılığıyla yaşamaya devam eder
(yalnızca numaraları değişir), asıl iş **A.3'ün 29 bilgi güvenliği kontrolünü**
karşılamak ve **bağımsız yönetim sistemi gövdesini** (Madde 4–10) kurmaktır.
27001 belgesi olan bir kuruluşta A.3'ün büyük kısmı zaten karşılanmıştır;
işin çoğu yeniden numaralandırma ve kanıt eşlemesidir.

## Kullanıcı tek doküman istediğinde

Süreci kısalt, kaliteyi koru: sürüm, rol, kuruluş, kapsam ve varsa şablonu sor;
üret; ilgili maddeleri, kontrol numarasını (doğru sürümle) ve kanıt beklentisini
dokümanın sonunda belirt.

## Entegre sistem

**27001 ile:** en yaygın kombinasyon. 2019'da zaten zorunlu. Ortak dokümanları
(doküman kontrol, iç tetkik, YGG, DÖF, yetkinlik, ihlal yönetimi) `EYS-` önekiyle
tek doküman üret; ihlal prosedürüne KVKK bildirim akışını ek bölüm olarak koy.

**42001 ile:** otomatik karar veren YZ sistemleri varsa kesişir. 42001'in etki
değerlendirmesi ile 27701'in gizlilik etki değerlendirmesi birbirini besler ama
**aynı şey değildir**: gizlilik etki değerlendirmesi mahremiyet odaklı ve hukuki,
YZ etki değerlendirmesi daha geniş (adillik, özerklik, toplumsal etki). İkisini
birleştirme, birbirine referans ver.

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/surum-2019.md` | 2019 sürümü seçildiyse — madde yapısı, doküman listesi |
| `references/surum-2025.md` | 2025 sürümü seçildiyse — madde yapısı, doküman listesi |
| `references/kontroller.md` | Her iki sürümün kontrol tabloları ve karşılıklı eşlemesi |
| `references/gecis-2019-2025.md` | Geçiş veya boşluk analizi isteniyorsa |
| `references/kvkk-eslesme.md` | Türkiye'deki her kurulumda — VERBİS, aydınlatma, İKBS, aktarım |
| `references/icerik-rehberi.md` | Metin kalitesi — örnek zayıf/güçlü metinler |
| `references/gorusme-rehberi.md` | Genel açılış anketi ve soru stratejisi |
| `references/dokuman-mimarisi.md` | Kodlama, hiyerarşi, ortak bölümler |
| `references/denetim-oz-kontrol.md` | Teslim öncesi |

## Bağımlılıklar

```bash
pip install python-docx openpyxl --break-system-packages
```