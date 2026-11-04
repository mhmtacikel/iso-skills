# ISO/IEC 27701:2025 — Madde Yapısı ve Doküman Listesi

## İçindekiler

- 1. Madde yapısı
  - Madde 4 — Kuruluşun bağlamı
  - Madde 5 — Liderlik
  - Madde 6 — Planlama
  - Madde 7 — Destek
  - Madde 8 — İşletim
  - Madde 9 — Performans değerlendirmesi
  - Madde 10 — İyileştirme
- 2. Doküman listesi (2025)
  - 00 — Kapsam ve çerçeve
  - 01 — Politikalar
  - 02 — Prosedürler
  - 03 — Envanterler ve kayıtlar (Excel)
  - 04 — Formlar ve planlar
  - 07 — Denetim hazırlık
- 3. Sayısal beklenti

**Bu sürüm bağımsız bir yönetim sistemi standardıdır.** ISO/IEC 27001 gerekmez.
Annex SL gövdesini kullanır, yani 27001/22301/42001 ile aynı iskelete oturur ve
entegre kurulum kolaydır.

Tam adı: *Information security, cybersecurity and privacy protection — Privacy
information management systems — Requirements and guidance* (Ekim 2025).

## 1. Madde yapısı

| Madde | İçerik |
|---|---|
| 1–3 | Kapsam, atıflar, terimler ve tanımlar |
| **4** | **Kuruluşun bağlamı** — 4.1 bağlam, 4.2 ilgili taraflar, 4.3 kapsam, 4.4 KVYS |
| **5** | **Liderlik** — 5.1 liderlik ve taahhüt, 5.2 politika, 5.3 roller |
| **6** | **Planlama** — 6.1 risk ve fırsatlar, 6.2 hedefler, 6.3 değişiklikler |
| **7** | **Destek** — 7.1 kaynaklar, 7.2 yetkinlik, 7.3 farkındalık, 7.4 iletişim, 7.5 dokümante bilgi |
| **8** | **İşletim** — 8.1 planlama ve kontrol, risk değerlendirme ve işleme uygulaması |
| **9** | **Performans değerlendirmesi** — 9.1 izleme/ölçme, 9.2 iç tetkik, 9.3 YGG |
| **10** | **İyileştirme** — uygunsuzluk, düzeltici faaliyet, sürekli iyileştirme |
| Ek A (normatif) | A.1 veri sorumlusu (31), A.2 veri işleyen (18), A.3 bilgi güvenliği (29) |
| Ek B (normatif) | A.1/A.2/A.3 için uygulama kılavuzu (B.1 / B.2 / B.3) |
| Ek C | ISO/IEC 29100 gizlilik çerçevesi eşlemesi |
| Ek D | GDPR eşlemesi |
| Ek E | ISO/IEC 27018 ve ISO/IEC 29151 eşlemesi |
| Ek F | ISO/IEC 27701:2019 eşlemesi (geçiş için) |

**Ek B normatiftir** — yani "isteğe bağlı öneri" değildir. Kontrolleri
uygularken B.1/B.2/B.3'teki kılavuza uyulması beklenir.

### Madde 4 — Kuruluşun bağlamı

| Alt madde | Gereklilik | Doküman | Denetçi ne sorar |
|---|---|---|---|
| 4.1 | İç ve dış hususlar; **kuruluşun rolü** (veri sorumlusu / veri işleyen / her ikisi) | KVYS-FR-00 Rol Beyanı + Bağlam Analizi | "Bu işleme faaliyetinde hangi roldesiniz?" |
| 4.2 | İlgili taraflar ve gereklilikleri — **ilgili kişiler ve denetim otoritesi dahil** | KVYS-LS-05 | "İlgili kişiler listenizde var mı? Beklentileri ne?" |
| 4.3 **Z** | KVYS kapsamı | KVYS-PL-00 | "Hangi işleme faaliyetleri kapsam dışı, neden?" |
| 4.4 | KVYS'nin kurulması ve sürekli iyileştirilmesi | KVYS-EK-01 | "Süreç haritanız?" |

### Madde 5 — Liderlik

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 5.1 | Üst yönetimin liderlik ve taahhüdü | YGG tutanakları, bütçe, kaynak kararları |
| 5.2 **Z** | **Kişisel veri koruma politikası** — amaca uygun, hedeflere çerçeve, uygulanabilir gereklilikleri karşılama ve sürekli iyileştirme taahhüdü; dokümante, duyurulmuş, erişilebilir | KVYS-PL-01 |
| 5.3 | Roller, sorumluluklar ve yetkiler | Görev tanımları; KVKK irtibat kişisi ataması |

