# ISO/IEC 42005:2025 hizalaması (etki değerlendirmesi metodolojisi)
42005 yayımlandığından `[teyit]` beri denetçiler etki değerlendirmesi
metodolojisini bu rehberle karşılaştırmaya başladı. Rehberdir, belgelendirme
şartı değildir; ama metodolojinin 42005 dikkate alınarak kurulduğunu göstermek
"biçimsel değerlendirme" eleştirisine karşı en güçlü savunmadır.

Metodoloji dokümanında (etki değerlendirmesi prosedürü) şunların her biri
görünür olmalı — hepsi `etki-degerlendirmesi.md` §3'teki yapıyla zaten büyük
ölçüde örtüşür, eksik olanı ekle:

| 42005'in beklediği unsur (özet) | Bu sette karşılığı | Sık eksik |
|---|---|---|
| Değerlendirmenin **kuruluş süreçlerine entegrasyonu** — risk yönetimi, tasarım, tedarik, değişiklik yönetimiyle bağ | Prosedürde 6.1.2, 6.3, A.6 ve A.10 ile bağlantı maddeleri | Etki değerlendirmesinin tedarik (A.10) sürecine bağlanmaması |
| **Zamanlama ve tetikleyiciler** | `etki-degerlendirmesi.md` §4 tetikleyici listesi | Tetikleyiciyi fark edecek kişinin tanımlanmaması |
| **Kapsam** — sistemin sınırı, bileşenleri, değerlendirmenin sınırı | Envanter satırı + rapor kapsam bölümü | Üçüncü taraf bileşenin kapsam dışı bırakılması |
| **Amaçlanan kullanım ve makul öngörülebilir kötüye kullanım** | Envanterin üç kullanım sütunu | Amaç dışı kullanım sütununun boş kalması |
| **Etkilenen paydaşlar**, özellikle kırılgan gruplar | A.5.4 sekiz alan + etkilenen kişi grubu | Dolaylı etkilenenlerin (ör. adayın ailesi değil, reddedilen aday havuzu) unutulması |
| **Fiilî ve potansiyel etkiler — olumlu ve olumsuz** | A.5.3 yedi kalem | Olumlu etkilerin yazılmaması |
| **Önlemler ve artık etki** | Azaltıcı önlem + artık etki + kabul eden unvan | Artık etkiyi kimin kabul ettiğinin yazılmaması |
| **Hassas veya kısıtlı kullanımlar için eşikler** — hangi durumda üst onay veya kullanmama kararı | Eklenti profilindeki yönetişim kademeleri ve kırmızı çizgiler | Eşiğin kişisel takdire bırakılması |
| **Dokümantasyon, iletişim ve gözden geçirme** | Rapor + A.8 şeffaflık + gözden geçirme tarihi | Değerlendirme sonucunun etkilenenlere nasıl iletileceğinin yazılmaması |

**Eklentiyle bağ.** `aia-generation` hukuki AIA'yı üretir (rejim bazlı
sınıflandırma, FRIA gerekip gerekmediği, politika farkı). 42001 etki
değerlendirmesi kişi/grup/toplum etkisini 42005 çerçevesinde belgeler. İkisi
**aynı sistem için paralel yürür**:

- 42001 raporunda "Yasal bağlam" bölümü AIA'nın **sonucunu ve referansını**
  taşır, gerekçesini değil (Ek E1 §4).
- AIA'da bulunan her somut risk (eklentinin "kötü risk / iyi risk" kalitesinde)
  42001 raporunda bir etki satırına karşılık gelmeli; karşılığı yoksa ya AIA
  42001 alanlarında bir boşluk bulmuştur ya da etki değerlendirmesi eksiktir.
- Eklentinin önem derecesi taban olarak geçer (sessiz düşürme yok).
- FRIA gerekiyorsa bu üç değerlendirmeden (42001 etki, hukuki AIA, KVKK/PIA)
  ayrı bir teslimattır; hiçbiri diğerinin yerine geçmez.

Çift zincir kontrolünü elle değil `scripts/envanter_senkron.py zincir` ile yap;
eklenti envanteri verilirse AB bağlantılı sistemlerde hukuki sınıflandırmanın
da yapılıp yapılmadığını aynı raporda gösterir. Bu bölümde 42005'in madde
numaraları verilmedi; metodoloji dokümanına yazılacaksa standardın metninden
doğrulanarak eklenir.
