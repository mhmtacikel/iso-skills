# ISO 45001:2018 (+Amd 1:2024) — Üretilecek Doküman Listesi

`Z` = standardın zorunlu kıldığı dokümante bilgi. `U` = denetimde beklenen.
`Y` = Türk mevzuatı gereği zaten bulunması gereken (6331 ve alt mevzuat) — denetçi
45001 maddesi altında bunları da ister, çünkü 6.1.3 yasal şartlara uyumu kapsar.

**Sade set** ne zaman: 50 çalışan altı **ve** az tehlikeli/tehlikeli sınıf, tek lokasyon.
Çok tehlikeli sınıfta çalışan sayısı ne olursa olsun risk, iş izni ve acil durum
prosedürleri ayrı kalır — sadeleştirme bu üçüne dokunmaz.

Kayıtlar (`LS`/`PN` Excel) `scripts/kayitlar_45001.py` ile üretilir; aşağıdaki
kodlar o scriptle **aynı** tutulur. Değiştirirsen ikisini birlikte değiştir.

---

## 00 — Kapsam ve El Kitabı

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSGYS-PL-00 | İSGYS Kapsam Dokümanı | Word | **4.3 Z** | Z | El Kitabı içinde |
| İSGYS-EK-01 | İSGYS El Kitabı (süreç etkileşimi, madde-doküman eşlemesi, ekler: organizasyon şeması, İSG kurulu şeması) | Word | 4.4, 5.3 | U | U |
| İSGYS-LS-03 | İç-Dış Hususlar ve İlgili Taraflar Listesi | Excel | 4.1, 4.2 | U | U |

Kapsam dokümanında: tüzel kişilik, adres(ler), faaliyetler, SGK işyeri sicil no ve
**NACE kodu + tehlike sınıfı**, yükleniciler ve onların faaliyetlerinin kapsamla
ilişkisi. Amd 1:2024 gereği "iklim değişikliği ilgili bir husus mudur" sorusunun
cevabı 4.1'de yazılı olmalı — "ilgili değil" de bir cevaptır ama gerekçeli.

---

## 01 — Politikalar

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| İSGYS-PL-01 | **İSG Politikası** | Word | **5.2 Z** | Z | Z |
| İSGYS-PL-02 | Alkol, Uyuşturucu ve Sigara Politikası | Word | 8.1.2 | sektöre göre | — |
| İSGYS-PL-03 | Psikososyal Riskler ve İşyerinde Şiddet/Mobbing Politikası | Word | 6.1.2.1 (ISO 45003) | U | Politika içinde |

Politika 1 sayfaya sığmalı, üst yönetim imzalı ve tarihli; panoya asılacak sürüm
budur. 14001 ile entegre ise ortak politika `EYS-PL-01` olur.

---

## 02 — Prosedürler

