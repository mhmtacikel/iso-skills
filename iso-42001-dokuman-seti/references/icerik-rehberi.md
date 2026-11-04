# İçerik Rehberi — Kalite Çıtası ve Örnek Metinler

Her örneğin zayıf ve güçlü sürümü verilmiştir.

---

## 1. Kapsam beyanı

**Zayıf:** "Şirketimizde kullanılan yapay zekâ sistemleri YZYS kapsamındadır."

**Güçlü:**
> Bu yapay zekâ yönetim sistemi, ACME Sigorta A.Ş.'nin İstanbul Genel Müdürlük
> lokasyonunda;
>
> - **geliştirici ve sağlayıcı** sıfatıyla ürettiği **hasar dosyası ön
>   değerlendirme modeli** (YZS-001) ve **müşteri talep sınıflandırma modeli**
>   (YZS-002),
> - **kullanıcı** sıfatıyla işlettiği **üçüncü taraf büyük dil modeli tabanlı
>   müşteri asistanı** (YZS-003)
>
> sistemlerinin tasarım, geliştirme, devreye alma, işletim ve emekliye ayırma
> aşamalarını kapsar.
>
> **Kapsam dışı:** Pazarlama biriminin içerik taslağı üretiminde kullandığı genel
> amaçlı üretken YZ araçları, kişiler hakkında karar üretmemesi ve kurumsal veriye
> erişmemesi nedeniyle kapsam dışıdır; kullanımı YZYS-PL-03 Sorumlu Kullanım
> Politikası ile yönetilir.
>
> Uygulanabilirlik Bildirgesi YZYS-LS-01 Rev. 01 geçerlidir.

Rol ayrımını sistem bazında yapmak 42001'e özgüdür ve denetçinin hangi
gereklilikleri arayacağını netleştirir.

---

## 2. Envanter kaydı

**Zayıf:** `YZS-003 | ChatGPT | Müşteri hizmetleri | Aktif`

**Güçlü:**

| Alan | Değer |
|---|---|
| Sistem No / Adı | YZS-003 / Müşteri Asistanı (poliçe bilgilendirme sohbet botu) |
| Sağlayıcı / Model tipi | [Sağlayıcı] · üçüncü taraf büyük dil modeli, RAG mimarisi ile poliçe dokümanlarına bağlı |
| Kuruluşun rolü | Kullanıcı (model geliştirilmiyor; sistem entegrasyonu kuruluşa ait) |
| Amaçlanan kullanım | Mevcut poliçe sahiplerinin teminat kapsamı, prim ve yenileme tarihi sorularının yanıtlanması |
| **Yasak / amaç dışı kullanım** | Hasar kararı verme, teminat kapsamı dışı beyanı, tıbbi veya hukuki tavsiye, yeni poliçe satışı, fiyat taahhüdü |
| Kullanıcı grubu | Poliçe sahipleri (web ve mobil) |
| **Etkilenen kişi grubu** | Poliçe sahipleri ve lehtarları — yanlış bilgi maddi karar hatasına yol açabilir |
| Karar özerkliği | İçerik üretimi; bağlayıcı karar üretmez, her yanıtta insan desteğine yönlendirme bağlantısı bulunur |
| İşlenen veri | Poliçe numarası, teminat bilgisi, sohbet geçmişi — kişisel veri var, özel nitelikli yok |
| Yaşam döngüsü / Kritiklik | İşletim / Yüksek |
| Risk kaydı / Etki değerlendirmesi | R-014, R-019 / ED-003 |

"Yasak / amaç dışı kullanım" sütunu A.9.4'ün doğrudan kanıtıdır ve boş bırakılamaz.

---

## 3. Risk ile etkinin ayrımı — aynı sistem, iki kayıt

**Zayıf:** Tek tabloda "Model yanlış cevap verebilir | Yüksek | İzleniyor."

**Güçlü:**

