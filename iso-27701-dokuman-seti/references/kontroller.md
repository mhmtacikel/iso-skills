# ISO/IEC 27701 Kontrol Tabloları — 2019 ↔ 2025 Karşılıklı Eşleme

İki sürümün numaralandırması farklıdır ama **veri sorumlusu ve veri işleyen**
kontrollerinin içeriği büyük ölçüde korunmuştur. 2025'te her alt bölümün ilk
maddesi (`X.Y.1`) *Amaç* beyanına ayrıldığı için kontrol numaraları bir
kayar: 2019 `7.2.1` → 2025 `A.1.2.2`.

Atıf verirken **hangi sürümde çalıştığını doğrula.** Tek bir dokümanda iki
numaralandırmayı karıştırmak denetçide 'hangi standarda göre kurdunuz?'
sorusunu doğurur.

| | 2019 | 2025 |
|---|---|---|
| Veri sorumlusu | Ek A — 31 kontrol | Ek A.1 — 31 kontrol |
| Veri işleyen | Ek B — 18 kontrol | Ek A.2 — 18 kontrol |
| Bilgi güvenliği | *yok* (27002 zemininde) | Ek A.3 — 29 kontrol |
| **Toplam** | **49** | **78** |

**Hariç tutma:** Kontroller gerekçelendirilerek hariç tutulabilir; ana maddeler
(2019'da Madde 5–8, 2025'te Madde 4–10) hariç tutulamaz. Rol gereği
uygulanmayan kontroller (ör. yalnız veri işleyen olan kuruluşta A.1 kontrolleri)
SoA'da 'rol gereği uygulanabilir değil' gerekçesiyle işaretlenir — silinmez.

---

## Veri sorumlusu kontrolleri (2019 Ek A / 2025 Ek A.1)

