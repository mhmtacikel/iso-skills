# Görüşme Rehberi — Ne Zaman Sor, Ne Zaman Varsay

## İçindekiler

- 1. Açılış anketi (her zaman, üretimden önce)
- 1b. Sistem bazlı derin anket (yalnızca kapsamdaki YZ sistemleri için)
  - Veri tarafı
  - Kullanım tarafı
- 2. Doküman iste — hangi durumda, nasıl
- 3. Karmaşık durumlar — soru sormadan ilerleme
  - Kapsam belirsizliği
  - Hariç tutma talebi
  - Entegre sistem sinyali
  - Ölçek uyumsuzluğu
  - Gerçek veri talebi
  - Sektörel zorunluluk
- 4. Soru sorma — ne zaman sorMA
- 5. Üretim öncesi teyit

Bu skill'in en kolay hata yapacağı yer burası. İki uçtan da kaçınmak gerekiyor:

- **Az sorup çok varsaymak:** jenerik, kuruluşa benzemeyen, denetçinin ilk
  bakışta "internetten indirmiş" diyeceği bir set çıkar.
- **Çok sorup hiç üretmemek:** kullanıcı 30 soruluk anketle karşılaşır, sıkılır,
  yarıda bırakır. Kimse form doldurmak için gelmedi.

Doğru denge: **açılış anketi kısa, derinleşme talep üzerine ve yerinde.**

---

## 1. Açılış anketi (her zaman, üretimden önce)

Bu altı soruyu **tek turda** sor. `AskUserQuestion` varsa onu kullan — çoktan
seçmeli seçenekler kullanıcının yazma yükünü kaldırır. Cevaplar zaten
konuşmadaysa tekrar sorma, teyit et ve geç.

| # | Soru | Neden bu soru | Cevap yoksa varsayım |
|---|---|---|---|
| 1 | Kuruluşun tam ticari unvanı ve faaliyet alanı? | Kapak, antet ve her dokümanın kapsamı buna bağlı | Sorulmadan üretilmemeli — **zorunlu** |
| 2 | Yönetim sisteminin kapsamı: hangi lokasyon, hangi birim, hangi hizmet/ürün? | Kapsam beyanı denetimin çıpasıdır; yanlışsa her doküman yanlış | **Zorunlu** |
| 3 | Toplam çalışan sayısı ve kapsam içindeki çalışan sayısı | Doküman derinliğini ve kontrol ölçeğini belirler | 50 kişi altı = sadeleştirilmiş set |
| 4 | Dış kaynak kullanılan süreçler var mı? (bulut, veri merkezi, çağrı merkezi, yazılım geliştirme) | Tedarikçi kontrolleri ve kapsam sınırı buna bağlı | Bulut kullanımı varsayılır, `[DOLDURULACAK]` bırakılır |
| 5 | Halihazırda hangi dokümanlar var? (varsa yükleyin) | Var olanı yeniden yazmak kullanıcıyı kızdırır | Sıfırdan kurulum varsayılır |
| 6 | Hedef: ilk belgelendirme mi, gözetim/yeniden belgelendirme mi, yoksa boşluk kapatma mı? | Üretim kapsamını tamamen değiştirir | İlk belgelendirme |

Standarda özgü 1–2 ek soru her skill'in kendi `SKILL.md`'sinde tanımlı.

---

## 1b. Sistem bazlı derin anket (yalnızca kapsamdaki YZ sistemleri için)

Açılış anketi kuruluşu tanır; bu anket **her YZ sistemini** tanır. Envanter,
risk kaydı ve etki değerlendirmesinin üçü de bu cevaplardan doğar. Sistem
sayısı azsa hepsini, çoksa önce kritik olanları geç.

**Soruyu açık uçlu sorma — seçenekleri ver.** "Hangi tip veri kullanıyorsunuz?"
sorusu boş bakışla karşılanır; aşağıdaki seçenekli hâli hızla ilerler.

### Veri tarafı

