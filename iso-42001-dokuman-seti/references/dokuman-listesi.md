# ISO/IEC 42001:2023 — Üretilecek Doküman Listesi

## İçindekiler

- 00 — Kapsam ve El Kitabı
- 01 — Politikalar
- 02 — Prosedürler
- 03 — Envanterler ve Değerlendirmeler (Excel)
  - YZ Sistem Envanterinin zorunlu sütunları
  - Etki Değerlendirmesinin yapısı
- 04 — Formlar ve Planlar
- Yaşam döngüsü kontrol noktaları (YZYS-PN-01)
- 07 — Denetim Hazırlık
- Sayısal beklenti

`Z` = zorunlu dokümante bilgi. `U` = denetimde beklenen.
Sade set: az sayıda YZ sistemi, çoğunlukla üçüncü taraf kullanıcı rolü.

---

## 00 — Kapsam ve El Kitabı

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| YZYS-EK-01 | YZYS El Kitabı | Word | 4.4 | U | U |
| YZYS-PL-00 | YZYS Kapsam Dokümanı | Word | **4.3 Z** | Z | Z |
| YZYS-FR-01 | Bağlam Analizi ve YZ Rol Tanımı | Word | 4.1 | U | U |
| YZYS-LS-05 | İlgili Taraflar ve Etkilenen Gruplar Analizi | Excel | 4.2 | U | U |

Bağlam analizinde **kuruluşun YZ rolü** (geliştirici/sağlayıcı/kullanıcı) sistem
bazında tanımlanmalı. İlgili taraflar listesinde **kararın muhatabı olan kişiler**
mutlaka yer almalı — 42001'in ayırt edici beklentisi budur.

---

## 01 — Politikalar

| Kod | Doküman | Format | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|---|
| YZYS-PL-01 | **YZ Politikası** | Word | **5.2 Z**, A.2.2–A.2.4 | Z | Z |
| YZYS-PL-02 | Sorumlu YZ Geliştirme İlkeleri ve Hedefleri | Word | A.6.1.2 | U | geliştirici ise |
| YZYS-PL-03 | Sorumlu YZ Kullanım Politikası | Word | A.9.2, A.9.3 | U | U |
| YZYS-PL-04 | YZ Veri Yönetişimi Politikası | Word | A.7.2 | U | U |
| YZYS-LS-08 | Politika Uyum Matrisi (diğer kurumsal politikalarla) | Excel | **A.2.3** | U | U |

Politika uyum matrisi küçük ama yüksek getirili bir çıktı: bilgi güvenliği,
KVKK, kalite ve etik politikalarıyla çelişki taramasını görünür kılar (A.2.3).

---

## 02 — Prosedürler

| Kod | Doküman | Format | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|---|
| YZYS-PR-01 | YZ Risk Yönetimi Prosedürü (metodoloji) | Word | **6.1.2, 6.1.3 Z** | Z | Z |
| YZYS-PR-02 | **YZ Sistemi Etki Değerlendirme Prosedürü** | Word | **6.1.4, 8.4 Z**, A.5.2 | Z | Z |
| YZYS-PR-03 | Sorumlu Tasarım ve Geliştirme Prosedürü | Word | A.6.1.3, A.6.2.2, A.6.2.3 | U | geliştirici ise |
| YZYS-PR-04 | Doğrulama ve Geçerleme (V&V) Prosedürü | Word | A.6.2.4 | U | geliştirici ise |
| YZYS-PR-05 | Devreye Alma Prosedürü | Word | A.6.2.5 | U | U |
| YZYS-PR-06 | İşletim, İzleme ve Olay Günlüğü Prosedürü | Word | A.6.2.6, A.6.2.8 | U | U |
| YZYS-PR-07 | Veri Yönetişimi Prosedürü | Word | **A.7.2–A.7.6** | U | U |
| YZYS-PR-08 | Şeffaflık ve Raporlama Prosedürü | Word | A.8.3, A.8.5 | U | U |
| YZYS-PR-09 | Endişe Bildirim Prosedürü | Word | **A.3.3** | U | U |
| YZYS-PR-10 | YZ Olay Yönetimi Prosedürü | Word | A.8.4 | U | U |
| YZYS-PR-11 | Sorumlu Kullanım ve İnsan Gözetimi Prosedürü | Word | A.9.2 | U | U |
| YZYS-PR-12 | Üçüncü Taraf ve Model Sağlayıcı Yönetimi Prosedürü | Word | **A.10.2–A.10.4** | U | U |
| YZYS-PR-13 | Değişiklik Yönetimi Prosedürü (**altı unsur**) | Word | 6.3, 8.1 | U | U |
| YZYS-PR-14 | Doküman ve Kayıt Kontrol Prosedürü | Word | **7.5 Z** | Z | Z |
| YZYS-PR-15 | İç Tetkik ve YGG Prosedürü | Word | **9.2, 9.3 Z** | Z | Z |
| YZYS-PR-16 | Uygunsuzluk ve Düzeltici Faaliyet Prosedürü | Word | **10.2 Z** | Z | Z |

