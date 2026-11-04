# Türk İSG Mevzuatı ile ISO 45001 Kesişimi

ISO 45001 yasal şartlara uyumu taahhüt ettirir (5.2), belirletir (6.1.3) ve
değerlendirtir (9.1.2). Türkiye'de bu şartların omurgası **6331 sayılı Kanun** ve
alt mevzuatıdır. Bu dosya iki şeyi verir: (1) dokümanlara gömülecek sayısal yasal
kuralların özet tablosu, (2) yasal şart listesinin nasıl kurulacağı.

> **Güncellik kuralı:** Aşağıdaki değerler skill yazıldığı tarihte (Ekim 2026)
> bilinen durumdur. Üretim sırasında `WebSearch`/Firecrawl ile mevzuat.gov.tr ve
> Resmî Gazete'den teyit et; teyit edilemeyen künyeyi `[TEYİT: RG tarih/sayı]`
> olarak bırak. Uydurma Resmî Gazete tarihi/sayısı yazmak, yanlış yazmaktan daha
> kötüdür — denetçi tek bir hatada tüm listeye güvenini kaybeder.
> `regulatory-legal:reg-feed-watcher` / `policy-diff` skill'leri yüklüyse mevzuat
> değişikliği takibi için kullan.

## İçindekiler

1. Dokümanlara gömülecek sayısal kurallar
2. 2026 değişiklikleri
3. Rol eşlemesi — 6331 ↔ ISO 45001
4. Yasal şart listesinin kurulması
5. Mülga mevzuat — listeye girmemeli

---

## 1. Dokümanlara gömülecek sayısal kurallar

Tehlike sınıfına göre değişen değerler. Kuruluşun sınıfını görüşmede sabitle ve
**bütün sette aynı değeri** kullan (bir dokümanda "yılda bir tatbikat", ötekinde
"6 ayda bir" olmasın — kuruluş daha sık yapıyorsa en sık olanı her yere yaz).

| Konu | Az tehlikeli | Tehlikeli | Çok tehlikeli | Dayanak (teyit et) | Doküman |
|---|---|---|---|---|---|
| Risk değerlendirmesi yenileme (en geç) | 6 yıl | 4 yıl | 2 yıl | RD Yön. | PR-03, LS-01 |
| İSG kurulu toplantı sıklığı (50+ çalışan, 6 aydan uzun süreli işler) | 3 ayda bir | 2 ayda bir | ayda bir | İSG Kurulları Yön. | PR-05, FR-12 |
| Destek elemanı (her bir ekip için, çalışan sayısına göre) | 50'ye kadar 1 | 30'a kadar 1 | 20'ye kadar 1 | Acil Durumlar Yön. | PN-01, LS-12 |
| İlk yardımcı | 20 çalışana 1 | 15 çalışana 1 | 10 çalışana 1 | İlkyardım Yön. | PN-01, LS-12 |
| Periyodik sağlık muayenesi | 5 yılda bir | 3 yılda bir | yılda bir | İSG Hizmetleri Yön. | PR-19 |
| Tatbikat | en az yılda bir | en az yılda bir | en az yılda bir | Acil Durumlar Yön. | PR-12, PN-01 |
| Çalışan temsilcisi sayısı | 2–50: 1 · 51–100: 2 · 101–500: 3 · 501–1000: 4 · 1001–2000: 5 · 2001+: 6 | | | 6331 m.20 | PR-05, FR-17 |
| İş kazası SGK bildirimi | kazadan sonraki en geç 3 iş günü | | | 5510 m.13, 6331 m.14 | PR-16 |
| Meslek hastalığı bildirimi | öğrenildiği tarihten itibaren 3 iş günü | | | 5510 m.14 | PR-16 |

## 2. 2026 değişiklikleri (skill yazılırken bilinenler)

**Çalışanların İSG Eğitimlerinin Usul ve Esasları Hakkında Yönetmelik** —
2 Nisan 2026 tarihli, 33212 sayılı Resmî Gazete (ikincil kaynaktan; resmî metinden teyit et):

- Temel İSG eğitimi işe girişten itibaren **en geç 3 ay** içinde tamamlanır
- **1 ders saati = 45 dk eğitim + 15 dk ara** (60 dk)
- Ek-1 konu başlıklarından 1–3 (genel, sağlık, teknik) uzaktan/yüz yüze/karma verilebilir;
  **4. başlık (işe ve işyerine özgü riskler)** tehlikeli ve çok tehlikeli sınıfta **yalnız yüz yüze**
- 4. başlık asgari süresi: az tehlikeli 2, tehlikeli 3, çok tehlikeli 4 ders saati
- Tekrar eğitimlerinde toplam asgari süre sınıflardan bağımsız 8 ders saati olarak bildirilmektedir — teyit et
- Uzaktan eğitimde giriş-çıkış saatleri, tamamlama oranı ve ölçme-değerlendirme sonuçları kayıt altına alınır
- Temel eğitim belgesinde eğitimin türü (ilk/tekrar), şekli (uzaktan/yüz yüze) ve konu başlığı süreleri yazılır

