# Doküman Mimarisi — Kodlama, Hiyerarşi, İçerik Kalıpları

Bu dosya dört yönetim sistemi skill'inde ortaktır. Standarda özgü doküman listesi
ayrı dosyadadır; burada **her doküman için geçerli** kurallar var.

## İçindekiler

1. [Doküman hiyerarşisi](#1-doküman-hiyerarşisi)
2. [Kodlama sistemi](#2-kodlama-sistemi)
3. [Klasör yapısı](#3-klasör-yapısı)
4. [Zorunlu ortak bölümler](#4-zorunlu-ortak-bölümler)
5. [Doküman tipi içerik kalıpları](#5-doküman-tipi-içerik-kalıpları)
6. [Yazım dili ve ton](#6-yazım-dili-ve-ton)
7. [Denetçinin dokümanda aradığı izler](#7-denetçinin-dokümanda-aradığı-izler)

---

## 1. Doküman hiyerarşisi

Belgelendirme denetçisi dokümantasyonu bir piramit olarak okur. Üstteki katman
*niyeti*, alttaki katman *kanıtı* verir. Bir katmanı atlarsanız zincir kopar ve
"uygulama kanıtı yok" bulgusu gelir.

| Seviye | Tip | Ne yapar | Onay | Tipik sayı |
|---|---|---|---|---|
| 1 | El Kitabı / Kapsam | Sistemin sınırlarını ve mimarisini anlatır | Üst yönetim | 1 |
| 2 | Politika (PL) | Taahhüt ve ilke beyanı; "ne" ve "neden" | Üst yönetim | 1 ana + konuya özgü |
| 3 | Prosedür (PR) | Süreç akışı; "kim, ne zaman, hangi sırayla" | Süreç sahibi + YS yöneticisi | 8–15 |
| 4 | Talimat (TL) | Tekil işin adım adım yapılışı | Süreç sahibi | Gerektiği kadar |
| 5 | Form / Liste (FR/LS) | Doldurulacak boş şablon | YS yöneticisi | 15–30 |
| 6 | Kayıt (KY) | Doldurulmuş form = uygulamanın kanıtı | — | Sürekli |
| 7 | Plan (PN) | Zaman/kaynak bağlı program (tetkik, eğitim, risk işleme) | Üst yönetim | 4–8 |

**Kritik nokta:** Skill politika–prosedür–form üretir. Kayıtları (seviye 6)
kuruluş üretir; skill bunları **örnek doldurulmuş** olarak üretebilir ama bunu
açıkça "ÖRNEK — gerçek kayıtla değiştirilecek" diye işaretlemelidir. Sahte kayıt
üretip gerçekmiş gibi sunmak denetimde sistemi çökertir ve etik değildir.

---

## 2. Kodlama sistemi

Kullanıcının kendi kodlama kuralı varsa **onu kullan** — sorup öğren. Yoksa:

```
[SİSTEM]-[TİP]-[SIRA]        örn. BGYS-PR-04
[SİSTEM]-[TİP]-[SIRA].[REV]  revizyonu koda gömmek isteyenler için
```

| Sistem kısaltması | Standart |
|---|---|
| BGYS | ISO/IEC 27001 — Bilgi Güvenliği Yönetim Sistemi |
| İSYS | ISO 22301 — İş Sürekliliği Yönetim Sistemi |
| HYYS | ISO/IEC 20000-1 — Hizmet Yönetim Sistemi |
| YZYS | ISO/IEC 42001 — Yapay Zekâ Yönetim Sistemi |
| EYS  | Entegre Yönetim Sistemi (birden çok standart tek gövdede) |

| Tip kodu | Anlam |
|---|---|
| EK | El Kitabı |
| PL | Politika |
| PR | Prosedür |
| TL | Talimat |
| PN | Plan |
| FR | Form |
| LS | Liste / Envanter |
| RP | Rapor |

Entegre kurulumda ortak dokümana `EYS-` öneki verilir (örn. `EYS-PR-01 Doküman
Kontrol Prosedürü`), standarda özgü olana kendi öneki. Aynı prosedürü iki kez
yazma — bir kez yaz, kapsam bölümünde her iki standardın maddesine atıf ver.

---

## 3. Klasör yapısı

```
[Kuruluş] - [Sistem] Doküman Seti/
├── 00_Kapsam_ve_ElKitabi/
├── 01_Politikalar/
├── 02_Prosedurler/
├── 03_Talimatlar/
├── 04_Formlar_ve_Listeler/
├── 05_Planlar/
├── 06_Kayitlar_ORNEK/          ← YALNIZCA gerektiğinde; aşağıdaki nota bakın
├── 07_Denetim_Hazirlik/        ← ana doküman listesi, kanıt matrisi, öz değerlendirme
└── OKUBENI.md                  ← ne üretildi, ne eksik, sonraki adımlar
```

`OKUBENI.md` her zaman üretilir. Kullanıcı 40 dosyalık bir klasörle baş başa
kalmamalı; hangi dosyanın neden var olduğunu ve hangi alanların doldurulması
gerektiğini oradan görmeli.

**`06_Kayitlar_ORNEK` hakkında — varsayılan: bu klasörü açma.** Örnek satırları
formun/kaydın kendi içine 1–3 satır olarak koy ve `[ÖRNEK — doğrulanacak]` ile
etiketle; kullanıcı formatı orada görür, ayrı klasöre gerek kalmaz. Ayrı bir
örnek kayıt klasörü yalnızca kullanıcı açıkça "doldurulmuş örnek kayıt da ver"
derse açılır ve içindeki her dosyanın adı `ORNEK_` ile başlar. Gerekçe: gerçek
kayıtlardan ayırt edilemeyen örnek kayıtlar denetimde sahte kanıt olarak
değerlendirilebilir — bu, doküman setinin tümünün güvenilirliğini yok eder.

---

## 4. Zorunlu ortak bölümler

Her Word dokümanı şu iskeleti taşır (`ys_docx.py` bunu üretir):

1. **Kapak** — kuruluş, sistem adı, doküman adı, doküman no, revizyon, tarih, gizlilik
2. **Revizyon geçmişi** — rev no, tarih, değişiklik açıklaması, yapan
3. **İçindekiler** — 3 seviye, Word alan kodu (F9 ile güncellenir)
4. **Amaç** — bu doküman neden var
5. **Kapsam** — hangi birim/süreç/lokasyon/varlık; hariç tutulanlar ve gerekçesi
6. **Tanımlar ve kısaltmalar** — sadece dokümanda geçenler
7. **Sorumluluklar** — RACI benzeri tablo (Rol | Sorumluluk)
8. **Uygulama** — dokümanın asıl gövdesi
9. **İlgili dokümanlar** — kod + ad tablosu (çapraz referans)
10. **Standart madde ilişkisi** — bu doküman hangi maddeleri karşılıyor
11. **Kayıtlar** — bu dokümandan doğan kayıtlar, saklama süresi, sorumlu
12. **Onay bloğu** — Hazırlayan / Kontrol Eden / Onaylayan + imza alanı

Madde 10 çoğu şablonda yoktur ama denetimde **çok işe yarar**: denetçi "bu
gereklilik nerede karşılanıyor?" diye sorduğunda cevap dokümanın içinde durur.

---

## 5. Doküman tipi içerik kalıpları

### Politika (PL)
Kısa olmalı — 2–4 sayfa. Uzun politika okunmaz, okunmayan politika uygulanmaz.

```
1. Amaç ve Taahhüt        ← üst yönetimin birinci ağızdan taahhüdü
2. Kapsam
3. Politika İlkeleri      ← 6–12 madde, her biri tek cümlelik ilke
4. Hedeflerle İlişki      ← ölçülebilir hedeflere çerçeve
5. Roller ve Sorumluluklar
6. Uyumsuzluk ve Yaptırım
7. Gözden Geçirme         ← "yılda en az bir kez ve önemli değişiklikte"
8. Duyurulma ve Erişim    ← kime, nasıl duyuruldu; ilgili taraflara erişim
```

### Prosedür (PR)
Akış içerir. Süreç adımlarını tablo hâlinde vermek denetçi için en okunaklısı:

| Adım | Faaliyet | Sorumlu | Girdi | Çıktı / Kayıt | Süre |
|---|---|---|---|---|---|

Ardından "Ölçüm ve İzleme" bölümü: bu sürecin performansı hangi göstergeyle,
hangi sıklıkta ölçülüyor. 9.1 maddesi bunu ister.

### Talimat (TL)
Numaralı adımlar, her adım bir eylem fiili ile başlar. Ekran görüntüsü/şema
yer tutucusu bırak. 1–3 sayfa.

### Form (FR) / Liste (LS)
Excel üretilir (`ys_xlsx.py`). Her zaman: Bilgi sayfası + başlık satırı +
donmuş bölme + otomatik filtre + açılır listeler + en az 20 boş satır +
1–3 satır **örnek veri** (kullanıcı formatı anlasın diye, açıkça "ÖRNEK" etiketli).

### Plan (PN)
Zaman ekseni içerir. Tablo: Faaliyet | Sorumlu | Başlangıç | Bitiş | Kaynak |
Durum | Doğrulama yöntemi. Gantt benzeri görsel gerekmez ama tarih olmadan plan
olmaz — tarihler `[DOLDURULACAK]` bile olsa alan bulunmalı.

---

## 6. Yazım dili ve ton

- **Emir kipi değil, zorunluluk kipi.** "Yedekleme yapılır" değil → "Yedekleme,
  BT Yöneticisi tarafından günlük olarak yapılır." Özne olmayan cümle sorumsuz
  cümledir; denetçi "kim yapıyor?" diye sorar.
- **Standardın kelimelerini kullan** ama kopyalama. "Dokümante edilmiş bilgi",
  "ilgili taraf", "artık risk", "düzeltici faaliyet" gibi terimler denetçinin
  aradığı kancalardır. Standart metninin kendisini birebir aktarma — hem telif
  sorunu hem de "şablon indirmiş" izlenimi verir.
- **Ölçülebilir yaz.** "Düzenli olarak" değil → "üç ayda bir". "Yeterli" değil →
  "en az 8 karakter, 3 karakter sınıfı". Belirsiz ifade denetimde en sık
  bulgu kaynağıdır.
- **Kuruluşa özgü yaz.** Gerçek birim adları, gerçek sistem adları, gerçek
  lokasyonlar. Jenerik doküman denetçinin ilk fark ettiği şeydir.
- Türkçe yaz (kullanıcı aksini istemedikçe). Terimlerin İngilizce karşılığını
  ilk geçtiği yerde parantezde ver.

---

## 7. Denetçinin dokümanda aradığı izler

Bunlar, doküman seti "tamam" görünse bile bulgu üreten şeylerdir. Üretim
sırasında her dosya için kontrol et:

| İz | Neden önemli | Nasıl sağlanır |
|---|---|---|
| Onay tarihi geçmişte, revizyon tarihi tutarlı | Onaylanmamış doküman yürürlükte değildir | Kapak + revizyon tablosu aynı tarihi göstersin |
| Doküman kodları çapraz referanslarda doğru | Kopuk referans "kontrol edilmemiş doküman" demektir | Tüm setin doküman listesinden kod çek |
| Kapsam beyanları birbiriyle çelişmiyor | En sık bulgu türlerinden biri | Kapsam metnini tek kaynaktan üret, kopyala |
| Politika hedeflerle, hedefler ölçümle bağlı | 5.2 → 6.2 → 9.1 zinciri | Hedef tablosunu politikaya referansla |
| Risk → kontrol → doküman zinciri kapalı | Risk işleme planının uygulandığının kanıtı | Kanıt matrisini üret |
| Hariç tutmalar gerekçelendirilmiş | Gerekçesiz hariç tutma kabul edilmez | Kapsam dokümanında ayrı bölüm |
| Saklama süreleri belirtilmiş | 7.5.3 gerekliliği | Her dokümanın "Kayıtlar" bölümü |
| Boş bırakılmış alan yok | Yarım doküman güvensizlik yaratır | `[DOLDURULACAK]` etiketlerini sayıp raporla |

Son iki madde skill'in **OKUBENI.md** ve **öz değerlendirme** çıktılarının
varlık sebebidir: kullanıcı denetime girmeden önce neyi kapatması gerektiğini
bilmeli.