### Madde 6 — Planlama

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 6.1 **Z** | Risk ve fırsatlar; risk değerlendirme ve işleme; **Ek A ile karşılaştırma**; **SoA** | KVYS-FR-05 Risk Envanteri + KVYS-LS-11 SoA |
| 6.2 **Z** | Kişisel veri koruma hedefleri — ölçülebilir, izlenen, duyurulan | KVYS-FR-04 |
| 6.3 | Değişikliklerin planlı yapılması | KVYS-PR-12 |

**İki risk boyutu:** Risk değerlendirmesi hem kuruluşa yönelik riski hem
**ilgili kişiye yönelik riski** kapsamalıdır. Bunlar farklı sorulardır ve
farklı önlemler doğurur. Risk envanterinde ayrı sütun aç:

- *Kuruluşa etki* — yaptırım, itibar, operasyon, sözleşme kaybı
- *İlgili kişiye etki* — mahremiyet ihlali, ayrımcılık, maddi kayıp, itibar,
  kontrol kaybı

Gizlilik etki değerlendirmesi (DPIA) ikinci boyutun derinleştirilmiş hâlidir
ve eşik kriterlerini karşılayan faaliyetler için ayrıca yapılır.

### Madde 7 — Destek

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 7.1 | Kaynaklar | Bütçe, kadro |
| 7.2 **Z** | Yetkinlik ve **yetkinlik kanıtı** | KVYS-LS-12 Yetkinlik Matrisi |
| 7.3 | Farkındalık | KVYS-PN-02 |
| 7.4 | İletişim — iç ve dış; **ilgili kişilerle iletişim** dahil | KVYS-PN-04 |
| 7.5 **Z** | Dokümante bilgi: oluşturma, güncelleme, kontrol | KVYS-PR-14 |

Yetkinlik matrisinde kişisel veri koruma yetkinliği ayrı izlenmeli: hukuki
bilgi (KVKK), teknik bilgi (anonimleştirme, şifreleme), süreç bilgisi.

### Madde 8 — İşletim

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 8.1 **Z** | İşletim planlama ve kontrol; kriterler; dış kaynaklı proseslerin kontrolü | Prosedürler + tedarikçi yönetimi |
| 8.x **Z** | Risk değerlendirmesinin ve risk işleme planının uygulanması; **sonuçların kaydı** | KVYS-FR-05, KVYS-FR-03 DPIA |

### Madde 9 — Performans değerlendirmesi

| Alt madde | Gereklilik | Doküman |
|---|---|---|
| 9.1 **Z** | Ne izlenecek, yöntem, ne zaman, kim; **sonuçların kaydı** | KVYS-FR-04 + periyodik raporlar |
| 9.2 **Z** | İç tetkik ve program; tarafsızlık | KVYS-PR-15 + KVYS-PN-03 |
| 9.3 **Z** | YGG girdileri ve kararları | KVYS-FR-06 |

YGG girdilerine 27701'e özgü başlıklar eklenmeli: ilgili kişi başvuru
istatistikleri ve süre uyumu, veri ihlalleri ve Kurul bildirimleri, DPIA
sonuçları, mevzuat değişiklikleri, aktarım değişiklikleri.

### Madde 10 — İyileştirme

Uygunsuzluk ve düzeltici faaliyet (kök neden, benzerinin araştırılması,
etkinlik doğrulama) + sürekli iyileştirme. Kaynaklar arasına **ilgili kişi
şikâyetleri** ve **Kurul kararları** eklenmeli.

---

## 2. Doküman listesi (2025)

`Z` = zorunlu dokümante bilgi. Sade set: az sayıda işleme faaliyeti, tek rol,
< 50 çalışan.

### 00 — Kapsam ve çerçeve

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| KVYS-PL-00 | KVYS Kapsam Dokümanı | Word | **4.3 Z** | Z | Z |
| KVYS-EK-01 | KVYS El Kitabı | Word | 4.4 | U | U |
| KVYS-FR-00 | Rol Belirleme Beyanı ve Bağlam Analizi | Word | **4.1** | Z | Z |
| KVYS-LS-05 | İlgili Taraflar Analizi (ilgili kişi dahil) | Excel | 4.2 | U | U |

### 01 — Politikalar

