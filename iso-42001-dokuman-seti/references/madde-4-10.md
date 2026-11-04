# ISO/IEC 42001:2023 Madde 4–10 — Gereklilik / Doküman / Kanıt

`Z` = dokümante edilmiş bilgi olarak açıkça istenen. Hiçbir madde hariç tutulamaz.
Ek A kontrolleri gerekçeyle hariç tutulabilir.

---

## 4 — Kuruluşun bağlamı

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 4.1 | İç ve dış hususlar; **kuruluşun YZ ile ilgili rolü/rolleri**; **iklim değişikliğinin ilgili bir husus olup olmadığı** | YZYS-FR-01 Bağlam Analizi | "Bu sistemde üretici misiniz, müşteri mi? Yükümlülük farkını nasıl ele aldınız?" · "İklim değişikliğini değerlendirdiniz mi?" |
| 4.2 | İlgili taraflar ve gereklilikleri; **ilgili tarafların iklimle ilgili gereklilikleri** | YZYS-LS-05 | "YZ sisteminizin kararına maruz kalan kişiler ilgili taraf listenizde var mı?" |
| 4.3 **Z** | YZYS kapsamı; hangi YZ sistemleri, hangi yaşam döngüsü aşamaları | YZYS-PL-00 Kapsam Dokümanı | "Kapsam dışı bıraktığınız YZ sistemi var mı, neden?" |
| 4.4 | YZYS'nin kurulması ve sürekli iyileştirilmesi | YZYS-EK-01 | "Süreç haritanız?" |

### İklim değişikliği — atlanırsa kesin bulgu

Tüm Annex SL yönetim sistemi standartlarına 2024 tadilatıyla eklenen iki cümle
42001 için de geçerlidir ve **belgelendirme kuruluşlarının tetkik kontrol
listelerinde ayrı satır olarak** yer alır:

1. Kuruluş, **iklim değişikliğinin ilgili bir husus olup olmadığını** belirlemelidir (4.1).
2. İlgili tarafların **iklim değişikliğiyle ilgili gereklilikleri olabilir** (4.2 notu).

İki soru da "evet" cevabı gerektirmez — gerektirdiği şey **değerlendirmenin
yapıldığının gösterilmesidir.** "İlgili değildir" cevabı da geçerlidir, ama
gerekçesiz olamaz.

42001'de bu maddenin özel bir ağırlığı vardır: A.4.5 zaten YZ iş yükünü çalıştıran
donanımın **maliyet ve çevresel etkisinin nicelendirilmesini** ister, A.5.5 ise
toplumsal etki değerlendirmesinde **çevresel sürdürülebilirlik, doğal kaynak
kullanımı ve sera gazı emisyonlarını** sayar. Yani 42001'de iklim, bağlam
analizinde bir kutucuk değil, üç ayrı yerde beslenen bir zincirdir:

```
4.1 iklim ilgili bir husus mu? → A.4.5 hesaplama kaynağının çevresel etkisi
                               → A.5.5 toplumsal etki: çevresel sürdürülebilirlik
                               → 6.2 varsa ölçülebilir hedef
```

Bağlam analizinde bu değerlendirmeyi bir paragrafla geç, ama üç ayağın da
karşılığını üret. Yalnızca 4.1'de "değerlendirildi" yazıp A.4.5 ve A.5.5'i boş
bırakmak zinciri kopartır.

**Yazarken:** 4.1'de kuruluşun YZ rolünü açıkça belirtmek 42001'e özgü ve
kritiktir. Rol taksonomisi üç değil dörttür (sağlayıcı · üretici · müşteri ·
ortak); ayrıntı ve rol-kontrol eşlemesi için `roller-ve-yetkinlik.md` §1.
Aynı kuruluş bir sistemde üretici, başkasında müşteri olabilir; envanterde her
sistem için rol sütunu bulunmalı. İlgili taraflar listesinde **YZ süjeleri**
(müşteri değil, kararın muhatabı) ve **ilgili otoriteler** mutlaka yer almalı —
bu 42001'in ayırt edici beklentisidir.