| 2019 | 2025 | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|---|
| A.7.2.1 | A.1.2.2 | Amacın tanımlanması ve dokümante edilmesi | KVYS-LS-01 Kişisel Veri İşleme Envanteri | Her işleme faaliyeti için yazılı amaç; VERBİS kaydıyla tutarlılık |
| A.7.2.2 | A.1.2.3 | Yasal dayanağın tanımlanması | KVYS-LS-01 §Hukuki Sebep, KVYS-LS-03 Mevzuat Matrisi | KVKK m.5/m.6 dayanak eşlemesi; meşru menfaat testleri |
| A.7.2.3 | A.1.2.4 | Rızanın ne zaman ve nasıl alınacağının belirlenmesi | KVYS-PR-02 Rıza Yönetimi Prosedürü | Rıza gereken/gerekmeyen işleme ayrımı, karar kriterleri |
| A.7.2.4 | A.1.2.5 | Rızanın alınması ve kaydedilmesi | KVYS-FR-02 Açık Rıza Metni, KVYS-LS-05 Rıza Kayıt Defteri | Zaman damgalı rıza kayıtları, metin sürümü, kanal |
| A.7.2.5 | A.1.2.6 | Gizlilik etki değerlendirmesi (PIA/DPIA) | KVYS-PR-03 Etki Değerlendirme Prosedürü, KVYS-FR-03 | Tamamlanmış ve onaylı DPIA raporları, eşik kriterleri |
| A.7.2.6 | A.1.2.7 | Kişisel veri işleyenlerle yapılan sözleşmeler | KVYS-FR-08 Veri İşleyen Sözleşme Eki | İmzalı veri işleyen sözleşmeleri, talimat maddesi |
| A.7.2.7 | A.1.2.8 | Ortak kişisel veri sorumlusu | KVYS-FR-09 Ortak Veri Sorumlusu Mutabakatı | Sorumluluk paylaşım mutabakatı, ilgili kişiye duyurulan özet |
| A.7.2.8 | A.1.2.9 | Kişisel veri işlenmesine ilişkin kayıtlar | KVYS-LS-01 Kişisel Veri İşleme Envanteri | Güncel envanter; VERBİS bildirimi ile eşleşme |
| A.7.3.1 | A.1.3.2 | Veri sahiplerine karşı yükümlülüklerin belirlenmesi ve yerine getirilmesi | KVYS-PR-04 İlgili Kişi Başvuru Prosedürü | Yükümlülük listesi, yerine getirme kanıtı |
| A.7.3.2 | A.1.3.3 | Veri sahiplerine verilecek bilgilerin belirlenmesi | KVYS-FR-01 Aydınlatma Metni | Aydınlatma metni içerik kontrol listesi (KVKK m.10) |
| A.7.3.3 | A.1.3.4 | Veri sahiplerine bilgi verilmesi | KVYS-FR-01, yayım kanalları | Web sitesi/ekran görüntüsü, form üzerindeki metin, duyuru kaydı |
| A.7.3.4 | A.1.3.5 | Rızanın değiştirilmesi veya geri çekilmesine ilişkin mekanizmanın sağlanması | KVYS-PR-02 §Geri Çekme | Geri çekme kanalı, işlenen geri çekme talepleri |
| A.7.3.5 | A.1.3.6 | Veri işlemesine itiraz mekanizmasının sağlanması | KVYS-PR-04 §İtiraz | İtiraz kanalı ve sonuçlandırma kayıtları |
| A.7.3.6 | A.1.3.7 | Erişim, düzeltme ve/veya silme | KVYS-PR-04, KVYS-LS-06 Başvuru Kayıt Defteri | 30 günlük yanıt süresi kanıtı, işlem kayıtları |
| A.7.3.7 | A.1.3.8 | Veri sorumlularının üçüncü tarafları uyarma yükümlülüğü | KVYS-PR-04 §Üçüncü Taraf Bildirimi | Aktarım yapılan taraflara gönderilen düzeltme/silme bildirimleri |
| A.7.3.8 | A.1.3.9 | İşlenen kişisel verilerin kopyasının sağlanması | KVYS-PR-04 §Veri Taşınabilirliği | Kopya/taşınabilirlik talep kayıtları, format tanımı |
| A.7.3.9 | A.1.3.10 | Taleplerin ele alınması | KVYS-LS-06 Başvuru Kayıt Defteri | Süre takibi, ret gerekçeleri, Kurul'a yansıyan şikâyetler |
| A.7.3.10 | A.1.3.11 | Otomatikleştirilmiş karar verme | KVYS-FR-10 Otomatik Karar Envanteri | Otomatik karar veren sistemler listesi, insan müdahale yolu, itiraz hakkı |
| A.7.4.1 | A.1.4.2 | Toplamanın sınırlandırılması | KVYS-PL-01 §Veri Minimizasyonu, KVYS-LS-01 | Toplanan alan listesi ve her alan için gereklilik gerekçesi |
| A.7.4.2 | A.1.4.3 | İşlemenin sınırlandırılması | KVYS-PL-01 §Amaçla Sınırlılık | Amaç dışı işleme kontrolleri, erişim kısıtları |
| A.7.4.3 | A.1.4.4 | Doğruluk ve nitelik | KVYS-PR-05 Veri Kalitesi Prosedürü | Güncelleme mekanizması, doğruluk kontrolleri |
| A.7.4.4 | A.1.4.5 | Kişisel verileri en aza indirme hedefleri | KVYS-FR-04 KVYS Hedefleri | Minimizasyon hedefi, ölçüm ve sonuç |
| A.7.4.5 | A.1.4.6 | Kişisel verilerin işleme sonunda anonim hâle getirilmesi ve silinmesi | KVYS-PR-06 Saklama ve İmha Prosedürü | Anonimleştirme yöntemi, uygulanmış örnekler |
| A.7.4.6 | A.1.4.7 | Geçici dosyalar | KVYS-PR-06 §Geçici Dosyalar | Geçici dosya temizleme mekanizması ve periyodu |
| A.7.4.7 | A.1.4.8 | Saklama (tutma) | KVYS-LS-02 Saklama ve İmha Politikası/Tablosu | Veri türü bazında saklama süresi ve mevzuat dayanağı |
| A.7.4.8 | A.1.4.9 | Yok etme | KVYS-PR-06 §İmha | Periyodik imha tutanakları (KVKK Yönetmelik: 6 aylık periyot) |
| A.7.4.9 | A.1.4.10 | Kişisel veri aktarım kontrolleri | KVYS-PR-07 Aktarım Prosedürü | Aktarım kanalı şifreleme, aktarım öncesi kontrol kayıtları |
| A.7.5.1 | A.1.5.2 | Yetki alanları arası kişisel veri aktarımı için dayanağın tanımlanması | KVYS-LS-04 Yurt Dışı Aktarım Envanteri | KVKK m.9 dayanağı: yeterlilik kararı / standart sözleşme / BKK / açık rıza |
| A.7.5.2 | A.1.5.3 | Kişisel verilerin aktarılabileceği ülkeler ve uluslararası kuruluşlar | KVYS-LS-04 §Ülke Listesi | Ülke listesi, Kurul'a bildirilen standart sözleşmeler |
| A.7.5.3 | A.1.5.4 | Kişisel veri aktarımının kayıtları | KVYS-LS-04 §Aktarım Kayıtları | Her aktarımın kaydı: alıcı, ülke, tarih, dayanak |
| A.7.5.4 | A.1.5.5 | Üçüncü taraflara yapılan kişisel veri ifşalarının kayıtları | KVYS-LS-07 İfşa/Paylaşım Kayıt Defteri | İfşa kayıtları, hukuki dayanak, talep eden makam |