> **Risk R-019 (kuruluşa etki)** — Kategori: Model davranışı.
> Asistanın teminat kapsamı hakkında hatalı bilgi vermesi hâlinde kuruluş,
> müşteri şikâyeti, Sigortacılık ve Özel Emeklilik Düzenleme ve Denetleme
> Kurumu nezdinde uyuşmazlık ve itibar kaybı riskiyle karşılaşır.
> Olasılık 3 × Etki 4 = 12 (Orta). İşleme: azalt.
> Kontroller: RAG kaynak sınırlama (A.6.2.6), yanıt sonu sorumluluk reddi
> (A.8.2), haftalık örneklem kalite kontrolü. Artık risk 2 × 4 = 8.
> Risk sahibi: Dijital Kanallar Müdürü — onaylandı 2026-08-11.
>
> **Etki Değerlendirmesi ED-003 satır 4 (kişilere etki)** — Etki alanı: Güvenlik
> ve emniyet. Etkilenen taraf: poliçe sahibi, özellikle **dijital okuryazarlığı
> düşük ve yaşlı kullanıcılar (kırılgan grup)**. Potansiyel olumsuz etki: asistanın
> teminat kapsamını olduğundan geniş göstermesi hâlinde kullanıcı, aslında
> teminat altında olmayan bir masrafı yapıp maddi zarara uğrayabilir.
> Nasıl ortaya çıkar: model, poliçe metnindeki istisna maddesini bağlam
> penceresi dışında bırakırsa. Şiddet 4 × Olasılık 3 = 12; tersine çevrilebilir:
> **Hayır** (masraf yapılmışsa geri alınamaz); kırılgan grup: Evet → **Öncelik: Yüksek.**
> Azaltıcı önlem: teminat sorularında istisna maddelerinin zorunlu olarak
> yanıta eklenmesi; tutar içeren her yanıtta "bağlayıcı değildir, teyit için
> müşteri temsilcisine bağlanın" uyarısı; aylık örneklem üzerinde istisna
> atlama oranı ölçümü (hedef ≤ %1). Kalan etki: 2 × 3 = 6, kabul edildi —
> Dijital Kanallar Müdürü ve Uyum Müdürü, 2026-08-11.

İkisi aynı olayı anlatıyor gibi görünse de farklı sorulara cevap verir ve
farklı önlemler doğurur. Risk kaydı itibar/uyum, etki kaydı kullanıcının cebi
üzerine düşünür. Denetçi bu ayrımı görmek ister.

---

## 4. İnsan gözetimi

**Zayıf:** "Sistem insan gözetimi altında çalışmaktadır."

**Güçlü:**
> **İnsan gözetimi (ED-003 §5):** Hasar ön değerlendirme modeli (YZS-001) hiçbir
> koşulda nihai karar üretmez; çıktısı bir öneri skorudur.
>
> - **Gözeten:** Hasar Eksperi (yetki seviyesi 2 ve üzeri).
> - **Devreye girme eşiği:** Tüm dosyalar eksper onayından geçer. Model skoru
>   ile eksper kararının uyuşmadığı dosyalar ayrıca Hasar Müdürü'ne düşer.
> - **Müdahale için sunulan bilgi:** Eksper ekranında model skoru, skoru en çok
>   etkileyen üç faktör ve modelin güven aralığı gösterilir; ham dosya her zaman
>   erişilebilirdir.
> - **Müdahale süresi:** Eksperin karar süresi dosya başına asgari 4 dakika
>   olacak şekilde iş akışı tasarlanmıştır; bu süre altındaki kararlar aylık
>   raporda işaretlenir.
> - **Sistemi durdurma:** Dijital Kanallar Müdürü tek başına modeli devre dışı
>   bırakabilir; bu durumda süreç tamamen manuel akışa döner (YZYS-PR-06 §9).
> - **Gözetim etkinliği izlemesi:** Eksperin model önerisinden saptığı dosya
>   oranı aylık izlenir. Oranın %2'nin altına düşmesi, gözetimin biçimselleştiği
>   sinyali olarak değerlendirilir ve incelemeye alınır.

Son madde ayırt edicidir: hiç müdahale edilmeyen bir gözetim mekanizması
çalışmıyor olabilir. Bunu izlemek denetçiye olgunluk gösterir.

---

## 5. Veri kökeni

**Zayıf:** `Eğitim verisi | Kurum içi | 500 bin kayıt`

**Güçlü:**

