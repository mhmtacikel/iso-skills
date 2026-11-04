# BIA, RTO/RPO/MTPD, Strateji ve Plan Yazımı

## İçindekiler

- 1. Terimler — karıştırılması en pahalı üç kısaltma
- 2. BIA nasıl yapılır
  - Adım 1 — Faaliyetleri listele
  - Adım 2 — Kesinti etkisini zaman içinde değerlendir
  - Adım 3 — MTPD ve RTO belirle
  - Adım 4 — Bağımlılıkları çıkar
  - Adım 5 — Önceliklendir
  - BIA tablosunun zorunlu sütunları
- 3. Strateji ve boşluk analizi
  - Kaynak gereksinimi tablosu (8.3.4)
- 4. İş sürekliliği planının yapısı (8.4.4)
- 5. Tatbikat programı (8.5)
- 6. Değerlendirme (8.6)

22301'in tamamı bu zincirin üzerine kuruludur. Zincir koparsa sistem çöker:

```
Faaliyet → Kesinti etkisi (zaman içinde) → MTPD → RTO/RPO/MBCO
   → Boşluk analizi → Strateji → Kaynak gereksinimi → Plan → Tatbikat → İyileştirme
```

Denetçi rastgele bir faaliyet seçer ve bu zinciri ucundan ucuna takip eder.
Her üretilen dokümanda halkanın bir sonrakine bağlandığından emin ol.

---

## 1. Terimler — karıştırılması en pahalı üç kısaltma

| Terim | Ne demek | Kim belirler | İlişki |
|---|---|---|---|
| **MTPD** (Maksimum Tahammül Edilebilir Kesinti Süresi) | Faaliyetin durmasının kuruluş için kabul edilemez hâle geldiği süre | İş tarafı / üst yönetim | Üst sınır |
| **RTO** (Kurtarma Süresi Hedefi) | Faaliyetin minimum seviyede yeniden başlatılması için konan hedef süre | İş + BT birlikte | **RTO < MTPD olmalı** |
| **RPO** (Kurtarma Noktası Hedefi) | Kabul edilebilir azami veri kaybı — "kaç saatlik veriyi kaybedebiliriz" | Veri sahibi | RTO'dan bağımsız |
| **MBCO** (Minimum Kabul Edilebilir Hizmet Seviyesi) | Kesinti sırasında sürdürülmesi gereken asgari çıktı | İş tarafı | Strateji buna göre boyutlanır |

**En sık hata:** RTO ≥ MTPD yazılması. Bu mantıksal olarak imkânsızdır — hedef,
tahammül sınırını aşamaz. BIA tablosunda otomatik kontrol koy.

**İkinci sık hata:** RPO'nun RTO ile aynı yazılması. Bunlar farklı şeyler ölçer.
Bir sistem 4 saatte ayağa kalkabilir (RTO=4s) ama son yedek 24 saat öncesine
aitse RPO=24s'tir ve bu ayrı bir sorundur.

---

## 2. BIA nasıl yapılır

### Adım 1 — Faaliyetleri listele
Süreç değil **faaliyet** düzeyinde. "Finans" bir birimdir; "müşteri ödemelerinin
tahsilatı ve mutabakatı" bir faaliyettir. 20–60 faaliyet tipik bir aralıktır.

### Adım 2 — Kesinti etkisini zaman içinde değerlendir
Tek bir "etki" puanı yetmez; standart etkinin **zaman içinde** değerlendirilmesini
ister. Zaman dilimleri kullan:

| Faaliyet | 0–4 saat | 4–24 saat | 1–3 gün | 3–7 gün | 7+ gün |
|---|---|---|---|---|---|
| Müşteri ödemesi tahsilatı | Düşük | Orta | Yüksek | Kritik | Kritik |

Etki kategorileri (her biri ayrı değerlendirilmeli):
finansal · operasyonel · yasal/düzenleyici · itibar · müşteri/hizmet · personel güvenliği

### Adım 3 — MTPD ve RTO belirle
MTPD, etkinin "Kritik" olduğu ilk zaman dilimidir. RTO bundan kısa seçilir —
tipik olarak MTPD'nin yarısı ile üçte ikisi arası, ama gerekçelendirilmeli.

### Adım 4 — Bağımlılıkları çıkar
Her faaliyet için: hangi personel/rol, hangi sistem/uygulama, hangi veri, hangi
tedarikçi, hangi lokasyon, hangi ekipman, hangi diğer iç faaliyet.
**Bağımlılık zinciri** en çok atlanan kısımdır: A faaliyeti B faaliyetine bağlıysa
B'nin RTO'su A'nınkinden kısa olmak zorundadır.

### Adım 5 — Önceliklendir
RTO'ya göre sırala. En kısa RTO'lu faaliyetler "öncelikli faaliyetler"dir ve
strateji çalışmasının odağıdır.

### BIA tablosunun zorunlu sütunları

`Faaliyet No | Faaliyet | Sahip Birim | Süreç Sahibi | Etki: 0-4s / 4-24s / 1-3g /
3-7g / 7+g | Baskın etki türü | MTPD | RTO | RPO | MBCO (asgari çıktı) |
Bağımlı olduğu personel/rol | Sistemler | Veri | Tedarikçiler | Lokasyon |
Bağımlı olduğu diğer faaliyetler | Zirve dönem (mevsimsellik) | Mevcut kurtarma
yeteneği | Boşluk | Değerlendirme tarihi`

"Zirve dönem" sütununu atlama: bordro faaliyetinin ayın 25'inde kesilmesiyle
ayın 5'inde kesilmesi aynı şey değildir. Denetçi bunu sorar.

---

## 3. Strateji ve boşluk analizi