| Kod | Doküman | Format | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|---|
| KVYS-PL-01 | Kişisel Veri Koruma Politikası | Word | **5.2 Z** | Z | Z |
| KVYS-PL-02 | Veri İşleyen Politikası | Word | A.2.2 | işleyen ise | işleyen ise |
| KVYS-PL-03 | Bilgi Güvenliği Politikası | Word | **A.3.3** | Z | 27001 varsa atıf |
| KVYS-PL-04 | Bilgi Sınıflandırma Politikası | Word | A.3.5–A.3.6 | U | U |
| KVYS-PL-05 | Kabul Edilebilir Kullanım / Temiz Masa | Word | A.3.19 | U | birleşir |
| KVYS-PL-06 | Uç Nokta Güvenliği Politikası | Word | A.3.22 | U | birleşir |
| KVYS-PL-07 | Kriptografi Politikası | Word | A.3.26 | U | U |
| KVYS-PL-08 | Test Verisi ve Maskeleme Politikası | Word | A.3.31 | U | — |
| KVYS-LS-02 | Kişisel Veri Saklama ve İmha Politikası | Word + Excel | A.1.4.8–A.1.4.9 | Z | Z |

**27001 belgesi olan kuruluşta** PL-03…PL-08'i yeniden yazma; mevcut BGYS
politikalarına atıf ver ve SoA'nın "uygulayan doküman" sütununa BGYS kodlarını
yaz. A.3 kontrolleri bu şekilde karşılanır.

### 02 — Prosedürler

| Kod | Doküman | Format | Kontrol / Madde | Tam | Sade |
|---|---|---|---|---|---|
| KVYS-PR-01 | Kişisel Veri İşleme Envanteri Yönetimi | Word | A.1.2.9 / A.2.2.7 | Z | Z |
| KVYS-PR-02 | Rıza Yönetimi Prosedürü | Word | A.1.2.4–A.1.2.5, A.1.3.5 | Z | sorumlu ise |
| KVYS-PR-03 | Gizlilik Etki Değerlendirme (DPIA) Prosedürü | Word | **A.1.2.6** | Z | Z |
| KVYS-PR-04 | İlgili Kişi Başvuru Prosedürü | Word | A.1.3.2–A.1.3.10 / A.2.3.2 | Z | Z |
| KVYS-PR-05 | Veri Kalitesi Prosedürü | Word | A.1.4.4 | U | birleşir |
| KVYS-PR-06 | Saklama ve İmha Prosedürü | Word | A.1.4.6–A.1.4.9 | Z | Z |
| KVYS-PR-07 | Kişisel Veri Aktarım Prosedürü | Word | A.1.4.10, A.1.5.x, A.3.7 | Z | Z |
| KVYS-PR-08 | Talimat Değerlendirme Prosedürü | Word | A.2.2.5 | işleyen ise | işleyen ise |
| KVYS-PR-09 | Sözleşme Sonu İade/İmha Prosedürü | Word | A.2.4.3 | işleyen ise | işleyen ise |
| KVYS-PR-10 | Yasal Talep ve İfşa Prosedürü | Word | A.2.5.5–A.2.5.6 | işleyen ise | işleyen ise |
| KVYS-PR-11 | Alt Yüklenici / Tedarikçi Yönetimi | Word | A.2.5.7–A.2.5.9, A.3.10, A.3.30 | Z | Z |
| KVYS-PR-12 | Değişiklik Yönetimi Prosedürü | Word | 6.3 | U | birleşir |
| KVYS-PR-13 | Veri İhlali Yönetim Prosedürü | Word | **A.3.11–A.3.12** | Z | Z |
| KVYS-PR-14 | Doküman ve Kayıt Kontrol Prosedürü | Word | **7.5 Z**, A.3.14 | Z | Z |
| KVYS-PR-15 | İç Tetkik ve YGG Prosedürü | Word | **9.2, 9.3 Z**, A.3.15 | Z | Z |
| KVYS-PR-16 | Uygunsuzluk ve Düzeltici Faaliyet | Word | **10 Z**, A.3.16 | Z | Z |
| KVYS-PR-12b | Erişim ve Kimlik Yönetimi | Word | A.3.8–A.3.9, A.3.23 | Z | 27001 varsa atıf |
| KVYS-PR-17 | Ortam Yönetimi ve Güvenli İmha | Word | A.3.20–A.3.21 | U | 27001 varsa atıf |
| KVYS-PR-18 | Yedekleme Prosedürü | Word | A.3.24 | U | 27001 varsa atıf |
| KVYS-PR-19 | Log Yönetimi ve İzleme | Word | A.3.25 | U | 27001 varsa atıf |
| KVYS-PR-20 | Güvenli Geliştirme Prosedürü | Word | A.3.27–A.3.29 | geliştirme varsa | — |

### 03 — Envanterler ve kayıtlar (Excel)