---

## 5 — Liderlik

| Madde | Gereklilik | Doküman |
|---|---|---|
| 5.1 | Üst yönetimin liderlik ve taahhüdü; YZ hedeflerinin stratejiyle uyumu | YGG tutanakları, bütçe, kaynak kararları |
| 5.2 **Z** | **YZ politikası**: amaca uygun, hedeflere çerçeve, uygulanabilir gereklilikleri karşılama ve sürekli iyileştirme taahhüdü; dokümante, duyurulmuş, erişilebilir | YZYS-PL-01 |
| 5.3 | Rol, sorumluluk ve yetkiler | YZYS-EK-01 §Roller, görev tanımları |

**Yazarken:** YZ politikası (Ek A.2.3 gereği) **diğer kurumsal politikalarla
uyumlu** olmalı — bilgi güvenliği, kişisel veri, kalite, etik politikalarıyla
çelişki taranmalı. Bu taramayı bir uyum matrisiyle belgele; denetçi çelişki
arar ve bulduğunda politikanın gerçekten yönetilmediği sonucuna varır.

---

## 6 — Planlama

| Madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 6.1.1 | Risk ve fırsatların belirlenmesi; **tek bir risk kriteri seti** | YZYS-PR-01 | "Kabul edilebilir ve edilemez riski nasıl ayırıyorsunuz?" |
| 6.1.2 **Z** | **YZ risk değerlendirmesi**: risk kriterleri (kabul + değerlendirme), tekrarlanabilirlik, tanımlama, analiz, değerlendirme; **süreç hakkında yazılı bilgi** | YZYS-PR-01 + YZYS-FR-03 | "Risk kabul kriteriniz nedir?" |
| 6.1.3 **Z** | **YZ risk işleme**: seçenekler, kontroller, **Ek A ile karşılaştırma**, **SoA**, risk işleme planı, risk sahibi onayı | YZYS-LS-01 SoA + risk işleme planı | "SoA'daki bu kontrol neden gerekli? Hangi riskten geliyor?" |
| 6.1.4 **Z** | **YZ sistemi etki değerlendirmesi süreci** — kişiler, kişi grupları ve toplum üzerindeki potansiyel sonuçların değerlendirilmesi | YZYS-PR-02 + YZYS-FR-04 | "Bu sistem kime zarar verebilir? Nasıl değerlendirdiniz?" |
| 6.2 **Z** | YZ hedefleri: ölçülebilir, izlenen, duyurulan, güncellenen; **hedefe ulaşma planı** | YZYS-FR-02 | "Bu yılki YZ hedefleriniz ve mevcut durumunuz?" |
| 6.3 | Değişikliklerin planlı yapılması — **altı unsur** | YZYS-PR-13 | "Son model güncellemesinde geri alma planınız neydi?" |

**6.1.4 diğer hiçbir Annex SL standardında yoktur.** Bu madde 42001'in varlık
sebebidir; ayrıntı için `etki-degerlendirmesi.md` dosyasını oku. Risk
değerlendirmesiyle birleştirilmiş bir doküman bu maddeyi karşılamaz.

### 6.1.1 — risk kriteri seti üçünü birden kapsamalı

Tetkik kontrol listelerindeki soru şudur: risk kriterleri, **kabul edilebilir ve
kabul edilemez riski ayırt etmek**, **risk değerlendirmesi yapmak**, **risk
işleme yürütmek** *ve* **YZ risk etkilerini değerlendirmek** için oluşturulmuş
mu? Yani tek bir kriter seti, hem 6.1.2/6.1.3 zincirini hem de 6.1.4 zincirini
beslemek zorundadır.

Pratik sonuç: risk metodolojisi dokümanında **iki ayrı ölçek** tanımla.

