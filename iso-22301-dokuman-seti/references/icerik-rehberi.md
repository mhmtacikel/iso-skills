# İçerik Rehberi — Kalite Çıtası ve Örnek Metinler

## İçindekiler

- 1. Kapsam beyanı
- 2. BIA satırı
- 3. Tetikleyici kriter
- 4. Müdahale adımı (kontrol listesi formatı)
- 5. Geri dönüş (8.4.5)
- 6. Kaynak gereksinimi satırı
- 7. Tatbikat başarı kriteri
- 8. `[DOLDURULACAK]` ve `[ÖRNEK]` kullanımı
- 9. Ton kontrolü

Her örneğin zayıf ve güçlü sürümü verilmiştir. Zayıf sürümler gerçek denetimlerde
bulgu almış kalıplardır.

---

## 1. Kapsam beyanı

**Zayıf:** "Şirketimizin tüm kritik faaliyetleri İSYS kapsamındadır."

**Güçlü:**
> Bu iş sürekliliği yönetim sistemi, ACME Lojistik A.Ş.'nin Gebze Dağıtım Merkezi
> (…) ve İstanbul Genel Müdürlük (…) lokasyonlarında yürüttüğü yurt içi parça
> yük taşımacılığı ve depolama hizmetlerinin, kesinti hâlinde önceden tanımlanmış
> asgari seviyede sürdürülmesini kapsar.
>
> **Kapsam dışı:** Adana Şubesi, 2026 Q4'te faaliyete geçecek olması ve henüz
> operasyonel veri üretmemesi nedeniyle bu revizyonda kapsam dışıdır; Rev. 02'de
> dahil edilecektir.
>
> **Kapsam belirlenirken dikkate alınanlar (4.3.2):** kuruluşun "kesintisiz
> tedarik zinciri" misyonu, müşteri sözleşmelerindeki 8 saatlik teslim taahhüdü,
> Karayolu Taşıma Yönetmeliği yükümlülükleri ve üst yönetimin belirlediği risk
> iştahı (yıllık ciro kaybı ≤ %2).

4.3.2'ye açık atıf yapmak denetçiye "bu maddeyi okumuşlar" mesajı verir ve
kapsam tartışmasını kısaltır.

---

## 2. BIA satırı

**Zayıf:** `Muhasebe | Yüksek | 24 saat`

**Güçlü:**

