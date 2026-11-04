# ISO/IEC 27701:2019 — Madde Yapısı ve Doküman Listesi

**Bu sürüm bir eklentidir.** ISO/IEC 27001 belgesi olmadan 27701:2019
belgelendirmesi yapılamaz. Kullanıcının 27001 belgesi yoksa bunu ilk cümlede
söyle ve iki yol öner: (a) önce 27001, sonra 27701:2019; (b) doğrudan
27701:2025 (bağımsız, 27001 gerektirmez). Çoğu durumda (b) daha mantıklıdır.

## 1. Madde yapısı

| Madde | İçerik | Ne yapar |
|---|---|---|
| 1–3 | Kapsam, atıflar, terimler | Standart girişi |
| 4 | Genel | KVYS'nin 27001/27002 ile ilişkisi, uygulama biçimi |
| **5** | **ISO/IEC 27001 ile ilgili KVYS'ye özgü gereklilikler** | 27001 Madde 4–10'a *eklemeler* |
| **6** | **ISO/IEC 27002 ile ilgili KVYS'ye özgü kılavuz** | 27002 kontrollerine *eklemeler* |
| **7** | **Veri sorumluları için ek kılavuz** | Ek A'daki 31 kontrolün açıklaması |
| **8** | **Veri işleyenler için ek kılavuz** | Ek B'deki 18 kontrolün açıklaması |
| Ek A | Veri sorumlusu kontrol hedefleri ve kontrolleri (31) | SoA'ya girer |
| Ek B | Veri işleyen kontrol hedefleri ve kontrolleri (18) | SoA'ya girer |
| Ek C | ISO/IEC 29100 eşlemesi | Bilgi amaçlı |
| Ek D | GDPR eşlemesi | Bilgi amaçlı |
| Ek E | ISO/IEC 27018 ve 29151 eşlemesi | Bilgi amaçlı |
| Ek F | 27701'in 27001/27002'ye nasıl uygulanacağı | Uygulama kılavuzu |

### Madde 5 — 27001'e eklemeler (alt maddeler)

| 27701 | Karşılık geldiği 27001 maddesi | Eklemenin özü |
|---|---|---|
| 5.2.1 | 4.1 Bağlamı anlama | Kuruluşun **veri sorumlusu ve/veya veri işleyen** rolü belirlenmeli |
| 5.2.2 | 4.2 İlgili taraflar | **İlgili kişiler (veri sahipleri)** ve düzenleyici otorite ilgili taraf olarak eklenir |
| 5.2.3 | 4.3 Kapsam | KVYS kapsamı, kişisel veri işlemeyi içerecek şekilde belirlenir |
| 5.2.4 | 4.4 Yönetim sistemi | BGYS, KVYS'yi içerecek biçimde genişletilir |
| 5.3.1 | 5.1 Liderlik | Kişisel veri koruma taahhüdü eklenir |
| 5.3.2 | 5.2 Politika | Bilgi güvenliği politikası kişisel veri koruma taahhüdünü içerecek şekilde genişletilir |
| 5.3.3 | 5.3 Roller | Kişisel veri koruma rolleri (ör. irtibat kişisi) atanır |
| 5.4.1 | 6.1 Risk ve fırsatlar | Risk değerlendirmesi **ilgili kişiye yönelik riskleri** de kapsar |
| 5.4.2 | 6.2 Hedefler | Kişisel veri koruma hedefleri eklenir |
| 5.5.1–5.5.5 | 7.1–7.5 Destek | Kaynak, yetkinlik, farkındalık, iletişim, dokümante bilgi kişisel veri boyutuyla genişletilir |
| 5.6.1–5.6.3 | 8.1–8.3 İşletim | Risk değerlendirme ve işleme kişisel veri risklerini içerir |
| 5.7.1–5.7.3 | 9.1–9.3 Performans | İzleme, iç tetkik, YGG kişisel veri boyutunu kapsar |
| 5.8.1–5.8.2 | 10.1–10.2 İyileştirme | Uygunsuzluk ve iyileştirme kişisel veri konularını kapsar |

**Kritik nokta 5.4.1:** 27001'in risk değerlendirmesi kuruluşa yönelik riske
bakar; 27701 buna **ilgili kişiye yönelik riski** ekler. İkisi ayrı ayrı
değerlendirilmeli — bu, 2025'teki ayrımın da temelidir.

### Madde 6 — 27002'ye eklemeler