| Kod | Doküman | Madde | Tam | Sade |
|---|---|---|---|---|
| İSGYS-PR-01 | Doküman ve Kayıtların Kontrolü | 7.5 | Z* | Birleşik "Yönetim Sistemi Prosedürü" |
| İSGYS-PR-02 | Bağlam, İlgili Taraflar, Risk ve Fırsatların Yönetimi | 4.1, 4.2, 6.1.1, 6.1.2.3 | U | PR-03 ile birleşik |
| İSGYS-PR-03 | Tehlike Belirleme ve Risk Değerlendirmesi | **6.1.2 Z**, 8.1.2 | Z | Z |
| İSGYS-PR-04 | Yasal ve Diğer Şartlar ve Uygunluk Değerlendirmesi | **6.1.3 Z**, 9.1.2 | Z | Z |
| İSGYS-PR-05 | Çalışanların Danışılması ve Katılımı (İSG Kurulu ve Çalışan Temsilcisi dahil) | **5.4** | U | U |
| İSGYS-PR-06 | Yetkinlik, Eğitim ve Farkındalık | 7.2, 7.3 | U | Birleşik |
| İSGYS-PR-07 | İç ve Dış İletişim | 7.4 | U | Birleşik |
| İSGYS-PR-08 | Operasyonel Kontrol ve İzinli Çalışma (iş izni sistemi) | **8.1 Z** | Z | Z |
| İSGYS-PR-09 | Enerji İzolasyonu — Kilitleme ve Etiketleme | 8.1.2 | makine/enerji varsa | PR-08 eki |
| İSGYS-PR-10 | Değişiklik Yönetimi | **8.1.3** | U | U |
| İSGYS-PR-11 | Satın Alma, Yükleniciler ve Dış Kaynak | **8.1.4** | U | U |
| İSGYS-PR-12 | Acil Durumlara Hazırlık ve Müdahale | **8.2 Z** | Z | Z |
| İSGYS-PR-13 | İzleme, Ölçme ve Performans Değerlendirmesi (periyodik kontrol, ortam ölçümü, sağlık gözetimi) | **9.1 Z** | Z | Birleşik |
| İSGYS-PR-14 | İç Tetkik | **9.2 Z** | Z | Birleşik |
| İSGYS-PR-15 | Yönetimin Gözden Geçirmesi | **9.3 Z** | Z | Birleşik |
| İSGYS-PR-16 | Olay (Kaza, Ramak Kala, Meslek Hastalığı) Bildirimi ve İncelemesi | **10.2 Z** | Z | Z |
| İSGYS-PR-17 | Uygunsuzluk ve Düzeltici Faaliyet | **10.2 Z**, 10.3 | Z | PR-16 ile birleşik |
| İSGYS-PR-18 | Kişisel Koruyucu Donanım Yönetimi | 8.1.2 | U | PR-08 eki |
| İSGYS-PR-19 | Sağlık Gözetimi ve Özel Politika Gerektiren Gruplar | 6.1.2.1, 8.1.2; 6331 m.15 | U | PR-13 içinde |

`*` 7.5 bir prosedür istemez, dokümante bilginin kontrolünü ister; ama 9001/14001
ile ortak çalışan kuruluşlarda tek prosedür en az sürtünmeli yoldur — ve **tek**
olmalı. Mevcut sette birden çok doküman kontrol prosedürü varsa birleştirmek
diğer sistemlerin sahiplerinin onayını gerektirir; bunu OKUBENI'de karar maddesi
olarak yaz, tek taraflı birleştirme.

Sade set: PR-01 + PR-06 + PR-07 + PR-13 + PR-14 + PR-15 → **İSGYS-PR-01 Yönetim
Sistemi Prosedürü**; PR-16 + PR-17 → **İSGYS-PR-16**. Sonuç ≈ 8 prosedür.

---

## 03 — Talimatlar (risk değerlendirmesine göre seçilir — hepsi değil)

Talimat listesi sabit değildir: risk değerlendirmesinde **Önemli** ve üzeri çıkan
her faaliyetin ya bir talimatı ya da iş izni formunda kontrol listesi olmalı.
Tipik katalog:

| Kod | Talimat | Ne zaman |
|---|---|---|
| İSGYS-TL-01 | Genel İSG Kuralları (çalışan, yüklenici, ziyaretçi bölümleriyle) | Her zaman |
| İSGYS-TL-02 | Yüksekte Çalışma | 1 m üstü çalışma, platform, çatı |
| İSGYS-TL-03 | Kapalı / Sınırlı Alanlarda Çalışma | Tank, silo, kuyu, rogar |
| İSGYS-TL-04 | Sıcak İş (kaynak, kesme, taşlama) | Bakım atölyesi, yüklenici işleri |
| İSGYS-TL-05 | Elektrikli Çalışmalar | Pano, trafo, bakım |
| İSGYS-TL-06 | Forklift, Transpalet ve İstif Makinesi Kullanımı | Depo, sevkiyat |
| İSGYS-TL-07 | Kaldırma Ekipmanları (vinç, caraskal, manlift) | |
| İSGYS-TL-08 | Tehlikeli Kimyasallarla Çalışma ve Döküntü Müdahalesi | Kimyasal envanteri boş değilse |
| İSGYS-TL-09 | Elle Taşıma ve Ergonomi | |
| İSGYS-TL-10 | KKD Kullanımı (bölüm-KKD matrisine atıfla) | |
| İSGYS-TL-11 | Kesici Aletler (bıçak, falçata) | Paketleme, depo |
| İSGYS-TL-12 | Basınçlı Kaplar, Kazanlar, Kompresörler | |
| İSGYS-TL-13 | Araç Sürücüleri ve İşyeri İçi Trafik | Lojistik |
| İSGYS-TL-14 | Gece Vardiyasında Kaza ve Acil Durumda Yapılacaklar | Vardiyalı çalışma |
| İSGYS-TL-15 | Patlayıcı Ortam (toz/gaz) Çalışma Kuralları | Toz patlaması riski (un, şeker, kakao, nişasta) |
| İSGYS-TL-2xx | **Makine Güvenlik Talimatı — [makine adı]** (makine başına) | Her üretim makinesi; sıra no makine envanterinden |

