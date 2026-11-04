# ISO/IEC 27001:2022 — Üretilecek Doküman Listesi

## İçindekiler

- 00 — Kapsam ve El Kitabı
- 01 — Politikalar
- 02 — Prosedürler
- 03 — Talimatlar
- 04 — Formlar ve Listeler (Excel)
  - SoA'nın zorunlu sütunları (6.1.3 d)
  - Risk envanterinin zorunlu sütunları
- 05 — Planlar
- 07 — Denetim Hazırlık
- Sayısal beklenti

İki set var: **tam set** (50+ çalışan, düzenlemeye tabi sektör, karmaşık BT) ve
**sadeleştirilmiş set** (50 altı çalışan, tek lokasyon, bulut ağırlıklı).
Sadeleştirilmiş sette prosedürler birleştirilir; gereklilikler kaybolmaz, sadece
daha az dosyaya sığar. Kullanıcının ölçeğine bakıp doğru seti seç ve seçimini
söyle.

`Z` = standardın açıkça dokümante edilmiş bilgi olarak istediği (zorunlu).
`U` = uygulamada denetçinin beklediği ama standardın adını koymadığı.

---

## 00 — Kapsam ve El Kitabı

| Kod | Doküman | Format | Madde | Tam | Sade |
|---|---|---|---|---|---|
| BGYS-EK-01 | BGYS El Kitabı | Word | 4.4 | U | U |
| BGYS-PL-00 | BGYS Kapsam Dokümanı | Word | **4.3 Z** | Z | Z |
| BGYS-FR-01 | Bağlam Analizi (SWOT / PESTLE) | Word | 4.1 | U | birleşir→BGYS-LS-06 (tek Word: "Bağlam ve İlgili Taraflar Analizi"; taraf tablosu içinde) |
| BGYS-LS-06 | İlgili Taraflar ve Beklentileri Analizi | Excel | 4.2 | U | U |

Kapsam dokümanı bu setin en kritik dosyasıdır. Şunları içermeli: sertifikada
yazacak kapsam cümlesi, dahil edilen lokasyon/birim/süreç listesi, hariç tutulan
alanlar **ve gerekçeleri**, arayüzler ve bağımlılıklar (4.3 c), dış kaynak
kullanılan süreçler ve bunların kontrol biçimi.

---

## 01 — Politikalar

| Kod | Doküman | Format | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|---|
| BGYS-PL-01 | Bilgi Güvenliği Politikası (ana) | Word | **5.2 Z**, A.5.1 | Z | Z |
| BGYS-PL-02 | Erişim Kontrol Politikası | Word | A.5.15, A.8.3 | U | U |
| BGYS-PL-03 | Kabul Edilebilir Kullanım Politikası | Word | A.5.10, A.7.7, A.5.32 | U | U |
| BGYS-PL-04 | Bilgi Sınıflandırma Politikası | Word | A.5.12, A.5.13 | U | U |
| BGYS-PL-05 | Parola ve Kimlik Doğrulama Politikası | Word | A.5.17, A.8.5 | U | birleşir→PL-02 |
| BGYS-PL-06 | Bulut Hizmetleri Güvenlik Politikası | Word | A.5.23 | U | U |
| BGYS-PL-07 | Kişisel Verilerin Korunması Politikası | Word | A.5.34 | U | U |
| BGYS-PL-08 | Uzaktan Çalışma Politikası | Word | A.6.7 | U | birleşir→PL-03 |
| BGYS-PL-09 | Fiziksel ve Çevresel Güvenlik Politikası | Word | A.7.1–A.7.13 | U | U |
| BGYS-PL-10 | Uç Nokta ve Taşınabilir Cihaz Politikası | Word | A.8.1, A.7.9 | U | birleşir→PL-03 |
| BGYS-PL-11 | Kötü Amaçlı Yazılımdan Korunma Politikası | Word | A.8.7 | U | birleşir→PL-14 |
| BGYS-PL-12 | Veri Maskeleme ve Test Verisi Politikası | Word | A.8.11, A.8.33 | U | — |
| BGYS-PL-13 | Veri Sızıntısı Önleme Politikası | Word | A.8.12 | U | — |
| BGYS-PL-14 | Ağ Güvenliği Politikası | Word | A.8.20–A.8.23 | U | U |
| BGYS-PL-15 | Kriptografi ve Anahtar Yönetimi Politikası | Word | A.8.24 | U | U |

Ana politika 2–4 sayfayı geçmemeli. Konuya özgü politikalar 2–6 sayfa. Uzun
politika okunmaz; okunmayan politika denetimde "farkındalık yok" bulgusuna döner.

---

## 02 — Prosedürler

