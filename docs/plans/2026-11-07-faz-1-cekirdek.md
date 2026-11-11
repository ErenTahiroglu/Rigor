# Faz 1 — Çekirdek Implementation Plan

> **Eskidi (2026-11-11) — bu planla kod yazılmaz.** Plan eski üç etiketli sözleşmeyi kuruyor (karar kaydı B-8). Yeni
> mimari ([`../design/2026-11-11-rigor-mimari.md`](../design/2026-11-11-rigor-mimari.md)) ve faz planına
> ([`2026-11-11-rigor-faz-plani.md`](2026-11-11-rigor-faz-plani.md)) göre F0'da yeniden yazılacak. Yeni planda F1
> (çekirdek güven tabanı) ve F2 (arayüzler ve onay) bu planın kapsamını ikiye böler.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Elle kurulan (veya ajanın gönderdiği) tipli bir IR'ı birim, yapı ve alan kapılarından geçirip, kullanıcı onayıyla, iki bağımsız yoldan çözen, sertifikalandıran ve etiketli kanıt raporu üreten alandan bağımsız çekirdeği; ince bir MCP kabuğunu ve `rigor doctor`'ı kurmak.

**Architecture:** `src/rigor/core` alandan bağımsızdır ve yalnızca çekirdek bağımlılıkları içe aktarır (yol haritası §1). IR Pydantic v2 ile, `eval` olmadan; sayılar kesin `Fraction`. Motorlar: SymPy (kesin cebir), Z3 (tutarlılık, ∀, teklik), python-flint Arb (aralık değerlendirme). Faz 1'de Red Team yoktur, bu yüzden her sonuç en fazla `CROSS_VALIDATED`'dir (spec §4.4).

**Tech Stack:** Python ≥3.12 (geliştirme 3.15), uv, pydantic 2.14, sympy 1.14, z3-solver 5.3.3, python-flint 0.9 (abi3), pint 0.26 (`non_int_type=Fraction`), networkx 3.7, mpmath 1.4, hypothesis 6.170, mcp 2.3 (`MCPServer`), pytest.

**Spec:** [`docs/design/2026-11-07-rigor-design.md`](../design/2026-11-07-rigor-design.md) — Faz 1 = §10 madde 1. Yol haritası: [`2026-11-07-rigor-yol-haritasi.md`](2026-11-07-rigor-yol-haritasi.md).

## Global Constraints

- `requires-python = ">=3.12"`; geliştirme 3.15; CI 3.12 / 3.14 / 3.15 (spec §8.1, K11).
- Kaynak kodda `lazy` anahtar kelimesi yok; ağır modüller `__lazy_modules__` listesinde (K11).
- LLM çıktısı veya kullanıcı metni asla `eval` / `exec` / `sympy.parse_expr` / `sympify(str)` ile işlenmez (A3). İfadeler yalnızca IR ağacından derlenir.
- Sayılar kesin: girdiler `str | int | Fraction`; `float` her yerde `TypeError` (A2, K4).
- Her büyüklük ya bir birim ya da açıkça `"dimensionless"` taşır; `unit=None` her zaman soru üretir (spec §6.3).
- `rigor.core` → `rigor.domains | rigor.llm | rigor.mcp | rigor.templates | rigor.lean | rigor.finance` içe aktaramaz (K24).
- Faz 1'de `decide_label` hiçbir zaman `PROVEN` döndüremez çünkü `red_team="not_applied"` (spec §4.4); `PROVEN` için ayrıca onay `USER_DIRECT` olmalıdır (spec §4.3).
- Bağımlılık lisansları: yalnızca MIT/BSD/Apache-2.0/PSF/MPL-2.0 veya dinamik LGPL; GPL yok (spec §8.3).
- Varsayılan anlatım dili Türkçe; İngilizce `lang="en"` (spec §6.7).
- Çalışma dalı `development`; `main`'e doğrudan commit yok (spec §8.4). Bota ait kimlik bilgisi hiçbir izlenen dosyaya girmez.
- Commit sonu: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## Review Focus

1. **`float` girdisi** (`given("m", 0.1, "kg")`): sessizce `0.1000000000000000055…` olmamalı → `TypeError`. Test: Görev 4.
2. **Ondalık virgül** (`"0,1"`): Türkçe kullanıcı için `1` veya `1/10` diye tahmin edilmemeli → `AmbiguousNumberError`. Test: Görev 2.
3. **Ofsetli birimle çarpma** (`25 degC * 2`): pint istisnasıyla çökmemeli → `offset_unit_misuse` kapı sorunu. Test: Görev 5.
4. **Birden çok kök** (`x² = 4`): Rigor kök seçmemeli (Tip-2) → `NEEDS_INPUT` + aday listesi; kısıt eklenince tek kök. Test: Görev 11.
5. **Kurcalanmış oturum dosyası**: sessizce devam etmemeli → `SessionIntegrityError`. Test: Görev 14.

---

### Task 1: Proje iskeleti, ortam, CI, çekirdek bağımlılık kuralı

**Files:**
- Create: `pyproject.toml`, `src/rigor/__init__.py`, `src/rigor/core/__init__.py`, `.github/workflows/ci.yml`, `tests/test_architecture.py`, `.python-version`

**Interfaces:**
- Produces: paket `rigor` (`rigor.__version__ == "0.1.0.dev0"`), konsol betikleri `rigor = "rigor.cli:main"` ve `rigor-mcp = "rigor.mcp.server:main"` (Görev 16 ve 18 doldurur).

- [ ] **Step 1: Ortamı hazırla**

Run: `uv self update && uv python install 3.15 && uv python list | grep 3.15`
Expected: `cpython-3.15.x-macos-aarch64-none` kurulu satırı (alfa değil; araştırma notları §16).

- [ ] **Step 2: `pyproject.toml` ve `.python-version` (`3.15`) yaz**

Değerler: `name = "rigor"`, `version = "0.1.0.dev0"`, `requires-python = ">=3.12"`, `license = "LicenseRef-PolyForm-Noncommercial-1.0.0"`, `license-files = ["LICENSE"]`; bağımlılıklar `pydantic>=2.14,<3`, `sympy>=1.14`, `z3-solver>=5.3.3`, `python-flint>=0.9`, `pint>=0.26`, `networkx>=3.7`, `mpmath>=1.4`, `hypothesis>=6.170`, `mcp>=2.3,<3`; dev grubu `pytest>=8`; build backend `hatchling`; `src` düzeni; pytest `testpaths = ["tests"]`.

- [ ] **Step 3: Mimari testini yaz (başarısız olmalı)**

```python
# tests/test_architecture.py
import ast, pathlib, sys, subprocess
FORBIDDEN = ("rigor.domains", "rigor.llm", "rigor.mcp", "rigor.templates", "rigor.lean", "rigor.finance")

def test_core_never_imports_outer_layers():
    core = pathlib.Path("src/rigor/core")
    assert core.is_dir()
    for f in core.rglob("*.py"):
        for node in ast.walk(ast.parse(f.read_text(encoding="utf-8"))):
            names = [a.name for a in node.names] if isinstance(node, ast.Import) else \
                    [node.module or ""] if isinstance(node, ast.ImportFrom) else []
            assert not any(n.startswith(FORBIDDEN) for n in names), (f, names)

def test_version():
    import rigor
    assert rigor.__version__ == "0.1.0.dev0"

def test_lazy_import_keeps_sympy_unloaded_on_315():
    if sys.version_info < (3, 15):
        return
    out = subprocess.run([sys.executable, "-c", "import rigor, sys; print('sympy' in sys.modules)"],
                         capture_output=True, text=True, check=True)
    assert out.stdout.strip() == "False"
```

- [ ] **Step 4: Çalıştır, başarısız olduğunu gör**

Run: `uv run pytest tests/test_architecture.py -v`
Expected: FAIL (`src/rigor/core` yok / `rigor` içe aktarılamıyor).

