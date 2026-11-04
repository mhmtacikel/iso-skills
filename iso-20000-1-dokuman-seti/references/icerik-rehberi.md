# İçerik Rehberi — Kalite Çıtası ve Örnek Metinler

## İçindekiler

- 1. Kapsam beyanı
- 2. Hizmet kataloğu kaydı
- 3. SLA hedefi
- 4. SLA–OLA–UC hizalaması
- 5. Olay–problem ayrımı (aynı vaka, iki kayıt)
- 6. Değişiklik kaydı — geri alma planı
- 7. CMDB doğrulama kaydı
- 8. Hizmet raporu tanımı
- 9. `[DOLDURULACAK]` ve `[ÖRNEK]`
- 10. Ton kontrolü

Her örneğin zayıf ve güçlü sürümü verilmiştir. Zayıf sürümler gerçek denetimlerde
bulgu almış kalıplardır.

---

## 1. Kapsam beyanı

**Zayıf:** "BT departmanının sunduğu tüm hizmetler HYYS kapsamındadır."

**Güçlü:**
> Bu hizmet yönetim sistemi, ACME Bilişim A.Ş.'nin İstanbul Maslak Merkez Ofisi
> ve Ankara Veri Merkezi'nden, kamu ve özel sektör müşterilerine sunduğu
> **bulut altyapı barındırma (IaaS)**, **yönetilen veritabanı** ve **7/24 hizmet
> masası** hizmetlerinin planlanması, sunulması, izlenmesi ve iyileştirilmesini
> kapsar. Kapsanan hizmetler HYYS-LS-01 Hizmet Kataloğu Rev. 02'de listelenmiştir.
>
> **Kapsam dışı:** Yazılım geliştirme danışmanlığı, proje bazlı sunulduğu ve
> sürekli bir hizmet niteliği taşımadığı için kapsam dışıdır.
>
> **Diğer taraflarca işletilen prosesler (8.2.3):** Veri merkezi fiziksel
> altyapısı XYZ Veri Merkezi A.Ş. tarafından işletilmektedir. Kuruluş bu proses
> üzerinde; sözleşmedeki erişilebilirlik hedefleri, aylık performans raporlaması,
> çeyreklik yerinde denetim hakkı ve hedef ihlalinde yaptırım maddesi yoluyla
> yönetişim göstermektedir (bkz. HYYS-LS-05).

Son paragraf 20000-1'de kritiktir. 8.2.3'e açık atıf, kapsam tartışmasını
denetimden önce kapatır.

---

## 2. Hizmet kataloğu kaydı

**Zayıf:** `SRV-01 | Exchange | E-posta sunucusu | BT`

**Güçlü:**

| Alan | Değer |
|---|---|
| Hizmet Kodu / Adı | SRV-004 / Kurumsal E-posta ve Takvim |
| Kategori | İletişim |
| Açıklama (müşteri dili) | Kurumsal e-posta hesabı, paylaşımlı takvim ve mobil erişim. 50 GB posta kutusu, spam ve zararlı içerik filtreleme dahil. |
| Hedef kullanıcı grubu | Tüm kadrolu personel ve 6 aydan uzun süreli danışmanlar |
| Hizmet Sahibi / Teknik Sahip | Kurumsal Hizmetler Müdürü / Sistem Yönetimi Ekip Lideri |
| Bağımlı KÖ'ler | CI-0112 (Exchange kümesi), CI-0034 (AD), CI-0201 (spam ağ geçidi) |
| Bağımlı hizmetler | SRV-001 Ağ Bağlantısı, SRV-002 Kimlik Yönetimi |
| Tedarikçi bağımlılığı | Microsoft 365 E3 lisansı (TED-004) |
| Hizmet / destek saatleri | 7/24 / 08:00–18:00 iş günleri (P1 için 7/24) |
| İlgili SLA / Kritiklik | SLA-002 / Yüksek |
| Devreye alma / Durum | 2024-03-01 / Aktif |

Açıklama sütunu teknoloji değil **fayda** anlatır. Denetçi katalogdan bir hizmet
seçip müşteriye sorabilir: "bu hizmetin ne olduğunu bu tarifle anladınız mı?"

---

## 3. SLA hedefi