Etkilenen dokümanlar: PR-06, PN-03 (Eğitim Matrisi "3 ay" formülü), FR-05 (yöntem ve ders saati alanları).

**21 Temmuz 2026, 33316 sayılı Resmî Gazete:** İşyerlerinde İşin Durdurulmasına
Dair Yönetmelik'te değişiklik (ve maden İSG değişikliği). PR-04'te izleme kaydı
olarak geç; tehlikeli/çok tehlikeli işyerlerinde iş durdurma riskini YGG girdisine al.

**ISO 45001 revizyonu:** ISO/DIS 45001 2026'da yayımlandı; nihai standardın 2027'de
yayımlanması ve 3 yıllık geçiş beklenmektedir. Odak: psikososyal riskler, iyi oluş,
hibrit/uzaktan çalışma, iklim kaynaklı riskler ve dayanıklılık, tedarik zinciri/
yüklenici yönetimi, güvenlik kültürü. Kullanıcı yeni sürüme göre üretim isterse
önce yayımlanıp yayımlanmadığını web'den teyit et; yayımlanmadıysa 2018+Amd 1:2024
ile üret ve OKUBENI'ye "2027 geçişine hazırlık notları" bölümü ekle.

## 3. Rol eşlemesi — 6331 ↔ ISO 45001

Rol adlarını görüşmede sabitle ve setin tamamında aynı kullan. Mevcut setlerde aynı
kişi için "İş Güvenliği ve Çevre Sorumlusu", "Çevre ve İSG Uzmanı", "İSG ve Çevre
Mühendisi" gibi üç ayrı unvan görülür — denetçi bunu tutarsızlık olarak yazar.

| 6331 rolü | 45001 karşılığı | Not |
|---|---|---|
| İşveren / işveren vekili | Üst yönetim (5.1) | Sorumluluk devredilemez |
| İş güvenliği uzmanı (A/B/C sınıfı — tehlike sınıfına uygun) | İSGYS koordinasyonu, RD liderliği | OSGB'den hizmet alınıyorsa 8.1.4.3 dış kaynak |
| İşyeri hekimi, diğer sağlık personeli | Sağlık gözetimi (9.1, PR-19) | |
| Çalışan temsilcisi | 5.4'ün birincil kanalı | Seçim/atama kaydı FR-17 |
| Destek elemanı | 8.2 acil durum ekipleri | |
| İSG kurulu | 5.4 kanalı + 5.1 e | 5.4'ün tamamı değil |
| Yönetim temsilcisi (OHSAS mirası) | Zorunlu değil | İsteğe bağlı "İSGYS Koordinatörü" |

## 4. Yasal şart listesinin kurulması

`kayitlar_45001.py yasal` çekirdek listeyi (yalnız ad, künyesiz) üretir. Sonra:

1. Kuruluşun faaliyetine göre uygulanabilirliği işaretle; uygulanmayanı silme, "Hayır + gerekçe"
2. Künyeyi mevzuat.gov.tr'den yaz (ilk yayın + son değişiklik)
3. "İlgili maddeler / yükümlülük" sütununa **kuruluşun yapması gereken eylemi** yaz
   ("m.12: kurul ayda bir toplanır") — madde numarası listesi tek başına uygunluk
   değerlendirmesine yaramaz
4. Sektörel ekler: gıda (çalışma koşulları için), BEKRA, patlayıcı ortam, yapı işleri,
   radyasyon, maden, sağlık kuruluşu
5. Diğer şartlar: müşteri/grup şirketi İSG şartları, sigorta şartları, sözleşmeler
6. 9.1.2 uygunluk değerlendirmesi sütunları en az yılda bir doldurulur; "Uygun Değil" → DÖF

Çevre mevzuatı (14001) aynı listeye girecekse **EYS** listesi olur ve "İlgili standart"
sütunu eklenir; ama iki sistemin yükümlülük satırları birbirine karıştırılmaz.

## 5. Mülga mevzuat — listeye girmemeli

Eski setlerde sık görülür; görürsen boşluk raporunda "yürürlükten kalkmış mevzuata
atıf" bulgusu olarak yaz:

- İşçi Sağlığı ve İş Güvenliği Tüzüğü (eski "İş Güvenliği Tüzüğü" maddeleri)
- Yapı İşlerinde İşçi Sağlığı ve İş Güvenliği Tüzüğü
- Parlayıcı, Patlayıcı, Tehlikeli ve Zararlı Maddelerle Çalışılan İşyerlerinde ve İşlerde Alınacak Tedbirler Hakkında Tüzük
- Eski "Kişisel Koruyucu Donanım Yönetmeliği" (piyasaya arz) ile "KKD'lerin İşyerlerinde Kullanılması Hakkında Yönetmelik" karıştırılmamalı — ikincisi işverene yöneliktir
- OHSAS 18001 (2021'de geçerliliği sona erdi) — dış kaynaklı doküman listesinden çıkarılır

Tüzüklerin yürürlük durumu 6331 sonrası düzenlemelerle değişti; tek tek teyit et.