27002:2013'ün eski numaralandırmasıyla (5–18) her kontrol alanına kişisel veri
boyutu eklenir: politikalar, organizasyon, İK güvenliği, varlık yönetimi,
erişim kontrolü, kriptografi, fiziksel güvenlik, işletim, iletişim, tedarik,
ihlal yönetimi, süreklilik, uygunluk.

**Dikkat:** 27701:2019, 27002'nin **2013** sürümünün yapısına göre yazılmıştır.
Kuruluş 27001:2022 / 27002:2022'ye geçtiyse numaralandırma uyuşmaz. Bu durumda
27002:2022'nin eski-yeni eşleme tablosunu kullan ve dokümanda hangi eşlemeyi
kullandığını açıkça belirt. Bu uyumsuzluk 2025 sürümünün çıkış nedenlerinden
biridir; kullanıcıya geçişi düşünmesini önerebilirsin.

---

## 2. Doküman listesi (2019)

`Z` = zorunlu dokümante bilgi. `U` = denetimde beklenen.
27001 setiyle **birlikte** çalışır; 27001 dokümanları (BGYS-xx) tekrar üretilmez,
genişletilir. Ortak dokümanlarda `EYS-` öneki kullanılabilir.

### 00 — Kapsam ve çerçeve

| Kod | Doküman | Format | Madde | Not |
|---|---|---|---|---|
| KVYS-PL-00 | KVYS Kapsam Dokümanı (BGYS kapsamına atıflı) | Word | **5.2.3 Z** | BGYS kapsamını aşamaz |
| KVYS-EK-01 | KVYS El Kitabı / BGYS El Kitabı Eki | Word | 5.2.4 | Mevcut BGYS el kitabına ek bölüm de olabilir |
| KVYS-FR-00 | Rol Belirleme Beyanı (sorumlu/işleyen) | Word | **5.2.1** | Faaliyet bazında rol |
| KVYS-LS-05 | İlgili Taraflar Analizi (ilgili kişi dahil) | Excel | 5.2.2 | BGYS listesine ilgili kişi eklenir |

### 01 — Politikalar

| Kod | Doküman | Format | Madde |
|---|---|---|---|
| KVYS-PL-01 | Kişisel Veri Koruma / Gizlilik Politikası | Word | **5.3.2 Z** |
| KVYS-PL-02 | Veri İşleyen Politikası (işleyen rolü varsa) | Word | 8.2 |
| KVYS-LS-02 | Kişisel Veri Saklama ve İmha Politikası | Word + Excel | 7.4.7–7.4.8 |

BGYS'nin bilgi güvenliği politikası kişisel veri koruma taahhüdünü içerecek
şekilde **revize edilmeli** (5.3.2) — ayrı politika yazmak yetmez, mevcut
politikanın revizyonu da gerekir. Bu, denetimde sıkça atlanan bir noktadır.

### 02 — Prosedürler

| Kod | Doküman | Format | Kontrol |
|---|---|---|---|
| KVYS-PR-01 | Kişisel Veri İşleme Envanteri Yönetim Prosedürü | Word | 7.2.8 / 8.2.6 |
| KVYS-PR-02 | Rıza Yönetimi Prosedürü | Word | 7.2.3, 7.2.4, 7.3.4 |
| KVYS-PR-03 | Gizlilik Etki Değerlendirme (DPIA) Prosedürü | Word | **7.2.5** |
| KVYS-PR-04 | İlgili Kişi Başvuru Prosedürü | Word | 7.3.1–7.3.9 |
| KVYS-PR-05 | Veri Kalitesi Prosedürü | Word | 7.4.3 |
| KVYS-PR-06 | Saklama ve İmha Prosedürü | Word | 7.4.5–7.4.8 / 8.4.1 |
| KVYS-PR-07 | Kişisel Veri Aktarım Prosedürü | Word | 7.4.9, 7.5.x / 8.4.3, 8.5.x |
| KVYS-PR-08 | Talimat Değerlendirme Prosedürü (işleyen) | Word | 8.2.4 |
| KVYS-PR-09 | Sözleşme Sonu İade/İmha Prosedürü (işleyen) | Word | 8.4.2 |
| KVYS-PR-10 | Yasal Talep ve İfşa Prosedürü (işleyen) | Word | 8.5.4–8.5.5 |
| KVYS-PR-11 | Alt Yüklenici Yönetimi Prosedürü (işleyen) | Word | 8.5.6–8.5.8 |
| KVYS-PR-13 | Veri İhlali Yönetim Prosedürü | Word | Madde 6 (ihlal yönetimi eklemesi) |

