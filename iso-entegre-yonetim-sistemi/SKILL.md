---
name: iso-entegre-yonetim-sistemi
description: "Birden fazla ISO yönetim sistemi standardını (27001, 20000-1, 22301, 27701, 42001 ve iso- ile başlayıp -dokuman-seti ile biten her yeni skill) Annex SL ortak üst yapısı altında TEK bir Entegre Yönetim Sistemi (EYS) doküman setinde birleştirir; alttaki iso-*-dokuman-seti skillerini kendi motoru olarak çalıştırır ve tüm sete tek, istikrarlı bir \"ghost writer\" sesiyle yazar. Kullanıcı \"entegre yönetim sistemi kur\", \"EYS\", \"IMS\", \"çoklu standart\", \"27001 ve 22301'i birlikte kur\", \"birden fazla ISO sertifikasyonuna hazırlan\", \"Annex SL\", \"mevcut sistemlerimi birleştir\" dediğinde ya da iki veya daha fazla ISO standardı gündeme geldiğinde mutlaka kullan."
metadata:
  surum: "2.0.0"
---

# Entegre Yönetim Sistemi (EYS) Kurulumu — Annex SL Orkestrasyonu

Bu skill kendi başına doküman üretmez. **Orkestra şefidir:** hangi ISO standartlarının
kapsamda olduğunu belirler, Annex SL'in (ISO/IEC Yönergeleri Bölüm 1, Ek SL — Üst Düzey
Yapı / High Level Structure) sağladığı ortak Madde 4–10 iskeletini tek sette kurar,
standarda özgü kısımlar için ilgili `iso-*-dokuman-seti` skill'lerini kendi motoru
olarak çağırır ve en sonunda **tüm sete** — hangi alt skill'den geldiğine bakmaksızın —
tek, tutarlı bir yazar sesiyle son bir geçiş yapar.

Bu son geçiş bu skill'in var oluş sebebidir. Beş standardı beş ayrı skill ile ayrı ayrı
üretirseniz teknik olarak doğru ama birbirinden kopuk beş doküman seti elde edersiniz:
bir sette "BT Müdürü", ötekinde "Bilgi İşlem Şefi"; biri "üç ayda bir" derken öteki
aynı faaliyet için "altı ayda bir" der. Denetçi bunu ilk bakışta yakalar ve "yaşamayan,
gerçek olmayan sistem" bulgusu yazar. Entegre kurulumun bütün amacı budur: kuruluş
gerçekten **tek bir** yönetim sistemi işletir, beş tane değil — dokümantasyon da öyle
görünmeli.

(Not: kullanıcı "ANNEX XL" diyebilir; standardın resmî adı **Annex SL**'dir — sık
karışan bir isimdir, düzeltip devam et, konuyu uzatma.)

## Üretim mekaniği — her doküman setinde geçerli değişmez kurallar

Bu kurallar doküman üretiminin mekaniğine aittir: hangi standart kapsamda olursa
olsun, hangi alt skill üretirse üretsin geçerlidir. Hepsi üretime **başlamadan
önce** motora yerleştirilir; sonradan düzeltmek tüm seti yeniden üretmeyi gerektirir.

### K1 — Türkçe büyük/küçük harf dönüşümü

Python'un `str.upper()` metodu "i" harfini **"I"** yapar; Türkçede doğrusu **"İ"**dir.
Aynı şekilde `str.lower()` "I" harfini "i" yapar; doğrusu "ı"dır. Doküman adları
antet tablosunda, başlıklar gövdede otomatik büyük harfe çevrildiği için bu hata
sette yüzlerce kez tekrarlanır: "BİLGİ GÜVENLİĞİ YÖNETİM SİSTEMİ" yerine
"BILGI GÜVENLIĞI YÖNETIM SISTEMI" yazılır ve set amatör görünür.

**Kural: üretim kodunda doğrudan `.upper()` / `.lower()` çağırma.** Motor 2.0.0
bu iki fonksiyonu içerir (`from ys_docx import tr_upper, tr_lower`); kendi
kodunda da bunları kullan:

```python
def tr_upper(metin):
    return str(metin).replace("i", "İ").replace("ı", "I").upper()


def tr_lower(metin):
    return str(metin).replace("I", "ı").replace("İ", "i").lower()
```

Diğer Türkçe harfler (ğ, ü, ş, ö, ç) Python'da doğru dönüşür; sorun yalnızca
i/I çiftindedir. Teslimden önce sette şu kalıpları ara — biri bile bulunuyorsa
dönüşüm fonksiyonu kullanılmamış demektir: `YÖNETIM`, `BILGI`, `POLITIKA`,
`ILGILI`, `SISTEM`, `TETKIK`, `DEĞIŞIKLIK`, `GÜVENLIĞI`, `ERIŞIM`, `EĞITIM`,
`KIMLIK`, `IHLAL`, `TEKNIK`, `KRITIK`, `HIZMET`. Buna karşılık `TANIMLAR`,
`KAYITLAR`, `SINIRLAR`, `DIŞ`, `KAPSAM` doğrudur (ı → I dönüşümü) — bunları
hata sanma.

