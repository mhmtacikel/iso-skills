# ISO/IEC 42001:2023 Ek A — Referans Kontrol Hedefleri ve Kontrolleri

Uygulanabilirlik Bildirgesi bu tablodan üretilir. `Doküman` sütunu skill'in
ürettiği dosyalara, `Kanıt` sütunu denetçinin sahada isteyeceği uygulama kanıtına
işaret eder. Ek B, her kontrol için uygulama kılavuzu sağlar; Ek C potansiyel
YZ risk kaynaklarını, Ek D sektörel kullanımı içerir (ikisi bilgi amaçlıdır).

> **Kontrol başlığı ≠ kontrol gerekliliği.** Her kontrolün altında denetçinin tek
> tek sorduğu 2–7 alt gereklilik vardır. Aşağıdaki tablolar başlık seviyesindedir;
> **alt gereklilik listesi `assets/denetim_sorulari_42001.json` dosyasındadır**
> (38 kontrol, 128 soru). SoA'da bir kontrolü "uygulanıyor" işaretlemeden önce
> o kontrolün alt gerekliliklerinin hepsinin karşılandığını doğrula. En sık
> kaçırılan alt gereklilikler bu dosyanın sonundaki §"Sık kaçırılan alt
> gereklilikler" bölümündedir.

**Hariç tutma:** Ek A kontrolleri gerekçelendirilerek hariç tutulabilir; Madde 4–10
hariç tutulamaz. Hariç tutma gerekçesi hem 'neden uygulanabilir değil' hem de
'ilgili risk başka hangi kontrolle karşılanıyor' sorusunu yanıtlamalıdır.


## A.2 — YZ ile ilgili politikalar

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.2.2 | YZ politikası | YZYS-PL-01 YZ Politikası | Onaylı politika, duyuru kaydı, üst yönetim taahhüdü |
| A.2.3 | Diğer kurumsal politikalar ile uyum | YZYS-PL-01 §Uyum, YZYS-LS-08 Politika Uyum Matrisi | Bilgi güvenliği, KVKK, kalite politikalarıyla çelişki analizi |
| A.2.4 | YZ politikasının gözden geçirilmesi | YZYS-PL-01 §Gözden Geçirme | Yıllık gözden geçirme tutanağı, revizyon kaydı |

## A.3 — İç organizasyon

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.3.2 | YZ rolleri ve sorumlulukları | YZYS-EK-01 §Roller, YZYS-FR-01 Görev Tanımları | Organizasyon şeması, YZ sorumlusu ataması, RACI matrisi |
| A.3.3 | Endişelerin raporlanması | YZYS-PR-09 Endişe Bildirim Prosedürü | Bildirim kanalı kanıtı, gelen bildirim kayıtları, gizlilik güvencesi |

## A.4 — YZ sistemleri için kaynaklar

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.4.2 | Kaynak dokümantasyonu | YZYS-LS-02 YZ Kaynak Envanteri | Yaşam döngüsü aşaması bazında kaynak dokümantasyonu |
| A.4.3 | Veri kaynakları | YZYS-LS-03 Veri Kaynakları Envanteri | Veri seti listesi, kaynak, izin/lisans durumu |
| A.4.4 | Araç ve donanım kaynakları | YZYS-LS-02 §Araç ve Donanım | Kullanılan çerçeve, kütüphane, GPU/hesaplama kaynağı listesi |
| A.4.5 | Sistem ve bilgi işlem kaynakları | YZYS-LS-02 §Sistem ve Bilgi İşlem | Eğitim/çıkarım altyapısı, kapasite kayıtları |
| A.4.6 | İnsan kaynakları | YZYS-LS-07 Yetkinlik Matrisi | YZ yetkinlik gereksinimleri, eğitim kayıtları |

## A.5 — YZ sistemlerinin etkilerinin değerlendirilmesi

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.5.2 | YZ sistemi etki değerlendirme süreci | YZYS-PR-02 Etki Değerlendirme Prosedürü | Metodoloji dokümanı, uygulanmış değerlendirme örnekleri |
| A.5.3 | YZ sistemi etki değerlendirmelerinin dokümantasyonu | YZYS-FR-04 YZ Sistemi Etki Değerlendirmesi | Tamamlanmış ve onaylanmış etki değerlendirme kayıtları |
| A.5.4 | YZ sisteminin kişiler veya kişi grupları üzerindeki etkisinin değerlendirilmesi | YZYS-FR-04 §Kişi/Grup Etkisi | Etkilenen gruplar analizi, adillik ve ayrımcılık değerlendirmesi |
| A.5.5 | YZ sistemlerinin toplumsal etkilerinin değerlendirilmesi | YZYS-FR-04 §Toplumsal Etki | Çevresel, ekonomik ve toplumsal etki değerlendirmesi |

