---
name: iso-42001-dokuman-seti
description: "ISO/IEC 42001:2023 Yapay Zekâ Yönetim Sistemi için denetimden geçebilecek doküman setini üretir ve yaşatır: kapsam, YZ politikası, risk ve etki değerlendirmesi (42005 hizalı), Ek A/Uygulanabilirlik Bildirgesi, envanter, veri yönetişimi, olay-bildirim zinciri, YZ okuryazarlığı, yasal uyum matrisi, Aşama 1/2 ve gözetim denetimi paketleri, 208 soruluk soru bankası. ai-governance-legal eklentisi kuruluysa profilini, ai-systems.yaml envanterini ve triyaj, AIA, tedarikçi, boşluk analizi, politika çıktılarını sete bağlar. \"ISO 42001\", \"YZYS\", \"AIMS\", \"AI yönetişimi\", \"YZ politikası\", \"AI etki değerlendirmesi\", \"YZ risk değerlendirmesi\", \"AI envanteri\", \"42001 belgelendirme/iç tetkik\", \"Aşama 1/2 denetimi\", \"YGG hazırlığı\", \"yeni YZ aracını YZYS'ye ekle\" denince mutlaka kullan; standart anılmasa da sorumlu YZ, AI Act hazırlığı veya eklenti çıktılarını yönetim sistemine işleme bağlamında devreye gir."
metadata:
  surum: "2.0.0"
---

# ISO/IEC 42001:2023 Yapay Zekâ Yönetim Sistemi Doküman Seti Üretimi

Bu skill bir kuruluşun YZYS'sini kuran doküman setini üretir ve belgelendirme
sonrasında yaşatır. Hedef dosya
sayısı değil: **denetçinin masaya koyduğunda uygunsuzluk yazamayacağı bir set.**

42001'in diğer yönetim sistemlerinden en önemli farkı: burada **iki ayrı
değerlendirme** vardır ve ikisi karıştırılamaz.

- **YZ risk değerlendirmesi (6.1.2/6.1.3)** — riskin *kuruluşa* etkisi
- **YZ sistemi etki değerlendirmesi (6.1.4/8.4)** — YZ sisteminin *kişilere,
  kişi gruplarına ve topluma* etkisi

İkinci değerlendirme diğer hiçbir Annex SL standardında yoktur ve 42001'in
varlık sebebidir. Bu skill'in ağırlık merkezi oradadır.

## Çalışma akışı

### 0 — Modu ve eklentiyi algıla (her çalışmanın ilk dakikası)

**Mod.** İstek kurulum mu, sürdürme mi (set var, yeni sistem/değişiklik/YGG),
denetim hazırlığı mı (Aşama 1, Aşama 2, gözetim, yeniden belgelendirme), yoksa
mevcut dokümanların boşluk analizi mi? Sürdürme ve denetim modları için
`references/surdurme-ve-denetim-asamalari.md` dosyasını oku; bu modlarda yeni
doküman seti üretme, mevcut kayıtları revize et.

