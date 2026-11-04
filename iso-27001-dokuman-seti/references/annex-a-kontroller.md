# ISO/IEC 27001:2022 Ek A — 93 Kontrol / Doküman / Kanıt Matrisi

## İçindekiler

- A.5 — Kurumsal kontroller
- A.6 — Kişi kontrolleri
- A.7 — Fiziksel kontroller
- A.8 — Teknolojik kontroller

Uygulanabilirlik Bildirgesi (SoA) bu tablodan üretilir. `Doküman` sütunu skill'in
ürettiği dosya kodlarına, `Kanıt` sütunu denetçinin sahada isteyeceği uygulama
kanıtına işaret eder. Kontrol başlıkları TS EN ISO/IEC 27001:2023 Türkçe
karşılıklarıdır.

**Hariç tutma:** Ek A kontrolleri gerekçelendirilerek hariç tutulabilir. Madde 4–10
gereklilikleri hariç tutulamaz. Her hariç tutmanın SoA'da yazılı gerekçesi olmalı.

**Doküman kodları TAM sete göredir.** Sadeleştirilmiş set üretiyorsan bu
tablodaki bazı kodların (PL-05, PL-08, PL-10, PL-11, PL-12, PL-13, PR-06,
PR-11, PR-12, PR-13, PR-14, PR-15, PR-17, PR-22) karşılığı olan doküman
üretilmez — bunları olduğu gibi SoA'ya yazarsan **var olmayan dokümana atıf**
bulgusu alırsın. `scripts/kayitlar_27001.py` bunu otomatik çözer:

```bash
python3 scripts/kayitlar_27001.py --kurulus "..." --cikti "..." --hangi soa --sade
```

Elle yazıyorsan aynı dosyadaki `SADE_ESLEME` sözlüğünü kullan.