## A.6 — YZ sistemi yaşam döngüsü

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| **A.6.1** | *YZ sistem geliştirme için yönetim rehberliği* (alt grup) | | |
| A.6.1.2 | YZ sisteminin sorumlu geliştirilmesi için hedefler | YZYS-PL-02 Sorumlu YZ Geliştirme Hedefleri | Adillik, şeffaflık, güvenlik, açıklanabilirlik hedefleri ve ölçümleri |
| A.6.1.3 | YZ sorumlu sistem tasarımı ve geliştirme süreçleri | YZYS-PR-03 Sorumlu Tasarım ve Geliştirme Prosedürü | Tasarım gözden geçirme kayıtları, etik kontrol noktaları |
| **A.6.2** | *YZ sistem yaşam döngüsü* (alt grup) | | |
| A.6.2.2 | YZ sistem gereklilikleri ve özellikleri | YZYS-FR-05 YZ Sistem Gereksinim Formu | Fonksiyonel ve fonksiyonel olmayan gereksinimler, kabul kriterleri |
| A.6.2.3 | YZ sistem tasarımı ve geliştirmesinin dokümantasyonu | YZYS-FR-06 Tasarım ve Geliştirme Dokümantasyonu | Mimari, model seçim gerekçesi, hiperparametre kayıtları |
| A.6.2.4 | YZ sistem doğrulaması ve geçerliliği | YZYS-PR-04 Doğrulama ve Geçerleme Prosedürü | Test planı, performans metrikleri, yanlılık testi sonuçları |
| A.6.2.5 | YZ sisteminin devreye alınması | YZYS-PR-05 Devreye Alma Prosedürü | Dağıtım planı, kabul onayı, geri alma planı |
| A.6.2.6 | YZ sistemi işletimi ve izlenmesi | YZYS-PR-06 İşletim ve İzleme Prosedürü | İzleme metrikleri, model kayması (drift) takibi, uyarı kayıtları |
| A.6.2.7 | YZ sistemi teknik dokümantasyonu | YZYS-FR-07 Teknik Dokümantasyon / Model Kartı | Model kartı, sistem kartı, ilgili taraflara sunulan teknik doküman |
| A.6.2.8 | YZ sistemi olay günlüklerinin kaydı | YZYS-PR-06 §Olay Günlükleri | Hangi aşamada hangi log, saklama süresi, erişim kontrolü |

## A.7 — YZ sistemleri için veriler

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.7.2 | YZ sisteminin geliştirilmesi ve iyileştirilmesi için veriler | YZYS-PR-07 Veri Yönetişimi Prosedürü | Veri yönetimi yaklaşımı, sorumluluklar |
| A.7.3 | Verilerin edinilmesi | YZYS-LS-03 §Edinme | Veri edinme kayıtları, lisans/izin belgeleri, sözleşmeler |
| A.7.4 | YZ sistemleri için verilerin kalitesi | YZYS-FR-08 Veri Kalitesi Değerlendirme Formu | Kalite kriterleri, ölçüm sonuçları, temsil edicilik analizi |
| A.7.5 | Veri kökeni | YZYS-LS-03 §Köken | Veri kökeni (provenance) kayıtları, dönüşüm izleri |
| A.7.6 | Veri hazırlama | YZYS-PR-07 §Hazırlama | Ön işleme adımları, etiketleme prosedürü, etiketleyici talimatları |

## A.8 — YZ sistemlerinin ilgili tarafları için bilgiler

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.8.2 | Kullanıcılar için sistem dokümantasyonu ve bilgileri | YZYS-FR-09 Kullanıcı Dokümantasyonu | Kullanım kılavuzu, sınırlılıklar beyanı, uyarılar |
| A.8.3 | Harici raporlama | YZYS-PR-08 Şeffaflık ve Raporlama Prosedürü | Dış bildirim kanalı, olumsuz etki bildirim mekanizması |
| A.8.4 | Olayların iletilmesi | YZYS-PR-10 YZ Olay Yönetimi Prosedürü | Kullanıcıya olay bildirim kayıtları, bildirim şablonları |
| A.8.5 | İlgili taraflar için bilgiler | YZYS-PR-08 §İlgili Taraflar | İlgili taraf bilgilendirme kayıtları, şeffaflık beyanları |

