# ISO 22301:2019 Madde 4–10 — Gereklilik / Doküman / Kanıt

`Z` = standardın dokümante edilmiş bilgi olarak açıkça istediği çıktı.
Hiçbir madde hariç tutulamaz.

---

## 4 — Kuruluşun bağlamı

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 4.1 | Amaçla ilgili iç ve dış hususlar | İSYS-FR-01 Bağlam Analizi | "Faaliyetinizi kesintiye uğratabilecek dış etkenler neler?" |
| 4.2.1 | İlgili taraflar ve gereklilikleri | İSYS-LS-06 | "Müşteri sözleşmelerinizde süreklilik taahhüdü var mı?" |
| 4.2.2 **Z** | **Yasal ve düzenleme amaçlı gereklilikler** — belirlenmeli, erişilebilir olmalı, güncel tutulmalı | İSYS-LS-03 Yasal Yükümlülükler Matrisi | "Sektörünüzde süreklilik konusunda zorunluluk var mı? Nasıl takip ediyorsunuz?" |
| 4.3.1 **Z** | Kapsam sınırları ve uygulanabilirlik; kapsam dışı bırakılanların gerekçesi | İSYS-PL-00 Kapsam Dokümanı | "Kapsam dışı bıraktığınız birim/faaliyet var mı, neden?" |
| 4.3.2 | Kapsam belirlenirken misyon, hedefler, iç/dış yükümlülükler, risk iştahı dikkate alınmalı | İSYS-PL-00 | "Kapsamı belirlerken neyi göz önüne aldınız?" |
| 4.4 | İSYS'nin kurulması, uygulanması, sürdürülmesi, sürekli iyileştirilmesi | İSYS-EK-01 El Kitabı | "Süreç haritanız var mı?" |

**Yazarken:** 4.2.2 diğer Annex SL standartlarında olmayan **ayrı bir alt
maddedir** — 22301'e özgü ağırlığı vardır. Yasal yükümlülük matrisini ayrı ve
somut yap: mevzuat adı, ilgili madde, kuruluşa etkisi, uyum durumu, sorumlu,
gözden geçirme sıklığı.

---

## 5 — Liderlik

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 5.1 | Üst yönetimin liderlik ve taahhüdü | YGG tutanakları, bütçe, kaynak kararları | "Süreklilik için ayırdığınız bütçe/kaynak nedir?" |
| 5.2.1 **Z** | Politika: amaca uygun, hedeflere çerçeve, uygulanabilir gereklilikleri karşılama ve sürekli iyileştirme taahhüdü | İSYS-PL-01 | "Politikayı üst yönetim onayladı mı, ne zaman?" |
| 5.2.2 | Politikanın **iletilmesi**: dokümante, duyurulmuş, uygunsa ilgili taraflara açık | Duyuru kanıtı | "Politika çalışanlara nasıl ulaştı?" |
| 5.3 | Görev, sorumluluk ve yetkilerin atanması ve duyurulması; İSYS performansının üst yönetime raporlanması | Görev tanımları, organizasyon şeması | "İSYS performansını kim, ne sıklıkla raporluyor?" |

---

## 6 — Planlama

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 6.1.1 | İSYS'ye ilişkin risk ve fırsatların belirlenmesi | İSYS-PR-02 | "İSYS'nin amaçlanan sonuca ulaşmasını ne engelleyebilir?" |
| 6.1.2 | Risk ve fırsatların ele alınması; eylemlerin entegrasyonu ve etkinliğin değerlendirilmesi | İSYS-FR-03 | "Bu riske karşı hangi eylemi aldınız, işe yaradı mı?" |
| 6.2.1 | Amaçların belirlenmesi | İSYS-FR-04 | — |
| 6.2.2 **Z** | Hedefler: politikayla tutarlı, ölçülebilir, gereklilikleri dikkate alan, izlenen, duyurulan, güncellenen; ne/kaynak/kim/ne zaman/nasıl değerlendirilecek | İSYS-FR-04 | "Bu yılki süreklilik hedefleriniz ve mevcut durumunuz?" |
| 6.3 | İSYS değişikliklerinin planlı yapılması | İSYS-PR-08 | "Son değişikliği nasıl planladınız?" |

