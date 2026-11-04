# Annex SL Çekirdek Haritası — Madde 4–10 Standartlar Arası Eşleme

Bu dosya, kapsamdaki standartların Madde 4–10'unun nerede **birleştirilebileceğini**,
nerede **ortak çerçeve + standarda özgü içerik** gerektirdiğini ve nerede
**tamamen ayrışacağını** gösterir. Amaç: her standardın kendi `madde-4-10.md`
(veya eşdeğeri, örn. 42001'de aynı isimli dosya, 27701'de kendi referans seti)
dosyasını beşer kez okuyup beşer ayrı doküman yazmak yerine, tek geçişte doğru
kararı vermek.

**Bu dosya bir kısayoldur, kaynak değildir.** Kesin gereklilik metni, madde
numarası ve "Z" (zorunlu dokümante bilgi) işaretleri için her zaman kapsamdaki
standardın kendi `iso-*-dokuman-seti` skill'indeki referans dosyasına git ve
oradan doğrula — burada anlatılan "hangi madde nereye gider" mantığıdır, madde
metninin kendisi değil.

---

## Katman 1 — Doğrudan birleşir (tek `EYS-` dokümanı, çoklu madde referansı)

Bu maddelerin çekirdek metni Annex SL'de neredeyse birebir aynıdır. Kapsamdaki
standart sayısı kaç olursa olsun **tek** doküman yaz, "Standart madde ilişkisi"
bölümünde her standardın kendi numarasını ayrı satırda listele.