**Hafif yol.** Kullanıcı kısa bir soru soruyorsa ("hangi dokümanlar
güncellenmeli?", "bu kontrol ne ister?") anketi ve üretim akışını çalıştırma:
cevabı ilgili referanstan ver, cevabı değiştirecek en fazla 3–5 netleştirme
sorusunu sonda sor. Açılış anketi yalnız set üretimi veya kayıt doldurma
başlarken zorunludur.

**Eklenti.** Kullanıcı eklentinin kurulu olmadığını söylediyse o beyan
esastır. Aksi hâlde `ai-governance-legal:*` yetenekleri listede varsa
`references/eklenti-entegrasyonu.md` dosyasını oku ve profili ara
(`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/` — bulutta,
yoksa bağlı bilgisayarda). Profil doluysa açılış anketini profilden önceden
doldur ve yalnız eksikleri sor. Profil yoksa skill **durmaz**: kendi anketini
yürüt, bir kez `cold-start-interview` öner. Profil ve `ai-systems.yaml`
yalnızca okunur; yazma eklentinin kendi yetenekleriyle ve kullanıcı onayıyla
olur. Eklenti yoksa sürdürme akışlarındaki eklenti
adımlarının elle karşılığı `surdurme-ve-denetim-asamalari.md` §2'deki
"Eklenti yoksa" tablosundadır; hukuki sınıflandırma (AB YZ Yasası rolü/seviyesi,
KVKK aktarım dayanağı) bu skill'de yapılmaz, hukuk birimine `[Hukuk teyidi]`
etiketiyle devredilir.

**Bağlam.** Danışman çok müşteriye set hazırlıyorsa matter workspace kullan
(`eklenti-entegrasyonu.md` §7): aktif müşteri belli olmadan üretme, müşteriler
arası içerik taşıma.

**Güncellik.** Mevzuat veya standart tarihine dayanan her bölümden önce
`guncellik-izleme.md` son teyit tarihine bak; 90 günden eskiyse
ilgili satırları web aramasıyla kontrol et.

### 1 — Kuruluşu tanı (üretimden önce, her zaman)

`references/gorusme-rehberi.md` dosyasındaki altı soruluk açılış anketini sor.
`AskUserQuestion` varsa onunla sor. Eklenti profili doluysa cevapları
`eklenti-entegrasyonu.md` §2 eşlemesiyle önceden doldur ve "profilinizde şunu
gördüm, doğru mu?" diye tek ekranda teyit ettir.

42001'e özgü olarak şu beşini mutlaka sor — kapsam ve rol tanımı bunlara bağlı:

- **YZ ekosistemindeki rolünüz hangisi: sağlayıcı, üretici, müşteri, ortak?**
  Standart bu rolleri ayırır ve yükümlülükler role göre değişir. Eski üçlü ayrım
  (geliştirici/sağlayıcı/kullanıcı) yetersizdir; tam taksonomi ve rol-kontrol
  eşlemesi `references/roller-ve-yetkinlik.md` §1'dedir. Çoğu kuruluş birden
  fazla roldedir; hangisi hangi sistem için netleşmeli. Eklenti envanterindeki
  AB YZ Yasası rolü (provider/deployer…) **başka bir eksendir**; eşleme önerisi
  `eklenti-entegrasyonu.md` §5'tedir, otomatik çevirme.
- **Hangi YZ sistemlerini kullanıyor/geliştiriyorsunuz?** `ai-systems.yaml`
  varsa oradan başla. Yoksa somut liste isteyin —
  "yapay zeka kullanıyoruz" bir envanter değildir. Üçüncü taraf büyük dil modeli
  arayüzleri, gömülü YZ özellikli yazılım hizmetleri ve kendi modelleriniz ayrı
  ayrı sayılmalı.
- **YZ sistemi kişiler hakkında karar veriyor mu, veriyi etkiliyor mu?**
  (işe alım, kredi, sigorta, sağlık, eğitim, içerik moderasyonu, fiyatlandırma)
  Etki değerlendirmesinin ağırlığını bu belirler.
- **Hangi verilerle eğitiliyor/besleniyor?** Kişisel veri, özel nitelikli veri,
  telifli içerik, müşteri verisi? Ek A.7 veri kontrollerinin uygulanabilirliği
  buna bağlı; kişisel veri varsa 27701 kesişimi doğar.
- **AB bağlantınız var mı?** AB'de sunuluyor mu, AB'deki kişileri etkileyen
  çıktı üretiyor mu? Cevap "evet" ise yasal uyum matrisi (YZYS-LS-10) devreye
  girer; bkz. `references/mevzuat-kesisimi.md`.

Kapsamdaki her YZ sistemi için ayrıca `gorusme-rehberi.md` §1b'deki **sistem
bazlı derin anketi** geç — envanter, risk kaydı ve etki değerlendirmesinin üçü
de o cevaplardan doğar.

Ayrıca sor: kişi adı mı unvan mı kullanılacak, Revizyon 0 yayın tarihi, kurumsal
şablon birebir mi kullanılacak, mevcut dokümanlar yeniden mi yazılacak yoksa
revizyon rehberiyle mi ele alınacak.

Kurumsal şablon yüklendiyse önce tanı:

```bash
python scripts/sablon_analiz.py "<şablon.docx>"
```

### 2 — Kapsamı ve plan taslağını onaylat

Üretime başlamadan tek ekranlık planı sun: kapsam beyanı, kuruluşun YZ rolü/rolleri,
kapsanan YZ sistemleri, doküman sayısı, kodlama kuralı, hariç tutulacak Ek A
kontrolleri, hangi dosyaların kodsuz yol gösterici olacağı.

Kapsam cümlesi kalıbı:

> "[Unvan]'ın [lokasyon] adresinde, [rol: sağlayıcı/üretici/müşteri/ortak]
> sıfatıyla [YZ sistemi/sistemleri] üzerinde yürüttüğü [faaliyetler] kapsamındaki
> yapay zekâ yönetim sistemi. Uygulanabilirlik Bildirgesi Rev. [nn] geçerlidir."

Kuruluşun YZ rolünü kapsam beyanında belirtmek, denetçinin hangi gereklilikleri
arayacağını netleştirir ve gereksiz tartışmayı önler.

### 3 — Üret

Sıra kritiktir; iki değerlendirme zinciri paraleldir:

1. **Kapsam + El Kitabı** (4.3, 4.4)
2. **Bağlam, ilgili taraflar, YZ rolü, iklim değerlendirmesi** (4.1, 4.2)
3. **YZ politikası** (5.2) ve diğer kurumsal politikalarla uyum (Ek A.2.3) —
   kuruluşun YZ kullanım politikası yoksa önce `policy-starter` taslağını al;
   42001'in zorunlu taahhütlerini (gerekliliklere uyum, sürekli iyileştirme,
   hedef çerçevesi) sen ekle. Profildeki kırmızı çizgiler yasaklı kullanımlara girer.