| | Kurumsal risk ölçeği | Etki ölçeği |
|---|---|---|
| Eksen | Olasılık × Etki (kuruluşa) | Şiddet × Olasılık × Etkilenen kitle |
| Ek eksen | — | **Tersine çevrilebilirlik**, kırılgan grup |
| Kabul kararı | Risk sahibi | Risk sahibi **+ etki sahibi/etik sorumlusu** |

Tek ölçekle iki zinciri yönetmeye çalışmak, etki değerlendirmesini risk
değerlendirmesinin bir sütununa indirger — 6.1.4'ün karşılanmadığı yer tam
burasıdır.

Ayrıca kontrol listesi "risk değerlendirmesi **planlı aralıklarla ve kuruluşta
değişiklik olduğunda** gözden geçiriliyor mu?" diye sorar. Metodolojide sıklık
sayıyla yazılmalı ("yılda bir" değil, hangi ay; "önemli değişiklikte" değil,
tetikleyici listesiyle).

### 6.3 — değişiklik yönetiminin altı unsuru

"YZYS'de değişiklikler planlı yapılır" cümlesi bu maddeyi karşılamaz. Denetçi
her uygulanan değişiklik için altı unsurun izini arar:

1. **İhtiyacın belirlenmesi** — değişiklik neden gerekli
2. **Etkinin değerlendirilmesi** — risk ve **etki** değerlendirmesinin yeniden çalıştırılması
3. **Paydaşlara duyuru** — kimin haberi olacak, hangi kanaldan
4. **Geri alma (roll-back) stratejisi** — çalışmazsa nasıl dönülecek
5. **Uygulamanın kontrolü** — onay, aşamalı yayın, test kapısı
6. **Uygulama sonrası gözden geçirme** — hedefe ulaşıldı mı, yeni kabul edilemez risk doğdu mu

YZ bağlamında 4. unsur özellikle önemlidir: model yeniden eğitildiğinde önceki
sürüme dönebilmek teknik bir yetenek meselesidir; prosedürde yazılı olması
yetmez, MLOps tarafında karşılığı olmalıdır. PR-13'ü "birleşir" diye geçme;
en azından bu altı başlıklı bir bölüm üret.

---

## 7 — Destek

| Madde | Gereklilik | Doküman |
|---|---|---|
| 7.1 | Kaynaklar | Bütçe, kadro, hesaplama kaynağı envanteri |
| 7.2 **Z** | Yetkinlik ve **yetkinlik kanıtı** | YZYS-LS-07 Yetkinlik Matrisi |
| 7.3 | Farkındalık: politika, katkı, uygunsuzluğun sonuçları | YZYS-PN-02 |
| 7.4 | İletişim: ne, ne zaman, kime, nasıl | YZYS-PN-04 İletişim Planı |
| 7.5.1–7.5.3 **Z** | Dokümante bilgi: oluşturma, güncelleme, kontrol | YZYS-PR-14 |

**Yazarken:** 7.2 yetkinlik 42001'de özel ağırlık taşır — YZ yetkinliği yalnızca
teknik değildir. Etki değerlendirmesi yapacak kişinin etik, hukuk ve alan
bilgisine de ihtiyacı vardır. Yetkinlik matrisinde teknik/etik/hukuki/alan
boyutlarını ayır.

---

## 8 — İşletim

| Madde | Gereklilik | Doküman |
|---|---|---|
| 8.1 | İşletim planlama ve kontrol; kriterlerin belirlenmesi; **istenmeyen değişikliklerin sonuçlarının gözden geçirilmesi**; **dış kaynaklı ürün, hizmet ve proseslerin kontrolü** | Yaşam döngüsü prosedürleri (Ek A.6) |
| 8.2 **Z** | YZ risk değerlendirmesinin planlı aralıklarla ve önemli değişiklikte uygulanması; **sonuçların kaydı** | YZYS-FR-03 (tarihli sürümler) |
| 8.3 **Z** | YZ risk işleme planının uygulanması; **sonuçların kaydı** | Risk işleme planı (durum sütunu dolu) |
| 8.4 **Z** | **YZ sistemi etki değerlendirmesinin uygulanması; sonuçların kaydı** | YZYS-FR-04 |

