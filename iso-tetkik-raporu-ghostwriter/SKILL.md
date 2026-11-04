---
name: "iso-tetkik-raporu-ghostwriter"
description: "ISO 27001:2022 / ISO 20000-1:2018 belgelendirme denetimlerinde Aşama 1 ve Aşama 2 tetkik raporu (BT-YS-FR-02-09 / 02-10) ve entegre tetkik soru listesi (BT-YS-LS-02-02) Word şablonlarını, baş tetkikçi ağzından ghostwriting diliyle ve uygunsuzluk bulunmamış şekilde doldurur. Kullanıcı \"tetkik raporunu doldur\", \"denetim raporu yaz\", \"soru listesini doldur\" dediğinde kullan."
---

# ISO Tetkik Raporu Ghostwriter

ISO 27001:2022 ve ISO 20000-1:2018 belgelendirme denetimi için Aşama 1 / Aşama 2 tetkik raporlarını ve entegre tetkik soru listelerini, baş tetkikçinin kendi kaleminden çıkmış gibi, **uygunsuzluk bulunmamış** sonucuyla doldurur.

## 0) Başlangıç — bağlamı topla

Denetim klasörünü tara. Tipik yapı:

- `BAŞVURU EVRAKLARI/` → Belgelendirme Başvuru Formu, Teklif, Sözleşme, Gizlilik Sözleşmesi (PDF)
- `1.AŞAMA/` → Tetkik Plan Formu, Tetkikçi Görevlendirme, Tetkik Toplantı Formu (PDF) + **Tetkik Raporu Aşama 1 (DOCX)** + **Entegre Tetkik Soru Listesi (DOCX)**
- `2.AŞAMA/` → aynı set + **Tetkik Raporu Aşama 2 (DOCX)** + Tetkikçi Değerlendirme / Sertifika Düzenleme Bilgi Formu

PDF'lerden şu bilgileri çıkar: firma unvanı ve başvuru no, adres, firma temsilcisi, kapsam metni, sektör kodları, personel sayısı, tetkik tarihleri, tetkik süresi/zamanı (a/g), baş tetkikçi ve ekip, **tetkik plan formundaki gün/saat dağılımı ve her oturumda incelenecek standart maddeleri**, görüşülen personel ve unvanları. Aşama sütunlarının işaretlenmesi bu plana göre yapılır.

Kullanıcıya başlamadan önce sadece şunu doğrula: hangi standartlar kapsamda, sonuç "uygunsuzluk yok" mu, hangi aşamalar doldurulacak.

## 1) Ghostwriting kuralı (kritik)

Her cümle baş tetkikçinin kendi elinden çıkmış gibi olmalı:

- **Yasaklı klişeler:** "kapsamlı bir şekilde", "önemli ölçüde", "sağlam bir temel oluşturmaktadır", "titizlikle", "detaylı bir analiz sonucunda", "genel olarak değerlendirildiğinde", "ayrıca belirtmek gerekir ki".
- Süsleme, övgü, pazarlama dili yok. Tetkikçi not tutar, methiye yazmaz.
- Form alanlarına **akıcı kısa paragraflar** (2–5 cümle) yaz; madde işareti bombardımanı yapma.
- **Edilgen + geçmiş zaman:** "…incelenmiştir", "…doğrulanmıştır", "…görülmüştür", "…teyit edilmiştir", "…örneklenmiştir".
- Cümle uzunluğunu değiştir; arada kısa kesik tespit cümlesi kullan.
- Meta yorum, emoji, yapay zekâ referansı yok.

## 2) Uydurma referans yasağı (kritik)

- Dokümanlar **yalnızca adıyla** anılır. **Doküman kodu, revizyon numarası, yayım/revizyon tarihi ve kayıt numarası (ticket, değişiklik, olay, problem no) yazılmaz.**
- **Uydurma istatistik yazılmaz.** "218 kayıt", "47 risk senaryosu", "yüzde 94" yerine "dönem içinde açılan kayıtlar", "risk senaryoları", "hedefin gerçekleştiği" denir.
- **Kullanılabilecek tek tarih grubu gerçek tetkik tarihleridir.** Firma kayıtlarına ait tarih/ay-yıl yerine "dönem içinde", "planlanan periyotta", "yürürlük tarihinden bu yana" kullanılır.
- **Örnekleme dili serbesttir:** "üç kayıt örneklenmiştir", "iki müşteri sözleşmesi incelenmiştir", "personelin tamamı" yazılabilir.
- Aynı doküman tüm dosyalarda **aynı adla** anılır.
- Tarih yazılmasa da kronoloji tutarlı olmalı: risk değerlendirme → iç tetkik → YGG sırası korunur.

