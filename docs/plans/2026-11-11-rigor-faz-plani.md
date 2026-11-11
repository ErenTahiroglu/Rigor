# Rigor — faz planı (takvimsiz)

- **Tarih:** 2026-11-11
- **Mimari:** [`../design/2026-11-11-rigor-mimari.md`](../design/2026-11-11-rigor-mimari.md) (çakışmada mimari belge geçerlidir)
- **Yerini aldığı belge:** [`2026-11-07-rigor-yol-haritasi.md`](2026-11-07-rigor-yol-haritasi.md). Eski Faz 1 TDD planı
  ([`2026-11-07-faz-1-cekirdek.md`](2026-11-07-faz-1-cekirdek.md)) F0'da bu plana göre yeniden yazılır.
- **Takvim:** yok (S-19). Sıra yalnızca bağımlılıktan gelir; bağımlılığı olmayan iki faz arasında sahibin önceliği
  (S-18) karar verir.
- **İnceleme:** taze gözlü incelemenin plana dair bulguları (G-I1 … G-I15) işlendi; mimari belge §11.

İşaretler mimari belgedeki gibidir: **[S]** sahip kararı, **[K]** kanıt, **[V]** varsayım, **[Ö]** öneri.

## 1. Bağımlılık grafiği

```text
F0 ─► F1 ══K-1══► F2 ─┬─► F3 ─┐
                      └─► F4 ─┴─► F5 ══K-2══► v1.0.0
                                                │
   ┌────────────────────────────────────────────┘
   ▼
  F6 ══K-3══► F7 ─► F8 ══K-4══► (PROVEN)
   │           │     │
   │           └─────┼─► F9   (belge, toplu onay)       F6 + F7
   │                 └─► F10  (şablon, hakem paneli)   F4 + F6 + F8
   │
  F11 (optimizasyon)    F1; Sentinax B2 kısmı için F4
  F12 (Lean)            F1; PROVEN katkısı F8 kurallarıyla
  F13 (alan uyarlama)   F3 + F4; PDE için F3'ün ODE motoru
  F14 (platform, erişim) kalem başına (§4)
```

- F3 ve F4 birbirinden bağımsızdır; ikisi de F2'den sonra, istenen sırayla ya da birlikte yapılabilir.
- F11, F12 ve F13'ün teknik bağımlılığı azdır; sahibin kullanımında en az gerekenler oldukları için (S-17, S-18)
  sonda dururlar. Sahip öne almak isterse grafik izin verir.

## 2. Kalite kapıları ve ortak ölçütler

Kapılar yalnızca dört kritik geçişte **[S]** (S-31). Kapı geçilmeden sonraki faz `development`'a birleştirilmez.

| Kapı | Geçiş | Neden kritik |
| --- | --- | --- |
| K-1 | F1 → F2 | Bütün etiketler bu güven tabanına dayanır; sonradan değiştirmek her şeyi kırar |
| K-2 | F5 → `v1.0.0` | İlk kararlı sürüm; yabancının eline geçen ilk vaat |
| K-3 | F6'nın birleştirilmesi | İlk ağ çağrısı: veri ilk kez makineden çıkar, ilk kez harcama olur |
| K-4 | F8 → `PROVEN` | En üst etiket geri gelir |

Her kapıda dört adım:

1. **Otomatik ölçütler:** fazın otomatik kabul ölçütlerinin hepsi macOS ve Linux CI'da, Python 3.12, 3.14, 3.15'te
   yeşil.
2. **Sahip yerel kabul kaydı:** sahibin gerçek dosyalarıyla yapılan kabul (dosyalar `docs/private/` altında, depoya
   girmez) karar kaydına yazılır: tarih, dosya özetleri (SHA-256), sonuç. Her yerel kabulün CI'da aynı şemalı yapay
   bir eşdeğeri vardır (G-I6).
3. **Taze gözlü inceleme (EGM):** yalnızca o kapının riskine bakan en çok üç inceleme ajanı, ucuz modelle
   (`model: "sonnet"`); birleştirmeyi ana ajan yapar (S-31). Çözülmemiş engelleyici bulgu kalmaz.
4. **Güvenlik:** `gitleaks` (`--redact`) temiz; K-2 ve K-3'te ayrıca `uvx pip-audit` ile çalışma anı
   bağımlılıklarında bilinen yüksek önemde açık yok ya da her biri gerekçesiyle kayıtlı. K-1'de denetleyici ve
   köprüde mutasyon testi (`mutmut`): hayatta kalan her mutant ya öldürülür ya gerekçesiyle kayıtlıdır.

Kapılar dışında fazların otomatik ölçütleri her birleştirmede CI'da çalışır; ayrıca inceleme istemez.

