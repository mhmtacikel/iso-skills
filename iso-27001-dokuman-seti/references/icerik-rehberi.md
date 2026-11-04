# İçerik Rehberi — Kalite Çıtası ve Örnek Metinler

## İçindekiler

- 1. Kapsam beyanı
- 2. Politika ilkesi
- 3. Sorumluluk tanımı
- 4. Prosedür süreç tablosu
- 5. Risk kaydı
- 6. SoA gerekçesi
- 7. Hedef
- 8. `[DOLDURULACAK]` kullanımı
- 9. Ton kontrolü

Bu dosya "nasıl yazılacağını" örnekle gösterir. Doküman iskeletleri
`dokuman-mimarisi.md` §5'te; burada **metnin kendisi** var.

Kural şu: her örneğin bir zayıf, bir güçlü sürümü verilmiştir. Zayıf sürümler
gerçek denetimlerde bulgu almış kalıplardır — tanıyıp kaçınman için buradalar.

---

## 1. Kapsam beyanı

**Zayıf:**
> Şirketimizin tüm faaliyetleri BGYS kapsamındadır.

Neden bulgu alır: hangi tüzel kişilik, hangi lokasyon, hangi faaliyet belirsiz.
Sertifikaya bu cümle yazılamaz. 4.3 c) arayüz ve bağımlılıklar yok.

**Güçlü:**
> Bu bilgi güvenliği yönetim sistemi, ACME Yazılım A.Ş.'nin İstanbul Ataşehir
> (Merkez Ofis, Barbaros Mah. …) ve Ankara Teknokent (Ar-Ge Ofisi, …)
> lokasyonlarında yürüttüğü bulut tabanlı insan kaynakları yazılımı (ACME HRM)
> hizmetinin geliştirilmesi, işletilmesi, müşteri desteği ve bu faaliyetleri
> destekleyen bilgi teknolojileri, insan kaynakları ve satın alma süreçlerini
> kapsar.
>
> **Kapsam dışı:** İzmir Satış Ofisi, yalnızca satış öncesi görüşme yürüttüğü ve
> müşteri üretim verisine erişimi bulunmadığı için kapsam dışında tutulmuştur.
>
> **Arayüzler ve bağımlılıklar (4.3 c):** Üretim altyapısı AWS eu-central-1
> bölgesinde barındırılmakta olup fiziksel ve altyapı katmanı güvenliği
> paylaşılan sorumluluk modeli çerçevesinde AWS tarafından sağlanmaktadır;
> ilgili kontroller BGYS-PL-06 ve tedarikçi değerlendirmesiyle yönetilir.
> Bordro işlemleri XYZ Mali Müşavirlik tarafından yürütülmekte olup veri
> aktarımı BGYS-PR-11 kapsamındadır.
>
> Uygulanabilirlik Bildirgesi BGYS-LS-02 Rev. 01 geçerlidir.

---

## 2. Politika ilkesi

**Zayıf:**
> Bilgilerimizin gizliliği, bütünlüğü ve erişilebilirliği önemlidir ve korunur.

Neden bulgu alır: taahhüt değil temenni. Kim, neye göre, hangi sonuçla?

**Güçlü:**
> Bilgi varlıklarımız BGYS-PL-04 uyarınca dört seviyede sınıflandırılır ve her
> seviye için tanımlı asgari koruma önlemleri uygulanır. Sınıflandırma
> yapılmamış bilgi "İç Kullanım" kabul edilir. Bu ilkeye uyum, altı ayda bir
> yapılan uyum gözden geçirmesiyle (BGYS-PR-13) ölçülür ve sonuçları Yönetimin
> Gözden Geçirmesi'ne girdi oluşturur.

---

## 3. Sorumluluk tanımı

**Zayıf:**
> Yedekleme düzenli olarak yapılır.

Üç hata: özne yok, sıklık belirsiz, doğrulama yok. Denetçi "kim yapıyor,
ne sıklıkla, yapıldığını nasıl biliyorsunuz?" diye sorar; cevap dokümanda yok.

**Güçlü:**
> Üretim veritabanlarının tam yedeği Sistem Yöneticisi tarafından her gün
> 02:00'de otomatik olarak alınır; artımlı yedek altı saatte bir çalışır.
> Yedekleme işlerinin başarı durumu her sabah 09:00'da Sistem Yöneticisi
> tarafından kontrol edilir ve başarısız iş aynı gün içinde BGYS-FR-11 ile
> kayıt altına alınır. Geri yükleme testi üç ayda bir yapılır; test sonucu
> BGYS-PR-18 Ek-1 formuna işlenir ve BT Müdürü tarafından onaylanır.

---

## 4. Prosedür süreç tablosu

Prosedürün gövdesi bu tablo olmalı. Denetçi akışı buradan okur:

| Adım | Faaliyet | Sorumlu | Girdi | Çıktı / Kayıt | Süre |
|---|---|---|---|---|---|
| 1 | Erişim talebi oluşturulur | Talep eden yönetici | Personel bilgisi, gerekçe | BGYS-FR-05 (elektronik) | — |
| 2 | Talep, en az yetki ilkesi açısından değerlendirilir | Varlık Sahibi | BGYS-FR-05, rol-yetki matrisi | Onay/ret kaydı | 2 iş günü |
| 3 | Ayrıcalıklı yetki talebi ise ek onay alınır | BT Müdürü | Adım 2 çıktısı | İkinci onay kaydı | 1 iş günü |
| 4 | Yetki sistemde tanımlanır | Sistem Yöneticisi | Onaylı talep | Sistem log kaydı, kapatılan talep | 1 iş günü |
| 5 | Tanımlama talep edene ve kullanıcıya bildirilir | Sistem Yöneticisi | — | Bildirim e-postası | Aynı gün |

