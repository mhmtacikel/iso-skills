---
name: iso-tetkik-raporu-ghostwriter
description: "ISO 27001:2022 / ISO 20000-1:2018 belgelendirme tetkiklerinde baş tetkikçinin asistanı olarak Aşama 1 / Aşama 2 tetkik raporunu (BT-YS-FR-02-09 / 02-10) ve entegre tetkik soru listesini (BT-YS-LS-02-02) baş tetkikçinin notlarından, onun kalemiyle yazar. Bulgu sınıflandırmasını ve sonucu tetkikçiye sorar; isim, delil, sayı uydurmaz. Kullanıcı \"tetkik raporunu doldur\", \"Aşama 1/2 raporu yaz\", \"soru listesini doldur\", \"tetkik notlarımı rapora dök\", \"uygunsuzluk yaz\", \"OFI yaz\" dediğinde ya da bir denetim klasöründe tetkik raporu/soru listesi şablonu üzerinde çalışılacağında kullan."
metadata:
  surum: "2.0.0"
---

# ISO Tetkik Raporu — Baş Tetkikçi Asistanı

Baş tetkikçinin yaptığı tetkiki, onun notlarından ve denetim klasöründeki
evraktan, onun kalemiyle rapora ve soru listesine döker. Sonucu (uygunsuzluk
var/yok, sınıfı, belgelendirme önerisi) **baş tetkikçi belirler**; bu skill
yazar, karar vermez.

Rapor bir belgelendirme kaydıdır: akreditasyon kurumu, belgelendirme kuruluşu
ve müşterinin müşterileri ona güvenir. Bu yüzden içindeki her cümle üç
kaynaktan birine dayanır: **(a) baş tetkikçinin notu/sözü, (b) denetim
klasöründeki evrak, (c) tetkikçinin onayladığı taslak.** Dördüncü kaynak yoktur.

## Akış

### 0 — Bağlamı topla

Denetim klasörünü tara. Tipik yapı:

- `BAŞVURU EVRAKLARI/` → Başvuru Formu, Teklif, Sözleşme, Gizlilik Sözleşmesi (PDF)
- `1.AŞAMA/` → Tetkik Plan Formu, Tetkikçi Görevlendirme, Tetkik Toplantı Formu (PDF) + **Tetkik Raporu Aşama 1 (DOCX)** + **Entegre Tetkik Soru Listesi (DOCX)**
- `2.AŞAMA/` → aynı set + **Tetkik Raporu Aşama 2 (DOCX)** + Tetkikçi Değerlendirme / Sertifika Düzenleme Bilgi Formu

PDF'lerden çıkar: unvan, başvuru no, adres, firma temsilcisi, kapsam metni,
sektör kodları, personel sayısı, tetkik tarihleri, tetkik süresi (a/g), baş
tetkikçi ve ekip, **plan formundaki gün/saat dağılımı ve her oturumun standart
maddeleri**, toplantı formundaki katılımcılar. Firmanın klasörde bulunan
dokümanlarının adlarını da listele (doküman gözden geçirme delili buradan gelir).

Sonra **tetkikçinin notlarını** al: sohbetteki metin, yüklenen not dosyası,
ses kaydı dökümü, el notu fotoğrafı. Not yoksa iste — notsuz Aşama 2 raporu
yazılmaz.

### 1 — Notları sınıflandır ve tek seferde sor

Her notu şu dört gruba ayır:

| Grup | Örnek not | Ne yapılır |
|---|---|---|
| Uygunluk delili | "risk envanteri incelendi, metodolojiye uygun" | Delil cümlesine çevrilir |
| **Olası uygunsuzluk** | "yedekleme testi 8 aydır yok, prosedür 3 ay diyor" | Taslak bulgu yazılır, **sınıf tetkikçiye sorulur** |
| İyileştirme fırsatı | "hedef takibi Excel'de dağınık" | OFI cümlesine çevrilir |
| Eksik bilgi | "görüşülenleri plana yazmadım" | Tetkikçiye sorulur |