A.3.3 endişe bildirimi (raising concerns) 42001'e özgüdür: çalışanların bir YZ
sistemiyle ilgili kaygılarını misilleme korkusu olmadan bildirebileceği bir kanal
gerekir. Küçük bir prosedür ama denetçi bunu sorar.

---

## 03 — Envanterler ve Değerlendirmeler (Excel)

| Kod | Doküman | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|
| YZYS-LS-04 | **YZ Sistem Envanteri** | 4.3, 8.1 | Z | Z |
| YZYS-FR-03 | **YZ Risk Envanteri ve Risk İşleme Planı** | **6.1.2, 6.1.3, 8.2, 8.3 Z** | Z | Z |
| YZYS-LS-01 | **Uygulanabilirlik Bildirgesi (SoA)** | **6.1.3 Z** | Z | Z |
| YZYS-FR-04 | **YZ Sistemi Etki Değerlendirmesi** | **6.1.4, 8.4 Z** | Z | Z |
| YZYS-LS-03 | Veri Kaynakları ve Köken Envanteri | **A.4.3, A.7.3, A.7.5** | U | U |
| YZYS-LS-02 | YZ Kaynak Envanteri (araç, donanım, hesaplama) | A.4.2, A.4.4, A.4.5 | U | birleşir→LS-04 |
| YZYS-LS-06 | Üçüncü Taraf ve Model Sağlayıcı Envanteri | A.10.3 | U | U |
| YZYS-LS-07 | Yetkinlik ve Eğitim Matrisi | **7.2 Z**, A.4.6 | Z | Z |
| YZYS-LS-09 | Doküman Ana Listesi | 7.5.3 | U | U |
| YZYS-LS-10 | **Yasal Uyum ve Yükümlülük Matrisi** | 4.1, 4.2, A.2.3, A.10.2 | U | U |

`YZYS-LS-10` yasal yükümlülükleri 42001 dokümanlarından **ayrı** izler. Yapısı,
doldurma kuralları ve "uydurma yasak" listesi için `mevzuat-kesisimi.md` §4.
Bu matris bir hukuki görüş değildir; her satırın hukuk birimince doğrulanması
gerekir ve matriste bunun için ayrı bir sütun bulunur.

### YZ Sistem Envanterinin zorunlu sütunları

```
Sistem No | Sistem Adı | Sağlayıcı | Kuruluşun YZ Rolü (sağlayıcı/üretici/
müşteri/ortak) | Önemli Değişiklik Yapıldı mı? | Model Tipi | Teknik Yaklaşım |
Uygulama Alanı | Amaçlanan Kullanım | Öngörülebilir Amaç Dışı Kullanım |
Yasak Kullanım | Kullanıcı Grubu | Etkilenen Kişi Grubu | Karar Özerkliği
(destekleyici/tamamlayıcı/otonom) | İşlenen Veri Tipleri | Kişisel Veri |
Özel Nitelikli Veri | Yaşam Döngüsü Aşaması | Sistem Sahibi | Teknik Sahip |
Kritiklik | Risk Kaydı No | Etki Değerlendirmesi No | AB Bağlantısı |
AB YZ Yasası Rolü | AB YZ Yasası Risk Seviyesi | Yasal Uyum Matrisi Ref |
Devreye Alma | Son Gözden Geçirme | Durum
```

**Etkilenen kişi grubu** ile **kullanıcı grubu** ayrı sütunlardır. İşe alım
eleme modelinde kullanıcı İK uzmanı, etkilenen adaydır. Bu ayrımı yapmayan
envanter etki değerlendirmesini besleyemez.

**Üç ayrı sütun gerektiren üç ayrı kavram:**