Ardından mutlaka:

> **Ölçüm ve izleme (9.1):** Bu sürecin performansı iki göstergeyle izlenir:
> (a) talep kapatma süresi ortalaması — hedef ≤ 3 iş günü, aylık ölçülür;
> (b) üç aylık erişim gözden geçirmesinde tespit edilen gereksiz yetki sayısı —
> hedef ≤ 5. Sonuçlar BGYS-FR-04'e işlenir.

---

## 5. Risk kaydı

**Zayıf:**
> R-001 | Siber saldırı | Yüksek | Güvenlik duvarı var

Varlık yok, tehdit ve açıklık ayrışmamış, sahibi yok, işleme kararı yok.

**Güçlü:**

| Alan | Değer |
|---|---|
| Risk No | R-014 |
| Varlık / Süreç | ACME HRM müşteri veritabanı (VE-003) |
| Varlık Sahibi | Ürün Müdürü |
| Tehdit | Dışarıdan yetkisiz erişim yoluyla müşteri kişisel verilerinin ele geçirilmesi |
| Açıklık | Uygulama katmanında çok faktörlü kimlik doğrulama yalnızca yönetici hesaplarında etkin |
| Mevcut kontroller | WAF, parola politikası, günlük kayıt tutma |
| Olasılık / Etki | 3 / 5 → Skor 15 (Yüksek) |
| Risk Sahibi | Bilgi Teknolojileri Müdürü |
| İşleme seçeneği | Azalt |
| Planlanan kontroller | A.8.5 (tüm kullanıcılarda MFA), A.5.18 (üç aylık erişim gözden geçirme), A.8.16 (anormal oturum uyarısı) |
| Aksiyon sorumlusu / Termin | Sistem Yöneticisi / 2026-11-30 |
| Artık risk | 2 × 5 = 10 (Orta) |
| Risk sahibi onayı | Onaylandı — 2026-08-11 |

Dikkat: **tehdit ile açıklık ayrı sütunlardır.** "Siber saldırı" tehdittir;
onu mümkün kılan eksiklik açıklıktır. Bu ayrımı yapmayan risk envanteri
6.1.2 c) gerekliliğini karşılamaz ve denetçinin ilk yakaladığı şeydir.

---

## 6. SoA gerekçesi

**Zayıf:** "Gerekli" / "Standart gereği" / boş

**Güçlü — dahil etme:**
> R-014 ve R-021 numaralı riskler ile 6698 sayılı KVKK madde 12 kapsamındaki
> veri güvenliği yükümlülüğü gereği uygulanmaktadır.

**Güçlü — hariç tutma:**
> Kuruluş yazılım geliştirme faaliyeti yürütmemekte, tüm uygulamalar hazır ticari
> ürün olarak temin edilmektedir; kaynak koda erişim bulunmadığından bu kontrol
> uygulanabilir değildir. Tedarik edilen yazılımların güvenliği A.5.21 ve A.8.30
> kontrolleriyle yönetilmektedir.

Hariç tutma gerekçesi **her zaman** iki şeyi söylemeli: neden uygulanabilir
değil, ve o riskin başka hangi kontrolle karşılandığı. İkincisi olmadan gerekçe
"biz bunu yapmıyoruz" demekten öteye geçmez.

---

## 7. Hedef

**Zayıf:** "Bilgi güvenliği farkındalığını artırmak"

**Güçlü:**

| Alan | Değer |
|---|---|
| Hedef | Oltalama saldırılarına karşı personel direncini artırmak |
| Politika ilkesiyle ilişkisi | BGYS-PL-01 §3.4 (insan faktörü) |
| Gösterge | Çeyreklik oltalama tatbikatında bağlantıya tıklama oranı |
| Ölçüm yöntemi | Simülasyon aracı raporu, tüm kapsam personeli |
| Başlangıç değeri | %23 (2026 Q1) |
| Hedef değer | ≤ %8 (2026 Q4) |
| Ölçüm sıklığı | Üç aylık |
| Sorumlu / Kaynak | BGYS Yöneticisi / simülasyon aracı lisansı, 4 saat eğitim |
| Değerlendirme | Q3 sonunda hedefe ulaşılmazsa hedefli ek eğitim planlanır |

---

## 8. `[DOLDURULACAK]` kullanımı

Bilmediğin bilgiyi uydurma, ama boş da bırakma. Etiketi **ne istendiğini
söyleyecek şekilde** yaz:

- Kötü: `[DOLDURULACAK]`
- İyi: `[DOLDURULACAK: BT biriminin resmî adı ve bağlı olduğu genel müdür yardımcılığı]`
- İyi: `[DOLDURULACAK: 2026 yılı BGYS bütçesi — YGG kararıyla onaylanan tutar]`

Üretim sonunda bunları say ve `OKUBENI.md`'de dosya bazında listele. Kullanıcı
denetime girmeden kaç boşluk kapatması gerektiğini görmeli.

Örnek/varsayım verisi kullandığında ise etiketi ayır:
`[ÖRNEK — kuruluş tarafından doğrulanacak]`. Bu ikisini karıştırma; biri eksik
bilgi, diğeri doğrulanmamış varsayım.

---

## 9. Ton kontrolü

Bir dokümanı bitirdiğinde şu üç soruyu sor:

1. **Bu cümleyi başka bir şirkete kopyalasam anlamı değişir mi?** Değişmiyorsa
   fazla jenerik.
2. **Denetçi "kanıtını gösterin" derse ne gösterilecek?** Cevap yoksa o cümle
   ya kanıta bağlanmalı ya çıkarılmalı.
3. **Bu sıklığı/eşiği kim, neye göre belirledi?** Keyfî sayı, sorulduğunda
   savunulamaz. Ya gerekçelendir ya `[DOLDURULACAK]` bırak.