**Zayıf:** "Hizmet yüksek erişilebilirlikte sunulur ve arızalar hızla giderilir."

**Güçlü:**

| Hedef | Metrik | Eşik | Ölçüm dönemi | Ölçüm kaynağı | İstisnalar |
|---|---|---|---|---|---|
| H-01 Erişilebilirlik | Aylık hizmet erişilebilirliği | ≥ %99,5 | Takvim ayı | Zabbix erişilebilirlik raporu, 5 dk örnekleme | En az 5 iş günü önce duyurulan planlı bakım (ayda azami 4 saat) |
| H-02 P1 ilk müdahale | Kayıt açılışından ilk müdahaleye süre | ≤ 15 dk | Takvim ayı, vakaların %95'i | Jira SM SLA raporu | Müşteri kaynaklı bilgi bekleme süreleri duraklatılır |
| H-03 P1 çözüm | Kayıt açılışından çözüme süre | ≤ 4 saat | Takvim ayı, vakaların %90'ı | Jira SM SLA raporu | Tedarikçi kaynaklı donanım tedarik süresi hariç (ayrıca raporlanır) |

"Vakaların %95'i" ifadesi önemlidir: tek bir istisnai vakanın SLA'yı ihlal
etmesini engeller ve ölçümü gerçekçi kılar.

---

## 4. SLA–OLA–UC hizalaması

**Zayıf:** SLA'da "P1 çözüm 4 saat" yazılı, tedarikçi sözleşmesinde 8 saat.
Bu tutarsızlık yazıldığı anda SLA tutulamaz hâle gelir.

**Güçlü:**

| Hizmet | Hedef | SLA | OLA (iç) | UC (tedarikçi) | Toplam | Kontrol |
|---|---|---|---|---|---|---|
| SRV-004 | P1 çözüm | 4 sa | BT Operasyon: 2,5 sa | Microsoft Premier: 1 sa | 3,5 sa | OK — 0,5 sa tampon |
| SRV-002 | P1 çözüm | 2 sa | Kimlik ekibi: 1,5 sa | Donanım tedarikçisi: 2 sa | 3,5 sa | **ÇELİŞKİ** — SLA 2 sa'ya sığmıyor |

İkinci satır bir bulgudur ve SLA imzalanmadan çözülmelidir: ya SLA hedefi
gevşetilir, ya tedarikçi sözleşmesi sıkılaştırılır, ya yedek çözüm konur.
Bu tabloyu üretmek denetçinin işini önceden yapmaktır.

---

## 5. Olay–problem ayrımı (aynı vaka, iki kayıt)

**Zayıf:** Tek kayıtta "e-posta çalışmıyordu, sunucu yeniden başlatıldı, kapatıldı."

**Güçlü:**

> **Olay INC-2026-0412** — 14 Mart 09:12'de kullanıcılar e-postaya erişemedi.
> Etki: Yüksek (tüm kullanıcılar), Aciliyet: Yüksek → **P1**. İlk müdahale 09:19.
> Exchange kümesinde bellek tükenmesi tespit edildi; düğüm yeniden başlatıldı,
> hizmet 10:38'de normale döndü. Çözüm süresi 1 sa 26 dk (SLA 4 sa — uygun).
> Aynı belirti son 60 günde 3. kez görüldüğü için **PRB-2026-018 açıldı.**
>
> **Problem PRB-2026-018** — Kaynak: tekrarlayan olay (INC-2026-0301, -0367, -0412).
> Analiz yöntemi: 5 Neden. **Kök neden:** posta kutusu büyüme oranı kapasite
> planında öngörülenin 2,4 katı; bellek tahsisi 2024 yılı boyutlandırmasında kalmış
> ve kapasite izleme eşiği bu bileşen için tanımlanmamış.
> **Geçici çözüm:** haftalık planlı yeniden başlatma (bakım penceresinde).
> **Kalıcı çözüm:** bellek 64 GB'a çıkarılacak (CHG-2026-0091) ve kapasite
> izlemeye bellek eşiği eklenecek (HYYS-FR-10 satır 23).
> Kapanış: kalıcı çözüm sonrası 30 gün tekrar gözlenmezse.

İki kaydın birbirine referans vermesi zinciri gösterir: olay → problem →
değişiklik → kapasite kaydı. Denetçinin görmek istediği tam olarak budur.