| Annex SL maddesi | Tipik EYS dokümanı | Standartlar arası fark |
|---|---|---|
| 4.1 İç/dış hususlar | EYS-FR-01 Bağlam Analizi | Yok — hususların listesi ortak, yalnızca bazı dış hususlar (mevzuat) standarda göre çeşitlenir; aynı tabloya ek sütun olarak eklenebilir |
| 4.2 İlgili taraflar | EYS-LS-01 İlgili Taraflar Analizi | Yok — hangi tarafın hangi standartla ilgili olduğu bir sütunla işaretlenir |
| 4.4 Sistemin kurulması | EYS-EK-01 El Kitabı | Yok, tek kitap tüm sistemi anlatır |
| 5.1 Liderlik ve taahhüt | YGG tutanakları, taahhüt beyanı | Yok |
| 5.3 Rol ve sorumluluk | Organizasyon şeması, görev tanımları | Yok — roller genelde ortak (Üst Yönetim, EYS Yöneticisi); standarda özgü rol varsa (örn. Veri Sorumlusu Temsilcisi, YZ Sistem Sahibi) ek satır |
| 6.3 Değişikliklerin planlanması | EYS-PR-21 Değişiklik Yönetimi (EYS düzeyinde) | Yok |
| 7.1 Kaynaklar | Bütçe/kadro kayıtları | Yok |
| 7.2 Yetkinlik | EYS-LS-02 Yetkinlik Matrisi | Standarda özgü yetkinlikler (örn. YZ okuryazarlığı — 42001 madde 7'nin kendine özgü eki, aşağıya bak) matrise ek sütun/satır olarak girer, ayrı doküman değil |
| 7.3 Farkındalık | EYS-PN-01 Farkındalık Planı + eğitim kayıtları | Standarda özgü içerik (KVKK, bilgi güvenliği, iş sürekliliği, sorumlu YZ) aynı planın farklı modülleri olarak |
| 7.4 İletişim | EYS-PN-02 İletişim Planı | Yok |
| 7.5.1–7.5.3 Dokümante bilgi | EYS-PR-01 Doküman Kontrol Prosedürü + EYS-LS-03 Doküman Ana Listesi | Yok — ana liste tüm standartların dokümanlarını tek tabloda tutar, "ilgili standart" sütunuyla filtrelenir |
| 9.1 İzleme, ölçme, analiz | EYS-FR-04 Hedef ve Performans Göstergeleri | Standarda özgü göstergeler (oltalama tıklama oranı, RTO gerçekleşme oranı, model sapma oranı, hizmet seviyesi uyum oranı) aynı tabloda ayrı satırlar |
| 9.2.1–9.2.2 İç tetkik | EYS-PR-10 İç Tetkik Prosedürü + EYS-PN-03 Tetkik Programı | Tek program, tek denetim döneminde tüm kapsamdaki standartlar birlikte tetkik edilebilir (kaynak tasarrufu) — programda "hangi standart(lar)" sütunu |
| 9.3.1–9.3.3 YGG | EYS-PR-22 YGG Prosedürü + EYS-FR-13 YGG Tutanağı | On girdi başlığı ortak; her standardın kendi performans özeti (BGYS özeti, İSYS özeti, YZYS özeti…) YGG gündeminde ayrı alt madde olarak yer alır, ayrı toplantı değil |
| 10.1 / 10.2 Uygunsuzluk ve iyileştirme | EYS-PR-03 Düzeltici Faaliyet Prosedürü + EYS-FR-12 DÖF Formu | **Alt madde sırası (10.1/10.2) standarda ve sürüme göre değişir** — birleştirilmiş dokümanda madde numarasını değil madde **adını** ("Uygunsuzluk ve Düzeltici Faaliyet" / "Sürekli İyileştirme") esas al, sonra "Standart madde ilişkisi" tablosunda her standart için doğru numarayı ayrı ayrı yaz |

## Katman 2 — Ortak çerçeve, standarda özgü içerik (bağlı ama ayrı belgeler olabilir)

Madde numarası ve üst düzey gereklilik (kriter belirle, değerlendir, işle, kaydet)
ortaktır ama **neyin** değerlendirildiği standarttan standarda kökten değişir. Tek
tabloya sıkıştırmayı zorlama; ortak bir "Risk ve Fırsat Yönetimi Çerçevesi"
dokümanında kriterleri/ölçeği/rolleri bir kez tanımla, sonra her standardın kendi
kayıt setini (risk envanteri türü) ayrı ama **aynı format ve aynı sesle** yaz.

| Madde | Ortak olan | 27001 | 22301 | 27701 | 42001 | 20000-1 |
|---|---|---|---|---|---|---|
| 6.1.1 Risk ve fırsat | Süreç zorunluluğu | Bilgi güvenliği riski | İş kesintisi riski | Kişisel veri riski | YZ riski | Hizmet sürekliliği/kapasite riski |
| 6.1.2/6.1.3 (numara standarda göre kayabilir) | Kriter + değerlendirme + işleme süreci zorunluluğu | Risk envanteri + SoA (Ek A karşılaştırması zorunlu) | Bu standartta ayrı: BIA madde 8.2'ye kayar (aşağı bak) | Veri işleme riski + DPIA tetikleyicisi | Risk **ve** sistem/kişi **etki** değerlendirmesi ikilisi (ikisi ayrı kayıttır, karıştırma) | Hizmet riski, tedarikçi riski |
| 6.2 Hedefler | Ölçülebilir hedef tablosu zorunluluğu | Bilgi güvenliği hedefleri | Süreklilik hedefleri (RTO/RPO'ya bağlanabilir) | Veri koruma hedefleri | Sorumlu YZ hedefleri (adillik, şeffaflık ölçütleri dahil) | Hizmet seviyesi hedefleri |

**42001'e özgü not:** ISO/IEC 42001 madde 6'ya ek olarak kendi Annex A'sı yanında
**etki değerlendirmesi**yi risk değerlendirmesinden ayrı bir kayıt olarak ister
(kuruluşa etki vs. kişilere/topluma etki). Bunu 27001'in tek risk envanteri
kalıbına sıkıştırma — `iso-42001-dokuman-seti` skill'inin kendi ürettiği ayrı etki
değerlendirmesi kaydını oldğu gibi bırak, yalnızca çerçeve (kriter, ölçek, rol)
düzeyinde ortak dokümana bağla.

## Katman 3 — Neredeyse tamamen standarda özgü (Madde 8, ayrı belgeler)

Annex SL Madde 8'in ortak metni yalnızca "işletim planlaması ve kontrolü,
kriterlerin belirlenmesi, planlı/plansız değişikliklerin kontrolü, dış kaynaklı
proseslerin kontrolü" der — **gerisi tamamen standarda özgü ektir.** Bunları
birleştirmeye çalışma; her biri kendi standardının skill'i tarafından, kendi
önekiyle üretilir. Entegre sistemde bu belgelerin ortak yanı yalnızca **biçim ve
ses**tir (bkz. `ghost-writer-tutarlilik-rehberi.md`), içerik değil.

| Standart | Madde 8 alt kapsamı | Tipik çıktı |
|---|---|---|
| 27001 | 8.2 Risk değerlendirmesinin çalıştırılması, 8.3 Risk işleme planının uygulanması | Risk envanteri (tarihli), Risk İşleme Planı, SoA |
| 22301 | 8.2 İş Etki Analizi ve risk değerlendirmesi, 8.3 Süreklilik stratejisi, 8.4 Süreklilik planları, 8.5 Tatbikat programı, 8.6 Dokümantasyonun değerlendirilmesi | BIA raporu, strateji dokümanı, olay müdahale/iş sürekliliği planları, tatbikat programı ve raporları |
| 27701 | Veri işleme envanteri, DPIA, aydınlatma/rıza süreçleri, saklama-imha, yurt dışı aktarım, veri ihlali yönetimi | Envanter, DPIA formu, aydınlatma metinleri, ihlal prosedürü |
| 42001 | YZ sistem yaşam döngüsü kontrolü, veri yönetişimi, üçüncü taraf/tedarik zinciri | YZ sistem envanteri, model kartları, veri kökeni kayıtları, Ek A + SoA |
| 20000-1 | Hizmet portföyü/kataloğu, talep/olay/problem/değişiklik/sürüm/konfigürasyon yönetimi, kapasite ve süreklilik, tedarikçi yönetimi | Hizmet kataloğu, SLA/OLA, CMDB, süreç prosedürleri |

## Kararı hızlı vermek için

1. Doküman "kim yapar, ne sıklıkla, nasıl kaydedilir" sorusuna standarttan
   bağımsız aynı cevabı veriyorsa → **Katman 1, birleştir.**
2. Süreç zorunluluğu ortak ama girdi/çıktı verisi standarda göre kökten
   değişiyorsa → **Katman 2, ortak çerçeve + ayrı kayıt seti, aynı sesle.**
3. Doküman doğrudan bir standardın kendi Ek A'sından, kendi teknik alanından
   doğuyorsa (SoA, BIA, DPIA, model kartı, hizmet kataloğu) → **Katman 3,
   ayrı doküman, standardın kendi öneki.**

Bu üç sorunun cevabı belirsizse kullanıcıya sor — yanlış birleştirme (farklı
riskleri tek tabloya sıkıştırmak) yanlış ayırmaktan (aynı prosedürü beş kez
yazmak) daha tehlikelidir, çünkü ilkinde denetçinin bulacağı hata gizlenmiş olur.