4. **Rol ve sorumluluk matrisi** (5.3, A.3.2) — on sorumluluk alanının tamamı;
   profildeki eskalasyon tablosuyla tutarlı olmalı
5. **YZ sistem envanteri** — iki zincirin de girdisi. `ai-systems.yaml` varsa
   `scripts/envanter_senkron.py aktar` ile hukuki sütunları doldur; 42001
   alanlarını kullanıcıyla tamamla. AB bağlantılı ama sınıflandırılmamış sistem
   → `ai-inventory classify` devri
6. **YZ risk değerlendirmesi → risk işleme → Uygulanabilirlik Bildirgesi** (6.1.2, 6.1.3) —
   eklenti bulgularının önem derecesi taban olarak geçer
7. **YZ sistemi etki değerlendirmesi** (6.1.4, 8.4, Ek A.5) — ayrı zincir, 42005
   hizalı (`42005-hizalama.md`). Hukuki AIA (`aia-generation`) paralel
   yürür; 42001 raporuna yalnız sonucu ve referansı girer
8. **Yaşam döngüsü prosedürleri** (Ek A.6): gereksinim, tasarım, doğrulama/geçerleme, devreye alma, işletim/izleme, teknik dokümantasyon, olay günlükleri
9. **Veri yönetişimi** (Ek A.7): veri edinme, kalite, köken, hazırlama
10. **Şeffaflık ve iletişim** (Ek A.8), **sorumlu kullanım** (Ek A.9; kullanım
    onay akışının ilk adımı `use-case-triage`), **üçüncü taraf** (Ek A.10;
    sözleşmesi incelenmemiş her model/API için `vendor-ai-review`)
11. **Olay ve bildirim zinciri** (A.8.4, A.3.3, 10.2) ve **YZ okuryazarlığı /
    yetkinlik matrisi** (7.2, 7.3, A.4.6) — `olay-bildirim-ve-okuryazarlik.md`
12. **Yasal uyum matrisi** (YZYS-LS-10) — AB bağlantısı veya sektörel düzenleme
    varsa; satırlar `reg-gap-analysis` çıktısından beslenir
13. **Performans, iç tetkik, YGG, DÖF** (9–10) — `policy-monitor` taraması
    YGG girdisi ve A.2.4 kanıtıdır
14. **OKUBENI.md**
15. **Denetim hazırlık yol göstericileri** (kodsuz): boşluk raporu, kontrol-kanıt
    matrisi, öz değerlendirme, denetim soru bankası; denetim tarihi verildiyse
    aşamaya özgü paket (`surdurme-ve-denetim-asamalari.md` §4)

