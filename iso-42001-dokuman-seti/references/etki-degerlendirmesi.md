# YZ Risk Değerlendirmesi ile YZ Sistemi Etki Değerlendirmesi

Bu ayrım 42001'in kalbidir ve en sık yapılan hata bunları birleştirmektir.
Birleştirilmiş bir doküman her iki gerekliliği de karşılamaz.

> **Yardımcı standartlar.** İki zincirin de kendi rehber standardı vardır ve
> metodoloji dokümanında bunlara atıf vermek denetimde metodolojinin
> "uydurulmadığını" gösterir:
> **ISO/IEC 42005** — YZ sistemi etki değerlendirmesi rehberi (bu dosyanın konusu),
> **ISO/IEC 23894** — YZ risk yönetimi rehberi,
> **ISO/IEC 5259 serisi** — analitik ve makine öğrenmesi için veri kalitesi,
> **ISO/IEC 22989** — YZ kavram ve terminolojisi (rol taksonomisinin kaynağı),
> **ISO/IEC 38507** — YZ'nin kurumsal yönetişimi,
> **ISO/IEC TR 24027** — YZ'de yanlılık, **ISO/IEC TR 24028** — güvenilirlik,
> **ISO/IEC TR 24368** — etik ve toplumsal kaygılar.
> Bunlar belgelendirilebilir gereklilik değil, rehberdir; "uyumluyuz" denmez,
> "metodoloji şu rehber dikkate alınarak kurulmuştur" denir.

---

## 1. İki soru, iki değerlendirme

| | **YZ Risk Değerlendirmesi** (6.1.2, 6.1.3, 8.2, 8.3) | **YZ Sistemi Etki Değerlendirmesi** (6.1.4, 8.4, Ek A.5) |
|---|---|---|
| Sorduğu soru | "Bu YZ sistemi beklenmedik davranırsa **kuruluş** ne kaybeder?" | "Bu YZ sistemi **tasarlandığı gibi çalışırken bile** kime, nasıl zarar verebilir?" |
| Bakış açısı | İçeriden dışarı — kuruluşun hedeflerine etki | Dışarıdan içeri — kişilere, gruplara, topluma etki |
| Etkilenen | Kuruluş: itibar, finans, uyum, operasyon | Bireyler, kişi grupları, toplum, çevre |
| Tipik bulgu | "Model kayması nedeniyle tahmin doğruluğu düşer, müşteri kaybı olur" | "Model eğitim verisindeki temsil eksikliği nedeniyle belirli bir grup için sistematik olarak düşük skor üretir" |
| Çıktı | Risk envanteri, risk işleme planı, SoA | Etki değerlendirme raporu, azaltıcı önlemler, şeffaflık taahhütleri |
| Zamanlama | Planlı aralıklarla ve önemli değişiklikte (8.2) | Yaşam döngüsü boyunca; tasarım aşamasında başlar (8.4, A.5.2) |

**Kritik nokta:** Bir YZ sistemi kusursuz çalışıyor, hiçbir kuruluş riski
üretmiyor ama yine de kişilere zarar veriyor olabilir. Kredi skorlama modeli
%99 doğrulukla çalışırken belirli bir demografiye sistematik dezavantaj
üretebilir. Risk değerlendirmesi bunu göremez; etki değerlendirmesi görür.

---

## 2. YZ risk değerlendirmesi (6.1.2 / 6.1.3)

Yapı 27001'e benzer ama YZ'ye özgü risk kaynakları vardır. Standardın Ek C'si
potansiyel risk kaynaklarını listeler; başlıca kategoriler:

| Kategori | Örnek risk kaynakları |
|---|---|
| Model davranışı | Model kayması (drift), aşırı öğrenme, halüsinasyon, öngörülemezlik |
| Veri | Yetersiz kalite, temsil eksikliği, etiketleme hatası, veri zehirlenmesi |
| Güvenlik | Çekişmeli (adversarial) saldırı, model çalma, komut enjeksiyonu, veri sızıntısı |
| Şeffaflık | Açıklanamazlık, kara kutu kararlar, izlenebilirlik eksikliği |
| Bağımlılık | Üçüncü taraf model/API bağımlılığı, sağlayıcı değişikliği, sürüm kesintisi |
| Yönetişim | Rol belirsizliği, gözetim eksikliği, sorumluluk boşluğu |
| Uyum | Yasal düzenleme değişikliği, telif ihlali, kişisel veri ihlali |
| Kaynak | Hesaplama maliyeti, yetkinlik eksikliği, altyapı yetersizliği |

Risk envanteri sütunları: `Risk No | İlgili YZ Sistemi | Risk Kategorisi |
Risk Tanımı | Tetikleyici/Senaryo | Mevcut Kontroller | Olasılık | Etki |
Risk Skoru | Risk Sahibi | İşleme Seçeneği | Planlanan Kontroller (Ek A ref) |
Sorumlu | Termin | Artık Risk | Risk Sahibi Onayı | Durum`

---

## 3. YZ sistemi etki değerlendirmesi (6.1.4 / 8.4 / Ek A.5)

Bu, 42001'i diğer yönetim sistemi standartlarından ayıran çıktıdır. Her YZ
sistemi için ayrı yapılır ve yaşam döngüsü boyunca güncellenir.

### A.5.3 — dokümantasyonun içermek zorunda olduğu yedi kalem

Tetkik kontrol listeleri bu kalemleri tek tek sorar. Aşağıdaki tabloyu etki
değerlendirme şablonunun kapak kontrolü olarak kullan; **eksik kalem = bulgu.**

| # | Kalem | Nerede karşılanır | Sık atlanan yön |
|---|---|---|---|
| 1 | Amaçlanan kullanım ve **makul şekilde öngörülebilir amaç dışı kullanım** | Bölüm 1 | "Yasak" listesi yazılıyor ama "öngörülebilir amaç dışı" yazılmıyor — ikisi farklıdır |
| 2 | **Olumlu** ve olumsuz etkiler | Bölüm 3 | Olumlu etki neredeyse hiç yazılmaz; oysa standart ikisini de ister |
| 3 | **Öngörülebilir hatalar** ve bunları azaltacak faaliyetler | Bölüm 3b | Etki listesi var, hata modu listesi yok |
| 4 | Sistemin uygulanabildiği **ilgili demografik gruplar** | Bölüm 2 | "Herkes" yazılıyor; grup ayrıştırması yapılmıyor |
| 5 | **Sistemin karmaşıklığı** | Bölüm 1 | Hiç yazılmıyor — oysa açıklanabilirlik ve gözetim tasarımının gerekçesidir |
| 6 | İnsanların sistemle ilişkisindeki **rolü** | Bölüm 5 | Gözetim yazılıyor, rol/ilişki yazılmıyor |
| 7 | **İstihdam ve personel beceri kazanımı** üzerindeki etki | Bölüm 3c | Neredeyse her sette eksik |
| + | **Sonuçların tanımlı bir süre saklanması** | Kapak/meta | Saklama süresi belirtilmiyor |

**5. kalem — karmaşıklık.** "Bu sistem ne kadar karmaşık?" sorusunun cevabı
gözetim tasarımını belirler: çıktısı bir kural motorundan gelen sistemle,
milyarlarca parametreli bir dil modelinden gelen sistemin gözetimi aynı olamaz.
Karmaşıklığı bir cümleyle yaz ve bunun açıklanabilirlik üzerindeki sonucunu
belirt.

**7. kalem — istihdam etkisi.** Bir YZ sistemi bir işi tamamen ortadan
kaldırmasa bile o işin içeriğini değiştirir: rutin karar azalır, istisna
yönetimi artar, yeni yetkinlik gerekir. Bunu yazmak hem A.5.3'ü karşılar hem
7.2 yetkinlik zinciriyle bağlanır. Cevap "istihdam etkisi yoktur" ise bile
gerekçesi yazılmalıdır.

