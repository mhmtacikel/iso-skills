# ISO/IEC 27001:2022 Madde 4–10 — Gereklilik / Doküman / Kanıt

Ek A kontrolleri "ne yapılacağını" söyler; Madde 4–10 **yönetim sisteminin
kendisini** kurar. Denetçinin Aşama 1 tetkikinde neredeyse tamamen bu maddelere
baktığını unutma — Ek A daha çok Aşama 2'nin konusudur.

**Bu maddelerin hiçbiri hariç tutulamaz.** Standart bunu açıkça söyler: uygunluk
iddiasında bulunan bir kuruluş Madde 4 ila 10'daki gerekliliklerden herhangi
birini hariç tutamaz.

`Z` işareti: standardın dokümante edilmiş bilgi olarak açıkça istediği çıktı.

---

## 4 — Kuruluşun bağlamı

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 4.1 | İç ve dış hususların belirlenmesi | BGYS-FR-01 Bağlam Analizi | "İç ve dış hususlarınız neler, nasıl belirlediniz, ne zaman güncellediniz?" |
| 4.2 | İlgili taraflar ve gereklilikleri; hangilerinin BGYS'de ele alınacağı | BGYS-LS-06 | "Müşterileriniz hangi güvenlik gerekliliklerini getiriyor? Hangileri BGYS kapsamında?" |
| 4.3 **Z** | Kapsam sınırları ve uygulanabilirlik; arayüz ve bağımlılıklar | BGYS-PL-00 Kapsam Dokümanı | "Kapsam dışı bıraktığınız birim var mı, neden? Dış kaynaklı süreçler nasıl kontrol ediliyor?" |
| 4.4 | BGYS'nin kurulması, prosesler ve etkileşimleri | BGYS-EK-01 El Kitabı | "Süreç haritanız var mı? Süreçler nasıl etkileşiyor?" |

**Yazarken:** 4.1'i SWOT'a indirgemek yaygın ama zayıf. İç hususlar (organizasyon
yapısı, yetkinlik, kültür, teknoloji borcu) ve dış hususlar (mevzuat, tehdit
ortamı, tedarikçi bağımlılığı, sektörel baskı) ayrı ayrı listelenmeli, her biri
BGYS'ye etkisiyle birlikte. 4.3 c) arayüz ve bağımlılıkları çoğu kuruluş atlar —
bulut sağlayıcı, grup şirketi BT'si, dış çağrı merkezi bu başlığa girer.

---

## 5 — Liderlik

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 5.1 | Üst yönetimin sekiz maddelik liderlik göstergesi | YGG tutanakları, taahhüt beyanı, bütçe kayıtları | Genel müdürle görüşür: "BGYS'den ne bekliyorsunuz? Son çeyrekte hangi kararı verdiniz?" |
| 5.2 **Z** | Politika: amaca uygun, hedef içeren/çerçeve veren, uyum ve sürekli iyileştirme taahhüdü; dokümante, duyurulmuş, erişilebilir | BGYS-PL-01 | "Politika çalışanlara nasıl duyuruldu? İlgili taraflar erişebiliyor mu?" |
| 5.3 | Rol, sorumluluk, yetki ataması ve duyurulması; uygunluk sağlama ve üst yönetime raporlama sorumlulukları | Görev tanımları, organizasyon şeması, atama yazıları | "BGYS performansını üst yönetime kim raporluyor? Ne sıklıkla?" |

**Yazarken:** 5.1 en çok "kâğıt üstünde kalan" maddedir. Politikaya üst yönetim
imzası koymak yetmez; YGG tutanağında alınmış somut karar, ayrılmış bütçe, atanmış
kaynak izleri gerekir. Politikanın duyurulma kanıtını (intranet ekran görüntüsü,
e-posta, oryantasyon içeriği) üretilecek kanıt listesine ekle.

---

## 6 — Planlama

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 6.1.1 | Risk ve fırsatların belirlenmesi, eylem planlanması, etkinliğin değerlendirilmesi | BGYS-PR-02 | "BGYS'nin amaçlanan çıktısına ulaşmasını engelleyecek riskler neler?" |
| 6.1.2 **Z** | Risk kriterleri (kabul + değerlendirme), tekrarlanabilirlik, tanımlama/analiz/değerlendirme; **süreç hakkında yazılı bilgi** | BGYS-PR-02 + BGYS-FR-03 | "Risk kabul kriteriniz nedir? Aynı riski iki kişi değerlendirse aynı sonucu alır mı?" |
| 6.1.3 **Z** | İşleme seçenekleri, kontrollerin belirlenmesi, **Ek A ile karşılaştırma**, **SoA**, risk işleme planı, **risk sahibi onayı ve artık risk kabulü** | BGYS-LS-02 SoA + BGYS-PN-01 | "SoA'daki şu kontrol neden gerekli? Hangi riskten geliyor? Artık riski kim kabul etti?" |
| 6.2 **Z** | Hedefler: politikayla tutarlı, ölçülebilir, izlenen, duyurulan, güncellenen; ne/kim/kaynak/ne zaman/nasıl değerlendirilecek | BGYS-FR-04 | "Bu yılki bilgi güvenliği hedefleriniz neler? Şu an neredesiniz?" |
| 6.3 | Değişikliklerin planlı yapılması | BGYS-PR-21 | "BGYS'de yaptığınız son değişikliği nasıl planladınız?" |