Makine talimatları için tek bir **şablon** üret (çalıştırma öncesi kontroller,
güvenli çalıştırma, tehlikeli bölgeler, koruyucular, temizlik/bakımda LOTO,
yasaklar, KKD, acil durdurma), makineleri kullanıcıdan liste olarak al ve yalnız
şablonu + 1 örnek doldurulmuş talimat ver; gerisi kullanıcı verisiyle çoğaltılır.

---

## 04 — Formlar ve Listeler

### Kayıtlar (Excel, `kayitlar_45001.py`)

| Kod | Doküman | Madde | Tam | Sade |
|---|---|---|---|---|
| İSGYS-LS-01 | Tehlike Belirleme ve Risk Değerlendirme Tablosu | 6.1.2 Z | Z | Z |
| İSGYS-LS-02 | İSGYS Risk ve Fırsat Listesi | 6.1.1, 6.1.2.3 | U | U |
| İSGYS-LS-03 | İç-Dış Hususlar ve İlgili Taraflar Listesi | 4.1, 4.2 | U | U |
| İSGYS-LS-04 | Yasal ve Diğer Şartlar Listesi ve Uygunluk Değerlendirmesi | 6.1.3 Z, 9.1.2 Z | Z | Z |
| İSGYS-LS-05 | KKD Standart Listesi (Bölüm-KKD Matrisi + Zimmet) | 8.1.2 | U | U |
| İSGYS-LS-06 | Olay, Kaza ve Ramak Kala Kayıt ve İstatistik Tablosu | 10.2 Z | Z | Z |
| İSGYS-LS-07 | Uygunsuzluk ve Düzeltici Faaliyet Takip Listesi | 10.2 Z | Z | Z |
| İSGYS-LS-08 | Doküman Ana Listesi (iç + dış kaynaklı) | 7.5 | U | U |
| İSGYS-LS-09 | Değişiklik Yönetimi Kayıt Listesi | 8.1.3 | U | — (FR-09 yeter) |
| İSGYS-LS-10 | Yüklenici ve Tedarikçi İSG Değerlendirme Listesi | 8.1.4 | U | U |
| İSGYS-LS-11 | Çalışan Danışma ve Katılım Kayıt Listesi | 5.4 | U | — (kurul tutanağı + öneri formu) |
| İSGYS-LS-12 | Acil Durum Ekipleri ve Tatbikat Takip Listesi | 8.2 Z, Y | Z | Z |
| İSGYS-LS-13 | Tehlikeli Kimyasallar Envanteri | 8.1.2, Y | U | kimyasal varsa |
| İSGYS-LS-14 | Periyodik Kontrole Tabi İş Ekipmanları Envanteri | 9.1.1, Y | U | PN-04 içinde |

### Formlar (Word — sahada doldurulur, kısa tut)

