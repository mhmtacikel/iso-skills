# Mevcut İSG Doküman Setinin Analizi ve Yenilenmesi

Türkiye'de 45001 işi çoğu zaman sıfırdan kurulum değil, **yıllardır biriken bir
setin yenilenmesidir**: OHSAS 18001 döneminden kalma prosedürler, sonradan eklenmiş
talimatlar, iki farklı kodlama düzeni, arşivle karışmış güncel dosyalar. Bu dosya
gerçek bir gıda üreticisinin ~280 dosyalık İSG klasörünün incelenmesinden
genelleştirilmiş desenleri ve izlenecek yolu verir.

> Kuruluşun dosyaları **asla silinmez, üzerine yazılmaz**. Yeni sürümler ayrı
> klasöre / ayrı adla üretilir. Silme/taşıma kararı kullanıcınındır.

---

## 1. İş akışı

1. **Envanter (script ile, kullanıcının bilgisayarında):**
   `python3 scripts/envanter.py "<klasör>" "<klasör>/../İSGYS Envanter.xlsx"`
   — dosya adı + docx/xlsx antetinden kod, revizyon, yürürlük; çöp dosya, kopya,
   kod çakışması, formül hatası bulguları. `.doc/.xls` çoksa önce
   `soffice --headless --convert-to docx` ile **geçici kopyada** dönüştür (kendi
   scratch alanında, kullanıcı klasöründe değil).
2. **İçerik okuması (yalnız çekirdek dokümanlar):** politika, prosedürler, risk
   değerlendirmesi, yasal şart listesi, acil durum planı, organizasyon şeması.
   Talimat/form içerikleri örnekleme ile okunur (her türden 2–3).
3. **Madde bazlı boşluk analizi:** `madde-4-10.md` tablosundaki her satır için
   "var / kısmen / yok" + kanıt dosyası.
4. **Kullanıcıya bilgi ver, karar al:** kodlama (mevcut korunacak mı, aile kodu
   mu), birleştirilecek dokümanlar, iptal edilecekler, kapsam. Üretmeden önce
   anlat — kullanıcı onaylamadan toplu üretim yapma.
5. **Üret:** önce eksik süreçler (genelde 5.4, 8.1.3, 8.1.4, 4.1/4.2), sonra
   revize edilecekler, en son kod geçiş tablosu ve doküman ana listesi.

---

## 2. Sık görülen bulgu desenleri ve ne yapılacağı

### Doküman kontrolü (7.5)

| Desen | Neden sorun | Ne yap |
|---|---|---|
| İki kodlama düzeni yan yana (ör. `01-PR-004` ve `1000-11-PR-014`) | Hangi kodun geçerli olduğu belirsiz; çapraz referans kopar | Kod Geçiş Tablosu (yol gösterici) üret: eski → yeni → durum |
| Aynı kod farklı belgelere verilmiş (ör. `01-LS-006` hem kaldırma araçları hem transpalet listesi) | Doküman kimliği tekil değil | Birine yeni kod öner, geçiş tablosunda göster |
| Aynı dokümanın birden çok sürümü aktif klasörde (`rev.2`, `rev.3`, `(1)`, `Kopya ...`, `_FİLİGRAN`, TR-EN varyantı) | Sahada eski sürüm kullanılabilir | Yürürlükteki tek sürümü belirle; diğerleri için "arşive taşınması önerilir" listesi |
| Formun adında yıl (`... 2019`, `... 2020`) | Şablon ile doldurulmuş kayıt karışmış | Şablon yılsız; kayıt ayrı klasör |
| `iptal` adlı dosya aktif klasörde | İptal edilmiş doküman erişilebilir | İptal listesi |
| Çöp dosyalar (`~$`, `Thumbs.db`, `.tmp`, `debug.log`) | Doküman değil | Envantere almadan raporla |
| Eski biçim (`.doc`, `.xls`, `.ppt`) çoğunlukta | Antet okunamaz, izlenebilirlik zayıf | Yeni sürümler docx/xlsx |
| Revizyon no / tarih boş | 7.5.2 onay ve tanımlama eksik | Bulgu |
| Birden fazla doküman kontrol prosedürü (Kalite, İSG, Çevre ayrı) | Çelişen kurallar | Tek prosedür — diğer sistem sahiplerinin onayıyla (karar maddesi) |
| İlgili dokümanlar bölümünde var olmayan kodlar | Kırık referans | Geçiş tablosundan düzelt |

### İçerik (45001 uyumu)