**İsteğe bağlı güvenlik pilotu [Ö]:** K-1 ya da K-2 öncesinde Cloudflare security-audit-skill ile sınırlı bir
inceleme yapılabilir (mimari §5.4). Kapsamı: ayrıştırıcı, dosya okuyucular, kaynak sınırları, MCP girdi sınırı.
Kapı adımı değildir. Pilot kabul kuralı mimari §5.4'tedir; ölçütü: bilinen bir örnek kusuru bulması ve düzeltilmiş
sürümde aynı bulguyu geri çekmesi.

**Bütün fazlarda ortak ölçütler:**

- Altın sette (mimari §6.16) yanlış `CERTIFIED` = 0 ve yanlış `CROSS_VALIDATED` = 0; dönen `PROVEN` = 0 (F8'e kadar).
- Mimari sözleşmeler yeşil.
- Ağ engeli düzeneği yeşil: F6'ya kadar bütün paket, F6'dan sonra `rigor.llm` dışı her şey.

**Ölçüm kümeleri kuralı (G-I14):** "%100", "= 0" ve "doğru davranış" türü her ölçüt, ölçüldüğü kümeye bağlıdır. Her
fazın ilk işi o fazın ölçüm kümelerini sayıyla sabitlemektir: küme, boyut, eşik. Küme sonradan küçültülemez;
büyütülebilir.

---

## 3. V1 fazları

### F0 — Hazırlık

- **Kapsam:** kod yazılmadan önceki işler: belgeler, envanter, geliştirme ortamı, test altyapısı.
- **İşler:**
  1. Eski tasarım, yol haritası ve Faz 1 planına "yerini aldı" notu; karar kaydına S-20 … S-32 (bu turda yapıldı).
  2. **v1 kabul envanteri** (G-I7, G-Z12c): R1–R11 ve kripto botu ile Sentinax formüllerinin tek tek listesi. Her
     satır için: soru türü, istenen iddia özellikleri, gereken denetleyici yeteneği, en yüksek etiket, karşılaştırma
     toleransı (sayıyla), kaynakçadaki referans tanım. Denetleyicinin kapsamadığı satırın tavanı `CROSS_VALIDATED`.
     Finans satırları sahibin onayıyla dondurulur; değişiklik sahibe bağlı. Bot adı açık belgelerde anonim (K23).
  3. Faz 1 TDD planını bu plana ve envantere göre yeniden yazmak (B-8). Planda mimari §6.1–§6.16'nın her maddesi bir
     göreve eşlenir.
  4. Proje ayarından eklentileri çıkarmak (T-10) — **sahip onayıyla**.
  5. Geliştirme ortamı — **sahip onayıyla**, çünkü kurulum yapar: Python 3.15 (`uv python install`), `uv`
     güncellemesi, `pyproject.toml` (`requires-python = ">=3.12"`), geliştirme araçları (mimari §5.2), `uv.lock`.
  6. **Bağımlılık matrisi** (G-I10): F1–F3'ün bütün çalışma anı bağımlılıkları (mimari §5.3) 2 işletim sistemi × 3
     Python hücresinde kurulup içe aktarılıyor mu. Olmayan hücre sahibe sorulur (K11 değişir).
  7. **Ağ engeli düzeneği** (G-I2, mimari §6.14): ana süreç, alt süreç (`sitecustomize`), Linux'ta ağ ad alanı
     denemesi.
  8. **Altın set şeması** (G-I1, mimari §6.16) ve doğru cevap kuralı; ilk satırlar envanterden.
  9. CI iskeleti: ruff, pytest (Hypothesis dahil), import-linter, mypy (güven tabanı), ağ engeli düzeneği.
  10. Birincil kaynak ve deney doğrulamaları: D-10 (Pydantic 2.14 `frozen`), z3-solver 5.x ile Faz 1 karşı
      örnekleri.
  11. README durum notu (yapıldı); tam metin F5'te.
- **Bağımlılık:** yok.
- **Çıktı:** güncel belgeler, dondurulmuş v1 envanteri, yeniden yazılmış F1 planı, CI'dan geçen boş paket iskeleti.
- **Testler:** ağ engeli düzeneğinin kendi testi; boş paketin CI'da çalışması.
- **Kabul ölçütleri:**
  - Depodaki bütün göreli bağlantılar çözülüyor (kırık bağlantı = 0).
  - `uv sync` temiz bir klonda hatasız; `uv.lock` commit'te.
  - Bağımlılık matrisinin 6 hücresi de dolu (kuruldu / kurulamadı + neden); kurulamayan hücre için sahip kararı
    karar kaydında.
  - Ağ engeli: ana süreçte ve alt süreçte bilerek açılan bağlantı testleri düşüyor (2/2).
  - Envanterin her satırında yukarıdaki yedi alan dolu; finans satırları için sahip onayı karar kaydında.
  - D-10 ve z3 5.x sonuçları karar kaydında, kaynakla.

### F1 — Çekirdek güven tabanı

- **Kapsam:** `rigor.core`, `rigor.report`'un deterministik kısmı ve `rigor.runner`. Arayüz yalnızca Python
  fonksiyonları.
- **İşler:**
  1. Ölçüm kümelerini sabitlemek: altın set alt sınırları (mimari §6.16), sahte sertifika matrisi, kaynak sınırı
     değerleri.
  2. IR: demet tipli düğümler, `Table` ve aralıklı girdi (veri modeli), kurucu API, kanonik JSON + SHA-256,
     `schema_version`.
  3. Katı ayrıştırıcı: dilbilgisi belgesi, `ast` beyaz listesi, kaynak sınırları.
  4. İşlem anlamı profili ve `Decimal` politikası; sürümlü politika dosyası (eşikler, toleranslar, bağımsız yol
     çiftleri; m-9).
  5. Kapılar: birim (pint, saf sayı istisnası), yapı (Dulmage–Mendelsohn), tanımlılık yükümlülükleri.
  6. Derleyiciler IR → SymPy, Z3, Arb; anlam korunamazsa red.
  7. Motorlar: cebir, özdeşlik, mantık; yönlendirici; `EngineOutcome` türleri.
  8. **Karşılaştırma kuralı ve bağımsızlık tablosu** (G-I8): hangi yol çiftleri bağımsız, ortak bileşen listesi,
     tolerans politikası, sınır testleri kümesi.
  9. Bağımsız denetleyici (envanterin gerektirdiği yetenekler), izin listesi dosyası, köprü ve geri yazım.
  10. İddia özellikleri, soru türü → istenen özellikler eşlemesi, `solver_verdict`.
  11. `decide_label` karar tablosu ve tek `RefusalCode` listesi.
  12. Saf oturum durum makinesi (olay üretir); tek köken kaydı.
  13. `rigor.runner`: çözücü alt süreci, süre ve bellek sınırı, kaynak olayları.
  14. Deterministik rapor, dört alanlı kutu, gömülü olaylar; saklanan kanıtı yeniden denetleme.
  15. Mimari testler: import-linter sözleşmeleri; denetleyici için ayrı süreçte `sys.modules` denetimi.
- **Bağımlılık:** F0.
- **Çıktı:** `rigor.core`, `rigor.report`, `rigor.runner`; `v0.1.0`.
- **Testler:**
  - Birim testleri her modül için.
  - Hypothesis: ayrıştır → yaz → ayrıştır; kanonik JSON kararlılığı; karar tablosunun bütün koşul ve
    `EngineOutcome` birleşimlerinde tek sonuç vermesi; hiçbir girdide `PROVEN` dönmemesi; denetleyicinin SymPy ve
    flint'e karşı farklılık testi; "bir `given`'ı sil ya da değersiz yap" mutasyonunda sonucun her zaman
    `MISSING_VALUE` olması (G-I3).
  - Karşı örnekler: Y-1 (`sin x = 0`), Y-2 (negatif bölenli `mod`, her derleyici ve denetleyici), Y-3 (`x/x`), Y-10
    (`Decimal` ara yuvarlama), Y-12 (`0 = 0`), Y-13 (değiştirme), Y-14 (derin ağaç, dev üs, uzun belirteç),
    G-1 (`x**3 - 2*x == 0` ℝ'de: tamlık yoksa "doğrulanmış adaylar"), G-2 (aynı derleyiciyi paylaşan iki yol
    `CROSS_VALIDATED` vermez).
  - Sahte sertifika matrisi (G-I15f): her iddia özelliği × her alan (ℚ, ℤ, ℝ, aralık) için en az 50 üretilmiş sahte
    sertifika.
  - Köprü: geri yazılan ifade yeniden ayrıştırıldığında IR özeti değişmiyor.
  - Rapor kutusu: dört alan şeması; "harcama: yok" satırı (G-I15d).
  - Kaynak sınırı: sınırı aşan çözücü `REFUSED(RESOURCE_LIMIT)` veriyor ve süreç ağacında artık süreç kalmıyor.
- **Kabul ölçütleri:**
  - Sahte sertifika matrisinde reddedilen / toplam = 1.
  - Altın sette (F1 kümesi) yanlış `CERTIFIED` = 0, yanlış `CROSS_VALIDATED` = 0, dönen `PROVEN` = 0.
  - Denetleyicinin içe aktarma kümesi = izin listesi (iki katmanlı test).
  - Çözülen IR özeti = raporlanan IR özeti, bütün altın satırlarda.
  - mypy katı denetimi güven tabanı dosyalarında hatasız (mimari §6.3).
  - Ağ engeli düzeneğinde bütün testler yeşil.
- **Kapı:** K-1 (mutasyon testi dahil).

### F2 — Arayüzler

- **Kapsam:** SDK, CLI, MCP; hepsi eşzamanlı ve durumsuz (mimari §6.8).
- **İşler:**
  1. **Arayüz sözleşmesi belgesi** (G-I11): CLI çıkış kodu tablosu, JSON çıktı şeması, MCP araç şemaları (girdi,
     çıktı, hata kodları), `rigor verify` algoritması.
  2. Python SDK: kurucu API, `solve`, `audit_formula`, `reconcile`, `verify`.
  3. CLI: `rigor doctor | solve | audit | reconcile | report | verify`.
  4. MCP: `rigor_solve`, `rigor_audit_formula`, `rigor_reconcile`, `rigor_report`; stdio; ilerleme bildirimi.
  5. Köken kaydının arayüz katmanında yazılması; girdideki köken alanlarının yok sayılması.
  6. `rigor doctor`: yerel arka uçları yükler, sürümleri yazar, ağ kullanmaz.
- **Bağımlılık:** F1 (K-1 geçilmiş).
- **Çıktı:** kurulabilir paket; `v0.2.0`.
- **Testler:**
  - Sözleşme: her CLI komutu ve MCP aracı için örnek JSON çıktılarının şema doğrulaması.
  - Eksik değer matrisi (G-I3): eksik değer kaynakları (kurucu API'de değersiz `given`, MCP'de eksik değer, CSV / xlsx
    boş hücre, `NaN`, kısmi tablo satırı) × arayüzler (SDK, CLI, MCP); her hücrede sonuç `MISSING_VALUE`.
  - Köken: MCP'den gelen her ifade ve değer `VIA_AGENT_UNVERIFIED`; girdide `USER_DIRECT` yazsa bile.
  - MCP: gerçek `mcp` 2.3 istemcisiyle stdio üzerinden uçtan uca.
  - `rigor doctor` ağ engeli altında çalışıyor.
- **Kabul ölçütleri:**
  - F1 altın setinin tamamı SDK, CLI ve MCP üzerinden aynı etiketi ve aynı IR özetini veriyor.
  - Eksik değer matrisinin bütün hücrelerinde olumlu etiket = 0.
  - Örnek çıktıların %100'ü sözleşme şemasından geçiyor.
  - Sahibin istemcilerinde (Claude Code CLI ve VS Code eklentisi) `rigor_solve` ile R1'den bir örnek çalıştı;
    sonuç yerel kabul kaydında.

### F3 — Roket paketi (R1–R11)

- **Kapsam:** `rocket` modülü; sahibin roket hesapları.
- **İşler:**
  1. Ölçüm kümelerini sabitlemek: envanterden R1–R11 altın satırları, okuyucu bozuk dosya kümesi.
  2. Okuyucular: `.eng`, xlsx (bağımlılık seçimi, mimari §5.3), CSV; dosya özeti ve satır konumu (`USER_FILE`).
  3. Model kütüphanesi: Barrowman (R3), ISA (R7), ideal gaz (R8); sürümlü ve adlandırılmış (K10).
  4. `Table` ve aralıklı girdi için motor tarafı (IR düğümleri F1'de).
  5. ODE: IR → SciPy ve IR → mpmath ayrı derleyici modülleri; iki yolun her birinde adım yarılama; R5 ve R6 için 3
     serbestlik dereceli nokta kütle (eski §5.3). mpmath yolunun R6 ölçeğinde süre ve doğruluk ölçümü **[V]**.
  6. OpenRocket simülasyon CSV'si ile karşılaştırma raporu (K17).
- **Bağımlılık:** F2. IR'a ya da denetleyiciye dokunan bir değişiklik gerekirse `schema_version` artar ve K-1
  ölçütleri yeniden çalışır (G-I12).
- **Çıktı:** `rocket` modülü; `v0.3.0`.
- **Testler:**
  - Envanterdeki her R satırı için altın test (biri kasıtlı bozuk).
  - EK-1 kuaterniyon formülü hatasının yeniden bulunması (`docs/research/evidence/`).
  - ODE: iki yolun uyuşmazlığında `ENGINE_DISAGREEMENT`; yakınsamayan adım dizisinde red.
  - Okuyucular: bozuk dosya kümesi (bozuk biçim, eksik sütun, birimsiz sütun, boş hücre) → soru ya da red; dosya
    özeti rapora yazılıyor.
  - Sahibin dosyalarının yapay eşdeğerleri (aynı şema, uydurma değerler) CI'da.
- **Kabul ölçütleri:**
  - R1–R11 altın satırlarının hepsi envanterdeki etiketi alıyor; bozuk satırların hepsi yakalanıyor.
  - Bozuk dosya kümesinde olumlu etiket = 0.
  - Sahibin gerçek motor ve kütle bütçesi dosyalarıyla yerel kabul kaydı.
  - OpenRocket CSV karşılaştırması en az bir örnekte rapor üretiyor; fark etiketi değiştirmiyor.
  - mpmath ikinci yolunun ölçüm sonucu bu plana ya da mimari belgeye işlendi (uymadıysa yeni ikinci yol seçimiyle).

### F4 — Finans paketi (B1, B2)

- **Kapsam:** kripto botu ve Sentinax için B1 ve B2; Sentinax hazırlık özeti.
- **İşler:**
  1. Ölçüm kümelerini sabitlemek: F0'da dondurulan finans envanteri; her formülün doğru ve kasıtlı bozuk sürümü.
  2. B1: formül ile referans tanımın `IDENTITY` iddiası; denetleyicinin kapsamındaysa `CERTIFIED`, değilse iki
     bağımsız yolla `CROSS_VALIDATED`; yanlışsa karşı örnek.
  3. B2: çıktı dosyalarından (CSV) girdi ve sonuçların okunması; aynı formülün her satıra uygulanması; `Decimal`
     politikasıyla birebir yeniden hesap; kapalı formlu istatistiklerde envanterdeki tolerans; rastgele tohumlu
     hesaplarda bağımsız bootstrap ve Monte Carlo payı (envanterde sayıyla).
  4. Sentinax hazırlık özeti, köken şartıyla (mimari §6.11); optimizasyon çıktıları "denetlenmedi" listesinde.
- **Bağımlılık:** F2. F3'ten bağımsız.
- **Çıktı:** `finance` modülü; `v0.4.0`.
- **Testler:**
  - Envanterdeki her formülün doğru sürümü geçiyor, bozuk sürümü karşı örnekle yakalanıyor.
  - B2: hassasiyeti ya da yuvarlama modu farklı iki politikanın farklı sonuç verdiğinin raporlanması (Y-10);
    uyuşmazlıkta somut satır ve iki değer.
  - Kapı: ajan kaynaklı bir değerle ya da ajanın aktardığı formülle hesaplanan satır "canlıya hazır" listesine
    girmiyor.
  - Sahibin çıktı dosyalarının yapay eşdeğerleri CI'da.
- **Kabul ölçütleri:**
  - Envanterdeki formüllerin her biri ya B1'den geçmiş ya da "denetlenmedi" listesinde bir ret koduyla
    (mimari §6.4.1); "denetlenmedi" satırları F0'daki envanterde önceden öyle işaretlenmiş olanlardan fazla değil.
  - Bozuk sürümlerin hepsi yakalanıyor.
  - Sahibin gerçek çıktı dosyalarıyla yerel B2 kabul kaydı.
  - Sentinax hazırlık özetinin her satırı bir B1 ya da B2 kaydına bağlı.

### F5 — v1 sağlamlaştırma ve sürüm

- **Kapsam:** v1 kabul envanterinin tamamı, güvenlik testleri, belgeler, sürüm.
- **İşler:**
  1. v1 altın setinin tamamlanması: F1–F4 satırları + tuzak sınıfları.
  2. **T1 ve T2 güvenlik vakaları** (G-I5), numaralı liste:
     1. MCP girdisinde `USER_DIRECT` köken alanı göndermek.
     2. "Bunu kullanıcı yazdı" diyerek ifade aktarmak.
     3. Eksik değeri tahminle doldurup göndermek.
     4. Ortam değişkeni, ayar dosyası ya da araç argümanıyla `PROVEN` istemek.
     5. Ajan kaynaklı değerle Sentinax "canlıya hazır" listesine girmek.
     6. Raporu sonradan değiştirip `rigor verify`'dan geçirmek.
     7. Kaynak sınırını aşan girdiyle süreç ağacını askıda bırakmak.
     8. Alt süreçten ağ bağlantısı açmak.
  3. README'nin tam yeniden yazımı: vaat, etiketler, sınırlar (T3, ağ, platform), kurulum, kullanım; lisans notları
     (python-flint LGPL bileşeni).
  4. Ajanlar için kullanım dosyası (Ö-3-7): araçlar, ret kodları, "eksik değeri uydurma, kullanıcıya sor" kuralı.
  5. Sürüm: `development` → `main` PR'ı, `v1.0.0` etiketi.
- **Bağımlılık:** F3 ve F4.
- **Çıktı:** `v1.0.0`.
- **Testler:** v1 altın setinin tamamı; sekiz güvenlik vakası; temiz bir macOS ve Linux makinesinde README'deki
  kurulum adımlarının birebir çalıştırılması.
- **Kabul ölçütleri:**
  - v1 altın setinde yanlış `CERTIFIED` = 0, yanlış `CROSS_VALIDATED` = 0, dönen `PROVEN` = 0.
  - Sekiz güvenlik vakasının 8'i de beklenen davranışı veriyor (vaka 6: `rigor verify` değişikliği yakalıyor;
    yakalanamayan değişiklik türleri README'de T3 sınırı olarak yazılı).
  - README'deki her vaat cümlesi bir teste ya da mimari belgedeki bir sınıra bağlı (eşleme tablosu).
  - Temiz kurulum iki platformda README'den sapmadan çalışıyor.
- **Kapı:** K-2.

---

## 4. V1 sonrası fazlar

Her faz başlarken kendi ayrıntılı planını alır ve ilk işi ölçüm kümelerini sabitlemektir (§2). Burada kapsam ve
kabul sınırı sabitlenir.

### F6 — Doğal dil yolu, onay ve veri çıkışı izni

- **Kapsam:** metinden tek formülasyonlu denklem çıkarma (eski F3a); ajanın IR'ı; Rigor'un kendi LLM erişimi; onay;
  izinler; uzun işler.
- **İşler:**
  - Formül yolları: `Formalizer` protokolü; ajanın yazdığı IR ya da formül için ayrı araç (`rigor_submit_formula`);
    MCP sampling "ajan aracılı" sayılır (M-12).
  - Onay (mimari §6.7): üç seçenek (S-11), "bilmiyorum" (S-24), `AGENT_ASSERTED`, düzeltme turu sınırı (A-10);
    işletim sistemi bağdaştırıcıları (macOS `osascript`, Linux `zenity`) için sahte bağdaştırıcıyla CI testleri ve
    gerçek pencereyle sahip yerel kabulü (G-I4); elicitation deneyi; D-6, D-7, D-9.
  - Uzun işler: iş modeli (`job_id`, durum, sonuç), kalıcı olay kaydı (önceki olayın özetiyle zincir, atomik ekleme,
    dosya kilidi, çökme sonrası kurtarma kuralı; G-14), tekrar anahtarı, `expected_revision` (Y-6), `RIGOR_DEPTH`.
  - İzinler: başsız istemci bağdaştırıcıları, sağlayıcı başına açma bayrağı, varsayılan kapalı (S-25); dört ayrı izin
    (Y-9); çağrı birimi ve bütçe (M-8); 15 dakika kuralı (S-15, Ö-4-1); değişikliğe göre izin sorma (M-9); iş sonu
    harcama satırı ve işletim sistemi bildirimi (Ö-4-3, Ö-4-4); `NEEDS_CONSENT`; `.env` dosyaları hiç okunmaz
    (Ö-3-10); sağlayıcı koşullarının birincil kaynaktan doğrulanması (D-1 … D-3).
  - Yoklama soruları (M-6).
- **Bağımlılık:** v1.0.0.
- **Kabul ölçütleri:** bütçe hiçbir testte tek çağrı bile aşılmıyor; izin verilmeden açılan ağ bağlantısı = 0 (ağ
  engeli düzeneğiyle); `.env` okuma girişimi = 0; ajan kanalından `CONFIRMED` = 0; eksik değeri "bilmiyorum" ile
  geçen sonuç = 0; her sağlayıcının koşul kaydı birincil kaynakla karar kaydında; tuzak metin kümesinde (en az / en
  fazla, birim, iki yorum; küme boyutu ilk işte) her metin doğru soru ya da redde.
- **Kapı:** K-3.

### F7 — Red Team ve denklik

- **Kapsam:** eski F3'ün çoklu formülasyon kısmı.
- **İşler:** birbirini görmeyen çoklu formülatör; hizalama; denklik denetleyicisi; geri çeviri; mutasyon testi;
  değerlendiricinin önce sınanması (R-5); LLM ile sade anlatım, anlatım koruması, okunabilirlik (K7); yeniden
  üretimin ikinci ve üçüncü işlemi (Y-15).
- **Bağımlılık:** F6.
- **Kabul ölçütleri:** önceden etiketlenmiş eşdeğer / eşdeğer olmayan çift kümesinde yanlış "eşdeğer" = 0; kasıtlı
  bozulmuş formülasyonların yakalanma oranı ilk işte belirlenen eşiğin üstünde; sade anlatımda sayı ya da ilişki
  değiştiren çıktıların hepsi koruma tarafından reddediliyor.

### F8 — Yeterlik, heyet ve `PROVEN`

- **Kapsam:** `PROVEN`'ın geri gelmesi için gereken her şey.
- **İşler:** yeterlik kayıt şeması (çekirdekte veri modeli) ve doğrulaması (dışarıda); ölçüm: 300 + 100 görev,
  50'lik pilot, iki aşamalı kabul 311 + 311 (Ö-2-2'nin düzeltilmiş hali), tabaka başına sınırlar (Ö-2-3); heyet:
  üç zorunlu üye, en az iki aile, 100 görevlik heyet kabulü, hata korelasyonunun ölçülüp raporlanması (R-2, M-22);
  kayıtsız üye danışman (R-7); kayıt süresi ve düşürme kuralları (R-6, M-3); imzalı, sürümü yalnızca artan kayıt
  dağıtımı (M-17); test setinin sızmasına karşı zaman ayrımı (M-16, Ö-2-6); toplayıcı kuralı (A-4, M-15); heyet
  ayrışırsa yayın durur (B-2 düzeltilmiş); görev profili (A-6); `decide_label`'a `PROVEN` satırının kod
  değişikliğiyle eklenmesi.
- **Bağımlılık:** F7.
- **Kabul ölçütleri:** bağımsız, önceden gizli bir sette yanlış `PROVEN` = 0; her `PROVEN` sonucunda üç zorunlu
  üyenin geçerli kaydı ve doğrudan insan onayı kanıtı rapora yazılı; eski ya da düşük sürümlü kayıt listesiyle
  `PROVEN` = 0; iki aşamalı kabulün her hata oranında geçme olasılığı tablosu yayımlanmış.
- **Kapı:** K-4.

### F9 — Belge ve toplu girdi

- **Kapsam:** PDF / DOCX okuyucu (A-11, M-11), toplu onay ekranı (Ö-3-6), `.ork` okuyucu.
- **İşler:** dosya okuma izin ve yasak listesi; belge metninin güvenilmeyen veri zarfıyla verilmesi; emir cümlelerinin
  işaretlenmesi; her verilen değerin kaynakta geçmesi (M-11'in düzeltilmiş hali); toplu ekranda kalem başına IR özeti,
  "hepsini kabul et" varsayılanı yok. Belge dönüştürücü için MarkItDown pilotu (mimari §5.4): ayrı araç ortamı,
  kapalı eklentiler ve bulut seçenekleri; gerçek belgelerde formül, indis, eksi işareti, birim ve tablo dipnotu
  kaybı ölçülür; her çıkarım özgün dosya özeti ve konumuyla eşlenir.
- **Bağımlılık:** F6 (okuma izni, güvenilmeyen veri zarfı, onay) ve F7 (gizli talimata karşı çoklu formülasyon).
  `.ork` okuyucu yalnızca F3'e bağlıdır ve istenirse önce yapılabilir.
- **Kabul ölçütleri:** gizli talimat içeren belge kümesinde talimatın sonuca sızması = 0; ayrıca talimatların hepsi
  onay ekranında işaretli; kapsam dışı dosya okuma girişimi = 0.

### F10 — Şablonlar, alarm hakemliği ve öğrenme (K18, K19)

- **Kapsam:** kayıtlı şablonlar, bütünlük ve regresyon öz-denetimi (K18); öz-denetim alarmında hakem LLM'leri ve
  karar defteri (K19); şablonlarda kayıt geçerliliği (M-5).
- **Bağımlılık:** F4 (B2'nin tekrar eden hesapları), F6 (LLM erişimi), F8 (hakemlerin yeterliği).
- **Kabul ölçütleri:** senaryo kümesinde (bozulmuş şablon, sürüm değişikliği, yanlış alarm, gerçek hata; küme ilk
  işte sayıyla) her senaryo beklenen sonucu veriyor; kaydı düşmüş üyeli şablon üst etiket vermiyor (0).

### F11 — Optimizasyon

- **Kapsam:** HiGHS, CVXPY; LP dual sertifikası, MILP ve konveks KKT ayrı kabul profilleri (Y-11); Sentinax'ın
  optimizasyon çıktılarının B2'ye girmesi.
- **Bağımlılık:** F1; Sentinax kısmı için F4. `highspy` ve `cvxpy`'nin 3.15 tekerleği **[V]** (eski §8.1'de yoktu).
- **Kabul ölçütleri:** LP altın satırları dual sertifikasıyla `CERTIFIED`; `max x, 2x ≤ 3, x ∈ ℤ≥0` türü MILP
  satırlarında gevşetme değeri sonuç olarak dönmüyor (0).

### F12 — Lean 4 (K26)

- **Kapsam:** eski §6.11: comparator ve nanoda, yasaklı yapılar, ifade dondurma, yalıtım.
- **Bağımlılık:** F1; `PROVEN` katkısı F8'in kurallarıyla.
- **Kabul ölçütleri:** hileli ispat kümesinin (sorry, axiom, native, ifade değiştirme; küme ilk işte sayıyla) hepsi
  reddediliyor; basit tümevarım teoremleri sertifikalı.

### F13 — Alan uyarlama

- **Kapsam:** `DomainPack` protokolünün `rocket` ve `finance`'tan çıkarılması; `rigor domain new / verify / bench`,
  olgunluk düzeyleri (ilk işte tanımlanır), güvenlik tabanı, `fluids` örnek paketi, PDE, geniş alan altın seti, paket
  yazma rehberi (K24, K25).
- **Bağımlılık:** F3 ve F4; PDE için F3'ün ODE motoru.
- **Kabul ölçütleri:** `fluids` paketi tanımlı en üst olgunluk düzeyinde; güvenlik kuralını gevşeten paket
  yüklenmiyor (0).

### F14 — Platform ve erişim

Her kalem ayrı ve kendi bağımlılığıyla:

| Kalem | Bağımlılık | Kabul sınırı |
| --- | --- | --- |
| Windows (S-27) | F2; onay için F6 | Windows'ta gerçek bir onay bağdaştırıcısı sınanmış; yoksa onay gerektiren işlem yok |
| Birinci sınıf İngilizce | F7 (anlatım) | Rapor ve kutu iki dilde aynı alanları taşıyor |
| DeepSeek Harness (S-6, A-9) | F6 | İsteğe bağlı istemci; çekirdek bağımlılığı değil |
| Roket R12–R14 | F3; R13 için Cantera ve bağımsız ikinci yol | Her biri eski §5.3'teki etiket sınırıyla |
| Web arayüzü (istenirse) | F6 (onay ekranı) | Tarayıcı test aracı olarak Playwright seçeneklerinden biri; tasarım için Frontend Design (mimari §5.4) |

---

## 5. Ertelenenlerin yerleşimi

Karar kaydındaki erteleme sırasının (sahibin kullanımına göre) her maddesi bir faza yerleşti; hiçbiri iptal edilmedi.

| Erteleme sırası | Madde | Faz |
| --- | --- | --- |
| 1 | Lean 4 | F12 |
| 2 | Alan araçları, `fluids`, PDE, geniş altın set | F13 |
| 3 | `KANITLANDI`'nın tamamı, toplayıcılar | F8 |
| 4 | Hakem paneli ve öğrenme | F10 |
| 5 | Başsız istemci, izin, bütçe, 15 dakika, bildirim | F6 |
| 6 | PDF / DOCX | F9 |
| 7 | Optimizasyon | F11 |
| 8 | Red Team, LLM sadeleştirme, okunabilirlik, İngilizce | F7, F14 |
| 9 | `.ork` okuyucu | F9 |
| 10 | Toplu onay ekranı | F9 |
| 11 | Katı ayrıştırıcı | **v1'de (F1)**: S-23 doğrudan matematiği v1'e aldı |

İncelemeden sonra v1'den çıkarılanlar (mimari §11) ve yerleri: onay ekranı ve bağdaştırıcılar, iş modeli, kalıcı olay
kaydı, `RIGOR_DEPTH`, ajanın IR'ı → F6; kayıtlı şablonlar ve öz-denetim (K18) → F10; `DomainPack` protokolü → F13.

## 6. Eski yol haritasıyla eşleme

| Eski | Yeni |
| --- | --- |
| F1 Çekirdek | F1 + F2 (arayüzler ayrıldı); onay ve bant dışı pencere F6'ya |
| F2 Roket | F3 |
| F3 Red Team + doğal dil | F6 + F7 |
| F4 Şablon + öz-denetim + hakem | F10 |
| F5 Lean 4 | F12 |
| F6 Alan uyarlama | F13 |
| F7 Finans | F4 (öne alındı) |
| F8 Optimizasyon | F11 |
| F9 Sağlamlaştırma | F5 (v1) ve her kapı |
| — | F0 (hazırlık; yeni) |
| — | F8 (yeterlik ve heyet; yeni) |
| — | F9 (belge ve toplu girdi; yeni) |
| — | F14 (platform ve erişim; yeni) |