| Kod | Doküman | Kontrol / Madde | Tam | Sade |
|---|---|---|---|---|
| KVYS-LS-01 | **Kişisel Veri İşleme Envanteri** (VERBİS hizalı) | **A.1.2.9 / A.2.2.7 Z** | Z | Z |
| KVYS-LS-11 | **Uygulanabilirlik Bildirgesi (SoA)** | **6.1 Z** | Z | Z |
| KVYS-FR-05 | **Risk Envanteri** (kuruluş + ilgili kişi etkisi) | **6.1, 8 Z** | Z | Z |
| KVYS-FR-03 | **DPIA Kayıtları** | **A.1.2.6 Z** | Z | Z |
| KVYS-LS-03 | KVKK / Mevzuat Uyum Matrisi | A.3.13 | Z | Z |
| KVYS-LS-04 | Yurt Dışı Aktarım Envanteri | A.1.5.x / A.2.5.x | Z | Z |
| KVYS-LS-05 | Rıza Kayıt Defteri | A.1.2.5 | sorumlu ise | sorumlu ise |
| KVYS-LS-06 | İlgili Kişi Başvuru Kayıt Defteri | A.1.3.10 | Z | Z |
| KVYS-LS-07 | İfşa / Paylaşım Kayıt Defteri | A.1.5.5 / A.2.5.4 | U | U |
| KVYS-LS-08 | Veri İşleyen İşleme Kayıtları | A.2.2.7 | işleyen ise | işleyen ise |
| KVYS-LS-09 | Alt Yüklenici Envanteri | A.2.5.7 | işleyen ise | işleyen ise |
| KVYS-LS-10 | Veri İhlali Kayıt Defteri | A.3.11–A.3.12 | Z | Z |
| KVYS-LS-12 | Yetkinlik ve Eğitim Matrisi | **7.2 Z** | Z | Z |
| KVYS-LS-13 | Doküman Ana Listesi | 7.5 | U | U |
| KVYS-FR-04 | KVYS Hedefleri ve İzleme Tablosu | **6.2, 9.1 Z** | Z | Z |
| KVYS-FR-10 | Otomatik Karar Envanteri | A.1.3.11 | varsa | varsa |

### 04 — Formlar ve planlar

| Kod | Doküman | Format | Kontrol |
|---|---|---|---|
| KVYS-FR-01 | Aydınlatma Metinleri (grup bazında ayrı) | Word | A.1.3.3–A.1.3.4 |
| KVYS-FR-02 | Açık Rıza Metni | Word | A.1.2.5 |
| KVYS-FR-06 | Yönetimin Gözden Geçirmesi Formu | Word | **9.3 Z** |
| KVYS-FR-07 | Uygunsuzluk ve DÖF Takip Formu | Excel | **10 Z** |
| KVYS-FR-08 | Veri İşleyen Sözleşme Eki | Word | A.1.2.7 |
| KVYS-FR-09 | Ortak Veri Sorumlusu Mutabakatı | Word | A.1.2.8 |
| KVYS-FR-11 | Veri İşleyen Hizmet Sözleşmesi | Word | A.2.2.2 |
| KVYS-FR-12 | Müşteri Bilgilendirme Formu | Word | A.2.2.6 |
| KVYS-FR-13 | Gizlilik Taahhütnamesi | Word | A.3.18 |
| KVYS-FR-14 | Veri İhlali Bildirim Formu (iç + Kurul) | Word | A.3.11–A.3.12 |
| KVYS-FR-15 | İç Tetkik Soru Listesi ve Bulgu Formu | Excel | 9.2 |
| KVYS-PN-02 | Farkındalık ve Eğitim Planı | Word + Excel | 7.3, A.3.17 |
| KVYS-PN-03 | Yıllık İç Tetkik Programı | Excel | **9.2 Z** |
| KVYS-PN-04 | İletişim Planı | Word | 7.4 |

### 07 — Denetim hazırlık

| Kod | Dosya | İçerik |
|---|---|---|
| KVYS-RP-01 | Kontrol-Kanıt Matrisi | Kontrol → doküman → kanıt → sorumlu → durum |
| KVYS-RP-02 | Öz Değerlendirme | Madde ve kontrol bazlı uygunluk |
| KVYS-RP-03 | Envanter Zincir Kontrolü | Faaliyet → hukuki sebep → saklama → aydınlatma → DPIA |
| — | OKUBENI.md | Ne üretildi, ne eksik, sonraki adımlar |

---

## 3. Sayısal beklenti

| Senaryo | Word | Excel | Toplam |
|---|---|---|---|
| 27001 belgeli, yalnız sorumlu (sade) | ~16 | ~11 | ~27 |
| 27001 belgeli, her iki rol | ~22 | ~14 | ~36 |
| 27001 yok, bağımsız, her iki rol (tam) | ~34 | ~16 | ~50 |

Son satır en büyüğüdür çünkü A.3'ün 29 bilgi güvenliği kontrolü için doküman
üretmek gerekir. 27001 belgesi varsa bu yük büyük ölçüde ortadan kalkar —
kullanıcıya bunu söyle, gereksiz doküman üretme.