### K2 — Denetim hazırlık dosyaları kodsuz "Yol Gösterici"dir

`07_Denetim_Hazirlik` (veya kurduğun şemadaki karşılığı) klasöründeki dosyalar —
mevcut doküman değerlendirme ve boşluk raporu, mevcut dokümanlar için revizyon
rehberleri, birleşik kontrol-kanıt matrisi, öz değerlendirme, denetçi soru
listesi, denetim günü kontrol listesi — kuruluşun yönetim sisteminin **parçası
değildir**. Bunlar belgelendirme denetiminden önce **üst yönetime ve yönetim
sistemi komitesine neyin, kim tarafından, hangi sırayla yapılacağını gösteren
yol göstericilerdir.**

- Dosya adı yalnızca dokümanın adıdır: `Birleşik Kanıt Matrisi.xlsx` — kod öneki yok.
- Kapakta kod yerine **"YOL GÖSTERİCİ"** yazılır. Antet tablosunda "Doküman
  No/Kodu" satırı yerine **"Doküman Türü | Yol Gösterici"** yazılır; diğer
  alanlar (yayın tarihi, revizyon, gizlilik sınıfı) korunur. Antetteki toplam
  sayfa alanını ya da içindekileri güncelleyen kod her iki etiketi de tanımalı.
- Onay satırı yönetim sistemi komitesi başkanıdır; üst yönetim onayı gerekmez.
- Metnin başına bir not konur: "Bu dosya yönetim sistemi dokümanı değildir;
  doküman kontrolüne tabi değildir; iş ilerledikçe güncellenir."
- Geçerli Doküman Listesi'ne **girmez**. Listenin not alanına bunun bilinçli bir
  tercih olduğunu yazan bir cümle koy, yoksa denetçi "eksik doküman" sanır.
  OKUBENI'de sayıyı "n kodlu doküman + m yol gösterici" diye ayrı ver.
- Setin geri kalanından bu dosyalara kodla değil **adıyla** atıf verilir. Üretim
  sırasında kısa iç kod kullandıysan `tr()` içinde bir regex ile (Türkçe
  ekleriyle birlikte) ada çevir ve teslimden önce eski kod kalmadığını tara.
- Kullanıcı mevcut bir seti kodsuza çevirtirse bağlı klasördeki eski kodlu
  dosyaları silme; `_to_delete/` alt klasörüne `mv -n` ile taşı ve söyle.

Gerekçe: kodlu her doküman doküman kontrol prosedürüne tabidir — revizyon, onay,
duyuru, saklama. Denetime hazırlanırken sürekli güncellenen bir çalışma dosyasını
bu rejime sokmak, ya sahte revizyon geçmişi üretmeye ya da doküman kontrol
prosedürünün ihlaline yol açar. İkisi de denetimde bulgudur.

### K3 — Türkçe terim sözlüğü

Kullanıcı aksini istemedikçe başlık ve doküman adlarında İngilizce kısaltma
kullanılmaz (SoA → Uygulanabilirlik Bildirgesi, DPIA → Gizlilik Etki
Değerlendirmesi, PII → kişisel veri, BIA → İş Etki Analizi, SLA → Hizmet Düzeyi
Anlaşması, OLA → Operasyonel Düzey Anlaşması, CMDB → Konfigürasyon Yönetim
Veri Tabanı, RTO/RPO/MTPD → Kurtarma Süresi Hedefi / Kurtarma Noktası Hedefi /
Azami Tolere Edilebilir Kesinti Süresi, AIMS → Yapay Zekâ Yönetim Sistemi,
DLP / SIEM / CCTV / IVR / MFA → Türkçe karşılıkları). Motor 2.0.0 bu sözlüğü
(`TERIMLER`) ve `tr()` fonksiyonunu içerir, Word metinlerini otomatik geçirir;
Excel kayıtlarında ve kendi yazdığın kodda `tr()`'yi çağır. İngilizce karşılık
yalnız Tanımlar tablosunda parantez içinde bir kez görünür. Ürün adları olduğu
gibi kalır. Kullanıcının mevcut dokümanlarından alınan çevirilerdeki ekli
biçimleri ("PII'nin", "PII ilgilileri") de sözlüğe ekle; uzun ifadeleri önce
değiştir ki ek uyumu bozulmasın. 6. adımdaki geçişte kalan kısaltmaları regex
ile tara.

### K4 — Kurumsal şablon birebir istendiğinde klonla

