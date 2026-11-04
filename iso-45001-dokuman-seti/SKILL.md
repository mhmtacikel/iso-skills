---
name: "iso-45001-dokuman-seti"
description: "ISO 45001:2018 (+Amd 1:2024, TS EN ISO 45001) İş Sağlığı ve Güvenliği Yönetim Sistemi için 6331 sayılı Kanun ve alt mevzuatıyla entegre, belgelendirme denetiminden geçebilecek doküman seti üretir ya da mevcut İSG setini analiz edip yeniler — kapsam, İSG politikası, prosedürler, tehlike belirleme ve risk değerlendirme tablosu, yasal şartlar listesi, acil durum planı, iş izni, talimatlar, makine güvenlik talimatları, formlar, planlar; kurumsal Word/Excel stilleriyle. Kullanıcı \"45001 dokümanları hazırla\", \"İSG yönetim sistemi kur\", \"İSG prosedürü yaz\", \"risk değerlendirmesi formu\", \"acil durum planı\", \"İSG doküman setimi incele/yenile\", \"OHSAS'tan 45001'e geçiş\", \"İSG belgelendirmeye hazırlan\", \"iş güvenliği talimatı\" dediğinde ya da İSG/iş güvenliği dokümantasyonu, ISO 45001 denetimine hazırlık, boşluk analizi, İSG klasörü düzenleme işi geçtiğinde mutlaka kullan — standardı açıkça anmasa bile iş sağlığı ve güvenliği yönetim sistemi bağlamı varsa devreye girmeli."
---

# ISO 45001 Doküman Seti Üretimi ve Yenilenmesi

Bu skill bir kuruluşun İSG Yönetim Sistemi'ni (İSGYS) sıfırdan kurar ya da yıllar
içinde birikmiş mevcut İSG setini analiz edip 45001'e uygun hale getirir. Hedef
dosya sayısı değil: **belgelendirme denetçisinin ve iş müfettişinin masaya
koyduğunda bulgu yazamayacağı, sahada yaşayan bir set.**

İSG'de bu iki denetçi aynı dosyaya bakar. 45001 denetçisi süreci, müfettiş 6331'i
sorar; ama ikisinin de ilk istediği risk değerlendirmesi, eğitim kayıtları, acil
durum planı ve periyodik kontrollerdir. Bu yüzden set, yasal yükümlülükleri ayrı
bir "mevzuat dosyası" olarak değil, standardın maddelerine gömülü olarak taşır.

Bu skill `iso-*-dokuman-seti` ailesinin üyesidir: kodlama, klasör yapısı, Word/Excel
motoru, OKUBENI ve yol gösterici kuralları ailedeki 27001/42001/27701 skill'leriyle
aynıdır ve `iso-entegre-yonetim-sistemi` tarafından motor olarak çağrılabilir.

## Çalışma akışı

### 1 — Kuruluşu tanı (üretimden önce, her zaman)

`references/gorusme-rehberi.md` içindeki **altı soruluk açılış anketini** sor
(`AskUserQuestion` ile, çoktan seçmeli). 45001'e özgü olarak şunları da sor:

- **NACE kodu ve tehlike sınıfı** (az tehlikeli / tehlikeli / çok tehlikeli) —
  RD yenileme süresi, kurul sıklığı, destek elemanı ve ilk yardımcı sayısı, sağlık
  muayenesi periyodu, eğitim süreleri bununla değişir. Tahmin etme; sor.
- **Çalışan sayısı, vardiya düzeni, yükleniciler ve İSG hizmetinin kaynağı**
  (kendi İGU/İH mı, OSGB mi) — 5.4, 8.1.4 ve gece vardiyası düzenlemeleri buna bağlı.
- **Mevcut bir İSG doküman seti var mı?** Varsa klasörü iste (aşağıda §Mevcut set).
- **Kuruluşun kendi kodlama kuralı ve antet formatı var mı?** Varsa o kullanılır.

### 2 — Kapsamı ve planı onaylat