| Desen | Madde | Ne yap |
|---|---|---|
| Prosedürlerde "OHSAS 18001", "Yönetimin Çevre ve İSG Temsilcisi" zorunlu rol, "Düzeltici ve **Önleyici** Faaliyet" | Genel, 10.2 | Revizyon rehberinde işaretle; yeni sürümde 45001 terimleri |
| YGG prosedürü 27001/9001/22000 için ortak ama İSG girdileri (danışma-katılım, olay eğilimleri, yasal uygunluk, iklim) yok | 9.3 | EYS YGG'ye İSG girdi listesi ekle |
| Çalışan danışma ve katılımı için süreç yok; yalnız kurul | 5.4 | PR-05 + LS-11 |
| Değişiklik yönetimi yalnız "yeni makine devreye alma" | 8.1.3 | PR-10 (tüm değişiklik türleri) |
| Yükleniciler yalnız ceza şartnamesi/tebliğ tutanağıyla yönetiliyor | 8.1.4 | PR-11 + LS-10 (seçim kriteri, RD koordinasyonu, izleme); ceza şartnamesi prosedür eki olarak korunur |
| SWOT var, ilgili taraf ihtiyaç-beklenti analizi ve iklim kararı yok | 4.1, 4.2 | LS-03 |
| Risk ve fırsat listesi var ama tehlike RD'siyle aynı kavramlar karışmış | 6.1.1 / 6.1.2 | İkisini ayır |
| RD prosedüründe kontrol hiyerarşisi yok; matris tablosunda tutarsız seviye | 8.1.2, 6.1.2.2 | PR-03 yeniden; seviyeler formülle |
| RD dosyaları yenileme süresini geçmiş / pandemi ağırlıklı | 6.1.2, yasal | Boşluk raporunda **ilk sıra** (yasal risk) |
| Politika 5.2 taahhütlerinden "tehlikeleri ortadan kaldırma ve riskleri azaltma" eksik; "gerektiğinde gözden geçirir" | 5.2 | Revize metin öner; gözden geçirme sıklığını sayıyla yaz |
| Mevzuat listesinde mülga tüzükler, eski RG tarihleri, Excel tarih seri no'ları (44193 gibi) görünüyor | 6.1.3 | Yeni LS-04 |
| Excel kayıtlarında `#VALUE!`, ağırlıklar 100'e toplanmıyor | 9.1 | Yeni kayıtlar formül kontrollü |
| Rol unvanları dokümandan dokümana farklı | 5.3 | Rol tablosu (EK-01 eki), tüm sette tek ad |
| Eğitim prosedürü 2026 değişikliğini (3 ay, ders saati, yüz yüze 4. başlık) içermiyor | 7.2, yasal | PR-06 revizyonu |

### Kayıtlarda veri gizliliği

Kaza formu, sağlık tarama listesi, engelli çalışan listesi gibi kayıtlarda tanı/sağlık
bilgisi görülürse: bu **özel nitelikli kişisel veridir** (KVKK m.6). Analiz çıktısına
kişisel veri kopyalama; yalnız "şu dosyada sağlık verisi var, erişim kısıtı ve
saklama süresi tanımlı mı?" bulgusu yaz. Envanter scripti içerik değil yalnız antet okur.

---

## 3. Revizyon rehberi formatı (yol gösterici)

Her mevcut doküman için tek satır:

`Mevcut kod | Ad | Rev | Karar (Koru / Revize et / Birleştir → kod / İptal) | Gerekçe (madde) | Yeni kod | Öncelik | Sorumlu`

Öncelik sırası: (1) yasal risk (RD yenileme, eğitim, periyodik kontrol), (2) majör
uygunsuzluk adayı (5.4, 8.1.3, 8.1.4, 6.1.2 yöntem), (3) doküman kontrolü, (4) biçim.

---

## 4. Proje belleği (çok oturumlu işler)

Büyük bir seti yenilemek tek oturumda bitmez. Kullanıcının klasöründe bir proje
belleği tut (kullanıcı onaylarsa): `00-PROJE/00-PROJE-DURUM.md` (nerede kalındı,
açık sorular), `01-KARARLAR.md` (K-01, K-02 … kalıcı kararlar), `02-BULGULAR.md`
(envanter ve boşluk özeti). Her oturum bu dosyaları okuyarak başlar, güncelleyerek
biter. Kuruluşa özel bir proje skill'i varsa (ör. `altinmarka-cisg-dokuman-sistemi`)
onun kararları bu skill'in varsayılanlarının önüne geçer.
