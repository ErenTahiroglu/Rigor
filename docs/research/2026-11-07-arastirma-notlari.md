# Rigor — Araştırma Notları (2026-11-07)

Tasarım belgesinin ([`../superpowers/specs/2026-11-07-rigor-design.md`](../superpowers/specs/2026-11-07-rigor-design.md))
dayandığı bulgular. Önceki oturumun envanteri için [`../../Handoff`](../../Handoff) §2'ye bakın; burada yalnızca
bu oturumda doğrulanan ya da yeni bulunanlar var.

> Not: Bulguların bir kısmı yalnızca makale özetlerinden (abstract) veya üçüncü taraf sayfalardan okunmuştur;
> bunlar "özetten" diye işaretlidir. Uygulamaya geçmeden önce birincil kaynakla doğrulanmalıdır.

## 1. Formülasyon (Tip-2) doğrulamasında durum

- **Derlenmek doğruluk değildir.** Bir formalizasyonun Lean/Coq'ta tip kontrolünden geçmesi anlamının doğru
  olduğunu göstermez; anlamsal denklik ayrıca kontrol edilmelidir.
  — [Autoformalization in the Era of LLMs: A Survey (arXiv 2505.23486)](https://arxiv.org/pdf/2505.23486)
- **Ölçek:** IndiMathBench'te derlenen formalizasyonların yalnızca ~%11.5'i insan yazımı referansla eşdeğer çıkmış.
  — [IndiMathBench (Microsoft Research)](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/IndiMathBench_MS_hosting.pdf)
- **VERGE (2026):** Cevap atomik iddialara ayrılır; matematik/mantık iddiaları SMT'ye, belirsiz olanlar LLM
  konsensüsüne gider. İddia başına K=3 formalizasyon; iki aday yalnızca Z3 iki yönlü eşdeğerliği (`¬(F1⇔F2)` unsat)
  doğrularsa aynı grupta sayılır; en büyük grup ≥⌈K/2⌉ ise kabul. Hata yeri Minimal Correction Set ile bulunur.
  Sınırlar: QF_UF/QF_LIA dışı (doğrusal olmayan, kuantörlü) iddialar yumuşak doğrulamaya düşüyor; ~20B altı
  modeller yalnızca ~%30 kullanılabilir SMT kodu üretiyor; iterasyon başına 15–30 sn.
  — [VERGE (arXiv 2601.20055)](https://arxiv.org/html/2601.20055v2)
  → **Rigor farkı:** çoğunluk yerine oybirliği (K2); ayrışma kullanıcıya soru olur.
- **Roundtrip doğrulama ve onarım (2026, özetten):** formüle et → doğal dile geri çevir → yeniden formüle et →
  denklik kontrolü; uyuşmazlıkta hangi aşamanın bozulduğunu teşhis edip yalnızca onu onarıyor. Uyuşmazlık,
  anlam kaymasıyla (NLI drift) 1.4–2.5 kat ilişkili. Claude Opus 4.6 ve GPT-5.2 ile, iki yasal metin alanında test.
  — [Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031)](https://arxiv.org/abs/2604.25031)
- **SOVER (EMNLP 2026 Findings, özetten):** iki optimizasyon formülasyonunun eşdeğerliğini sertifikalar. LLM yalnızca
  değişken eşlemesini önerir; doğrusal karma tamsayıda Z3, sürekli doğrusal olmayanda dReal ile uygunluk ve amaç
  sıralaması karşı örneği aranır. NLEquiv-150'de 149/150; tek hata eksik eşleme çıkarımı.
  — [SOVER (arXiv 2609.00728)](https://arxiv.org/abs/2609.00728)
  → **Rigor dersi:** değişken hizalaması belirsizse tahmin değil, soru.
- **Diğerleri:** [VeriSimpl (arXiv 2607.20474)](https://arxiv.org/pdf/2607.20474) — optimizasyon modellerinde ince
  anlamsal hatalar için çözücüyle sadeleştirilmiş tanı sorguları;
  [Autoformulation (arXiv 2411.01679)](https://arxiv.org/pdf/2411.01679) — SMT ile kısıt kümesi denkliği;
  [FormalMATH (arXiv 2505.02735)](https://arxiv.org/pdf/2505.02735) — çoklu LLM anlamsal doğrulama + olumsuzlama ile çürütme filtresi;
  [Symbolic equivalence & semantic consistency (arXiv 2410.20936)](https://arxiv.org/pdf/2410.20936).

**Sonuç:** Tip-2 için hiçbir yöntem garanti vermiyor; en güçlü pratik kombinasyon = bağımsız çoklu formülasyon +
solver tabanlı denklik + roundtrip + insan onayı. Rigor'un etiket sistemi bu yüzden var.

## 2. Açıklamaların (anlatımın) sadakati

- Theorem prover ile açıklama doğrulama: [Explanation-Refiner (EMNLP 2024)](https://aclanthology.org/2024.emnlp-main.172.pdf),
  [Faithful-Refiner (ACL 2025)](https://aclanthology.org/2025.acl-long.867.pdf). Uyarı: prover başarısı yalnızca
  formalize edilmiş açıklamanın geçerli olduğunu gösterir, formalizasyonun sadık olduğunu değil.
  — [Pith review](https://pith.science/paper/2505.24264)
- [Logic-LM](https://aclanthology.org/2023.findings-emnlp.248.pdf): çözücü sonucunu doğal dile çeviren yorumlayıcı.
- [FaithLM (arXiv 2402.04678)](https://arxiv.org/html/2402.04678): sadakat = içerik çelişkilendirildiğinde tahminin değişmesi.
- Doğrudan "çözücü izinden üretilen açıklamada halüsinasyon oranı" ölçen 2025–26 çalışması bulunamadı.
  → **Rigor tasarımı:** deterministik iskelet + LLM sadeleştirme + sayı/birim/karşılaştırma koruması + anlam roundtrip'i.
- **Türkçe okunabilirlik:** Ateşman (1997, Flesch uyarlaması; 70–89 "kolay", 90–100 "çok kolay"),
  Bezirci-Yılmaz (2010), Çetinkaya-Uzun (2010). Formüller aynı metne farklı seviyeler verebiliyor.
  — [DergiPark 1942363](https://dergipark.org.tr/en/download/article-file/1942363),
  [DergiPark 4334687](https://dergipark.org.tr/tr/download/article-file/4334687)

## 3. Sayısal kesinlik

- **Arb / python-flint:** top (mid-rad aralık) aritmetiği; her değere hata sınırı eklenir, hata analizi otomatikleşir.
  Kesin hata sınırlı sayısal integral ve aralıkta kök izolasyonu var.
  — [FLINT feature overview](https://flintlib.org/doc/overview.html), [arb_calc](https://arblib.org/arb_calc.html),
  [Arb ile sayısal integral (arXiv 1802.07942)](https://arxiv.org/pdf/1802.07942)
- **Doğrulanmış (validated) ODE çözücü:** Python'da hazır, bakımlı bir seçenek bulunamadı. → ODE sonuçları
  `CROSS_VALIDATED` ile sınırlı.
- **dReal:** δ-tamamlı SMT (unsat ya da δ-sat), her iki sonuç için sertifika; pip ile kurulur ama IBEX/CLP sistem
  kütüphanesi ister; dokümanlar ~2023. Opsiyonel.
  — [dreal4](https://github.com/dreal/dreal4), [dReal (CADE-24)](https://www.doi.org/10.1007/978-3-642-38574-2_14)

## 4. Kod denetimi (Mod B)

- **CrossHair:** tip açıklamalı fonksiyonları sembolik girdilerle çağırıp SMT ile karşı örnek arar; iki fonksiyon
  arasındaki davranış farkını bulabilir; Hypothesis'e `backend="crosshair"` ile arka uç olarak bağlanır.
  `Decimal` desteği doğrulanmadı — uygulamada küçük bir deneyle test edilmeli.
  — [crosshair](https://github.com/pschanely/crosshair), [hypothesis-crosshair](https://github.com/pschanely/hypothesis-crosshair)
- **Kişisel kripto alım-satım botu (özel repo, 2026-11-07'de incelendi):** para hesaplarında `Decimal`; fail-closed,
  köken (provenance) etiketli ücret modeli; bağımsız bir muhasebe denetçisi var (henüz kısmi). Spot, kaldıraçsız.
  Henüz onaylı strateji yok. Kimliği belirleyen ayrıntılar `docs/private/` altında (repoya girmez).

## 5. Roket

- **RocketPy:** uçuş verisiyle doğrulama örnekleri — NDRT apogee −%0.75, Bella Lui +%0.45; Juno III'te ~%5.8 fark
  (yalnızca drogue paraşüt açılmış). `FlightComparator` ile OpenRocket/RASAero karşılaştırması. Rakamlar projenin
  kendi dokümanından; bağımsız değerlendirme bulunamadı.
  — [RocketPy](https://github.com/rocketpy-team/RocketPy)
  → **Rigor dersi:** bu farkların çoğu fiziksel model/olay farkıdır, matematik hatası değil → kapsam dışı, raporda uyarı.

## 6. Mevcut araçların durumu

| Araç | Durum (2026-11) | Rigor için anlamı |
|---|---|---|
| `morluto/jacobian` | Aktif, v0.23.0; SymPy/NetworkX/Z3/Python-FLINT; `math.find`/`math.run`; CPython 3.12–3.13 | İşlem sözlüğü olarak değerlendirilebilir; birim/DoF/formülasyon yok — [README](https://raw.githubusercontent.com/morluto/jacobian/main/README.md) |
| `sdiehl/usolver` | Arşivlenmiş, bakım yok | Yalnızca referans — [listing](https://www.juheapi.com/mcp-servers/sdiehl/usolver) |
| `sdiehl/sympy-mcp` | Durumu belirsiz; `parse_expr` (eval) kullanıyor | Güvenlik nedeniyle kullanılmaz — [listing](https://www.scriptbyai.com/sympy-mcp/) |

## 7. MCP

- **Python SDK:** PyPI'da `mcp` 2.3.0 (2026-11-07 kontrol). v2 dokümanları elicitation'ı ve 2026-07-28 protokolünü anlatıyor.
  — [py.sdk.modelcontextprotocol.io](https://py.sdk.modelcontextprotocol.io/v2/llms-full.txt)
- **Elicitation (sunucu kullanıcıdan yapılandırılmış girdi ister):** Claude Code v2.1.76'da (2026-03-14) eklendi —
  ikincil kaynaklardan; bir sürümde capability'nin ilan edilmediğine dair kapanmış bir hata kaydı var.
  — [changelog mirror](https://claude-code-changelog-web.pages.dev/releases/v2.1.76),
  [issue mirror](https://claudeissues.com/issue/65572-claude-code-does-not-advertise-elicitation-mcp-capability-despite-elicitation-ho)
- **Sampling (sunucu istemcinin LLM'ini kullanır):** Claude Code'da desteklendiği doğrulanamadı; açık özellik isteği var.
  — [anthropics/claude-code#1785](https://github.com/anthropics/claude-code/issues/1785)

## 8. PyPI sürümleri (2026-11-07)

mcp 2.3.0 · z3-solver 5.3.3.0 · sympy 1.14.0 · pint 0.26.2 (≥3.12) · python-flint 0.9.0 · hypothesis 6.170.15 ·
crosshair-tool 0.0.113 · highspy 1.15.1 · cvxpy 1.9.3 · mpmath 1.4.1 · networkx 3.7 (≥3.12) · pydantic 2.14.3 ·
rocketpy 1.13.0 · dreal 4.21.6.2 · jacobian 0.23.0 (3.12–3.13) · anthropic 2.6.0 · openai 3.46.0 · google-genai 3.0.0

## 9. TEKNOFEST 2026 şartnamesinin Red Team incelemesi

Kaynak: `OneDrive/.../Roket Takımı/Yarışma Şartnameleri` (şartname PDF + EK-1…EK-14 + kütle bütçesi + motor verileri).
Tam matematik envanteri tasarım belgesi §5.3'te. Burada yalnızca **bulgular** var.

### 9.1. Kapsamı belirleyen gerçekler
- Asgari irtifalar **ft** (A2 8.000 ft, A3 15.000 ft), rampa çıkış hızları **m/s** (A2 25 m/s), iniş hızları m/s,
  kütleler g/kg → birim karışması gerçek bir risk; birim kapısı zorunlu.
- Hedef irtifaya ±%15 tolerans (3.2.19); 0,3 Mach'ta statik marjin 1,5–2,5 (4.4.5); 85° rampa açısı (4.1.35);
  görev yükü ≥ 4,0 kg ve OpenRocket'ta "PAYLOAD" adıyla tek parça (4.1.33); OpenRocket verileri raporlarla aynı olmalı (4.1.32).
- Motorlar: A1 L1256, A2/A4 M1850, A5 N3300 + L1256 (4.1.18–4.1.21).

### 9.2. EK-1 kuaterniyon çarpım formülü **yanlış** (kanıtlandı)
- EK-1'de Hamilton çarpımı `a⊗b = [s_a·s_b − V_a·V_b ; s_a·V_a + s_b·V_b + V_a×V_b]` olarak yazılmış
  (DOCX'in matematik XML'inden doğrulandı, metin çıkarma hatası değil).
- Doğrusu: vektör kısmı `s_a·V_b + s_b·V_a + V_a×V_b`.
- **Karşı örnek:** `a = (1, 0,0,0)` birim kuaterniyon, `b = (0, 1,0,0)`. Birimle çarpım `b`'yi değiştirmemeli;
  EK-1 formülü vektör kısmını `(0,0,0)` verir, doğrusu `(1,0,0)`.
- Kanıt betiği: [`evidence/ek1_kuaterniyon_dcm_kontrol.py`](evidence/ek1_kuaterniyon_dcm_kontrol.py) (SymPy'nin
  `Quaternion` cebiriyle sembolik karşılaştırma).
- **Takım için anlamı:** UKB'de veya simülasyonda bu formül kopyalanırsa yönelim hesabı yanlış olur.

### 9.3. EK-1'deki iki kavramsal hata (formülleri etkilemiyor)
- "DCM θ=90°'de kilitlenir": DCM'in kendisi θ=90°'de tanımlı ve ortogonal kalıyor (sembolik kontrol). Bu açıda DCM
  yalnızca `φ−ψ` farkına bağlı oluyor, yani tekillik **DCM'den Euler açılarını geri çıkarırken** (ve Euler açısı
  kinematik denklemlerinde) ortaya çıkıyor.
- "α/2, θ=90° sorununu önlemek için kullanılır": yanlış gerekçe. Yarım açı `q⊗v⊗q*` çarpımının iki taraflı
  olmasından gelir. Kuaterniyonlar kilitlenmeyi üç ardışık açı kullanmadıkları için önler.
- DCM'in kendisi (`Rx·Ry·Rz`, ZYX, pasif dönüşüm, `C_eb = C_beᵀ`) **doğru** ve MATLAB `angle2dcm(ψ,θ,φ,'ZYX')` ile tutarlı.

### 9.4. Eksen tanımında belirsizlik (soru üretir)
- EK-1 gövde z eksenini "yere doğru", EK-7 ise gövde eksen takımında "pozitif yönü yeryüzüne doğru" olarak tanımlıyor.
  Gövdeye sabit bir eksen her an yere bakamaz (roket dikeyken gövde z ekseni yataydır). Uçak geleneği (seviye uçuşta
  z aşağı) kastediliyor olabilir. SİT/SUT testlerinde ivme işaretlerini etkileyebileceği için Rigor bunu
  kullanıcıya soru olarak getirmelidir (komiteye de sorulabilir).

### 9.5. Motor verisi denetimi (sorun yok)
- Komite tablosu yakıt kütlesindeki ölçüm farkı oranıyla (M1850: (4103−3951)/3951 = %3,847) **zaman eksenini**
  ölçekliyor, itki değerlerini aynı bırakıyor. Toplam impuls 7365,9 → 7649,28 N·s. Rigor kesin rasyonel trapezle
  aynı değerleri buldu.
- Bu bir **modelleme varsayımıdır** (sabit Isp, aynı itki seviyesi, daha uzun yanma). Rigor bunu onay anlatımında
  varsayım olarak göstermelidir.
- `Teknofest26_M1850_Rev1.eng`: başlık `TFM1850W 75 935.4 1000 4.103 7.010 Teknofest26`, yani ölçülen kütlelerle
  tutarlı. Zamanlar 3 ondalığa yuvarlanmış. Yalnızca CR satır sonu var.

## 10. Python 3.15 Red Team incelemesi

- PEP 810 (explicit lazy imports) **Final**, hedef 3.15; `lazy import x` / `lazy from x import y`. Yalnızca modül
  düzeyinde, `try` dışında, yıldızlı import yok. `-X lazy_imports=all|normal|none`, `sys.set_lazy_imports_filter`,
  `__lazy_modules__` (eski sürümlerde yok sayılır). Hatalar ve yan etkiler ilk kullanıma ertelenir.
  — [PEP 810](https://peps.python.org/pep-0810/)
- 3.15.0, 2026-10-09'da yayımlandı (ikincil kaynaklar; ilk hedef 2026-10-01 idi).
  — [Real Python, Ekim 2026](https://realpython.com/python-news-october-2026/),
  [linuxcompatible](https://www.linuxcompatible.org/story/python-3150-is-out-lazy-imports-frozendict-and-faster-speeds/)
- **macOS arm64 cp315 wheel durumu (PyPI, 2026-11-07):**
  - Var: numpy 2.5.4, scipy 1.18.1, pydantic-core 2.50.4, scs 3.3.1, crosshair-tool 0.0.113, netCDF4.
  - Sürümden bağımsız (sorun yok): z3-solver (py3 wheel), clarabel (abi3), sympy, mpmath, pint, networkx, mcp, rocketpy.
  - **Yok:** python-flint 0.9.0 (yalnızca cp313/cp314), highspy 1.15.1, cvxpy 1.9.3, osqp 1.1.3, ecos, cantera 3.2.0.
  - **Uyumsuz:** jacobian 0.23 (`<3.14`).
- Yerelde: uv, CPython 3.15'i yalnızca `3.15.0a7` olarak listeliyor (uv sürümü eski olabilir); 3.14.3 ve 3.12.16 kurulu.

## 11. OmniRoute Red Team incelemesi (2026-11-07)

Depo: [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute), son commit 2026-11-06, v3.8.54, MIT,
~27.700 dosya (TypeScript/Next.js, Electron). Bulgular depodaki belgelerden okundu; kod çalıştırılmadı.

- **Ne yapıyor:** 380 sağlayıcıyı `localhost:20128/v1` altında OpenAI/Claude/Gemini uyumlu tek uç noktada topluyor;
  20 yönlendirme stratejisi, 4 katmanlı otomatik yedekleme (Abonelik → API → Ucuz → Ücretsiz), istem sıkıştırma,
  semantik önbellek, bellek, MCP (110 araç), A2A.
- **Semantik yanıt önbelleği:** `SEMANTIC_CACHE_*` ayarları "Max cached temperature=0 responses" diye tanımlı
  (`docs/reference/ENVIRONMENT.md`). → Aynı istemle yapılan "bağımsız" formülasyonlar tek bir önbellek yanıtına
  dönüşebilir.
- **Sıkıştırma:** "Default stacked combo runs RTK → Caveman"; istek içeriği şeffafça değiştiriliyor; uygulanan plan
  `X-OmniRoute-Compression` yanıt başlığında; istek başına `x-omniroute-compression` başlığıyla kontrol edilebiliyor.
- **Yönlendirme şeffaflığı:** Her yanıtta `X-OmniRoute-Decision` başlığı strateji/sağlayıcıyı bildiriyor → Rigor
  bunu doğrulamak için kullanabilir.
- **Abonelik köprüleri:** `claude` (Claude Code OAuth), `codex` (OpenAI Codex OAuth), `github` (Copilot OAuth),
  `agy` (Antigravity) sağlayıcıları; README'de "TLS stealth", ChatGPT Web → Codex köprüsü, "Claude Code-compatible
  transform defaults and billing-header behavior" ifadeleri.
- **ToS çelişkisi:** README: "Providers marked `tos: avoid` … are excluded from automatic routing by default".
  `docs/reference/FREE_TIERS.md` §140: "ToS flag is advisory, not a routing gate … still included in routing and
  combo/fallback by default". Katalog Antigravity'nin ToS'unun proxy üzerinden OAuth kullanımını yasakladığını,
  Gemini ücretsiz katmanı için "caution" notunu kendisi yazıyor.
- **Anthropic politikası (ikincil kaynaklar):** Free/Pro/Max OAuth token'ları yalnızca Claude Code ve Claude.ai için;
  üçüncü taraf araçlarda (bazı kaynaklara göre Agent SDK dahil) yasak; Ocak 2026'da teknik engelleme, Şubat 2026'da
  belge güncellemesi. — [The Register](https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access),
  [WinBuzzer](https://winbuzzer.com/2026/02/19/anthropic-bans-claude-subscription-oauth-in-third-party-apps-xcxwbn/),
  [AlternativeTo](https://alternativeto.net/news/2026/2/anthropic-officially-bans-using-subscription-authentication-for-third-party-claude-use)
  → Birincil metin (Claude Code "Legal and Compliance" sayfası, Consumer Terms) uygulamadan önce okunmalı.

## 12. Abonelikleri resmi CLI'larla kullanmak

Sahibin makinesinde kurulu (2026-11-07): Claude Code 2.1.302, codex-cli 0.167.0, Gemini CLI 0.64.0.

| CLI | Headless | Yapılandırılmış çıktı | İzolasyon bayrakları (yardım metninden) |
|---|---|---|---|
| `claude` | `-p/--print` | `--json-schema <schema>`, `--output-format` | `--tools`, `--strict-mcp-config`, `--setting-sources`, `--system-prompt`, `--no-session-persistence`, `--model` (`--fallback-model` kullanılmamalı) |
| `codex exec` | evet | `--output-schema <FILE>`, `--json`, `-o` | `-s/--sandbox`, `--ephemeral`, `--skip-git-repo-check`, `-m` |
| `gemini` | `-p/--prompt` | `-o json` | `--approval-mode plan` (salt-okunur), `-s/--sandbox`, `-m` |

Açık konular: her CLI'ın kullanıcı global talimat/bellek dosyalarını (ör. `~/.claude/CLAUDE.md`) bu modda yükleyip
yüklemediği deneyle doğrulanmalı. Yanıttaki gerçek model kimliğinin nasıl okunacağı her CLI için belirlenmeli.

## 13. Groq ücretsiz katmanı (ikincil kaynaklar)

- Sınırlar model başına; örnek `openai/gpt-oss-120b`: 30 istek/dk, 1.000 istek/gün, 8.000 token/dk, 200.000 token/gün.
  Kaynaklar arasında farklı rakamlar var; yetkili kaynak hesabın konsol sayfası.
  — [benchlm](https://benchlm.ai/md/free-tier/groq.md), [Groq community](https://community.groq.com/t/what-are-the-rate-limits-for-the-groq-api-for-the-free-and-dev-tier-plans/42)
- Veri: hizmet sözleşmesine göre girdiler/çıktılar açık izin olmadan eğitimde kullanılmıyor; loglar 30 güne kadar; ZDR
  açılabiliyor (üçüncü taraf özeti). — [aireiter](https://aireiter.com/blog/best-free-ai-api), [eesel](https://eesel.ai/blog/groq-pricing)
- Aile çeşitliliği: Groq'taki açık ağırlıklı modeller farklı kuruluşlardan (Meta Llama, Alibaba Qwen, OpenAI gpt-oss,
  Moonshot Kimi) → Red Team bağımsızlığı için değerli. VERGE bulgusu hatırlatma: ~20B altı modeller kullanılabilir SMT
  çıktısını yalnızca ~%30 oranında üretiyor; formülatör olarak büyük modeller seçilmeli.

## 14. Kripto botu formül envanteri (2026-11-07; anonim)

Sahip kararı K20: bot kodu denetlenmez, yalnızca matematik kontrol edilir. Envanter için botun istatistik, maliyet
ve muhasebe protokol belgeleri okundu (yollar ve sürüm `docs/private/` altında).

| Formül | Botun yazdığı | Literatürle ön kontrol |
|---|---|---|
| Günlük basit getiri | `r_t = equity_t / equity_(t-1) − 1` | Standart |
| Sharpe | ortalama / örneklem std (ddof=1), risksiz oran 0 | Standart |
| Yıllıklandırma | `× √365.25` (yalnızca betimleyici) | Kripto 7/24 için tutarlı |
| Beklenen maks. Sharpe | `√V·((1−γ)Φ⁻¹(1−1/N) + γΦ⁻¹(1−1/(N·e)))` | Bailey & López de Prado ile aynı |
| DSR | `Φ((SR−SR0)·√(T−1) / √(1 − skew·SR + (kurt−1)/4·SR²))`, kurtosis ham (fazlalık değil) | Makaledeki formülle aynı; ham kurtosis doğru seçim |
| PBO | CSCV, `ω = rank/(N+1)`, `λ = ln(ω/(1−ω))`, PBO = λ ≤ 0 oranı | Bailey vd. ile uyumlu |
| SPA | `max(max_k √T·mean(d_k)/ω_k, 0)`, durağan bootstrap | Hansen (2005) ile uyumlu |
| Ücret | oran × kote nominal; alışta baz, satışta kote varlıkta | Borsa belgesiyle uyumlu (botun kendi kaynağı) |

Bot henüz hazır olmadığı için deneme sayısıyla ilgili bir nokta ertelendi (ayrıntı `docs/private/`).

## 15. Sentinax ön inceleme (2026-11-07, commit `1257e81`, public repo)

Hedef K21: canlıya almadan matematiksel doğruluk. 810 dosya, `backend/engine` ~63.600 satır. Bu ön inceleme
**örneklemedir** (tam tarama değil): Buffett motoru, TEFAS getiri/düşüş modülleri, Bayes sonsalının başlığı okundu.

| Yer | Bulgu | Tür |
|---|---|---|
| `backend/engine/buffett/valuation.py` `DCFValuation.__init__` | `risk_free_rate=0.25`, `equity_risk_premium=0.08`, `terminal_growth=0.15` parametreleri alınıyor ama **hiç kullanılmıyor**; gerçekte sabit `WACC = 0.12` ve terminal büyüme `0.03` kullanılıyor. Çağıran parametre verdiğini sanıp farklı bir hesap alır. | Formül/girdi uyuşmazlığı |
| aynı dosya, `evaluate` | `owner_earnings = max(FCF, 0.70·net_income)`. Yorum "FCF negatifse ya da büyüme yatırımıyla baskılanmışsa net kârı kullan" diyor; `max` ise her zaman ikisinden **iyimser olanı** seçiyor. İç değer ve güvenlik marjı sistematik olarak yukarı kayar; "muhafazakâr iç değer" iddiasıyla çelişir. | Tip-2 (niyet ≠ formül) |
| `backend/engine/buffett/llm_integration.py` → `orchestrator.py:63` | Moat puanı LLM'den değil **sabit kodlu bir sözlükten** geliyor (BIMAS 8, AKBNK 4, THYAO 7, diğer her şirket 5,0) ve tek aktif router olan `/buffett` yolunda kullanılıyor. Kaynağı olmayan bir sayı yayımlanan puana giriyor; README'deki "veri uydurma yasaktır" ilkesiyle çelişir. | Kaynaksız girdi |
| Buffett motoru genel | `float` aritmetiği; özel motor (`engine/private`) ise `Decimal` ve kanonik yeniden hesap kullanıyor. İki bağlam arasında sayısal semantik farklı. | Not |
| `fund_annualized_returns.py` | `(1+R)^(12/H) − 1`, yalnızca 12/36/60 ay; doğru. | Uyumlu |
| `fund_drawdown.py` + Calmar | Maks. düşüş `1 − fiyat/zirve`, `[0,1]` büyüklük; Calmar = yıllık getiri / maks. düşüş, işaret doğru. | Uyumlu |
| `allocation_user_view_posterior.py` | Black-Litterman benzeri sonsal, Joseph karekök formu, LDLᵀ ile çözüm (ters alma yok). Formüllerin referansla denkliği **henüz kontrol edilmedi**; B1'in ilk adaylarından. | Kontrol edilecek |