### Alt bölümler

| 2019 | 2025 | Konu |
|---|---|---|
| 7.2 | A.1.2 | Toplama ve işleme koşulları |
| 7.3 | A.1.3 | Veri sahiplerine (ilgili kişilere) karşı yükümlülükler |
| 7.4 | A.1.4 | Tasarım gereği gizlilik ve varsayılan olarak gizlilik |
| 7.5 | A.1.5 | Kişisel verileri paylaşma, aktarma ve ifşa etme |

---

## Veri işleyen kontrolleri (2019 Ek B / 2025 Ek A.2)

| 2019 | 2025 | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|---|
| B.8.2.1 | A.2.2.2 | Müşteri anlaşması | KVYS-FR-11 Veri İşleyen Hizmet Sözleşmesi | İmzalı sözleşmeler; sorumluluk ve talimat maddeleri |
| B.8.2.2 | A.2.2.3 | Kuruluşun amaçları | KVYS-PL-02 §Amaç Sınırı | Müşteri talimatı dışında işleme yapılmadığının kanıtı |
| B.8.2.3 | A.2.2.4 | Pazarlama ve reklam kullanımı | KVYS-PL-02 §Pazarlama Yasağı | Müşteri verisinin pazarlamada kullanılmadığına dair kontrol |
| B.8.2.4 | A.2.2.5 | İhlale sebep olan talimatlar | KVYS-PR-08 Talimat Değerlendirme | Hukuka aykırı talimat tespiti ve müşteriye bildirim kaydı |
| B.8.2.5 | A.2.2.6 | Müşteri yükümlülükleri | KVYS-FR-12 Müşteri Bilgilendirme Formu | Müşteriye sağlanan bilgi ve destek kanıtı |
| B.8.2.6 | A.2.2.7 | Kişisel verilerin işlenmesine ilişkin kayıtlar | KVYS-LS-08 Veri İşleyen İşleme Kayıtları | Müşteri bazında işleme faaliyeti kaydı |
| B.8.3.1 | A.2.3.2 | Veri sahiplerine karşı yükümlülükler | KVYS-PR-04 §Veri İşleyen Rolü | İlgili kişi taleplerinin veri sorumlusuna yönlendirilme kaydı |
| B.8.4.1 | A.2.4.2 | Geçici dosyalar | KVYS-PR-06 §Geçici Dosyalar | Geçici dosya temizleme kanıtı |
| B.8.4.2 | A.2.4.3 | Kişisel verilerin iadesi, aktarımı ve yok edilmesi | KVYS-PR-09 Sözleşme Sonu Prosedürü | Sözleşme bitiminde iade/imha tutanakları |
| B.8.4.3 | A.2.4.4 | Kişisel veri aktarım kontrolleri | KVYS-PR-07 Aktarım Prosedürü | Aktarım güvenlik kontrolleri |
| B.8.5.1 | A.2.5.2 | Yetki alanları arası kişisel veri aktarımına ilişkin dayanak | KVYS-LS-04 Yurt Dışı Aktarım Envanteri | Aktarım dayanağı ve müşteri onayı |
| B.8.5.2 | A.2.5.3 | Kişisel verilerin aktarılabileceği ülkeler ve uluslararası kuruluşlar | KVYS-LS-04 §Ülke Listesi | Müşteriye bildirilen ülke listesi |
| B.8.5.3 | A.2.5.4 | Üçüncü taraflara yapılan kişisel veri ifşalarının kayıtları | KVYS-LS-07 İfşa Kayıt Defteri | İfşa kayıtları |
| B.8.5.4 | A.2.5.5 | Kişisel veri ifşa taleplerinin bildirimi | KVYS-PR-10 Yasal Talep Prosedürü | Kolluk/idari taleplerin müşteriye bildirim kaydı |
| B.8.5.5 | A.2.5.6 | Yasal olarak bağlayıcı kişisel veri ifşaları | KVYS-PR-10 §Bağlayıcı Talepler | Talep, hukuki inceleme ve yanıt kayıtları |
| B.8.5.6 | A.2.5.7 | Kişisel veri işleme için kullanılan alt yüklenicilerin ifşa edilmesi | KVYS-LS-09 Alt Yüklenici Envanteri | Müşteriye açıklanan alt yüklenici listesi |
| B.8.5.7 | A.2.5.8 | Kişisel verilerin işlenmesi için alt yüklenici kullanımı | KVYS-PR-11 Alt Yüklenici Yönetimi | Müşteri onayı, alt yüklenici sözleşmeleri, denetim kayıtları |
| B.8.5.8 | A.2.5.9 | Kişisel veri işleme için kullanılan alt yüklenicinin değişikliği | KVYS-PR-11 §Değişiklik Bildirimi | Alt yüklenici değişikliğinin müşteriye önceden bildirim kaydı |