**Yazarken:** 6.1.3 c) "Ek A ile karşılaştırma ve hiçbir gerekli kontrolün
atlanmadığının doğrulanması" bir *faaliyet*tir, sadece SoA'nın varlığı değil.
Bu karşılaştırmanın yapıldığını gösteren bir kayıt (tarihli SoA gözden geçirme
notu) üret.

6.2 hedefleri en sık şu yüzden bulgu alır: hedef ölçülebilir değil ("farkındalığı
artırmak") ya da izleme kanıtı yok. Hedef tablosunu şu sütunlarla kur:
`Hedef | Gösterge | Başlangıç değeri | Hedef değer | Ölçüm sıklığı | Sorumlu |
Kaynak | Termin | Güncel durum | Değerlendirme`

---

## 7 — Destek

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 7.1 | Kaynakların belirlenmesi ve sağlanması | Bütçe, kadro, YGG kararları | "BGYS için ayrılan bütçe/personel nedir?" |
| 7.2 **Z** | Yetkinlik belirleme, sağlama, etkinliği değerlendirme; **yetkinlik kanıtı** | BGYS-LS-07 Yetkinlik Matrisi | "BGYS yöneticisinin yetkinliği neyle kanıtlanıyor?" |
| 7.3 | Politika, katkı, uygunsuzluğun sonuçları konusunda farkındalık | BGYS-PN-02 + eğitim kayıtları | Rastgele bir çalışana sorar: "Politikayı biliyor musunuz? Bir olayı kime bildirirsiniz?" |
| 7.4 | İletişim: ne, ne zaman, kime, nasıl | BGYS-PN-06 İletişim Planı | "Bir ihlal olayında dış paydaşlarla kim, nasıl iletişim kurar?" |
| 7.5.1 **Z** | Standardın istediği + kuruluşun gerekli gördüğü dokümante bilgi | BGYS-LS-04 Doküman Ana Listesi | — |
| 7.5.2 **Z** | Tanımlama, format, gözden geçirme ve onay | BGYS-PR-01 | "Bu doküman kim tarafından onaylandı, ne zaman?" |
| 7.5.3 **Z** | Erişilebilirlik, koruma, dağıtım, saklama, değişiklik kontrolü, saklama/imha; dış kaynaklı dokümanların kontrolü | BGYS-PR-01 | "Eski sürüm nerede? Nasıl engelliyorsunuz kullanılmasını?" |

**Yazarken:** 7.3 farkındalık maddesi denetimde çalışan mülakatıyla test edilir —
doküman ne kadar iyi olursa olsun çalışan bilmiyorsa bulgu gelir. Bu yüzden
farkındalık planına ölçüm koy (kısa sınav, oltalama tatbikatı sonucu) ve bunu
hedef tablosuna bağla.

7.5.3'te en sık atlanan: **dış kaynaklı dokümanların kontrolü** (standartlar,
mevzuat metinleri, tedarikçi el kitapları). Doküman ana listesinde ayrı bir
sekme aç.

---

## 8 — İşletim

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 8.1 | Proseslerin planlanması, uygulanması, kontrolü; kriterlerin belirlenmesi; **planlı değişikliklerin kontrolü, plansız değişikliklerin gözden geçirilmesi**; dış kaynaklı proseslerin kontrolü | Prosedürler + BGYS-PR-21 | "Dış kaynaklı süreçleri nasıl kontrol ediyorsunuz?" |
| 8.2 **Z** | Risk değerlendirmesinin planlı aralıklarla ve önemli değişiklikte yapılması; **sonuçların kaydı** | BGYS-FR-03 (tarihli sürümler) | "Risk değerlendirmesini en son ne zaman yaptınız? Neden o zaman?" |
| 8.3 **Z** | Risk işleme planının uygulanması; **sonuçların kaydı** | BGYS-PN-01 (durum sütunu dolu) | "Risk işleme planındaki şu aksiyon tamamlandı mı? Kanıtı nerede?" |

**Yazarken:** 8.2 ve 8.3'ün 6.1.2/6.1.3'ten farkı zamandır — 6.1 süreci *tanımlar*,
8.2/8.3 süreci *çalıştırır* ve sonucu kaydeder. Bu yüzden risk envanterinde
"değerlendirme tarihi" ve "bir sonraki gözden geçirme" alanları olmalı; boş bir
risk envanteri 6.1'i karşılar ama 8.2'yi karşılamaz.

---

