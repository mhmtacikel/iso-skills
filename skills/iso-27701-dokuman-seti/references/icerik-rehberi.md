# İçerik Rehberi — Kalite Çıtası ve Örnek Metinler

## İçindekiler

- 1. Kapsam beyanı
- 2. İşleme envanteri satırı
- 3. Hukuki sebep ifadesi
- 4. Aydınlatma metni
- 5. DPIA eşiği
- 6. Saklama süresi
- 7. Veri ihlali kaydı
- 8. İlgili kişi başvurusu
- 9. `[DOLDURULACAK]` ve `[ÖRNEK]`
- 10. Ton kontrolü

Her örneğin zayıf ve güçlü sürümü verilmiştir. Zayıf sürümler gerçek
denetimlerde bulgu almış kalıplardır.

---

## 1. Kapsam beyanı

**Zayıf:** "Şirketimizde işlenen tüm kişisel veriler KVYS kapsamındadır."

**Güçlü (2025, her iki rol):**
> Bu kişisel veri yönetim sistemi, ACME İnsan Kaynakları A.Ş.'nin İstanbul
> Ümraniye Merkez Ofisi'nde;
>
> - **veri sorumlusu** sıfatıyla kendi çalışanları, iş başvurusu yapan adaylar,
>   tedarikçi çalışanları ve ziyaretçilerine ait kişisel verilerin işlenmesi,
> - **veri işleyen** sıfatıyla kurumsal müşterileri adına yürüttüğü bordro ve
>   özlük yönetimi hizmeti kapsamında müşteri çalışanlarına ait kişisel
>   verilerin işlenmesi
>
> faaliyetlerini kapsar. Kapsanan işleme faaliyetleri KVYS-LS-01 Kişisel Veri
> İşleme Envanteri Rev. 02'de listelenmiştir.
>
> **Kapsam dışı:** Grup şirketi ACME Bilişim A.Ş. adına yürütülen faaliyetler,
> ayrı tüzel kişilik ve ayrı veri sorumlusu olması nedeniyle kapsam dışıdır.
>
> Uygulanabilirlik Bildirgesi KVYS-LS-11 Rev. 01 geçerlidir.

**Güçlü (2019 ek cümlesi):**
> Bu KVYS, BGYS-PL-00 Rev. 03 ile tanımlanan bilgi güvenliği yönetim sisteminin
> bir uzantısı olup, kapsamı BGYS kapsamı içinde kalmaktadır.

Rolü **faaliyet grubuyla birlikte** yazmak 27701'e özgüdür ve denetçinin ilk
sorusunu peşinen yanıtlar.

---

## 2. İşleme envanteri satırı

**Zayıf:** `İK | Çalışan verileri | Özlük | Süresiz`

Rol yok, hukuki sebep yok, saklama dayanağı yok, "süresiz" saklama KVKK m.4/2-d
ile çelişir.

**Güçlü:**

| Alan | Değer |
|---|---|
| Faaliyet No | İF-012 |
| Faaliyet Adı | Çalışan özlük dosyasının oluşturulması ve yönetimi |
| Kuruluşun Rolü | Veri sorumlusu |
| İlgili Kişi Grubu | Kadrolu çalışanlar (istihdam süresi boyunca ve sonrasında) |
| Veri Kategorileri | Kimlik, iletişim, özlük, finans (banka/IBAN), eğitim, aile durumu (AGİ için) |
| Özel Nitelikli | Var — sağlık (işe giriş muayene raporu, rapor kayıtları) |
| İşleme Amacı | İş sözleşmesinin kurulması ve ifası, ücret ve yan hak yönetimi, yasal bildirimlerin yapılması (SGK, İŞKUR), iş sağlığı ve güvenliği yükümlülükleri |
| Hukuki Sebep | Genel veri: KVKK m.5/2-c (sözleşmenin ifası) ve m.5/2-a (kanunlarda öngörülme). Özel nitelikli sağlık verisi: m.6/3 çerçevesinde iş sağlığı ve güvenliği yükümlülüğü kapsamında; işyeri hekimi tarafından işlenir. **Açık rıza alınmaz** — hukuki sebep mevcuttur. |
| Toplama Yöntemi | İşe giriş formu (fiziksel), İK portalı (elektronik), işyeri hekimliği |
| Aktarılan Taraflar | SGK, İŞKUR, bankası (maaş ödemesi), mali müşavir (TED-003), işyeri hekimi |
| Yurt Dışına Aktarım | Yok |
| Saklama Süresi | İş sözleşmesinin sona ermesinden itibaren 10 yıl |
| Saklama Dayanağı | [DOLDURULACAK: hukuk birimince teyit edilecek — genel zamanaşımı ve iş mevzuatı kaynaklı süreler] |
| İmha Yöntemi | Fiziksel: kâğıt imha makinesi. Elektronik: güvenli silme + yedeklerden çıkarma |
| Teknik Tedbirler | Erişim kontrolü (yalnız İK ve yönetici), disk şifreleme, erişim log'u |
| İdari Tedbirler | Gizlilik taahhütnamesi, yıllık KVKK eğitimi, temiz masa |
| Aydınlatma Metni | KVYS-FR-01/Çalışan Rev. 02 |
| Rıza Gerekiyor mu | Hayır — hukuki sebep m.5/2-c ve m.5/2-a |
| DPIA Gerekli mi | Evet — özel nitelikli veri işlendiği için. DPIA No: ED-004 |
| Sistem / Ortam | İK portalı (Sistem-07), fiziksel özlük arşivi (Arşiv Odası B-2) |
| Son Güncelleme | 2026-08-11 |

