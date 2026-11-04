# Tehlike Belirleme ve Risk Değerlendirmesi — Yöntem, Ekip, Kapsam

İSGYS'nin kalbi bu kayıttır: politikadaki taahhüt buradan önleme, önlemden talimata,
talimattan eğitime ve denetim kontrol listesine akar. Denetçi sahada bir çalışanın
yanında durup "bu işin risk değerlendirmesini göster" der; cevap `İSGYS-LS-01`'deki
bir satır olmalıdır.

## İçindekiler

1. Yasal çerçeve ve ISO 45001 farkı
2. Yöntem seçimi (L-matris / Fine-Kinney)
3. Ekip ve katılım
4. Kapsam kontrol listesi — neyin içinde olması gerekir
5. Kontrol hiyerarşisi
6. Sektöre göre tehlike başlangıç katalogları
7. Sık yapılan hatalar

---

## 1. Yasal çerçeve ve ISO 45001 farkı

6331 m.10 ve İSG Risk Değerlendirmesi Yönetmeliği risk değerlendirmesini **işverene**
zorunlu kılar; 45001 bunu bir **süreç** olarak ister (6.1.2 sürekli ve proaktif).
İkisi tek kayıtta birleşir — ayrı "yasal RD" ve "ISO RD" tutmak denetimde çelişki doğurur.

Yönetmelikten gelen ve dokümana mutlaka yazılması gerekenler:

| Konu | Kural (teyit et: mevzuat.gov.tr) |
|---|---|
| Ekip | İşveren/vekili, İGU, İH, çalışan temsilcisi, destek elemanları, bölümleri bilen çalışanlar |
| Yenileme | Tehlike sınıfına göre en geç **çok tehlikeli 2, tehlikeli 4, az tehlikeli 6 yıl** |
| Tetikleyiciler | Bina/eklenti taşınması veya değişikliği; teknoloji, madde, ekipman değişikliği; üretim yöntemi değişikliği; iş kazası, meslek hastalığı, ramak kala; mevzuat değişikliği; ölçüm sonucu; yeni bilgi |
| Özel politika grupları | Gebe/emziren, genç, yaşlı, engelli, kronik hastalığı olan, yabancı uyruklu çalışanlar ayrıca değerlendirilir |
| Kayıt içeriği | İşyeri unvanı/adresi, ekip, tarih, geçerlilik, tehlikeler, riskler, önlemler, sorumlular, termin |

Tehlike sınıfı NACE koduna göre **İşyeri Tehlike Sınıfları Tebliği**'nden alınır;
kullanıcıya sor, tahmin etme (gıda imalatının alt kolları farklı sınıflarda olabilir).

---

## 2. Yöntem seçimi

Mevcut kuruluşun yöntemi varsa **onu koru** — yöntem değiştirmek tüm tarihçeyi
karşılaştırılamaz yapar. Yeni kurulumda:

| Yöntem | Ne zaman | Not |
|---|---|---|
| **5×5 L tipi matris** (Olasılık × Şiddet) — varsayılan | Çoğu imalat ve hizmet işletmesi | Anlaşılır, sahada çalışanla birlikte puanlanabilir |
| **Fine-Kinney** (O × F × Ş) | Maruziyet sıklığı riski belirgin değiştiren işler (vardiyalı, rutin dışı bakım yoğun) | Skor aralığı geniş; eşikler 20/70/200/400 |
| HAZOP / FMEA | Proses güvenliği, BEKRA, kimya | 45001 kaydına özet + bağlantı olarak girer |
| Kontrol listesi | Ofis, perakende, az tehlikeli | Küçük kuruluşta tek başına yeterli olabilir |

**Seviye eşikleri tek yerde tanımlanır ve formülle uygulanır.** `kayitlar_45001.py`
bunu yapar (Yöntem sayfası + Risk Seviyesi formülü). Elle yazılmış seviye sütunu,
prosedürdeki matristen kopyalanırken hata taşır — sahada görülen tipik örnek:
prosedür tablosunda aynı skor (12) bir hücrede "Orta", başka hücrede "Yüksek"
yazılmış. Prosedürdeki matris tablosu da kayıttaki eşiklerden üretilmelidir.

L-matris varsayılan eşikleri (kuruluş farklıysa onunkini kullan):
1 Önemsiz · 2–6 Kabul edilebilir · 8–12 Orta (≤3 ay) · 15–20 Önemli (≤1 ay, önlemsiz işe başlanmaz) · 25 Tolere edilemez (iş durur).

---

## 3. Ekip ve katılım (5.4 bağlantısı)

Risk değerlendirmesi 5.4 e-2'nin doğrudan konusudur. Kayıtta ekip listesi
**adıyla ve göreviyle** tutulur; içinde en az bir yönetici olmayan çalışan ve
çalışan temsilcisi bulunur. Saha turu tarihleri ve katılan çalışanlar LS-11'e
"e2 Tehlike/risk belirleme" satırı olarak işlenir — 5.4 kanıtı buradan çıkar.

---

## 4. Kapsam kontrol listesi

Kaydı teslim etmeden önce şu başlıkların her birinden en az bir satır olup
olmadığını kontrol et; yoksa ya ekle (ÖRNEK etiketli) ya da OKUBENI'de "kuruluşla
doğrulanacak" diye yaz:

- [ ] Rutin üretim faaliyetleri — bölüm/hat bazında
- [ ] **Rutin dışı**: bakım, arıza, temizlik (CIP, makine içi), devreye alma, kalibrasyon
- [ ] Yüklenici işleri: inşaat/tadilat, çatı, elektrik, ilaçlama/fümigasyon, temizlik, yemek, güvenlik
- [ ] Ziyaretçi, sürücü (sevkiyat şoförleri), stajyer
- [ ] Acil durum ve anormal koşullar: elektrik kesintisi, buhar/hava kaçağı, yangın, deprem, sel
- [ ] İş ekipmanı: forklift, istif, vinç, manlift, basınçlı kap, kazan, kompresör
- [ ] Kimyasallar ve toz (patlayıcı ortam dahil)
- [ ] Fiziksel etmenler: gürültü, titreşim, termal konfor, aydınlatma
- [ ] Ergonomi ve elle taşıma, tekrarlayan hareket
- [ ] **Psikososyal**: iş yükü, vardiya/gece çalışması, yalnız çalışma, mobbing/şiddet, iş güvencesizliği (ISO 45003 rehber)
- [ ] **İnsan faktörleri**: yorgunluk, dikkat dağınıklığı, dil engeli
- [ ] **İklim (Amd 1:2024)**: ısı stresi, aşırı hava olayları, sel; ayrıca karbon azaltım projelerinin getirdiği yeni tehlikeler (ör. yeni enerji sistemleri). ISO/PAS 45007:2026 rehberdir
- [ ] Özel politika grupları — en az bir değerlendirme satırı veya ayrı bölüm
- [ ] İşyeri dışı: sevkiyat, saha servisi, uzaktan/hibrit çalışma (ofis personeli varsa)

Son üç madde (psikososyal, iklim, uzaktan çalışma) ISO 45001'in 2027 revizyon
taslağında belirgin şekilde öne çıkıyor (DIS 2026); bugünden kayıtta bulunmaları
geçişi kolaylaştırır. Revizyonu kesinleşmiş şart gibi sunma — "yaklaşan revizyonun
odak konuları" diye an.

---

## 5. Kontrol hiyerarşisi (8.1.2)

Her ek önlem satırı hangi kademeye ait olduğunu söyler. KKD tek önlemse ek
önlem sütununda neden üst kademelerin uygulanamadığı yazılır. Denetçinin en sık
sorduğu soru: "Bu riskin önlemi yalnız KKD ve eğitim — mühendislik kontrolü
değerlendirildi mi?"

| Kademe | Örnek |
|---|---|
| Ortadan kaldırma | Yüksekte işi yerde yapılacak şekilde tasarlamak |
| İkame | Solvent bazlı temizleyici yerine su bazlı |
| Mühendislik | Makine koruyucusu, kilitlemeli kapak, lokal havalandırma, ışık perdesi |
| İdari | İş izni, LOTO, rotasyon, talimat, eğitim, işaretleme |
| KKD | Son çare; KKD matrisi (LS-05) ile seçilir |

---

## 6. Sektöre göre başlangıç katalogları (ÖRNEK satır üretirken)

**Gıda / şekerleme / kakao-çikolata işleme:** hareketli makine aksamı (karıştırıcı,
değirmen, konç, kalıplama), sıcak yüzey ve sıcak ürün (temperleme, kavurma),
buhar/kazan, toz patlaması (kakao, şeker, un — ATEX bölgelendirmesi), CIP
kimyasalları (kostik, asit), soğuk oda/donma, forklift-yaya çarpışması, elle
taşıma (çuval), gürültü (değirmen, kırıcı), kayma (yağlı zemin), fümigasyon
(depolanan hammadde), bıçak/falçata (ambalaj açma), gece vardiyası.

**Metal / makine imalatı:** pres, CNC, kaynak dumanı ve UV, taşlama, vinç, gürültü-titreşim.

**Lojistik / depo:** raf devrilmesi, forklift, yükleme rampası, araç manevrası, yüksekte istif.

**Ofis / hizmet:** ergonomi, ekranlı araç, psikososyal, yangın-tahliye, elektrik.

Her kataloğu **ÖRNEK — kuruluşla doğrulanacak** diye işaretle. Kuruluşun gerçek
hat/makine adları gelmeden bu satırlar tamamlanmış sayılmaz.

---

## 7. Sık yapılan hatalar

- Risk değerlendirmesinin tarihi yenileme periyodunu geçmiş — en sık yasal bulgu
- Pandemi döneminde yapılmış, hâlâ Covid satırları ağırlıklı ve güncellenmemiş kayıt
- Seviye sütunu elle yazılmış, matrisle çelişiyor
- Kalan (artık) risk hesaplanmamış — önlemin etkinliği görünmüyor (6.1.4)
- Olay kaydında "RD güncellendi mi?" sorusu yok; kazadan sonra RD satırı değişmemiş
- Yükleniciler ve rutin dışı işler kayıtta yok
- Önlem sütununda "dikkat edilecek", "eğitim verilecek" gibi ölçülemez ifadeler
- Risk ve Fırsat listesi (6.1.1) ile tehlike kaynaklı RD (6.1.2) aynı tabloda karışmış — İSGYS'nin kendisine yönelik risk (ör. İGU'nun ayrılması) ile makine sıkışma riski farklı kayıtlardır