| Kod | Doküman | Format | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|---|
| BGYS-PR-01 | Doküman ve Kayıt Kontrol Prosedürü | Word | **7.5.2, 7.5.3 Z**, A.5.33 | Z | Z |
| BGYS-PR-02 | Risk Yönetimi Prosedürü (metodoloji) | Word | **6.1.2, 6.1.3 Z** | Z | Z |
| BGYS-PR-03 | Düzeltici Faaliyet ve Uygunsuzluk Prosedürü | Word | **10.2 Z** | Z | Z |
| BGYS-PR-04 | İnsan Kaynakları Güvenliği Prosedürü | Word | 7.2, A.6.1–A.6.6 | U | U |
| BGYS-PR-05 | Erişim ve Kimlik Yönetimi Prosedürü | Word | A.5.16–A.5.18, A.8.2 | U | U |
| BGYS-PR-06 | Fiziksel Erişim Kontrol Prosedürü | Word | A.7.2, A.7.4 | U | birleşir→PL-09 |
| BGYS-PR-07 | Ortam ve Güvenli İmha Prosedürü | Word | A.7.10, A.7.14, A.8.10 | U | U |
| BGYS-PR-08 | Tedarikçi Güvenliği Prosedürü | Word | A.5.19–A.5.22, A.8.30 | U | U |
| BGYS-PR-09 | Bilgi Güvenliği İhlal Olayı Yönetim Prosedürü | Word | A.5.24–A.5.28, A.6.8 | U | U |
| BGYS-PR-10 | İç Tetkik Prosedürü | Word | **9.2 Z** | Z | Z |
| BGYS-PR-11 | Bilgi Transferi Prosedürü | Word | A.5.14 | U | birleşir→PL-04 |
| BGYS-PR-12 | Proje Güvenliği Prosedürü | Word | A.5.8, A.8.4 | U | — |
| BGYS-PR-13 | Uyum Gözden Geçirme Prosedürü | Word | A.5.31, A.5.35, A.5.36 | U | birleşir→PR-10 |
| BGYS-PR-14 | Tehdit İstihbaratı Prosedürü | Word | A.5.7 | U | birleşir→PR-16 |
| BGYS-PR-15 | Kapasite Yönetimi Prosedürü | Word | A.8.6 | U | — |
| BGYS-PR-16 | Teknik Açıklık ve Yama Yönetimi Prosedürü | Word | A.8.8 | U | U |
| BGYS-PR-17 | Konfigürasyon Yönetimi Prosedürü | Word | A.8.9, A.8.19 | U | birleşir→PR-21 |
| BGYS-PR-18 | Yedekleme ve Geri Yükleme Prosedürü | Word | A.8.13, A.8.14 | U | U |
| BGYS-PR-19 | Kayıt (Log) ve İzleme Prosedürü | Word | A.8.15–A.8.17 | U | U |
| BGYS-PR-20 | Güvenli Yazılım Geliştirme Prosedürü | Word | A.8.25–A.8.31 | U | geliştirme varsa |
| BGYS-PR-21 | Değişiklik Yönetimi Prosedürü | Word | 6.3, A.8.32 | U | U |
| BGYS-PR-22 | Yönetimin Gözden Geçirmesi Prosedürü | Word | **9.3 Z** | Z | birleşir→PR-10 |

---

## 03 — Talimatlar

| Kod | Doküman | Format | Kontrol |
|---|---|---|---|
| BGYS-TL-01 | Bilgi Etiketleme Talimatı | Word | A.5.13 |
| BGYS-TL-02 | Adli Kanıt Toplama Talimatı | Word | A.5.28 |
| BGYS-TL-03 | Güvenli Alanlarda Çalışma Talimatı | Word | A.7.6 |
| BGYS-TL-04 | Güvenli Kodlama Talimatı | Word | A.8.28 |

Talimatlar sektöre göre değişir; kuruluşun gerçek işine karşılık gelmiyorsa üretme.

---

## 04 — Formlar ve Listeler (Excel)

| Kod | Doküman | Madde / Kontrol | Tam | Sade |
|---|---|---|---|---|
| BGYS-LS-01 | Varlık Envanteri | A.5.9 | U | U |
| BGYS-LS-02 | **Uygulanabilirlik Bildirgesi (SoA)** | **6.1.3 d) Z** | Z | Z |
| BGYS-LS-03 | Yasal ve Sözleşmesel Yükümlülükler Matrisi | A.5.31 | U | U |
| BGYS-LS-04 | Doküman Ana Listesi | 7.5.3 | U | U |
| BGYS-LS-05 | Tedarikçi Envanteri ve Risk Sınıfı | A.5.19 | U | U |
| BGYS-LS-06 | İlgili Taraflar Analizi | 4.2 | U | U |
| BGYS-LS-07 | Yetkinlik ve Eğitim Matrisi | **7.2 Z** | Z | Z |
| BGYS-FR-03 | **Risk Envanteri ve Risk İşleme Planı** | **6.1.2, 6.1.3, 8.2, 8.3 Z** | Z | Z |
| BGYS-FR-04 | Bilgi Güvenliği Hedefleri ve İzleme Tablosu | **6.2, 9.1 Z** | Z | Z |
| BGYS-FR-05 | Erişim Talep ve Yetkilendirme Formu | A.5.18 | U | U |
| BGYS-FR-06 | İç Tetkik Soru Listesi ve Bulgu Formu | 9.2 | U | U |
| BGYS-FR-07 | İşe Giriş / Çıkış Güvenlik Kontrol Formu | A.6.5, A.5.11 | U | U |
| BGYS-FR-08 | İş Sözleşmesi Bilgi Güvenliği Eki | A.6.2 | U | U |
| BGYS-FR-09 | Gizlilik Taahhütnamesi (NDA) | A.6.6 | U | U |
| BGYS-FR-10 | Tedarikçi Güvenlik Sözleşme Eki | A.5.20 | U | U |
| BGYS-FR-11 | Bilgi Güvenliği Olay Bildirim ve Kayıt Formu | A.6.8, A.5.25 | U | U |
| BGYS-FR-12 | Düzeltici Faaliyet Formu / DÖF Takip | **10.2 Z** | Z | Z |
| BGYS-FR-13 | Yönetimin Gözden Geçirmesi Toplantı Formu | **9.3 Z** | Z | Z |
| BGYS-FR-14 | Değişiklik Talep ve Onay Formu | A.8.32 | U | U |