Üretime başlamadan tek ekranlık plan sun: kapsam beyanı cümlesi, tehlike sınıfı,
tam/sade set kararı, üretilecek doküman listesi (sayıyla), kodlama, risk yöntemi,
hangi talimatların (risk profiline göre) üretileceği, hangi dosyaların kodsuz
yol gösterici olacağı. Kullanıcının açık talebi olmadan toplu üretim yapma —
yanlış kapsam kırk dosyada düzeltilmez, burada bir satırda düzeltilir.

### 3 — Üret

Sırayı koru; sonraki doküman öncekine atıf verir:

1. **Kapsam + El Kitabı** (rol-sorumluluk tablosu ve rol adları burada sabitlenir)
2. **Bağlam ve ilgili taraflar** (4.1/4.2 — Amd 1 iklim kararı dahil)
3. **İSG Politikası**
4. **RD zinciri:** yöntem → Tehlike Belirleme ve RD Tablosu → Risk ve Fırsat Listesi →
   Hedefler ve Program. RD diğer her şeyin girdisidir: talimat listesi, KKD
   matrisi, eğitim matrisi, iş izni gerektiren işler, acil durum senaryoları
   RD'den türetilir.
5. **Yasal şartlar listesi**
6. **Prosedürler** — doküman kontrolünden başla; sonra eksik olma ihtimali en
   yüksek olanlar: 5.4 danışma-katılım, 8.1.3 değişiklik, 8.1.4 yükleniciler
7. **Acil Durum Planı, talimatlar, formlar, planlar**
8. **OKUBENI.md** — her zaman, en son
9. **Denetim hazırlık yol göstericileri** (kodsuz, K2): boşluk raporu, revizyon
   rehberi, kod geçiş tablosu (mevcut set varsa), madde-kanıt matrisi, öz değerlendirme

Word için `scripts/ys_docx.py` (`antet="klasik"` sahada yaygın 4 satırlı Türk
antetini verir; kuruluşun dokümanları böyleyse onu kullan). Talimat ve sahada
doldurulan formlar için `standart_belge(..., saha=True)`: kapak ve içindekiler
yok, klasik antet + altbilgide onay şeridi; talimat 1–2 sayfaya sığmalı, çünkü
makinenin yanına asılır. Excel için `scripts/ys_xlsx.py`. Tekrar eden Excel kayıtlarının tamamı tek komutla:

```bash
python3 scripts/kayitlar_45001.py --kurulus "..." --cikti "<04_Formlar_ve_Listeler>" \
  --tarih 2026-10-02 --hazirlayan "İş Güvenliği Uzmanı" --onaylayan "Genel Müdür" \
  --tehlike-sinifi "çok tehlikeli" [--yontem fine-kinney] [--sade] \
  [--kodlar '{"risk":"1000-11-FR-022"}']
```

Bu script risk seviyesini, KSO/KAO'yu, sonraki periyodik kontrol tarihini, 3 aylık
temel eğitim son tarihini ve yüklenici ağırlıklı puanını **formülle** kurar. Elle
yazılmış seviye sütunu ve `#VALUE!` hatası mevcut setlerde en sık görülen kayıt
kusurlarıdır; motoru atlayıp elle tablo kurma.

Hangi dokümanlar: `references/dokuman-listesi.md` · Madde bazlı gereklilik ve
6331 kesişimi: `references/madde-4-10.md` · Gövde içerikleri: `references/icerik-rehberi.md`

### 4 — Öz denetim yap ve raporla

