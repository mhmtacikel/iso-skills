# iso-skills

ISO yönetim sistemi skill'leri (Agent Skills formatı):

| Skill | Ne yapar |
|---|---|
| `iso-27001-dokuman-seti` | BGYS doküman seti |
| `iso-20000-1-dokuman-seti` | HYYS doküman seti |
| `iso-22301-dokuman-seti` | İSYS doküman seti |
| `iso-27701-dokuman-seti` | KVYS doküman seti (2019 ve 2025) |
| `iso-42001-dokuman-seti` | YZYS doküman seti ve sürdürme |
| `iso-45001-dokuman-seti` | İSGYS doküman seti (6331 entegre) |
| `iso-entegre-yonetim-sistemi` | Birden fazla standardı tek EYS setinde birleştirir |
| `iso-tetkik-raporu-ghostwriter` | Baş tetkikçi asistanı: Aşama 1/2 raporu ve soru listesi |

## Kurulum

**Claude Code** (bir kez):

```
/plugin marketplace add <github-kullanici>/iso-skills
/plugin install iso-skills@iso-skills
```

Güncelleme: `/plugin marketplace update iso-skills`. Private repo olduğu için
makinede GitHub'a erişim (git kimlik bilgisi) gerekir.

**claude.ai / Cowork:** Releases sayfasındaki son sürümün 8 zip dosyasını
Ayarlar → Skills'ten yükleyin (eski sürümlerin yerine).

**Diğer ajanlar** (Codex, Gemini CLI, Copilot CLI vb.): repoyu klonlayın ve
`skills/` altındaki klasörleri ajanın skill dizinine (örn. `~/.agents/skills/`)
kopyalayın veya bağlayın.

Gereksinim: `pip install python-docx openpyxl` (42001 eklenti senkronu için `pyyaml`).

## Bakım

- Ortak Word/Excel motorunun tek kaynağı `_ortak/scripts/`. Skill'lerin
  `scripts/` altındaki kopyalarını elle düzenlemeyin.
- Değişiklikten sonra:
  ```
  python _ortak/senkron.py      # motoru 6 skill'e kopyalar
  python _ortak/dogrula.py      # spesifikasyon + senkron kontrolü
  ```
- Her push'ta GitHub Actions doğrulamayı ve kayıt üreteçlerini çalıştırır.
- Sürüm: `.claude-plugin/plugin.json` ve `marketplace.json`'daki `version` ile
  SKILL.md'lerdeki `metadata.surum` değerini artırın, `DEGISIKLIKLER.md`'yi
  güncelleyin, `git tag vX.Y.Z && git push --tags`. Yayın iş akışı zip'leri
  Release'e ekler.