### Değerlendirme yapısı

**Bölüm 1 — Sistem tanımı**
- Sistem adı, sürüm, sağlayıcı, model tipi
- Amaçlanan kullanım · **öngörülebilir amaç dışı kullanım** · yasak kullanım (A.9.4)
- **Karar özerkliği düzeyi:** *destekleyici* (YZ önerir, insan karar verir) ·
  *tamamlayıcı* (paylaşımlı kontrol, insan onaylar) · *otonom* (korkuluklarla
  otomatik hareket eder)
- **Sistemin karmaşıklığı** ve bunun açıklanabilirliğe etkisi (A.5.3)
- Devreye alma bağlamı: hangi süreçte, hangi kararı etkiliyor

Özerklik düzeyinin üç kademeli yazılması gözetim tasarımının çıpasıdır: aynı
sistem "destekleyici" iken kabul edilebilir olan bir etki, "otonom"a geçtiğinde
kabul edilemez hâle gelebilir. Özerklik değişikliği bu nedenle yeniden
değerlendirme tetikleyicisidir.

**Bölüm 2 — Etkilenen taraflar**
- Doğrudan etkilenenler (sistemi kullananlar)
- Dolaylı etkilenenler (sistemin kararına maruz kalanlar — çoğu zaman asıl grup)
- **İlgili demografik gruplar** — sistemin uygulandığı nüfusun ayrıştırılması (A.5.3)
- Kırılgan gruplar (çocuklar, engelliler, dil azınlıkları, düşük dijital okuryazarlık)
- Toplumsal/çevresel etki alanı

Dolaylı etkilenenler en sık atlananlardır. İşe alım eleme modelinde kullanıcı
İK uzmanıdır ama **etkilenen** adaydır.

**Bölüm 3 — Etki analizi**

**3a — Kişiler ve kişi grupları üzerindeki etkiler (A.5.4).** Kontrol listesi
sekiz alanı sayar; her biri ayrı satır olmalı:

| Etki alanı | Sorulacak soru |
|---|---|
| **Adillik** | Belirli gruplar sistematik olarak dezavantajlı çıkıyor mu? Hangi metrikle ölçüldü? |
| **Hesap verebilirlik** | Karar yanlış çıkarsa sorumlu kim? Kime başvurulur? |
| **Şeffaflık ve açıklanabilirlik** | Kişi bir YZ sistemiyle etkileştiğini biliyor mu? Karar gerekçesi açıklanabiliyor mu? |
| **Güvenlik ve mahremiyet** | Hangi kişisel veri işleniyor, minimizasyon uygulandı mı, veri sızıntısı riski ne? |
| **Emniyet ve sağlık** | Hatalı çıktı fiziksel veya sağlık zararına yol açabilir mi? |
| **Finansal sonuçlar** | Kişi maddi kayba uğrayabilir mi? Fiyatlandırma veya erişim etkileniyor mu? |
| **Erişilebilirlik** | Engelli, yaşlı, düşük okuryazarlıklı kullanıcı sistemi eşit kullanabiliyor mu? İtiraz kanalı erişilebilir mi? |
| **İnsan hakları** | Ayrımcılık yasağı, ifade özgürlüğü, özel hayatın gizliliği, adil yargılanma gibi haklara dokunuyor mu? |

Son iki satır neredeyse her sette eksiktir ve tetkik kontrol listelerinde
açıkça sayılır. **Erişilebilirlik**, itiraz kanalının kendisini de kapsar:
yalnızca web formuyla itiraz kabul eden bir sistem, dijital erişimi olmayan
etkilenen için itiraz hakkını fiilen ortadan kaldırır.

**3b — Öngörülebilir hatalar (A.5.3).** Etki listesinden ayrı bir tablodur.
"Ne olursa yanlış olur?" sorusuna cevap verir:

| Hata modu | Nasıl ortaya çıkar | Kime zarar verir | Tespit yolu | Azaltıcı önlem |
|---|---|---|---|---|

Tipik YZ hata modları: model kayması, dağılım dışı girdi, halüsinasyon,
bağlam penceresi taşması, veri sızıntısı, komut enjeksiyonu, sessiz sürüm
değişikliği, geri bildirim döngüsüyle yanlılığın pekişmesi.

**3c — İstihdam ve beceri etkisi (A.5.3).** İşin içeriği nasıl değişiyor, hangi
yeni yetkinlik gerekiyor, gözetim yapacak kişinin iş yükü ne oluyor. Cevap
"etkisi yok" ise gerekçesi yazılır.

**3d — Olumlu etkiler (A.5.3).** Standart olumlu etkilerin de dokümante
edilmesini ister. Bu bir pazarlama bölümü değildir: olumlu etkiyi yazmak,
kabul edilen kalan etkinin **karşılığında ne elde edildiğini** gösterir ve
kabul kararını gerekçelendirir. Ölçülebilir yaz (erişimin genişlemesi, bekleme
süresinin düşmesi, insan hatasının azalması) ve ölçüm yoksa `[DOLDURULACAK]`
bırak — uydurma.

**3e — Toplumsal etkiler (A.5.5).** Dört alan ayrı ayrı değerlendirilir:

| Alan | Kapsam |
|---|---|
| **Çevresel sürdürülebilirlik** | Doğal kaynak kullanımı, enerji, sera gazı emisyonu — eğitim *ve* çıkarım ayrı (4.1 iklim değerlendirmesi ve A.4.5 ile bağlanır) |
| **Ekonomi** | Finansal hizmetlere erişim, vergi, istihdam olanakları, ticaret ve rekabet |
| **Yönetişim** | Yasama süreci, siyasi kazanç amaçlı yanlış bilgi, ulusal güvenlik, ceza adaleti sistemleri |
| **Sağlık ve emniyet** | Toplum ölçeğinde sağlık ve emniyet sonuçları |

Çoğu kuruluş için "yönetişim" alanı uygulanabilir değildir — sorun değil, ama
**"uygulanabilir değil" de yazılmalıdır.** Boş bırakılan alan, değerlendirilmemiş
alandır.

**Bölüm 4 — Etki değerlendirmesi ve azaltıcı önlemler**

Her tespit edilen etki için: şiddet · olasılık · etkilenen kitle büyüklüğü ·
tersine çevrilebilirlik · azaltıcı önlem · kalan etki · kabul kararı ve onaylayan.

**Tersine çevrilebilirlik** sütunu önemlidir: geri alınamayan bir zarar (yanlış
tıbbi tanı, haksız iş reddi) düşük olasılıkta bile yüksek öncelikli olabilir.

**Bölüm 5 — İnsan gözetimi ve insanın sistemle ilişkisi**
- **İnsanın rolü** (A.5.3): sistem insanın yerine mi geçiyor, kararını mı
  hazırlıyor, iş akışını mı değiştiriyor? Gözetimden önce bu ilişki tanımlanmalı
- Kim gözetiyor, hangi yetkiyle
- Hangi eşikte insana devrediliyor
- Gözetenin karara müdahale için ihtiyaç duyduğu bilgi ve süre
- Sistemi devre dışı bırakma (kill switch) yetkisi ve prosedürü

"İnsan kontrolünde" ifadesi yeterli değildir. Gözetim yapan kişi sistemin
çıktısını sorgulayacak bilgiye ve zamana sahip değilse gözetim biçimseldir —
denetçi bunu sorar.

**Bölüm 6 — Şeffaflık ve iletişim taahhütleri**
- Etkilenen kişilere ne söylenecek, nasıl, ne zaman
- İtiraz ve geri bildirim kanalı
- Olumsuz etki bildirim mekanizması (A.8.3)