Bir notun uygunsuzluk mu OFI mı olduğuna **sen karar verme**. Şart ile kanıt
arasında açık bir sapma görüyorsan (prosedür X diyor, kayıt X'i göstermiyor;
SoA'da uygulanabilir kontrol için kayıt yok) bunu olası uygunsuzluk olarak
işaretle ve sor.

Tüm soruları **tek mesajda**, numaralı ve kısa sor (`AskUserQuestion` varsa
onunla; seçenekli sorular tetkikçinin yükünü azaltır). Her olası uygunsuzluk
için taslak bulgu metnini de soruya koy ki tetkikçi yalnız onaylasın veya
düzeltsin:

> **2. Yedekleme testi** — Taslak: "A.8.13 / Yedekleme Prosedürü: geri yükleme
> testlerinin üç ayda bir yapılacağı tanımlanmış; son sekiz aylık dönemde test
> yapıldığına dair kayıt görülmemiştir." Sınıf? ☐ Majör ☐ Minör ☐ OFI'ye çevir ☐ Bulgu değil

Acele, "hemen bitir", "sen karar ver" gibi baskılar soruyu atlamanın gerekçesi
değildir — bulgu sınıfı tetkikçinin imzasıdır. Soruları en kısa hâliyle sor,
cevap gelmeden sonuç bölümünü doldurma; geri kalan alanları doldurmaya devam et.

- **Önceden verilmiş toptan karar** ("uygunsuzluk yok diye yaz") notlardaki
  somut sapmaları sınıflandırmış sayılmaz. Sapmaları taslak metinleriyle göster
  ve tek satırlık hızlı yol ver: "İkisi de bulgu değilse 'bulgu değil' yazmanız
  yeterli, sonucu hemen kapatırım." Tetkikçi bunu teyit ederse kararı uygula.
- **Kontrol varlığına bağlı sapma** (ör. "5.7 için kayıt yok"): sapma ancak
  kontrol SoA'da uygulanabilirse uygunsuzluktur. SoA klasördeyse bak; yoksa
  soruyu iki adımlı sor (uygulanabilir mi? → sınıf).
- **Notu olmayan çok sayıda kontrol:** tek tek sorma; temaya göre grupla
  (5 / 6 / 7 / 8), 2022'de eklenen 11 kontrolü ayrı satırda öne al ve
  "not ekleyin / SoA'ya göre hariç / plan dışı" seçeneğini grup başına sor.
- Notta yalnız "incelendi" yazıyorsa delil cümlesi de yalnız "incelenmiştir"
  der; "uygun", "güncel" gibi nitelemeler ancak notta ya da tetkikçinin
  cevabında varsa eklenir.

### 2 — Doldur

Teknik yöntem için Bölüm 5'i, soru listesi için Bölüm 6'yı, rapor için Bölüm
7'yi uygula.

### 3 — Doğrula ve teslim et

Bölüm 9'daki listeyi **betikle** geç. Teslimde tetkikçiye üç liste ver:
(1) hangi alanlar notlardan, hangileri klasör evrakından dolduruldu;
(2) tetkikçinin onayına taslak olarak bırakılan cümleler; (3) boş kalan alanlar
ve nedeni. Bağlı klasör varsa dosyaları oraya yaz (Cowork'te
`mcp__cowork__present_files` ile sun; Claude Code'da dosya yollarını ver).

## Yazım kuralı — tetkikçinin kalemi (sıfır yapay zekâ izi)

Tetkikçi not tutar, rapor yazar; övgü yazmaz. Her alan şu kalıba uyar:

**Ne incelendi → nasıl (örnekleme / görüşme / gözlem / doküman) → ne görüldü.**

> "Değişiklik yönetimi prosedürü incelenmiş, dönem içinde açılan değişiklik
> kayıtlarından üçü örneklenmiştir. Kayıtlarda etki değerlendirmesi ve onay
> adımlarının tamamlandığı görülmüştür."

- Edilgen + geçmiş zaman: …incelenmiştir, …doğrulanmıştır, …görülmüştür, …örneklenmiştir.
- Alanlara 2–5 cümlelik düz paragraf; madde işareti yalnız şablon istiyorsa.
- Cümle uzunluğunu değiştir; arada kısa tespit cümlesi kullan ("Kayıtlar günceldir.").
- Ardışık iki delil satırı aynı fiil ve aynı kalıpla başlamaz; delil türleri
  arasında dolaş (politika, prosedür, form, log/ekran görüntüsü, tutanak,
  sözleşme, taahhütname, eğitim kaydı, yetki matrisi, test raporu, envanter,
  hizmet masası kaydı, SLA raporu).
- **Yasaklı kelime ve kalıplar:** "kapsamlı bir şekilde", "önemli ölçüde",
  "sağlam bir temel", "titizlikle", "detaylı bir analiz sonucunda", "genel
  olarak değerlendirildiğinde", "ayrıca belirtmek gerekir ki", "büyük önem",
  "etkin ve verimli", "başarıyla", "dikkat çekicidir", "son derece".
  Meta yorum, emoji, yapay zekâ referansı, "aşağıda belirtilmiştir" türü
  dolgu yok.
- OFI dili: "…iyileştirilebilir", "…güçlendirilmesi önerilir", "…faydalı olacaktır".
  Uygunsuzluğu OFI kılığına sokma; tetkikçi OFI dediyse OFI'dir.
- Uygunsuzluk dili üç parçalıdır: **şart** (madde/kontrol + kuruluşun kendi
  dokümanı) — **bulgu** (ne görülmedi/ne sapıyor) — **kanıt** (neye bakıldı).

## Uydurma yasağı

- Doküman **adıyla** anılır; doküman kodu, revizyon no, kayıt numarası
  (ticket/değişiklik/olay no) yalnız tetkikçinin notunda veya klasördeki
  evrakta geçiyorsa yazılır.
- Sayı, yüzde, adet yalnız nottan gelir. Notta yoksa niteliksel yaz
  ("dönem içinde açılan kayıtlar"). Örnekleme adedi tetkikçinin notundaysa
  yazılır ("üç kayıt örneklenmiştir").
- Tarih: gerçek tetkik tarihleri ve klasördeki evrakın tarihleri. Firma
  kayıtlarına ait tarih notta yoksa "dönem içinde", "planlanan periyotta".
- **Kişi adı ve unvanı** yalnız plan/toplantı formundan veya tetkikçiden gelir.
  Yoksa sor; tetkikçi vermezse satır boş kalır ve teslimde listelenir.
- Notlarda ve evrakta karşılığı olmayan bir kontrol için delil cümlesi
  yazma. Aşama 2'de kapsanmamış kontroller tetkikçiye liste olarak gösterilir:
  "Bu N kontrol için notunuz yok — notunuzu ekleyin ya da plan dışı olarak
  işaretleyeyim mi?"
- Klasördeki firma dokümanından türetilen delil (ör. "Erişim Kontrol Politikası
  incelenmiştir") doküman gözden geçirme delilidir; uygulama delili gibi
  ("kayıtlar örneklenmiştir") yazılmaz.
- Aynı doküman tüm dosyalarda aynı adla anılır; kronoloji tutarlı kalır
  (risk değerlendirme → iç tetkik → YGG).

## 4) Kapsam sınırı

Kapsam dışı standartlara ait tablolar, sütunlar ve rapor özet blokları **hiç
dokunulmadan boş bırakılır** — "kapsam dışı" notu bile yazılmaz, satır silinmez.
BÖLÜM 3 standart-özel özet bloklarından yalnız kapsamdakiler doldurulur
(ISO 27001 → BGYS özeti, ISO 20000-1 → HYS özeti); Kalite / Çevre / İSG /
Yapay Zekâ / İş Sürekliliği blokları boş kalır.

## 5) Teknik yöntem — şablona zarar verme

1. Önce `docx` skill'ini oku ve uygula; PDF okuma için `pdf` skill'i.
2. Düzenlemeden önce her dosyanın `_ORIJINAL` ekli yedeğini al.
3. **Önce keşif:** her DOCX'in tüm tablolarını, satır/sütun sayılarını ve mevcut
   hücre metinlerini dök. Sütun başlıklarını çalışma anında doğrula, varsayma.
4. Tablo/satır/sütun **eklenmez, silinmez, birleştirilmez**. Başlıklar, form
   kodları, üstbilgi/altbilgi, logo, sayfa yapısı değişmez.
5. **Biçim mirası:** doldurulan hücrelerdeki run biçimi aynı tablodaki orijinal
   bir gövde hücresinin `w:rPr`'sinden kopyalanır (kalın/italik/renk kaldırılır).
6. **Onay kutuları `w:sdt` içinde olabilir.** `paragraph.runs` bunları görmez;
   hücredeki tüm `w:t` elemanlarını tarayıp `☐` → `☒` yap. Yanına "X" yazma.
7. Alternatif cümle blokları: geçerli olan bırakılır, geçersizler paragraf olarak silinir.
8. Türkçe büyük harf: `"i".upper()` → `"I"`. `tr_upper()` kullan
   (`str(m).replace("i","İ").replace("ı","I").upper()`).
9. Dosya Word'de açıksa yazma "Permission denied" verir; kilitli dosyayı
   bildir ve kapatılmasını iste.

## 6) Soru listesi

### Tablo 1 (ana standart maddeleri)

Aşama 1 kopyasında **AŞ1**, Aşama 2 kopyasında **AŞ2** sütunu işaretlenir;
**G1/G2 gözetim içindir, boş kalır.** Plana girmeyen satırın delil hücresine:
"Aşama 1 tetkik planında yer almamıştır; Aşama 2'de değerlendirilecektir."

### Tablo 2 (ISO 27001 Ek A) — "2022 Şartlar" sütununa göre

Bu şablonun satır yapısı 2017 sürümüne göredir; **"2022 Şartlar" sütunu yalnız
dört blokta doludur:** "5. Organizasyonel kontroller" + alt satırda 5.1…5.37;
"6. İnsan kontrolleri" + 6.1…6.8; "7. Fiziksel kontroller" + 7.1…7.14;
"8. Teknolojik kontroller" + 8.1…8.34 (aynı hücrede).

- Delil yalnız bu satırlara yazılır; **2022 karşılığı "-" olan 2017 satırları boş kalır.**
- Tema başlığı satırına 2–3 cümlelik tema özeti (kaç kontrol, hariç tutulan
  var mı, delil türü).
- Alt satıra her kontrol için bir satır: `5.1 <kontrol adı> — <delil cümlesi>`.
  Kontrol adı şarttır: bazı şablonlarda 2022 numaralandırması bozuktur
  (5.23/5.24 ve 5.29/5.30 bölünmüş, 5.24 ve 5.37 atlanmış olabilir); eşleşme
  satır konumuna değil ada dayanır. Resmî numaralandırma kullanılır (93 kontrol);
  şablondaki hata taklit edilmez, tetkikçiye bildirilir.
- SoA'da hariç tutulan kontrol: "Uygulanabilirlik Bildirgesi'nde gerekçesiyle
  hariç tutulmuştur; gerekçe kapsamla tutarlıdır." (tutarlılığı notlar veya
  SoA gösteriyorsa).
- Aşama 1'de plan dışı kontrol: "Aşama 1 tetkik planında yer almamıştır;
  Aşama 2 tetkikinde değerlendirilecektir."
- Aşama 2'de 93 kontrolün her biri ya delillendirilir ya hariç tutma
  gerekçesine bağlanır ya da tetkikçiye "notu yok" listesiyle sorulur.
  2022'de eklenen 11 kontrol (5.7, 5.23, 5.30, 7.4, 8.9, 8.10, 8.11, 8.12, 8.16,
  8.23, 8.28) denetçilerin en çok sorduğu kontrollerdir; bunlarda not eksikse
  soruların başına koy.
- Bazı şablonlarda Tablo 2'de AŞ2 sütunu yoktur; Aşama 2 dosyasında mevcut aşama
  sütunu "tetkik edildi" işareti olarak kullanılır ve tercih tetkikçiye bildirilir.

### Ortak

- **Firma Bilgileri / Görüşülen Kişiler:** plan ve toplantı formlarındaki
  isim-unvanlar; yoksa tetkikçiden. Tüm dosyalarda aynı.
- **ISO 20000-1:2018 delil odakları:** hizmet kataloğu, SLA/OLA ve tedarikçi
  sözleşmeleri, hizmet sürekliliği ve kapasite planı, olay/istek/problem,
  değişiklik, sürüm/dağıtım, konfigürasyon, hizmet raporlama, iyileştirme kayıtları.

## 7) Rapor

### Aşama 1 — doküman gözden geçirme odaklı

BÖLÜM 3 alt başlıkları, her biri 3–6 cümle: başvuru bilgilerinin doğrulanması;
kapsam değerlendirmesi; sertifika-marka-logo bilgilendirmesi; sahaya özgü
şartlar; yasal ve düzenleyici şartlar (Türkiye için tipik: 6698 KVKK, 5651,
6563, 5846 FSEK, lisans yükümlülükleri — yalnız firmanın yasal şartlar
listesinde veya notta geçenler); yönetim sistemi uygunluğu; iç tetkik ve YGG;
tetkik ekibi gözlemleri; entegre uygulanma durumu; BGYS özeti; HYS özeti.

### Aşama 2 — uygulama ve etkinlik odaklı

Örneklenmiş kayıtlar, yerinde doğrulama, görüşmeler, sistem gözlemi anlatılır.
Ek alanlar: önceki tetkik sonuçlarının karşılaştırılması; planlama bilgilerinin
yerinde doğrulanması; "incelenemeyen hususlar"; kontrol soruları tablosu;
BÖLÜM 4'te belgelendirme önerisi ve Açıklamalar.

**Aşama 1 ↔ Aşama 2 tutarlılığı:** Aşama 2, Aşama 1'deki doküman adlarını ve
gözlemleri tanır; Aşama 1 OFI'larının durumu tetkikçinin notuna göre
(kapanmış / devam ediyor) yazılır.

### Sonuç bölümü — tetkikçinin kararına göre

| Tetkikçinin kararı | BÖLÜM 4 | Kontrol soruları |
|---|---|---|
| Uygunsuzluk yok | Uygunsuzluk tablosu boş (sıra no kalır); "Uygunsuzluk Tespit Edilmemiştir." ☒. Aşama 1: "Aşama 2 Denetimi planlanabilir." Aşama 2: "Yönetim sistemi, standart isteklerini karşılamaktadır, belgelendirilmesi önerilir." | Hedeflere ulaşıldı **Evet**; plan sapması / önemli değişiklik / görüş ayrılığı — notlara göre (yoksa **Hayır**) |
| Yalnız minör | Her uygunsuzluk tabloya: madde/kontrol — şart — bulgu — kanıt — **sınıf: Minör**. "Uygunsuzluk Tespit Edilmiştir." ☒. Öneri: "Düzeltici faaliyet planının belgelendirme kuruluşuna sunulması ve kabulü şartıyla belgelendirilmesi önerilir." | Notlara göre |
| En az bir majör | Tabloya **sınıf: Majör**. Öneri: "Düzeltici faaliyetlerin uygulandığının doğrulanmasının ardından belgelendirme kararı verilecektir." (Aşama 1'de: "Aşama 2 öncesi kapatılmalıdır.") | Notlara göre |

Kuruluşun kendi formu farklı cümle/kutu sunuyorsa formdaki ifade esastır;
yukarıdaki tablo yalnız hangi alternatifin seçileceğini gösterir. "Tetkik
Ekibi Gözlemleri"nde yalnız notlarda dayanağı olan olumlu tespitler ve
tetkikçinin OFI olarak onayladığı maddeler yer alır (tipik 2–4 OFI).

## 8) Ölçek gerçekçiliği

Firma personel sayısına uygun yaz. Küçük bir hizmet sağlayıcı için ayrı bilgi
güvenliği departmanı, 7/24 güvenlik operasyon merkezi, kalabalık değişiklik
kurulu yazılmaz; görev birleştirme ve dış kaynak bu ölçekte normaldir.

## 9) Son doğrulama (atlanmaz, betikle)

- [ ] Tablo/satır/sütun sayıları `_ORIJINAL` ile aynı
- [ ] Sonuç kutuları ve uygunsuzluk tablosu **tetkikçinin verdiği karar** ile birebir
- [ ] Her uygunsuzluğun şart–bulgu–kanıt–sınıf alanı dolu; sınıfı tetkikçi verdi
- [ ] Kapsam dışı tablolar/sütunlar/bloklar ve G1/G2 boş
- [ ] Tablo 2'de yalnız "2022 Şartlar" satırlarında delil; 2017 satırları boş
- [ ] Aşama 2'de 93 kontrolün her biri delil / hariç tutma / tetkikçiye soruldu durumunda
- [ ] Metindeki her sayı, kod, kayıt no, kişi adı nottan veya klasör evrakından
- [ ] Görüşülen kişiler tüm dosyalarda aynı
- [ ] Yasaklı kelime taraması sıfır; ardışık aynı kalıp yok
- [ ] `İ/I` doğru; edilgen geçmiş zaman tutarlı
- [ ] Bir sayfa LibreOffice ile PDF'e çevrilip görsel kontrol edildi
- [ ] Teslimde üç liste (kaynak, taslak, boş alan) verildi
