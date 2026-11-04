# Teslim Öncesi Öz Kontrol

## İçindekiler

- A — Bütünlük
- A2 — 42001'e özgü zorunlu kontroller
- B — Tutarlılık
- C — Denetlenebilirlik
- D — Biçim
- E — Dürüstlük
- F — Ölçek
- Otomatik kontrol
- OKUBENI.md kalıbı
- Ne üretildi
- Denetim öncesi kapatılması gerekenler
- [DOLDURULACAK] alanlar
- Doğrulanması gereken varsayımlar
- Üretilmeyenler ve nedeni
- Sonraki adımlar
- Öz kontrol §A3: eklenti entegrasyonu kontrolleri

Doküman seti üretildikten sonra, kullanıcıya teslim etmeden önce bu listeyi geç.
Amaç mükemmellik değil — **kullanıcının denetimde şaşırmaması.** Bulduğun her
açığı `OKUBENI.md` içinde açıkça yaz; gizlemek kimseye yaramaz.

## A — Bütünlük

- [ ] Standardın zorunlu kıldığı her dokümante bilgi kaleminin karşılığı olan bir dosya var
- [ ] Doküman listesindeki her kod, üretilen bir dosyaya karşılık geliyor
- [ ] Üretilmeyen dokümanlar `OKUBENI.md`'de gerekçesiyle listelenmiş
- [ ] `OKUBENI.md` üretildi ve klasör kökünde

## A2 — 42001'e özgü zorunlu kontroller

Bunlar diğer yönetim sistemi standartlarında karşılığı olmayan, atlanırsa
doğrudan bulgu üreten kalemlerdir. Teslim öncesi tek tek doğrula:

- [ ] **İklim değişikliği** 4.1'de değerlendirilmiş (evet veya gerekçeli hayır) ve A.4.5 (hesaplama kaynağının çevresel etkisi) ile A.5.5 (çevresel sürdürülebilirlik) ayakları boş değil
- [ ] Kuruluşun **YZ rolü sistem bazında** tanımlı; envanterde rol sütunu dolu
- [ ] **YZ süjeleri** (kararın muhatabı kişiler) ilgili taraf listesinde var
- [ ] **İlgili otoriteler** ilgili taraf listesinde var
- [ ] Risk kriteri seti hem risk hem **etki** değerlendirmesini kapsıyor (6.1.1)
- [ ] Etki değerlendirmesinde A.5.3'ün **yedi kalemi** var: olumlu etkiler · öngörülebilir hatalar · demografik gruplar · sistem karmaşıklığı · insanın rolü · istihdam ve beceri etkisi · saklama süresi
- [ ] A.5.4'ün **sekiz alanı** ayrı ayrı ele alınmış; **erişilebilirlik** ve **insan hakları** boş değil
- [ ] A.5.5'in **dört alanı** ele alınmış; ele alınmayan için "uygulanabilir değil" gerekçesi yazılmış
- [ ] **Amaçlanan kullanım / öngörülebilir amaç dışı kullanım / yasak kullanım** üçü ayrı yazılmış
- [ ] Endişe bildirim prosedüründe **eskalasyon**, **misillemeden koruma** ve **bildirene geri bildirim** ayrı bölümler hâlinde var (A.3.3)
- [ ] Olay günlüğü tasarımında **saklama süresi**, **koruma** ve **performans aralığı dışı çalışmanın tespiti** yazılı (A.6.2.8)
- [ ] İşletim prosedüründe **veri zehirlenmesi / model çalma / model tersine çevirme** karşı önlemleri var (A.6.2.6)
- [ ] Değişiklik yönetiminde **geri alma (roll-back) stratejisi** ve **uygulama sonrası gözden geçirme** var (6.3)
- [ ] İç tetkikçi **bağımsızlığı** ve **yetkinliği** yazılı (9.2)
- [ ] Tedarikçi sözleşme kontrolünde **düzeltici faaliyet talep hakkı** ve **model sürüm değişikliği bildirimi** ele alınmış (A.10.3)
- [ ] Kişisel veri işleniyorsa **veri sorumlusu / veri işleyen** ayrımı yapılmış (A.10.2)
- [ ] Mevzuat atıflarının tamamı `[yerleşik]` / `[teyit]` / `[teyit-madde]` etiketli; hiçbiri doğrulanmış gibi sunulmamış

## B — Tutarlılık

- [ ] Kapsam beyanı **kelimesi kelimesine aynı** — kapsam dokümanı, el kitabı, politika ve SoA'da
- [ ] Kuruluş unvanı her dosyada aynı yazılmış (A.Ş. / AŞ / Anonim Şirketi karışıklığı yok)
- [ ] Doküman kodları çapraz referanslarda doğru — var olmayan koda atıf yok
- [ ] Tarihler tutarlı: kapak tarihi = revizyon tablosundaki son satır = onay tarihi
- [ ] Rol adları her dokümanda aynı (bir yerde "BT Müdürü", başka yerde "Bilgi İşlem Şefi" değil)
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

# 4) Denetim soru bankasını üret ve kapsama bak
python3 scripts/kayitlar_42001.py soru_bankasi --cikti "07_Denetim_Hazirlik/Denetim-Soru-Bankasi.xlsx"
```

Soru bankası 65 bölüm (27 madde + 38 kontrol) ve 208 soru içerir. Teslim
öncesi bu dosyadaki her bölüm için **en az bir doküman referansı** girilmiş
olmalı; referanssız kalan bölüm, karşılığı üretilmemiş gereklilik demektir ve
`OKUBENI.md`'ye yüksek öncelikli olarak yazılır.

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
| Yüksek | Varlık envanteri boş | BGYS-LS-01 | Gerçek varlıklar girilmeli, sahip atanmalı |

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

## Öz kontrol §A3: eklenti entegrasyonu kontrolleri

Teslim öncesi `denetim-oz-kontrol.md` §A2 listesine ek olarak geç:

- [ ] `Ek E4` son teyit tarihi 90 günden yeni; değilse ilgili satırlar web aramasıyla kontrol edildi
- [ ] YZYS kayıtlarında eklentinin gizlilik başlığı ("PRIVILEGED", "ATTORNEY WORK PRODUCT") **yok**; hukuki notlara yalnızca sonuç + referans + tarih ile atıf var
- [ ] Envanterde iki rol sütunu ayrı: 42001 rolü ve AB YZ Yasası rolü; biri diğerinden otomatik türetilmemiş
- [ ] `envanter_senkron.py fark` çalıştırıldı; yalnız-Excel sistemler için öneri taslağı kullanıcıya sunuldu, çelişkiler kapatıldı
- [ ] `envanter_senkron.py zincir` raporunda açık zincir yok veya OKUBENI'de listelendi
- [ ] Eklenti bulgularının önem derecesi risk kaydında taban olarak korunmuş; düşürülen her bulgu için gerekçe var
- [ ] Profildeki kırmızı çizgiler YZ politikasının yasaklı kullanımlarında ve envanterin "Yasak Kullanım" sütununda yer alıyor
- [ ] Danışman modunda: dosyalar doğru matter altında, başka müşteriye ait içerik yok
- [ ] Olay prosedüründe tespit zamanı dakika hassasiyetinde ve her bildirim kolu (KVKK, AB YZ Yasası, siber, sektörel, tedarikçi) için karar sütunu var
- [ ] Yetkinlik matrisi kişi grubu × YZ sistemi bazında; insan gözetimi yapanlar ve dış kişiler ayrı satırda