### Alt bölümler

| 2019 | 2025 | Konu |
|---|---|---|
| 8.2 | A.2.2 | Toplama ve işleme koşulları |
| 8.3 | A.2.3 | Veri sahiplerine karşı yükümlülükler |
| 8.4 | A.2.4 | Tasarım gereği gizlilik ve varsayılan olarak gizlilik |
| 8.5 | A.2.5 | Kişisel verileri paylaşma, aktarma ve ifşa etme |

---

## Bilgi güvenliği kontrolleri — YALNIZCA 2025 (Ek A.3)

2025 sürümü bağımsız bir yönetim sistemi olduğu için, 27001'e dayanamaz ve
kişisel veri koruması açısından kritik bilgi güvenliği kontrollerini kendi
içine almak zorundadır. Bu 29 kontrol ISO/IEC 27002:2022'den seçilmiştir.

**27001 belgesi olan kuruluşta bu kontrollerin çoğu zaten karşılanmıştır.**
O hâlde iş, yeni kontrol kurmak değil, mevcut BGYS kanıtlarını A.3 numaralarına
eşlemektir. 'İlgili doküman' sütununda kendi BGYS doküman kodlarını kullan.

| 2025 | ISO 27002:2022 | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|---|
| A.3.3 | 5.1 | Bilgi güvenliği politikaları | KVYS-PL-03 Bilgi Güvenliği Politikası | Onaylı politika, duyuru kaydı |
| A.3.4 | 5.2 | Bilgi güvenliği rolleri ve sorumlulukları | KVYS-EK-01 §Roller | Görev tanımları, atama yazıları |
| A.3.5 | 5.12 | Bilgilerin sınıflandırılması | KVYS-PL-04 Sınıflandırma Politikası | Sınıflandırma şeması; kişisel veri ayrı sınıf |
| A.3.6 | 5.13 | Bilgilerin etiketlenmesi | KVYS-TL-01 Etiketleme Talimatı | Etiketlenmiş örnekler |
| A.3.7 | 5.14 | Bilgi transferi | KVYS-PR-07 Aktarım Prosedürü | Transfer kuralları ve anlaşmaları |
| A.3.8 | 5.16 | Kimlik yönetimi | KVYS-PR-12 Erişim ve Kimlik Yönetimi | Kimlik yaşam döngüsü kayıtları |
| A.3.9 | 5.18 | Erişim hakları | KVYS-PR-12 §Erişim Hakları | Periyodik erişim gözden geçirme; kişisel veriye erişim log'u |
| A.3.10 | 5.20 | Tedarikçi sözleşmelerinde bilgi güvenliğinin ele alınması | KVYS-FR-08 / FR-11 Sözleşme Ekleri | İmzalı güvenlik ve gizlilik maddeleri |
| A.3.11 | 5.24 | Bilgi güvenliği ihlal olayı yönetimi planlaması ve hazırlığı | KVYS-PR-13 Veri İhlali Yönetim Prosedürü | Rol atamaları, 72 saat Kurul bildirim akışı |
| A.3.12 | 5.26 | Bilgi güvenliği ihlal olaylarına müdahale | KVYS-PR-13 §Müdahale, KVYS-LS-10 İhlal Kayıt Defteri | İhlal kayıtları, Kurul ve ilgili kişi bildirimleri |
| A.3.13 | 5.31 | Yasal, meşru, düzenleyici ve sözleşmeye tabi gereklilikler | KVYS-LS-03 Mevzuat ve Yükümlülük Matrisi | KVKK, ikincil mevzuat, sektörel düzenleme takibi |
| A.3.14 | 5.33 | Kayıtların korunması | KVYS-PR-14 Doküman ve Kayıt Kontrol | Saklama planı, erişim kısıtları |
| A.3.15 | 5.35 | Bilgi güvenliğinin bağımsız gözden geçirilmesi | KVYS-PR-15 İç Tetkik Prosedürü | Bağımsız gözden geçirme raporu |
| A.3.16 | 5.36 | Bilgi güvenliğine yönelik politikalar, kurallar ve standartlara uygunluk | KVYS-PR-16 Uygunluk Gözden Geçirme | Uyum kontrol listeleri ve sonuçları |
| A.3.17 | 6.3 | Bilgi güvenliği farkındalığı, eğitim ve öğretim | KVYS-PN-02 Farkındalık ve Eğitim Planı | Eğitim kayıtları; kişisel veri farkındalık içeriği |
| A.3.18 | 6.6 | Gizlilik veya ifşa etmeme anlaşmaları | KVYS-FR-13 Gizlilik Taahhütnamesi | İmzalı taahhütnameler (çalışan ve tedarikçi) |
| A.3.19 | 7.7 | Temiz masa ve temiz ekran | KVYS-PL-05 Kabul Edilebilir Kullanım | Periyodik denetim kayıtları |
| A.3.20 | 7.10 | Depolama ortamı | KVYS-PR-17 Ortam Yönetimi | Ortam envanteri, taşıma ve imha kayıtları |
| A.3.21 | 7.14 | Ekipmanın güvenli bir şekilde yok edilmesi veya tekrar kullanılması | KVYS-PR-17 §Güvenli İmha | İmha tutanakları, veri silme sertifikaları |
| A.3.22 | 8.1 | Kullanıcı uç nokta cihazları | KVYS-PL-06 Uç Nokta Politikası | MDM/şifreleme yapılandırması |
| A.3.23 | 8.5 | Güvenli kimlik doğrulama | KVYS-PR-12 §Kimlik Doğrulama | MFA yapılandırma kanıtı |
| A.3.24 | 8.13 | Bilgi yedekleme | KVYS-PR-18 Yedekleme Prosedürü | Yedek kayıtları, geri dönüş testi; yedekte saklama süresi uyumu |
| A.3.25 | 8.15 | Kaydetme (log tutma) | KVYS-PR-19 Log Yönetimi | Kişisel veriye erişim log'ları, saklama süresi, bütünlük |
| A.3.26 | 8.24 | Kriptografi (şifreleme) kullanımı | KVYS-PL-07 Kriptografi Politikası | Şifreleme standartları, anahtar yönetimi |
| A.3.27 | 8.25 | Güvenli geliştirme yaşam döngüsü | KVYS-PR-20 Güvenli Geliştirme | SDLC tanımı, güvenlik kapıları |
| A.3.28 | 8.26 | Uygulama güvenlik gereklilikleri | KVYS-PR-20 §Güvenlik Gereksinimleri | Gereksinim listesi; tasarım gereği gizlilik kanıtı |
| A.3.29 | 8.27 | Güvenli sistem mimarisi ve mühendislik ilkeleri | KVYS-PR-20 §Mimari | Mimari prensipler, tehdit modelleme |
| A.3.30 | 8.30 | Dış kaynak yoluyla geliştirme | KVYS-PR-11 §Dış Geliştirme | Sözleşme maddeleri, kabul testleri |
| A.3.31 | 8.33 | Test bilgisi | KVYS-PL-08 Test Verisi Politikası | Test ortamında maskeleme/anonimleştirme kanıtı |

---

## 2025'in diğer ekleri (bilgi amaçlı)

| Ek | İçerik | Ne işe yarar |
|---|---|---|
| Ek B (normatif) | A.1/A.2/A.3 için uygulama kılavuzu (B.1/B.2/B.3) | Her kontrolün nasıl uygulanacağı |
| Ek C | ISO/IEC 29100 gizlilik çerçevesi eşlemesi | Gizlilik ilkeleriyle hizalama |
| Ek D | GDPR eşlemesi | AB müşterisi olan kuruluşlar için |
| Ek E | ISO/IEC 27018 ve 29151 eşlemesi | Bulut hizmet sağlayıcıları için |
| Ek F | ISO/IEC 27701:2019 eşlemesi | Geçiş yaparken doğrulama kaynağı |

Ek F, bu dosyadaki 2019↔2025 eşlemesinin resmî karşılığıdır. Kullanıcının
standarda erişimi varsa geçiş çalışmasında oradan teyit etmesini öner.