## A.5 — Kurumsal kontroller

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.5.1 | Bilgi güvenliği politikaları | BGYS-PL-01, konuya özgü politikalar | Onaylı politika, yayım/duyuru kaydı, yıllık gözden geçirme tutanağı |
| A.5.2 | Bilgi güvenliği rolleri ve sorumlulukları | BGYS-EK-01 §6, BGYS-FR-01 Görev Tanımları | Organizasyon şeması, imzalı görev tanımları, atama yazıları |
| A.5.3 | Görevlerin ayrılığı | BGYS-PR-05 Erişim Kontrol Prosedürü §Görev Ayrılığı | Görev ayrılığı matrisi, çakışan yetki analizi |
| A.5.4 | Yönetim sorumlulukları | BGYS-PL-01 §Yönetim Sorumlulukları | YGG tutanağı, yönetim taahhüt beyanı |
| A.5.5 | Yetkililerle iletişim | BGYS-PR-09 İhlal Olayı Yönetimi §Yetkili İletişimi | Yetkili kurum iletişim listesi (USOM, KVKK, kolluk), bildirim kayıtları |
| A.5.6 | Özel ilgi gruplarıyla iletişim | BGYS-LS-06 İlgili Taraf ve İletişim Listesi | Üyelik/abonelik kayıtları, forum katılım kanıtı |
| A.5.7 | Tehdit istihbaratı | BGYS-PR-14 Tehdit İstihbaratı Prosedürü | İstihbarat kaynak listesi, periyodik istihbarat raporları |
| A.5.8 | Proje yönetiminde bilgi güvenliği | BGYS-PR-12 Proje Yönetiminde Bilgi Güvenliği | Proje kontrol listesi, proje risk değerlendirmeleri |
| A.5.9 | Bilgi envanteri ve diğer ilgili varlıklar | BGYS-LS-01 Varlık Envanteri | Güncel varlık envanteri, varlık sahibi atamaları |
| A.5.10 | Bilgilerin ve diğer ilişkili varlıkların kabul edilebilir kullanımı | BGYS-PL-03 Kabul Edilebilir Kullanım Politikası | İmzalı kullanım taahhütnameleri |
| A.5.11 | Varlıkların iadesi | BGYS-PR-04 İK Güvenliği §Çıkış, BGYS-FR-07 İşten Ayrılış Formu | Doldurulmuş çıkış formları, zimmet iade kayıtları |
| A.5.12 | Bilgilerin sınıflandırılması | BGYS-PL-04 Bilgi Sınıflandırma Politikası | Sınıflandırma şeması, sınıflandırılmış varlık örnekleri |
| A.5.13 | Bilgilerin etiketlenmesi | BGYS-TL-01 Bilgi Etiketleme Talimatı | Etiketlenmiş doküman/ortam örnekleri |
| A.5.14 | Bilgi transferi | BGYS-PR-11 Bilgi Transferi Prosedürü | Transfer anlaşmaları, güvenli transfer kayıtları |
| A.5.15 | Erişim kontrolu | BGYS-PL-02 Erişim Kontrol Politikası | Erişim kuralları, rol-yetki matrisi |
| A.5.16 | Kimlik yönetimi | BGYS-PR-05 Erişim Kontrol Prosedürü | Kimlik yaşam döngüsü kayıtları, açma/kapama talepleri |
| A.5.17 | Kimlik doğrulama bilgileri | BGYS-PL-05 Parola/Kimlik Doğrulama Politikası | Parola politikası teknik ayarları, MFA yapılandırma kanıtı |
| A.5.18 | Erişim hakları | BGYS-PR-05 §Erişim Hakları, BGYS-FR-05 Erişim Talep Formu | Periyodik erişim gözden geçirme kayıtları, onaylı talepler |
| A.5.19 | Tedarikçi ilişkilerinde bilgi güvenliği | BGYS-PR-08 Tedarikçi Güvenliği Prosedürü | Tedarikçi risk değerlendirmeleri, tedarikçi listesi |
| A.5.20 | Tedarikçi anlaşmalarında bilgi güvenliğinin ele alınması | BGYS-FR-10 Tedarikçi Güvenlik Ekleri | İmzalı sözleşme güvenlik maddeleri, GİA/NDA |
| A.5.21 | Bilgi ve iletişim teknolojisi (BİT) tedarik zincirinde bilgi güvenliğini yönetme | BGYS-PR-08 §BİT Tedarik Zinciri | Tedarik zinciri risk analizi, ürün doğrulama kayıtları |
| A.5.22 | Tedarikçi hizmetlerinin izlenmesi, gözden geçirilmesi ve değişiklik yönetimi | BGYS-PR-08 §İzleme | Tedarikçi performans/SLA gözden geçirme raporları |
| A.5.23 | Bulut hizmetlerinin kullanımı için bilgi güvenliği | BGYS-PL-06 Bulut Hizmetleri Güvenlik Politikası | Bulut sağlayıcı değerlendirmesi, sorumluluk paylaşım matrisi, çıkış planı |
| A.5.24 | Bilgi güvenliği ihlal olayı yönetimi planlaması ve hazırlığı | BGYS-PR-09 İhlal Olayı Yönetim Prosedürü | Olay müdahale planı, rol atamaları, tatbikat kaydı |
| A.5.25 | Bilgi güvenliği ihlal olaylarını değerlendirme ve karar verme | BGYS-PR-09 §Değerlendirme | Olay kayıt defteri, sınıflandırma kararları |
| A.5.26 | Bilgi güvenliği ihlal olaylarına yanıt verme | BGYS-PR-09 §Müdahale | Olay müdahale kayıtları, kapanış raporları |
| A.5.27 | Bilgi güvenliği ihlal olaylarından ders çıkarma | BGYS-PR-09 §Ders Çıkarma | Olay sonrası değerlendirme raporları, iyileştirme aksiyonları |
| A.5.28 | Kanıt toplama | BGYS-TL-02 Adli Kanıt Toplama Talimatı | Kanıt saklama zinciri formu, örnek kanıt kaydı |
| A.5.29 | Kesinti sırasında bilgi güvenliği | BGYS-PN-04 İş Sürekliliği/BİT Süreklilik Planı | Kesinti senaryosu planı, tatbikat raporu |
| A.5.30 | İş sürekliliği için BİT hazırlığı | BGYS-PN-04 §BİT Hazırlığı | RTO/RPO tanımları, yedekleme/geri dönüş testleri |
| A.5.31 | Yasal, meşru, düzenleyici ve sözleşmeye tabi gereklilikler | BGYS-LS-03 Yasal ve Sözleşmesel Yükümlülükler Matrisi | Mevzuat listesi, uyum değerlendirme kayıtları |
| A.5.32 | Fikri Mülkiyet Hakları | BGYS-PL-03 §Fikri Mülkiyet | Lisans envanteri, yazılım uyum denetimi kayıtları |
| A.5.33 | Kayıtların korunması | BGYS-PR-01 Doküman ve Kayıt Kontrol Prosedürü | Saklama planı, arşiv/imha kayıtları |
| A.5.34 | Kişiyi tespit bilgisinin (PII) gizliliği ve korunması | BGYS-PL-07 Kişisel Veri Koruma Politikası | VERBİS kaydı, aydınlatma metinleri, işleme envanteri |
| A.5.35 | Bilgi güvenliğinin bağımsız gözden geçirilmesi | BGYS-PR-10 İç Tetkik Prosedürü, bağımsız gözden geçirme | Bağımsız gözden geçirme raporu, sızma testi raporu |
| A.5.36 | Bilgi güvenliğine yönelik politikalar, kurallar ve standartlara uygunluk | BGYS-PR-13 Uygunluk Gözden Geçirme | Uyum kontrol listeleri, teknik uyum tarama raporları |
| A.5.37 | Dokümante edilmiş işletim prosedürleri | BGYS-TL-xx İşletim Talimatları | Yayımlanmış işletim talimatları, personel erişim kanıtı |