- [ ] **Step 5: `src/rigor/__init__.py` ve `src/rigor/core/__init__.py` oluştur**

`__init__.py` içinde `__version__ = "0.1.0.dev0"` ve `__lazy_modules__ = ["sympy", "z3", "flint", "pint", "networkx", "mpmath"]`; genel API yeniden dışa aktarımları sonraki görevlerde eklenir (Görev 4, 14).

- [ ] **Step 6: CI iş akışı**

`.github/workflows/ci.yml`: `push` ve `pull_request` (dallar `development`, `main`); matris `os: [macos-latest, ubuntu-latest]`, `python: ["3.12", "3.14", "3.15"]`; adımlar `astral-sh/setup-uv`, `uv python install ${{ matrix.python }}`, `uv sync --python ${{ matrix.python }}`, `uv run pytest -q`, `uv run rigor doctor` (Görev 16'dan sonra yeşil olur; o zamana kadar `continue-on-error: true` ile bu adım işaretli).

- [ ] **Step 7: Testleri geçir ve commit et**

Run: `uv run pytest tests/test_architecture.py -v` → Expected: PASS (3.15'te lazy testi de PASS).

```bash
git add pyproject.toml .python-version src tests .github
git commit -m "Faz 1: proje iskeleti, CI ve çekirdek bağımlılık kuralı"
```

---

### Task 2: Kesin sayılar

**Files:**
- Create: `src/rigor/core/numbers.py`, `tests/core/test_numbers.py`

**Interfaces:**
- Produces: `parse_exact(text: str | int | Fraction) -> Fraction`; `class AmbiguousNumberError(ValueError)`; `NumberDomain = Literal["integer", "rational", "real", "decimal"]`; `format_exact(x: Fraction) -> str` (`"12192/5"`, tamsayıda `"36"`).

- [ ] **Step 1: Testleri yaz**

```python
from fractions import Fraction
import pytest
from rigor.core.numbers import parse_exact, format_exact, AmbiguousNumberError

@pytest.mark.parametrize("text,expected", [
    ("0.1", Fraction(1, 10)), ("1/3", Fraction(1, 3)), ("-2.50", Fraction(-5, 2)),
    ("1e3", Fraction(1000)), ("1.5e-3", Fraction(3, 2000)), (7, Fraction(7)), (Fraction(2, 3), Fraction(2, 3)),
])
def test_parse_exact(text, expected):
    assert parse_exact(text) == expected

def test_float_rejected():
    with pytest.raises(TypeError):
        parse_exact(0.1)

def test_decimal_comma_is_ambiguous():
    with pytest.raises(AmbiguousNumberError):
        parse_exact("0,1")

@pytest.mark.parametrize("bad", ["nan", "inf", "-inf", "", "1/0", "abc", "1.2.3"])
def test_invalid(bad):
    with pytest.raises(ValueError):
        parse_exact(bad)

def test_bool_rejected():
    with pytest.raises(TypeError):
        parse_exact(True)

def test_format_exact():
    assert format_exact(Fraction(12192, 5)) == "12192/5"
    assert format_exact(Fraction(36)) == "36"
```

- [ ] **Step 2: Çalıştır** → `uv run pytest tests/core/test_numbers.py -v` → FAIL (modül yok).
- [ ] **Step 3: Uygula.** `Fraction(str)` kullan; önce `,` kontrolü (`AmbiguousNumberError`, mesajda "ondalık ayırıcı olarak nokta kullan"); `bool`/`float` için `TypeError`; sonsuz/NaN için `ValueError`.
- [ ] **Step 4: Çalıştır** → PASS.
- [ ] **Step 5: Commit** — `git commit -m "Faz 1: kesin sayı okuma"`

---

### Task 3: IR düğümleri ve kanonik özet

**Files:**
- Create: `src/rigor/core/ir/__init__.py`, `src/rigor/core/ir/nodes.py`, `src/rigor/core/ir/canonical.py`, `tests/core/test_ir.py`

**Interfaces:**
- Produces (hepsi `pydantic.BaseModel`, `model_config = ConfigDict(frozen=True, extra="forbid")`):
  - `Role = Literal["given", "unknown", "intermediate"]`
  - `SourceRef(kind: Literal["text", "file", "model", "builder"], detail: str)`
  - `Quantity(id: str, name: str, unit: str | None, role: Role, domain: NumberDomain = "real", value: str | None = None, interval: tuple[str, str] | None = None, source: SourceRef)` — `value` ve `interval` birlikte olamaz; `interval` alt ≤ üst (spec §6.2: şema aralıkları baştan destekler; Faz 1 oturumu aralıklı girdiyi `REFUSED UNSUPPORTED_MATH`, ayrıntı "aralıklı girdiler Faz 2'de" ile reddeder — Görev 14'e test eklenir)
  - `OpName = Literal["add","sub","mul","div","pow","neg","sqrt","exp","log","sin","cos","tan","asin","acos","atan","atan2","abs","mod","floor"]`
  - `Num(kind: Literal["num"], value: str)`, `Ref(kind: Literal["ref"], id: str)`, `Op(kind: Literal["op"], op: OpName, args: list[Expr])`, `Expr = Annotated[Num | Ref | Op, Field(discriminator="kind")]`
  - `Relation(id: str, rel: Literal["eq","le","lt","ge","gt","ne"], lhs: Expr, rhs: Expr, source: SourceRef)`
  - Hedefler: `SolveGoal(kind: Literal["solve"], unknowns: list[str])`, `IdentityGoal(kind: Literal["identity"], lhs: Expr, rhs: Expr, over: list[str])`, `ForAllGoal(kind: Literal["forall"], relation_id: str, over: list[str])`, `ConsistencyGoal(kind: Literal["consistency"])`; `Goal` ayrımcı birleşim.
  - `Problem(schema_version: Literal[1] = 1, quantities: list[Quantity], relations: list[Relation], goal: Goal)`
  - `canonical_json(p: Problem) -> str`, `ir_hash(p: Problem) -> str` (SHA-256 hex)

- [ ] **Step 1: Testleri yaz**

```python
import pytest
from pydantic import ValidationError
from rigor.core.ir.nodes import Problem
from rigor.core.ir.canonical import canonical_json, ir_hash

SRC = {"kind": "builder", "detail": "test"}
def q(i, unit="kg", role="unknown", value=None):
    return {"id": i, "name": i, "unit": unit, "role": role, "value": value, "source": SRC}
F_MA = {"quantities": [q("F", "N"), q("m", "kg", "given", "12"), q("a", "m/s**2", "given", "3")],
        "relations": [{"id": "r1", "rel": "eq", "lhs": {"kind": "ref", "id": "F"},
                       "rhs": {"kind": "op", "op": "mul", "args": [{"kind": "ref", "id": "m"}, {"kind": "ref", "id": "a"}]},
                       "source": SRC}],
        "goal": {"kind": "solve", "unknowns": ["F"]}}

def test_valid_problem_roundtrip():
    p = Problem.model_validate(F_MA)
    assert Problem.model_validate_json(canonical_json(p)) == p

def test_hash_is_stable_and_order_independent_of_dict_keys():
    p = Problem.model_validate(F_MA)
    assert ir_hash(p) == ir_hash(Problem.model_validate(dict(reversed(list(F_MA.items())))))
    assert len(ir_hash(p)) == 64

@pytest.mark.parametrize("mutate,msg", [
    (lambda d: d["relations"][0]["lhs"].update(id="X"), "unknown reference"),
    (lambda d: d["quantities"].append(q("F")), "duplicate id"),
    (lambda d: d["relations"][0]["rhs"].update(op="eval"), ""),
    (lambda d: d["relations"][0]["rhs"].update(args=[{"kind": "ref", "id": "m"}]), "arity"),
    (lambda d: d["quantities"][1].update(value="0,5"), ""),
    (lambda d: d["goal"].update(unknowns=["m"]), "not an unknown"),
    (lambda d: d["quantities"][1].update(interval=("11", "13")), "both value and interval"),
    (lambda d: d["quantities"][1].update(value=None, interval=("13", "11")), "lower bound"),
])
def test_invalid_problems_rejected(mutate, msg):
    import copy
    d = copy.deepcopy(F_MA); mutate(d)
    with pytest.raises(ValidationError, match=msg):
        Problem.model_validate(d)
```

- [ ] **Step 2: Çalıştır** → FAIL.
- [ ] **Step 3: Uygula.** `Problem` üzerinde `model_validator(mode="after")`: benzersiz id'ler (büyüklük + ilişki ortak ad alanı), her `Ref` ve hedefteki id çözülür, `SolveGoal.unknowns` rolü `unknown` olan büyüklükler, `ForAllGoal.relation_id` var. Arity: 1 (`neg sqrt exp log sin cos tan asin acos atan abs floor`), 2 (`sub div pow atan2 mod`), ≥2 (`add mul`). `Num.value` ve `Quantity.value` `parse_exact` ile doğrulanır ama `str` olarak saklanır. `canonical_json` = `json.dumps(p.model_dump(mode="json"), sort_keys=True, separators=(",", ":"), ensure_ascii=False)`.
- [ ] **Step 4: Çalıştır** → PASS.
- [ ] **Step 5: Commit** — `git commit -m "Faz 1: tipli IR ve kanonik özet"`

---

### Task 4: Python kurucu API

**Files:**
- Create: `src/rigor/core/ir/builder.py`, `tests/core/test_builder.py`
- Modify: `src/rigor/__init__.py` (dışa aktar: `given, unknown, num, eq, le, lt, ge, gt, ne, sqrt, exp, log, sin, cos, tan, mod, floor, build_problem, build_identity, build_forall`)

**Interfaces:**
- Consumes: Görev 2, 3.
- Produces: `class Q` (büyüklük tutamacı; `+ - * / ** -x` ve sayı ile karışık işlemler `Expr` taşıyan `E` döndürür), `class E`; `given(name: str, value: str | int | Fraction | None, unit: str | None, *, domain: NumberDomain = "real", interval: tuple[str, str] | None = None) -> Q` (`None` = değeri henüz bilinmeyen verilen; soru üretir); `unknown(name: str, unit: str | None, *, domain="real") -> Q`; `num(v) -> E`; `eq/le/lt/ge/gt/ne(a, b) -> RelationDraft`; `build_problem(relations: list[RelationDraft], solve: list[Q]) -> Problem`; `build_identity(lhs, rhs, over: list[Q]) -> Problem`; `build_forall(relation: RelationDraft, over: list[Q]) -> Problem`. Id = ad; ilişki id'leri `r1, r2, …`; `source = SourceRef(kind="builder", detail=<çağrı sırası>)`.

- [ ] **Step 1: Testleri yaz**

```python
import pytest, rigor
from rigor.core.ir.canonical import ir_hash

def test_builder_builds_f_equals_ma():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", "12", "kg"), rigor.given("a", 3, "m/s**2")
    p = rigor.build_problem([rigor.eq(F, m * a)], solve=[F])
    assert [x.id for x in p.quantities] == ["F", "m", "a"]
    assert p.relations[0].rhs.op == "mul" and p.goal.unknowns == ["F"]

def test_float_value_rejected():
    with pytest.raises(TypeError):
        rigor.given("m", 0.1, "kg")

def test_number_mixing_is_exact():
    x = rigor.unknown("x", "dimensionless")
    p = rigor.build_problem([rigor.eq(x * x - 5 * x + 6, 0)], solve=[x])
    assert '"value":"5"' in rigor.core.ir.canonical.canonical_json(p)

def test_same_construction_same_hash():
    def mk():
        x = rigor.unknown("x", "dimensionless")
        return rigor.build_problem([rigor.eq(x ** 2, 4)], solve=[x])
    assert ir_hash(mk()) == ir_hash(mk())

def test_builder_never_evaluates_strings():
    with pytest.raises(TypeError):
        rigor.eq("__import__('os')", 1)
```

- [ ] **Step 2: Çalıştır** → FAIL. **Step 3: Uygula** (operatörler yalnızca `Q | E | int | Fraction | str-sayı` kabul eder; sayı olmayan `str` → `TypeError`; `Q` kendi `Quantity` taslağını taşır, `build_*` görülen tüm `Q`'ları sırayla toplar). **Step 4: Çalıştır** → PASS.
- [ ] **Step 5: Commit** — `git commit -m "Faz 1: Python kurucu API"`

---

### Task 5: Birim kapısı

**Files:**
- Create: `src/rigor/core/gates/__init__.py`, `src/rigor/core/gates/units.py`, `tests/core/test_units_gate.py`

**Interfaces:**
- Consumes: Görev 3.
- Produces: `UnitIssue(kind: Literal["missing_unit","unknown_unit","mismatch","nondimensionless_arg","offset_unit_misuse"], node: str, message: str)`; `UnitReport(ok: bool, issues: list[UnitIssue])`; `check_units(p: Problem) -> UnitReport`; `ureg() -> pint.UnitRegistry` (tekil, `non_int_type=Fraction`); `convert_exact(value: Fraction, src: str, dst: str) -> Fraction`.

- [ ] **Step 1: Testleri yaz**

```python
from fractions import Fraction
import rigor
from rigor.core.gates.units import check_units, convert_exact

def kinds(p): return [i.kind for i in check_units(p).issues]

def test_ft_to_m_exact():
    assert convert_exact(Fraction(8000), "ft", "m") == Fraction(12192, 5)
    assert convert_exact(Fraction(25), "degC", "K") == Fraction(5963, 20)

def test_consistent_units_ok():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", 12, "kg"), rigor.given("a", 3, "m/s**2")
    assert check_units(rigor.build_problem([rigor.eq(F, m * a)], solve=[F])).ok

def test_mismatch():
    x, L, t = rigor.unknown("x", "m"), rigor.given("L", 1, "m"), rigor.given("t", 1, "s")
    assert kinds(rigor.build_problem([rigor.eq(x, L + t)], solve=[x])) == ["mismatch"]

def test_missing_unit_is_question():
    x, k = rigor.unknown("x", "m"), rigor.given("k", 2, None)
    assert kinds(rigor.build_problem([rigor.eq(x, k)], solve=[x])) == ["missing_unit"]

def test_pure_math_dimensionless_ok():
    x = rigor.unknown("x", "dimensionless")
    assert check_units(rigor.build_problem([rigor.eq(x * x - 5 * x + 6, 0)], solve=[x])).ok

def test_exp_of_dimensioned_rejected():
    y, L = rigor.unknown("y", "dimensionless"), rigor.given("L", 1, "m")
    assert kinds(rigor.build_problem([rigor.eq(y, rigor.exp(L))], solve=[y])) == ["nondimensionless_arg"]

def test_offset_unit_in_product_is_issue_not_crash():
    y, T = rigor.unknown("y", "degC"), rigor.given("T", 25, "degC")
    assert kinds(rigor.build_problem([rigor.eq(y, T * 2)], solve=[y])) == ["offset_unit_misuse"]

def test_unknown_unit():
    x = rigor.unknown("x", "furlongz")
    assert kinds(rigor.build_problem([rigor.eq(x, 1)], solve=[x])) == ["unknown_unit"]
```

- [ ] **Step 2: Çalıştır** → FAIL.
- [ ] **Step 3: Uygula.** Her ifadenin boyutu, değer yerine `1 * unit` büyüklükleriyle ağaç üzerinde pint ile hesaplanır; `Num` boyutsuz; `pow` üssü boyutsuz ve tabanı birimliyse üs `Num` olmalı; `exp log sin cos tan asin acos atan` argümanı boyutsuz; `add sub` ve ilişkinin iki yanı aynı boyut; pint `OffsetUnitCalculusError` → `offset_unit_misuse`; `UndefinedUnitError` → `unknown_unit`; `unit is None` → `missing_unit` (diğer kontrolleri o büyüklük için atla).
- [ ] **Step 4: Çalıştır** → PASS. **Step 5: Commit** — `git commit -m "Faz 1: birim kapısı"`

---

### Task 6: Yapı kapısı (serbestlik derecesi, Dulmage–Mendelsohn)

**Files:**
- Create: `src/rigor/core/gates/structure.py`, `tests/core/test_structure_gate.py`

**Interfaces:**
- Produces: `StructureReport(status: Literal["well", "under", "over"], missing_givens: list[str], dof: int, candidates: list[str], surplus_relations: list[str])`; `analyze_structure(p: Problem) -> StructureReport` (yalnızca `SolveGoal` için; diğer hedeflerde `status="well"`, `dof=0`).

- [ ] **Step 1: Testleri yaz**

```python
import rigor
from rigor.core.gates.structure import analyze_structure

def test_well_determined():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", 12, "kg"), rigor.given("a", 3, "m/s**2")
    r = analyze_structure(rigor.build_problem([rigor.eq(F, m * a)], solve=[F]))
    assert (r.status, r.dof, r.missing_givens) == ("well", 0, [])

def test_under_determined_lists_candidates():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", 12, "kg"), rigor.unknown("a", "m/s**2")
    r = analyze_structure(rigor.build_problem([rigor.eq(F, m * a)], solve=[F]))
    assert r.status == "under" and r.dof == 1 and set(r.candidates) == {"F", "a"}

def test_given_without_value_is_missing():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", None, "kg"), rigor.given("a", 3, "m/s**2")
    assert analyze_structure(rigor.build_problem([rigor.eq(F, m * a)], solve=[F])).missing_givens == ["m"]

def test_over_determined():
    x, y = rigor.unknown("x", "dimensionless"), rigor.unknown("y", "dimensionless")
    r = analyze_structure(rigor.build_problem(
        [rigor.eq(x + y, 2), rigor.eq(x - y, 0), rigor.eq(x + y, 3)], solve=[x, y]))
    assert r.status == "over" and len(r.surplus_relations) == 1
```

(`given(..., None, ...)` değer bekleyen verilen büyüklüktür; Görev 4'ün `given` imzası `value: ... | None` kabul eder.)

- [ ] **Step 2: Çalıştır** → FAIL.
- [ ] **Step 3: Uygula.** Yalnızca `eq` ilişkileri; değişken düğümleri = `unknown` + `intermediate` (değerli `given` sabit sayılır, değersiz `given` `missing_givens`'a gider ve DM'de bilinmeyen gibi davranır). `networkx.bipartite.hopcroft_karp_matching`; eşleşmemiş değişkenlerden alternatif yollarla ulaşılan değişkenler = `candidates` (DM'nin eksik tanımlı bloğu), `dof` = eşleşmemiş değişken sayısı; eşleşmemiş denklemler = `surplus_relations` → `over` (tutarlılık Görev 13'te Z3 ile).
- [ ] **Step 4: Çalıştır** → PASS. **Step 5: Commit** — `git commit -m "Faz 1: yapı kapısı (DoF/DM)"`

---

### Task 7: Alan yükümlülükleri

**Files:**
- Create: `src/rigor/core/gates/domain.py`, `tests/core/test_domain_gate.py`

**Interfaces:**
- Produces: `Obligation(kind: Literal["nonneg", "positive", "nonzero", "unit_interval"], expr: Expr, origin: str)`; `domain_obligations(p: Problem) -> list[Obligation]` (`sqrt`→`nonneg`, `log`→`positive`, `div` paydası ve `mod` böleni→`nonzero`, `asin/acos`→`unit_interval`; `origin` = ilişki id'si).

- [ ] **Step 1: Test** — `y = sqrt(x) / log(z)` için yükümlülükler `[("nonneg", x), ("positive", z), ("nonzero", log(z))]` (tür ve `origin == "r1"` karşılaştır). **Step 2** FAIL → **Step 3** ağaç üzerinde özyinelemeli topla → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: alan yükümlülükleri"`.

---

### Task 8: Derleyiciler — SymPy, Arb, Z3

**Files:**
- Create: `src/rigor/core/compile/__init__.py`, `src/rigor/core/compile/sympy_c.py`, `src/rigor/core/compile/arb_c.py`, `src/rigor/core/compile/z3_c.py`, `tests/core/test_compilers.py`

**Interfaces:**
- Produces:
  - `symbols_for(p: Problem) -> dict[str, sympy.Symbol]` (`real=True`; `domain="integer"` → `integer=True`)
  - `to_sympy(e: Expr, syms: Mapping[str, sympy.Symbol]) -> sympy.Expr` (`Num` → `sympy.Rational`)
  - `relation_to_sympy(r: Relation, syms) -> sympy.Rel`
  - `eval_arb(e: Expr, env: Mapping[str, flint.arb], prec_bits: int = 256) -> flint.arb`
  - `to_z3(e: Expr, vars: Mapping[str, z3.ArithRef]) -> z3.ArithRef`, `relation_to_z3(r, vars) -> z3.BoolRef`, `z3_vars_for(p) -> dict[str, z3.ArithRef]` (`Real`, `integer` → `Int`)
  - `class UnsupportedForEngine(Exception)` (ör. Z3 için `sin`, rasyonel olmayan üs)

- [ ] **Step 1: Testleri yaz**

```python
from fractions import Fraction
import flint, sympy, z3, rigor
from rigor.core.compile.sympy_c import symbols_for, to_sympy
from rigor.core.compile.arb_c import eval_arb
from rigor.core.compile.z3_c import to_z3, z3_vars_for, UnsupportedForEngine
import pytest

def mk(expr_fn):
    x = rigor.unknown("x", "dimensionless")
    p = rigor.build_problem([rigor.eq(expr_fn(x), 0)], solve=[x]); return p, p.relations[0].lhs

def test_sympy_exact():
    p, e = mk(lambda x: x * x - rigor.num("0.1"))
    s = symbols_for(p)
    assert to_sympy(e, s) == s["x"] ** 2 - sympy.Rational(1, 10)

def test_arb_ball_contains_true_value():
    p, e = mk(lambda x: rigor.sqrt(x))
    v = eval_arb(e, {"x": flint.arb(2)})
    assert v.contains(flint.arb(2).sqrt()) and v.rad() < flint.arb("1e-70")

def test_z3_polynomial_and_unsupported():
    p, e = mk(lambda x: x ** 2 - 2 * x + 1)
    v = z3_vars_for(p); s = z3.Solver(); s.add(to_z3(e, v) < 0)
    assert s.check() == z3.unsat
    p2, e2 = mk(lambda x: rigor.sin(x))
    with pytest.raises(UnsupportedForEngine):
        to_z3(e2, z3_vars_for(p2))
```

- [ ] **Step 2** FAIL → **Step 3** her `OpName` için eşleme tablosu (SymPy: `Mod`, `floor`, `atan2`; Arb: `flint.ctx.prec` geçici olarak `prec_bits`'e ayarlanır ve geri alınır; Z3: `add sub mul div neg pow(tamsayı Num üs) mod abs`, gerisi `UnsupportedForEngine`) → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: SymPy/Arb/Z3 derleyicileri"`.

---

### Task 9: Etiketler, şartlar, sonuç

**Files:**
- Create: `src/rigor/core/provenance.py`, `src/rigor/core/labels.py`, `src/rigor/core/outcome.py`, `tests/core/test_labels.py`

**Interfaces:**
- Produces:
  - `ProvenanceKind(StrEnum)`: `USER_DIRECT, VIA_AGENT_UNVERIFIED, USER_FILE`; `Provenance(kind, channel: Literal["sdk","elicitation","os_dialog","agent","file"], detail: str = "")` (frozen dataclass)
  - `Label(StrEnum)`: `PROVEN, CROSS_VALIDATED, REFUSED`
  - `RefusalCode(StrEnum)`: `UNDERDETERMINED, INCONSISTENT, DIMENSION_MISMATCH, DOMAIN_VIOLATION, NO_CONSENSUS, SOLVER_UNKNOWN, CERTIFICATE_FAILED, USER_REJECTED_SPEC, ENGINE_DISAGREEMENT, UNSUPPORTED_MATH, INSUFFICIENT_INDEPENDENCE, TEMPLATE_SELF_CHECK_FAILED, PROOF_NOT_FOUND, LEAN_FORBIDDEN_CONSTRUCT`
  - `Conditions(spec_confirmed: bool, confirmation: Provenance | None, red_team: Literal["applied","not_applied"], model_families: int, unanimous: bool | None, certificate: Literal["formal","none"], paths_agree: bool, boundary_tests_passed: bool)`
  - `decide_label(c: Conditions) -> Label`; `condition_rows(c: Conditions) -> list[tuple[str, bool | None, str]]` (rapor tablosu için)
  - `Outcome(label: Label, values: dict[str, str], approx: dict[str, str], units: dict[str, str], refusal: RefusalCode | None, detail: str, conditions: Conditions | None, certificate: "Certificate | None", engines: list[str], warnings: list[str])`

- [ ] **Step 1: Testleri yaz**

```python
from rigor.core.labels import Conditions, decide_label, Label
from rigor.core.provenance import Provenance, ProvenanceKind as K

USER = Provenance(K.USER_DIRECT, "sdk"); AGENT = Provenance(K.VIA_AGENT_UNVERIFIED, "agent")
def c(**kw):
    base = dict(spec_confirmed=True, confirmation=USER, red_team="applied", model_families=2, unanimous=True,
                certificate="formal", paths_agree=True, boundary_tests_passed=True)
    base.update(kw); return Conditions(**base)

def test_proven_requires_everything(): assert decide_label(c()) is Label.PROVEN
def test_phase1_cap_without_red_team(): assert decide_label(c(red_team="not_applied", unanimous=None, model_families=0)) is Label.CROSS_VALIDATED
def test_agent_confirmation_caps(): assert decide_label(c(confirmation=AGENT)) is Label.CROSS_VALIDATED
def test_single_family_caps(): assert decide_label(c(model_families=1)) is Label.CROSS_VALIDATED
def test_no_certificate_caps(): assert decide_label(c(certificate="none")) is Label.CROSS_VALIDATED
def test_unconfirmed_refused(): assert decide_label(c(spec_confirmed=False)) is Label.REFUSED
def test_paths_disagree_refused(): assert decide_label(c(paths_agree=False)) is Label.REFUSED
def test_split_vote_refused(): assert decide_label(c(unanimous=False)) is Label.REFUSED
```

- [ ] **Step 2** FAIL → **Step 3** spec §4.1 kuralları; `PROVEN` yalnızca tüm şartlar + `confirmation.kind is USER_DIRECT` → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: etiket kuralları ve sonuç modeli"`.

---

### Task 10: Geri koyma sertifikası

**Files:**
- Create: `src/rigor/core/certify/__init__.py`, `src/rigor/core/certify/backsub.py`, `tests/core/test_certify.py`

**Interfaces:**
- Consumes: Görev 7, 8.
- Produces: `CheckRow(relation_id: str, status: Literal["satisfied","violated","undetermined"], method: Literal["exact","arb"], residual: str)`; `Certificate(kind: Literal["backsubstitution","unsat_core","identity","forall_unsat"], rows: list[CheckRow], all_satisfied: bool, detail: dict[str, str])`; `certify_solution(p: Problem, solution: Mapping[str, sympy.Expr]) -> Certificate` (tüm ilişkiler + alan yükümlülükleri satır olur; yükümlülük `origin` id'si `"<rid>:<kind>"`).

- [ ] **Step 1: Testler** — (a) `x² − 2 = 0`, çözüm `sqrt(2)` → satır `satisfied`, `method="exact"` (SymPy `simplify` sıfır); (b) çözüm `Rational(141421, 100000)` → `violated`; (c) `x > 0` kısıtı ve `x = -sqrt(2)` → kısıt satırı `violated`; (d) `y = sqrt(x)` için `x = -1` → `r1:nonneg` `violated`; (e) kapalı sıfır kanıtlanamayan ama Arb topu sıfırı içeren artık → `undetermined` ve `all_satisfied is False` (fail-closed).
- [ ] **Step 2** FAIL → **Step 3** önce kesin (`sympy.nsimplify` yok; yalnızca `simplify`/`expand` ve rasyonel karşılaştırma), değilse 256 bit Arb: eşitlikte top 0'ı dışlarsa `violated`, içerirse ve sembolik sıfır kanıtı yoksa `undetermined`; eşitsizlikte top tamamen doğru taraftaysa `satisfied` → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: geri koyma sertifikası"`.

---

### Task 11: Cebirsel çözüm (iki bağımsız yol, kök seçimi yok)

**Files:**
- Create: `src/rigor/core/solve/__init__.py`, `src/rigor/core/solve/base.py`, `src/rigor/core/solve/algebraic.py`, `tests/core/test_algebraic.py`

**Interfaces:**
- Produces: `EngineResult(status: Literal["solved","multiple","none","unknown","unsupported"], solutions: list[dict[str, sympy.Expr]], engine: str, detail: str)`; `solve_algebraic(p: Problem) -> EngineResult` (yol A, SymPy); `confirm_uniqueness(p: Problem, solution: Mapping[str, sympy.Expr]) -> Literal["unique","not_unique","unknown","unsupported"]` (yol B, Z3: denklemler ∧ kısıtlar ∧ `Or(x ≠ çözüm)` → `unsat` ise tek); `crosscheck_numeric(p, solution) -> bool` (yol B yedeği, Z3 desteklemezse: 60 basamak mpmath `findroot` farklı başlangıçlardan aynı köke yakınsar).

- [ ] **Step 1: Testleri yaz**

```python
import sympy, rigor
from rigor.core.solve.algebraic import solve_algebraic, confirm_uniqueness

def quad(constraint=None):
    x = rigor.unknown("x", "dimensionless")
    rels = [rigor.eq(x * x - 5 * x + 6, 0)] + ([constraint(x)] if constraint else [])
    return rigor.build_problem(rels, solve=[x])

def test_two_roots_are_not_chosen():
    r = solve_algebraic(quad())
    assert r.status == "multiple" and sorted(s["x"] for s in r.solutions) == [2, 3]

def test_constraint_selects_root_and_z3_confirms_unique():
    p = quad(lambda x: rigor.gt(x, rigor.num("2.5")))
    r = solve_algebraic(p)
    assert r.status == "solved" and r.solutions == [{"x": sympy.Integer(3)}]
    assert confirm_uniqueness(p, r.solutions[0]) == "unique"

def test_no_real_solution():
    x = rigor.unknown("x", "dimensionless")
    assert solve_algebraic(rigor.build_problem([rigor.eq(x * x, -1)], solve=[x])).status == "none"

def test_givens_substituted_exactly():
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", "0.1", "kg"), rigor.given("a", 3, "m/s**2")
    r = solve_algebraic(rigor.build_problem([rigor.eq(F, m * a)], solve=[F]))
    assert r.solutions == [{"F": sympy.Rational(3, 10)}]
```

- [ ] **Step 2** FAIL → **Step 3** verilenleri `Rational` olarak yerine koy; `sympy.solve(eqs, unknowns, dict=True)`; karmaşık kökleri ele; eşitsizlik/kısıt ilişkileriyle filtrele; >1 → `multiple`, 0 → `none`. **Birimler:** tüm verilenler `convert_exact` ile SI temel birimlerine çevrilerek çözülür; çözüm, bilinmeyenin kendi birimine kesin olarak geri çevrilir. → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: cebirsel çözüm, iki yol"`.

---

### Task 12: Özdeşlik / iddia denetimi (Ek-1 kuaterniyon)

**Files:**
- Create: `src/rigor/core/solve/identity.py`, `tests/core/test_identity.py`

**Interfaces:**
- Produces: `IdentityResult(holds: bool | None, counterexample: dict[str, Fraction] | None, proof: Literal["sympy_zero","z3_unsat"] | None, engines: list[str])`; `check_identity(p: Problem) -> IdentityResult` (`IdentityGoal`). Yol A: SymPy `expand(l − r) == 0`; değilse tohumlu (seed=0) rasyonel noktalarda kesin arama → karşı örnek. Yol B: Z3 `Not(l == r)`; `unsat` → doğru, `sat` → modelden karşı örnek. İki yol çelişirse `holds=None`.

- [ ] **Step 1: Testleri yaz**

```python
from fractions import Fraction
import rigor
from rigor.core.solve.identity import check_identity
from rigor.core.compile.sympy_c import symbols_for, to_sympy

def ek1_x(standard: bool):
    sa, sb, a1, a2, a3, b1, b2, b3 = [rigor.unknown(n, "dimensionless") for n in
                                      ("s_a", "s_b", "a1", "a2", "a3", "b1", "b2", "b3")]
    cross_x = a2 * b3 - a3 * b2
    claimed = (sa * b1 + sb * a1 + cross_x) if standard else (sa * a1 + sb * b1 + cross_x)
    ref = sa * b1 + sb * a1 + cross_x          # Hamilton çarpımının vektör x bileşeni
    return rigor.build_identity(claimed, ref, over=[sa, sb, a1, a2, a3, b1, b2, b3])

def test_ek1_formula_is_false_with_exact_counterexample():
    p = ek1_x(standard=False); r = check_identity(p)
    assert r.holds is False and set(r.engines) == {"sympy", "z3"}
    s = symbols_for(p); env = {s[k]: v for k, v in r.counterexample.items()}
    assert (to_sympy(p.goal.lhs, s) - to_sympy(p.goal.rhs, s)).subs(env) != 0

def test_standard_formula_holds():
    r = check_identity(ek1_x(standard=True))
    assert r.holds is True and r.proof in ("sympy_zero", "z3_unsat")
```

- [ ] **Step 2** FAIL → **Step 3** uygula → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: özdeşlik denetimi (Ek-1)"`.

---

### Task 13: Tutarlılık, ∀ ispatı, tamsayı/modüler hesap

**Files:**
- Create: `src/rigor/core/solve/logic.py`, `tests/core/test_logic.py`

**Interfaces:**
- Produces: `ConsistencyResult(status: Literal["sat","unsat","unknown"], unsat_core: list[str], model: dict[str, str] | None)`; `check_consistency(p: Problem, timeout_ms: int = 60_000) -> ConsistencyResult` (her ilişki `assert_and_track(id)`); `ForAllResult(holds: bool | None, counterexample: dict[str, str] | None, engines: list[str])`; `prove_forall(p: Problem, timeout_ms: int = 60_000) -> ForAllResult` (yol A Z3: `Not(rel)` `unsat` → doğru; yol B SymPy tek değişkende `solve_univariate_inequality(Not)` boş küme; çok değişkende yol B yok → `engines == ["z3"]`).

- [ ] **Step 1: Testleri yaz**

```python
import rigor
from rigor.core.solve.logic import check_consistency, prove_forall

def test_inconsistent_core():
    x, y = rigor.unknown("x", "dimensionless"), rigor.unknown("y", "dimensionless")
    p = rigor.build_problem([rigor.eq(x + y, 2), rigor.eq(x + y, 3)], solve=[x, y])
    r = check_consistency(p)
    assert r.status == "unsat" and sorted(r.unsat_core) == ["r1", "r2"]

def test_forall_square_nonneg():
    x = rigor.unknown("x", "dimensionless")
    r = prove_forall(rigor.build_forall(rigor.ge(x * x - 2 * x + 1, 0), over=[x]))
    assert r.holds is True and set(r.engines) == {"z3", "sympy"}

def test_forall_false_gives_counterexample():
    x = rigor.unknown("x", "dimensionless")
    r = prove_forall(rigor.build_forall(rigor.ge(x * x - 2 * x, 0), over=[x]))
    assert r.holds is False and r.counterexample is not None

def test_checksum_mod_256():   # R10 örneği: (0x12 + 0x34 + 0xFF) mod 256 = 0x45
    c = rigor.unknown("c", "dimensionless", domain="integer")
    p = rigor.build_problem([rigor.eq(c, rigor.mod(rigor.num(0x12) + 0x34 + 0xFF, 256))], solve=[c])
    from rigor.core.solve.algebraic import solve_algebraic
    assert solve_algebraic(p).solutions == [{"c": 69}]
```

(`rigor.mod` Görev 4'teki dışa aktarımlara eklenir.)

- [ ] **Step 2** FAIL → **Step 3** uygula; `unknown` sonucu asla sonuç sayılmaz (spec §6.5) → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: tutarlılık, ∀ ispatı, modüler hesap"`.

---

### Task 14: Oturum, kaynak kaydı, deterministik anlatım

**Files:**
- Create: `src/rigor/core/narrative.py`, `src/rigor/core/session.py`, `tests/core/test_session.py`, `tests/core/test_narrative.py`
- Modify: `src/rigor/__init__.py` (dışa aktar: `Session, Provenance, ProvenanceKind`)

**Interfaces:**
- Consumes: Görev 3–13.
- Produces:
  - `render_expr(e: Expr, names: Mapping[str, str]) -> str` (infix, `·`, `√`, üs `²`/`^`), `confirmation_text(p: Problem, lang: Literal["tr","en"] = "tr") -> str`, `result_text(o: Outcome, lang="tr") -> str`
  - `StepState(StrEnum)`: `NEEDS_INPUT, NEEDS_CONFIRMATION, DONE`
  - `Question(id: str, quantity_id: str | None, text: str, expected_unit: str | None, choices: list[str] | None)`
  - `Answer(value: str | None = None, unit: str | None = None, choice: str | None = None)`
  - `Step(session_id: str, state: StepState, questions: list[Question], narrative: str | None, outcome: Outcome | None)`
  - `class Session`: `__init__(self, store: Path | None = None)` (varsayılan `./.rigor/sessions`); `submit_ir(self, p: Problem, *, provenance: Provenance) -> Step`; `answer(self, step: Step, answers: Mapping[str, Answer], *, provenance: Provenance) -> Step`; `confirm(self, step: Step, decision: Literal["accept","reject"], *, provenance: Provenance) -> Step`; `@classmethod load(cls, session_id: str, store: Path | None = None) -> "Session"`; `record(self) -> dict` (rapor girdisi)
  - `class SessionIntegrityError(Exception)`

Akış (spec §4.2, sıra sabit): aralıklı girdi varsa → `REFUSED UNSUPPORTED_MATH` ("aralıklı girdiler Faz 2'de") → birim kapısı (`mismatch`/`nondimensionless_arg`/`offset_unit_misuse` → `REFUSED DIMENSION_MISMATCH`; `missing_unit`/`unknown_unit` → soru) → yapı (`missing_givens` ve `under` → soru, aday listesiyle; `over` → tutarlılık: `unsat` → `REFUSED INCONSISTENT` + çekirdek) → `NEEDS_CONFIRMATION` (anlatım ①) → onay `reject` → `REFUSED USER_REJECTED_SPEC`; `accept` → hedefe göre çöz (Görev 11–13) → `multiple` → `NEEDS_INPUT` (seçenekler = kökler; seçilen kök yeni bir eşitlik kısıtı olarak IR'a eklenir ve kaydedilir) → sertifika → `Conditions(red_team="not_applied", model_families=0, unanimous=None, …)` → `decide_label` → `DONE`. Her olay (`event`, zaman, kaynak, kanonik IR özeti) kayda eklenir; dosya `{"events": [...], "record_sha256": ...}`; `load` özeti yeniden hesaplar.

- [ ] **Step 1: Testleri yaz**

```python
import json, pytest, rigor
from rigor.core.session import Session, StepState, Answer, SessionIntegrityError
from rigor.core.labels import Label
from rigor.core.provenance import Provenance, ProvenanceKind as K
USER = Provenance(K.USER_DIRECT, "sdk")

def fma(m_value="12"):
    F, m, a = rigor.unknown("F", "N"), rigor.given("m", m_value, "kg"), rigor.given("a", 3, "m/s**2")
    return rigor.build_problem([rigor.eq(F, m * a)], solve=[F])

def test_happy_path(tmp_path):
    s = Session(tmp_path); st = s.submit_ir(fma(), provenance=USER)
    assert st.state is StepState.NEEDS_CONFIRMATION and "F = m · a" in st.narrative
    st = s.confirm(st, "accept", provenance=USER)
    assert st.state is StepState.DONE and st.outcome.label is Label.CROSS_VALIDATED
    assert st.outcome.values == {"F": "36"} and st.outcome.units == {"F": "N"}

def test_missing_given_asks_then_continues(tmp_path):
    s = Session(tmp_path); st = s.submit_ir(fma(None), provenance=USER)
    assert st.state is StepState.NEEDS_INPUT and st.questions[0].quantity_id == "m"
    st = s.answer(st, {"m": Answer(value="12")}, provenance=USER)
    assert st.state is StepState.NEEDS_CONFIRMATION

def test_reject_spec(tmp_path):
    s = Session(tmp_path); st = s.confirm(s.submit_ir(fma(), provenance=USER), "reject", provenance=USER)
    assert st.outcome.refusal.name == "USER_REJECTED_SPEC"

def test_multiple_roots_ask_user(tmp_path):
    x = rigor.unknown("x", "dimensionless")
    s = Session(tmp_path); st = s.submit_ir(rigor.build_problem([rigor.eq(x * x, 4)], solve=[x]), provenance=USER)
    st = s.confirm(st, "accept", provenance=USER)
    assert st.state is StepState.NEEDS_INPUT and sorted(st.questions[0].choices) == ["-2", "2"]
    st = s.answer(st, {st.questions[0].id: Answer(choice="2")}, provenance=USER)
    assert st.outcome.values == {"x": "2"}

def test_agent_confirmation_recorded(tmp_path):
    s = Session(tmp_path)
    st = s.confirm(s.submit_ir(fma(), provenance=USER), "accept", provenance=Provenance(K.VIA_AGENT_UNVERIFIED, "agent"))
    assert st.outcome.label is Label.CROSS_VALIDATED and any("ajan" in w for w in st.outcome.warnings)

def test_interval_given_refused_in_phase1(tmp_path):
    F, a = rigor.unknown("F", "N"), rigor.given("a", 3, "m/s**2")
    m = rigor.given("m", None, "kg", interval=("11", "13"))
    st = Session(tmp_path).submit_ir(rigor.build_problem([rigor.eq(F, m * a)], solve=[F]), provenance=USER)
    assert st.outcome.refusal.name == "UNSUPPORTED_MATH" and "Faz 2" in st.outcome.detail

def test_tampered_record_refused(tmp_path):
    s = Session(tmp_path); st = s.submit_ir(fma(), provenance=USER)
    f = next(tmp_path.glob("*.json")); d = json.loads(f.read_text()); d["events"][0]["ir_sha256"] = "0" * 64
    f.write_text(json.dumps(d))
    with pytest.raises(SessionIntegrityError):
        Session.load(st.session_id, tmp_path)
```

- [ ] **Step 2** FAIL → **Step 3** uygula (anlatım: verilenler değer + birimle, aranan, her ilişki `render_expr` ile, birimsiz problemde "Bu problemde birim yok, sayılar saf sayı olarak alındı."; ajan onayı uyarısı metni "Onay ajan aracılığıyla geldi; doğrudan senden geldiği doğrulanamadı.") → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: oturum durum makinesi ve kaynak kaydı"`.

---

### Task 15: Kanıt raporu ve replay

**Files:**
- Create: `src/rigor/report/__init__.py`, `src/rigor/report/markdown.py`, `src/rigor/report/replay.py`, `tests/report/test_report.py`

**Interfaces:**
- Produces: `render_report(record: dict, lang: Literal["tr","en"] = "tr") -> str`; `replay(session_id: str, store: Path | None = None) -> Outcome` (kayıttaki IR + cevaplar + onay kararıyla LLM'siz yeniden çözer; sürüm bilgisi farklıysa uyarı ekler).

- [ ] **Step 1: Testler** — Görev 14'ün mutlu yol oturumundan rapor: başlıklar sırasıyla `## 1. Özet`, `## 2. Sonuç anlatımı`, `## 3. Problemin onaylı tanımı`, `## 4. Varsayımlar ve girdiler`, `## 5. Doğrulama şartları`, `## 6. Red Team kaydı`, `## 7. Çözüm ve sertifika`, `## 8. Kapsam uyarıları`, `## 9. Yeniden üretim`; özet satırında `ÇAPRAZ DOĞRULANDI` ve `F = 36 N`; §6'da `Uygulanmadı (Faz 1: tek formülasyon)`; §9'da IR SHA-256 ve `rigor`, `sympy`, `z3-solver`, `python-flint`, `pint` sürümleri; `replay(id) == ` kayıttaki sonuç. Raporda kaydın içermediği hiçbir sayı yok (A4): rapordaki tüm sayı belirteçleri kayıttaki sayılarla eşleşir (regex ile çıkar, karşılaştır).
- [ ] **Step 2** FAIL → **Step 3** uygula → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: kanıt raporu ve replay"`.

---

### Task 16: `rigor doctor` ve CLI

**Files:**
- Create: `src/rigor/doctor.py`, `src/rigor/cli.py`, `tests/test_doctor_cli.py`
- Modify: `src/rigor/core/session.py` (`Session.__init__` önce `ensure_doctor()` çağırır)

Not: `doctor.py` `rigor.core` dışında olduğu için `Session`'a enjeksiyonla bağlanır: `Session.__init__(..., preflight: Callable[[], None] | None = None)`; `rigor.Session` (üst paket) varsayılan olarak `rigor.doctor.ensure_doctor`'ı geçirir.

**Interfaces:**
- Produces: `DoctorCheck(name: str, ok: bool, version: str, detail: str)`; `DoctorReport(ok: bool, checks: list[DoctorCheck])`; `run_doctor() -> DoctorReport` (Python ≥3.12; her çekirdek bağımlılığı gerçekten içe aktar + sürüm; duman testleri: `sympy.Rational(1,10)*10 == 1`, Z3 `x*x < 0` `unsat`, `flint.arb(2).sqrt()` topu `1.4142135623730950488` içerir, `convert_exact(8000, "ft", "m") == 12192/5`); `ensure_doctor() -> None` (süreç başına bir kez; başarısızsa `DoctorFailed`); `main(argv: list[str] | None = None) -> int` (`rigor doctor` → 0/1 ve tablo; `rigor report <id> [--lang en]`; `rigor replay <id>`).

- [ ] **Step 1: Testler** — `run_doctor().ok is True`; bir bağımlılığın içe aktarımı `monkeypatch` ile bozulunca `ok is False` ve ilgili satır `ok is False`; `main(["doctor"]) == 0`; `ensure_doctor` bozuk ortamda `DoctorFailed` fırlatır ve `rigor.Session()` oluşturulamaz.
- [ ] **Step 2** FAIL → **Step 3** uygula (ImportError'ı yakala ama yut**ma**: rapora yaz, `ok=False`) → **Step 4** PASS; CI'daki `continue-on-error` kaldırılır → **Step 5** `git commit -m "Faz 1: rigor doctor ve CLI"`.

---

### Task 17: Bant dışı onay (işletim sistemi diyaloğu)

**Files:**
- Create: `src/rigor/confirm/__init__.py`, `src/rigor/confirm/os_dialog.py`, `tests/test_os_dialog.py`

**Interfaces:**
- Produces: `ask_os_dialog(title: str, message: str, *, runner: Callable[..., subprocess.CompletedProcess] = subprocess.run, platform: str = sys.platform) -> Literal["accept", "reject", "unavailable"]`.
  macOS: `osascript -e 'on run argv' -e 'display dialog (item 2 of argv) with title (item 1 of argv) buttons {"Reddet", "Onayla"} default button "Onayla"' -e 'end run' <title> <message>` — **metin argv ile geçer, betiğe gömülmez** (enjeksiyon yok); çıkış `button returned:Onayla` → `accept`, kod 1 (iptal) → `reject`. Linux: `zenity --question --title <t> --text <m>` (0 → accept, 1 → reject). Komut yok / başka platform → `unavailable`.

- [ ] **Step 1: Testler** (sahte `runner`): macOS onay/ret/iptal eşlemesi; mesaj `'"; do shell script "rm -rf ~"'` içerdiğinde `runner`'a giden argv listesinde mesajın **ayrı bir öğe** olduğu ve `-e` betik metinlerinde geçmediği; `FileNotFoundError` → `unavailable`; `platform="win32"` → `unavailable`.
- [ ] **Step 2** FAIL → **Step 3** uygula → **Step 4** PASS → **Step 5** `git commit -m "Faz 1: bant dışı onay"`.

---

### Task 18: İnce MCP sunucusu + elicitation

**Files:**
- Create: `src/rigor/mcp/__init__.py`, `src/rigor/mcp/tools.py`, `src/rigor/mcp/server.py`, `tests/mcp/test_tools.py`, `scripts/elicitation_probe.py`

**Interfaces:**
- Consumes: Görev 14, 15, 17.
- Produces:
  - `tools.py` (MCP'den bağımsız, test edilebilir): `class ConfirmPort(Protocol)`: `async def ask(self, title: str, text: str) -> tuple[Literal["accept","reject","unavailable"], Provenance]`; `async def solve_ir(store: Path, ir: dict) -> dict`; `async def answer(store, session_id: str, answers: dict[str, dict]) -> dict` (kaynak her zaman `VIA_AGENT_UNVERIFIED/agent`); `async def confirm(store, session_id: str, port: ConfirmPort, *, agent_decision: Literal["accept","reject"] | None = None) -> dict`; `async def report(store, session_id: str, lang: str = "tr") -> str`; `async def status(store, session_id: str) -> dict`. Dönen sözlük = `Step`'in JSON hali (`state`, `questions`, `narrative`, `outcome`).
  - `confirm` sırası: `port.ask` → `accept/reject` ise o karar ve port'un kaynağı; `unavailable` ise `agent_decision` verilmişse `VIA_AGENT_UNVERIFIED/agent` ile, verilmemişse `NEEDS_CONFIRMATION` + "Onayı kullanıcıya sor ve `agent_decision` ile ilet; kendin karar verme." talimatı.
  - `server.py`: `build_server(store: Path) -> MCPServer` (`from mcp.server.mcpserver import MCPServer, Context`); araçlar `rigor_solve_ir`, `rigor_answer`, `rigor_confirm`, `rigor_report`, `rigor_status`; her açıklamada "Bu sorulara kendin cevap verme; kullanıcıya sor." `rigor_confirm`'in port'u: `ctx.client_capabilities` elicitation içeriyorsa `await ctx.elicit(text, schema=ConfirmForm)` (`ConfirmForm(BaseModel): onay: bool`) → `AcceptedElicitation` → `USER_DIRECT/elicitation`; `Declined`/`Cancelled`/yetenek yok → `ask_os_dialog` → `USER_DIRECT/os_dialog`; o da `unavailable` → `unavailable`. `main() -> None`: `build_server(Path.cwd() / ".rigor/sessions").run("stdio")`.
  - `scripts/elicitation_probe.py`: tek araçlı (`probe`) `MCPServer`; `ctx.client_capabilities` ve `ctx.elicit` sonucunu (`accepted/declined/cancelled/error`) `.rigor/elicitation_probe.json`'a yazar.

- [ ] **Step 1: Testler** (sahte port, MCP yok): `solve_ir` → `NEEDS_CONFIRMATION`; port `accept` + `USER_DIRECT/elicitation` → `DONE`, sonuç kaynağı `elicitation`; port `unavailable`, `agent_decision=None` → `NEEDS_CONFIRMATION` ve talimat metni; port `unavailable`, `agent_decision="accept"` → `DONE` + ajan uyarısı; `answer` kaynağı her zaman ajan; `build_server` beş aracı kaydeder (adlar listesi).
- [ ] **Step 2** FAIL → **Step 3** uygula → **Step 4** PASS
- [ ] **Step 5: Elle deneme (sahip)** — `claude mcp add rigor-probe -- uv run python scripts/elicitation_probe.py` ile hem terminal CLI'da hem VS Code eklentisinde `probe` aracını çağır; `.rigor/elicitation_probe.json` sonuçlarını araştırma notlarına "§17 Elicitation deneyi" olarak işle (ortam, sürüm, sonuç).
- [ ] **Step 6: Commit** — `git commit -m "Faz 1: ince MCP sunucusu, elicitation ve bant dışı onay bağlantısı"`

---

### Task 19: Faz 1 altın test seti ve sürüm hazırlığı

**Files:**
- Create: `tests/golden/test_faz1.py`
- Modify: `README.md` (Durum satırı: "Faz 1 (çekirdek) kullanılabilir"), `pyproject.toml` (`version = "0.1.0"`)

**Interfaces:**
- Consumes: genel API (`rigor.Session`, kurucu), Görev 12–13 fonksiyonları.

- [ ] **Step 1: Altın testleri yaz** (her biri tam oturum akışıyla, `USER_DIRECT/sdk` onayla; beklenen etiket parantezde):
  - G1 R1: `h = 8000 ft` → `m` cinsinden `12192/5` (`CROSS_VALIDATED`), yaklaşık `2438.4`.
  - G2 `F = m·a`, `m = 12 kg`, `a = 3 m/s²` → `36 N` (`CROSS_VALIDATED`).
  - G3 `x² − 5x + 6 = 0` → `NEEDS_INPUT` (`2`, `3`); `x > 2.5` eklenince `3`.
  - G4 eksik tanım: `F = m·a`, yalnız `m` → `NEEDS_INPUT`, adaylar `{F, a}` dahil.
  - G5 çelişki: `x + y = 2`, `x + y = 3` → `REFUSED INCONSISTENT`, çekirdek `[r1, r2]`.
  - G6 birim tuzağı: `x = L + t` (m + s) → `REFUSED DIMENSION_MISMATCH`.
  - G7 Ek-1: `check_identity` yanlış + kesin karşı örnek; standart formül doğru.
  - G8 `∀x: x² − 2x + 1 ≥ 0` doğru (iki motor); `∀x: x² − 2x ≥ 0` yanlış + karşı örnek.
  - G9 R10 checksum `0x45`.
  - G10 `float` girdisi `TypeError`; `"0,1"` `AmbiguousNumberError`.
  - G11 Faz 1'de hiçbir altın sonuç `PROVEN` değil (tüm `Outcome.label` toplanır, `Label.PROVEN` yok) — yanlış `PROVEN` = 0 ölçütü.
- [ ] **Step 2: Çalıştır** → `uv run pytest -q` (tümü) → PASS; `uv run --python 3.12 pytest -q` ve `uv run --python 3.14 pytest -q` → PASS.
- [ ] **Step 3: Commit ve push** — `git commit -m "Faz 1: altın test seti, v0.1.0"`; `git push origin development`.
- [ ] **Step 4: Sürüm** — CI yeşilse `gh pr create --base main --head development --title "v0.1.0 — Faz 1 çekirdek"`; sahip onaylayıp birleştirince `git tag v0.1.0 && git push origin v0.1.0`.