**Yazarken:** 8.4 ayrı bir işletim gerekliliğidir — 6.1.4 süreci *tanımlar*,
8.4 süreci *çalıştırır* ve sonucu kaydeder. Etki değerlendirmesi formunda
"değerlendirme tarihi" ve "sonraki gözden geçirme" alanları olmalı; hiç
uygulanmamış bir metodoloji 8.4'ü karşılamaz.

**8.1'in en çok atlanan yarısı: dış kaynaklı prosesler.** Üçüncü taraf model
API'si kullanan bir kuruluş için modelin kendisi dış kaynaklı bir prosestir.
"Kontrol ediyoruz" demek yetmez; hangi kontrolün nasıl uygulandığı yazılı
olmalı: sağlayıcı seçim kriteri, sözleşmedeki YZ hükümleri, sürüm değişikliği
bildirimi, performans izleme, çıkış (exit) planı. Bu, A.10.2–A.10.4 ile aynı
malzemeyi kullanır; iki kez yazma, 8.1'den YZYS-PR-12'ye atıf ver.

**İstenmeyen değişiklikler.** 6.3 *planlı* değişikliği yönetir; 8.1 ise
**istenmeyen** değişikliğin sonuçlarının gözden geçirilmesini ister. YZ
bağlamında bunun en tipik örneği sağlayıcının haber vermeden yaptığı model
güncellemesi ve verinin dağılımının zamanla kaymasıdır (drift). İkisi de
"planlanmamış değişiklik" olarak PR-06 İşletim ve İzleme Prosedürü'nde
adlandırılmalı, tespit yöntemi ve müdahale eşiği yazılmalıdır.

---

## 9 — Performans değerlendirmesi

| Madde | Gereklilik | Doküman |
|---|---|---|
| 9.1 **Z** | İzleme, ölçme, analiz ve değerleme: ne, yöntem, ne zaman, kim; **sonuçların kaydı** | YZYS-FR-02 + izleme raporları |
| 9.2.1–9.2.2 **Z** | İç tetkik ve tetkik programı; **tetkikçi yetkinliği ve bağımsızlığı**; sonuçların raporlanması | YZYS-PR-15 + YZYS-PN-03 |
| 9.3.2 | YGG girdileri: önceki YGG, değişen hususlar, performans bilgisi (uygunsuzluk/DÖF, izleme, tetkik sonuçları, hedeflere ulaşma), ilgili taraf geri bildirimi, risk değerlendirme sonuçları, **etki değerlendirme sonuçları**, iyileştirme fırsatları | YZYS-FR-06 |
| 9.3.3 **Z** | Kararlar ve **sonuçların kaydı** | YZYS-FR-06 |

**Yazarken:** 9.1'de YZ'ye özgü izleme metrikleri ayrılmalı: model performansı
(doğruluk, gecikme), **adillik metrikleri**, model kayması (drift) göstergeleri,
olay sayısı, kullanıcı geri bildirimi, insan müdahale oranı. Sadece teknik
performans izleyen bir ölçüm sistemi 42001'in beklentisini karşılamaz.

**9.2'de iki ayrı soru sorulur ve ikisi de yazılı kanıt ister:**

- **Yetkinlik** — YZYS tetkikçisi neyi bilmek zorunda? Yönetim sistemi tetkik
  tekniği yetmez; YZ yaşam döngüsü, veri yönetişimi ve etki değerlendirmesi
  mantığı da gerekir. Tetkikçi yetkinlik kriterini PR-15'te yaz, kanıtını
  YZYS-LS-07'ye bağla.