## 3) Uygunsuzluk yok — ama kusursuz da değil

- Uygunsuzluk tablolarını **boş bırak** (sıra numaraları kalsın).
- Aşama 1: "Uygunsuzluk Tespit Edilmemiştir." + "Aşama 2 Denetimi planlanabilir."
- Aşama 2: "Uygunsuzluk Tespit Edilmemiştir." + "Yönetim sistemi, standart isteklerini karşılamaktadır, belgelendirilmesi … önerilir."
- Aşama 2 önceki uygunsuzluk bloğu: "Önceki tetkikte uygunsuzluk tespit edilmemiştir." bırak, alternatif cümleleri sil.
- Aşama 2 kontrol soruları: hedeflere ulaşıldı **Evet**; plan sapması **Hayır**; önemli değişiklik **Hayır**; görüş ayrılığı **Hayır**.
- "Tetkik Ekibi Gözlemleri" alanında **2–4 iyileştirme fırsatı (OFI)** yaz. OFI'lar asla "eksiktir / yapılmamıştır" ile yazılmaz; "…iyileştirilebilir", "…güçlendirilmesi önerilir", "…faydalı olacaktır" kullanılır.

## 4) Kapsam sınırı

Kapsam dışı standartlara ait tablolar, sütunlar ve rapor özet blokları **hiç dokunulmadan boş bırakılır** — "kapsam dışı" notu bile yazılmaz, satır silinmez.

Rapordaki BÖLÜM 3 standart-özel özet bloklarından yalnızca kapsamdakiler doldurulur (ISO 27001 → BGYS özeti, ISO 20000-1 → HYS özeti). Kalite / Çevre / İSG / Yapay Zekâ / İş Sürekliliği blokları boş kalır.

## 5) Teknik yöntem — şablona zarar verme

1. Önce **`docx` skill'ini** oku ve uygula. PDF okuma gerekiyorsa **`pdf` skill'i**.
2. `python-docx` bash ortamında kuruludur.
3. **Önce keşif:** her DOCX'in tüm tablolarını, satır/sütun sayılarını ve mevcut hücre metinlerini dök. Sütun başlıklarını **çalışma anında doğrula**, varsayma.
4. Tablo/satır/sütun **eklenmez, silinmez, birleştirilmez**. Başlıklar, form kodları, üstbilgi/altbilgi, logo, sayfa yapısı **değişmez**.
5. **Biçim mirası:** doldurulan hücrelerdeki run biçimi, aynı tablodaki orijinal bir gövde hücresinden `w:rPr` kopyalanarak ayarlanır (kalın/italik/renk kaldırılır). Aksi hâlde metin belgenin varsayılan fontuna düşer.
6. **Onay kutuları `w:sdt` içinde olabilir.** `paragraph.runs` bunları görmez. Hücredeki tüm `w:t` elemanlarını tarayıp `☐` → `☒` yap. Kutunun yanına ayrıca "X" yazma.
7. Alternatif cümle blokları: geçerli olan bırakılır, geçersizler paragraf olarak silinir.
8. Düzenlemeden önce her dosyanın `_ORIJINAL` ekli yedeğini al.
9. Türkçe büyük harf tuzağı: `"i".upper()` Python'da `"I"` verir. Cümle başı düzeltmesinde `i → İ` eşlemesini elle yap.
10. Kullanıcı dosyayı Word'de açık bırakmışsa yazma "Permission denied" verir; hangi dosyanın kilitli olduğunu tespit edip kapatmasını iste.
11. Bitince `mcp__cowork__present_files` ile dosyaları sun.

## 6) Soru listesi doldurma

### Tablo 1 (ana standart maddeleri)