`references/denetim-oz-kontrol.md` listesini (G bölümü İSGYS'ye özgü) geç;
`[DOLDURULACAK]` ve `[TEYİT]` etiketlerini say, rol adı ve sıklık tutarlılığını,
çapraz referansları, Türkçe büyük harf hatalarını tara. Sonuçları OKUBENI'de
"denetim öncesi kapatılması gerekenler" altında ver.

## Mevcut set varsa — önce analiz, sonra üretim

Türkiye'de 45001 işi çoğunlukla OHSAS 18001'den kalma bir setin yenilenmesidir.
`references/mevcut-set-analizi.md`'yi oku ve şu sırayla ilerle:

1. Klasör bağlıysa envanteri **kullanıcının bilgisayarında** çıkar
   (`device_bash` ile `scripts/envanter.py`) — yüzlerce dosyayı tek tek açma.
2. Çekirdek dokümanları oku (politika, prosedürler, RD, mevzuat listesi, acil durum planı).
3. Madde bazlı boşluk analizi + revizyon rehberi + kod geçiş tablosu üret.
4. Kullanıcıya anlat, karar al (korunacak / revize / birleştirilecek / iptal).
5. Sonra üret. Orijinal dosyalar asla silinmez ve üzerine yazılmaz; yeni sürümler
   ayrı alt klasöre (`İSGYS Yeni Set/` gibi) gider.

## Kırılma noktaları

Setin denetimde başarısız olmasına yol açan en yaygın hatalar:

**5.4'ü İSG Kurulu'na indirgemek.** Kurul bir kanaldır. Denetçi bir operatöre
"risk değerlendirmesine katıldın mı, kaza incelemesine çağrıldın mı?" diye sorar.
5.4 d/e'deki her konu için kanal + kayıt eşlemesi olmalı (PR-05, LS-11).

**Risk değerlendirmesinin yaşamaması.** Tarihi yasal yenileme süresini geçmiş,
kazadan sonra güncellenmemiş, yükleniciler ve rutin dışı işler yok, seviye elle
yazılmış, kontrol hiyerarşisi yok. `references/risk-degerlendirme.md` bunların
her birinin nasıl önleneceğini anlatır.

**8.1.3 ve 8.1.4'ün eksikliği.** "Yeni makine devreye alma" değişiklik yönetiminin
yalnız bir parçasıdır; "taşeron ceza şartnamesi" yüklenici yönetiminin yalnız
yaptırım ucudur.

**OHSAS mirası.** "Önleyici faaliyet", zorunlu "yönetim temsilcisi", "18001"
atıfları — 45001'de bunlar yok. Revize ederken temizle.

**Mevzuat hatası.** Mülga tüzükler, uydurulmuş Resmî Gazete künyeleri, güncel
olmayan eğitim kuralları (2 Nisan 2026 değişikliği). Künyeyi teyit edemiyorsan
`[TEYİT]` yaz — `references/mevzuat-kesisimi.md`.

**Rol ve sayı tutarsızlığı.** Aynı kişiye üç farklı unvan; bir dokümanda "ayda bir",
ötekinde "üç ayda bir" kurul. Rol adlarını ve tehlike sınıfına bağlı sayıları
El Kitabı'nda bir kez sabitle, her yerde aynısını kullan.

**Uydurulmuş kayıt ve kişisel veri.** Örnek risk/olay satırı üretebilirsin ama
"ÖRNEK —" ile işaretle. Kaza, sağlık, engelli listesi gibi kayıtlarda tanı veya
sağlık bilgisi isteme ve analiz çıktısına kişisel veri kopyalama (KVKK m.6).

**Ölçek uyumsuzluğu.** 30 kişilik az tehlikeli bir işletmeye 19 prosedür zarar
verir. Sade seti kullan — ama çok tehlikeli sınıfta RD, iş izni ve acil durum
sadeleştirilmez.

**Ölçülemez ifadeler.** "Gerektiğinde", "düzenli olarak", "dikkat edilir" —
her birini sayı, sıklık ve sorumluyla değiştir.

## Yaklaşan revizyon

ISO/DIS 45001 2026'da yayımlandı; 2027'de yeni sürüm ve 3 yıllık geçiş bekleniyor
(odak: psikososyal riskler, iyi oluş, hibrit çalışma, iklim ve dayanıklılık,
tedarik zinciri, güvenlik kültürü). Varsayılan hedef 2018+Amd 1:2024'tür.
Kullanıcı yeni sürümü isterse yayımlanıp yayımlanmadığını önce web'den teyit et.
Psikososyal ve iklim satırlarını RD'ye bugünden koymak geçişi kolaylaştırır;
bunları "zorunlu yeni şart" gibi sunma.

## Kullanıcı tek doküman istediğinde

"Bana sadece yüksekte çalışma talimatı lazım" gibi tekil isteklerde aynı kaliteyi
koru ama süreci kısalt: kuruluş adı, tehlike sınıfı, kodlama/antet ve varsa
mevcut örnek dokümanı sor; üret; sonunda ilgili maddeleri, ilgili RD satırını ve
kanıt beklentisini yaz. Setin gerisini dayatma, bir cümleyle teklif et.

## Entegre sistem

14001 (çevre) en sık birlikte kurulan standarttır; 9001, 22000, 50001 de olabilir.
Ortak dokümanlar (doküman kontrol, iç tetkik, YGG, DÖF, yetkinlik, iletişim,
bağlam, yasal şartlar listesi) `EYS-` önekiyle tek kez yazılır; politika ortaksa
taahhütler sistem bazında ayrı paragrafta durur. İki veya daha fazla standart
gündemdeyse `iso-entegre-yonetim-sistemi` skill'ini kullan; bu skill onun motoru olur.
Mevcut sette diğer sistemlerin sahiplerine ait ortak prosedürleri (ör. Kalite'nin
doküman kontrolü) tek taraflı birleştirme — karar maddesi olarak OKUBENI'ye yaz.

## Kurumsal şablonu birebir kullanma

Kullanıcı mevcut bir dokümanını "şablon olarak kullan" derse `scripts/sablon_analiz.py`
ile yazı tipi, renk, antet ve kod kalıbını çıkar; antet hücrelerini değiştir
(adı `tr_upper()` ile büyüt), gövde paragraflarını rPr dahil prototip olarak çoğalt.
Her dosyayı `soffice` ile PDF'e çevirip görsel kontrol et.

## Türkçe kuralları

`tr_upper()`/`tr_lower()` kullan, `.upper()` değil (İSG başlıklarında "GÜVENLIĞI",
"YÖNETIM" hatası çok görünür). İngilizce kısaltma yerine Türkçe terim: LOTO →
Kilitleme ve Etiketleme, PPE → KKD, near miss → ramak kala, SDS → Güvenlik Bilgi
Formu, ATEX → patlayıcı ortam; İngilizcesi yalnız Tanımlar tablosunda parantezde.

## Kullanılacak skill'ler ve araçlar

| Aşama | Araç | Ne için |
|---|---|---|
| Girdi | Cihaz köprüsü (`device_list_dir`, `device_bash`) | Bağlı klasörde envanter ve okuma yerinde; yalnız görsel kontrol gereken dosyayı buluta al |
| Mevzuat | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher`, `policy-diff` | Resmî Gazete künyeleri ve 2026 değişiklikleri |
| İş hukuku | `employment-legal:policy-drafting`, `internal-investigation` | Disiplin/ihlal yaptırımları, iş kazası sonrası soruşturma |
| Yüklenici | `commercial-legal:vendor-agreement-review` | Alt işveren sözleşmelerinde İSG maddeleri |
| Kişisel veri | `privacy-legal:*` | Sağlık verisi, kamera, kaza kayıtları |
| Çıktı | `anthropic-skills:docx`, `xlsx`, `pdf` | Üretim ve doğrulama |
| Entegrasyon | `iso-entegre-yonetim-sistemi` | 14001/9001 ile birlikte kurulum |
| Teslim | `device_commit_files` (bağlı klasörde yeni alt klasör) | Kullanıcının dosyalarını değiştirmeden teslim |

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/gorusme-rehberi.md` | Her çalışmanın başında |
| `references/dokuman-listesi.md` | Plan aşamasında — tam/sade set, kodlar |
| `references/dokuman-mimarisi.md` | Kodlama, klasör, ortak bölümler (aile ortak dosyası) |
| `references/madde-4-10.md` | Yönetim sistemi dokümanlarını yazarken; boşluk analizinde |
| `references/risk-degerlendirme.md` | RD prosedürü ve tablosunu kurarken |
| `references/mevzuat-kesisimi.md` | Yasal şartlar, sayısal kurallar, roller, 2026 değişiklikleri |
| `references/icerik-rehberi.md` | Her dokümanın gövdesini yazarken |
| `references/mevcut-set-analizi.md` | Mevcut İSG seti verildiğinde — üretimden önce |
| `references/denetim-oz-kontrol.md` | Üretim bitince — teslim öncesi |

## Bağımlılıklar

```bash
pip install python-docx openpyxl --break-system-packages
```