## 9 — Performans değerlendirmesi

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 9.1 **Z** | Ne izlenecek, yöntem, ne zaman, kim, sonuçlar ne zaman analiz edilecek, kim tarafından; **sonuçların kaydı** | BGYS-FR-04 + periyodik raporlar | "Kontrollerin etkinliğini nasıl ölçüyorsunuz? Örnek bir ölçüm gösterin." |
| 9.2.1 | Planlı aralıklarla iç tetkik; kendi gerekliliklerine ve standarda uygunluk, etkin uygulanma | BGYS-PR-10 | — |
| 9.2.2 **Z** | Tetkik programı: sıklık, yöntem, sorumluluk, planlama, raporlama; kriter ve kapsam tanımı; tarafsız tetkikçi; sonuçların yönetime raporlanması; **program ve sonuçların kaydı** | BGYS-PN-03 + BGYS-FR-06 | "Tetkikçi kendi işini tetkik etmiş mi? Tarafsızlık nasıl sağlandı?" |
| 9.3.1 | Planlı aralıklarla YGG | BGYS-PR-22 | — |
| 9.3.2 | On girdi başlığı: önceki YGG aksiyonları, değişen iç/dış hususlar, ilgili taraf gereklilikleri, performans geri bildirimi (uygunsuzluk/DÖF, izleme sonuçları, tetkik sonuçları, hedeflere ulaşma), sürekli iyileştirme fırsatları, risk değerlendirme sonuçları ve risk işleme planı durumu | BGYS-FR-13 | "YGG gündeminde şu girdi var mı?" — tek tek kontrol eder |
| 9.3.3 **Z** | Sürekli iyileştirme fırsatları ve BGYS değişiklik ihtiyaçlarına ilişkin kararlar; **sonuçların kaydı** | BGYS-FR-13 tutanak | "YGG'de alınan kararlar uygulandı mı?" |

**Yazarken:** 9.3.2'nin girdi listesi denetimde madde madde kontrol edilir. YGG
formunu **girdi başlıklarının her birine ayrı bölüm ayıracak** şekilde tasarla;
bu tek tasarım kararı en sık görülen YGG bulgusunu ortadan kaldırır.

9.1'de "sonuçların ne zaman ve kim tarafından analiz edileceği" ayrı bir
gerekliliktir — ölçüm yapmak yetmiyor, analiz sorumlusu ve zamanı da tanımlı olmalı.

---

## 10 — İyileştirme

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 10.1 | BGYS'nin uygunluk, yeterlilik ve etkinliğinin sürekli iyileştirilmesi | YGG kararları, iyileştirme kayıtları | "Son bir yılda sistemi nasıl iyileştirdiniz?" |
| 10.2 **Z** | Uygunsuzlukta: tepki verme ve düzeltme, sonuçları ele alma; **kök neden analizi**, benzer uygunsuzluk var mı incelemesi, düzeltici faaliyet, etkinliğin gözden geçirilmesi, gerekirse BGYS değişikliği; **uygunsuzluk/faaliyet ve sonuçların kaydı** | BGYS-PR-03 + BGYS-FR-12 | "Şu uygunsuzluğun kök nedeni ne? Benzeri başka yerde var mı diye baktınız mı? Etkinliğini nasıl doğruladınız?" |

**Yazarken:** DÖF formunun üç alanı en sık eksik çıkar: **kök neden analizi**
(5 Neden / balık kılçığı gibi bir yöntem adı geçmeli), **benzer uygunsuzluk
taraması**, ve **etkinlik doğrulama** (kapatma tarihinden sonra ayrı bir kontrol,
ayrı tarih ve imza ile). Formu bu üç alanı zorunlu kılacak şekilde tasarla.

---

## Zorunlu dokümante bilgi — hızlı kontrol listesi

Denetçinin "bunlar yoksa devam edemem" dediği çıktılar:

1. BGYS kapsamı (4.3)
2. Bilgi güvenliği politikası (5.2)
3. Risk değerlendirme süreci (6.1.2)
4. Risk işleme süreci (6.1.3)
5. **Uygulanabilirlik Bildirgesi** (6.1.3 d)
6. Bilgi güvenliği hedefleri (6.2)
7. Yetkinlik kanıtı (7.2)
8. Standardın ve kuruluşun gerekli gördüğü dokümante bilgi (7.5.1)
9. İşletim planlama ve kontrol kanıtı (8.1)
10. Risk değerlendirme sonuçları (8.2)
11. Risk işleme sonuçları (8.3)
12. İzleme ve ölçme sonuçları (9.1)
13. İç tetkik programı ve sonuçları (9.2.2)
14. YGG sonuçları (9.3.3)
15. Uygunsuzluk ve düzeltici faaliyet kayıtları (10.2)

Bu on beşinin tamamı üretilen sette karşılığı olan bir dosyaya işaret etmeli.
Öz kontrol adımında bunu tek tek doğrula.