Aşama 1 kopyasında **AŞ1**, Aşama 2 kopyasında **AŞ2** sütunu işaretlenir; **G1/G2 gözetim tetkikleri içindir, boş bırakılır.** Plana girmeyen satırın delil hücresine "Aşama 1 tetkik planında yer almamıştır; Aşama 2'de değerlendirilecektir." yazılır.

### Tablo 2 (ISO 27001 Ek A) — **"2022 Şartlar" sütununa göre doldurulur**

Bu şablonun satır yapısı 2017 sürümüne göre kurulmuştur; **"2022 Şartlar" sütunu yalnızca dört hücrede doludur:**

| Satır | İçerik |
|---|---|
| tema başlığı | "5. Organizasyonel kontroller" |
| alt satır | 5.1 … 5.37 (37 kontrol tek hücrede, satır satır) |
| tema başlığı | "6. İnsan kontrolleri" |
| alt satır | 6.1 … 6.8 |
| tema başlığı | "7. Fiziksel kontroller" |
| alt satır | 7.1 … 7.14 |
| tema + liste | "8. Teknolojik kontroller" + 8.1 … 8.34 (aynı hücrede) |

Kural:

- Delil yalnızca bu satırlara yazılır. **2022 karşılığı "-" olan 2017 satırları boş bırakılır** — denetim 2022 sürümüne göre yapıldığı için o satırların karşılığı yoktur.
- Tema başlığı satırına 2–3 cümlelik tema özeti yazılır (kaç kontrol, hariç tutulan var mı, delil türü).
- Alt satıra **her kontrol için bir satır** yazılır; format: `5.1 <kontrol adı> — <delil cümlesi>`. Kontrol adının yazılması şarttır: bazı şablonlarda 2022 listesinin numaralandırması bozuktur (ör. 5.23/5.24 ve 5.29/5.30 satırları ikiye bölünmüş, 5.24 ve 5.37 atlanmış olabilir); ad yazılırsa eşleşme satır konumuna değil isme dayanır.
- Numaralandırma **resmî ISO/IEC 27001:2022 numaralandırmasıdır** (5.1–5.37, 6.1–6.8, 7.1–7.14, 8.1–8.34 = 93 kontrol). Şablondaki yazım hatası taklit edilmez; sapma kullanıcıya bildirilir.
- Aşama 1'de plana girmeyen kontrolün satırı "Aşama 1 tetkik planında yer almamıştır; Aşama 2 tetkikinde değerlendirilecektir." olur. Aşama 2'de 93 kontrolün tamamı delillendirilir.
- **Yeni 11 kontrol için delil zorunlu:** 5.7, 5.23, 5.30, 7.4, 8.9, 8.10, 8.11, 8.12, 8.16, 8.23, 8.28.
- Bazı şablonlarda Tablo 2'de AŞ2 sütunu yoktur; bu durumda Aşama 2 dosyasında mevcut aşama sütunu "tetkik edildi" işareti olarak kullanılır ve tercih kullanıcıya bildirilir.

### Ortak

- **Delil çeşitliliği:** aynı kalıbı arka arkaya tekrarlama. Politika, prosedür, talimat, form, log/ekran görüntüsü, toplantı tutanağı, sözleşme, taahhütname, eğitim katılım listesi, yetki matrisi, test raporu, envanter, hizmet masası kaydı, SLA raporu arasında dolaş.
- **Firma Bilgileri / Görüşülen Kişiler tabloları:** plan ve toplantı formlarındaki isim-unvanlar kullanılır; yoksa firma ölçeğine uygun 4–6 satır üretilir ve tüm dosyalarda aynı kalır. Üretilen isimler iş sonunda varsayım olarak bildirilir.

**ISO 20000-1:2018 delil odakları:** hizmet kataloğu, SLA/OLA ve tedarikçi sözleşmeleri, hizmet sürekliliği ve kapasite planı, olay/istek/problem yönetimi, değişiklik yönetimi, sürüm/dağıtım, konfigürasyon yönetimi, hizmet raporlama ve ölçüm, iyileştirme kayıtları.

## 7) Rapor doldurma