Her eklenti devrini kullanıcıya açıkça söyle ("bu sınıflandırmayı ben
yapmıyorum; `ai-inventory classify sys-003` ile yapılmalı"). Eklenti çıktısı
42001 kaydına girerken **iki katman kuralı** geçerlidir: hukuki not eklentinin
klasöründe gizli kalır, YZYS kaydına yalnız sonuç + tarih + karar veren +
referans geçer (`eklenti-entegrasyonu.md` §4).

Word için `scripts/ys_docx.py`, Excel için `scripts/ys_xlsx.py`, standarda özgü
kayıtlar için `scripts/kayitlar_42001.py` kullan. Ek A kontrolleri
`references/annex-a-kontroller.md` dosyasındadır ve bildirge scriptte hazır gelir.

Denetim hazırlık dosyaları ayrıca üretilebilir:

```bash
python scripts/kayitlar_42001.py --kurulus "<Unvan>" \
  --cikti "07_Denetim_Hazirlik" --hangi soru_bankasi,yasal,raci
```

Bu komutun çıktısını ayır: **soru bankası** bir yol göstericidir ve
`07_Denetim_Hazirlik`'te kodsuz kalır. **Yasal uyum matrisi** (YZYS-LS-10) ve
**sorumluluk matrisi** ise yönetim sisteminin işleyen kayıtlarıdır; kodlu olarak
formlar/listeler klasörüne taşı ve Doküman Listesi'ne gir. Script dosya adına kod
ekliyorsa soru bankasının adından kodu kaldır ve K2 antetini uygula.

### 4 — Öz denetim yap ve raporla

`references/denetim-oz-kontrol.md` listesini geç. §A2 bölümü 42001'e özgü
zorunlu kontrollerdir — atlanırsa doğrudan bulgu üretirler; §A3 eklenti
entegrasyonu kontrolleridir (`denetim-oz-kontrol.md` §A3). Çift zincir kontrolünü
`scripts/envanter_senkron.py zincir` ile yap: envanterdeki her YZ sisteminin
hem bir risk kaydı hem bir etki değerlendirmesi, AB bağlantısı varsa hukuki
sınıflandırması olmalı. Bir betikle kalan İngilizce kısaltmaları, kırık kod
atıflarını, yol gösterici dosyalara kodla verilmiş atıfları ve etiket sayılarını
tara. Bulguları `OKUBENI.md`'de "Denetim öncesi kapatılması gerekenler"
tablosunda raporla. Kullanıcı hukukçu değilse belirsiz tarih ve eşikler
"Emin olmadığım ve teyit edilmesi gerekenler" listesinde toplanır.

Teslimden önce tutarlılık taramasını çalıştır (K1 büyük harf, K2 kodlu
yol gösterici, K3 kısaltma, kırık kod atıfları, klişe ve ölçülemez ifade,
etiket sayımı, yayın tarihi):

```bash
python scripts/tutarlilik_tarama.py "<set klasörü>" --md "<set klasörü>/_tarama.md"
```

Çıkış kodu 1 ise bulgular vardır; kapat veya `OKUBENI.md`'de gerekçesiyle listele.

### 5 — Sonraki adım seçenekleri

Teslimden sonra kararı kullanıcıya bırakan kısa bir seçenek listesi ver:
(1) açık zincirleri ve `[DOLDURULACAK]` alanları kapatmak için sistem bazlı
oturum, (2) bekleyen hukuki devirleri sırayla çalıştırmak (hangi komut, hangi
sistem), (3) denetim aşamasına özgü paket, (4) sürdürme takvimini zamanlanmış
görev olarak kurmak, (5) başka bir şey. Envanter veya bulgu listesi 10 satırı
aşıyorsa pano (dashboard) önerisini de ekle.

## Kırılma noktaları

**İki değerlendirmenin karıştırılması.** En sık ve en ciddi hata. Risk
değerlendirmesi "bu YZ sistemi bozulursa kuruluş ne kaybeder?" sorusuna,
etki değerlendirmesi "bu YZ sistemi doğru çalışırken bile kime zarar verebilir?"
sorusuna cevap verir. İkincisi olmadan 42001 karşılanmaz. Ayrı doküman, ayrı
metodoloji, ayrı kayıt üret. Risk kriteri seti (6.1.1) **iki zinciri de**
kapsamalıdır — tek ölçekle iki zincir yönetilemez.

**İklim değişikliğinin atlanması.** 2024 tadilatıyla tüm yönetim sistemi
standartlarına eklenen madde 42001'de de geçerlidir ve belgelendirme
kuruluşlarının tetkik kontrol listelerinde ayrı satırdır: kuruluş iklim
değişikliğinin ilgili bir husus olup olmadığını belirlemelidir (4.1) ve ilgili
tarafların iklimle ilgili gereklilikleri olabilir (4.2). "İlgili değildir"
cevabı geçerlidir; **gerekçesiz bırakmak değildir.** 42001'de bu, A.4.5
(donanımın çevresel etkisi) ve A.5.5 (çevresel sürdürülebilirlik) ile besleyen
üç ayaklı bir zincirdir.

**Envanterin belirsizliği.** "ChatGPT kullanıyoruz" bir envanter kaydı değildir.
Her YZ sistemi için: adı, sağlayıcısı, kuruluşun rolü, model tipi, teknik
yaklaşım, amaçlanan kullanım, öngörülebilir amaç dışı kullanım, yasak kullanım,
kullanıcı grubu, etkilenen kişi grubu, karar özerkliği, işlenen veri, yaşam
döngüsü aşaması, sahibi. Envanter olmadan ne risk ne etki değerlendirmesi
yapılabilir.

**Üç kullanım kavramının tek sütuna sıkıştırılması.** *Amaçlanan kullanım*
(ne için tasarlandı), *öngörülebilir amaç dışı kullanım* (kullanıcı ne yapar —
A.5.3 bunu ister) ve *yasak kullanım* (ne yasaklandı — A.9.4) üç ayrı şeydir.
İkincisi neredeyse her sette eksiktir.

**Etki değerlendirmesinin eksik kalemleri.** A.5.3 yedi kalem ister ve bunların
üçü hemen her sette atlanır: **olumlu etkiler**, **öngörülebilir hatalar**,
**istihdam ve beceri etkisi**. A.5.4'ün sekiz alanından **erişilebilirlik** ve
**insan hakları** de düzenli olarak eksiktir. Ayrıntı `etki-degerlendirmesi.md`.

**İnsan gözetiminin belirsizliği.** YZ sisteminin kararına insanın ne zaman,
nasıl müdahale edebileceği tanımlı olmalı — "insan kontrolünde" ifadesi yetmez.
Kim, hangi eşikte, hangi bilgiyle, ne kadar sürede müdahale edebiliyor? Ayrıca
gözetimin **etkinliği** izlenmeli: hiç müdahale edilmeyen bir gözetim
mekanizması biçimseldir.

**Veri kökeninin atlanması.** Ek A.7.5 veri kökenini ister: verinin nereden
geldiği, hangi izinle kullanıldığı, yaşam döngüsü boyunca nasıl izlendiği —
oluşturma, güncelleme, aktarım, soyutlama, doğrulama ve kontrolün devri adımları
dahil. Telifli içerik, kazınmış veri veya belirsiz kaynaklı veri seti bu maddede
açığa çıkar. Kullanıcıya bunu sor; cevap yoksa `[DOLDURULACAK]` bırak ama görünür
bırak.

**Endişe bildiriminin tek cümleye indirgenmesi.** A.3.3 beş ayrı şey ister:
gizlilik/anonimlik, **eskalasyon mekanizması**, **misillemeden koruma**,
bildirene **durum geri bildirimi**, kanalın **yetkin kişilerce yönetilmesi**.
"Bildirim kanalı vardır" bunların hiçbirini karşılamaz.

**YZ'ye özgü güvenlik tehditlerinin atlanması.** A.6.2.6 veri zehirlenmesi,
model çalma ve model tersine çevirme saldırılarına karşı önlem ister. Genel
bilgi güvenliği kontrollerine atıf vermek yetmez; bu üç tehdide özgü önlem
yazılmalıdır.

**Teknik dokümantasyonun tek muhataba yazılması.** A.6.2.7 **her ilgili taraf
kategorisi için** teknik dokümantasyon ister. Tek bir model kartı son kullanıcı,
kurumsal müşteri ve denetim otoritesine aynı anda hitap etmeyebilir.

**Olay günlüklerinin planlanmamış olması.** A.6.2.8, hangi aşamada hangi
günlüğün tutulacağını, **saklama süresini**, **günlüklerin korunmasını** ve
günlüklerin **amaçlanan performans aralığı dışına çıkışı tespit etmeye imkân
vermesini** ister. "Loglar tutuluyor" yeterli değil.

**Tetkikçi bağımsızlığının atlanması.** 9.2 hem tetkikçi yetkinliği hem
bağımsızlığı ister. Modeli geliştiren kişi o modelin iç tetkikini yapamaz.

**Hukuki notun YZYS kaydına kopyalanması.** Eklentinin AIA'sı, triyaj
gerekçesi veya redline'ı gizlilik başlığıyla gelir. Olduğu gibi etki
değerlendirmesine veya envantere yapıştırılırsa gizli hukuki analiz denetçiye
açılır. YZYS kaydına yalnız sonuç ve referans girer (`eklenti-entegrasyonu.md` §4).

**İki rol ekseninin tek sütuna indirgenmesi.** "Deployer = YZ müşterisi"
genellikle doğrudur ama her zaman değil — kendi müşterisine YZ'li hizmet sunan
deployer 42001'de sağlayıcıdır da. Envanterde iki sütun kalır.

**Olay prosedüründe saat yok.** "Olay kaydedilir ve değerlendirilir" yazan
prosedür, KVKK ve AB YZ Yasası bildirim sürelerinin tespit anından başladığını
göstermez. Tespit zamanı dakika hassasiyetinde, her bildirim kolu için karar
satırı olmalı (`olay-bildirim-ve-okuryazarlik.md` §1).

**Okuryazarlığın tek satır eğitime indirgenmesi.** "Tüm personele YZ
farkındalık eğitimi" ne 7.2'yi ne AB YZ Yasası okuryazarlık hükmünü karşılar.
Kişi grubu × sistem × hedef × kanıt matrisi gerekir; insan gözetimi yapanlar
ve dış kişiler ayrı satırdır.

**Eskimiş tarihle yazılmış yasal bağlam.** AB YZ Yasası yüksek risk tarihleri
Digital Omnibus ile değişti; Türkiye'de kanun teklifleri bekliyor. Eğitim
verisinden veya eski bir izleme listesinden yazılan tarih, setin en hızlı
eskiyen kısmıdır. Her seferinde `guncellik-izleme.md` kontrolü.

**Uydurulmuş test/değerlendirme sonucu.** Model performans metrikleri, yanlılık
test sonuçları, doğruluk oranları uydurulamaz. Boş şablon ve metodoloji üret;
sayıları kuruluş doldurur. Bu özellikle kritik: sahte adillik metriği hem
denetimi hem de etkilenen kişileri yanıltır.

**Uydurulmuş mevzuat atfı.** Madde numarası, yürürlük tarihi, ceza tutarı ve
"uyumludur" beyanı bu skill tarafından üretilemez. Her mevzuat atfı
`[yerleşik]` / `[teyit]` / `[teyit-madde]` etiketlerinden biriyle işaretlenir;
kural `mevzuat-kesisimi.md` §1'dedir.

## Mevcut doküman analizi

Kullanıcı hazır dokümanlar verdiğinde önce **Mevcut Doküman Değerlendirme ve
Boşluk Raporu**'nu (kodsuz yol gösterici) üret. Tara ve raporla: envanterde risk
kaydı veya etki değerlendirmesi olmayan sistemler, tek sütuna sıkıştırılmış
kullanım kavramları, eksik etki değerlendirmesi kalemleri, gerekçesiz iklim
kararı, Uygulanabilirlik Bildirgesi'nde gerekçe/durum sütunu olmaması, formülsüz
skorlar, doküman listesinde aynı adlı farklı kodlar. Kullanıcı mevcut dokümanların
yeniden yazılmasını istemiyorsa her biri için "eklenecek içerik + öncelik + kabul
kriteri" veren bir **revizyon rehberi** (kodsuz yol gösterici) üret.

## Denetim hazırlık yol göstericileri (07_Denetim_Hazirlik)

Boşluk raporu, revizyon rehberleri, kontrol-kanıt matrisi, öz değerlendirme ve
denetim soru bankası yönetim sistemi dokümanı değildir; denetim öncesinde üst
yönetime neyin, kim tarafından, hangi sırayla yapılacağını gösteren yol
göstericilerdir. `iso-entegre-yonetim-sistemi` K2 kuralı uygulanır: doküman kodu
yok, dosya adı yalnız ad; kapakta "YOL GÖSTERİCİ", antette "Doküman Türü | Yol
Gösterici"; onay YZYS komitesi başkanı; metnin başında "yönetim sistemi dokümanı
değildir" notu; Doküman Listesi'ne girmez ve listenin not alanında bu açıklanır;
setin geri kalanı bu dosyalara adıyla atıf verir.
Motorda: `Kimlik(..., tur="yol_gosterici")` ver ve dosyayı `k.dosya_adi()` ile kaydet; kapak, antet etiketi, giriş notu ve kodsuz dosya adı otomatik gelir.

## Türkçe terim kuralı

Kullanıcı aksini istemedikçe başlık ve doküman adlarında İngilizce kısaltma
kullanma: AIMS → Yapay Zekâ Yönetim Sistemi, AI → YZ, AIIA → YZ Sistemi Etki
Değerlendirmesi, SoA → Uygulanabilirlik Bildirgesi, LLM → büyük dil modeli,
bias → yanlılık, model card → model kartı, provenance → veri kökeni, data
poisoning → veri zehirlenmesi, human oversight → insan gözetimi, RACI →
sorumluluk matrisi. İngilizce karşılık yalnız Tanımlar tablosunda parantez
içinde bir kez verilir; ürün adları olduğu gibi kalır. Motor (`ys_docx.py` 2.0.0)
Word metinlerine `tr()` sözlüğünü otomatik uygular; Excel'de ve kendi kodunda
`tr()` ve `tr_upper()` çağır.

## Kurumsal şablonu birebir kullanma

Kullanıcı bir kurumsal dokümanı "şablon olarak bire bir kullan" derse
`ys_docx.py` yerine şablonu klonla (`iso-entegre-yonetim-sistemi` K4): kapak kodu
ve antet hücrelerini değiştir, başlık/gövde/liste paragraflarını rPr dahil
prototip olarak çoğalt, İçindekiler'i bookmark + `PAGEREF` ile kurup sayfa
numaralarını LibreOffice render + `pdftotext` ile hesapla, sabit toplam sayfa
metnini `SECTIONPAGES` alanıyla değiştir. Excel'de kuruluşun mevcut liste
dosyasının bilgi sayfasını ve logosunu koru. Her dosyayı PDF'e çevirip görsel
kontrol et.

## Kullanıcı tek doküman istediğinde

Süreci kısalt, kaliteyi koru: kuruluş, YZ rolü, ilgili sistem ve varsa şablonu
sor; üret; ilgili maddeleri ve kanıt beklentisini dokümanın sonunda belirt.

## Entegre sistem ve mevzuat

ISO 27001 ile birlikte kurulması yaygındır: 42001'in veri ve güvenlik kontrolleri
27001 Ek A ile büyük ölçüde örtüşür; ortak dokümanları `EYS-` önekiyle tek
doküman üret. Kişisel veri işleyen veya kişiler hakkında otomatik karar veren
sistemlerde 27701 (7.3.10 / A.1.3.11) kesişir: YZ etki değerlendirmesi ile
gizlilik etki değerlendirmesini birleştirme, birbirine referans ver. Birden fazla
standart kapsamdaysa `iso-entegre-yonetim-sistemi` ile çalış.

**42001 tek başına hiçbir yasal uyumu sağlamaz.** Bunu net söyle — abartılı uyum
iddiası kullanıcıyı yanıltır ve gerçek bir riske sokar. Doğru cümle şudur:
42001, AB YZ Yasası ve benzeri düzenlemelerin beklediği kanıtlarla **aynı
malzemeyi** üretir (risk yönetimi, veri yönetişimi, teknik dokümantasyon, olay
günlükleri, şeffaflık, insan gözetimi) ama **aynı yükümlülüğü karşılamaz.**

Kullanıcı AB YZ Yasası, KVKK veya sektörel YZ düzenlemelerinden bahsederse:
`references/mevzuat-kesisimi.md` dosyasını oku ve YZYS-LS-10 Yasal Uyum ve
Yükümlülük Matrisi'ni üret. Sınıflandırma (rol, risk seviyesi, hukuki dayanak)
**bu skill tarafından yapılmaz** — matriste yeri açılır, hukuk birimine
devredilir. `ai-governance-legal` kuruluysa devir somut komutlarla yapılır
(`mevzuat-kesisimi.md` §6, `eklenti-entegrasyonu.md` §3); yürürlük tarihleri
`guncellik-izleme.md`'den kontrol edilir.

## Çalışma ortamı

Bu skill hem Cowork'te hem Claude Code'da çalışır. Aracı ortama göre seç:

| İş | Cowork (bağlı klasör) | Claude Code / yerel |
|---|---|---|
| Mevcut dosyaları okuma | `device_list_dir`, `device_bash` ile yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları `device_stage_files` ile al | `Read`, `Glob`, `Bash`/`PowerShell` ile doğrudan |
| Script çalıştırma | `python3 scripts/<betik>.py …` | `python scripts/<betik>.py …` (Windows'ta `py -3` de olur). `scripts/` yolu skill'in taban dizinine (bu SKILL.md'nin bulunduğu klasör) göredir; Claude Code skill yüklenirken bunu "Base directory" satırında verir, dosya doğrudan okunduysa SKILL.md'nin klasörünü kullan |
| Teslim | `device_commit_files` ile bağlı klasörde **yeni alt klasör** | Kullanıcının gösterdiği klasörde **yeni alt klasör**; klasör belirtilmediyse üretimden önce sor |
| Dosyaları sunma | `mcp__cowork__present_files` | Tam dosya yollarını listele |

Her iki ortamda: kullanıcının mevcut dosyalarını değiştirme ve silme. Yeniden
üretimde adı değişen eski dosyaları `_to_delete/` alt klasörüne taşı
(`mv -n`) ve söyle.

## Kullanılacak skill'ler ve connector'ler

| Aşama | Skill / connector | Ne için |
|---|---|---|
| Girdi | `ai-governance-legal` profili + `ai-systems.yaml` | Açılış anketi, envanter, kırmızı çizgiler, tedarikçi pozisyonları, eskalasyon (`eklenti-entegrasyonu.md`) |
| Girdi | Bağlı klasör / yerel dosya sistemi (bkz. Çalışma ortamı) | Bağlı klasördeki envanter, profil ve dokümanları yerinde oku; yalnız şablon ve görsel kontrol gereken dosyaları buluta al |
| Girdi | Google Drive connector | Doküman kütüphanesi Drive'daysa |
| Kullanım onayı (A.9) | `ai-governance-legal:use-case-triage` | Yeni YZ talebinin ilk adımı; sonuç onay kaydına, 🔴 gerekçeleri politikaya |
| Hukuki sınıflandırma | `ai-governance-legal:ai-inventory` (`add`, `classify`) | Sistem bazlı AB YZ Yasası rol ve risk seviyesi — skill sınıflandırmaz |
| Hukuki etki | `ai-governance-legal:aia-generation` | Rejim bazlı değerlendirme, FRIA ihtiyacı; 42001 etki değerlendirmesine sonuç + referans |
| Tedarikçi (A.10) | `ai-governance-legal:vendor-ai-review`; `commercial-legal:saas-msa-review` | Model/API sözleşmesinin YZ maddeleri ve geri kalanı |
| Yasal uyum (LS-10) | `ai-governance-legal:reg-gap-analysis`; `regulatory-legal:reg-feed-watcher` | Yeni düzenleme → gereklilik → matris satırı |
| Politika (5.2) | `ai-governance-legal:policy-starter` | Model politikalardan kaynaklı taslak gövde |
| İzleme / YGG | `ai-governance-legal:policy-monitor` | Sapma taraması → 9.1, A.2.4, 9.3 girdisi |
| Profil | `ai-governance-legal:customize`, `cold-start-interview` | 42001 çalışmasında kararlaşan yeni kırmızı çizgi/kademe; profil yoksa kurulum |
| Müşteri ayrımı | `ai-governance-legal:matter-workspace` | Danışman modu |
| Kişisel veri | `iso-27701-dokuman-seti`, `privacy-legal:pia-generation`, `privacy-legal:reg-gap-analysis` | Eğitim/girdi verisinde kişisel veri, otomatik karar |
| Mevzuat | WebSearch / Firecrawl; Yargı MCP (eklentiyle gelir) | Güncellik, KVKK Kurul kararları; tarih uydurma |
| İK | `employment-legal:policy-drafting` | İşe alımda YZ, istihdam ve beceri etkisi |
| Zamanlama | Zamanlanmış görevler (`create_trigger`) | Sürdürme takvimi — yerel cron değil |
| Çıktı | `anthropic-skills:docx`, `anthropic-skills:xlsx`, `anthropic-skills:pdf` | Üretim ve doğrulama |
| Görsel kontrol | `soffice` → `pdftoppm` → Read | Şablon birebirliği, tablo taşmaları |
| Entegrasyon | `iso-entegre-yonetim-sistemi`, `iso-27001-dokuman-seti` | Ortak katman, K1–K4 kuralları |
| Teslim | Yeni alt klasöre teslim (bkz. Çalışma ortamı) | Kullanıcının dosyalarını değiştirmeden teslim |

## Referans dosyaları

| Dosya | Ne zaman oku |
|---|---|
| `references/gorusme-rehberi.md` | Her çalışmanın başında (§1b sistem bazlı anket dahil) |
| `references/dokuman-listesi.md` | Plan aşamasında |
| `references/roller-ve-yetkinlik.md` | Rol taksonomisi, sorumluluk ve yetkinlik matrisi yazarken |
| `references/madde-4-10.md` | Yönetim sistemi dokümanlarını yazarken |
| `references/annex-a-kontroller.md` | Bildirge ve kontrol dokümanlarını yazarken |
| `references/etki-degerlendirmesi.md` | Etki değerlendirmesi ve risk ayrımı — bu standardın kalbi |
| `references/mevzuat-kesisimi.md` | AB bağlantısı, KVKK, sektörel düzenleme veya tedarikçi sözleşmesi gündeme geldiğinde |
| `references/icerik-rehberi.md` | Metin kalitesi — örnek zayıf/güçlü metinler |
| `references/dokuman-mimarisi.md` | Kodlama, hiyerarşi, ortak bölümler |
| `references/denetim-oz-kontrol.md` | Teslim öncesi (§A2 42001'e özgü, §A3 eklenti kontrolleri) |
| `references/eklenti-entegrasyonu.md` | `ai-governance-legal` kuruluysa — her zaman; iki katman kuralı, rol/etiket eşlemesi, danışman modu |
| `references/surdurme-ve-denetim-asamalari.md` | Set zaten varsa, denetim tarihi verildiyse, YGG/iç tetkik hazırlığında |
| `references/olay-bildirim-ve-okuryazarlik.md` | Olay prosedürü, endişe bildirimi, yetkinlik/eğitim matrisi yazarken |
| `references/42005-hizalama.md` | Etki değerlendirmesi metodolojisini 42005:2025'e hizalarken |
| `references/guncellik-izleme.md` | Mevzuat veya standart tarihi içeren her bölümden önce |

## Varlıklar

| Dosya | İçerik |
|---|---|
| `assets/annex_a_42001.json` | 38 Ek A kontrolü — bildirge üreticisinin girdisi |
| `assets/denetim_sorulari_42001.json` | **208 denetçi sorusu**, 65 bölüm (27 madde + 38 kontrol), her bölüm için kanıt listesi |

## Betikler

| Betik | Ne yapar |
|---|---|
| `scripts/ys_docx.py` | Kurumsal Word dokümanı |
| `scripts/ys_xlsx.py` | Kurumsal Excel kaydı |
| `scripts/kayitlar_42001.py` | Standarda özgü kayıtlar (envanter, SoA, risk, etki, olay, yetkinlik, soru bankası, yasal, sorumluluk matrisi…) |
| `scripts/envanter_senkron.py` | `ai-systems.yaml` ↔ YZYS-LS-04 iki yönlü eşleme: `aktar` (YAML hukuki alanları Excel'e, 42001 alanları mevcut Excel'den korunur), `fark` (çelişki raporu), `oneri` (yalnız Excel'deki sistemler için YAML taslağı — ai-systems.yaml'a dokunmaz), `zincir` (risk + etki + hukuki sınıflandırma kapalılığı) |
| `scripts/sablon_analiz.py` | Kurumsal şablon tanısı |

Sahiplik kuralı: hukuki alanlar (ad, sahip, durum, AB bağlantısı, AB YZ Yasası
rolü ve seviyesi) YAML'dan Excel'e akar, geri akmaz. Çelişkide YAML yanlışsa
önce `ai-inventory edit <id>` ile düzeltilir, sonra `aktar` tekrarlanır.

## Bağımlılıklar

`python-docx` ve `openpyxl` gerekir (42001 eklenti senkronu için ayrıca `pyyaml`):

```bash
pip install python-docx openpyxl pyyaml
```

Linux'ta "externally-managed-environment" hatası alırsan komuta
`--break-system-packages` ekle; Windows ve macOS'ta gerekmez.