## A.9 — YZ sistemlerinin kullanımı

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.9.2 | YZ sistemlerinin sorumlu kullanılmasına yönelik süreçler | YZYS-PR-11 Sorumlu Kullanım Prosedürü | Kullanım kuralları, kullanıcı eğitimi, izleme kayıtları |
| A.9.3 | YZ sisteminin sorumlu kullanılmasına yönelik hedefler | YZYS-PL-03 Sorumlu Kullanım Hedefleri | Kullanım ilkeleri, insan gözetimi tanımı |
| A.9.4 | YZ sisteminin amaçlanan kullanımı | YZYS-FR-10 Amaçlanan Kullanım Beyanı | Amaçlanan kullanım, amaç dışı/yasak kullanım listesi, sapma izleme |

## A.10 — Üçüncü taraf ve müşteri ilişkileri

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.10.2 | Sorumlulukların tahsisi | YZYS-PR-12 Üçüncü Taraf Yönetimi Prosedürü | Yaşam döngüsü boyunca sorumluluk paylaşım matrisi |
| A.10.3 | Tedarikçiler | YZYS-LS-06 Tedarikçi ve Model Sağlayıcı Envanteri | Sağlayıcı değerlendirmesi, sözleşme YZ ekleri |
| A.10.4 | Müşteriler | YZYS-FR-11 Müşteri Bilgilendirme ve Yükümlülük Formu | Müşteriye sunulan bilgi, sorumluluk sınırları, geri bildirim kanalı |

---

## Sık kaçırılan alt gereklilikler

Aşağıdakiler, kontrol başlığı "yapıldı" görünürken denetimde bulgu üreten
maddelerdir. Doküman üretirken her birinin karşılığını açıkça yaz.