Kullanıcı bir kurumsal dokümanı "şablon olarak bire bir kullan" diye verirse
varsayılan `ys_docx.py` kimliğini kullanma; şablonu klonla: kapak kodu ve antet
hücrelerini değiştir (K1 ile), şablonun başlık/gövde/liste paragraflarını rPr
dahil prototip olarak çoğalt, İçindekiler'i bookmark + `PAGEREF` ile yeniden
kur ve sayfa numaralarını LibreOffice render + `pdftotext` ile hesapla, sabit
toplam sayfa metnini `SECTIONPAGES` alanıyla değiştir. Excel'de kuruluşun mevcut
liste dosyasının bilgi sayfasını ve logosunu koru. Revizyon 0 yayın tarihini
kullanıcı aksini söylemedikçe boş bırak; kişi adı yerine unvan yaz. Her
dosyadan en az bir sayfayı PDF'e çevirip görsel kontrol et.

## Neden bu mümkün: Annex SL'in verdiği ortak zemin

2012'den beri yayımlanan tüm ISO yönetim sistemi standartları (27001, 22301, 20000-1,
27701, 42001, ayrıca 9001/14001/45001 gibi bu ailede henüz kendi `dokuman-seti`
skill'i olmayanlar) aynı iskelet üzerine kuruludur: aynı 10 ana madde başlığı, çoğu
alt maddede **kelimesi kelimesine aynı** çekirdek metin, aynı temel terimler (ilgili
taraf, dokümante edilmiş bilgi, risk ve fırsat, uygunsuzluk, düzeltici faaliyet).
Standartlar birbirinden **Madde 8 (İşletim)** içeriğinde ve madde 6.1.2/6.1.3'ün
hangi somut sürece karşılık geldiğinde ayrışır — biri bilgi güvenliği riski, öteki
iş etki analizi, öteki YZ risk+etki değerlendirmesi ister. Bu skill'in tüm mantığı
bu ayrımı bilmekten gelir: **4, 5, 6.1.1, 6.2, 6.3, 7, 9, 10 tek sette birleşir;
6.1.2/6.1.3 ortak çerçevede ama standarda özgü içerikle yazılır; 8 neredeyse tamamen
standarda özgü kalır.** Ayrıntılı harita: `references/annex-sl-cekirdek-haritasi.md`.

