# Olay ve bildirim zinciri · YZ okuryazarlığı

## İçindekiler

- 1. Olay ve bildirim zinciri
  - 1a. Tek giriş, çok çıkış
  - 1b. Kollar — dokümana girecek çerçeve
  - 1c. Olay kaydına eklenecek alanlar
  - 1d. Eklenti ile bağ
- 2. YZ okuryazarlığı ve yetkinlik
  - 2a. İki kaynak, bir kayıt
  - 2b. Matrise eklenecek sütunlar
  - 2c. Kalite çıtası
İki konu da aynı hatayla eksik kalır: 42001 dokümanı yazılır ama yasal
yükümlülükle bağı kurulmaz. Olay prosedürü "olay kaydedilir" der, KVKK veya AB
YZ Yasası bildirim saatinin işlemeye başladığını söylemez. Eğitim matrisi
"YZ farkındalık eğitimi verilir" der, AB YZ Yasası okuryazarlık yükümlülüğünün
kanıtını üretmez. Bu bölüm o bağları kurar.

Bu bölümdeki **hiçbir süre ve madde numarası nihai değildir.** Hepsi
`[teyit]`/`[teyit-madde]` etiketiyle dokümana girer; hangi bildirimin
yapılacağına hukuk birimi karar verir. Skill akışı ve kayıt alanlarını kurar.

## 1. Olay ve bildirim zinciri

### 1a. Tek giriş, çok çıkış

YZ ile ilgili bir olay tek bir kapıdan girer (YZYS olay formu) ve sınıflandırma
anında **birden fazla saat** işlemeye başlayabilir. Prosedür bunu açıkça
göstermeli:

```
Olay tespiti (izleme, kullanıcı şikâyeti, endişe bildirimi A.3.3, tedarikçi bildirimi)
   │
   ▼
YZYS olay kaydı açılır — tespit zamanı DAKİKA hassasiyetinde kaydedilir
   │
   ▼
İlk sınıflandırma (olay sorumlusu, en geç [DOLDURULACAK] saat içinde)
   ├─ Kişisel veri ihlali var mı?                 → KVKK bildirim kolu
   ├─ Sistem AB YZ Yasası kapsamında yüksek riskli mi ve
   │  ciddi olay tanımına giriyor mu?               → AB YZ Yasası kolu
   ├─ Siber olay mı?                              → Siber güvenlik kolu
   ├─ Sektörel düzenleyiciye bildirim var mı?      → Sektörel kol (BDDK, SPK, EPDK, Sağlık…)
   ├─ Tedarikçinin modeli mi kaynaklı?             → Tedarikçi kolu (sözleşmedeki bildirim maddesi)
   └─ Etkilenen kişilere/ilgili taraflara bildirim (A.8.4)
   │
   ▼
Her kol için: karar veren, karar zamanı, bildirildi/bildirilmedi + gerekçe
   │
   ▼
Kök neden → DÖF (10.2) → risk kaydı ve etki değerlendirmesi güncellemesi
```

### 1b. Kollar — dokümana girecek çerçeve

| Kol | Bilinen çerçeve | Etiket | Kim karar verir |
|---|---|---|---|
| KVKK veri ihlali | Veri sorumlusu ihlali Kurul'a ve ilgili kişilere en kısa sürede bildirir; Kurul kararıyla bu süre Kurul'a bildirim için 72 saat olarak yorumlanmıştır | `[teyit-madde]` (KVKK m.12/5 ve ilgili Kurul kararı) | Veri sorumlusu / KVKK irtibat kişisi + hukuk |
| AB YZ Yasası ciddi olay | Yüksek riskli YZ sistemi **sağlayıcıları** ciddi olayları piyasa gözetim otoritesine bildirir; olayın türüne göre farklı ve kısa süreler vardır. Uygulayıcı (deployer) ciddi olayı tespit ederse sağlayıcıyı ve ilgili otoriteyi bilgilendirir | `[teyit-madde]` (sağlayıcı bildirimi ve uygulayıcı yükümlülükleri ile ilgili maddeler); yüksek risk yükümlülüklerinin uygulama tarihleri Digital Omnibus ile ertelendi — Ek E4 | Hukuk birimi; sistem sahibi bilgi sağlar |
| Genel amaçlı YZ modeli (sistemik risk) | Sistemik riskli model sağlayıcılarının ciddi olay takibi ve raporlama yükümlülüğü | `[teyit-madde]` | Yalnız kuruluş bu sıfatta ise |
| Siber güvenlik | 7545 sayılı Siber Güvenlik Kanunu ve ikincil düzenlemeler kapsamında bildirim yükümlülükleri olabilir | `[teyit]` | Bilgi güvenliği + hukuk |
| Sektörel | Bankacılık, sermaye piyasası, sağlık, enerji, elektronik haberleşmede ayrı bildirim kuralları | `[teyit]` | Uyum birimi |
| Tedarikçi | Sözleşmedeki olay bildirim süresi ve kapsamı | `vendor-ai-review` çıktısından | Tedarikçi ilişki sahibi |