### Aşama 1 — doküman gözden geçirme odaklı

BÖLÜM 3 alt başlıkları, her biri 3–6 cümle: başvuru bilgilerinin doğrulanması; kapsam değerlendirmesi; sertifika-marka-logo bilgilendirmesi; sahaya özgü şartlar; yasal ve düzenleyici şartlar (Türkiye için tipik: 6698 KVKK, 5651, 6563, 5846 FSEK, lisans yükümlülükleri); yönetim sistemi uygunluğu; iç tetkik ve YGG; tetkik ekibi gözlemleri (2–3 pozitif + 2–3 OFI); entegre uygulanma durumu; BGYS özeti (risk metodolojisi, varlık envanteri, risk işleme planı, SoA, hariç tutulan kontrol gerekçesi); HYS özeti.

BÖLÜM 4: uygunsuzluk tablosu boş, "Uygunsuzluk Tespit Edilmemiştir." + "Aşama 2 planlanabilir.", baş tetkikçi adı ve Aşama 1 tarihi.

### Aşama 2 — uygulama ve etkinlik odaklı

Örneklenmiş kayıtlar, yerinde doğrulama, personel görüşmeleri, sistem gözlemi anlatılır. Ek alanlar: önceki tetkik sonuçlarının karşılaştırılması; planlama bilgilerinin yerinde doğrulanması; "incelenemeyen hususlar" → "Bulunmamaktadır."; kontrol soruları tablosu; BÖLÜM 4'te belgelendirme önerisi ve Açıklamalar alanına 2–3 cümlelik tavsiye.

**Aşama 1 ↔ Aşama 2 tutarlılığı:** Aşama 2, Aşama 1'de anılan doküman adlarını ve gözlemleri tanır ve ileri taşır; Aşama 1'deki OFI'lar kapanmış ya da değerlendirilmiş olarak anılır.

## 8) Ölçek gerçekçiliği

Firma personel sayısına uygun yaz. Küçük bir hizmet sağlayıcı için ayrı bilgi güvenliği departmanı, 7/24 SOC ekibi, onlarca kişilik değişiklik kurulu kurgulanmaz. Görev birleştirme ve dış kaynak kullanımı bu ölçekte normaldir.

## 9) Son doğrulama (atlanmaz)

Doldurulmuş dosyaları bağımsız bir doğrulama turuyla — mümkünse betikle — kontrol et:

- [ ] Tablo/satır/sütun sayıları orijinaliyle aynı
- [ ] Uygunsuzluk satırları boş; her iki raporda "Uygunsuzluk Tespit Edilmemiştir." işaretli
- [ ] Doğru sonuç kutuları `☒`, diğerleri `☐`; kutuların yanında artık metin yok
- [ ] Kapsam dışı tablolar, sütunlar ve özet blokları boş; G1/G2 boş
- [ ] Tablo 2'de yalnızca "2022 Şartlar" sütunu dolu olan satırlarda delil var; 2017 satırları boş
- [ ] Ek A'da 93 kontrolün tamamı delillendirilmiş; yeni 11 kontrol dâhil
- [ ] Metinde doküman kodu, revizyon numarası, kayıt numarası veya firma kaydına ait tarih/ay-yıl yok
- [ ] Uydurma istatistik yok; aynı doküman her yerde aynı adla anılıyor
- [ ] Görüşülen personel isim/unvanları tüm dosyalarda aynı
- [ ] Firma ölçeğiyle çelişen ifade yok
- [ ] Yasaklı klişe, methiye dili, meta yorum, emoji yok
- [ ] Türkçe imla doğru (özellikle `I` / `İ`); edilgen geçmiş zaman tutarlı
- [ ] `_ORIJINAL` yedekler mevcut
- [ ] Bir sayfa LibreOffice ile PDF'e çevrilip görsel olarak kontrol edildi

## 10) Belirsizlik yönetimi

Bir bilgi evraklarda yoksa durup sorma; firma ölçeğine uygun makul ve tutarlı bir varsayım üret, ilerle ve **iş bitiminde varsayımların listesini kullanıcıya ayrı bir not olarak sun**. Belgeye "[?]", "XXX", "…" gibi yer tutucu bırakma.

