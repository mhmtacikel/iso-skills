# iso-* skill'leri — 2.0.0 değişiklikleri (2026-11-04)

Kurulum ve bakım: `README.md`.

## Test bulgularına göre yapılanlar
| Bulgu (baseline test) | Çözüm |
|---|---|
| Tetkik skill'i "uygunsuzluk yok" sonucunu dayatıyor, eksik kişi adı ve delil uyduruyordu; test ajanı skill'e karşı gelmek zorunda kaldı | Skill baş tetkikçi asistanı olarak yeniden yazıldı: sınıfı ve sonucu tetkikçi verir, sorular tek mesajda ve taslak metinle sorulur, uydurma yok, yazım kalıbı tarifli (sıfır klişe) |
| 42001 SKILL.md 1467 satırdı, ajan %61'ini okudu; ekler references ile çift kopyaydı | 482 satıra indi; ekler 5 reference dosyasına, gömülü Python betiği `scripts/envanter_senkron.py`'ye taşındı; hafif yol ve eklentisiz akış eklendi |
| 4.1/4.2'de iklim değişikliği tadilatı (Amd 1:2024) yoktu | 27001, 22301, 20000-1 madde rehberlerine ve entegre haritaya eklendi |
| Motor 6 skill'de kopya ve ayrışmıştı; 5'inde `tr_upper` yoktu | Motor 2.0.0 tek kaynak; K1 (`tr_upper`), K2 (`Kimlik(tur="yol_gosterici")`), K3 (`tr()` sözlüğü) yerleşik |
| `kayitlar_27701.py` her çalıştırmada çöküyordu (sayfa adında "/") | Motorda sayfa adı temizleme |
| Cowork araçlarına bağlıydı (device_*) | Her skill'de "Çalışma ortamı" tablosu: Cowork ↔ Claude Code |
| 10 maddelik tutarlılık taraması her seferinde elle yazdırılıyordu | `scripts/tutarlilik_tarama.py` |
| K2 (kodsuz yol gösterici) ile doküman listelerindeki RP kodları çelişiyordu | 27001, 27701, entegre referansları ve 27701 betiği düzeltildi |
| 100 satırı aşan referanslarda içindekiler yoktu | Eklendi |
