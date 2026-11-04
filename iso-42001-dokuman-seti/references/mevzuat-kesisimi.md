# Mevzuat Kesişimi — 42001 Nerede Biter, Hukuk Nerede Başlar

**Bu dosyanın birinci kuralı:** ISO/IEC 42001 bir yönetim sistemi standardıdır.
Tek başına hiçbir yasal yükümlülüğü karşılamaz, hiçbir uyumu garanti etmez.
Yaptığı şey, uyumun **altyapısını** kurmaktır: envanter, rol tanımı, risk ve
etki değerlendirmesi, kayıt disiplini, insan gözetimi, tedarikçi yönetimi.
Bu altyapı olmadan yasal uyum iddia edilemez; bu altyapı ile de yasal uyum
otomatik gelmez.

Kullanıcıya bunu **net söyle.** Abartılı uyum iddiası ("42001 aldık, AB YZ
Yasası'na uyumluyuz") hem yanlıştır hem de kullanıcıyı gerçek bir riske sokar.

---

## 1. Kaynak etiketleme disiplini — zorunlu

Bu skill'in ürettiği hiçbir dokümanda **doğrulanmamış hukuki atıf bulunamaz.**
Mevzuata yapılan her atıfı şu üç etiketten biriyle işaretle:

| Etiket | Ne zaman | Örnek |
|---|---|---|
| `[yerleşik]` | Uzun süredir yürürlükte, değişmesi beklenmeyen temel hüküm | KVKK'nın kişisel veri tanımı, ilgili kişinin başvuru hakkı |
| `[teyit]` | Gerçek olduğu bilinen ama güncelliği doğrulanmalı: yönetmelik, kurul kararı, ikincil düzenleme, tebliğ, yürürlük tarihi | Kurul kararları, sektörel tebliğler, geçiş süreleri |
| `[teyit-madde]` | **Madde/fıkra/bent numarası içeren her atıf.** En yüksek hata riski buradadır | "KVKK m.9/6", "AB YZ Yasası Ek III/4" |

`[teyit-madde]` etiketli hiçbir atıf, birincil kaynaktan (Resmî Gazete, AB Resmî
Gazetesi, kurumun kendi yayını) doğrulanmadan nihai dokümanda bırakılmamalıdır.
Madde numaraları mevzuat konsolidasyonlarında kayar; ezberden yazılan madde
numarası denetimde ve hukuki incelemede en hızlı yakalanan hatadır.

**Tarih ve süre ifadelerinde ek kural.** Kullanıcı hukukçu değilse, belirsiz
bir yürürlük tarihini metnin içine yazma. "1 Şubat 2026'da yürürlüğe girer
`[teyit]`" ifadesi, etiketin ne demek olduğunu bilmeyen bir okuyucu için
"1 Şubat 2026'da yürürlüğe girer" demektir. Bunun yerine metinde "yürürlük
tarihi: hukuk biriminden teyit alınacak" yaz ve tüm belirsiz kalemleri
dokümanın sonunda ayrı bir bölümde topla:

> **Dayanağı teyit edilmemiş hususlar — ilerlemeden önce hukuk birimine
> doğrulatın:** [ne yazıldı] · [neyin belirsiz olduğu] · [neden önemli]

---

## 2. Türkiye katmanı — 42001 dokümanlarına nerede değer

### KVKK (Kişisel Verilerin Korunması)

YZ sistemleri kişisel veri işlediğinde 42001 dokümanları KVKK ile şu
noktalarda kesişir. Kesişim, **42001 dokümanının içine gömülmez**; ayrı bir
uyum matrisinde (YZYS-LS-10) izlenir ve 42001 dokümanından ona atıf verilir.

| Kesişim noktası | 42001 tarafı | KVKK tarafı — sorulacak soru |
|---|---|---|
| Eğitim ve besleme verisi | A.7.3 verilerin edinilmesi, A.7.5 veri kökeni | Hukuki dayanak ne? Aydınlatma yapılmış mı? Amaçla bağlantılı, sınırlı ve ölçülü mü? `[yerleşik]` |
| Özel nitelikli veri | A.7.2 veri yönetimi, A.5.4 etki değerlendirmesi | Sağlık, biyometrik, din, üyelik verisi işleniyor mu? Ek şartlar sağlanmış mı? `[teyit-madde]` |
| Bulut/API tabanlı model kullanımı | A.10.3 tedarikçiler, A.10.2 sorumluluk tahsisi | Veri yurt dışına aktarılıyor mu? Aktarım için hangi mekanizma kullanılıyor? `[teyit-madde]` |
| Otomatik karar | A.9.3 insan gözetimi, A.5.4 kişi etkisi | Kişi hakkında **yalnızca otomatik sistemle** karar veriliyor mu? İtiraz ve insan incelemesi yolu var mı? `[teyit-madde]` |
| Envanter ve kayıt | YZYS-LS-04 YZ sistem envanteri | İlgili veri işleme faaliyetleri sicil kaydında yer alıyor mu? `[teyit]` |
| İhlal | A.8.4 olayların iletilmesi | YZ kaynaklı bir olay aynı zamanda veri ihlali mi? Bildirim süresi ve muhatabı ne? `[teyit]` |
| Sorumlu/işleyen ayrımı | **A.10.2 doğrudan ister** | Model sağlayıcısı veri işleyen mi, ayrı sorumlu mu? Sözleşmede tanımlı mı? `[teyit-madde]` |

**A.10.2'nin özel önemi.** Bu kontrol, kişisel veri işlendiğinde sorumlulukların
"ilgili mevzuat uyarınca" veri sorumlusu ve veri işleyen arasında paylaştırılmasını
açıkça ister. Yani KVKK ayrımı 42001'in kendi metnindeki bir gerekliliktir —
opsiyonel bir ek değil. Tedarikçi sözleşmesinde bu ayrım yoksa A.10.2 karşılanmaz.

### Fikri mülkiyet ve ticari sır

| Konu | 42001 tarafı | Sorulacak soru |
|---|---|---|
| Eğitim verisinin telif durumu | A.7.3, A.7.5 veri kökeni | Kazınmış (scraped) veri, lisanssız içerik, telifli materyal var mı? Kullanım izni belgeli mi? |
| Üretilen çıktının mülkiyeti | A.10.4 müşteriler, A.10.3 tedarikçiler | Model çıktısının hakları kime ait? Sözleşmede açık mı? |
| Ticari sırrın modele girmesi | A.9.2 sorumlu kullanım, A.9.4 amaçlanan kullanım | Kaynak kodu, fiyatlandırma, müşteri listesi gibi veriler kurumsal sözleşmesi olmayan bir modele giriyor mu? |
| Meslek sırrı | A.9.2, A.9.4 | Avukat, hekim, mali müşavir gibi sır saklama yükümlüsü meslekler için ek kısıt var mı? |

Bu başlıklar **YZYS-PL-03 Sorumlu Kullanım Politikası**'ndaki yasak kullanım
listesini ve **YZYS-FR-10 Amaçlanan Kullanım Beyanı**'nı doğrudan besler.

### Sektörel katman

Finans, sağlık, kamu, telekom, enerji, sigorta ve kritik altyapıda ek düzenleyici
katman vardır. Bunu **varsayma, sor.** Açılış anketinde "tabi olduğunuz
düzenleyici gereklilikler neler?" sorusu yoksa uyum matrisi eksik doğar.
Sektörün düzenleyicisi YZ kullanımına ilişkin özel bir rehber veya karar
yayımladıysa, bu doğrudan 4.2 (ilgili taraf gereklilikleri) ve A.8.5 (ilgili
taraflara bilgi) kapsamına girer.

---

## 3. AB YZ Yasası katmanı

Kuruluş AB pazarına ürün/hizmet sunuyorsa, AB'de kullanıcısı varsa veya
çıktısı AB'deki kişileri etkiliyorsa bu katman devreye girer. Bunu tespit
etmek için tek soru yeter: **"AB bağlantınız var mı?"**

42001 ile AB YZ Yasası'nın rol taksonomileri **farklı eksenlerdir** ve
birbirine çevrilemez. İkisi ayrı sütunlarda izlenmelidir:

| | 42001 / ISO/IEC 22989 rolü | AB YZ Yasası rolü |
|---|---|---|
| Amaç | Yönetim sistemi kapsamını ve kontrol uygulanabilirliğini belirler | Yasal yükümlülüğün muhatabını belirler |
| Değerler | sağlayıcı · üretici · müşteri · ortak | sağlayıcı · uygulayıcı · ithalatçı · dağıtıcı · yetkili temsilci · ürün imalatçısı `[teyit-madde]` |
| Nerede yazılır | YZYS-LS-04 envanter, kapsam beyanı | YZYS-LS-10 yasal uyum matrisi |

**Risk seviyesi** ayrı bir eksendir ve yine sistem bazındadır: yasaklı ·
yüksek riskli · sınırlı (şeffaflık yükümlülüğü) · asgari; genel amaçlı model
ve sistemik riskli genel amaçlı model ayrı kategorilerdir. `[teyit-madde]`

**Skill'in yapacağı ve yapmayacağı.** Skill, envantere "AB bağlantısı",
"AB YZ Yasası rolü" ve "risk seviyesi" sütunlarını açar ve bu sütunları
`[DOLDURULACAK — hukuk birimince sınıflandırılacak]` bırakır. Skill
**sınıflandırma yapmaz**; sınıflandırmanın hangi eksende yapılacağını
gösterir ve nereye yazılacağını hazırlar. Sınıflandırma hukuki bir karardır
ve madde eşlemesi hızla değişmektedir.

**Kesişimin faydası.** 42001 dokümanlarının çoğu, AB YZ Yasası'nın yüksek
riskli sistemler için beklediği kanıtlarla aynı malzemeyi üretir: risk yönetim
sistemi, veri yönetişimi, teknik dokümantasyon, olay günlükleri, şeffaflık,
insan gözetimi, doğruluk/sağlamlık/güvenlik. **Aynı malzeme, farklı yükümlülük.**
Kullanıcıya söylenecek doğru cümle budur — "42001 bunu kolaylaştırır" doğru,
"42001 bunu karşılar" yanlış.

---

## 4. YZYS-LS-10 Yasal Uyum ve Yükümlülük Matrisi

42001, tabi olunan yasal gerekliliklerin belirlenmesini 4.1/4.2 üzerinden
zaten bekler; A.2.3 ise YZ politikasının diğer kurumsal politikalarla
çelişmemesini ister. Bu iki gereklilik tek bir çıktıda buluşur.

**Zorunlu sütunlar:**

```
Sıra | Düzenleme/Mevzuat | Dayanak (madde/karar) | Kaynak etiketi
[yerleşik/teyit/teyit-madde] | İlgili YZ Sistemi | Yükümlülük özeti |
İlgili 42001 maddesi/kontrolü | Bunu karşılayan doküman | Mevcut durum
(karşılanıyor / kısmen / karşılanmıyor / uygulanabilir değil) | Boşluk tanımı |
Sorumlu | Termin | Doğrulayan (hukuk) | Doğrulama tarihi | Durum
```

**"Doğrulayan (hukuk)" sütunu boş bırakılamaz.** Bu sütun, matrisin bir
hukuki görüş değil, hukukçu tarafından doğrulanmayı bekleyen bir çalışma
belgesi olduğunu görünür kılar. Skill matrisi doldurulmaya hazır ve
sektörden çıkarılmış aday satırlarla üretir; her aday satır
`[ÖRNEK — doğrulanacak]` etiketlidir.

**Matriste yapılmayacaklar:** uydurma madde numarası, uydurma yürürlük tarihi,
"uyumludur" beyanı, ceza/yaptırım tutarı. Bunların hiçbiri skill tarafından
üretilemez.

---

## 5. Tedarikçi ve model sağlayıcı sözleşmesi kontrolü

A.10.3 tedarikçi sözleşmelerinin "kuruluşun sorumlu YZ gerekliliklerini
içermesini" ister. Somutu şudur — **YZYS-PR-12 ve YZYS-LS-06'nın kontrol
listesi budur:**

| Kontrol başlığı | Sorulacak soru | Hedef pozisyon |
|---|---|---|
| **Model eğitimi** | Sağlayıcı, girdilerimizi/çıktılarımızı kendi veya üçüncü taraf modelini eğitmek için kullanabiliyor mu? | Sıfır eğitim hakkı; asgari koşul: etkin ve belgeli çıkış (opt-out) |
| **Veri saklama** | Girdi ve çıktılar ne kadar süre saklanıyor, nerede? | Sıfır/asgari saklama; saklama süresi sözleşmede sayıyla |
| **Girdi/çıktı hakları** | Çıktının mülkiyeti ve kullanım hakkı kime ait? Sağlayıcı çıktıyı başkasına gösterebiliyor mu? | Mülkiyet müşteride, sağlayıcıya gösterme hakkı yok |
| **Alt işleyen / alt sağlayıcı** | Veri hangi alt sağlayıcılara gidiyor? Liste sözleşmede mi, değişiklikte bildirim var mı? | Liste ekte, değişiklikte önceden bildirim ve itiraz hakkı |
| **Konum** | İşleme ve saklama hangi ülkede? | Belirli; değişiklikte bildirim |
| **Fikri mülkiyet tazminatı** | Çıktı üçüncü kişinin hakkını ihlal ederse sorumluluk kimde? | Sağlayıcıda; tazminat taahhüdü yazılı |
| **Performans ve düzeltme** | Sistem beklendiği gibi çalışmazsa düzeltici faaliyet talep hakkımız var mı? | **A.10.3 bunu açıkça ister** — sözleşmede olmalı |
| **Dokümantasyon** | Sağlayıcı model kartı/teknik dokümantasyon veriyor mu? | A.10.3 gereği yeterli ve eksiksiz dokümantasyon |
| **Olay bildirimi** | Sağlayıcı kendi tarafındaki YZ olaylarını bize bildiriyor mu, hangi sürede? | Süre sözleşmede sayıyla; A.8.4 ile bağlanır |
| **Model değişikliği** | Sağlayıcı modeli sürüm yükseltirse haberimiz oluyor mu? | Önceden bildirim — **yeniden değerlendirme tetikleyicisidir** |

Son satır 42001 açısından kritiktir: sağlayıcının sessizce yaptığı bir model
güncellemesi, kuruluşun etki değerlendirmesini geçersiz kılabilir. Bu, hem
A.10.3 hem 8.4 hem de A.6.2.6 ile bağlanan bir zincirdir. Sözleşmede bildirim
yükümlülüğü yoksa `YZYS-FR-03` risk envanterine "sağlayıcı kaynaklı kontrolsüz
model değişikliği" riski girmelidir.

---

## 6. Hukuk birimine devir — nerede durulur

Skill şu durumlarda **durur ve hukuk birimine yönlendirir.** Devam etmek,
hukuki görüş üretmek anlamına gelir ve bu skill'in işi değildir:

- Bir sistemin AB YZ Yasası risk seviyesinin veya rolünün belirlenmesi
- Kişisel veri işlemenin hukuki dayanağının seçilmesi
- Yurt dışına aktarım mekanizmasının belirlenmesi
- Otomatik kararın hukuka uygunluğunun değerlendirilmesi
- Tedarikçi sözleşmesinin redline'ının nihai hâle getirilmesi
- Bir kullanımın yasak olup olmadığı sorusu
- Ceza, yaptırım, idari para cezası tutarları

Bu başlıklarda skill'in üreteceği çıktı **soru listesi ve boş matris satırıdır**,
cevap değil. Kullanıcının kurumunda AI yönetişimi/hukuk eklentisi kuruluysa
(`ai-governance-legal` gibi), somut olarak şu devirleri öner:

| Durum | Devredilecek yer |
|---|---|
| Sistem bazlı AB YZ Yasası rol ve risk seviyesi sınıflandırması | AI envanteri / sınıflandırma akışı |
| Yeni bir kullanım senaryosunun ön triyajı (onay / şartlı / red) | Kullanım senaryosu triyajı |
| Tedarikçi YZ sözleşmesinin madde madde incelenmesi ve redline | Tedarikçi YZ sözleşme incelemesi |
| Yeni bir düzenlemenin mevcut duruma etkisi | Düzenleme boşluk analizi |
| Kişisel veri odaklı ayrı değerlendirme | Mahremiyet etki değerlendirmesi akışı |

Devri **açıkça söyle**: "Bu sınıflandırmayı ben yapmıyorum; matriste yerini
açtım, şu akışa devredilmeli." Sessizce boş bırakmak kullanıcıyı yanıltır.

---

## 7. Kullanıcıya söylenecek cümle

Doküman setinin `OKUBENI.md` dosyasına ve kapsam dokümanının uyum bölümüne
şu ölçüde bir ifade konur:

> Bu doküman seti ISO/IEC 42001:2023 yönetim sistemi gerekliliklerini karşılamak
> üzere hazırlanmıştır. Yasal uyum ayrı bir yükümlülüktür ve bu setle otomatik
> olarak sağlanmaz. Tabi olunan mevzuattan doğan yükümlülükler YZYS-LS-10 Yasal
> Uyum ve Yükümlülük Matrisi'nde izlenir; matristeki her satırın hukuk birimince
> doğrulanması gerekir. Bu sette yer alan mevzuat atıfları doğrulanmamış olup
> `[teyit]` ve `[teyit-madde]` etiketleriyle işaretlenmiştir.

Bu cümle kullanıcıyı korur ve denetçiye olgunluk gösterir. Çıkarma.
