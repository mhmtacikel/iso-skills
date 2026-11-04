# Teslim Öncesi Öz Kontrol

Doküman seti üretildikten sonra, kullanıcıya teslim etmeden önce bu listeyi geç.
Amaç mükemmellik değil — **kullanıcının denetimde şaşırmaması.** Bulduğun her
açığı `OKUBENI.md` içinde açıkça yaz; gizlemek kimseye yaramaz.

## A — Bütünlük

- [ ] Standardın zorunlu kıldığı her dokümante bilgi kaleminin karşılığı olan bir dosya var
- [ ] Doküman listesindeki her kod, üretilen bir dosyaya karşılık geliyor
- [ ] Üretilmeyen dokümanlar `OKUBENI.md`'de gerekçesiyle listelenmiş
- [ ] `OKUBENI.md` üretildi ve klasör kökünde

## B — Tutarlılık

- [ ] Kapsam beyanı **kelimesi kelimesine aynı** — kapsam dokümanı, el kitabı, politika ve risk değerlendirme kaydının Bilgi sayfasında
- [ ] Kuruluş unvanı her dosyada aynı yazılmış (A.Ş. / AŞ / Anonim Şirketi karışıklığı yok)
- [ ] Doküman kodları çapraz referanslarda doğru — var olmayan koda atıf yok
- [ ] Tarihler tutarlı: kapak tarihi = revizyon tablosundaki son satır = onay tarihi
- [ ] Rol adları her dokümanda aynı (bir yerde "İş Güvenliği Uzmanı", başka yerde "İSG Sorumlusu" değil)
- [ ] Sıklık ifadeleri çelişmiyor (bir dokümanda "üç ayda bir", diğerinde "altı ayda bir" aynı faaliyet için)

## C — Denetlenebilirlik

- [ ] Her prosedürde sorumlu **rol** tanımlı (özne olmayan cümle kalmadı)
- [ ] Her prosedürde ölçüm/izleme bölümü var (9.1 zinciri)
- [ ] Her dokümanın sonunda "İlgili dokümanlar" ve "Standart madde ilişkisi" bölümü var
- [ ] Her dokümanda kayıtlar ve saklama süreleri belirtilmiş
- [ ] "Düzenli olarak", "yeterli", "gerektiğinde", "uygun şekilde" gibi ölçülemez ifadeler taranıp sayısallaştırıldı
- [ ] Kanıt matrisi üretildi: gereklilik → doküman → kanıt → sorumlu

## D — Biçim

- [ ] Her Word dosyasında kapak, revizyon tablosu, içindekiler, onay bloğu var
- [ ] Antet/altbilgi doğru doküman kodunu ve revizyonu gösteriyor
- [ ] Kurumsal şablon verildiyse üretilen dosyalar o şablonun stillerini taşıyor
- [ ] Excel dosyalarında: Bilgi sayfası, donmuş bölme, otomatik filtre, açılır listeler çalışıyor
- [ ] Dosya adları kod + ad formatında ve klasör yapısı doğru

## E — Dürüstlük

- [ ] `[DOLDURULACAK]` etiketleri sayıldı ve dosya bazında listelendi
- [ ] Her `[DOLDURULACAK]` neyin istendiğini açıklıyor (çıplak etiket kalmadı)
- [ ] Örnek/varsayım veriler `[ÖRNEK — doğrulanacak]` ile işaretli
- [ ] Gerçekmiş gibi sunulan uydurma kayıt yok (tarih, imza, olay kaydı, ölçüm sonucu)
- [ ] Kuruluş hakkında doğrulanmamış iddia yok (sertifika, üyelik, sistem adı)

## F — Ölçek

- [ ] Doküman sayısı kuruluşun büyüklüğüyle orantılı
- [ ] Politikalar 2–6 sayfa aralığında (okunabilir uzunlukta)
- [ ] Kuruluşun yapmadığı bir faaliyete ilişkin prosedür üretilmemiş

---

## G — İSGYS'ye özgü