**Yazarken:** 22301'de hedefler, minimum kabul edilebilir hizmet seviyeleriyle
ilişkilendirilmelidir. Örnek: "kritik faaliyet A için RTO 4 saat hedefine
tatbikatta ulaşma oranı ≥ %90".

---

## 7 — Destek

| Madde | Gereklilik | Doküman |
|---|---|---|
| 7.1 | Kaynakların belirlenmesi ve sağlanması | Bütçe, kadro |
| 7.2 **Z** | Yetkinlik belirleme, sağlama, etkinlik değerlendirme; **yetkinlik kanıtı** | İSYS-LS-07 Yetkinlik Matrisi |
| 7.3 | Farkındalık: politika, katkı, uygunsuzluğun sonuçları, **kesinti anındaki kendi rolü** | İSYS-PN-02 Farkındalık Planı |
| 7.4 | İletişim: ne, ne zaman, kim, kime, nasıl | İSYS-PN-06 İletişim Planı |
| 7.5.1–7.5.3 **Z** | Dokümante bilgi: oluşturma, güncelleme, kontrol, erişim, saklama | İSYS-PR-01 |

**Yazarken:** 7.3 farkındalığı 22301'de daha somut: her çalışan **kesinti
anında kendi rolünü** bilmeli. Farkındalık planına "rol kartı" veya cep kartı
üretimini ekle — denetçi çalışana "kesinti olsa ilk ne yaparsınız?" diye sorar.

---

## 8 — İşletim (22301'in kalbi)

### 8.1 İşletimsel planlama ve kontrol
Proseslerin planlanması, kriterlerin belirlenmesi, kriterlere uygun kontrol,
dokümante bilginin saklanması; dış kaynaklı proseslerin kontrolü.

### 8.2 İş etki analizi ve risk değerlendirmesi **Z**

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 8.2.1 | BIA ve risk değerlendirme sürecinin uygulanması ve sürdürülmesi | İSYS-PR-03 BIA ve Risk Metodolojisi |
| 8.2.2 **Z** | BIA: faaliyet türlerinin analizi, kesinti etkilerinin zaman içinde değerlendirilmesi, **öncelikli faaliyetlerin belirlenmesi ve zaman çerçeveleri**, bağımlılıklar ve destekleyici kaynaklar | İSYS-FR-02 İş Etki Analizi |
| 8.2.3 | Öncelikli faaliyetlerin kesintiye uğrama riskinin değerlendirilmesi ve işlenmesi | İSYS-FR-03 Risk Değerlendirmesi |

BIA'nın çıktısı **zorunlu olarak** şunları içerir: önceliklendirilmiş faaliyetler,
her biri için kesintinin kabul edilemez hâle geldiği süre (MTPD), kurtarma süresi
hedefi (RTO), kurtarma noktası hedefi (RPO), minimum kabul edilebilir hizmet
seviyesi (MBCO) ve bağımlılıklar.

### 8.3 İş sürekliliği stratejileri ve çözümleri **Z**

| Alt madde | Gereklilik |
|---|---|
| 8.3.1–8.3.2 | Stratejilerin BIA ve risk değerlendirmesine dayalı belirlenmesi |
| 8.3.3 | Stratejilerin seçimi — kaynak gereksinimi ve maliyet gözetilerek |
| 8.3.4 | **Kaynak gereksinimleri**: insan; bilgi ve veri; fiziksel altyapı; ekipman ve sarf malzemeleri; BİT sistemleri; ulaşım ve lojistik; finans; ortaklar ve tedarikçiler |
| 8.3.5 | Seçilen çözümlerin uygulanması |

8.3.4'teki sekiz kaynak başlığının her birine bir satır ayır. Boş geçilen başlık
bulgu üretir; "uygulanabilir değil" yazacaksan gerekçesini yaz.

### 8.4 İş sürekliliği planları ve prosedürleri **Z**

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 8.4.1 | Kesintiye müdahale, sürdürme ve geri dönüş için yapı, plan ve prosedürler | İSYS-PN-03 IS Planları |
| 8.4.2 | **Müdahale yapısı**: olay değerlendirme, müdahale ekipleri, yetkiler, **yedek atamalar**, tetikleme kriterleri | İSYS-PN-01 Olay Müdahale Yapısı |
| 8.4.3 | **Uyarı ve iletişim**: iç/dış ilgili taraflar, yetkili merciler, **alternatif iletişim kanalları**, iletişim kayıtları | İSYS-PN-06 |
| 8.4.4 | **İş sürekliliği planları**: amaç ve kapsam, roller, aktivasyon, kaynaklar, iç/dış bağımlılıklar, bilgi gereksinimleri, ilgili taraf iletişimi | İSYS-PN-03 |
| 8.4.5 | **Eski hâline geri dönme** — normal operasyona dönüş prosedürleri | İSYS-PN-03 §Geri Dönüş |

