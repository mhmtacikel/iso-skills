# Entegrasyon Kodlama ve Klasör Şeması

Bu, her `iso-*-dokuman-seti` skill'inin kendi `dokuman-mimarisi.md`'sinde
zaten tanımlı olan `EYS-` önek kuralının (bkz. o dosyanın §2'si) **çok
standartlı kurulumda nasıl uygulanacağının** açılımıdır. Tek başına bir standart
kurarken bu dosyaya gerek yok; iki veya daha fazla standart aynı sette
birleşiyorsa buradan ilerle.

## Önek kuralı

| Önek | Ne zaman kullanılır |
|---|---|
| `EYS-` | Katman 1 dokümanları (bkz. `annex-sl-cekirdek-haritasi.md`) — birden fazla standarda hizmet eden her doküman |
| `BGYS-` / `İSYS-` / `HYYS-` / `KVYS-` / `YZYS-` | Katman 3 dokümanları — yalnızca o standarda özgü, kendi Ek A/teknik alanından doğan doküman |
| Standarda özgü önek + `EYS-` çapraz referansı | Katman 2 dokümanları — çerçeve `EYS-` ile, standarda özgü kayıt seti kendi önekiyle, ikisi birbirine "İlgili dokümanlar" bölümünden bağlanır |

Kullanıcının kendi kurumsal kodlama kuralı varsa (görüşmede sorulur, bkz.
`kapsam-belirleme-ve-gorusme.md`) o kural `EYS-` yerine geçer, mantık aynı kalır.

**Hangi standartlar kapsamdaysa, önek kısaltmasını görüşmenin başında bir kez
sabitle ve tüm üretim boyunca değiştirme.** İki farklı toplantıda "İSYS" bir kez
"BS" diye kısaltılırsa çapraz referanslar kopar.

## Klasör ağacı

```
[Kuruluş] - Entegre Yönetim Sistemi Doküman Seti/
├── 00_Kapsam_ve_ElKitabi/
│   ├── EYS-PL-00 Entegre Kapsam Dokümanı (ana kapsam + standarda özgü ekler)
│   └── EYS-EK-01 El Kitabı
├── 01_Politikalar/
│   ├── EYS-PL-01 Ana Politika (taahhüt, ilkeler — tüm standartlara atıfla)
│   └── [standarda özgü politikalar kendi önekiyle, örn. BGYS-PL-02 Erişim Kontrol Politikası]
├── 02_Prosedurler/
│   ├── EYS-PR-01 Doküman Kontrol
│   ├── EYS-PR-03 Düzeltici Faaliyet
│   ├── EYS-PR-10 İç Tetkik
│   ├── EYS-PR-21 Değişiklik Yönetimi (EYS düzeyinde)
│   ├── EYS-PR-22 Yönetimin Gözden Geçirmesi
│   └── [standarda özgü prosedürler kendi önekiyle — Katman 3, madde 8]
├── 03_Talimatlar/
├── 04_Formlar_ve_Listeler/
│   ├── EYS-LS-01 İlgili Taraflar Analizi
│   ├── EYS-LS-02 Yetkinlik Matrisi
│   ├── EYS-LS-03 Doküman Ana Listesi (tüm setin tek listesi, "ilgili standart" sütunuyla filtrelenir)
│   ├── EYS-FR-01 Bağlam Analizi
│   ├── EYS-FR-04 Hedef ve Performans Göstergeleri (standarda özgü göstergeler ayrı satır)
│   ├── EYS-FR-12 DÖF Formu
│   ├── EYS-FR-13 YGG Tutanağı
│   └── [standarda özgü form/liste kendi önekiyle — SoA, BIA, DPIA, hizmet kataloğu, YZ sistem envanteri…]
├── 05_Planlar/
│   ├── EYS-PN-01 Farkındalık Planı
│   ├── EYS-PN-02 İletişim Planı
│   ├── EYS-PN-03 Tetkik Programı (tek program, "hangi standart(lar)" sütunu)
│   └── [standarda özgü planlar — süreklilik/tatbikat planı, risk işleme planı…]
├── 06_Kayitlar_ORNEK/          ← yalnızca kullanıcı açıkça isterse (bkz. dokuman-mimarisi.md §3)
├── 07_Denetim_Hazirlik/
│   ├── EYS-RP-01 Birleşik Kanıt Matrisi (gereklilik → standart(lar) → doküman → kanıt → sorumlu)
│   └── EYS-RP-02 Öz Değerlendirme (ortak geçiş + her standardın kendine özgü geçişi)
└── OKUBENI.md
```

**Standart başına ayrı üst klasör açma.** `00_BGYS/`, `00_İSYS/` gibi bir yapı
tam olarak önlemeye çalıştığımız şeyi yeniden yaratır: beş ayrı sistem görüntüsü.
Klasörler doküman **tipine** göre ayrılır (politika, prosedür, form…), standarda
göre değil; standart ayrımı dosya önekinde ve `EYS-LS-03`'ün "ilgili standart"
sütununda yaşar.

## Doküman ana listesi — tek tablo, filtrelenebilir sütun

`EYS-LS-03 Doküman Ana Listesi` şu sütunları taşımalı:

```
Kod | Doküman Adı | Format | Tip | İlgili Standart(lar) | İlgili Madde(ler) | Rev No | Rev Tarihi | Onaylayan
```

"İlgili Standart(lar)" sütunu çoklu değer alabilir (örn. "27001, 22301, 42001")
— bu, Katman 1 dokümanlarının çoklu standarda hizmet ettiğini tek satırda
gösterir ve denetçiye "bu doküman beş kez değil bir kez yazıldı, kasıtlı"
mesajını verir.

## Kanıt matrisi — birleşik format

```
Madde | Gereklilik (kısa) | İlgili Standart(lar) | Doküman Kodu | Kanıt Türü | Sorumlu | Durum
```

Katman 1 satırları tek satırda birden fazla standardı işaretler (✓27001 ✓22301
✓42001). Katman 3 satırları yalnızca kendi standardını işaretler. Bu matris
`iso-*-dokuman-seti` skill'lerinin ayrı ayrı ürettiği kanıt matrislerinin yerine
geçer — beşini yan yana koyma, tek matriste birleştir.