| Soru | Seçenekler |
|---|---|
| Ne tür veri kullanılıyor? | Kişisel veri (ad, sağlık, finansal) · özel nitelikli veri · kişisel olmayan veri (sensör, makine logu, açık veri seti) · sentetik veri |
| Verinin tipi ne? | Sayısal · metin · kategorik · görüntü · ses · video · zaman serisi |
| Verinin yapısı ne? | Yapılandırılmış / yapılandırılmamış · dosya formatı · şema ve sürüm |
| Veri nereden geliyor? | Kurum içi sistemler (CRM, ERP, sensör, işlem kayıtları) · dış sağlayıcı veri setleri · açık veri kaynakları · kullanıcı üretimi içerik |
| Nasıl değerlendiriliyor? | Kalite kontrolleri (tamlık, doğruluk, güncellik) · yanlılık tespiti (hangi gruplar eksik temsil ediliyor) · amaca uygunluk |
| Nasıl saklanıyor ve korunuyor? | Bulut / yerinde · şifreleme, anonimleştirme, takma adlaştırma · erişim kontrolü · saklama süresi |
| YZ sisteminde nasıl kullanılıyor? | Eğitim verisi / işletim (gerçek zamanlı) verisi · durağan veri seti / sürekli akış · tek sisteme özel / çok sistemde paylaşılan |

Bu yedi soru A.4.3, A.7.2–A.7.6 kontrollerinin tamamının girdisidir ve
YZYS-LS-03 Veri Kaynakları ve Köken Envanteri'ni doğrudan doldurur.

### Kullanım tarafı

| Soru | Seçenekler |
|---|---|
| Amaçlanan kullanım ne? | Tek cümleyle, somut: "müşteri taleplerine İngilizce e-posta taslağı hazırlamak" — "verimliliği artırmak" değil |
| Teknik yaklaşım ne? | Makine öğrenmesi · derin öğrenme · doğal dil işleme · bilgisayarlı görü · pekiştirmeli öğrenme · üretken YZ (büyük dil modeli, görüntü) · kural/uzman sistemi |
| Hangi alana hizmet ediyor? | Müşteri desteği · İK ve işe alım · kredi/risk · sağlık triyajı · lojistik ve navigasyon · dolandırıcılık/güvenlik · perakende ve kişiselleştirme · üretim kalite kontrol · kamu ve sosyal hizmetler · eğitim |
| Karar özerkliği düzeyi ne? | **Destekleyici** (YZ önerir, insan karar verir) · **tamamlayıcı** (paylaşımlı kontrol, insan onaylar) · **otonom** (korkuluklarla otomatik hareket eder) |
| Kişiler hakkında karar veriyor mu? | Evet, doğrudan · evet, dolaylı olarak etkiliyor · hayır |
| AB bağlantısı var mı? | AB'de sunuluyor · AB'deki kişileri etkileyen çıktı üretiyor · hayır |

Son iki soru iki ayrı zinciri açar: kişi etkisi etki değerlendirmesinin
ağırlığını, AB bağlantısı yasal uyum matrisini (YZYS-LS-10) tetikler.

**Cevaplanamayan soru = boşluk, varsayım değil.** "Veri nereden geliyor?"
sorusuna cevap alınamıyorsa `[DOLDURULACAK]` bırak ve bunu `OKUBENI.md`'de
yüksek öncelikli olarak listele — çünkü A.7.5 veri kökeni bu cevap olmadan
karşılanamaz.

---

## 2. Doküman iste — hangi durumda, nasıl

Kullanıcı dosya yüklemeye açık ama ne yükleyeceğini bilmiyor olabilir. Şu
durumlarda **somut dosya adı vererek** iste; "ilgili dokümanları paylaşır
mısınız" gibi belirsiz istek işe yaramaz.

| Durum | İstenecek | Alınamazsa ne yap |
|---|---|---|
| Kurumsal şablon var dendi | `.docx` veya `.dotx` şablon + logo (`.png`) | Varsayılan kurumsal kimlikle üret, sonradan şablona geçilebileceğini söyle |
| Mevcut YS dokümanları var | Doküman listesi (Excel) veya klasörün kendisi | Sıfırdan üret, çakışma riskini not et |
| Organizasyon yapısı gerekiyor | Organizasyon şeması, görev tanımları | Rol tablosunu jenerik unvanlarla kur, `[DOLDURULACAK]` bırak |
| Risk değerlendirmesi yapılmış | Mevcut risk envanteri | Örnek riskleri sektöre göre üret, "doğrulanmalı" etiketle |
| Varlık/hizmet envanteri gerekiyor | Varlık listesi, hizmet kataloğu, uygulama envanteri | Boş şablon + sektör tipik örnekleri |
| Yasal yükümlülükler soruldu | Tabi olunan mevzuat listesi (KVKK, BDDK, EPDK, HHS vb.) | Sektörden çıkarım yap, teyit iste |
| Önceki denetim yapılmış | Tetkik raporu, uygunsuzluk listesi | Boşluk analizini standart maddeleri üzerinden yap |

