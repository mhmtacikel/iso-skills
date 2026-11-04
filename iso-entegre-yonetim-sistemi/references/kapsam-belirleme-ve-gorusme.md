# Kapsam Belirleme ve Birleşik Görüşme

## Adım 1 — Standart keşfi (bu skill'in ilk işi)

Elindeki skill listesinde `iso-` ile başlayıp `-dokuman-seti` ile biten her
skill'i bul. Bunu her çalışmada tekrar yap, sabit bir listeye güvenme — yeni bir
standart skill'i eklendiyse otomatik yakalanmalı. Bulduklarını kullanıcıya kısa
adlarıyla sun:

- `iso-27001-dokuman-seti` → ISO/IEC 27001 — Bilgi Güvenliği (BGYS)
- `iso-20000-1-dokuman-seti` → ISO/IEC 20000-1 — Hizmet Yönetimi (HYYS)
- `iso-22301-dokuman-seti` → ISO 22301 — İş Sürekliliği (İSYS)
- `iso-27701-dokuman-seti` → ISO/IEC 27701 — Kişisel Veri (KVYS)
- `iso-42001-dokuman-seti` → ISO/IEC 42001 — Yapay Zekâ (YZYS)

`AskUserQuestion` ile çoklu seçim sor. Kullanıcı listede olmayan bir standart
isterse (ISO 9001, 14001, 45001 gibi) dürüstçe söyle: o standardın doküman
listesi ve Ek A/madde eşlemesi bu ortamda mevcut değil; genel Annex SL
metodolojisiyle bir Madde 4–10 iskeleti kurulabilir ama doğrulanmamış olacağını
belirt, uydurma standarda özgü içerik (Ek A listesi, madde numaraları) üretme.

## Adım 2 — Ortak altı soru (bir kez sor)

Her `iso-*-dokuman-seti` skill'inin `gorusme-rehberi.md`'si aynı temel anketi
taşır. Onu kaynak skill'lerden birinden oku (hepsi aynıdır) ve **bir kez** sor.
Tipik başlıklar: kuruluş kimliği ve ölçek, mevcut yönetim sistemi (varsa),
kurumsal şablon (varsa, `sablon_analiz.py` ile taranır), kodlama tercihi, tam mı
sadeleştirilmiş mi set, hedef sertifikasyon takvimi.

## Adım 3 — Standarda özgü ek sorular (yalnızca seçilenler için)

Her standardın SKILL.md'sinde "27001'e özgü olarak şunu da sor" tarzında 1–2 ek
soru tanımlı. Kapsamda olan standartlar için bunları ekle, olmayanları sorma:

- **27001 (BGYS):** Bilgi varlıklarının ağırlığı nerede (müşteri verisi / fikri
  mülkiyet / finansal / sağlık / OT)? Yazılım geliştiriliyor mu, veri merkezi
  kendine mi ait?
- **42001 (YZYS):** Hangi YZ sistemleri kullanılıyor/geliştiriliyor, kuruluş
  hangi rolde (geliştirici / sağlayıcı / kullanıcı)? Karar özerkliği düzeyi ne —
  öneri mi üretiyor, bağlayıcı karar mı veriyor?
- **27701 (KVYS):** Hangi kişisel veri kategorileri işleniyor (özel nitelikli
  dahil mi)? 2019 sürümü mü (27001 eklentisi) yoksa 2025 sürümü mü (bağımsız)
  hedefleniyor, yoksa geçiş mi yapılıyor?
- **22301 (İSYS):** Kritik süreçler hangileri, tolerans edilebilir kesinti
  süresi (MTPD) yaklaşık ne? Daha önce bir olay/kesinti yaşandı mı?
- **20000-1 (HYYS):** Hizmet kataloğu var mı, müşteri tipi iç mi dış mı, mevcut
  bir ITSM aracı kullanılıyor mu?

## Adım 4 — Entegrasyona özgü ek sorular (bu skill'e has, her kurulumda sor)

Bunlar hiçbir tekil standart skill'inde yok, çünkü yalnızca birden fazla
standart aynı anda kurulduğunda anlamlı:

1. **Zaten ayrı ayrı kurulmuş bir sistem var mı?** Varsa "Mevcut ayrı sistemleri
   birleştirme" akışına geç (bkz. ana `SKILL.md`).
2. **Standartlar aynı anda mı sertifikalandırılacak, yoksa aşamalı mı** (örn.
   önce 27001, altı ay sonra 22301)? Aşamalıysa, sonradan eklenecek standardın
   Katman 1 dokümanlarını **şimdiden** o standardı da karşılayacak genişlikte mi
   yazalım, yoksa yalnızca ilk standarda mı odaklanalım — genişletme sonradan
   daha maliyetli olur, bunu kullanıcıya açıkça anlat ve tercihini sor.
3. **Standartlar arasında ortak organizasyonel sınır var mı, yoksa farklı
   birimler/lokasyonlar mı kapsıyor?** (örn. BGYS tüm şirketi kapsarken İSYS
   yalnızca üretim biriminde olabilir) — bu, kapsam beyanının nerede
   birleşeceğini, nerede ayrışacağını belirler.
4. **İç tetkik ve YGG tek programda mı birleşecek, yoksa standartlar farklı
   dönemlerde mi tetkik edilecek?** Tek programda birleşmek kaynak tasarrufu
   sağlar ama tüm standartların aynı anda hazır olmasını gerektirir.

## Soru sırası — önerilen akış

1. Standart keşfi + seçim (Adım 1)
2. Ortak altı soru (Adım 2)
3. Entegrasyona özgü dört soru (Adım 4) — kapsamın nasıl şekilleneceğini
   belirledikleri için standarda özgü sorulardan **önce** sorulmalı
4. Seçilen her standart için 1–2 özel soru (Adım 3)

Bu sırayı tersine çevirme: standarda özgü sorulara önce dalmak, kullanıcıyı
"zaten iki sistemim var, sadece birleştirmek istiyorum" gibi akışı değiştiren
bir bilgiyi geç vermeye iter.