| Kontrol | Kaçırılan alt gereklilik | Nerede karşılanır |
|---|---|---|
| A.2.2 | Politikanın **istisna ve sapmaların ele alınmasına ilişkin süreci** dokümante etmesi | YZYS-PL-01 §İstisna Yönetimi |
| A.2.4 | Politikanın geliştirilmesi, gözden geçirilmesi ve değerlendirilmesinden **sorumlu bir rolün atanmış olması** | YZYS-PL-01 §Gözden Geçirme + rol matrisi |
| A.3.2 | Rol listesinin **on alanı birden** kapsaması: risk, mahremiyet, güvenlik, emniyet, etki değerlendirmesi, performans, insan gözetimi, tedarikçi, uyum, veri kalitesi | `roller-ve-yetkinlik.md` §2 |
| A.3.3 | Gizlilik/anonimlik · **eskalasyon mekanizması** · **misillemeden koruma** · bildirene **durum geri bildirimi** · kanalın **yetkin kişilerce yönetilmesi** | YZYS-PR-09 — beşi de ayrı bölüm |
| A.4.3 | **Merkezi veri envanteri** · eğitim/doğrulama/test/üretim **kategorizasyonu** · **etiketleme** · **saklama ve imha politikası** | YZYS-LS-03 + YZYS-PR-07 |
| A.4.4 | Kullanılan **makine öğrenmesi model tiplerinin** dokümante edilmesi; veri hazırlama araçlarının ayrıca sayılması | YZYS-LS-02 |
| A.4.5 | Donanımın **maliyet ve çevresel etkisinin nicelendirilmesi**; gelecekteki kaynak ihtiyacı projeksiyonu | YZYS-LS-02 §Hesaplama — 4.1 iklim ve A.5.5 ile bağlanır |
| A.4.6 | Yetkinliğin **yaşam döngüsü aşaması bazında** eşlenmesi (geliştirme, devreye alma, işletim, değişiklik, bakım, transfer, hizmetten çıkarma, doğrulama, entegrasyon) | YZYS-LS-07 |
| A.5.2 | Etki değerlendirmesinin **hangi koşullarda** yapılacağının ve **hangi unsurları içereceğinin** belirlenmiş olması | YZYS-PR-02 §Tetikleyiciler |
| A.5.3 | **Olumlu etkiler** · **öngörülebilir hatalar** · **demografik gruplar** · **sistem karmaşıklığı** · **istihdam ve beceri etkisi** · **saklama süresi** | `etki-degerlendirmesi.md` §3 |
| A.5.4 | **Erişilebilirlik** ve **insan hakları** alanlarının ayrı değerlendirilmesi | YZYS-FR-04 §3a |
| A.5.5 | **Yönetişim** alanının (yasama, siyasi yanlış bilgi, ulusal güvenlik, ceza adaleti) ele alınması veya gerekçeyle "uygulanabilir değil" denmesi | YZYS-FR-04 §3e |
| A.6.1.3 | Süreçlerin **yayın (release) kriterleri, onay ve imzalar, değişiklik kontrolü ve ilgili taraf katılımını** içermesi | YZYS-PR-03 |
| A.6.2.4 | Test verisinin **kullanım alanı için temsil ediciliği**; **kişiler ve toplumlar üzerindeki etkilere yönelik ayrı değerlendirme planı**; kullanım kriterleri ve bunlara göre değerlendirme | YZYS-PR-04 |
| A.6.2.5 | Bileşenlerin **birlikte mi bağımsız mı** devreye alınacağı; **kullanıcı test gereklilikleri**; **onay ve imzalar** | YZYS-PR-05 |
| A.6.2.6 | **Onarım süreci** · **güncelleme süreci** · **kullanıcı desteği** · **veri zehirlenmesi, model çalma, model tersine çevirme** saldırılarına karşı kontroller | YZYS-PR-06 — dördü de ayrı bölüm |
| A.6.2.7 | Teknik dokümantasyonun **her ilgili taraf kategorisi için ayrı** belirlenmesi ve **o tarafın ihtiyacına uygun formatta** sunulması | YZYS-FR-07 — tek bir model kartı yetmeyebilir |
| A.6.2.8 | Günlüklerin **amaçlanan performans aralığı dışına çıkışı tespit etmeye imkân vermesi** · **saklama süresi** · **günlüklerin korunması** | YZYS-PR-06 §Olay Günlükleri |
| A.7.2 | Veri tarafında **şeffaflık ve açıklanabilirlik önlemleri**; **doğruluk ve bütünlüğün korunması**; eğitim verisinin **temsil ediciliği** | YZYS-PR-07 |
| A.7.5 | Köken kaydının **oluşturma, güncelleme, aktarım, soyutlama, doğrulama ve kontrolün devri** adımlarını içermesi | YZYS-LS-03 §Köken |
| A.8.2 | Kullanıcıya verilen bilginin **eksiksiz, güncel ve doğru olduğunun doğrulanması** | YZYS-FR-09 |
| A.8.3 | Bildirimlerin **kayda geçirilmesi, kategorize edilmesi, gözden geçirilmesi** ve gerektiğinde **düzeltici faaliyete dönüşmesi** | YZYS-PR-08 + YZYS-FR-05 bağlantısı |
| A.8.4 | İletilecek **olay tipleri**, **bildirim süresi** ve **iletilecek ayrıntıların** önceden belirlenmiş olması | YZYS-PR-10 |
| A.9.3 | Hedefler tanımlanırken **etki değerlendirmesi sonuçlarının**, özellikle insan gözetimi açısından, dikkate alınması | YZYS-PL-03 — FR-04'e atıf zorunlu |
| A.9.4 | Amaçlanan kullanıma uygunluğu **göstermek için olay günlüğü tutulması** | YZYS-PR-06 + YZYS-FR-10 |
| A.10.2 | Kişisel veri işlendiğinde sorumlulukların **mevzuata uygun şekilde veri sorumlusu/işleyen arasında paylaştırılması** | YZYS-PR-12 + YZYS-LS-10 |
| A.10.3 | Tedarikçiden **düzeltici faaliyet talep hakkı** ve **yeterli ürün dokümantasyonu** talebi | YZYS-PR-12 — sözleşme maddesi olarak |
| A.10.4 | Müşteri ihtiyaç ve beklentilerini **anlamak için çaba gösterildiğinin** kanıtı | YZYS-FR-11 + geri bildirim kayıtları |

### A.9.4'ün iki yüzü

A.9.4 çoğu sette yalnızca bir beyan dokümanı (Amaçlanan Kullanım Beyanı) olarak
ele alınır. Kontrol listesi ise ikinci bir şey daha ister: **sistemin fiilen
amaçlanan kullanıma uygun işletildiğini gösteren olay günlükleri.** Yani A.9.4
hem bir *beyan* hem bir *kanıt* kontrolüdür.

Pratik karşılığı: PR-06'daki olay günlüğü tasarımında "amaç dışı kullanım
sinyali" bir log kategorisi olarak yer almalı. Örnek sinyaller — sistemin
tanımlanmış alan dışındaki bir konuda sorgulanması, yasaklı kullanım kalıbına
uyan girdi, tanımlı kullanıcı grubunun dışından erişim. Bu sinyallerin sayısı
9.1 izleme metriklerine de girer.
