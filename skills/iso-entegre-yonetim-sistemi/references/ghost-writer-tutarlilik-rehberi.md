# Ghost-Writer Tutarlılık Rehberi — Tüm Sete Tek Ses

## "İstikrarlı ghost writer mantığı" ne demek

`iso-tetkik-raporu-ghostwriter` skill'i tek bir tür doküman (tetkik raporu) için
tek bir baş tetkikçi ağzını taklit eder. Bu skill beş farklı standardın onlarca
doküman türünü kapsadığı için "aynı kişinin kaleminden çıkmış gibi" ifadesi
literal bir ses taklidi değil, **bir disiplin**dir: doküman türü değişse de
(politika farklı yazılır, prosedür farklı, form farklı) aynı beş kural her
zaman geçerli kalır ve hiçbir dosyada çiğnenmez. "İstikrarlı" kelimesinin
karşıladığı risk şudur: beş standardı beş ayrı skill çalıştırması olarak
üretirseniz, her biri kendi `icerik-rehberi.md`'sini doğru uygulasa bile,
aralarında **görünmeyen** kaymalar birikir — bir sette "BT Müdürü" denen rol
ötekinde "Bilgi İşlem Şefi" olur, biri "üç ayda bir" derken öteki aynı işi
"periyodik olarak" yazar. Tek tek bakıldığında hiçbiri hatalı değildir; yan yana
konunca kuruluşun **tek** bir sistemi olmadığı, beş ayrı belge yığını olduğu
ortaya çıkar. Bu rehber, üretimin sonunda **tüm sete** uygulanacak son geçişin
kurallarıdır.

## Doküman türüne göre ses değişir, disiplin değişmez

| Doküman türü | Ses/kip | Kaynak |
|---|---|---|
| Politika, prosedür, talimat | Zorunluluk kipi, edilgen özneli ("... tarafından ... yapılır") | `dokuman-mimarisi.md` §6 |
| Form/kayıt gövdesi | Nötr, alan-değer | `dokuman-mimarisi.md` §5 |
| Kapsam/gerekçe/YGG gibi anlatı metni | Kuruluşa özgü, somut, üçüncü tekil şahıs | `icerik-rehberi.md` örnekleri |
| Tetkik raporu (bu skill'in kapsamı dışında, ama devam eden iş) | Edilgen + geçmiş zaman, baş tetkikçi ağzı | `iso-tetkik-raporu-ghostwriter` |

Sesi türe göre değiştirmek yanlış değildir — bir politikayı geçmiş zamanla
yazmak da tuhaf kaçar. Değişmeyen, **her türde** geçerli olan kurallar aşağıda.

## Her türde geçerli, hiçbirinde çiğnenmeyen beş kural

1. **Yasaklı klişe listesi tüm sette aynı ve sabit.** "Kapsamlı bir şekilde",
   "önemli ölçüde", "titizlikle", "genel olarak değerlendirildiğinde", "ayrıca
   belirtmek gerekir ki", "sağlam bir temel oluşturmaktadır" — hiçbir dosyada,
   hiçbir standardın setinde geçmez. Bir alt skill bunlardan birini üretmişse
   son geçişte temizle.

2. **Ölçülemez ifade yasak, her yerde aynı biçimde düzeltilir.** "Düzenli
   olarak" → somut sıklık; "yeterli" → somut eşik; "gerektiğinde" → somut
   tetikleyici. Bu sadece tek bir dokümanın kendi içinde tutarlı olması değil,
   **aynı faaliyetin** iki farklı standardın dokümanında aynı sıklıkla
   anılması demektir (örn. erişim gözden geçirmesi hem BGYS hem KVYS
   dokümanında geçiyorsa ikisi de "üç ayda bir" demeli, biri "altı ayda bir"
   dememeli — aksi hâlde hangisinin doğru olduğu belirsizleşir).

3. **Uydurma veri/istatistik/kayıt yasağı tüm sette geçerli.** Örnek risk,
   örnek varlık, örnek olay üretilebilir ama her biri `[ÖRNEK — kuruluş
   tarafından doğrulanacak]` etiketiyle işaretlenir. Bilinmeyen bilgi
   `[DOLDURULACAK: ne istendiği net yazılarak]` bırakılır, asla boş
   bırakılmaz ya da uydurulmaz. Bu iki etiket birbirine karıştırılmaz.

4. **Kuruluşa özgü yaz, jenerik cümleyi tespit edip çıkar.** Son geçişte her
   paragraf için sor: *bu cümleyi başka bir şirkete kopyalasam anlamı değişir
   mi?* Değişmiyorsa fazla jeneriktir — gerçek birim adı, gerçek sistem adı,
   gerçek lokasyon ekle ya da cümleyi çıkar.

5. **Terminoloji ve isimlendirme tüm sette birebir aynı.** Kuruluş unvanının
   yazımı (A.Ş. / AŞ / Anonim Şirketi), rol adları, sistem adları, standart
   kısaltmaları (BGYS/İSYS/HYYS/KVYS/YZYS/EYS) her dosyada aynı şekilde
   geçer. Bunu elle takip etmek yerine üretim başında bir **terim sözlüğü**
   (kuruluş unvanı, roller, sistem adları — tek kaynak) kur ve her dokümanı
   ondan besle; son geçişte sözlükten sapma var mı diye tara.

## Son geçiş — nasıl yapılır

Set tamamlandıktan sonra, dosya dosya değil **konu konu** tara — bu, standartlar
arası tutarsızlığı standart-içi tutarsızlıktan daha hızlı yakalar:

1. Tüm dosyalarda kuruluş unvanının yazımını ara, tek biçime indir.
2. Tüm dosyalarda geçen rol adlarını çıkar, aynı role iki farklı ad verilmiş mi
   kontrol et.
3. Aynı faaliyeti (iç tetkik, YGG, erişim gözden geçirme, yedekleme, farkındalık
   eğitimi) birden fazla dokümanda ara, sıklık/eşik ifadelerinin çakışıp
   çakışmadığını doğrula.
4. Yasaklı klişe listesini tüm sette ara (script ile grep etmek elle taramaktan
   çok daha güvenilirdir).
5. `[DOLDURULACAK]` ve `[ÖRNEK]` etiketlerini say, `OKUBENI.md`'de dosya bazında
   listele — bu sayım zaten her alt skill'in kendi öz kontrolünde var, burada
   yalnızca **tüm set için tek bir liste** hâline getir.

## Üç soruluk son kontrol (her doküman için, `icerik-rehberi.md`'den genelleştirilmiş)

1. Bu cümleyi başka bir şirkete kopyalasam anlamı değişir mi?
2. Denetçi "kanıtını gösterin" derse ne gösterilecek?
3. Bu sıklığı/eşiği kim, neye göre belirledi — savunulabilir mi, yoksa
   `[DOLDURULACAK]` mı bırakılmalı?

Bu üç soru tek bir dokümanı yazan bir kişi için yeterlidir. Entegre sette
buna dördüncü soru eklenir: **Bu bilgi setin başka bir yerinde farklı mı
anlatılıyor?** Cevap evetse, hangisinin doğru olduğunu kullanıcıya sor —
kendi başına birini seçme, çünkü seçtiğin yanlış olursa denetimde iki dokümanın
çelişmesinden çok daha kötü bir bulgu (yanlış bilgi verme) doğar.
