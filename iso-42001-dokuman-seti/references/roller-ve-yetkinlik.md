# Roller, Sorumluluklar ve Yetkinlik

## İçindekiler

- 1. Kuruluşun YZ ekosistemindeki rolü (4.1)
- 2. Kuruluş içindeki YZYS rolleri (5.3, A.3.2)
  - Başlangıç rol matrisi
- 3. RACI iskeleti
- 4. Yetkinlik matrisi (7.2, A.4.6)

Bu dosya iki farklı "rol" kavramını ayırır. Karıştırılması 42001'de en sık
görülen kavramsal hatalardan biridir:

1. **Kuruluşun YZ ekosistemindeki rolü** — 4.1'de belirlenir, sistem bazındadır,
   yükümlülüklerin kapsamını değiştirir.
2. **Kuruluş içindeki YZYS rolleri** — 5.3 ve A.3.2'de belirlenir, kişi/birim
   bazındadır, kimin ne yapacağını söyler.

Denetçi ikisini de sorar ve ikisi de dokümante edilmelidir.

---

## 1. Kuruluşun YZ ekosistemindeki rolü (4.1)

Standardın ve tetkik kontrol listelerinin kullandığı taksonomi ISO/IEC 22989
terminolojisine dayanır. Skill'in eski üçlü ayrımı (geliştirici/sağlayıcı/
kullanıcı) yetersizdir; denetçi bu altılıyı sorar:

| Rol | Ne demek | Tipik örnek | Ağırlık kazanan kontroller |
|---|---|---|---|
| **YZ sağlayıcı** (AI provider) | YZ sistemini/hizmetini başkalarının kullanımına sunar | Kendi modelini API olarak satan şirket | A.6 tamamı, A.8.2, A.8.4, A.10.4 |
| **YZ üreticisi** (AI producer) | YZ sistemini tasarlar, geliştirir, test eder, devreye alır | Kendi modelini geliştiren ekip | A.6.1, A.6.2.2–A.6.2.5, A.7 tamamı |
| **YZ müşterisi** (AI customer) | YZ sistemini kullanır veya kendi müşterisine sunar | Üçüncü taraf LLM API kullanan kurum | A.9 tamamı, A.10.2, A.10.3 |
| **YZ ortağı** (AI partner) | Sağlayıcı/müşteriye destek hizmeti verir (veri sağlayıcı, entegratör, değerlendirici) | Veri etiketleme firması, bağımsız değerlendirici | A.4.3, A.7.3, A.10.2 |
| **YZ süjesi** (AI subject) | Sistemin çıktısına maruz kalan kişi | Kredi başvurusu değerlendirilen kişi | Kuruluş rolü değil — **ilgili taraf**; 4.2 ve A.5.4'te görünür |
| **İlgili otorite** (relevant authority) | Düzenleyici, denetleyici kurum | KVKK, sektör düzenleyicisi | Kuruluş rolü değil — 4.2 ve A.8.5'te görünür |

**Kullanım kuralı.** Son iki satır kuruluşun rolü değildir; ilgili taraf
listesinde yer alır. İlk dördü kuruluşun rolüdür ve **sistem bazında** belirlenir.
Aynı kuruluş bir sistemde üretici, başkasında müşteri olabilir. Envanterde
(YZYS-LS-04) her sistem için ayrı rol sütunu bulunmalı.

**Kapsam beyanında rol.** Kapsam cümlesinde rol belirtmek denetçinin hangi
gereklilikleri arayacağını netleştirir ve gereksiz tartışmayı önler. Yalnızca
müşteri rolündeki kuruluş A.6.1 ve A.6.2.2–A.6.2.4 kontrollerini gerekçeyle
hariç tutabilir; SoA'da gerekçe yazılmalıdır.

**Rol değişimi tetikleyicisi.** Kuruluş üçüncü taraf bir modeli önemli ölçüde
değiştirirse (kendi verisiyle ince ayar, amaçlanan kullanımın değiştirilmesi,
kendi markası altında sunma) **müşteri rolünden üretici/sağlayıcı rolüne**
geçebilir ve o ana kadar hariç tuttuğu kontroller uygulanabilir hâle gelir.
Bu, hem 42001 hem de AB YZ Yasası açısından aynı yönde çalışan bir eşiktir
(bkz. `mevzuat-kesisimi.md`). Envanterde "önemli değişiklik yapıldı mı?"
sütunu bu tetikleyiciyi görünür kılar.

---

## 2. Kuruluş içindeki YZYS rolleri (5.3, A.3.2)

A.3.2 rol ve sorumlulukların şu alanları kapsamasını ister — denetçi tek tek
sorar, bir tanesi bile sahipsizse bulgu gelir:

> risk yönetimi · mahremiyet · güvenlik · emniyet · YZ sistemi etki
> değerlendirmesi · performans · **insan gözetimi** · tedarikçi ilişkileri ·
> uyum · veri kalitesi yönetimi

Küçük kuruluşta bir kişi birden çok alandan sorumlu olabilir; sorun değil.
Sorun, hiçbir alanın **isimsiz** kalmasıdır.