- **Bağımsızlık** — tetkikçi, tetkik ettiği faaliyetten sorumlu olamaz. Modeli
  geliştiren kişi o modelin tetkikini yapamaz. Küçük kuruluşta çözüm çapraz
  tetkik veya dış kaynaktır; prosedürde hangisinin kullanılacağı yazılmalıdır.

Tetkik programı (PN-03), tetkik planı, soru listesi ve tetkik raporu ayrı
çıktılardır — "tetkik yaptık" beyanı dördünü birden karşılamaz. Soru listesi
için `assets/denetim_sorulari_42001.json` doğrudan kullanılabilir.

---

## 10 — İyileştirme

| Madde | Gereklilik | Doküman |
|---|---|---|
| 10.1 | Sürekli iyileştirme: YZYS'nin uygunluğu, yeterliliği ve etkinliği | YGG kararları, iyileştirme kayıtları |
| 10.2 **Z** | Uygunsuzluk ve düzeltici faaliyet: tepki, kök neden, benzerinin araştırılması, etkinlik gözden geçirmesi; **kayıt** | YZYS-PR-16 + YZYS-FR-05 |

> **Numaralandırma uyarısı.** Bazı belgelendirme kuruluşlarının tetkik kontrol
> listeleri sürekli iyileştirmeyi 10.3 olarak numaralandırır. Denetim öncesi
> kuruluşun kullandığı kontrol listesindeki numaralandırmayı teyit et; kanıt
> matrisinde madde numarasını değil **gerekliliği** çıpa olarak kullan, böylece
> numaralandırma farkı bulguya dönüşmez.

**Yazarken:** YZ olaylarında kök neden analizi klasik yöntemlerle sınırlı
kalmamalı — veri, model, dağıtım ortamı ve kullanım biçimi ayrı ayrı
incelenmeli. DÖF formunda "kök neden katmanı" alanı (veri / model / süreç /
insan / ortam) ayırt edici bir tasarım kararıdır.

**Sürekli iyileştirme ayrı bir kanıt ister.** 10.1 çoğu sette "YGG'de görüşülür"
diye geçiştirilir ve denetçi "iyileştirme örneği verin" dediğinde boşluk çıkar.
YZ bağlamında güçlü örnekler: izleme eşiğinin bir olay sonrası sıkılaştırılması,
açıklanabilirlik arayüzünün kullanıcı geri bildirimiyle değiştirilmesi, insan
gözetimi etkinliği düşük çıktığı için iş akışının yeniden tasarlanması. Bu tür
kararların **tarihli ve sonucu ölçülmüş** en az bir örneğini iyileştirme
kaydında tut.

---

## Zorunlu dokümante bilgi — hızlı kontrol listesi

1. YZYS kapsamı (4.3)
2. YZ politikası (5.2)
3. YZ risk değerlendirme süreci (6.1.2)
4. YZ risk işleme süreci (6.1.3)
5. **Uygulanabilirlik Bildirgesi** (6.1.3)
6. **YZ sistemi etki değerlendirme süreci** (6.1.4)
7. YZ hedefleri (6.2)
8. Yetkinlik kanıtı (7.2)
9. Gerekli görülen dokümante bilgi (7.5.1)
10. İşletim planlama ve kontrol kanıtı (8.1)
11. YZ risk değerlendirme sonuçları (8.2)
12. YZ risk işleme sonuçları (8.3)
13. **YZ sistemi etki değerlendirme sonuçları** (8.4)
14. İzleme ve ölçme sonuçları (9.1)
15. İç tetkik programı ve sonuçları (9.2)
16. YGG sonuçları (9.3.3)
17. Uygunsuzluk ve düzeltici faaliyet kayıtları (10.2)

5, 6 ve 13 bu standardın imzasıdır; eksikse 42001 karşılanmamış demektir.
