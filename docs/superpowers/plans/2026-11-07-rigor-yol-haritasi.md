# Rigor — Mimari ve Faz Yol Haritası

**Spec:** [`docs/superpowers/specs/2026-11-07-rigor-design.md`](../specs/2026-11-07-rigor-design.md) (onaylı, K1–K26)
**Araştırma:** [`docs/research/2026-11-07-arastirma-notlari.md`](../../research/2026-11-07-arastirma-notlari.md) (§16: plan öncesi doğrulama)

Bu belge mimariyi ve fazları sabitler. Spec birbirinden bağımsız test edilebilen birçok alt sistem içerdiği için
**her fazın ayrıntılı TDD planı ayrı bir belgedir** ve o faz başlarken yazılır. Faz 1 planı:
[`2026-11-07-faz-1-cekirdek.md`](2026-11-07-faz-1-cekirdek.md).

---

## 1. Paket mimarisi

```text
src/rigor/
  __init__.py          genel API (Session, given, unknown, eq…, audit_formula, reconcile) + __lazy_modules__
  core/                ALANDAN BAĞIMSIZ ÇEKİRDEK (K24) — domains/, llm/, mcp/ içe aktaramaz
    numbers.py         kesin sayı okuma, sayı alanları
    ir/                tipli IR: nodes, builder, canonical (JSON + SHA-256)
    gates/             units (pint, Fraction), structure (eşleme + Dulmage–Mendelsohn), domain (sqrt/log/bölme)
    compile/           IR → SymPy, Z3, Arb (python-flint) [F2: → solve_ivp, F4d: → HiGHS/CVXPY]
    solve/             router + motorlar (algebraic, identity, logic) [F2: ode, F5: lean, F4d: optim]
    certify/           geri koyma, unsat çekirdeği [F4d: dual], [F5: Lean comparator]
    labels.py          Label, RefusalCode, Conditions, decide_label
    outcome.py         Outcome (etiket + değerler + sertifika + şartlar)
    provenance.py      girdi/onay kaynağı ve kanalı
    session.py         durum makinesi + kalıcı kayıt
    narrative.py       deterministik anlatım iskeleti (TR/EN) [F3: LLM sadeleştirme + koruma]
  report/              Markdown kanıt raporu, replay
  confirm/             bant dışı onay (işletim sistemi diyaloğu)
  doctor.py            ön kontrol (fail-closed)
  cli.py               `rigor doctor | replay | report` [sonraki fazlarda: selfcheck, domain …]
  mcp/                 MCPServer kabuğu (mcp 2.x)
  llm/                 [F3] formülatör adaptörleri: CLIFormalizer, OpenAICompatibleFormalizer, AgentSuppliedIR
  redteam/             [F3] hizalama, denklik, roundtrip, mutasyon
  templates/           [F4] şablonlar, öz-denetim, hakem, karar defteri
  lean/                [F5] ifade dondurma, yasaklı yapı taraması, comparator köprüsü
  domains/             [F2+] alan paketleri: DomainPack arayüzü, rocket/, finance/, fluids/
  finance/             [F7] Mod B1/B2, canlıya alma özeti
tests/                 core/ testleri alan paketi YÜKLEMEDEN geçmeli (§3.4 bağımsızlık testi)
```

**Bağımlılık kuralı (test edilir):** `rigor.core` yalnızca standart kütüphane + çekirdek bağımlılıkları (pydantic,
sympy, z3-solver, python-flint, pint, networkx, mpmath, scipy, hypothesis) içe aktarır; `rigor.domains`, `rigor.llm`,
`rigor.mcp`, `rigor.templates`, `rigor.lean`, `rigor.finance` modüllerini asla içe aktarmaz. Faz 1'de bir test bunu
AST taramasıyla doğrular.

**Fazlar arası sözleşmeler (Faz 1 tanımlar, sonrakiler genişletir):**
- `rigor.core.ir.nodes.Problem` — tek IR kökü; `schema_version` alanı ile sürümlü.
- `rigor.core.labels.Conditions` — etiket şartları; F3 `red_team` alanını `"applied"` yapar.
- `rigor.core.outcome.Outcome` — her yolun ortak sonucu.
- `rigor.core.provenance.Provenance` — `USER_DIRECT | VIA_AGENT_UNVERIFIED | USER_FILE` + kanal.
- `Engine` protokolü (`rigor.core.solve.base`): `name: str`, `supports(problem) -> bool`, `solve(problem) -> EngineResult`.
- F2'de eklenecek: `DomainPack` protokolü (`rigor.domains.base`), F3'te: `Formalizer` protokolü (`rigor.llm.base`).