### SoA'nın zorunlu sütunları (6.1.3 d)

`Kontrol No | Kontrol Başlığı | Uygulanabilir mi (E/H) | Dahil etme gerekçesi |
İlgili risk no | Uygulama durumu | Uygulayan doküman | Sorumlu | Hariç tutma gerekçesi`

Dört bilgi standardın açık isteğidir: gerekli kontroller, dahil etme gerekçesi,
uygulanıp uygulanmadığı, hariç tutma gerekçesi. Bu sütunlardan biri eksikse SoA
uygun değildir. Tüm 93 kontrol listelenmelidir — hariç tutulanlar dahil.

### Risk envanterinin zorunlu sütunları

`Risk No | Varlık/Süreç | Tehdit | Açıklık | Mevcut kontroller | Olasılık | Etki |
Risk Skoru | Risk Sahibi | İşleme Seçeneği | Planlanan kontroller (Ek A ref) |
Sorumlu | Termin | Artık Risk | Risk Sahibi Onayı | Durum`

Son iki sütunu atlama: 6.1.3 f) risk sahibinin risk işleme planını onaylamasını
ve artık riski kabul etmesini açıkça ister. Onay sütunu yoksa bu kanıt yoktur.

---

## 05 — Planlar

| Kod | Doküman | Format | Madde |
|---|---|---|---|
| BGYS-PN-01 | Risk İşleme Planı | Excel (FR-03 ile aynı dosyada sekme) | **6.1.3 e) Z** |
| BGYS-PN-02 | Farkındalık ve Eğitim Planı | Word + Excel | 7.3, A.6.3 |
| BGYS-PN-03 | Yıllık İç Tetkik Programı | Excel | **9.2.2 Z** |
| BGYS-PN-04 | İş Sürekliliği ve BİT Süreklilik Planı | Word | A.5.29, A.5.30, A.8.14 |
| BGYS-PN-05 | Bakım ve Test Planı | Excel | A.7.13, A.8.13 |
| BGYS-PN-06 | İletişim Planı | Word | 7.4 |

---

## 07 — Denetim Hazırlık

| Kod | Dosya | İçerik |
|---|---|---|
| — (yol gösterici) | Madde-Kanıt Matrisi.xlsx | Madde/kontrol → doküman → kanıt → sorumlu → durum |
| — (yol gösterici) | Öz Değerlendirme.xlsx | Her madde için uygunluk durumu ve boşluklar |
| — (yol gösterici) | Denetçi Soru Listesi.xlsx | Denetçinin soracağı sorular ve hazırlanan cevaplar |
| — | OKUBENI.md | Ne üretildi, ne eksik, `[DOLDURULACAK]` listesi, sonraki adımlar |

Denetim hazırlık dosyaları **kodsuz yol göstericidir** (K2): dosya adı yalnız
addır, kapakta "YOL GÖSTERİCİ", antette "Doküman Türü | Yol Gösterici" yazar,
Doküman Ana Listesi'ne girmez ve listenin not alanında bu açıklanır. Doküman
kontrolüne tabi değildir; denetime hazırlık süresince güncellenir.

Bu dört dosya seti "doküman yığını" olmaktan çıkarıp kullanılabilir hâle getirir.
Özellikle `OKUBENI.md`'yi asla atlama.

---

## Sayısal beklenti

| Ölçek | Word | Excel | Toplam |
|---|---|---|---|
| Sadeleştirilmiş (< 50 kişi) | 24–28 | 16–19 | 40–47 |
| Tam set | 33–38 | 19–22 | 52–60 |

Bu sayılar yukarıdaki tabloların `Tam` / `Sade` sütunlarından türer; çelişki
görürsen **tablolar esastır**, bu özet yaklaşıktır. Sade sette azalma dosya
sayısından çok *birleştirmeden* gelir: 22 prosedür 14'e, 15 politika 9'a iner.

Kullanıcı "hepsini üret" derse ve set büyükse, üretimi gruplar hâlinde yap ve
her grup sonunda kısa durum bildir. Tek seferde 57 dosya üretip sessiz kalmak
kullanıcıyı ne olduğunu anlamadan bırakır.
