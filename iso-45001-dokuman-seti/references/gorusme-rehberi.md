# Görüşme Rehberi — Ne Zaman Sor, Ne Zaman Varsay

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
| 4 | Yükleniciler / alt işverenler ve dış kaynaklı İSG hizmeti var mı? (OSGB, bakım firmaları, temizlik, yemek, güvenlik, inşaat) | 8.1.4 ve 6331 m.23 koordinasyonu; yüklenici yoğunluğu risk profilini değiştirir | OSGB'den İSG hizmeti ve sürekli bakım yüklenicisi varsayılır, `[DOLDURULACAK]` bırakılır |
| 5 | Halihazırda hangi dokümanlar var? (varsa yükleyin) | Var olanı yeniden yazmak kullanıcıyı kızdırır | Sıfırdan kurulum varsayılır |
| 6 | Hedef: ilk belgelendirme mi, gözetim/yeniden belgelendirme mi, yoksa boşluk kapatma mı? | Üretim kapsamını tamamen değiştirir | İlk belgelendirme |

Standarda özgü 1–2 ek soru her skill'in kendi `SKILL.md`'sinde tanımlı.

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
| Yasal yükümlülükler soruldu | Mevcut mevzuat listesi, son müfettiş/itfaiye raporları, periyodik kontrol raporları | `mevzuat-kesisimi.md` çekirdek listesinden başla, künyeleri teyit iste |
| Risk değerlendirmesi var | Son risk değerlendirmesi dosyası, kullanılan yöntem, ekip listesi | Yöntemi koru; tarih geçmişse yenileme ihtiyacını raporla |
| Kaza geçmişi | Son 3 yılın kaza/ramak kala kayıtları (isimsiz) | Sektör tipik tehlikelerinden başla, örnek etiketle |
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
→ ISO 45001 Madde 4–10 **hariç tutulamaz**; 45001'de Ek A kontrol listesi yoktur
(Ek A yalnız kullanım kılavuzudur). Kapsam lokasyon/faaliyet olarak daraltılabilir
ama kuruluşun kontrolündeki bir faaliyetin İSG riskini kapsam dışı bırakmak —
özellikle yüklenicilerin yaptığı işler — kabul görmez. Bunu net söyle.

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
Kullanıcı risk değerlendirmesini, makine/kimyasal envanterini "sen doldur" diyor.
→ Örnek/aday veri üretebilirsin ama **kuruluşun doğrulaması şart**. Bunu
söyle ve üretilen satırları "ÖRNEK — doğrulanacak" diye işaretle. Uydurulmuş
kayıt denetimde sistemin güvenilirliğini yok eder.

### Sektörel zorunluluk
Çok tehlikeli sınıf, BEKRA (büyük endüstriyel kaza) kapsamı, patlayıcı ortam
(toz/gaz), maden, yapı işleri, sağlık kuruluşu → ek mevzuat katmanı var.
→ Sor: NACE kodu ve tehlike sınıfı nedir? Patlayıcı ortam (ör. un, şeker, kakao
tozu, solvent) var mı? BEKRA bildirimine tabi misiniz? Bunlar yasal şartlar
listesine ve acil durum planına girer.

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
Kodlama        : İSGYS-XX-NN (veya kuruluşun kendi kuralı)
Tehlike sınıfı : ... (RD yenileme, kurul sıklığı, ekip sayıları buna göre)
Risk yöntemi   : 5×5 L-matris / Fine-Kinney / mevcut yöntem korunuyor
Şablon         : kurumsal şablon / varsayılan kimlik
Doldurulacak   : ~N alan (org şeması, makine listesi ve tahliye krokisi gelince kapanır)
```

Bu adım pahalı bir yanlış anlamayı ucuza yakalar. Kullanıcı "kapsamı şöyle
yazalım" derse 40 dosya yerine bir satır düzeltirsin.