## A.6 — Kişi kontrolleri

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.6.1 | Tarama | BGYS-PR-04 İK Güvenliği §İşe Alım | Özgeçmiş doğrulama, adli sicil, referans kontrol kayıtları |
| A.6.2 | İstihdam hüküm ve koşulları | BGYS-FR-08 İş Sözleşmesi Güvenlik Eki | İmzalı sözleşmeler / güvenlik ekleri |
| A.6.3 | Bilgi güvenliği farkındalığı, eğitim ve öğretim | BGYS-PN-02 Farkındalık ve Eğitim Planı | Eğitim kayıtları, katılım listeleri, sınav sonuçları, oltalama tatbikatı |
| A.6.4 | Disiplin süreci | BGYS-PR-04 §Disiplin Süreci | Disiplin yönetmeliği, uygulanmış disiplin kayıtları (anonim) |
| A.6.5 | İstihdamın sona ermesinden veya değiştirilmesinden sonraki sorumluluklar | BGYS-PR-04 §Görev Değişikliği ve Ayrılış | Çıkış kontrol listesi, yetki kapatma kayıtları |
| A.6.6 | Gizlilik veya ifşa etmeme anlaşmaları | BGYS-FR-09 Gizlilik Taahhütnamesi (NDA) | İmzalı NDA'lar, gözden geçirme tarihleri |
| A.6.7 | Uzaktan çalışma | BGYS-PL-08 Uzaktan Çalışma Politikası | Uzaktan erişim yapılandırması, VPN/MDM kayıtları |
| A.6.8 | Bilgi güvenliği olayı raporlanması | BGYS-PR-09 §Olay Bildirimi, BGYS-FR-11 Olay Bildirim Formu | Bildirim kanalı kanıtı, gelen bildirim kayıtları |

