# Güncellik izleme listesi (Türkiye, AB, standartlar)
**Son teyit: 2026-10-23.**

> **Eskime kontrolü.** Bu bölümü okuyan her çalışma önce yukarıdaki tarihe
> bakar. 90 günden eskiyse kullanıcıya söyle: "Güncellik listesi [tarih]
> tarihinde teyit edilmiş, [N] ay önce. Listeyi bir kaynak olarak değil, neyi
> araştırmam gerektiğinin kontrol listesi olarak kullanıyorum." Ardından ilgili
> satırlar için web araması yap. Bir satırı güncellediğinde tarihi de güncelle.
>
> Eskimiş bir izleme listesi hiç liste olmamasından kötüdür — güncel görünür
> ama yanlıştır.

Bu bölümdeki her bilgi ikincil kaynaklardan derlenmiştir ve dokümana
`[teyit]` etiketiyle girer. Birincil kaynak (Resmî Gazete, TBMM, KVKK,
EUR-Lex, ISO) ile doğrulanmadan nihai metne kesin hüküm olarak yazılmaz.
`ai-governance-legal` eklentisinin `references/currency-watch.md` dosyası ABD
eyalet yasalarını da izler; ikisini birlikte oku, çelişki varsa daha yeni
tarihli olanı esas al ve çelişkiyi kullanıcıya göster.

## 1. Türkiye

| Konu | Durum (2026-10-23 itibarıyla) | Doğrulama yeri |
|---|---|---|
| Bağımsız YZ kanunu | **Yürürlükte değil.** TBMM'ye sunulmuş kanun teklifleri var: 25 Haziran 2024 (bağımsız YZ kanunu taslağı, risk değerlendirmesi ve "YZ operatörü" yükümlülükleri), 10 Kasım 2025 (5651, TCK, 7545, 5809, KVKK'da değişiklik; deepfake ve geliştirici sorumluluğu), 3 Aralık 2025 (5651 üzerinden YZ içeriği işaretleme). Komisyon aşamasında görünüyorlar `[teyit]` | tbmm.gov.tr → Kanun Teklifleri |
| KVKK — üretken YZ | Kurum, "Üretken Yapay Zekâ ve Kişisel Verilerin Korunması Rehberi (15 Soruda)" yayımladı — 24 Kasım 2025 `[teyit]`. Eğitim verisi, şeffaflık, ilgili kişi hakları, yurt dışı aktarım başlıkları etki değerlendirmesine ve A.7 veri kontrollerine girdi olur | kvkk.gov.tr → Yayınlar / Rehberler |
| KVKK — yurt dışı aktarım | 2024 değişikliğiyle (7499 s. Kanun) m.9 rejimi yeniden düzenlendi; standart sözleşme bildirimi ve uygunluk kararı mekanizmaları `[teyit-madde]`. Bulut tabanlı YZ API'leri için kritik | Resmî Gazete, kvkk.gov.tr |
| Siber Güvenlik Kanunu (7545) | 2025'te yürürlüğe girdi; ikincil düzenlemeler ve bildirim yükümlülükleri izlenmeli `[teyit]` | Resmî Gazete, Siber Güvenlik Başkanlığı |
| Sektörel | BDDK, SPK, Sağlık Bakanlığı, BTK düzenlemelerinde YZ'ye özgü hüküm veya rehber çıkıp çıkmadığı sorulmalı — kuruluşun sektörüne göre `[teyit]` | İlgili kurum siteleri |
| Ulusal YZ stratejisi | Ulusal Yapay Zekâ Stratejisi ve eylem planları — politika belgesi, yükümlülük değil; 4.1 bağlam girdisi `[teyit]` | Cumhurbaşkanlığı Dijital Dönüşüm Ofisi |

## 2. Avrupa Birliği

| Konu | Durum | Doğrulama yeri |
|---|---|---|
| AB YZ Yasası (2024/1689) | Yürürlükte; yükümlülükler aşamalı uygulanıyor `[yerleşik]` (varlığı) | EUR-Lex |
| Digital Omnibus on AI | **Kabul edildi ve yürürlükte (Temmuz 2026)** `[teyit]`. İkincil kaynaklara göre: Ek III yüksek risk yükümlülükleri → **2 Aralık 2027**; Ek I (ürün mevzuatı) yüksek risk → **2 Ağustos 2028**; 2 Ağustos 2026 öncesi piyasaya arz edilmiş sentetik içerik üreten sistemler için m.50 şeffaflık/işaretleme → **2 Aralık 2026**; yeni yasak uygulamalar (rıza dışı cinsel içerik/çocuk istismarı içeriği üretimi) → **2 Aralık 2026** `[teyit]` | EUR-Lex (Omnibus tüzüğünün resmî metni) |
| Okuryazarlık hükmü (m.4) | Omnibus sonrası sağlayıcı ve uygulayıcıların okuryazarlığı destekleyici önlem alma yükümlülüğü sürüyor; her bireyin belirli yetkinliğe ulaştığını garanti etme beklentisi kaldırıldı `[teyit]` | EUR-Lex |
| Yasak uygulamalar (m.5) ve genel amaçlı modeller | 2025'ten beri uygulanıyor; Komisyon rehberleri ve GPAI uygulama kuralları (Code of Practice) izlenmeli `[teyit]` | AI Office, EUR-Lex |
| Uyumlaştırılmış standartlar | CEN-CENELEC JTC 21 çalışmaları; 42001'in uyumlaştırılmış standart statüsü **yoktur** — uygunluk varsayımı doğurmaz `[teyit]` | CEN-CENELEC, Resmî Gazete'de yayım |

**Not:** Omnibus ile yüksek risk tarihleri ertelendi ama 42001 setinin ürettiği
malzeme (risk yönetimi, veri yönetişimi, teknik dokümantasyon, günlükler,
insan gözetimi) aynı kalır. Ertelemeyi "hazırlığı bırakma" gerekçesi olarak
dokümana yazma.

## 3. Standartlar

| Standart | Durum | Sette nerede |
|---|---|---|
| ISO/IEC 42001:2023 | Yürürlükte; 2024 iklim tadilatı (Amd 1) dahil `[teyit]` | Tüm set |
| ISO/IEC 42005:2025 — YZ sistemi etki değerlendirmesi | Yayımlandı (2025) `[teyit]`. Rehber niteliğinde; belgelendirme şartı değil | Ek E5 |
| ISO/IEC 42006:2025 — YZYS denetim/belgelendirme kuruluşu gereklilikleri | Yayımlandı (2025) `[teyit]` | Ek E2 §5 |
| ISO/IEC 23894:2023 — YZ risk yönetimi rehberi | Yürürlükte `[teyit]` | 6.1.2 risk metodolojisi |
| ISO/IEC 22989:2022 — kavram ve terminoloji | Yürürlükte `[teyit]` | Rol taksonomisi |
| ISO/IEC 42001 TS (Türkçe) | TSE yayımı ve sürümü kontrol edilmeli `[teyit]` | Kapak ve atıflar |

## 4. Nasıl kullanılır

- Yasal Uyum Matrisi (LS-10) veya bağlam dokümanı (4.1) yazılırken bu
  listedeki her ilgili satır için **web araması yap** ve sonucu etiketle.
- Bir satır değiştiyse ve kuruluşun seti varsa → sürdürme modu (Ek E2 §2c;
  `reg-gap-analysis` → LS-10 güncellemesi).
- Kullanıcı kendi bildiği bir gelişmeyi söylerse önce doğrula; listeye eklemeden
  önce kaynak iste veya ara.