**İstisna — ISO/IEC 27701:2019 Annex SL yapısında değildir;** 27001'e eklentidir
(Madde 5 = 27001 Madde 4–10'a eklemeler, Madde 6 = 27002:2013 kontrollerine
eklemeler). Kapsamda 27701:2019 varsa ortak katman BGYS'dir; KVYS katmanı BGYS
dokümanlarına doküman bazında eklemeler olarak işlenir (BGYS Dokümanları KVYS
Revizyon Rehberi — K2'ye tabi) ve 27002:2013 → 2022 eşleme tablosu gerekir.
27701:2025 ise Annex SL yapısındadır ve normal akışa girer.

**Madde 10'un alt sıralaması (10.1/10.2) sürüme göre değişir** — 2022 Annex SL
tadilatından sonra yayımlanan/güncellenen standartlar (örn. ISO/IEC 27001:2022)
10.1'i "Sürekli iyileştirme", 10.2'yi "Uygunsuzluk" yapacak şekilde sırayı
değiştirdi; tadilat öncesi sürümler (örn. ISO 22301:2019, ISO/IEC 20000-1:2018)
eski sırayı korur. Bunu asla ezbere yazma — kapsamdaki her standardın kendi
`<alt skill>/references/madde-4-10.md` (veya eşdeğeri) dosyasındaki gerçek sırayı doğrula.

## Çalışma akışı

### 1 — Kapsamdaki standartları keşfet

Elindeki skill listesinde **`iso-` ile başlayıp `-dokuman-seti` ile biten** her
skill'i bul (bu, kendini ve `iso-tetkik-raporu-ghostwriter`'ı otomatik olarak
dışarıda bırakır — o bir denetim raporu skill'idir, doküman üreticisi değil).
Bu tarama sabit bir listeye güvenmez: yarın `iso-9001-dokuman-seti` eklenirse o da
otomatik olarak adaya çıkar. Bulduklarını kullanıcıya sade isimleriyle göster
(27001→BGYS, 20000-1→HYYS, 22301→İSYS, 27701→KVYS, 42001→YZYS) ve `AskUserQuestion`
ile (çoklu seçim) hangilerinin kapsamda olacağını sor.

Kullanıcı, kurulu bir skill'i olmayan bir standart isterse (örn. ISO 9001) bunu
söyle: o standardın doküman listesi/Ek A eşlemesi/madde metni bu ortamda yok, bu
yüzden onun standarda özgü katmanını üretemezsin. `annex-sl-cekirdek-haritasi.md`
metodolojisiyle **genel** bir Madde 4–10 iskeleti kurabileceğini ama bunun o
standarda göre doğrulanmamış olacağını açıkça belirt — uydurma Ek A/madde listesi
üretme.

Kullanıcı başka bir firmanın kurulmuş setini **örnek** olarak verirse oradan
**biçimi** al (kodlama şeması, antet düzeni, altbilgi ibaresi, klasör yapısı,
doküman adları), **içeriği** alma — o set o firmanın ölçeğine ve iş modeline göre
yazılmıştır. Örnek setteki doküman sayısını hedef sanma; kendi kullanıcının
ölçeğine göre yeniden karar ver.

### 2 — Tek, birleşik açılış görüşmesi yap

Her `iso-*-dokuman-seti` skill'inin `<alt skill>/references/gorusme-rehberi.md` dosyası **aynı
altı soruluk** temel anketi taşır (kuruluş, ölçek, mevcut sistem, şablon, kodlama,
sadeleştirilmiş/tam set tercihi) — bunu beş kez sorma, **bir kez** sor. Ardından
her kapsamdaki standardın kendi SKILL.md'sindeki standarda özgü 1–2 soruyu ekle
(27001: bilgi varlığı ağırlığı + geliştirme/veri merkezi; 42001: hangi YZ
sistemleri, hangi rolde; 27701: hangi kişisel veri kategorileri, 2019 mu 2025 mi,
veri sorumlusu/işleyen rolü; 22301: kritik süreçler ve tolere edilebilir kesinti
süresi; 20000-1: hizmet kataloğu ve müşteri tipi). Ayrıca her kurulumda şunları
sor: kişi adı mı unvan mı kullanılacak, Revizyon 0 tarihi, denetim hazırlık
dosyalarının kodsuz yol gösterici olacağının teyidi, hangi mevcut dokümanların
yeniden yazılmayıp revizyon rehberiyle ele alınacağı. Birleştirilmiş soru listesi
ve sıralaması: `references/kapsam-belirleme-ve-gorusme.md`.

Bir soru yanıtsız kalırsa üretimi durdurma: makul varsayımı yap, ama varsayımı ve
**somut sonucunu** (hangi maddenin/kontrolün hariç tutulduğunu, hangi dokümanın
üretilmediğini) `OKUBENI.md`'nin başında ayrı bir başlık altında yaz. Gerekçesiz
veya yanlış hariç tutma majör uygunsuzluktur.

Kullanıcının **zaten ayrı ayrı kurulmuş** sistemleri varsa (örn. 27001 seti hazır,
şimdi 22301 ekleniyor) bunu farklı bir akış olarak ele al — bkz. aşağıdaki
"Mevcut ayrı sistemleri birleştirme" bölümü.

### 3 — Tek kapsam beyanı üret

Her standardın kendi kapsam cümlesi kalıbı biraz farklıdır (BGYS kapsamı ≠ YZYS
kapsamı ≠ İSYS kapsamı) ama tüzel kişilik + lokasyon + faaliyet çekirdeği ortaktır.
**Tek bir ana kapsam paragrafı** yaz, sonra yalnızca gerçekten ayrışan kısımlar için
standarda özgü ek (42001'de rol ayrımı sağlayıcı/üretici/müşteri/ortak, 27701'de
veri sorumlusu/işleyen ayrımı, 22301'de kritik süreç listesi gibi) ekle. Aynı kapsam
cümlesini beş kez farklı kelimelerle yazmak en sık rastlanan entegre sistem bulgusu
kaynağıdır — denetçi ilk yaptığı işlerden biri kapsam beyanlarını yan yana koymaktır.

Kapsam cümlesini, kuruluş unvanını, adresi, rol adlarını ve tüm sıklık/eşik
değerlerini üretimin en başında **tek bir terim sözlüğü dosyasında** topla ve her
dokümanı oradan besle. Bu, 6. adımdaki tutarlılık geçişinin işini kolaylaştırmaz —
büyük ölçüde gereksiz kılar.

### 4 — Annex SL çekirdeğini (Madde 4–10) TEK SET olarak kur

`EYS-` önekiyle: El Kitabı, bağlam/ilgili taraf analizi, ana politika, doküman
kontrol prosedürü, yetkinlik/farkındalık, iç tetkik, YGG, düzeltici faaliyet —
bunların hepsi standarttan standarda hemen hemen aynı metni taşır, ayrı ayrı
yazılmamalı. Her dokümanın "Standart madde ilişkisi" bölümünde kapsamdaki **her**
standardın karşılık gelen madde numarasını ayrı ayrı listele (numaralar Annex SL
sayesinde aynıdır ama madde 10 alt sırası standarda göre değişebilir — yukarıdaki
uyarıyı hatırla).

6.1.2/6.1.3 (risk metodolojisi) için: standartlar arası ortak bir **risk ve
fırsat yönetimi çerçevesi** kur (kriterler, ölçek, roller aynı), ama somut
uygulamayı (bilgi güvenliği riski / iş etki analizi / YZ risk+etki
değerlendirmesi / kişisel veri riski) `references/annex-sl-cekirdek-haritasi.md`
rehberliğinde ya tek genişletilmiş tabloda ya da birbirine açıkça referans veren
bağlı alt dokümanlarda ele al. Zorla tek tabloya sıkıştırmak, farklı risk
türlerini (tehdit/açıklık ile etki/olasılık farklı boyutlardır) birbirine
karıştırıp her ikisini de zayıflatabilir — okunabilirlik kaybolacaksa ayır, ama
aynı format ve aynı sesle yaz.

Bu adımda motor olarak kapsamdaki standartlardan **herhangi birinin**
`<alt skill>/scripts/ys_docx.py` / `<alt skill>/scripts/ys_xlsx.py` dosyalarını kullan — bütün
`iso-*-dokuman-seti` skill'lerinde motor aynı sürümdür (dosya başındaki
`MOTOR_SURUM`; farklıysa büyük olanı kullan). O skill'i `Skill` aracıyla
çağırıp taban dizinini elde et, motoru oradan çalıştır; burada kopyalama.

Motor 2.0.0 K1–K3'ü yerleşik uygular: antette `tr_upper()`, metinlerde `tr()`
terim sözlüğü (kuruluşa özgü ek terimler `YSBelge(..., sozluk={...})`),
`tanimlar()` tablosunda çeviri yapılmaz, yol gösterici için
`Kimlik(tur="yol_gosterici")` kapak/antet/not/dosya adını (`k.dosya_adi()`)
otomatik değiştirir. Motoru kendin kurman gerekiyorsa (K4 — şablon birebir
klonlanacaksa) bu davranışları klon koduna da koy.

### 5 — Standarda özgü katmanı üret

Kapsamdaki **her** standart için o standardın kendi `iso-*-dokuman-seti` skill'ini
`Skill` aracıyla çalıştır ve ona şunu açıkça söyle: *"Bu entegre bir kurulumun
parçasısın. Kuruluş bilgisi ve kapsam beyanı şu (paylaş). Ortak Madde 4–10
dokümanlarını (El Kitabı, ana politika, doküman kontrol, iç tetkik, YGG, DÖF,
yetkinlik/farkındalık) tekrar üretme — bunlar zaten `EYS-` önekiyle üretildi. Yalnızca
kendine özgü katmanı üret: Ek A kontrolleri ve Uygulanabilirlik Bildirgesi (27001,
42001), İş Etki Analizi ve süreklilik stratejileri/planları (22301), veri işleme
envanteri/gizlilik etki değerlendirmesi/aydınlatma (27701), hizmet kataloğu/Hizmet
Düzeyi Anlaşmaları/Konfigürasyon Yönetim Veri Tabanı (20000-1). Denetim hazırlık
dosyalarını K2'ye göre kodsuz yol gösterici olarak üret."* Bu dokümanlar kendi
önekini korur (BGYS-, İSYS-, HYYS-, KVYS-, YZYS-) — o standardın kendi denetim
izini bağımsız da takip edilebilir tutmak için önek karıştırılmaz.

### 6 — Ghost-writer tutarlılık geçişi (bu skill'in asıl katkısı)

Set tamamlandığında, hangi dosyanın hangi alt skill'den geldiğine bakmaksızın
**tüm sete tek bir geçiş** yap: aynı rol adları, aynı kuruluş unvanı yazımı, aynı
sıklık ifadeleri, aynı yasaklı klişe listesi, aynı `[DOLDURULACAK]`/`[ÖRNEK]`
disiplini, doküman türüne göre tutarlı kip (politika/prosedür → zorunluluk kipi;
form/kayıt → nötr; yol gösterici → yönetime hitap eden, eylem ve sorumlu odaklı
tek ses). Tam kurallar ve "istikrarlı yazar" ne demek açıklaması:
`references/ghost-writer-tutarlilik-rehberi.md`. Bu geçiş atlanabilir bir "nice
to have" değil — beş skill'i ayrı ayrı çalıştırmak yerine bu skill'i kullanmanın
**tek** somut farkı budur; atlarsan kullanıcı beş ayrı klasör indirip elle
birleştirseydi ne elde edecekse onu almış olur.

Geçişi elle değil hazır betikle yap. Önce 3. adımdaki terim sözlüğünden bir
JSON yaz (`unvan`, `unvan_varyantlari`, `roller` {yanlış: doğru},
`yayin_tarihi`), sonra herhangi bir doküman seti skill'inin betiğini çalıştır:

```bash
python <iso-*-dokuman-seti taban dizini>/scripts/tutarlilik_tarama.py "<set>" \
  --sozluk "<set>/_terimler.json" --md "<set>/_tarama.md"
```

Betik .docx (gövde, antet, altbilgi) ve .xlsx metnini çıkarır, `_to_delete/`
klasörünü atlar ve şu on kontrolü yapar:

1. Kuruluş unvanı varyantları — tek biçime indir.
2. Sözlük dışı rol adları ("BT Müdürü" vs "Bilgi İşlem Şefi").
3. Yasaklı klişeler ("kapsamlı bir şekilde", "titizlikle", "önemli ölçüde").
4. Ölçülemez ifadeler ("düzenli olarak", "gerektiğinde", "en kısa sürede").
5. K1'deki hatalı büyük harf kalıpları.
6. Kırık doküman kodu çapraz referansları — metinde geçen her kodun sette
   karşılığı bir dosya var mı.
7. Yol gösterici dosyalara kodla verilmiş atıf (K2) — sıfır olmalı.
8. `[DOLDURULACAK]` / `[ÖRNEK]` / `[DOĞRULANACAK]` sayımı, dosya bazında.
9. Yayın tarihinin tüm dosyalarda aynı olması.
10. K3 sözlüğü dışında kalan İngilizce kısaltmalar (DPIA, PII, SoA, BIA, SLA,
    DLP, SIEM, CCTV…).

Çıkış kodu 1 ise bulgu vardır. Rol, unvan ve klişe bulgularını düzelt, betiği
yeniden çalıştır; kalan bulguları (ör. kullanıcının kararını bekleyen
`[DOLDURULACAK]`) `_tarama.md` özetiyle `OKUBENI.md`'ye gir. Betiğin
yakalayamadığı tek şey anlam tutarlılığıdır (aynı faaliyete iki farklı sıklık):
bunun için `ghost-writer-tutarlilik-rehberi.md`'deki okuma listesini uygula.

### 7 — Klasör ve kodlama şeması

`references/entegrasyon-kod-ve-klasor-semasi.md` içindeki birleşik klasör ağacını
kur. Kısaca: ortak katman `EYS-`, standarda özgü katman kendi öneki, tek
`00_Kapsam_ve_ElKitabi` ve tek `07_Denetim_Hazirlik` klasörü, standart başına ayrı
klasör açma — bu tam olarak "beş ayrı sistem" görüntüsünü yeniden yaratır.

`07_Denetim_Hazirlik` içindeki dosyalar **K2 kuralına tabidir**: kodsuz, kapakta
"YOL GÖSTERİCİ", antette "Doküman Türü | Yol Gösterici" ibaresiyle ve Geçerli
Doküman Listesi'nin dışında üretilir.

### 8 — Birleşik kanıt matrisi ve öz denetim (yol gösterici)

Beş ayrı öz kontrol yerine **tek** matris üret (K2'ye tabi): satırlar Madde 4–10 +
her standardın kendi Ek A/standarda özgü gereklilikleri, sütunlar kapsamdaki
her standart için "karşılanıyor mu / hangi dokümanla / hangi kanıtla". Ortak
maddeler bir kez görünür, çoklu ✓ alır. Sonra her standardın kendi
`<alt skill>/references/denetim-oz-kontrol.md` listesini yalnızca **o standarda özgü**
satırlar için ek bir geçiş olarak uygula — ortak maddeleri tekrar tekrar kontrol
etmek zaman kaybıdır ve tutarsız sonuç riski taşır.

Öz değerlendirmeye bir de **"Bilinen Boşluklar"** sekmesi ekle: üretim sırasında
fark ettiğin, kuruluşun kapatması gereken eksikler (atanmamış roller, ölçülmemiş
başlangıç değerleri, imzalanmamış sözleşmeler, yapılmamış tetkik/YGG) öncelik,
sorumlu ve termin sütunlarıyla listelenir. Bu sekme setin dürüstlüğünü gösterir
ve yönetim için yol haritası işlevi görür: üretilen dokümantasyonun neyi
karşıladığını ve neyi karşılamadığını ayırır.

### 9 — Teslim

`OKUBENI.md`'yi kök dizinde üret: kapsamdaki standartlar, üretilen kodlu doküman
sayısı ve yol gösterici sayısı (ayrı), yapılan varsayımlar ve somut sonuçları,
"Denetim öncesi kapatılması gerekenler" tablosu (öncelik, konu, dosya,
yapılacak), etiket sayımı, öz denetimde çıkan boşluklar, 6. adımdaki tutarlılık
taramasının sonucu, üretilmeyenler ve nedeni, sonraki adımlar.

Seti **yeni bir alt klasöre** yaz (ortama göre araç: Çalışma ortamı tablosu);
kullanıcının mevcut dosyalarını değiştirme. Yeniden üretimde adı değişen
dosyaların eski kopyalarını silme, `_to_delete/` alt klasörüne taşı.

## Çalışma ortamı

Bu skill hem Cowork'te hem Claude Code'da çalışır. Aracı ortama göre seç:

| İş | Cowork (bağlı klasör) | Claude Code / yerel |
|---|---|---|
| Mevcut dosyaları okuma | `device_list_dir`, `device_bash` ile yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları `device_stage_files` ile al | `Read`, `Glob`, `Bash`/`PowerShell` ile doğrudan |
| Script çalıştırma | `python3 scripts/<betik>.py …` | `python scripts/<betik>.py …` (Windows'ta `py -3` de olur). `scripts/` yolu skill'in taban dizinine göredir; Claude Code bu dizini skill yüklenirken "Base directory" satırında verir |
| Teslim | `device_commit_files` ile bağlı klasörde **yeni alt klasör** | Kullanıcının gösterdiği klasörde, yoksa çalışma dizininde **yeni alt klasör** |
| Dosyaları sunma | `mcp__cowork__present_files` | Tam dosya yollarını listele |

Her iki ortamda: kullanıcının mevcut dosyalarını değiştirme ve silme. Yeniden
üretimde adı değişen eski dosyaları `_to_delete/` alt klasörüne taşı
(`mv -n`) ve söyle.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Keşif | `iso-*-dokuman-seti` skill'leri (Skill aracı) | Standarda özgü katman ve motor |
| Girdi | Bağlı klasör / yerel dosya sistemi (bkz. Çalışma ortamı) | Mevcut dokümanları yerinde oku; yalnız şablon/görsel kontrol dosyalarını buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa |
| Mevzuat | WebSearch / Firecrawl; `regulatory-legal:reg-feed-watcher`, `regulatory-legal:policy-diff`, `regulatory-legal:gaps` | Mevzuat güncelliği ve politika boşlukları |
| Hukuki içerik | `privacy-legal:*` (27701), `ai-governance-legal:*` (42001), `commercial-legal:vendor-agreement-review` / `saas-msa-review` (tedarikçi), `employment-legal:policy-drafting` (İK) | Standarda özgü hukuki metinlerin kalitesi |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf`, `anthropic-skills:pptx` (YGG sunumu) | Üretim ve doğrulama |
| Görsel kontrol | `soffice` → `pdftoppm` → Read | Şablon birebirliği, tablo taşmaları |
| Teslim | Yeni alt klasöre teslim (bkz. Çalışma ortamı), gerekirse Artifact (paylaşılacak özet sayfa) | |

## Kanıt üretimi — nerede durulur

Kullanıcı doküman seti tamamlandıktan sonra sıklıkla "artık kanıtları da oluşturalım"
der: eğitim katılım kayıtları, iç tetkik raporu, YGG tutanağı, DÖF kayıtları,
geri dönüş testi sonucu. Burada net bir sınır vardır:

- **Üretilebilir:** boş şablonun kuruluşa özgü önceden doldurulmuş hâli — tetkik
  raporunun kapsam/kriter/soru bölümleri, YGG gündemi ve girdi başlıkları, eğitim
  içerik planı, tatbikat senaryosu. Bunlar faaliyeti **kolaylaştıran** hazırlıklardır.
- **Üretilemez:** gerçekleşmemiş bir faaliyetin gerçekleşmiş gibi görünen kaydı —
  yapılmamış tetkikin bulguları, toplanmamış YGG'nin kararları ve katılımcıları,
  verilmemiş eğitimin imzalı katılım listesi, yapılmamış testin sonucu, gerçek kişi
  adı ve telefon numarası uydurulmuş iletişim listesi.

Bu ayrım pazarlık konusu değildir. Sahte kayıt denetimde tespit edildiğinde tek bir
bulgu değil, **tüm sistemin güvenilirliğinin reddi** sonucunu doğurur; kuruluşu
doküman eksiğinden çok daha ağır bir yere koyar. Kullanıcı ısrar ederse bu sonucu
açıkça söyle ve alternatifi öner: faaliyeti gerçekten yürütmesi için gereken her
şeyi hazırla (gündem, soru listesi, sunum, form), faaliyet yapıldıktan sonra onun
verdiği gerçek bilgiyle kaydı doldur.

Aynı şekilde `[DOLDURULACAK]` alanlarını kapatırken: kişi adları, telefon
numaraları, gerçek sistem adları, sözleşme süreleri ve mali eşikler kullanıcıdan
alınır — uydurulmaz. Yalnızca kuruluşun kendi verdiği bilgiden türetilebilen
alanlar (tarih hesabı, sonuç türetimi, sınıflandırma) doldurulur; hangi alanların
kullanıcı girdisiyle, hangilerinin türetimle dolduğunu teslimde ayırt et.

## Mevcut ayrı sistemleri birleştirme

Kullanıcı sıfırdan kurmuyor, elinde zaten bir veya birkaç standart için ayrı
üretilmiş doküman seti varsa akış tersine döner:

1. Mevcut dosyaları klasör klasör tara, her dosyayı hangi maddeye/kontrole karşılık
   geldiğine göre sınıflandır (dosya adları çoğu zaman kodlama şemasından bellidir).
2. Aynı işi gören ama farklı standartlar için ayrı ayrı yazılmış dokümanları eşleştir
   (örn. iki ayrı "İç Tetkik Prosedürü" — biri BGYS-PR-10, öteki İSYS-PR-08). Bunlar
   birleştirme adayıdır.
3. İçerik olarak çelişen noktaları (farklı sıklık, farklı sorumlu rol) kullanıcıya
   göster ve hangisinin doğru/güncel olduğunu sor — kendi başına birini seçme.
4. Onaylanan birleşik içerikle tek `EYS-` dokümanı yaz, madde/kontrol referanslarını
   her iki standarda göre güncelle, eskilerini "birleştirildi → EYS-PR-XX" notuyla
   arşivlenmek üzere işaretle (silme kararını kullanıcıya bırak).
5. Kullanıcı mevcut dokümanların yeniden yazılmasını istemiyorsa her biri için
   "eklenecek içerik + öncelik + kabul kriteri" veren bir revizyon rehberi (K2,
   kodsuz) üret.
6. 4–9 arası adımları normal akıştaki gibi tamamla.

Mevcut dosyalarda sık görülen ve raporlanması gereken sorunlar: kayıt
dosyalarında sütun kayması (başka birimin/şablonun içeriği), formülsüz/#N/A
skorlar, "süresiz" saklama, Uygulanabilirlik Bildirgesi'nde gerekçe/durum sütunu
olmaması, doküman listesinde aynı adlı farklı kodlar ve boş revizyon alanları.
Bunları üretime geçmeden önce Mevcut Doküman Değerlendirme ve Boşluk Raporu'nda
(K2) listele.

## Ölçek gerçekçiliği

Entegre kurulum küçük bir kuruluşta dokümanı **azaltmalı**, çoğaltmamalı — bu
skill'in en güçlü tarafı budur. 30 kişilik bir şirkete beş standardın toplamı
kadar (150+) dosya vermek felç edici olur, kimse okumaz. Her standardın kendi
`dokuman-listesi.md`'sindeki sadeleştirilmiş set eşiğini (genelde 50 çalışan altı)
kapsamdaki **her** standart için ayrı ayrı değerlendir ama ortak katmanı bir kez
say — sadeleştirilmiş 27001 + sadeleştirilmiş 22301 ortak Madde 4–10'u paylaştığı
için toplam dosya sayısı iki setin toplamından belirgin şekilde azdır; bunu
planlama ekranında kullanıcıya göster, bu entegre kurulumun somut faydasıdır.

Çok küçük kuruluşlarda (10 kişi altı) sadeleştirme dosya **silmekten** değil
**birleştirmekten** gelir: ilişkili prosedürleri tek dokümanda topla (erişim
kontrolü + kullanıcı hesap yönetimi; iş sürekliliği + iş etki analizi; fiziksel
güvenlik + bakım), formları temaya göre gruplu tek dosyada ver, listeleri çok
sekmeli tek çalışma kitabında topla. Gereklilik kaybolmaz, dosya sayısı yarıya iner.

Ayrıca bu ölçekte **görevler ayrılığı** kaçınılmaz olarak tam sağlanamaz. Bunu
gizleme: atama yazısında çakışmaları tablo hâlinde listele ve her biri için telafi
edici kontrolü (ikinci onay, çapraz gözden geçirme tutanağı, dış tetkikçi kullanımı)
yazılı hâle getir. Denetçi bu tabloyu gördüğünde kuruluşun kısıtının farkında
olduğunu anlar; görmezse kendi bulur ve bulgu yazar.

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/annex-sl-cekirdek-haritasi.md` | Kapsam netleşince, Madde 4–10 planını kurarken |
| `references/kapsam-belirleme-ve-gorusme.md` | Görüşme adımında — birleşik soru sırası |
| `references/entegrasyon-kod-ve-klasor-semasi.md` | Üretime başlamadan, kodlama/klasör kararı verirken |
| `references/ghost-writer-tutarlilik-rehberi.md` | Üretim bitince — son tutarlılık geçişinde, atlama |

## Bağımlılıklar

Doğrudan bağımlılığı yok; kapsamdaki `iso-*-dokuman-seti` skill'lerinin
motorlarını kullanır ve onların bağımlılığını (`python-docx`, `openpyxl`) devralır:

```bash
pip install python-docx openpyxl
```

Linux'ta "externally-managed-environment" hatası alırsan komuta
`--break-system-packages` ekle; Windows ve macOS'ta gerekmez.