## A.7 — Fiziksel kontroller

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.7.1 | Fiziksel güvenlik sınırları | BGYS-PL-09 Fiziksel Güvenlik Politikası | Güvenlik sınırı krokisi, çevre güvenlik önlemleri |
| A.7.2 | Fiziksel giriş | BGYS-PR-06 Fiziksel Erişim Prosedürü | Kartlı geçiş logları, ziyaretçi defteri |
| A.7.3 | Ofislerin, odaların ve tesislerin güvenliğini sağlama | BGYS-PL-09 §Güvenli Alanlar | Güvenli alan tanımları, erişim yetki listesi |
| A.7.4 | Fiziksel güvenlik izleme | BGYS-PL-09 §İzleme | CCTV kayıt politikası, alarm sistemi kayıtları |
| A.7.5 | Fiziksel ve çevresel tehditlere karşı koruma | BGYS-PL-09 §Çevresel Tehditler | Yangın/su baskını önlemleri, çevresel risk değerlendirmesi |
| A.7.6 | Güvenli alanlarda çalışma | BGYS-TL-03 Güvenli Alanlarda Çalışma Talimatı | Kural duyurusu, refakat kayıtları |
| A.7.7 | Temiz masa ve temiz ekran | BGYS-PL-03 §Temiz Masa/Ekran | Periyodik temiz masa denetim kayıtları |
| A.7.8 | Ekipman konumlandırma ve koruma | BGYS-PL-09 §Ekipman | Sistem odası yerleşim planı, koruma önlemleri |
| A.7.9 | Kuruluş dışındaki varlıkların güvenliği | BGYS-PL-10 Taşınabilir Cihaz Politikası | Cihaz zimmet kayıtları, şifreleme kanıtı |
| A.7.10 | Depolama ortamı | BGYS-PR-07 Ortam Yönetimi Prosedürü | Ortam envanteri, imha tutanakları |
| A.7.11 | Destekleyici altyapı hizmetleri | BGYS-PL-09 §Destekleyici Altyapı | UPS/jeneratör bakım kayıtları, test raporları |
| A.7.12 | Kablo güvenliği | BGYS-PL-09 §Kablolama | Kablo altyapı planı, koruma önlemleri |
| A.7.13 | Ekipman bakımı | BGYS-PN-05 Bakım Planı | Periyodik bakım kayıtları, servis raporları |
| A.7.14 | Ekipmanın güvenli bir şekilde yok edilmesi veya tekrar kullanılması | BGYS-PR-07 §Güvenli İmha | İmha tutanakları, veri silme sertifikaları |

## A.8 — Teknolojik kontroller