| Sütun | Ne sorar | Neden ayrı |
|---|---|---|
| Amaçlanan kullanım | Sistem ne için tasarlandı? | A.9.4'ün birinci yarısı |
| **Öngörülebilir amaç dışı kullanım** | Kullanıcı yanlışlıkla veya kaçınılmaz olarak ne yapar? | A.5.3 bunu açıkça ister; "yasak" değil, "beklenen sapma" |
| Yasak kullanım | Ne açıkça yasaklanmıştır? | Politika ve yaptırım tarafı |

**AB YZ Yasası sütunları `[DOLDURULACAK]` bırakılır.** Skill sınıflandırma
yapmaz; sütunu açar ve hukuk birimine devreder — gerekçesi
`mevzuat-kesisimi.md` §3'te.

**"Önemli değişiklik yapıldı mı?" sütunu.** Üçüncü taraf bir modelin kendi
verisiyle ince ayarlanması, amaçlanan kullanımının değiştirilmesi veya kendi
markası altında sunulması kuruluşun rolünü değiştirebilir ve hariç tutulmuş
kontrolleri geri getirebilir. Bu sütun o eşiği görünür kılar.

### Etki Değerlendirmesinin yapısı
Sekiz bölümlü; ayrıntı `etki-degerlendirmesi.md` §3. Excel'de her YZ sistemi
bir satır + ayrıntılı Word raporu şeklinde ikili yapı en kullanışlısıdır.

---

## 04 — Formlar ve Planlar

| Kod | Doküman | Format | Madde / Kontrol |
|---|---|---|---|
| YZYS-FR-02 | YZ Hedefleri ve İzleme Tablosu (adillik metrikleri dahil) | Excel | **6.2, 9.1 Z** |
| YZYS-FR-05 | Uygunsuzluk ve Düzeltici Faaliyet Takip Formu | Excel | **10.2 Z** |
| YZYS-FR-06 | Yönetimin Gözden Geçirmesi Formu | Word | **9.3 Z** |
| YZYS-FR-07 | **Teknik Dokümantasyon / Model Kartı** | Word | **A.6.2.7** |
| YZYS-FR-08 | Veri Kalitesi Değerlendirme Formu | Excel | **A.7.4** |
| YZYS-FR-09 | Kullanıcı Dokümantasyonu ve Sınırlılıklar Beyanı | Word | **A.8.2** |
| YZYS-FR-10 | Amaçlanan Kullanım Beyanı | Word | **A.9.4** |
| YZYS-FR-11 | Müşteri Bilgilendirme ve Yükümlülük Formu | Word | A.10.4 |
| YZYS-FR-12 | YZ Olay Kayıt Formu | Excel | A.8.4 |
| YZYS-FR-13 | Endişe Bildirim Kayıt Formu | Excel | A.3.3 |
| YZYS-FR-14 | İç Tetkik Soru Listesi ve Bulgu Formu | Excel | 9.2 |
| YZYS-PN-01 | Yaşam Döngüsü Yönetim Planı | Word | 8.1, A.6 |
| YZYS-PN-02 | Farkındalık ve Eğitim Planı | Word + Excel | 7.3, A.4.6 |
| YZYS-PN-03 | Yıllık İç Tetkik Programı | Excel | **9.2 Z** |
| YZYS-PN-04 | İletişim Planı | Word | 7.4, A.8.5 |

**Model kartı (FR-07)** A.6.2.7'yi karşılamanın en temiz yoludur. İçermesi
gerekenler: model amacı ve kapsamı, eğitim verisi tanımı, performans metrikleri
ve ölçüm koşulları, bilinen sınırlılıklar, uygun olmayan kullanımlar, adillik
değerlendirmesi, sürüm ve tarih, iletişim noktası.

A.6.2.7 teknik dokümantasyonun **her ilgili taraf kategorisi için ayrı**
belirlenmesini ve o tarafın ihtiyacına uygun formatta sunulmasını ister. Tek bir
model kartı üç farklı muhataba (son kullanıcı · kurumsal müşteri · denetim
otoritesi) aynı anda hitap etmeyebilir. Pratik çözüm: tek kaynak model kartı +
muhatap bazlı özet çıkarımlar; hangi muhataba hangi sürümün verildiği FR-07'nin
dağıtım tablosunda izlenir.

---

## Yaşam döngüsü kontrol noktaları (YZYS-PN-01)

Yaşam Döngüsü Yönetim Planı, A.6.2 kontrollerini bir zaman eksenine oturtur.
Yedi kontrol noktası, yedi Ek A kontrolüyle birebir eşleşir — plan bu iskelet
üzerine kurulursa A.6.2'nin tamamı tek dokümanda izlenebilir hâle gelir:

| # | Kontrol noktası | Çıktı | Ek A | Kapı kriteri |
|---|---|---|---|---|
| 1 | Gereksinim ve şartname | Gereksinim dokümanı, kabul kriterleri | A.6.2.2 | Amaçlanan kullanım ve veri gereksinimi yazılı mı? |
| 2 | Tasarım ve geliştirme dokümantasyonu | Mimari, model seçim gerekçesi | A.6.2.3 | Tasarım tercihleri gerekçelendirilmiş mi? |
| 3 | Doğrulama ve geçerleme (TEVV) | Test planı, sonuçlar, yanlılık testi | A.6.2.4 | Yayın kriterleri karşılandı mı? Test verisi temsil edici mi? |
| 4 | Devreye alma | Devreye alma planı, onaylar | A.6.2.5 | Onaylar alındı mı, geri alma planı hazır mı? |
| 5 | İşletim ve izleme | İzleme metrikleri, uyarılar, onarım/güncelleme kayıtları | A.6.2.6 | Kayma ve adillik eşikleri tanımlı ve izleniyor mu? |
| 6 | Teknik dokümantasyon | Model/sistem kartı, muhatap bazlı sürümler | A.6.2.7 | Her ilgili taraf kategorisi karşılandı mı? |
| 7 | Olay günlükleri | Log tasarımı, saklama, koruma | A.6.2.8 | Performans aralığı dışı çalışma tespit edilebiliyor mu? |

**Etki değerlendirmesi bu eksene 1. noktada girer, 5. noktada güncellenir.**
Devreye alındıktan sonra yapılan etki değerlendirmesi 6.1.4'ün amacını
karşılamaz — A.5.2 değerlendirmenin "yaşam döngüsü boyunca" yapılmasını ister
ve denetçi ilk değerlendirmenin tarihini devreye alma tarihiyle karşılaştırır.

Kuruluş yalnızca **müşteri** rolündeyse 1–3 noktaları tedarikçi tarafında
gerçekleşir; bu durumda kuruluşun kontrol noktası "tedarikçinin bu adımları
yaptığını doğrulama"ya dönüşür (A.10.3) ve plan buna göre kısalır — ama
silinmez.

---

## 07 — Denetim Hazırlık

| Dosya | İçerik |
|---|---|
| `Madde-Kanit-Matrisi.xlsx` | Madde/kontrol → doküman → kanıt → sorumlu → durum |
| `Cift-Zincir-Kontrolu.xlsx` | Her YZ sistemi için risk + etki zincirinin kapalılığı |
| `Denetim-Soru-Bankasi.xlsx` | **208 denetçi sorusu** — belgelendirme kuruluşu kontrol listesinden; E/H/UD + kanıt + sorumlu + bulgu sütunlu |
| `Oz-Degerlendirme.xlsx` | Madde ve kontrol bazlı uygunluk özeti (soru bankasından türetilir) |
| `OKUBENI.md` | Ne üretildi, ne eksik, sonraki adımlar |

`Denetim-Soru-Bankasi.xlsx`, `assets/denetim_sorulari_42001.json` dosyasından
`scripts/kayitlar_42001.py soru_bankasi` komutuyla üretilir. Bu dosya iki işi
birden görür: **iç tetkik soru listesi** (9.2) ve **belgelendirme öncesi öz
değerlendirme**. Kuruluş bunu doldurduğunda hem 9.2 kanıtı üretmiş hem de
denetimde nerede zorlanacağını önceden görmüş olur.

`Cift-Zincir-Kontrolu.xlsx` bu standarda özgüdür: envanterdeki her sistemin hem
risk hem etki zincirinin tamamlandığını gösterir. Denetçinin yapacağı testtir.

---

## Sayısal beklenti

| Ölçek | Word | Excel | Toplam |
|---|---|---|---|
| Sadeleştirilmiş (üçüncü taraf kullanıcı) | ~16 | ~10 | ~26 |
| Tam set (geliştirici + sağlayıcı) | ~27 | ~15 | ~42 |

Kuruluş yalnızca YZ **kullanıcısı** ise geliştirme prosedürleri (PR-03, PR-04)
ve ilgili Ek A.6 kontrolleri hariç tutulabilir — ama SoA'da gerekçesi yazılmalı.