**Bölüm 7 — İzleme ve yeniden değerlendirme**
- Hangi metrikler izlenecek (performans + adillik metrikleri ayrı)
- İzleme sıklığı ve sorumlusu
- Yeniden değerlendirme tetikleyicileri: model güncellemesi, veri değişikliği,
  yeni kullanım alanı, olay, mevzuat değişikliği, planlı periyot

**Bölüm 8 — Sonuç ve onay**
- Genel değerlendirme, kalan etkilerin kabulü, onaylayan ve tarih
- **Saklama süresi** — bu kaydın ne kadar süre saklanacağı (A.5.3 tanımlı bir
  süre ister; "süresiz" veya boş kabul edilmez)
- Sonraki gözden geçirme tarihi

---

## 4. Ne zaman etki değerlendirmesi yapılır

- Yeni YZ sistemi tasarım aşamasında (devreye almadan önce — sonra yapmak geç)
- Amaçlanan kullanım değiştiğinde
- **Karar özerkliği düzeyi değiştiğinde** (destekleyici → tamamlayıcı → otonom)
- Model önemli ölçüde güncellendiğinde veya yeniden eğitildiğinde
- **Üçüncü taraf sağlayıcı modeli sürüm yükselttiğinde** — kuruluş bunu kendisi
  yapmasa da etki değişebilir; sözleşmede bildirim yükümlülüğü yoksa bu
  tetikleyici çalışmaz, o hâlde bu bir risktir (bkz. `mevzuat-kesisimi.md` §5)
- Yeni bir veri kaynağı eklendiğinde
- Yeni bir kullanıcı grubu veya coğrafya eklendiğinde
- Olumsuz etki bildirimi veya endişe bildirimi (A.3.3) geldiğinde
- İzlemede adillik veya performans eşiği aşıldığında
- Mevzuat değiştiğinde
- Planlı periyotta (tipik: yılda bir)

Bu tetikleyicileri prosedürde yaz; "gerektiğinde" ifadesi bulgu üretir.
Her tetikleyicinin **kim tarafından fark edileceği** de yazılmalı — fark edeni
olmayan tetikleyici çalışmaz.

---

## 5. Adillik metriği seçimi

Kullanıcı adillik ölçümü isterse bilinmesi gereken: **tek bir "adil" metrik
yoktur** ve bazı adillik tanımları matematiksel olarak aynı anda sağlanamaz.
Yaygın metrikler:

| Metrik | Ne ölçer |
|---|---|
| Demografik parite | Gruplar arası olumlu sonuç oranının eşitliği |
| Eşit fırsat | Gerçekten uygun olanlar arasında olumlu sonuç oranının eşitliği |
| Eşitlenmiş olasılıklar | Hem doğru hem yanlış pozitif oranlarının eşitliği |
| Kalibrasyon | Tahmin edilen olasılığın gruplar arasında aynı anlamı taşıması |

Doküman, hangi metriğin **neden** seçildiğini ve hangi ödünleşimin kabul
edildiğini yazmalı. Metrik seçimi teknik değil değer yargısı içeren bir karardır;
bunu gizlemek yerine gerekçelendirmek denetimde çok daha güçlüdür.

Sayısal sonuçları **uydurma.** Metodolojiyi ve boş tabloyu üret; ölçümü kuruluş
yapar. Sahte adillik metriği hem denetimi hem etkilenen kişileri yanıltır.

---

## 6. Çift zincir kontrolü

Üretim bitince şunu doğrula: **envanterdeki her YZ sisteminin hem bir risk kaydı
hem bir etki değerlendirmesi var mı?** Eksik olan varsa `OKUBENI.md`'de raporla.

```
YZ Sistem Envanteri
   ├─ (zincir 1) → Risk kaydı → İşleme kararı → SoA kontrolü → Uygulama kanıtı
   └─ (zincir 2) → Etki değerlendirmesi → Azaltıcı önlem → İzleme metriği → Şeffaflık taahhüdü
```

Denetçi envanterden bir sistem seçip iki zinciri de takip eder.