| Kontrol | Başlık | İlgili doküman | Denetimde istenen kanıt |
|---|---|---|---|
| A.8.1 | Kullanıcı uç nokta cihazları | BGYS-PL-10 Uç Nokta Güvenliği Politikası | MDM/uç nokta koruma yapılandırması, uyum raporu |
| A.8.2 | Ayrıcalıklı erişim hakları | BGYS-PR-05 §Ayrıcalıklı Erişim | Ayrıcalıklı hesap envanteri, PAM kayıtları, periyodik gözden geçirme |
| A.8.3 | Bilgi erişim kısıtlaması | BGYS-PL-02 §Bilgi Erişim Kısıtlaması | Yetki matrisi, uygulama seviyesinde erişim ayarları |
| A.8.4 | Kaynak koduna erişim | BGYS-PR-12 §Kaynak Kod Erişimi | Depo erişim yetkileri, kod deposu logları |
| A.8.5 | Güvenli kimlik doğrulama | BGYS-PL-05 §Güvenli Kimlik Doğrulama | MFA yapılandırması, oturum politikası ayarları |
| A.8.6 | Kapasite yönetimi | BGYS-PR-15 Kapasite Yönetimi | Kapasite izleme raporları, eşik uyarı kayıtları |
| A.8.7 | Kötü amaçlı yazılıma karşı koruma | BGYS-PL-11 Kötü Amaçlı Yazılımdan Korunma | AV/EDR konsol raporları, tarama kayıtları |
| A.8.8 | Teknik açıklıkların yönetimi | BGYS-PR-16 Açıklık Yönetimi Prosedürü | Zafiyet tarama raporları, yama takip kaydı, SLA'lar |
| A.8.9 | Konfigürasyon (yapılandırma) yönetimi | BGYS-PR-17 Konfigürasyon Yönetimi | Temel yapılandırma (baseline) dokümanları, sapma raporları |
| A.8.10 | Bilgi silme | BGYS-PR-07 §Bilgi Silme | Silme talep/onay kayıtları, silme doğrulama |
| A.8.11 | Veri maskeleme | BGYS-PL-12 Veri Maskeleme ve Anonimleştirme | Test ortamı veri maskeleme kanıtı |
| A.8.12 | Veri sızıntısı önleme | BGYS-PL-13 Veri Sızıntısı Önleme | DLP kural seti, ihlal uyarı kayıtları |
| A.8.13 | Bilgi yedekleme | BGYS-PR-18 Yedekleme Prosedürü | Yedekleme takvimi, başarı/başarısızlık logları, geri dönüş testi raporu |
| A.8.14 | Bilgi işleme tesislerinin yedek fazlalığı | BGYS-PN-04 §Yedeklilik | Yüksek erişilebilirlik mimarisi, devreye alma testleri |
| A.8.15 | Kaydetme (Log tutma) | BGYS-PR-19 Kayıt (Log) Yönetimi | Log envanteri, saklama süresi, bütünlük koruması, 5651 uyumu |
| A.8.16 | İzleme faaliyetleri | BGYS-PR-19 §İzleme | SIEM/izleme kuralları, alarm ve müdahale kayıtları |
| A.8.17 | Saat senkronizasyonu | BGYS-PR-19 §Saat Senkronizasyonu | NTP yapılandırma kanıtı |
| A.8.18 | Ayrıcalıklı destek programların kullanımı | BGYS-PR-05 §Ayrıcalıklı Yardımcı Programlar | Kısıtlama yapılandırması, kullanım logları |
| A.8.19 | İşletim sistemlerine yazılım kurulumu | BGYS-PR-17 §İşletim Sistemi Yazılımı | Yazılım kurulum onay kayıtları, imaj yönetimi |
| A.8.20 | Ağ güvenliği | BGYS-PL-14 Ağ Güvenliği Politikası | Ağ topolojisi, güvenlik duvarı kural seti, kural gözden geçirme |
| A.8.21 | Ağ hizmetlerinin güvenliği | BGYS-PL-14 §Ağ Hizmetleri | Hizmet seviyesi ve güvenlik özellikleri tanımları |
| A.8.22 | Ağların ayrımı | BGYS-PL-14 §Ağ Ayrımı | VLAN/segmentasyon şeması, DMZ tasarımı |
| A.8.23 | Web filtreleme | BGYS-PL-14 §Web Filtreleme | Web filtre politikası ve kural kayıtları |
| A.8.24 | Kriptografi (şifreleme) kullanımı | BGYS-PL-15 Kriptografi Politikası | Şifreleme algoritma/anahtar standartları, anahtar yönetimi kayıtları |
| A.8.25 | Güvenli geliştirme yaşam döngüsü | BGYS-PR-20 Güvenli Yazılım Geliştirme | SDLC tanımı, güvenlik kapıları, kod gözden geçirme kayıtları |
| A.8.26 | Uygulama güvenlik gereklilikleri | BGYS-PR-20 §Uygulama Güvenlik Gereksinimleri | Güvenlik gereksinim listesi, tasarım gözden geçirmeleri |
| A.8.27 | Güvenli sistem mimarisi ve mühendislik ilkeleri | BGYS-PR-20 §Güvenli Mimari | Mimari prensipler dokümanı, tehdit modelleme çıktıları |
| A.8.28 | Güvenli kodlama | BGYS-TL-04 Güvenli Kodlama Talimatı | Kodlama standardı, SAST tarama raporları |
| A.8.29 | Geliştirme ve kabul aşamasında güvenlik testleri | BGYS-PR-20 §Test | Güvenlik test planı ve raporları, sızma testi |
| A.8.30 | Dış kaynak yoluyla geliştirme | BGYS-PR-08 §Dış Kaynaklı Geliştirme | Sözleşme güvenlik maddeleri, kabul testleri |
| A.8.31 | Geliştirme, test ve canlı (gerçek) ortamlarının ayrılması | BGYS-PR-20 §Ortam Ayrımı | Ortam ayrım şeması, canlı veriyi test ortamında kullanmama kanıtı |
| A.8.32 | Değişiklik yönetimi | BGYS-PR-21 Değişiklik Yönetimi Prosedürü | Değişiklik talep/onay kayıtları, CAB tutanakları, geri alma planları |
| A.8.33 | Test bilgisi | BGYS-PL-12 §Test Bilgisi | Test verisi seçim ve koruma kayıtları |
| A.8.34 | Tetkik testi sırasında bilgi sistemlerinin korunması | BGYS-PR-10 §Tetkik Sırasında Sistem Koruması | Tetkik erişim planı, salt okunur erişim kanıtı |