Bu tek satır, denetçinin bir işleme faaliyeti hakkında soracağı soruların
neredeyse tamamını yanıtlar.

---

## 3. Hukuki sebep ifadesi

**Zayıf:** "Açık rıza"

Çoğu işlemede açık rıza **yanlış** hukuki sebeptir. Sözleşmenin ifası veya
kanunda öngörülme varken rıza almak, rızayı özgür irade olmaktan çıkarır ve
ilgili kişi rızayı geri çekince işlemenin dayanağı çöker.

**Güçlü:**
> **Hukuki sebep:** KVKK m.5/2-f (ilgili kişinin temel hak ve özgürlüklerine
> zarar vermemek kaydıyla, veri sorumlusunun meşru menfaati).
>
> **Meşru menfaat testi (özet):** İşyeri girişinde kamera kaydı, hırsızlık ve
> yetkisiz giriş risklerine karşı işletmenin ve çalışanların güvenliği için
> gereklidir. Dengeleme: kayıt yalnızca giriş-çıkış noktalarına yönlendirilmiş,
> çalışma alanları ve dinlenme alanları kapsam dışıdır; kayıtlar 30 gün sonra
> otomatik silinir; erişim Güvenlik Müdürü ile sınırlıdır; ilgili kişiler
> girişteki levha ve aydınlatma metniyle bilgilendirilmiştir. Bu önlemlerle
> ilgili kişinin temel hak ve özgürlüklerine zarar verilmediği değerlendirilmiştir.
> Test tarihi: 2026-03-14, Değerlendiren: Uyum Müdürü.

Meşru menfaate dayanıyorsan **dengeleme testini yaz.** Yazılı test olmadan meşru
menfaat savunulamaz ve denetimde en çok sorgulanan hukuki sebeptir.

---

## 4. Aydınlatma metni

**Zayıf:** "Kişisel verileriniz mevzuata uygun olarak işlenmektedir. Haklarınız
için bize başvurabilirsiniz."

Amaç yok, aktarım yok, hukuki sebep yok, haklar sayılmamış.

**Güçlü (yapı):**
> **ACME İnsan Kaynakları A.Ş. Çalışan Adayı Aydınlatma Metni**
>
> **1. Veri sorumlusu:** ACME İnsan Kaynakları A.Ş., [adres], [MERSİS/VKN].
> KVKK irtibat kişisi: [unvan], [e-posta].
>
> **2. İşlenen kişisel verileriniz:** Kimlik (ad, soyad, doğum tarihi),
> iletişim (telefon, e-posta, adres), eğitim ve mesleki deneyim bilgileri,
> referans bilgileri, varsa tarafınızca paylaşılan görsel (fotoğraf).
>
> **3. İşleme amacı:** Açık pozisyonlara uygunluğunuzun değerlendirilmesi,
> mülakat sürecinin yürütülmesi, işe alım kararının verilmesi ve olumsuz
> sonuçlanan başvurularda ileride açılacak pozisyonlar için havuzda tutulması.
>
> **4. Hukuki sebep:** Başvurunuzun değerlendirilmesi, KVKK m.5/2-c uyarınca
> sözleşmenin kurulmasıyla doğrudan ilgili olması sebebine dayanır. Başvuru
> havuzunda tutulması ise **açık rızanıza** dayanır ve rıza vermemeniz
> başvurunuzun değerlendirilmesini etkilemez.
>
> **5. Aktarım:** Verileriniz, başvurduğunuz pozisyonun bağlı olduğu birim
> yöneticisi ile paylaşılır. [Kullanılan işe alım platformu] altyapısı
> [ülke]'de barındırılmakta olup bu kapsamda yurt dışına aktarım söz konusudur;
> aktarım [KVKK m.9 dayanağı] çerçevesinde yapılmaktadır.
>
> **6. Toplama yöntemi:** Kariyer sayfamız üzerinden ilettiğiniz başvuru formu,
> tarafınızca gönderilen özgeçmiş ve mülakat notları aracılığıyla elektronik
> ortamda toplanır.
>
> **7. Saklama süresi:** Başvurunuz olumsuz sonuçlanırsa verileriniz [süre]
> sonunda imha edilir; havuzda tutulmasına rıza verdiyseniz [süre] boyunca
> saklanır.
>
> **8. Haklarınız (KVKK m.11):** [maddenin tüm bentleri sayılır]
>
> **9. Başvuru:** Taleplerinizi [kanallar] üzerinden iletebilirsiniz; en geç
> 30 gün içinde yanıtlanır.