Her öncelikli faaliyet için: **mevcut yetenek** ile **RTO hedefi** arasındaki
farkı yaz. Boşluk yoksa da yaz — "boşluk yok" bir bulgudur, bilgidir.

Strateji seçenekleri (8.3.2/8.3.3):

| Kategori | Seçenekler |
|---|---|
| Personel | Çapraz eğitim, yedek personel, uzaktan çalışma, dış kaynak, kilit personel yedeği |
| Lokasyon | Alternatif ofis, evden çalışma, karşılıklı destek anlaşması, mobil çalışma |
| Teknoloji | Yedekli altyapı, farklı bölge/veri merkezi, bulut yedekliliği, manuel geçici çözüm |
| Veri | Yedekleme sıklığı, çoğaltma (replikasyon), yedek saklama lokasyonu, geri yükleme testi |
| Tedarikçi | Alternatif tedarikçi, çift kaynak, stok tamponu, sözleşmede süreklilik maddesi |
| Finans | Acil durum fonu, sigorta, kredi limiti |

### Kaynak gereksinimi tablosu (8.3.4)

Sekiz başlığın **her biri** için satır aç:

| Kaynak başlığı | Normal ihtiyaç | Kesinti sırasında ihtiyaç | Mevcut | Boşluk | Aksiyon | Sorumlu | Termin |
|---|---|---|---|---|---|---|---|
| İnsan | | | | | | | |
| Bilgi ve veri | | | | | | | |
| Fiziksel altyapı | | | | | | | |
| Ekipman ve sarf malzemeleri | | | | | | | |
| BİT sistemleri | | | | | | | |
| Ulaşım ve lojistik | | | | | | | |
| Finans | | | | | | | |
| Ortaklar ve tedarikçiler | | | | | | | |

---

## 4. İş sürekliliği planının yapısı (8.4.4)

Plan **kesinti anında okunabilir** olmalı. 40 sayfalık anlatı plan değildir;
kimse krizde onu okumaz. Yapı:

```
1. Amaç, kapsam ve bu planın kapsadığı faaliyetler
2. Aktivasyon
   2.1 Tetikleyici kriterler (eşik değerlerle)
   2.2 Aktivasyon yetkisi ve yedek yetkili
   2.3 Aktivasyon bildirim akışı (kim → kimi → hangi kanaldan → ne kadar sürede)
3. Roller ve ekipler
   3.1 Müdahale ekibi ve yedekleri (isim + yedek + iletişim)
   3.2 Karar yetkileri ve limitler
4. Müdahale adımları
   4.1 İlk 1 saat        ← kontrol listesi formatında
   4.2 İlk 24 saat
   4.3 24 saat sonrası
5. Kaynaklar ve erişim bilgileri (sistem, lokasyon, ekipman, erişim yolu)
6. İç ve dış bağımlılıklar
7. İletişim (ek: iletişim şablonları)
8. Normal operasyona geri dönüş
   8.1 Dönüş kriterleri
   8.2 Dönüş adımları ve doğrulama
   8.3 Kapanış ve olay sonrası değerlendirme
9. Ekler: iletişim listesi, kontrol listeleri, kayıt formları
```

Adım 4 bölümlerini **kontrol listesi** olarak yaz — kutucuk, adım, sorumlu,
tamamlanma saati. Anlatı paragrafı değil.

---

## 5. Tatbikat programı (8.5)

Tatbikat türleri, artan gerçekçilik sırasıyla:

| Tür | Ne yapılır | Süre | Sıklık önerisi |
|---|---|---|---|
| Masa başı (tabletop) | Ekip senaryoyu tartışır | 2–3 saat | Altı ayda bir |
| Çağrı ağacı testi | İletişim zinciri test edilir | 1 saat | Üç ayda bir |
| Teknik kurtarma testi | Sistem gerçekten geri yüklenir | Yarım gün | Yılda bir (kritik sistemler için altı ayda bir) |
| Simülasyon | Ekipler gerçek zamanlı müdahale eder | 1 gün | Yılda bir |
| Tam ölçekli | Alternatif lokasyona gerçek geçiş | 1–2 gün | 2 yılda bir |

Tatbikat programı tablosu: `Tatbikat No | Tür | Senaryo | Kapsanan plan/faaliyet |
Hedef (neyin doğrulanacağı) | Başarı kriteri | Katılımcılar | Planlanan tarih |
Gerçekleşen | Sonuç | Tespit edilen boşluklar | DÖF no | Durum`

**Başarı kriteri** sütunu kritik: "tatbikat yapıldı" bir sonuç değildir.
"RTO 4 saat hedefine 3 saat 20 dakikada ulaşıldı" bir sonuçtur.

Tatbikat sonrası raporu (8.5 gereği) şunları içermeli: senaryo, katılımcılar,
gözlemler, hedeflere ulaşma durumu, tespit edilen boşluklar, öneriler, aksiyon
planı ve sorumlular.

---

## 6. Değerlendirme (8.6)

Tatbikattan farklıdır. 8.6, dokümantasyonun ve yeteneklerin **planlı aralıklarla
ve önemli değişiklikte** değerlendirilmesini ister. Değerlendirme başlıkları:

- Planlar güncel mi? (organizasyon, sistem, tedarikçi değişiklikleri yansıdı mı)
- İletişim listeleri güncel mi? (en sık bayatlayan veri budur)
- BIA'daki RTO/RPO'lar hâlâ geçerli mi?
- Tatbikat bulguları kapatıldı mı?
- Gerçek kesinti yaşandıysa planlar işe yaradı mı?

Bu değerlendirmenin **sonuçları dokümante edilmeli**. Ayrı bir form üret; iç
tetkikle karıştırma — 8.6 işletimsel bir değerlendirmedir, 9.2 tetkiktir.