## 2. Fazlar

Her faz `development` dalında yapılır; faz çıkış ölçütleri geçince `development` → `main` PR'ı açılır ve sürüm
etiketi alır (spec §8.4).

| Faz | Kapsam (spec) | Çıkış ölçütü | Etiket |
|---|---|---|---|
| **F1 Çekirdek** | §6.2 IR + kurucu, §6.3 kapılar, SymPy/Z3/Arb, §6.6 geri koyma, §4.1 etiketler (tek formülasyon → en fazla `CROSS_VALIDATED`), §4.2 oturum, §4.3 kaynak, §6.8 rapor (deterministik), `rigor doctor`, ince MCP + elicitation deneyi + bant dışı onay | Faz 1 altın testleri yeşil (3.12/3.14/3.15); yanlış `PROVEN` = 0; çekirdek bağımlılık kuralı testi yeşil | `v0.1.0` |
| **F2 Roket fiziği** | §5.4 `rocket` paketi + `DomainPack` arayüzü, §4.5 model doğrulama, `.eng`/xlsx/CSV/`.ork` okuyucular (`USER_FILE`), `Table` düğümü, ODE (DOP853 + Radau + yakınsama), aralıklı girdiler, §6.10 OpenRocket karşılaştırması | R2–R7 kütüphane ve dosyalarla otomatik; ISA tablo testleri; OpenRocket örnek dosyasıyla karşılaştırma raporu | `v0.2.0` |
| **F3 Red Team + doğal dil** | §6.1 ayrıştırma, §6.4 adaptörler (CLI izolasyonu, Groq), hizalama, denklik, roundtrip, mutasyon, §6.7 sade anlatım + koruma + okunabilirlik (TR + EN), tam MCP, §8.2 geçiş sözleşmesi | Doğal dilden `PROVEN`; altın sette tuzak problemleri (en az/en fazla, birim, iki yorum) doğru soru/ret üretir | `v0.3.0` |
| **F4 Şablon + öz-denetim + hakem** | §6.9, §6.9.1 | Bozulmuş şablon, sürüm değişikliği ve yanlış alarm senaryoları testte doğru davranır | `v0.4.0` |
| **F5 Lean 4** | §6.11 (`comparator` + `nanoda`, yasaklı yapılar, ifade dondurma, yalıtım) | Kasıtlı hileli ispatlar (sorry, axiom, native, ifade değiştirme) reddedilir; basit tümevarım teoremleri `PROVEN` | `v0.5.0` |
| **F6 Alan uyarlama** | §3.4 `rigor domain new/verify/bench`, olgunluk düzeyleri, güvenlik tabanı, `fluids` örnek paketi, paket yazma rehberi | `fluids` paketi `doğrulanmış`; güvenlik tabanını gevşeten paket yüklenmez | `v0.6.0` |
| **F7 Finans (Mod B)** | §5.2 B1 + B2, `finance` paketi, Sentinax canlıya alma özeti | Sentinax ve botun formül envanteri B1'den geçer; örnek çıktılar B2 ile mutabık | `v0.7.0` |
| **F8 Optimizasyon** | §6.5 HiGHS/CVXPY, dual sertifika, KKT | LP/MILP altın testleri `PROVEN` (dual sertifikalı) | `v0.8.0` |
| **F9 Sağlamlaştırma** | §9 altın setin tamamı, gerçek dosyalarla yerel kabul testi, belgeler | Tüm altın set yeşil; yanlış `PROVEN` = 0 | `v1.0.0` |

Sıra spec §10 ile aynıdır (1, 2, 3, 4, 4b, 4c, 5, 4d, 6). F7 (finans) F8'den önce gelir çünkü botun ve Sentinax'ın
formülleri optimizasyon motoru gerektirmez; Sentinax'ın CVaR/HRP optimizasyon çıktıları B2'de F8'e kadar
`CROSS_VALIDATED` ile sınırlıdır.

## 3. Faz 1'e giren riskler (araştırma notları §16)

- Sahibin makinesinde Python 3.15 yok ve `uv` eski → Faz 1 Görev 1'in ilk adımı.
- VS Code eklentisi elicitation'ı otomatik reddedebilir → bant dışı onay (işletim sistemi diyaloğu) Faz 1'de.
- `highspy`/`cvxpy` 3.15 wheel'i yok → Faz 1'de gerekmez; F8'de yeniden kontrol.