---

## 6. Değişiklik kaydı — geri alma planı

**Zayıf:** Geri alma planı sütunu boş veya "gerekirse geri alınır".

**Güçlü:**
> **Geri alma planı:** Dağıtım öncesi mevcut sanal makinenin anlık görüntüsü
> (snapshot) alınır. Sorun tespitinde Sistem Yöneticisi anlık görüntüye döner
> (tahmini süre 20 dk). Anlık görüntü, dağıtımdan 7 gün sonra silinir.
> Geri alma kararı, dağıtım sonrası doğrulama testlerinden herhangi birinin
> başarısız olması hâlinde Değişiklik Yöneticisi tarafından verilir; karar
> penceresi dağıtım sonrası ilk 2 saattir.

Geri alınamayan değişiklikler için (örn. veritabanı şema geçişi) bunu açıkça
yaz ve alternatif kurtarma yolunu belirt. Boş bırakmak seçenek değil.

---

## 7. CMDB doğrulama kaydı

**Zayıf:** CMDB dolu ama "son doğrulama" sütunu hiç doldurulmamış.

**Güçlü:**
> **Doğrulama yaklaşımı (HYYS-PR-08 §7):** Kritik KÖ'ler üç ayda bir, diğerleri
> yılda bir doğrulanır. Doğrulama, otomatik keşif (discovery) çıktısı ile CMDB
> kaydının karşılaştırılması ve farkların incelenmesiyle yapılır. Fark tespit
> edilirse kayıt düzeltilir ve farkın nedeni araştırılır — kontrolsüz değişikliğe
> işaret ediyorsa DÖF açılır. Doğrulama sonucu CMDB'nin "Son Doğrulama Tarihi",
> "Doğrulayan" ve "Doğrulama Sonucu" sütunlarına işlenir; özet, üç aylık hizmet
> raporunda yer alır.

Son cümle önemli: doğrulamanın raporlamaya bağlanması, yapıldığının kanıtıdır.

---

## 8. Hizmet raporu tanımı

**Zayıf:** "Müşteriye aylık rapor gönderilir."

**Güçlü:**

| Alan | Değer |
|---|---|
| Rapor adı | SRV-004 Aylık Hizmet Performans Raporu |
| Amaç | SLA-002 hedeflerine uyumun müşteriye gösterilmesi ve sapmaların gerekçelendirilmesi |
| Hedef kitle | Müşteri BT Koordinatörü, Hizmet Sahibi, HYYS Yöneticisi |
| İçerik | Erişilebilirlik, olay hacmi ve öncelik dağılımı, SLA uyum oranları, ihlaller ve nedenleri, açık problemler, planlı değişiklikler, kapasite trendi |
| Veri kaynağı | Zabbix (erişilebilirlik), Jira SM (olay/talep/SLA), CMDB (değişiklik) |
| Sıklık / Teslim | Aylık, takip eden ayın 5. iş gününe kadar |
| Format / Kanal | PDF, müşteri portalı + e-posta |
| Sorumlu | Hizmet Seviyesi Yöneticisi |

---

## 9. `[DOLDURULACAK]` ve `[ÖRNEK]`

- `[DOLDURULACAK: Jira SM'de tanımlı P1 ilk müdahale SLA süresi]`
- `[ÖRNEK — doğrulanacak]` — ürettiğin varsayım satırları

**Uydurulamayacaklar:** gerçekleşmiş olay kayıtları, SLA gerçekleşme rakamları,
CMDB doğrulama tarihleri, müşteri memnuniyet skorları. Boş şablon üret, örneği
etiketle.

---

## 10. Ton kontrolü

1. **Her SLA hedefinin beş bileşeni var mı?** (metrik, eşik, dönem, kaynak, istisna)
2. **Olay ile problem birbirine karışmış mı?** Aynı prosedürde ikisini
   birleştirdiysen ayır.
3. **Katalogdaki her hizmet zincirin sonuna kadar takip edilebiliyor mu?**
   (SLA → OLA/UC → ölçüm → rapor)
4. **Bu prosedürü hizmet masası çalışanı okuyup uygulayabilir mi?**
   Uygulanamayan prosedür denetimde "yaşamayan süreç" bulgusu üretir.