| Alan | Değer |
|---|---|
| Veri seti | VS-004 Geçmiş hasar dosyaları (2019–2025) |
| Kaynak türü | Kurum içi üretim (hasar yönetim sistemi) |
| **Köken** | 2019-01 – 2025-12 arası kapatılmış hasar dosyalarından, Hasar Yönetim Sistemi'nden 2026-02-14 tarihli tek seferlik dışa aktarımla alındı. Aktarım kaydı: DATA-EXP-2026-011. Kimlik bilgileri aktarım sırasında sözde-anonimleştirildi (eşleme tablosu Hukuk biriminde ayrı tutulur). |
| **Kullanım izni / hukuki dayanak** | Sigorta sözleşmesinin ifası ve meşru menfaat (KVKK m.5/2-c, 5/2-f); model geliştirme amacı VERBİS bildiriminde yer almaktadır. |
| Temsil edicilik | Coğrafi dağılım kurum portföyüyle uyumlu; **ancak 2020–2021 pandemi döneminde hasar tipi dağılımı atipiktir ve bu dönem ayrıca ağırlıklandırılmıştır.** |
| Bilinen yanlılık | Portföyde büyükşehir ağırlığı yüksek (%71); kırsal hasar tiplerinde örneklem seyrek — model bu segmentte daha düşük güven aralığı üretiyor, ED-002'de ele alındı. |
| Ön işleme | Aykırı değer temizliği (üst %0,5 tutar), eksik alan doldurma (medyan), metin alanlarında kişi adı maskeleme |
| Saklama / sahip | 10 yıl (mevzuat) / Hasar Veri Sahibi |

"Bilinen yanlılık" alanını boş bırakma. Bilinmiyorsa `[DOLDURULACAK:
temsil edicilik analizi yapılmamış — VS-004 için planlanmalı]` yaz. Yanlılık
olmadığını iddia etmek, olduğunu söylemekten çok daha risklidir.

---

## 6. Model kartı (A.6.2.7)

Teknik dokümantasyon gerekliliğini karşılamanın en temiz yolu. Asgari başlıklar:

```
1. Model kimliği        : ad, sürüm, tarih, sahibi, iletişim
2. Amaçlanan kullanım   : kapsam, kullanıcı, karar bağlamı
3. Uygun olmayan kullanım: açıkça yasaklananlar
4. Mimari ve yaklaşım   : model tipi, girdi/çıktı, temel bileşenler
5. Eğitim verisi        : kaynak, dönem, hacim, ön işleme, bilinen sınırlar
6. Performans           : metrikler, ölçüm koşulları, test seti tanımı
7. Adillik değerlendirmesi: seçilen metrik, gruplar, sonuçlar, ödünleşimler
8. Bilinen sınırlılıklar: nerede iyi çalışmaz, hangi girdilerde güvenilmez
9. İnsan gözetimi       : gözetim modeli, müdahale yolu
10. İzleme              : izlenen metrikler, kayma tespiti, yeniden eğitim tetikleyicisi
11. Sürüm geçmişi       : değişiklikler ve gerekçeleri
```

6. ve 7. maddelerdeki sayıları **asla uydurma.** Tablo iskeletini üret,
`[DOLDURULACAK: test seti üzerinde ölçülecek]` bırak.

---

## 7. `[DOLDURULACAK]` ve `[ÖRNEK]`

42001'de özellikle katı ol. **Uydurulamayacaklar:** model performans metrikleri,
adillik test sonuçları, doğruluk oranları, olay kayıtları, kullanıcı geri
bildirim skorları, veri kalitesi ölçümleri.

Sahte bir adillik metriği yalnızca denetimi değil, o sistemden etkilenen
kişileri de yanıltır. Bu skill'in üreteceği en zararlı çıktı budur; metodoloji
ve boş tablo üret, ölçümü kuruluş yapsın.

---

## 8. Ton kontrolü

1. **Her YZ sisteminin hem risk hem etki kaydı var mı?** Yoksa 42001 karşılanmadı.
2. **Etki değerlendirmesinde "etkilenen taraf" kullanıcıdan farklı mı?**
   Aynıysa muhtemelen dolaylı etkilenenleri atladın.
3. **İnsan gözetimi tarif edilmiş mi, yoksa sadece iddia mı edilmiş?**
4. **Amaç dışı kullanımlar yazılı mı?**
5. **Bu metinde uydurulmuş bir sayı var mı?** Varsa çıkar.