- [ ] Politika 5.2'nin dört taahhüdünü içeriyor: güvenli ve sağlıklı çalışma koşulları, yasal şartlara uyum, tehlikeleri ortadan kaldırma ve riskleri azaltma, **çalışanlarla danışma ve katılım** — ve hedefler için çerçeve
- [ ] 5.4 için ayrı süreç var; yönetici olmayan çalışanların danışıldığı/katıldığı konular (5.4 d–e) tek tek eşlenmiş; "İSG Kurulu = 5.4" eşitlemesi yapılmamış
- [ ] Risk değerlendirme kaydında risk seviyesi **formül**; kontrol hiyerarşisi sütunu dolu; KKD tek önlem olan satırlar gerekçeli
- [ ] Rutin dışı faaliyetler, yükleniciler, ziyaretçiler, özel politika grupları, insan faktörleri, psikososyal riskler ve iklim kaynaklı tehlikeler (Amd 1:2024) risk değerlendirmesinde temsil ediliyor
- [ ] Risk değerlendirmesi yenileme periyodu tehlike sınıfıyla uyumlu (6/4/2 yıl) ve tetikleyiciler yazılı
- [ ] 8.1.3 değişiklik yönetimi ve 8.1.4 yüklenici/dış kaynak süreçleri var — yalnız ceza şartnamesi yeterli değil
- [ ] Yasal şartlar listesinde mülga tüzük yok; Resmî Gazete künyeleri teyitli ya da `[TEYİT]` etiketli; 2026 eğitim yönetmeliği değişikliği eğitim prosedürüne işlenmiş
- [ ] DÖF prosedüründe "önleyici faaliyet" kalmamış (45001'de yok — risk/fırsat sürecine taşındı)
- [ ] Olay incelemesine çalışan katılımı yazılı (5.4 e); SGK bildirim süresi (3 iş günü) doğru
- [ ] Rol adları tek: İş Güvenliği Uzmanı, İşyeri Hekimi, Diğer Sağlık Personeli, Çalışan Temsilcisi, Destek Elemanı — bir yerde "İSG Sorumlusu", başka yerde "Çevre ve İSG Mühendisi" yazılmamış
- [ ] Sağlık verisi (tanı, rapor içeriği) hiçbir form/listede istenmiyor (KVKK m.6); yalnız işyeri hekimi dosyasında

---

## Otomatik kontrol

Mekanik kontrolleri elle yapma; script yaz. En azından şu üçünü tara:

```bash
# 1) DOLDURULACAK sayımı — dosya bazında
python3 - <<'PY'
import glob, re, os
from docx import Document
for f in sorted(glob.glob("**/*.docx", recursive=True)):
    metin = "\n".join(p.text for p in Document(f).paragraphs)
    n = len(re.findall(r"\[DOLDURULACAK", metin))
    if n: print(f"{n:3d}  {os.path.basename(f)}")
PY

# 2) Ölçülemez ifade taraması
grep -rIl "düzenli olarak\|gerektiğinde\|uygun şekilde\|yeterli seviyede" . 2>/dev/null

# 3) Kırık çapraz referans: metinde geçen kodlar ile var olan dosya kodlarını karşılaştır
# 4) Türkçe büyük harf hatası (K1): YÖNETIM, GÜVENLIĞI, POLITIKA, TEHLIKE gibi kalıplar
grep -rIl "YÖNETIM\|GÜVENLIĞI\|POLITIKA\|TEHLIKE\|ILGILI\|EĞITIM" . 2>/dev/null
# 5) OHSAS mirası: "18001", "önleyici faaliyet", "yönetim temsilcisi" (45001'de zorunlu rol değil)
```

Bu üç taramanın sonucunu `OKUBENI.md`'ye tablo hâlinde koy. Kullanıcı "ne kadar
işim kaldı" sorusunun cevabını rakamla görmeli.

---

## OKUBENI.md kalıbı

```markdown
# [Kuruluş] — [Standart] Doküman Seti

Üretim tarihi: [tarih] · Kapsam: [kapsam cümlesi]

## Ne üretildi
[klasör bazında dosya sayısı ve liste]

## Denetim öncesi kapatılması gerekenler
| Öncelik | Konu | İlgili dosya | Ne yapılmalı |
|---|---|---|---|
| Yüksek | Risk değerlendirmesinde yalnız ÖRNEK satırlar var | İSGYS-LS-01 | Ekip sahada gerçek faaliyetleri değerlendirmeli, imzalı kayıt |

## [DOLDURULACAK] alanlar
| Dosya | Adet | Ne isteniyor |
|---|---|---|

## Doğrulanması gereken varsayımlar
[ÖRNEK etiketli içeriklerin listesi]

## Üretilmeyenler ve nedeni
[ör. Güvenli Yazılım Geliştirme Prosedürü — kuruluş yazılım geliştirmiyor]

## Sonraki adımlar
1. ...
```