İsterken **niçin** istediğini söyle. "Kapsam dokümanındaki birim adlarının
gerçek organizasyonla eşleşmesi için organizasyon şemanız gerekiyor" cümlesi,
kuru bir dosya talebinden çok daha yüksek yanıt alır.

---

## 3. Karmaşık durumlar — soru sormadan ilerleme

Bazı kararlar teknik değil **stratejik**tir; yanlış varsayım tüm seti bozar.
Bunlarla karşılaşınca dur ve sor. İşaretler:

### Kapsam belirsizliği
Kullanıcı "tüm şirket" dedi ama şirketin 4 lokasyonu, 3 iştiraki var.
→ Sor: hangi tüzel kişilik, hangi lokasyonlar, iştirakler dahil mi?
Belgelendirme sertifikasında yazacak metin budur; sonradan değiştirmek pahalıdır.

### Hariç tutma talebi
Kullanıcı bir maddeyi/kontrolü kapsam dışı bırakmak istiyor.
→ ISO/IEC 42001 Madde 4–10 **hariç tutulamaz** (standardın kendi ifadesi). Ek A
kontrolleri gerekçeyle hariç tutulabilir. Bunu net söyle; yanlış bilgiyle
üretilen SoA denetimde majör uygunsuzluk olur.

### Entegre sistem sinyali
Kullanıcı ikinci bir standarttan bahsediyor veya mevcut ISO 9001 sistemi var.
→ Sor: ortak dokümanları (doküman kontrol, iç tetkik, YGG, düzeltici faaliyet)
birleştirelim mi, ayrı mı? Birleştirmek doğru cevaptır ama kullanıcının mevcut
sistemini ezmemek gerekir.

### Ölçek uyumsuzluğu
12 kişilik şirkete 45 dokümanlık set üretmek zarar verir — kimse okuyamaz,
uygulayamaz, denetimde "yaşamayan sistem" bulgusu gelir.
→ Sor: sadeleştirilmiş set mi (birleştirilmiş prosedürler), tam set mi?

### Gerçek veri talebi
Kullanıcı risk envanterini, varlık listesini "sen doldur" diyor.
→ Örnek/aday veri üretebilirsin ama **kuruluşun doğrulaması şart**. Bunu
söyle ve üretilen satırları "ÖRNEK — doğrulanacak" diye işaretle. Uydurulmuş
kayıt denetimde sistemin güvenilirliğini yok eder.

### Sektörel zorunluluk
Finans, sağlık, kamu, telekom, kritik altyapı → ek mevzuat katmanı var.
→ Sor: tabi olduğunuz düzenleyici gereklilikler neler? (BDDK, KVKK, HHS,
BTK, EPDK, NIS2, DORA...) Bunlar yasal uyum matrisine girer.

**Soru sorma biçimi:** tek seferde en fazla 2–3 soru, her birinde önerilen
cevabı da ver. "Şunu mu, bunu mu?" formatı, açık uçlu sorudan çok daha hızlı
ilerletir. Karar kullanıcınındır ama tavsiyeni söyle.

---

## 4. Soru sorma — ne zaman sorMA

Bunları sorma, varsay ve `[DOLDURULACAK]` bırak. Sormak zaman kaybı:

- Doküman kodu numaralandırması (kural verildiyse otomatik ilerlet)
- Revizyon numarası (ilk yayın = 00)
- Sayfa kenar boşlukları, yazı tipi puntosu (şablon veya varsayılan)
- Standart madde başlıkları (standartta sabit)
- Prosedürlerin genel akış yapısı (sektörden bağımsız)
- Saklama süreleri (mevzuat/genel teamül; sonradan ayarlanır)
- Kişi isimleri (unvan yaz, isim `[DOLDURULACAK]`)

---

## 5. Üretim öncesi teyit

Anket cevapları geldikten sonra, üretime başlamadan **tek ekranlık bir plan**
sun ve onay al:

```
Üretilecek set — [Kuruluş] / [Standart]
Kapsam beyanı  : "..."
Doküman sayısı : X Word + Y Excel
Kodlama        : BGYS-XX-NN
Şablon         : kurumsal şablon / varsayılan kimlik
Doldurulacak   : ~N alan (org şeması ve varlık envanteri gelince kapanır)
```

Bu adım pahalı bir yanlış anlamayı ucuza yakalar. Kullanıcı "kapsamı şöyle
yazalım" derse 40 dosya yerine bir satır düzeltirsin.