| Kod | Form | Madde |
|---|---|---|
| İSGYS-FR-01 | Olay / Kaza Bildirim Formu | 10.2 |
| İSGYS-FR-02 | Kaza ve Ramak Kala İnceleme (Kök Neden) Raporu | 10.2 |
| İSGYS-FR-03 | Tehlikeli Durum / Ramak Kala / Öneri Bildirim Formu | 5.4, 6.1.2 |
| İSGYS-FR-04 | İş İzni Formu (genel + ekler: sıcak iş, yüksekte, kapalı alan, elektrik) | 8.1.2 |
| İSGYS-FR-05 | Eğitim Katılım Formu (konu başlığı, ders saati, yöntem: yüz yüze/uzaktan) | 7.2 |
| İSGYS-FR-06 | Eğitim Etkinlik Değerlendirme Formu | 7.2 c |
| İSGYS-FR-07 | Saha İSG Denetim Kontrol Listesi | 9.1 |
| İSGYS-FR-08 | Acil Durum Tatbikat Raporu | 8.2 |
| İSGYS-FR-09 | Değişiklik Talep ve Risk Değerlendirme Formu | 8.1.3 |
| İSGYS-FR-10 | Yüklenici İSG Taahhüt ve Giriş Bilgilendirme Formu | 8.1.4 |
| İSGYS-FR-11 | Ziyaretçi İSG Bilgilendirme ve Taahhüt Formu | 8.1.4, 7.4 |
| İSGYS-FR-12 | İSG Kurulu Toplantı Tutanağı | 5.4, Y |
| İSGYS-FR-13 | Yönetimin Gözden Geçirme Toplantı Tutanağı | 9.3 Z |
| İSGYS-FR-14 | İç Tetkik Raporu ve Bulgu Formu | 9.2 Z |
| İSGYS-FR-15 | Çalışmaktan Kaçınma Talep Formu (6331 m.13) | 5.4, Y |
| İSGYS-FR-16 | İSG Kuralları Tebliğ Tutanağı / İhlal Tutanağı | 7.3, 7.4 |
| İSGYS-FR-17 | Destek Elemanı / Çalışan Temsilcisi Görevlendirme Yazısı | 5.3, 8.2, Y |

---

## 05 — Planlar

| Kod | Plan | Madde | Not |
|---|---|---|---|
| İSGYS-PN-01 | **Acil Durum Planı** (Word) | 8.2 Z, Y | Acil Durumlar Yönetmeliği formatı; tahliye krokisi kullanıcıdan |
| İSGYS-PN-02 | Yıllık İSG Çalışma Planı (Word/Excel) | 6.2, Y | İSG Hizmetleri Yönetmeliği; İGU + İH hazırlar, kurul onaylar |
| İSGYS-PN-03 | Yıllık Eğitim Planı ve Eğitim Matrisi | 7.2, Y | Excel |
| İSGYS-PN-04 | İzleme, Ölçme ve Periyodik Kontrol Planı | 9.1.1 Z | Excel |
| İSGYS-PN-05 | İSG Hedefleri ve Programı | **6.2 Z** | Excel |
| İSGYS-PN-06 | İç Tetkik Programı | 9.2 Z | Excel |

---

## 07 — Denetim Hazırlık (kodsuz, Yol Gösterici — K2)

| Dosya | İçerik |
|---|---|
| Mevcut Doküman Envanteri ve Boşluk Raporu.xlsx | `envanter.py` çıktısı + madde bazlı boşluk |
| Mevcut Dokümanlar için Revizyon Rehberi.docx | Her mevcut doküman: korunacak / revize / birleştirilecek / iptal + gerekçe |
| Kod Geçiş Tablosu.xlsx | Eski kod → yeni kod (mevcut set yeniden kodlanıyorsa) |
| Madde-Kanıt Matrisi.xlsx | Madde → gereklilik → doküman → kanıt → sorumlu → durum |
| Öz Değerlendirme.xlsx | Belgelendirme öncesi kontrol listesi |

---

## Sayılar (yaklaşık)

| | Tam set | Sade set |
|---|---|---|
| Politika + kapsam + el kitabı | 3–5 | 2 |
| Prosedür | 17–19 | 7–8 |
| Talimat | risk sayısına göre (8–20 + makine) | 4–8 |
| Kayıt (Excel) | 14 + 6 plan | 10 + 4 plan |
| Form | 15–17 | 8–10 |