| Alan | Değer |
|---|---|
| Faaliyet No / Faaliyet | F-07 / Müşteri sevkiyat emirlerinin işlenmesi ve araç ataması |
| Sahip Birim / Süreç Sahibi | Operasyon / Operasyon Müdürü |
| Etki 0–4 sa | Düşük — bekleyen emirler manuel kuyruğa alınabilir |
| Etki 4–24 sa | Yüksek — teslim taahhüdü (8 sa) ihlal edilir, ceza işler |
| Etki 1–3 gün | Kritik — müşteri sözleşmesi fesih maddesi devreye girer |
| Baskın etki türü | Müşteri/Hizmet (ikincil: Finansal) |
| MTPD | 24 saat |
| RTO | 8 saat |
| RPO | 1 saat (sevkiyat emri kaybı kabul edilemez) |
| MBCO | Günlük 400 sevkiyatın en az 150'sinin işlenmesi |
| Bağımlı personel/rol | Operasyon Uzmanı (min. 2 kişi), Filo Sorumlusu |
| Bağımlı sistemler | TMS (Taşıma Yönetim Sistemi), GPS takip, ERP-sipariş modülü |
| Bağımlı veri | Aktif sipariş kuyruğu, araç/şoför müsaitlik tablosu |
| Bağımlı tedarikçiler | TMS SaaS sağlayıcısı (XYZ Bilişim), GSM operatörü |
| Bağımlı diğer faaliyetler | F-03 Sipariş kabul (RTO 4 sa — F-07'den kısa, tutarlı) |
| Zirve dönem | Ayın son 5 günü ve Kasım kampanya dönemi |
| Mevcut kurtarma yeteneği | 14 saat (TMS sağlayıcısının SLA'sı) |
| Boşluk | 6 saat — strateji gerekli (bkz. S-04) |

Son üç satır BIA'yı analiz olmaktan çıkarıp karar aracına dönüştürür.

---

## 3. Tetikleyici kriter

**Zayıf:** "Ciddi bir olay olduğunda plan devreye alınır."

**Güçlü:**
> **Aktivasyon kriterleri** — aşağıdakilerden herhangi biri gerçekleştiğinde
> Operasyon Müdürü (yokluğunda Operasyon Müdür Yardımcısı) planı devreye alır:
>
> - TMS'ye erişimin 2 saatten uzun süre kesilmesi veya 2 saatte çözüleceğine
>   dair sağlayıcıdan teyit alınamaması
> - Gebze Dağıtım Merkezi'ne fiziksel erişimin engellenmesi (yangın, sel, kolluk
>   kararı, iş kazası kaynaklı tahliye)
> - Operasyon ekibinin %50'sinden fazlasının aynı anda görev yapamaz hâle gelmesi
> - Ana GSM/internet hattının kesilmesi ve yedek hattın da 30 dakika içinde
>   devreye alınamaması
>
> Aktivasyon kararı, karar anından itibaren 15 dakika içinde İSYS-FR-08 Olay
> Kayıt Formu'na saat bilgisiyle işlenir.

Yetkinin **yedeği** ve kararın **kayda geçme süresi** olmadan bu bölüm eksiktir.

---

## 4. Müdahale adımı (kontrol listesi formatı)

Plan gövdesi anlatı değil, kontrol listesi olmalı. Kriz anında paragraf okunmaz.

**İlk 1 saat**

| ☐ | Adım | Sorumlu | Hedef süre | Tamamlanma saati |
|---|---|---|---|---|
| ☐ | Olayı doğrula, aktivasyon kriterini teyit et | Operasyon Müdürü | 0–10 dk | ______ |
| ☐ | Kriz ekibini çağrı ağacıyla topla (İSYS-FR-09) | Operasyon Müdürü | 0–20 dk | ______ |
| ☐ | Manuel sevkiyat kuyruğunu (Ek-3 formu) devreye al | Operasyon Uzmanı | 0–30 dk | ______ |
| ☐ | TMS sağlayıcısına olay bildir, tahmini süre al | BT Sorumlusu | 0–30 dk | ______ |
| ☐ | İlk müşteri bilgilendirmesini gönder (Şablon-1) | Müşteri İlişkileri | 30–60 dk | ______ |
| ☐ | Olay kaydını başlat, saat bilgisiyle | Kriz Sekreteri | Sürekli | ______ |

"Tamamlanma saati" sütunu tatbikatta ve gerçek olayda doldurulur; RTO'ya
ulaşılıp ulaşılmadığının kanıtı budur.

---

## 5. Geri dönüş (8.4.5)

Çoğu doküman setinin atladığı bölüm. Zayıf sürümü genellikle hiç yoktur.

**Güçlü:**
> **8. Normal operasyona geri dönüş**
>
> **8.1 Dönüş kriterleri** — aşağıdakilerin tamamı sağlandığında Operasyon Müdürü
> geri dönüş kararı verir: (a) TMS sağlayıcısı sistemin kararlı çalıştığını yazılı
> olarak teyit etmiştir; (b) manuel kuyrukta işlenmemiş sevkiyat kalmamıştır;
> (c) BT Sorumlusu veri bütünlüğü kontrolünü tamamlamıştır.
>
> **8.2 Dönüş adımları** — manuel kuyruktaki kayıtlar TMS'ye aktarılır ve çift
> kayıt kontrolü yapılır; araç atamaları sistemle karşılaştırılır; müşterilere
> normale dönüş bildirimi gönderilir (Şablon-4).
>
> **8.3 Kapanış** — olay kaydı kapatılır; 5 iş günü içinde olay sonrası
> değerlendirme toplantısı yapılır ve tespitler İSYS-FR-12'ye DÖF olarak işlenir.

---

## 6. Kaynak gereksinimi satırı

**Zayıf:** `İnsan | Yeterli personel | Var`

**Güçlü:**

| Kaynak başlığı | İnsan (personel, yetkinlik) |
|---|---|
| İlgili faaliyet | F-07 Sevkiyat emri işleme |
| Normal ihtiyaç | 4 Operasyon Uzmanı, 1 Filo Sorumlusu |
| Kesinti sırasında ihtiyaç | En az 2 Operasyon Uzmanı (MBCO 150 sevkiyat için) + manuel süreç eğitimi almış olmalı |
| Mevcut durum | 4 uzmandan yalnızca 1'i manuel süreç eğitimi almış |
| Boşluk | En az 2 kişilik çapraz eğitim eksiği |
| Aksiyon | 3 Operasyon Uzmanına manuel sevkiyat süreci eğitimi verilecek, masa başı tatbikatla doğrulanacak |
| Sorumlu / Termin | Operasyon Müdürü / 2026-10-31 |

---

## 7. Tatbikat başarı kriteri

**Zayıf:** "Tatbikat başarıyla tamamlandı."

**Güçlü:**
> **Doğrulanacak hedef:** F-07 faaliyetinin manuel süreçle 8 saatlik RTO içinde
> MBCO seviyesine (150 sevkiyat/gün) ulaşabildiğini doğrulamak.
>
> **Başarı kriteri:** (a) manuel kuyruk 30 dakika içinde devreye alınır;
> (b) 8 saat içinde en az 150 sevkiyat işlenir; (c) çağrı ağacında tüm kritik
> roller 20 dakika içinde ulaşılır.
>
> **Sonuç:** Kısmen başarılı. (a) 22 dk ✓ · (b) 8 saatte 131 sevkiyat ✗ ·
> (c) 2 rol ulaşılamadı (yedek telefon güncel değil) ✗
>
> **Boşluklar:** manuel süreç kapasitesi yetersiz — ek çapraz eğitim gerekli
> (DÖF-2026-014); iletişim listesi güncel değil (DÖF-2026-015).

Başarısız tatbikat kötü haber değildir — **tatbikat yapılmaması** kötü haberdir.
Bulgu üreten ve DÖF'e bağlanan bir tatbikat, sistemin çalıştığının kanıtıdır.
Bunu kullanıcıya da söyle: her tatbikatı "başarılı" gösteren kayıt inandırıcı değildir.

---

## 8. `[DOLDURULACAK]` ve `[ÖRNEK]` kullanımı

- `[DOLDURULACAK: TMS sağlayıcısının sözleşmedeki kurtarma SLA süresi]` — bilmediğin
  ama kullanıcının bildiği bilgi.
- `[ÖRNEK — doğrulanacak]` — senin ürettiğin, kuruluşun teyit etmesi gereken varsayım.

22301'de özellikle dikkat: **tatbikat kayıtları, olay kayıtları ve iletişim
listeleri uydurulamaz.** Boş şablon üret, örnek satırı açıkça etiketle.

---

## 9. Ton kontrolü

Her plan/dokümanı bitirdiğinde sor:

1. **Kriz anında bu sayfayı okuyacak kişi 30 saniyede ne yapacağını bulabilir mi?**
   Bulamıyorsa fazla anlatısal.
2. **Her adımın sorumlusu ve süresi var mı?**
3. **Bu faaliyetin zinciri BIA'dan tatbikata kadar kapalı mı?**
   Bir halka eksikse denetçi onu bulur.