**Kritik detay 4. maddede:** rıza gerektiren ve gerektirmeyen işlemenin
ayrıştırılması ve "rıza vermemeniz başvurunuzu etkilemez" ifadesi. Bu cümle
rızanın özgür iradeye dayandığının kanıtıdır.

---

## 5. DPIA eşiği

**Zayıf:** "Gerekli görülen hâllerde gizlilik etki değerlendirmesi yapılır."

**Güçlü:**
> **DPIA zorunluluk kriterleri (KVYS-PR-03 §4)** — aşağıdakilerden **en az
> biri** varsa DPIA yapılır ve işleme başlamadan önce tamamlanır:
>
> 1. Özel nitelikli kişisel veri işleniyorsa (KVKK m.6)
> 2. Kişiler hakkında otomatik karar veriliyor veya profilleme yapılıyorsa
> 3. Sistematik izleme söz konusuysa (kamera, konum, çalışan aktivite izleme)
> 4. Çocuklara ait veri işleniyorsa
> 5. Büyük ölçekli işleme varsa — bu kuruluş için eşik: **10.000'den fazla
>    ilgili kişi** veya **50.000'den fazla kayıt**
> 6. Yeni bir teknoloji kullanılıyorsa (biyometrik, YZ tabanlı analiz)
> 7. Yurt dışına aktarım, yeterlilik kararı bulunmayan bir ülkeye yapılıyorsa
> 8. İki veya daha fazla veri setinin eşleştirilmesi/birleştirilmesi varsa
>
> Kriter karşılanmıyorsa gerekçesi işleme envanterinin "DPIA Gerekli mi"
> sütununa yazılır — boş bırakılmaz.
>
> **Yeniden değerlendirme:** İşleme amacı, veri kategorisi, aktarım yapısı veya
> kullanılan teknoloji değiştiğinde ve en geç iki yılda bir tekrarlanır.

5. maddedeki sayıyı kuruluşun ölçeğine göre belirle ve gerekçelendir. Sayı
vermeden "büyük ölçekli" demek ölçülemez.

---

## 6. Saklama süresi

**Zayıf:** `Müşteri verileri | 10 yıl`

**Güçlü:**

| Alan | Değer |
|---|---|
| Veri kategorisi | Müşteri fatura ve ödeme kayıtları |
| İlgili faaliyet | İF-005 Satış ve tahsilat |
| Saklama süresi | 10 yıl |
| Sürenin başlangıcı | Faturanın düzenlendiği hesap döneminin kapanışı |
| Saklama dayanağı | [DOLDURULACAK: ticari defter ve belgelere ilişkin saklama yükümlülüğü — hukuk birimince madde numarasıyla teyit edilecek] |
| Saklama ortamı | ERP (Sistem-03), yedek: nesne depolama |
| İmha yöntemi | Elektronik: güvenli silme; yedeklerden 90 gün içinde düşer |
| Periyodik imha dönemi | 6 ayda bir (Haziran / Aralık) |
| Sorumlu | Mali İşler Müdürü |

**Yedekler satırını atlama.** "Sildik" diyen ama yedekte kopyası duran kuruluş,
ilgili kişinin silme talebini karşılamamış olur. Yedekten düşme süresi ve
yedekten geri yükleme hâlinde yeniden silme mekanizması yazılı olmalı.

---

## 7. Veri ihlali kaydı

**Zayıf:** "14 Mart'ta bir e-posta yanlış kişiye gitti, özür dilendi, kapatıldı."