### Başlangıç rol matrisi

Aşağıdaki tablo YZYS-EK-01 §Roller bölümünün ve A.3.2 kanıtının iskeletidir.
Kuruluşun ölçeğine göre birleştirilir — 12 kişilik şirkete 20 rol yazmak
denetimde "yaşamayan sistem" bulgusu üretir. Unvanlar `[DOLDURULACAK]`
bırakılabilir ama **sorumluluk alanı boş kalamaz**.

#### Yönetişim

| Rol | Temel sorumluluklar | İlgili madde/kontrol |
|---|---|---|
| Üst Yönetim Sponsoru / YZ Sorumlusu | YZYS'nin genel hesap verebilirliği, stratejik önceliklerin belirlenmesi, kaynak ve bütçe onayı | 5.1, 5.3, 7.1 |
| YZ Yönetişim ve Uyum Sorumlusu | 42001 uygulamasının koordinasyonu, mevzuat uyumunun izlenmesi, politika ve prosedür geliştirme, düzenleyici raporlama | 4.1, 4.2, 9.2, A.2.4 |
| YZ Etik Sorumlusu | Etik ilkelerin sürece gömülmesi, adillik ve hesap verebilirlik değerlendirmesi, etik ikilemlerin çözümü | 5.2, 6.2, A.5.4 |
| Hukuk ve Politika Danışmanı | Sözleşme yönetimi, düzenleyici gerekliliklerin takibi, hukuki risk değerlendirmesi, fikri mülkiyet | 4.2, 8.2, A.10.2 |
| İlgili Taraf İletişimi Sorumlusu | Paydaş diyaloğu, şeffaflık ve iletişim stratejisi, geri bildirim mekanizmalarının işletilmesi | 7.4, 9.3, A.8.5 |

#### Veri

| Rol | Temel sorumluluklar | İlgili madde/kontrol |
|---|---|---|
| Veri Mühendisi / Veri Sahibi | Veri hattı tasarımı ve yönetimi, veri kalitesi, veri güvenliği ve erişim kontrolü, veri dokümantasyonu | 7.5, 8.3, A.7.2–A.7.6 |
| Veri Bilimci / ML Mühendisi | Model geliştirme ve eğitim, model değerlendirme ve optimizasyon, öznitelik mühendisliği, performans metriklerinin tanımlanması | 6.3, 8.4, A.6.2.3 |
| Veri Sağlayıcı (iç/dış) | Veri setlerinin sağlanması, lisans ve kullanım hakları yönetimi, veri güncellemeleri, veri kalite güvence belgeleri | 7.5.2, A.4.3, A.7.3 |
| Çeşitlilik ve Kapsayıcılık Danışmanı | Veri setlerinde yanlılık analizi, temsil ve adillik değerlendirmesi, erişilebilirlik doğrulaması | A.5.4, A.7.4 |

#### Tasarım ve Mühendislik

| Rol | Temel sorumluluklar | İlgili madde/kontrol |
|---|---|---|
| Ürün Yöneticisi / YZ Tasarımcısı | Amaç ve kapsamın tanımlanması, kullanıcı ve paydaş gerekliliklerinin belirlenmesi, başarı kriterleri | 6.3, 8.1, A.6.2.2 |
| YZ Mühendisi | Model entegrasyonu, YZ bileşenlerinin geliştirilmesi, sistem optimizasyonu, teknik dokümantasyon | 8.1, A.6.2.3, A.6.2.7 |
| Alan Uzmanı | Sektöre özgü gerekliliklerin tanımlanması, risk değerlendirmesine katkı, kullanım senaryolarının doğrulanması | 6.2, 8.2, A.6.2.2 |
| Kullanıcı Deneyimi / İnsan Faktörleri Uzmanı | **İnsan gözetimi mekanizmalarının tasarımı**, açıklanabilirlik arayüzleri, geri bildirim ve itiraz süreçleri | A.5.4, A.8.2, A.9.3 |
| Sistem ve Yazılım Mühendisi | Teknik mimari tasarımı, API ve entegrasyon geliştirme, ölçeklenebilirlik, altyapı yönetimi | 7.1, A.4.4, A.4.5 |
| Siber Güvenlik ve Mahremiyet Sorumlusu | Tasarımdan güvenlik ve mahremiyet, tehdit modellemesi, YZ'ye özgü saldırılara karşı kontroller | A.6.2.6, A.7.2 |

#### Devreye Alma ve İşletim

| Rol | Temel sorumluluklar | İlgili madde/kontrol |
|---|---|---|
| YZ Operatörü / MLOps Mühendisi | Üretim sistemlerinin yönetimi, model devreye alma ve güncelleme, sistem sağlığı izleme | 8.1, A.6.2.5, A.6.2.6 |
| İzleme Sorumlusu | Gerçek zamanlı performans takibi, **model kayması (drift) tespiti**, uyarı sisteminin yönetimi | 9.1, A.6.2.6 |
| Dayanıklılık ve Olay Sorumlusu | Olay müdahale süreçleri, amaç dışı kullanım senaryolarına hazırlık, kurtarma koordinasyonu | 10.2, A.8.4 |
| Tedarik ve Tedarikçi İlişkileri Sorumlusu | Sorumlu tedarik yönetimi, tedarikçi değerlendirme ve denetimi, sözleşme yönetimi | A.10.2, A.10.3 |
| Eğitim ve Farkındalık Sorumlusu | YZ okuryazarlığı programları, çalışan farkındalık eğitimi, eğitim materyali geliştirme | 7.2, 7.3, A.4.6 |