Skill bu tabloyu olay prosedürüne **boş karar sütunlarıyla** koyar; süreleri
dokümanın gövdesine kesin hüküm olarak yazmaz. Kullanıcı hukukçu değilse
süre yerine "bildirim süresi: hukuk biriminden teyit alınacak" yazılır.

### 1c. Olay kaydına eklenecek alanlar

YZYS-FR-12 olay kaydında bu alanlar bulunmalı (betik sürümü bunları üretmiyorsa ekle):

- Tespit zamanı (tarih + saat:dakika) — bildirim süreleri buradan başlar
- İlgili YZ sistemi (Sistem No — envanterle eşleşir)
- Kişisel veri etkilendi mi (Evet/Hayır/Belirsiz) → KVKK kolu tetikleyicisi
- AB YZ Yasası risk seviyesi (envanterden; boşsa "sınıflandırılmamış" — bu
  kendi başına bir bulgudur)
- Her bildirim kolu için: değerlendirildi mi / karar / karar veren / zaman /
  bildirim referansı
- Etkilenen kişilere bildirim (A.8.4) yapıldı mı, nasıl
- Etki değerlendirmesi yeniden açıldı mı (Evet + kayıt no / Hayır + gerekçe)

### 1d. Eklenti ile bağ

- Olay hukuki değerlendirme gerektiriyorsa eklentinin eskalasyon tablosu
  (`## Governance team and escalation` → "Vendor AI incident", "Regulator
  inquiry") kimin devreye gireceğini söyler; olay prosedüründeki eskalasyon
  adımı bu tabloyla tutarlı olmalı.
- Düzenleyici sorgusu ("Regulator inquiry") eklenti profiline göre her zaman
  hukuk birimine anında eskalasyondur; prosedür bunu tekrarlar.
- Olay sonrası politika boşluğu varsa `policy-monitor` doğrudan sorgu modunda
  çalıştırılır.

## 2. YZ okuryazarlığı ve yetkinlik

### 2a. İki kaynak, bir kayıt

| Kaynak | Ne ister |
|---|---|
| 42001 7.2 | YZYS'yi etkileyen işleri yapan kişilerin yetkinliğinin belirlenmesi, sağlanması, etkinliğinin değerlendirilmesi ve **kanıt olarak saklanması** |
| 42001 7.3 | Farkındalık: YZ politikası, kişinin katkısı, uygunsuzluğun sonuçları |
| 42001 A.4.6 | YZ sistemlerinde çalışan insan kaynaklarının yetkinliği |
| AB YZ Yasası okuryazarlık hükmü | Sağlayıcı ve uygulayıcıların, çalışanları ve kendi adlarına YZ sistemleriyle uğraşan kişiler için yeterli YZ okuryazarlığını destekleyecek önlemler alması. Digital Omnibus sonrası yükümlülük sürüyor; ancak her bireyin belirli bir yetkinlik düzeyine ulaştığını **garanti etme** beklentisi kaldırıldı `[teyit]` — Ek E4 |

AB bağlantısı olan kuruluşta tek bir **Yetkinlik ve YZ Okuryazarlığı Matrisi**
(YZYS-LS-07 genişletilmiş) iki yükümlülüğün kanıtını birlikte üretir. Ayrı
eğitim sistemi kurma.

### 2b. Matrise eklenecek sütunlar

YZYS-LS-07 matrisinde bu sütunlar bulunmalı (betik sürümü bunları üretmiyorsa ekle):

- **Kişi grubu** — YZ sistemi kullanıcısı / sistem sahibi / geliştirici /
  insan gözetimi yapan / üst yönetim / kendi adına çalışan dış kişi
  (yüklenici, danışman)
- **İlgili YZ sistemleri** (Sistem No)
- **Rol bazlı okuryazarlık hedefi** — ör. gözetim yapan için "çıktıyı
  sorgulama, otomasyon yanlılığını tanıma, müdahale eşiğini bilme"
- **Bağlam faktörleri** — kişinin teknik bilgisi, deneyimi, eğitimi ve
  sistemin kullanılacağı bağlam ile etkilenecek kişiler (okuryazarlık
  önlemlerinin bu faktörlere göre ölçeklenmesi beklenir `[teyit]`)
- **Önlem** — eğitim, rehber, sistem içi uyarı, uygulamalı oturum
- **Kanıt** — katılım kaydı, değerlendirme, tarih
- **Tekrar sıklığı** ve **tetikleyici** (yeni sistem, önemli değişiklik)

### 2c. Kalite çıtası

- "Tüm personele YZ farkındalık eğitimi verilir" tek başına yetersizdir: kişi
  grubu ve sisteme bağlanmamıştır, etkinliği ölçülmez.
- **İnsan gözetimi yapan kişilerin eğitimi ayrı satırdır.** Gözetimin
  etkinliği (müdahale oranı) bu eğitimin etkinlik göstergesidir — 9.1 ile bağ.
- Dış kişiler (yüklenici, danışman, iş ortağı) okuryazarlık kapsamındadır;
  matriste yoksa denetimde sorulur.
- Eğitim içeriği YZ politikasındaki yasaklı kullanımları ve endişe bildirim
  kanalını (A.3.3) içermelidir — 7.3 farkındalık kanıtı.