Doküman kontrol, iç tetkik, YGG, DÖF, yetkinlik prosedürleri **BGYS'den gelir**;
yeniden yazma, kişisel veri boyutunu ekleyecek şekilde revize et.

### 03 — Envanterler ve kayıtlar (Excel)

| Kod | Doküman | Kontrol |
|---|---|---|
| KVYS-LS-01 | **Kişisel Veri İşleme Envanteri** (VERBİS hizalı) | **7.2.8 / 8.2.6 Z** |
| KVYS-LS-11 | **Uygulanabilirlik Bildirgesi (KVYS eki)** | 27001 6.1.3 d) uzantısı |
| KVYS-LS-03 | KVKK / Mevzuat Uyum Matrisi | Madde 6 uygunluk |
| KVYS-LS-04 | Yurt Dışı Aktarım Envanteri | 7.5.x / 8.5.x |
| KVYS-LS-05 | Rıza Kayıt Defteri | 7.2.4 |
| KVYS-LS-06 | İlgili Kişi Başvuru Kayıt Defteri | 7.3.9 |
| KVYS-LS-07 | İfşa / Paylaşım Kayıt Defteri | 7.5.4 / 8.5.3 |
| KVYS-LS-08 | Veri İşleyen İşleme Kayıtları (işleyen) | 8.2.6 |
| KVYS-LS-09 | Alt Yüklenici Envanteri (işleyen) | 8.5.6 |
| KVYS-LS-10 | Veri İhlali Kayıt Defteri | Madde 6 |
| KVYS-FR-10 | Otomatik Karar Envanteri | 7.3.10 |

**SoA notu (2019):** Kuruluşun mevcut BGYS SoA'sı 27001 Ek A'nın 93 kontrolünü
içerir. 27701 için buna Ek A (31) ve/veya Ek B (18) kontrolleri **eklenir**.
İki ayrı SoA yerine tek SoA'nın genişletilmesi tercih edilir; kaynak sütunu
(27001 / 27701) ekleyerek ayır.

### 04 — Formlar

| Kod | Doküman | Format | Kontrol |
|---|---|---|---|
| KVYS-FR-01 | Aydınlatma Metinleri (gruplara göre ayrı) | Word | 7.3.2–7.3.3 |
| KVYS-FR-02 | Açık Rıza Metni | Word | 7.2.4 |
| KVYS-FR-03 | Gizlilik Etki Değerlendirme (DPIA) Formu | Word + Excel | 7.2.5 |
| KVYS-FR-08 | Veri İşleyen Sözleşme Eki | Word | 7.2.6 |
| KVYS-FR-09 | Ortak Veri Sorumlusu Mutabakatı | Word | 7.2.7 |
| KVYS-FR-11 | Veri İşleyen Hizmet Sözleşmesi (işleyen) | Word | 8.2.1 |
| KVYS-FR-12 | Müşteri Bilgilendirme Formu (işleyen) | Word | 8.2.5 |
| KVYS-FR-13 | Gizlilik Taahhütnamesi | Word | Madde 6 (İK) |
| KVYS-FR-14 | Veri İhlali Bildirim Formu (iç + Kurul) | Word | Madde 6 |

### 07 — Denetim hazırlık

| Kod | Dosya | İçerik |
|---|---|---|
| KVYS-RP-01 | Kontrol-Kanıt Matrisi | Kontrol → doküman → kanıt → sorumlu → durum |
| KVYS-RP-02 | Öz Değerlendirme | Madde ve kontrol bazlı uygunluk |
| KVYS-RP-03 | Envanter Zincir Kontrolü | Faaliyet → hukuki sebep → saklama → aydınlatma → DPIA |
| — | OKUBENI.md | Ne üretildi, ne eksik, sonraki adımlar |

---

## 3. Sayısal beklenti

| Rol | Word | Excel | Toplam |
|---|---|---|---|
| Yalnız veri sorumlusu | ~16 | ~9 | ~25 |
| Yalnız veri işleyen | ~14 | ~8 | ~22 |
| Her ikisi | ~22 | ~12 | ~34 |

BGYS dokümanları bu sayıya dahil değildir; 2019'da onlar zaten var kabul edilir.
Var olmayan BGYS dokümanına atıf verme — 27001 seti yoksa kullanıcıya söyle.