#### Tetkik ve İzleme

| Rol | Temel sorumluluklar | İlgili madde/kontrol |
|---|---|---|
| YZ Değerlendirici / Test Uzmanı (TEVV) | Test, doğrulama ve geçerleme, **yanlılık ve adillik testi**, performans değerlendirmesi | A.6.2.4 |
| İç Tetkikçi (YZYS tetkikçisi) | İç tetkiklerin yürütülmesi, hazırlık düzeyi değerlendirmesi, tetkik raporlarının hazırlanması | 9.2 |
| Doküman ve Kayıt Yöneticisi | Kayıt yönetim sistemi, tasarım kararlarının dokümantasyonu, denetim izlerinin sürdürülmesi | 7.5 |
| Sürekli İyileştirme Sorumlusu | Öğrenilen derslerin analizi, düzeltici faaliyetlerin yönetimi, sistem güncellemelerinin koordinasyonu | 10.1, 10.2 |

**Bağımsızlık kuralı (9.2).** İç tetkikçi ve YZ Değerlendirici, denetledikleri
faaliyetten operasyonel olarak bağımsız olmalıdır. Modeli geliştiren kişi o
modelin iç tetkikini yapamaz. Küçük kuruluşta çözüm: çapraz tetkik veya dış
kaynak. Denetçi bunu doğrudan sorar.

---

## 3. RACI iskeleti

Aşağıdaki tablo YZYS-EK-01 ekine konur. Hücreleri kuruluş doldurur;
**her satırda tam olarak bir `A` (hesap veren) bulunmalıdır** — birden fazla
`A` sorumluluk boşluğu demektir.

| Faaliyet | Üst Yönetim Sponsoru | Yönetişim Sorumlusu | Veri Sahibi | YZ Mühendisi | MLOps | İç Tetkikçi | Etik Sorumlusu |
|---|---|---|---|---|---|---|---|
| YZ politikasının geliştirilmesi | A | R | C | C | I | I | C |
| YZ risk değerlendirmesi | A | R | C | C | C | I | C |
| **YZ sistemi etki değerlendirmesi** | A | R | C | C | I | I | **R** |
| Veri kalitesi yönetimi | I | C | **A/R** | C | I | I | C |
| Devreye alma ve işletim | I | I | C | R | **A/R** | I | I |
| Performans ve adillik izleme | I | C | C | R | R | I | C |
| İç tetkik | A | C | I | I | I | **R** | I |
| Olay müdahalesi | A | R | C | R | R | I | C |
| Sürekli iyileştirme | A | R | C | C | C | C | C |

`R` = yürüten · `A` = hesap veren · `C` = danışılan · `I` = bilgilendirilen

---

## 4. Yetkinlik matrisi (7.2, A.4.6)

42001'de yetkinlik **yalnızca teknik değildir**. Etki değerlendirmesi yapacak
kişinin etik, hukuk ve alan bilgisine de ihtiyacı vardır. Yetkinlik matrisi
(YZYS-LS-07) dört boyutu ayırmalı:

| Boyut | Ne kapsar | Kanıt tipi |
|---|---|---|
| **Teknik** | Model geliştirme, MLOps, veri mühendisliği, test metodolojisi | Diploma, sertifika, proje geçmişi |
| **Etik** | Adillik kavramları, yanlılık türleri, insan gözetimi tasarımı | Eğitim kaydı, vaka çalışması |
| **Hukuki** | KVKK, sektörel mevzuat, sözleşme, fikri mülkiyet | Eğitim kaydı, mesleki yeterlilik |
| **Alan** | Sektöre özgü süreç bilgisi (kredi, sağlık, İK, sigorta...) | Deneyim, iç sertifikasyon |

A.4.6 ayrıca **yaşam döngüsü aşaması bazında** yetkinlik eşlemesi ister:
geliştirme, devreye alma, işletim, değişiklik yönetimi, bakım, transfer,
hizmetten çıkarma, doğrulama ve entegrasyon aşamalarının her biri farklı
yetkinlik gerektirir. Matriste satır = kişi/rol, sütun = aşama olacak şekilde
kurmak bu gerekliliği doğrudan karşılar.

**Etkinlik değerlendirmesi (7.2).** Yetkinlik kazandırmak yetmez; alınan
önlemin **etkinliği değerlendirilmelidir**. Eğitim katılım listesi tek başına
kanıt değildir — eğitim sonrası değerlendirme, uygulama gözlemi veya
performans göstergesi gerekir. Denetçinin sık bulduğu açık budur.