**Güçlü:**
> **İhlal No:** İHL-2026-003
> **Tespit:** 2026-03-14 09:20 (gönderen çalışanın kendi bildirimi)
> **Öğrenme (72 saat başlangıcı):** 2026-03-14 09:20
> **Tip:** Gizlilik ihlali — yetkisiz ifşa
> **Ne oldu:** Bordro özet dosyası, otomatik tamamlama nedeniyle benzer adlı
> yanlış bir kurumsal alıcıya gönderildi.
> **Etkilenen veri:** Kimlik (ad-soyad), özlük (unvan), finans (net ücret).
> Özel nitelikli veri **yok**.
> **Etkilenen kişi sayısı:** 47 çalışan.
> **İlgili faaliyet:** İF-014 Bordro hazırlama
> **Olası sonuçlar:** Ücret bilgisinin üçüncü tarafça bilinmesi; maddi zarar
> beklenmiyor, ancak mahremiyet ve iş ilişkilerinde olumsuz etki riski var.
> **Acil müdahale:** 09:35'te alıcı telefonla arandı, dosyayı açmadan sildiğini
> teyit etti ve yazılı teyit gönderdi (Ek-1). E-posta geri çağırma denendi
> (başarısız).
> **Kurul'a bildirim değerlendirmesi:** Yapıldı — 2026-03-14 16:40, Veri İhlali
> Müdahale Ekibi kararı. Etkilenen kişi sayısı ve veri niteliği gereği bildirim
> yapılmasına karar verildi. **Bildirim: 2026-03-15 11:20 — 72 saat içinde ✓**
> **İlgili kişilere bildirim:** 2026-03-15 tarihinde 47 çalışana e-posta ile
> yapıldı; içerik Ek-2'de.
> **Kök neden:** E-posta istemcisinde harici alıcılar için uyarı mekanizması
> yok; bordro dosyaları şifresiz gönderiliyordu.
> **Düzeltici faaliyet (DÖF-2026-009):** (a) Harici alıcı uyarısı etkinleştirildi;
> (b) bordro dosyaları için parola koruması zorunlu hâle getirildi;
> (c) İK ekibine hedefli eğitim. Etkinlik doğrulama: 2026-06-15.
> **Kapanış:** 2026-03-28 · **Durum:** Kapalı

Kayıtta **saat** olmalı — 72 saat gün üzerinden hesaplanmaz.

---

## 8. İlgili kişi başvurusu

**Zayıf:** "Başvurular değerlendirilir ve yanıtlanır."

**Güçlü (prosedür maddesi):**
> **5.3 Süre yönetimi.** Başvurunun kuruluşa ulaştığı tarih, KVYS-LS-06 Başvuru
> Kayıt Defteri'ne aynı iş günü içinde işlenir ve 30 günlük süre bu tarihten
> başlar. Kayıt defterindeki "Kalan Gün" sütunu otomatik hesaplanır; 20. günde
> sorumluya, 25. günde Uyum Müdürü'ne otomatik uyarı gider.
>
> Talebin yerine getirilmesi ayrı bir maliyet gerektiriyorsa, Tebliğ'de
> belirlenen sınırlar dâhilinde ücret alınabilir; ücret talebi de 30 günlük
> süre içinde iletilir ve süreyi durdurmaz.
>
> **5.4 Ret.** Talep reddedilecekse gerekçe yazılı olarak bildirilir; hangi
> hukuki dayanağa (KVKK m.28 istisnası, hakkın kapsamı dışı olması vb.)
> dayanıldığı belirtilir. İlgili kişiye Kurul'a şikâyet hakkı hatırlatılır.

---

## 9. `[DOLDURULACAK]` ve `[ÖRNEK]`

- `[DOLDURULACAK: hukuk birimince teyit edilecek saklama süresi ve mevzuat maddesi]`
- `[ÖRNEK — doğrulanacak]` — ürettiğin envanter satırları, örnek riskler

**27701'de özellikle katı ol.** Uydurulamayacaklar: gerçekleşmiş ilgili kişi
başvuruları, gerçek ihlal kayıtları, imzalı rıza kayıtları, VERBİS kayıt
numarası, Kurul bildirim referansı, tamamlanmış DPIA sonuçları.

**Mevzuat maddesi numarası uydurma.** KVKK'nın temel maddeleri (m.4, 5, 6, 7,
9, 10, 11, 12, 13, 16, 28) bilinen ve sabit hükümlerdir; bunlara atıf verebilirsin.
Ancak ikincil mevzuatın madde numaraları, süreler, eşikler ve Kurul kararları
zaman içinde değişir — bunları `[DOLDURULACAK: teyit edilecek]` bırak veya
kullanıcıya doğrulatmasını söyle. Yanlış madde numarası, doküman setinin
tümünün güvenilirliğini düşürür.

---

## 10. Ton kontrolü

1. **Envanterdeki her satırın hukuki sebebi yazılı mı?** Yoksa sistem çalışmıyor.
2. **Aydınlatma ile rıza ayrı dosyalarda mı?** Birleştirdiysen ayır.
3. **Her saklama süresinin başlangıcı ve dayanağı var mı?**
4. **Kontrol atıfları doğru sürümün numaralandırmasıyla mı?** (2019: `7.2.1`,
   2025: `A.1.2.2`)
5. **"İlgili kişi" ile "müşteri/kullanıcı" karıştırılmış mı?** İlgili kişi,
   verisi işlenen gerçek kişidir; müşteri tüzel kişi olabilir.
6. **Bu metinde uydurulmuş bir mevzuat maddesi, süre veya sayı var mı?**