### 8.5 Alıştırma (tatbikat) programı **Z**
Tatbikatlar: hedeflerle tutarlı, senaryolar planlı ve gerçekçi, riski minimize
edecek biçimde, resmî tatbikat sonrası raporu (sonuç, öneri, iyileştirme),
sonuçlara göre iyileştirme yapılması. Planlı aralıklarla ve **önemli değişiklik
sonrası** yapılmalı.

### 8.6 İş sürekliliği dokümantasyonunun ve yeteneklerinin değerlendirilmesi **Z**
Planlı aralıklarla ve önemli değişiklikte değerlendirme; **sonuçlar dokümante
edilmeli** ve iyileştirmeye dönüşmeli.

---

## 9 — Performans değerlendirmesi

| Madde | Gereklilik | Doküman |
|---|---|---|
| 9.1 **Z** | Ne izlenecek, yöntem, ne zaman, kim; sonuçların ne zaman ve kim tarafından analiz ve değerlendirileceği; **sonuçların kaydı** | İSYS-FR-04 + periyodik rapor |
| 9.2.1–9.2.2 **Z** | İç tetkik; program: sıklık, yöntem, sorumluluk, planlama, raporlama; tarafsızlık; **program ve sonuç kaydı** | İSYS-PR-05 + İSYS-PN-04 |
| 9.3.2 | YGG girdileri: önceki YGG durumu, değişen iç/dış hususlar, performans bilgisi (uygunsuzluk/DÖF, izleme, tetkik sonuçları), ilgili taraf geri bildirimi, **BIA ve risk değerlendirmesi güncellik durumu**, **tatbikat sonuçları**, iyileştirme fırsatları | İSYS-FR-13 |
| 9.3.3 **Z** | Kararlar: sürekli iyileştirme fırsatları, İSYS değişiklik ihtiyaçları; **sonuçların kaydı** | İSYS-FR-13 |

---

## 10 — İyileştirme

| Madde | Gereklilik | Doküman |
|---|---|---|
| 10.1 **Z** | Uygunsuzlukta: tepki ve düzeltme, sonuçları ele alma, **kök neden**, benzerinin var olup olmadığı, düzeltici faaliyet, etkinlik gözden geçirmesi, gerekirse İSYS değişikliği; **kayıt** | İSYS-PR-04 + İSYS-FR-12 |
| 10.2 | Sürekli iyileştirme | YGG kararları |

**Dikkat:** 22301'de numaralandırma 27001'in tersidir — **10.1 uygunsuzluk ve
düzeltici faaliyet**, 10.2 sürekli iyileştirmedir. Doküman içinde madde atıfı
verirken bunu karıştırma; yanlış madde atıfı denetçide özensizlik izlenimi yaratır.

---

## Zorunlu dokümante bilgi — hızlı kontrol listesi

1. Yasal ve düzenleme amaçlı gereklilikler (4.2.2)
2. İSYS kapsamı ve hariç tutma gerekçeleri (4.3.1)
3. İş sürekliliği politikası (5.2.1)
4. İş sürekliliği hedefleri (6.2.2)
5. Yetkinlik kanıtı (7.2)
6. Gerekli görülen dokümante bilgi (7.5.1)
7. İşletim planlama ve kontrol kanıtı (8.1)
8. BIA ve risk değerlendirme süreci ve sonuçları (8.2)
9. Süreklilik stratejileri ve kaynak gereksinimleri (8.3)
10. Müdahale yapısı, iletişim ve iş sürekliliği planları (8.4)
11. Tatbikat programı ve tatbikat sonuç raporları (8.5)
12. Dokümantasyon ve yetenek değerlendirme sonuçları (8.6)
13. İzleme ve ölçme sonuçları (9.1)
14. İç tetkik programı ve sonuçları (9.2)
15. YGG sonuçları (9.3.3)
16. Uygunsuzluk ve düzeltici faaliyet kayıtları (10.1)
