# Rigor — hedef mimari ve v1 sınırları

- **Yazar:** Eren Tahiroğlu (sahip), tasarım taslağı kodlama ajanıyla
- **Tarih:** 2026-11-11
- **Durum:** Taslak. Sahip 2026-11-11'de on üç öneriyi onayladı (§2). Taze gözlü incelemenin (üç ajan) bulguları
  işlendi (§11).
- **Yerini aldığı belge:** [`2026-11-07-rigor-design.md`](2026-11-07-rigor-design.md). Çakışmada bu belge geçerlidir.
  Eski belgenin bu belgede ele alınmayan ayrıntıları (ör. §5.3 roket envanteri, §6.10 OpenRocket kuralları, §8.1
  Python sürümü incelemesi) bu belgeyle çelişmedikçe geçerli kalır ve "eski §5.3" diye anılır.
- **Faz planı:** [`../plans/2026-11-11-rigor-faz-plani.md`](../plans/2026-11-11-rigor-faz-plani.md).
- **Karar kaydı:** [`../decisions/2026-11-10-karar-kaydi.md`](../decisions/2026-11-10-karar-kaydi.md). B-, M-, m-,
  Y-, R-, Ö-, A-, D- ve S- numaraları oradadır.

## Okuma kuralı

Her iddianın yanında türü yazar:

| İşaret | Anlamı |
| --- | --- |
| **[S]** | Sahip kararı. Bağlayıcı. Daha yeni tarihli sahip kararı eskisinin yerini alır. |
| **[K]** | Kanıtlanmış bilgi: birincil kaynakta okundu ya da yerelde çalıştırıldı. Kaynağı ve tarihi yanında. |
| **[V]** | Varsayım: doğrulanmadı. Hangi fazda nasıl doğrulanacağı yanında. |
| **[Ö]** | Tasarımcı önerisi. Sahip "kayıttaki bütün öneriler kabul" dediği için (S-28) uygulanır; ama bir sahip kararıyla çelişirse sahip kararı geçerlidir ve öneri değiştirilebilir. |

"Etiket" Rigor'un bir sonuca verdiği güven sınıfıdır (§6.4). "Güven tabanı", bir etiketin doğru olması için doğru
çalışması gereken kod parçalarının toplamıdır (§6.3).

---

## 1. Rigor nedir, kimin için

Rigor, bir yapay zekâya ya da insana yaptırılan matematiğin doğruluğunu denetleyen bir Python kütüphanesi, komut satırı
aracı ve MCP sunucusudur. Hesabı dil modeli yapmaz; kesin aritmetik ve matematik motorları yapar. Rigor her sonuca,
kanıtın gücünü söyleyen bir etiket koyar ya da cevap vermeyi reddeder.

- **Hedef kullanıcı [S]:** aracı GitHub'da bulup kuran bir yabancı; aboneliği ya da API anahtarı olmayabilir (S-1).
- **Öncelik [S]:** v1'de yabancının ihtiyacı ile sahibin kendi kullanımı çatışırsa sahibinki önce gelir (S-18).
  Sahibin kullanımları: TEKNOFEST roket hesapları (R1–R11), bir kripto alım-satım botunun ve Sentinax'ın matematiği.
- **Takvim [S]:** yok (S-19). Faz planı yalnızca bağımlılık sırası verir.

## 2. Bu belgenin dayandığı sahip kararları (2026-11-11)

Sahip, bir önceki turdaki on üç öneriyi "önerilerin uygun" diyerek onayladı. Karar kaydına S-20 … S-32 olarak
işlendi.

| No | Karar |
| --- | --- |
| S-20 | v1'de `PROVEN` (KANITLANDI) kapalı. Kod değişmeden açılamaz; ayarla açılamaz. |
| S-21 | v1'in kabul hesapları: roket R1–R11; kripto botu ve Sentinax için B1 (formül denetimi) ve B2 (bağımsız yeniden hesap). |
| S-22 | Lean 4 arka ucu (K26) v1'den ertelenir; iptal edilmez (F12). |
| S-23 | v1 girdileri: doğrudan matematik (katı ayrıştırıcı) ve kurucu API. Doğal dil yolu v1'den sonraki ilk fazdır (F6). |
| S-24 | "Bilmiyorum" cevabı: Rigor çözer; etiket yalnızca çıkarılan denklemi kapsar; özet kutusu "tanımı kullanıcı onaylamadı" yazar; eksik bir değer varsa sonuç asla geçerli verilmez (K4 korunur). |
| S-25 | Başsız istemci sürme v1'de kapalı; sonra sağlayıcı başına ayrı bir açma bayrağıyla, varsayılan kapalı (F6). |
| S-26 | Aynı kullanıcı hesabında tam kabuk erişimi olan ajana karşı garanti verilmez; README ve raporda açıkça yazılır. |
| S-27 | Desteklenen platformlar macOS ve Linux; Windows sonra (F14). |
| S-28 | Karar kaydındaki bütün öneriler toplu kabul (Ö-2-1 dahil). İkinci dış taramada düzeltilen maddelerin düzeltilmiş hali geçerlidir. |
| S-29 | Geliştirme araçları varsayılan olarak yerel ve ağsız çalışır; model çağıran özellikleri açık izinle kullanılır. |
| S-30 | Depoda yalnızca belgelenmiş ve isteğe bağlı bir araç listesi olur; proje ayarıyla otomatik eklenti, kanca ya da MCP sunucusu açılmaz. |
| S-31 | Taze gözlü (Red Team) incelemeler yalnızca kritik faz geçişlerinde yapılır; inceleme ajanları daha ucuz modelle çalışır, birleştirmeyi ana ajan yapar. |
| S-32 | Çıktı: tasarım `docs/design/`, faz planı `docs/plans/` altında iki yeni dosya; eski tasarıma "yerini aldı" notu; commit için ayrıca onay. |

**S-23'ün yorumu [Ö]:** S-23 formülün nereden geldiğini sınırlar. Dosyalar (`.eng`, xlsx, CSV) formül getirmez,
verilen değerleri getirir; S-21'in istediği R2, R4 ve B2 bu yüzden v1'dedir. Çağıran ajanın JSON olarak yazdığı IR
ise yeni bir formül yoludur; v1'de yoktur, F6'dadır. MCP üzerinden gelen ifade metni katı ayrıştırıcıdan geçer ama
"ajan aktardı" diye kaydedilir (§6.6).

**S-24'ün v1'deki yeri [Ö]:** v1'de formülü her zaman kullanıcı yazar ya da ajan aktarır; üç seçenekli onay ekranı
doğal dil yolunun parçasıdır (F6). S-24 F6'da uygulanır. v1'de onay sorulmaz; kutu formülün kimden geldiğini yazar.

Eski K-kararlarının durumu:

| K | Durum |
| --- | --- |
| K1, K3, K5, K8, K9, K10, K11, K12, K13, K17, K20, K21, K22, K23, K24, K25 | Geçerli. K24/K25'in araçları (`rigor domain …`) F13'te; alandan bağımsızlık v1'de mimari testle korunur. |
| K2 | Geçerli. "Red Team denetiminden geçmiş kadar kesin" standardı yalnızca `PROVEN` için geçerlidir (M-18, S-28). |
| K4 | Geçerli ve S-24 ile pekişti: "bilmiyorum" eksik değer sorusunu kapatmaz. |
| K6 | Daraldı: v1'de formülü kullanıcı yazar (kurucu API, katı ayrıştırıcı) ya da ajan ifade olarak aktarır. Ajanın IR'ı ve Rigor'un kendi LLM erişimi F6'da. |
| K7 | v1'de anlatım deterministiktir; LLM ile sadeleştirme F7'de. |
| K14, K15 | F6'ya ertelendi; S-25'teki sağlayıcı başına bayrak ve dört ayrı izinle (Y-9). |
| K16 | Tarih bu planda kullanılmaz (S-19). "Ayrıntılı takvim yapılmaz" kuralı korunur. |
| K18 | F10'a ertelendi. v1'de B2, aynı formülü dosyanın her satırına uygular; kayıtlı şablon deposu ve öz-denetim yoktur. |
| K19 | F10'a ertelendi. |
| K26 | F12'ye ertelendi (S-22). |

## 3. Vaat (v1)

> Rigor'un döndürdüğü her sonuç, yanında yazan matematiksel iddiaya göre doğrulanmıştır ve doğrulamanın gücü
> etiketle yazar. Formülü kimin yazdığı ve kimin onayladığı sonuçla birlikte gösterilir. Rigor doğrulayamadığı
> sonucu vermez ve nedenini söyler. Etiketsiz bir sayı asla dönmez. **[S]** (Ö-3-13, S-28)

Vaadin sınırları, README'de ve her raporda aynı sözlerle **[S]** (S-26, S-29):

- Etiket, gösterilen denklemin doğru çözüldüğünü söyler; denklemin senin kastettiğin problem olduğunu söylemez.
- Aynı bilgisayarda, aynı kullanıcı hesabında, kabuk erişimi olan bir ajan Rigor'un dosyalarını ve çıktılarını
  değiştirebilir. Rigor bu ajana karşı garanti vermez.
- v1 hiçbir ağ çağrısı yapmaz, hiçbir dil modelini çağırmaz, hiçbir şey harcamaz.

## 4. Red Team bulguları ve çözüm kararları

Kaynak: karar kaydındaki iki tarama (B-, M-, m-, Y-), bu turdaki araç zinciri incelemesi (T-) ve bu belgenin taze
gözlü incelemesi (G-, §11). Her bulgunun ayrıntısı kaynağındadır; burada çözüm ve yeri var.

### 4.1. Etiket ve güven tabanı

| Bulgu | Çözüm | Yer |
| --- | --- | --- |
| B-1 onay kuralı çelişkisi, "bilmiyorum" kaçış kapısı | Onay bir durumdur; ajan kanalı `CONFIRMED` üretemez (G-5); eksik değer hiçbir durumda geçilmez **[S]** (S-24). v1'de onay yok (§2) | F6 |
| B-2 etiket sırası tanımsız; heyet ayrışması | Yukarıdan aşağıya tek karar tablosu ve motor sonucu türleri (§6.4). Heyet ayrışırsa amaçlanan problem için yayın durur | F1 (tablo), F8 (heyet) |
| B-3 bağımsız denetleyici tanımsız | `core/certify/kernel` (§6.5) ve ona giden köprü güven tabanında (§6.3). Z3 `unsat` ve SymPy sadeleştirmesi tek başına sertifika değildir | F1 |
| B-9, Y-1, Y-7, Y-12 aday, teklik, tamlık karışıyor | İddia edilecek özellikleri soru türü belirler, çözücü seçmez (§6.5). Tamlık gösterilmeden sonuç "çözüm kümesi" diye değil "doğrulanmış aday" diye sunulur. Boş aday listesi "çözüm yok" değildir | F1 |
| Y-2 `mod` anlamı arka uca göre değişiyor **[K]** (`7 mod −3`: Python −2, `Decimal` 1; 2026-11-11'de yerelde çalıştırıldı) | Sürümlü işlem anlamı profili: `mod_floor`, `mod_euclid`, `mod_trunc` ayrı işlemler; anlamı korunamayan derleme reddedilir | F1 |
| Y-3 tanımlılık yükümlülükleri | Sadeleştirmeden önce bütün ağaçtan çıkarılır (`x/x` → `x ≠ 0`) | F1 |
| Y-10 `Decimal` politikası kesin ifade değil **[K]** (2 basamakta `(1/3)·3` = 0,99; yerelde çalıştırıldı) | İki ayrı iddia: "kesin matematiksel değer" ve "belirtilen `Decimal` politikasının çıktısı" | F1, F4 |
| Y-13 `frozen=True` iç içe listeyi dondurmuyor | IR'da demet tipleri; değiştirme testi. Pydantic 2.14 davranışı F0'da ölçülür (D-10) | F0, F1 |
| Y-14 ayrıştırıcıda kaynak sınırı yok | Ayrıştırıcıya ve her çözücü alt sürecine boyut, derinlik, süre ve bellek sınırı (§6.10) | F1, F2 |
| Y-16 doğrusal olmayan eşitsizlikte bağımsız sertifika yok | Denetleyici kanıtlayamıyorsa `CERTIFIED` yok; `CROSS_VALIDATED` ancak ikinci yol iddiayı bağımsız bir karar yöntemiyle verirse (§6.4) | F1 |
| Y-19 içe aktarma testi geçişli ve dinamik içe aktarmayı kapsamayabilir | `import-linter` sözleşmeleri bütün katmanlar için; ayrı süreçte `sys.modules` denetimi denetleyici için, izin listesi dosyasından | F1 |
| Y-20 kanonik JSON sözdizimsel kimlik | İçerik özeti ile matematiksel denklik ayrı kavramlar; raporda ayrı satırlar | F1 |
| "`PROVEN` kapalıysa vaat kendiliğinden tutar" yanlış | Bütün kabul ölçütleri "yanlış `CERTIFIED` = 0" ve "yanlış `CROSS_VALIDATED` = 0" içerir; ölçüm altın sete karşı (§6.16) | Her faz |

### 4.2. Girdi, köken ve ajan

| Bulgu | Çözüm | Yer |
| --- | --- | --- |
| Y-4, Y-5 elicitation insan onayının kanıtı değil; form gönderimi ile karar karışıyor | Onay kaydı kanal, yanıtlayan ve insan varlığı kanıtı alanlarını taşır; reddetme son durumdur. v1'de onay olmadığı için F6'da | F6 |
| B-4, A-14 kabuk erişimli ajan | Tehdit modeli dört düzey (§6.13); tam kabuk erişimine karşı garanti yok **[S]** (S-26) | F1, F5, README |
| M-2, Y-6 uzun iş tek çağrıya sığmaz; yeniden deneme | v1'de işler kısa; araçlar eşzamanlıdır (G-Z1). İş modeli, tekrar anahtarı ve `expected_revision` F6'da, uzun işlerle birlikte. Araç eklemek mevcut araçları kırmaz | F6 |
| M-7 üç seçenekli ekranın veri biçimi yok | Doğal dil yoluyla birlikte F6'da | F6 |
| M-10 katı ayrıştırıcının dilbilgisi yok | Yayımlanmış dilbilgisi (§6.6); MCP'den gelen her ifade "ajan aktardı" | F1, F2 |
| M-19, M-21 rapor dosyası korunmuyor; iç içe çağrı | v1: `rigor verify <rapor>` saklanan kanıtı yeniden denetler; T3'e karşı yetki sınırı değildir. `RIGOR_DEPTH` yalnızca Rigor ajan çağırdığında anlamlı: F6 | F2, F6 |
| G-6 ajandan gelen değer Sentinax kapısını geçebiliyor | "Canlıya hazır" kümesi köken de ister (§6.11) | F4 |

### 4.3. Kapsam ve sıra

| Bulgu | Çözüm | Yer |
| --- | --- | --- |
| B-6, B-7 kapsam ve hedef kullanıcı çatışması | v1 kontrollü: sahibin hesapları ve doğrudan matematik (S-18, S-21, S-23). Gerisi sıralı fazlarda | Faz planı |
| B-8 Faz 1 sözleşmeleri eski üç etiketi donduracak | Faz 1 planı F0'da bu belgeye göre yeniden yazılır; dışarıya açılan sözleşmeler §6.15'te | F0 |
| M-1 kontrolün tersine çevrilmesinin yeri yok | Çekirdek saf kalır; izin, bütçe, istemci ve yeterlik çekirdek dışı katmanlarda (§6.1) | F1 (kural), F6, F8 |
| M-4, R-8 yeterlik ölçümünün fazı döngüsel | Doğal dil (F6) → Red Team ve denklik (F7) → yeterlik ve heyet (F8) sırası | Faz planı |
| Y-17 tasarım ile yol haritasının sırası farklı | Tek bağımlılık grafiği faz planında | Faz planı |
| Y-21, A-12 Lean ertelemesi | Sahip kararı S-22 | F12 |
| m-6 README eski vaadi gösteriyor | README durum notu güncellendi; tam metin v1 sürümünde | F0, F5 |

### 4.4. Araç zinciri (bu tur, 2026-11-11)

| No | Bulgu | Tür | Çözüm |
| --- | --- | --- | --- |
| T-1 | ATM kataloğunda codebase-memory-mcp ve Graphify `reviewState: unreviewed`; işlev testleri `not-run` ya da yalnızca "yayıncı anlatıyor" | [K] ATM `data/catalog-seed.json`, `docs/TOOL-COMPATIBILITY.md` (development, 2026-11-11) | İkisi de güvenilir sayılmaz; Rigor'un zorunlu araç zincirine girmez (§5) |
| T-2 | Graphify'da yüksek önemde güvenlik bildirimi: Fortran çıkarıcısı `#include` ile sistemdeki herhangi bir dosyayı okuyup grafiğe ve model sağlayıcısına sızdırabiliyordu; 0.9.70'te kapandı | [K] GHSA-pcc4-rvhr-2pr8 | Yereldeki 0.9.88 etkilenmez. Güvenilmeyen depoda çalıştırılmaz |
| T-3 | Graphify belgeler, PDF ve görseller için anlam çıkarma adımında içeriği modele gönderiyor; yalnızca kod çıkarımı yerel | [K] Graphify README "Privacy" | Rigor deposu büyük ölçüde belge; bu adım belgeleri sağlayıcıya gönderir. Kullanılırsa yalnızca `--code-only` |
| T-4 | Graphify'ın git dışı dosyaları (`docs/private/`) atlayıp atlamadığı | [V] doğrulanmadı | Doğrulanana kadar depo kökünde çalıştırılmaz; yalnızca `src/` üzerinde |
| T-5 | `graphifyy` paketi `requires_python <3.15`; Rigor'un birincil sürümü 3.15 (K11) | [K] PyPI, 2026-11-11 | Proje ortamına kurulmaz; ancak yalıtılmış `uv tool` olarak |
| T-6 | Graphify neredeyse her gün sürüm çıkarıyor (0.9.104–0.9.106 üç günde), 1.632 açık kayıt | [K] GitHub, 2026-11-11 | Sabitlenmiş sürüm olmadan iş akışına bağlanmaz |
| T-7 | codebase-memory-mcp yerelde 0.11.0 olarak kullanıcı düzeyinde kurulu; Grep, Glob, Bash, Read araçlarına, oturum ve alt ajan başlangıcına kanca takıyor; MCP sunucusu kullanıcı ayarında | [K] `~/.claude/settings.json`, `~/.claude.json` (yalnızca anahtar adları okundu) | Kullanıcının genel tercihi; Rigor'un kapsamı dışında. Rigor'un testleri, belgeleri ve iş akışı ona dayanmaz |
| T-8 | codebase-memory-mcp güncel sürüm 0.12.1; 0.12.0'ın paket kurulumları bozuktu; 0.11.0 → 0.12 dizin biçimi değişti | [K] GitHub sürüm notları | Yükseltme kullanıcının kararı; `/usage` işinde ele alınır |
| T-9 | codebase-memory-mcp "kendiliğinden ağ isteği yapmaz, telemetri toplamaz" diyor; imza paketi (`.bundle`) ve SBOM yayımlıyor | [K] yayıncı beyanı; [V] davranışı bağımsız ölçülmedi | Bağımsız ölçüm yapılmadan "ağsız" sayılmaz |
| T-10 | Proje ayarı (`.claude/settings.json`) EGM ve Superpowers eklentilerini depoyu klonlayan herkes için açıyor | [K] dosya içeriği | S-30 ile çelişiyor. Öneri: `enabledPlugins` ve `extraKnownMarketplaces` proje ayarından çıkarılır, sahibin kendi `settings.local.json` dosyasına ya da kullanıcı ayarına taşınır. **Sahip onayı bekliyor** (yapılandırma değişikliği) |
| T-11 | Gitleaks 8.30.1 yerelde Homebrew ile kurulu; yeni özellik geliştirilmiyor, yalnızca güvenlik yaması | [K] `gitleaks version`, ATM `TOOL-COMPATIBILITY.md` | Yerel, ağsız sır taraması için yeterli; çıktısı sırrı gösterebildiği için yalnızca `--redact` ile ve dosyaya yazmadan |
| T-12 | Makinede Python 3.15 yok; 3.12 ve 3.14 kurulu; `uv` 0.10.11 | [K] `uv python list --only-installed` | F0'da 3.15 kurulumu (sahip onayıyla) ve bütün bağımlılıkların sınanması |
| T-13 | `python-flint` lisansı "MIT AND LGPL-3.0-or-later" (FLINT kütüphanesi LGPL) | [K] PyPI | Rigor onu dağıtmaz, bağımlılık olarak kurar; lisans notu README'ye |
| T-14 | Uygunluk raporu mimarinin inceleme öncesi sürümüne göre yazıldı (rapor 12:56, mimari 13:00). Rapordaki "MCP iş modeli", "tekrar anahtarı, revizyon ve onay sözleşmesi" ve "MCP onay alanları" v1'de yok; F6'da | [K] dosya zamanları | Rapordaki araç kararları geçerli; bu konulara dair inceleme hedefleri F6'ya kayar |
| T-15 | codebase-memory dizini `docs/private/` ve `.claude/` klasörlerini dizine almıyor | [K] `index_status`, 2026-11-11 | Gizlilik kuralıyla uyumlu. Kural `.gitignore`'a dayanıyor: gizli klasör `.gitignore`'dan çıkarılırsa dizine girer |

## 5. Araç zinciri

### 5.1. Seçim ilkeleri [S]

- Zorunlu araçlar yerel çalışır ve ağ istemez (S-29). Ağ isteyen kontrol (bağımlılık açığı taraması) yalnızca kalite
  kapısında, o an elle çalıştırılır.
- Proje ayarı hiçbir eklentiyi, kancayı ya da MCP sunucusunu otomatik açmaz (S-30).
- Bir araç yalnızca Rigor'a ölçülebilir bir katkısı varsa girer. "Belki işe yarar" yeterli değildir.
- Aynı işi yapan iki araçtan yalnızca biri seçilir.

### 5.2. Zorunlu geliştirme araçları

Sürümler 2026-11-11'de PyPI ve GitHub'dan okundu **[K]**. Kesin sürümler `uv.lock` ile F0'da sabitlenir.

| Araç | Sürüm | Lisans | Katkı | Ağ |
| --- | --- | --- | --- | --- |
| `uv` | yerel 0.10.11 | MIT / Apache-2.0 | Python sürümleri, ortam, kilit dosyası. Tek kurulum aracı | Yalnızca paket indirirken |
| `pytest` | 9.2.0 | MIT | Test çalıştırıcı | Yok |
| `hypothesis` | 6.170.15 | MPL-2.0 (yalnızca geliştirme) | Özellik tabanlı testler: ayrıştır → yaz → ayrıştır, karar tablosu kapsaması, denetleyicinin SymPy ve flint'e karşı farklılık testi | Yok |
| `ruff` | 0.17.4 | MIT | Biçim ve stil denetimi; tek araç | Yok |
| `import-linter` | 2.16 | BSD-2 | Katman kurallarının statik ve geçişli denetimi (Y-19) | Yok |
| `mypy` | 2.4.1 | MIT | Yalnızca güven tabanı dosyalarında katı tip denetimi (§6.3) | Yok |
| `mutmut` | 3.8.1 | BSD-3 | Yalnızca denetleyici ve köprüde mutasyon testi: testler, koddaki küçük bir bozulmayı yakalıyor mu (G-10). K-1 kapısında | Yok |
| `gitleaks` | 8.30.1 (yerel) | MIT | Depo herkese açık; commit ve push öncesi elle sır taraması (`--redact`) | Yok |

Kapı kontrol listesinde, kurulu araç olmadan: `pip-audit` 2.10.1 (Apache-2.0) `uvx` ile o an çalıştırılır; çalışma
anı bağımlılıklarında bilinen açıkları arar; ağ ister (K-2, K-3).

CI: GitHub Actions, macOS ve Linux, Python 3.12, 3.14, 3.15 (K11, S-27). CI depo kodunu GitHub'da çalıştırır; depo
zaten herkese açık olduğu için yeni bir veri çıkışı değildir **[Ö]**.

### 5.3. Çalışma anı bağımlılıkları

Her bağımlılık onu ilk gerektiren fazda eklenir (G-Z12):

| Faz | Bağımlılık | Sürüm (PyPI, 2026-11-11) [K] |
| --- | --- | --- |
| F1 | `pydantic`, `sympy`, `z3-solver`, `python-flint`, `pint`, `networkx`, `mpmath` | 2.14.3, 1.14.0, 5.4.1.0, 0.9.0, 0.26.2, —, 1.4.1 |
| F2 | `mcp` | 2.3.0 |
| F3 | `scipy`; xlsx okuyucu (aday `openpyxl` **[V]**) | 1.18.1 |

- Eski tasarım z3'ün 4.x serisini sınamıştı; 5.x ile yeniden sınanır **[V]** (F0).
- Bütün bağımlılıkların Python 3.15 ve iki işletim sisteminde kurulup içe aktarılabildiği F0'da sınanır **[V]**.
  Biri kurulamazsa birincil sürümün 3.14'e inmesi sahibin kararıdır (K11'i değiştirir).
- Yeni bir çalışma anı bağımlılığı ancak faz planında gerekçesiyle eklenir.

### 5.4. İsteğe bağlı ve sonraki faz araçları (depoya bağlanmaz)

Kaynak: ATM `development` dalındaki 23 kaydın Rigor'a uygunluk raporu
([`../research/2026-11-11-atm-arac-uygunluk-raporu.md`](../research/2026-11-11-atm-arac-uygunluk-raporu.md)) ve
§4.4. Katalogdan v1 çalışma anına yeni bağımlılık girmez **[S]** (sahip, 2026-11-11).

| Araç | Durum | Kural |
| --- | --- | --- |
| Gitleaks | Şimdi; zorunlu zincirde (§5.2) | 2026-11-11'de sınandı **[K]**: yapay sırrı yakaladı ve `REDACTED` yazdı; temiz dosyada çıkış kodu 0; 7 commit'lik geçmişte ve commit'e girecek 27 dosyada bulgu 0 |
| EGM (yerel 0.1.1) | Şimdi; K-1 … K-4 kapılarında | Yalnızca kapılarda; inceleme ajanları ucuz modelle (S-31). 2026-11-11'de üç ajanla çalıştı **[K]** (§11). İnceleme sertifika üretmez ve F8'deki heyetin yerine geçmez |
| Superpowers (yerel 7.0.0; güncel 7.0.2) | Şimdi; isteğe bağlı yöntem | Sahibin kullanıcı ayarında. Proje ayarından çıkarılması önerilir (T-10). EGM kapı incelemeleriyle aynı işi tekrar etmez |
| codebase-memory-mcp (yerel 0.11.0; güncel 0.12.1) | Mevcut kullanım sürer | 2026-11-11'de sınandı **[K]**: Rigor dizini hazır; `docs/private/` ve `.claude/` dizin dışında; yeni mimari bölümü doğru satırda bulundu. Grafik sonucu kaynakla doğrulanır. CI, testler ve katman kuralları ona dayanmaz (katmanları `import-linter` zorlar) |
| Cloudflare security-audit-skill | Kod oluştuktan sonra sınırlı pilot | K-1 ya da K-2 öncesi; ayrıştırıcı, dosya okuyucular, kaynak sınırları ve MCP girdi sınırı. Kapı adımı değildir. Sürüm yok, yalnızca `main` dalı **[K]**: pilot bir commit'e sabitlenir. Hedef kod çalıştırılacaksa ağsız, işletim sistemiyle zorlanan bir sandbox gerekir **[V]** |
| MarkItDown (0.1.9) | F9 adayı | `requires_python <3.15` **[K]** (PyPI): ayrı araç ortamı. Formül, indis, eksi işareti, birim ve tablo aktarımı gerçek belgelerle sınanır; çıktı güvenilmeyen girdidir. xlsx ve CSV doğrudan okuyucularla okunur |
| Exa MCP Server | Araştırmada isteğe bağlı | Sorgular Exa'ya gider; v1 motoruna girmez. Bulunan içerik kanıt sayılmaz; özgün kaynak, tarih ve sürüm saklanır. Mevcut araştırma araçları yetiyorsa eklenmez |
| Playwright (Test, CLI, MCP), agent-browser | Web arayüzü olursa | Bugün web arayüzü yok. Gerekirse biri seçilir; üçü birden kurulmaz. Rigor'un MCP sözleşmesini sınamaz |
| Anthropic Frontend Design | Arayüz tasarlanırsa | F6 onay ekranı ya da rapor arayüzü için aday |
| Ponytail, Karpathy-inspired guidelines, Caveman | Eklenmez | Superpowers ve mevcut kurallarla örtüşür; Caveman açıklama ve ret gerekçesi kaybı riski taşır |
| agentic-awesome-skills | Kaynak kataloğu | Somut ihtiyaçta tek beceri seçilip incelenir; toplu kurulum yok |
| Graphify, Understand Anything | Önerilmez | Grafik aracı örtüşmesi, belge içeriğinin sağlayıcıya gitmesi (T-3), ayrı ortam. Graphify kullanılırsa: yalıtılmış `uv tool`, sabit sürüm, `--code-only`, yalnızca `src/` |
| Betterleaks | Seçilmedi | Gitleaks ile aynı iş (§5.1). Geçiş ancak Rigor örneklerinde ölçülmüş faydayla |
| Claude-Mem, Ruflo | Kapalı | ATM'de karantinada; kanca, daemon ve ek saklama yüzeyi |
| Apify MCP Server, Strix | Önerilmez | Uzak çalıştırma ve değişken maliyet; aktif hedef testi bugünkü ürüne uygun değil |

**Pilot kabul kuralı [Ö]:** bir aracın pilotu "araç çalıştı" ile kabul edilmez. Rigor'dan seçilmiş görevlerde
yakaladığı hata, harcadığı süre ve model maliyeti, yanlış bulgu, yazdığı dosyalar ve ağ davranışı kaydedilir. Katkısı
gösterilmeyen ya da başka bir aracın işini tekrar eden araç kalıcı zincire girmez.

## 6. Teknik mimari

### 6.1. Katmanlar ve bağımlılık yönü

```text
            ┌──────────── arayüzler ────────────┐
            │ rigor.sdk   rigor.cli   rigor.mcp  │   ince kabuklar; iş mantığı yok
            └───────┬───────────┬───────────┬────┘
                    ▼           ▼           ▼
            ┌──────────── yürütme ──────────────┐
            │ rigor.runner    çözücü alt süreci, sınırlar
            │ rigor.report    rapor, özet kutusu, yeniden denetim
            │ rigor.domains   rocket, finance (düz modüller)
            │ [F6] rigor.llm  rigor.consent  rigor.confirm  rigor.jobs
            │ [F7] rigor.redteam   [F8] rigor.qualification
            │ [F10] rigor.adjudication  [F12] rigor.lean
            └───────────────┬────────────────────┘
                            ▼
            ┌──────────── rigor.core (saf) ─────┐
            │ ir · parse · semantics · gates     │
            │ compile · solve · certify          │
            │ labels · outcome · provenance      │
            │ session (olay üretir) · policy     │
            │   certify/kernel  ← ayrı güven tabanı
            └────────────────────────────────────┘
```

Kurallar **[Ö]**, hepsi F1'den itibaren testle zorlanır:

1. Oklar yalnızca aşağı gider. `rigor.core` yukarıdaki hiçbir paketi içe aktarmaz.
2. `rigor.core` ağ, dosya yazma, alt süreç ve saat kullanmaz; girdiyi alır, sonucu döndürür. Çözücüler süreç içinde
   çağrılır. Zaman damgası, rastgelelik tohumu ve kaynak olayları (süre aşımı, bellek aşımı, çökme) dışarıdan,
   `rigor.runner`'dan girdi olarak gelir; `decide_label` onları ret nedeni olarak tüketir (G-7).
3. `core/certify/kernel` yalnızca izin listesindeki standart kütüphane modüllerini içe aktarır (§6.5). IR,
   pydantic, `compile/`, SymPy, Z3, pint ve flint'i içe aktaramaz.
4. Alan paketleri (`rigor.domains`) çekirdeği kullanır, çekirdek onları bilmez (K24).
5. v1'de hiçbir modül ağ soketi açmaz (§6.14).

### 6.2. Paket ağacı (v1)

```text
src/rigor/
  __init__.py            genel API + __lazy_modules__ (K11; hiçbir davranış buna bağlı değil)
  core/
    numbers.py           kesin sayı okuma
    ir/                  düğümler (demet tipli), Table ve aralıklı girdi dahil; kurucu; kanonik JSON + SHA-256; schema_version
    parse/               katı ifade dilbilgisi: ast beyaz listesi, kaynak sınırları
    semantics/           işlem anlamı profili (mod_floor/euclid/trunc), Decimal politikası
    gates/               birim (pint), yapı (Dulmage–Mendelsohn), tanımlılık yükümlülükleri
    compile/             IR → SymPy, Z3, Arb; F3'te IR → SciPy ve IR → mpmath ayrı modüller
    solve/               yönlendirici; motorlar: cebir, özdeşlik, mantık; F3'te ODE
    certify/
      kernel/            bağımsız denetleyici: kendi ifade tipi, kendi birim tablosu
      bridge.py          IR → denetleyici iddiası çevirisi ve geri yazımı (güven tabanında)
      claims.py          iddia özellikleri; solver_verdict
    labels.py            Label, RefusalCode (tek liste), EngineOutcome, decide_label
    outcome.py           sonuç: etiket, değerler ya da adaylar, iddia, kapsam
    provenance.py        tek köken kaydı: kaynak, formülün yazarı, kanal
    session.py           saf durum makinesi; olay üretir, saklamaz
    policy.py            sürümlü eşikler ve toleranslar
  runner/                çözücüyü alt süreçte, kaynak sınırlarıyla çalıştırır; kaynak olaylarını üretir
  report/                Markdown rapor, gömülü olay listesi ve kanıt; dört alanlı kutu; yeniden denetim
  domains/
    rocket/              R1–R11, .eng / xlsx / CSV okuyucular, OpenRocket CSV karşılaştırması
    finance/             B1 formül denetimi, B2 mutabakat, Sentinax hazırlık özeti
  sdk.py · cli.py · mcp/ ince kabuklar
tests/
  architecture/          import-linter sözleşmeleri; denetleyici için ayrı süreçte sys.modules denetimi
  kernel_negative/       denetleyicinin reddetmesi gereken üretilmiş sahte sertifikalar
  golden/                altın set (§6.16)
  network/               ağ engeli düzeneğinin kendi testi
```

### 6.3. Güven tabanı

Her etiketin doğru olması için doğru çalışması gerekenler **[Ö]** (G-3):

| Etiket | Güven tabanı |
| --- | --- |
| `CERTIFIED` | `parse` (kullanıcının yazdığı → IR), IR kanonik biçimi, işlem anlamı profili, `certify/bridge`, `kernel`, `labels.decide_label`, rapor kutusu. Çözücüler (SymPy, Z3, flint) güven tabanında **değildir**: yanılırlarsa denetleyici reddeder |
| `CROSS_VALIDATED` | `parse`, IR, işlem anlamı profili, iki yolun her biri (derleyici + motor), karşılaştırma kuralı ve tolerans politikası, `decide_label`, rapor kutusu |
| `REFUSED` | Ret nedeninin doğru raporlanması |

Köprünün yanlış çevirmesine karşı: denetleyici doğruladığı iddiayı kendi ifade tipinden kanonik metne geri yazar;
rapor kutusu kullanıcıya IR'ı değil, denetleyicinin gerçekten doğruladığı ifadeyi gösterir. Test: geri yazılan metin
yeniden ayrıştırıldığında onaylanan IR'ın özetini verir.

Güven tabanı küçük tutulur ki elle incelenebilsin; mypy katı denetimi, mutasyon testi ve K-1 incelemesi bu dosyalara
odaklanır.

### 6.4. Etiketler ve karar tablosu

| Etiket | Türkçe | Anlamı | v1 |
| --- | --- | --- | --- |
| `PROVEN` | KANITLANDI | Matematiksel kanıt kabul edildi **ve** tam süreç koşulları sağlandı: yeterlikli heyet, doğrudan insan onayı, köken | Yok (S-20) |
| `CERTIFIED` | MATEMATİKSEL SERTİFİKA DOĞRULANDI | Gösterilen iddianın istenen bütün özelliklerinin sertifikası bağımsız denetleyicide kabul edildi | Var |
| `CROSS_VALIDATED` | ÇAPRAZ DOĞRULANDI | Bağımsız iki yol aynı sonucu verdi ve sınır testleri geçti; sertifika yok | Var |
| `REFUSED` | REDDEDİLDİ | Rigor cevap vermiyor; nedenini ve ne gerektiğini söylüyor | Var |

`Label` türü dört değerlidir (sözleşme, §6.15); v1 kodunda `PROVEN` döndüren bir yol yoktur. S-20'nin "kod
değişmeden açılamaz" şartı böyle sağlanır; ayrı bir açma sabiti ya da ayar yoktur (G-12).

Her motor çalışmasının sonucu dört türden biridir (G-11): `AGREE` (diğer yolla aynı), `DISAGREE`, `UNKNOWN` (motor
karar veremedi ya da süre aştı), `NOT_RUN`.

`decide_label` yukarıdan aşağıya ilk uyan satırı seçer **[Ö]**:

1. Herhangi bir ret nedeni varsa → `REFUSED(neden)`. Ret nedenleri tek bir `RefusalCode` listesindedir (§6.4.1).
   İki yoldan biri `DISAGREE` ise ret nedeni `ENGINE_DISAGREEMENT`'tır; sertifika kabul edilmiş olsa bile.
2. [F8'de eklenir] `PROVEN`.
3. Soru türünün istediği bütün özelliklerin (§6.5) sertifikası denetleyicide kabul edildi → `CERTIFIED`. Diğer
   yolun `UNKNOWN` ya da `NOT_RUN` olması bunu engellemez.
4. İki bağımsız yol (aşağıdaki tanım) `AGREE` ve sınır testleri geçti → `CROSS_VALIDATED`.
5. Hiçbiri → `REFUSED(NO_ADEQUATE_EVIDENCE)` ve `solver_verdict` tanı kaydı (ör. "Z3 `unsat` dedi; denetlenebilir
   ispat nesnesi yok, ikinci yol çalışmadı"). Tanı kaydındaki değer sonuç olarak sunulmaz.

**Bağımsız iki yol [Ö]** (G-2): iki yol farklı motor ve farklı derleyici modülü kullanır; ortak olan yalnızca IR,
`parse` ve işlem anlamı profilidir. Aynı kütüphanenin iki algoritması (ör. SciPy DOP853 ve Radau) bağımsız sayılmaz.
Evrensel (∀) ve `unsat` iddialarında ikinci yol iddiayı bir karar yöntemiyle vermelidir; rastgele noktalarda
denemek bir yol sayılmaz. Hangi yol çiftlerinin bağımsız sayıldığı, sayısal uyuşma toleransları (mutlak ve göreli)
ve sınır testleri kümesi sürümlü politika dosyasında sayıyla yazılır (F1). Raporda iki yolun ortak bileşenleri
adıyla listelenir.

**Tavanlar:** alan paketi hesap başına en yüksek etiketi veri olarak taşır; etiket tavanı aşıyorsa tavana indirilir.
Kullanıcıya gösterilmeyen iç sıra (`PROVEN > CERTIFIED > CROSS_VALIDATED > REFUSED`) yalnızca bunun içindir.

#### 6.4.1. Ret nedenleri (v1)

`MISSING_VALUE` (K4), `DIMENSION_MISMATCH`, `UNDERDETERMINED`, `INCONSISTENT`, `DEFINEDNESS_UNPROVEN`,
`SEMANTICS_NOT_PRESERVED`, `UNSUPPORTED_MATH`, `PARSE_REJECTED`, `RESOURCE_LIMIT`, `ENGINE_DISAGREEMENT`,
`CERTIFICATE_REJECTED`, `NO_ADEQUATE_EVIDENCE`, `UNSUPPORTED_FILE`, `CEILING_REFUSED` (paket tavanı `REFUSED`).
Yeni kod ancak bu listeye eklenerek doğar; F6 ve sonrası kendi kodlarını ekler.

### 6.5. Sertifika iddiaları ve bağımsız denetleyici

**İddia özellikleri:** `WITNESS_VALIDITY` (verilen değer koşulları sağlıyor), `COMPLETENESS` (başka çözüm yok),
`UNIQUENESS` (tek çözüm), `IDENTITY` (iki ifade bütün tanımlı noktalarda eşit), `POLICY_OUTPUT` (belirtilen `Decimal`
politikasının çıktısı).

**Hangi özelliklerin isteneceğini soru türü belirler, çözücü değil [Ö]** (G-1):

| Soru türü | İstenen özellikler | Gösterim |
| --- | --- | --- |
| Hesapla (`evaluate`) | `WITNESS_VALIDITY` ya da `POLICY_OUTPUT` | Değer |
| Çöz (`solve`), alanı belirtilmiş | `WITNESS_VALIDITY` + `COMPLETENESS` | Çözüm kümesi, alanıyla |
| Tek çözüm iste | `WITNESS_VALIDITY` + `UNIQUENESS` | Değer |
| Özdeşlik denetle (B1) | `IDENTITY` | Doğru / yanlış ve karşı örnek |

Denetleyici bir özelliği kanıtlayamıyorsa o soru `CERTIFIED` alamaz. "Çöz" sorusunda tamlık kanıtlanmadıysa sonuç
"çözüm kümesi" diye değil "doğrulanmış adaylar" diye sunulur ve en çok `CROSS_VALIDATED` alır (bağımsız iki yol
kümeyi aynı bulduysa).

**Denetleyicinin kapsamı [Ö]** (G-4, G-Z4): F0'da v1 kabul envanterinin (R1–R11, B1, B2) her hesabı için "hangi
özellik, hangi denetleyici yeteneği" tablosu çıkarılır. Denetleyicinin v1 kapsamı tam olarak bu tablonun gerektirdiği
yeteneklerin birleşimidir; tabloda karşılığı olmayan yetenek yazılmaz. Aday yetenekler:

- Rasyonel ve tamsayı aritmetiği: dört işlem, tamsayı üs, karşılaştırma, profildeki `mod` işlemleri.
- `Decimal` politikasının yeniden oynatılması: hassasiyet, yuvarlama modu, işlem sırası ve yuvarlama noktaları
  sertifikanın parçasıdır (Y-10).
- Rasyonel aralık iddiaları: ör. `v ∈ [a, b]` iddiası, `v² = X` ise `a² ≤ X ≤ b²` ile denetlenir.
- ℚ üzerinde polinom özdeşliği; payda sıfır olmama yükümlülüğüyle rasyonel fonksiyon özdeşliği.
- SI birim dönüşümleri, kendi rasyonel katsayı tablosuyla (pint'ten bağımsız), yalnızca envanterdeki birimler.

Envanterde denetleyicinin kapsamadığı hesabın tavanı baştan `CROSS_VALIDATED` yazılır. Trigonometri, `sqrt`, `exp`,
`log` gibi işlemler için denetleyiciye yetenek eklemek ayrı bir faz kararıdır; F3 ya da F4 içinde sessizce eklenmez.
Eski §5.3'te `PROVEN` yazan satırlar v1'de otomatik olarak `CERTIFIED` olmaz.

**İzin listesi:** denetleyicinin içe aktarabileceği modüller tek dosyada yazılır (öneri: `fractions`, `decimal`,
`dataclasses`, `enum`, `typing`). import-linter sözleşmesi ve ayrı süreçteki `sys.modules` testi o dosyayı okur.
Kanonik JSON ve SHA-256 denetleyicide değil köprüdedir.

**Denetleyicinin kendi doğruluğu [Ö]** (G-10): yalnızca standart kütüphane kullanmak doğruluğun kanıtı değildir.
Üç ayrı test: (1) üretilmiş sahte sertifikalar (her özellik × her alan için, tür başına en az 50) reddedilmeli;
(2) Hypothesis ile rastgele ifadelerde SymPy ve flint'e karşı farklılık testi; (3) denetleyici ve köprüde mutasyon
testi.

### 6.6. Girdi yolları

| Yol | Ne | Formülün yazarı | v1 |
| --- | --- | --- | --- |
| Kurucu API | `rigor.given(...)`, `rigor.unknown(...)`, `rigor.eq(...)` ile Python'da IR kurmak | Kullanıcı | Var |
| Doğrudan matematik (SDK, CLI) | Katı ayrıştırıcıdan bütünüyle geçen ifade metni | Kullanıcı | Var |
| Doğrudan matematik (MCP) | Aynı metin, çağıran ajan iletir | Ajan aktardı | Var |
| Dosya | `.eng`, xlsx, CSV: verilen değerler; dosya özeti ve satır konumuyla | Dosya (`USER_FILE`) | Var (F3, F4) |
| Ajanın IR'ı | Çağıran ajanın JSON olarak yazdığı IR | Ajan yazdı | F6 |
| Doğal dil | Metinden denklem çıkarma | Rigor'un formülatörü | F6 |
| PDF / DOCX | Belge okuma | Rigor'un formülatörü | F9 |

Katı ayrıştırıcının dilbilgisi **[Ö]** (M-10, Y-14): Python ifade sözdiziminin bir alt kümesi; `**` üs, `^`
reddedilir; örtük çarpım (`5x`) reddedilir; `==`, `<=`, `<`, `>=`, `>` ilişkiler; Unicode eksi ve üst simgeler
sessizce çevrilmez, reddedilir; ondalık ayırıcı nokta, virgül reddedilir; hangi değişkenin çözüleceği açıkça verilir.
Belirsiz her durum soru ya da red olur. Dilbilgisi `docs/` altında yayımlanır ve Hypothesis ile "ayrıştır → yaz →
ayrıştır" özdeşliği sınanır.

**Tek köken kaydı [Ö]** (G-Z10): her verilen değer ve her ifade tek bir kayıt taşır: kaynak (`USER_DIRECT`,
`VIA_AGENT_UNVERIFIED`, `USER_FILE`), formülün yazarı (`user`, `agent`, `file`) ve kanal (`sdk`, `cli`, `mcp`).
Kayıt arayüz katmanında, çağrının nereden geldiğine bakılarak yazılır; girdinin içinde gelen köken alanları yok
sayılır (ajan "bunu kullanıcı yazdı" diyemez). MCP'den gelen her şey `VIA_AGENT_UNVERIFIED`'dir.

**Eksik değer [S]** (K4): bir `given` değersizse sonuç `MISSING_VALUE` ve gereken değerlerin listesidir. Ajan eksik
değeri sonraki çağrıda verirse değer `VIA_AGENT_UNVERIFIED` olarak kaydedilir ve kutuda görünür.

### 6.7. Onay (v1'de yok; F6 tasarımı)

v1'de onay sorulmaz (§2, S-24'ün yeri). Kutu formülün yazarını ve kaynağını yazar; formülü kullanıcıdan başkası
getirdiyse "Kapsam: yalnızca gösterilen denklem; tanımı kullanıcı onaylamadı" satırı her zaman vardır.

F6 için bağlayıcı kurallar **[Ö]**, bugünden yazılır ki F6 planı bunlardan sapmasın:

- Onay durumları: `CONFIRMED`, `CORRECTED`, `DELEGATED` ("bilmiyorum"), `REJECTED`, `ECHO_ONLY`, `AGENT_ASSERTED`.
- `CONFIRMED` ve `CORRECTED` yalnızca `responding_principal = user` olan güvenilen bir onay bağdaştırıcısından
  (işletim sistemi penceresi) üretilebilir. Ajanın `rigor_confirm` çağrısı ve MCP elicitation yanıtı
  `AGENT_ASSERTED` üretir; kutu "kullanıcı onaylamadı" yazar (G-5, Y-4).
- "Kabul edildi ve karar = onay" açık kural; reddetme ve iptal son durumdur, başka kanaldan yeniden sorulmaz (Y-5).
- `CORRECTED` sonrası yeniden onay turu sınırlıdır (A-10; F6 planında sayıyla).
- Kanal kayıt alanları: `transport_channel`, `responding_principal`, `human_presence_evidence`.

### 6.8. Oturum ve çağrı modeli (v1)

- **Durumsuz çağrılar [Ö]** (G-Z1, G-Z5): v1'de her çağrı kendi içinde tamdır. `rigor_solve` (ve CLI `rigor solve`)
  sonucu, kutuyu ve rapor yolunu döndürür ya da `MISSING_VALUE` ile gereken değerleri listeler; ajan değerleri ekleyip
  yeniden çağırır. Kalıcı oturum, iş kimliği, kilit, tekrar anahtarı ve `expected_revision` F6'dadır.
- **Oturum** saf durum makinesidir ve tek çağrı içinde yaşar: `NEEDS_INPUT` → `RUNNING` → `DONE` / `REFUSED`. Her
  adım bir olay üretir; olaylar saklanmaz, rapora gömülür.
- **Değişmez kural:** çözülen IR'ın özeti = raporlanan IR'ın özeti = (F6'da) onaylanan IR'ın özeti (B-8).
- **Çözücü alt süreci:** `rigor.runner` çözücüleri bir alt süreçte süre ve bellek sınırıyla çalıştırır; çekirdek
  alt sürecin içinde saf olarak çalışır. Aşımı ve çökmeyi kaynak olayı olarak çekirdeğe verir (§6.1 kural 2).
- **MCP:** `mcp` 2.3.0, stdio. Uzun işler v1'de beklenmediği için ilerleme bildirimi yeterlidir **[V]** (F2'de
  sahibin istemcilerinde ölçülür).

### 6.9. İşlem anlamı profili

IR'daki her işlem tek bir matematiksel anlama sahiptir; derleyici o anlamı hedef motorda koruyamıyorsa derleme
reddedilir **[Ö]** (Y-2). Profil sürümlüdür ve rapora yazılır. v1 profili en az şunları ayırır: `mod_floor`,
`mod_euclid`, `mod_trunc`; tamsayı bölmesi türleri; `Decimal` bağlamı (hassasiyet, yuvarlama modu, yuvarlama
noktaları). Negatif bölen testleri her derleyici ve denetleyici için zorunludur.

### 6.10. Kaynak sınırları

Varsayılan değerler **[Ö]**, F1'de ölçülüp sabitlenir; politika dosyasında sürümlüdür (m-9):

| Sınır | Başlangıç önerisi |
| --- | --- |
| İfade metni uzunluğu | 10.000 karakter |
| Ağaç derinliği | 200 |
| Tamsayı basamak sayısı | 10.000 |
| Üs büyüklüğü | 10.000 |
| Çözücü alt süreci süresi | çağrı başına yapılandırılır; sonsuz değil (K2) |
| Çözücü alt süreci belleği | işletim sistemi sınırıyla (`resource.setrlimit`) |

Sınır aşılırsa `REFUSED(RESOURCE_LIMIT)` ve hangi sınırın aşıldığı yazılır.

### 6.11. Alan paketleri

v1'de alan paketleri düz modüllerdir; ortak bir `DomainPack` protokolü yoktur. Protokol, iki gerçek paket görüldükten
sonra F13'te çıkarılır (G-Z7). Çekirdeğin alanları bilmediği mimari testle korunur.

- **`rocket`:** R1–R11 (eski §5.3). Hesap başına en yüksek etiket F0'daki envanter tablosundan gelir (§6.5).
  R5 ve R6 sayısal ODE: iki bağımsız yol SciPy `solve_ivp` ve mpmath `odefun` (Taylor serisi; ayrı kütüphane,
  ayrı derleyici modülü) **[V]** (F3'te R6 ölçeğinde süre ve doğruluk ölçülür; uymazsa ikinci yol yeniden seçilir
  ve bu belge güncellenir). Yakınsama için adım yarılama her yolda ayrıca yapılır. OpenRocket karşılaştırması
  CSV'den; fark bilgi olarak raporlanır, etiketi belirlemez (K17, m-7).
- **`finance`:** B1 formül denetimi (formül ile kaynakçadaki tanımın `IDENTITY` iddiası), B2 bağımsız yeniden hesap:
  aynı formül çıktı dosyasının her satırına uygulanır; `Decimal` politikası birebir (`POLICY_OUTPUT`), kapalı formlu
  istatistikler politika dosyasındaki tolerans içinde. Rastgele tohumlu hesaplar en çok `CROSS_VALIDATED`
  (eski §5.2). Kripto botunun kimliği açık belgelerde anonim kalır (K23).
- **Sentinax hazırlık özeti [Ö]** (G-6): bir formül "canlıya hazır" sayılmak için (1) B1'de `{CERTIFIED,
  CROSS_VALIDATED}` almış, (2) B2'de uyuşmazlığı yok, (3) bütün verilen değerleri `USER_FILE` ya da `USER_DIRECT`
  kaynaklı ve (4) formülün yazarı ajan değil olmalıdır. Biri eksikse "canlıya hazır değil" listesinde, nedeniyle.
  Optimizasyon çıktıları (HRP, CVaR, risk paritesi) F11'e kadar "denetlenmedi" listesinde.

### 6.12. Rapor ve özet kutusu

Her sonuçla dört alanlı bir kutu gelir **[Ö]** (R-1):

| Alan | İçerik |
| --- | --- |
| Sonuç | Değer, çözüm kümesi (alanıyla) ya da doğrulanmış adaylar; etiket |
| Doğrulanan iddia | Denetleyicinin geri yazdığı ifade; hangi özellikler; hangi denetleyici ya da hangi iki yol |
| Kaynak | Formülü kim yazdı; değerlerin kaynağı; kapsam notu |
| Doğrulanmayan | Neyin doğrulanmadığı, etiketin nasıl yükseltilebileceği; v1'de "harcama: yok" |

Rapor: girdiler ve kökenleri, profil ve politika sürümü, motor ve kütüphane sürümleri, sertifikalar, gömülü olay
listesi. `rigor verify <rapor>` saklanan kanıtı bugünkü denetleyiciyle yeniden denetler ve iki soruyu ayrı cevaplar:
o günkü politikayla kabul edildi mi, bugünküyle ediliyor mu (Y-15'in ilk işlemi; diğer ikisi F7'de).

### 6.13. Tehdit modeli ve güvence düzeyleri

| Düzey | Saldırgan | v1'de ne korunur |
| --- | --- | --- |
| T0 | Dürüst ajan | Bütün etiketler tanımlandığı gibi |
| T1 | Özensiz ajan: yanlış aktarır, eksik değeri tahminle doldurur | Köken kaydı ajanın aktardığını gösterir; eksik değer K4 ile durur; kutu "ajan aktardı" yazar; ajan kaynaklı değer Sentinax kapısını geçemez |
| T2 | Araç argümanlarıyla yalan söyleyen ajan (ör. "bunu kullanıcı yazdı" der) | Köken arayüz katmanında yazılır, girdideki köken alanları yok sayılır; `PROVEN` hiçbir argümanla dönmez |
| T3 | Aynı kullanıcı hesabında kabuk erişimli ajan | **Garanti yok** (S-26): Rigor'u çağırmadan sonuç ve rapor uydurabilir, dosyaları değiştirebilir. README ve her rapor bunu yazar |

### 6.14. Ağ politikası

- v1'de Rigor hiçbir ağ çağrısı yapmaz **[S]** (S-29'un çalışma anına uygulanması **[Ö]**).
- Test düzeneği (F0): ana süreçte soket bağlantısı engellenir; `rigor.runner`'ın başlattığı alt süreçler aynı
  engeli bir başlangıç modülüyle (`sitecustomize`) devralır; Linux CI'da paket ayrıca ağ ad alanı olmadan çalıştırılır
  **[V]** (GitHub'ın Linux makinelerinde yetkisiz ağ ad alanı açılabildiği F0'da sınanır). Düzeneğin kendi testi:
  ana süreçte ve alt süreçte bilerek açılan bir bağlantı testi düşürmelidir.
- `rigor doctor` ağ kullanmaz; yalnızca yerel arka uçları yükleyip sürümlerini yazar (eski §8.1).
- F6'dan itibaren ağ yalnızca `rigor.llm` içinden ve dört ayrı izinden (Y-9) sonra açılır; K-3 kapısı bunu denetler.

### 6.15. Dışarıya açılan sözleşmeler

Sonraki fazların kırmaması gereken, v1'de dışarıya açılan şeyler **[Ö]** (B-8). Başka genişleme noktası
önceden kurulmaz (G-Z8):

- `Label` dört değerli; JSON çıktısında da.
- Rapor ve JSON çıktısında `schema_version`; köken kaydı alanları; ret kodu listesi (yalnızca eklenir).
- CLI çıkış kodları, JSON çıktı şeması, MCP araç şemaları (F2'de yazılı sözleşme belgesi).
- IR şeması: `Table` ve aralıklı girdi düğümleri F1'de veri modeline girer (motorları F3'te). K-1'den sonra IR'da
  ya da denetleyicide yapılan her değişiklik `schema_version` artırır ve K-1 ölçütlerini yeniden çalıştırır.

### 6.16. Altın set

"Yanlış etiket" ölçütleri bu sete karşı ölçülür **[Ö]** (G-I1):

- **Satır şeması:** girdi, soru türü, beklenen etiket, beklenen ret nedeni, beklenen değer ya da küme, gerekçe,
  doğru cevabın kaynağı.
- **Doğru cevap:** Rigor'dan bağımsız belirlenir (el hesabı, kaynakçadaki değer ya da Rigor'un kullanmadığı bir araç)
  ve kaynağı satıra yazılır.
- **Yanlış etiket:** beklenenden yüksek bir etiket ya da olumlu etiketle yanlış değer.
- **Alt sınırlar:** karar tablosunun her satırı, her ret kodu ve her tuzak sınıfı (Y-1, Y-2, Y-3, Y-10, Y-12, Y-13,
  Y-14, eksik değer) için en az 5 satır; v1 kabul envanterindeki her hesap için en az 2 satır (biri kasıtlı bozuk).
- Set depoda; sahibin gerçek dosyalarıyla yapılan yerel kabul ayrıdır (faz planı §2).

## 7. V1 sınırları

### 7.1. V1'de var

- Etiketler `CERTIFIED`, `CROSS_VALIDATED`, `REFUSED`; `PROVEN` kodda yok.
- Girdi: kurucu API, katı ayrıştırıcı (SDK, CLI, MCP), `.eng` / xlsx / CSV dosyaları.
- Çekirdek: IR, işlem anlamı profili, birim, yapı ve tanımlılık kapıları, SymPy / Z3 / Arb, bağımsız denetleyici ve
  köprü, soru türüne bağlı iddia özellikleri, karar tablosu.
- Roket R1–R11, OpenRocket CSV karşılaştırması; finans B1 ve B2 (bot ve Sentinax), Sentinax hazırlık özeti.
- Arayüzler: Python SDK; `rigor doctor | solve | audit | reconcile | report | verify`; MCP araçları `rigor_solve`,
  `rigor_audit_formula`, `rigor_reconcile`, `rigor_report`; hepsi eşzamanlı.
- Platform: macOS ve Linux; Python 3.12, 3.14, 3.15.
- Ağ yok, model çağrısı yok, harcama yok, onay ekranı yok, kalıcı oturum yok.

### 7.2. V1'de yok (iptal değil; yeri faz planında)

| Özellik | Faz |
| --- | --- |
| Doğal dil yolu, ajanın IR'ı, Rigor'un kendi formülatörü, başsız istemci (sağlayıcı başına bayrak), dört izin, bütçe, 15 dakika kuralı, harcama satırı, iş sonu bildirimi; onay ekranı ve üç seçenek (S-11, S-24), onay bağdaştırıcıları, elicitation; iş modeli, kalıcı oturum, tekrar anahtarı; `RIGOR_DEPTH`; yoklama soruları (M-6) | F6 |
| Çoklu formülasyon, denklik denetleyicisi, geri çeviri, mutasyon, LLM ile sade anlatım ve koruması, okunabilirlik; yeniden üretimin ikinci ve üçüncü işlemi (Y-15) | F7 |
| Yeterlik kayıtları, heyet, heyet kabulü, kayıt dağıtımı, `PROVEN`, toplayıcıların katkı kuralı (A-4) | F8 |
| PDF / DOCX okuyucu, toplu onay ekranı, `.ork` okuyucu | F9 |
| Kayıtlı şablonlar ve öz-denetim (K18), alarm hakemliği ve öğrenme defteri (K19), şablonlarda kayıt geçerliliği (M-5) | F10 |
| Optimizasyon: HiGHS, CVXPY, LP dual, MILP ve KKT profilleri (Y-11) | F11 |
| Lean 4 (K26) | F12 |
| `DomainPack` protokolü, alan uyarlama araçları (`rigor domain new / verify / bench`), `fluids` paketi, PDE, geniş alan altın seti | F13 |
| Windows, DeepSeek Harness (A-9), birinci sınıf İngilizce, roket R12–R14 | F14 |

## 8. V1 sonrası hedefler

1. **Yabancı kullanıcıya tam akış (F6, F7):** "Bu problemi çöz" denen ajanın arkasında Rigor metinden denklemi
   çıkarır, Doğru / Yanlış / Bilmiyorum diye sorar, çözer; veri sağlayıcıya ancak izinle gider.
2. **`PROVEN`'ın geri gelmesi (F8):** yalnızca ölçülmüş yeterlik, iki aileli heyet, doğrudan insan onayı ve imzalı,
   güncel kayıt dağıtımıyla. Yanlış `PROVEN` = 0 ölçütü bağımsız sette.
3. **Matematik kapsamı (F11, F12, F13):** optimizasyon, soyut ispat, alan paketleri.
4. **Erişim (F9, F14):** belge okuma, Windows, ek istemciler ve diller.

## 9. Açık kalanlar

| No | Soru | Kimin | Engellediği |
| --- | --- | --- | --- |
| A-4 | Toplayıcıdan gelen üye en üst etikete katkı verir mi | Sahip (araştırıldı) | F8. O zamana kadar katkı yok |
| A-6 | İlk ölçülecek görev profili | Sahip | F8 |
| A-7 | Kayıtların sürümden bağımsız güncellenme yolu | Tasarımcı | F8 |
| A-9 | DeepSeek Harness'in yeri | Sahip | Hiçbir şey (F14) |
| A-10 | "Yanlış" seçeneğinde düzeltmenin biçimi ve tur sınırı | Tasarımcı | F6 planı |
| D-1 … D-3 | Sağlayıcı koşulları ve faturalandırma | Birincil kaynak | F6 (K-3) |
| D-6, D-7, D-9 | İstemcilerde elicitation; şema sınırları; MCP 2026-07-28 akışı | Birincil kaynak | F6 |
| D-10 | Pydantic 2.14'te `frozen` | Deney | F0 |
| T-10 | Proje ayarından eklentilerin çıkarılması | Sahip | Hiçbir faz; S-30'un uygulanması |
| — | v1 finans envanterinin sahipçe dondurulması | Sahip | F0 çıkışı |

A-2, A-3, A-5, A-8, A-11, A-12, A-13, A-14 S-20 … S-27 ile kapandı.

## 10. Kaynaklar

- Karar kaydı ve içindeki kaynakça: [`../decisions/2026-11-10-karar-kaydi.md`](../decisions/2026-11-10-karar-kaydi.md).
- ATM araçlarının Rigor'a uygunluk raporu (23 kayıt):
  [`../research/2026-11-11-atm-arac-uygunluk-raporu.md`](../research/2026-11-11-atm-arac-uygunluk-raporu.md).
- AI-Toolchain-Manager, `development` dalı (2026-11-11'de okundu): `data/catalog-seed.json`,
  `docs/TOOL-COMPATIBILITY.md`, `docs/catalog-03/RISK_AND_OVERLAP.md`, `docs/GITLEAKS-PILOT-ASSESSMENT.md`.
- [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp): README, v0.11.0 ve v0.12.x sürüm notları.
- [Graphify](https://github.com/Graphify-Labs/graphify): README "Privacy"; güvenlik bildirimi GHSA-pcc4-rvhr-2pr8.
- [Gitleaks](https://github.com/gitleaks/gitleaks), [Betterleaks](https://github.com/betterleaks/betterleaks),
  [Superpowers](https://github.com/obra/superpowers), [EGM](https://github.com/google/elephant-goldfish-model):
  depo ve sürüm bilgileri (GitHub API, 2026-11-11).
- PyPI JSON API (2026-11-11): ruff, pytest, hypothesis, import-linter, mypy, mutmut, pip-audit, mcp, pydantic,
  sympy, z3-solver, python-flint, pint, scipy, mpmath, graphifyy, codebase-memory-mcp.

## 11. Taze gözlü inceleme (2026-11-11)

**Yöntem:** üç EGM inceleme ajanı birbirini ve sohbeti görmeden, daha ucuz modelle (`sonnet`) çalıştı (S-31):
mimari eleştiri (G-1 … G-15), uygulamaya hazırlık (faz planı; G-I1 … G-I15), kapsam ve sadelik (G-Z1 … G-Z12).
Bulguları ana ajan birleştirdi. 42 bulgunun 39'u kabul edildi, 3'ü kısmen kabul edildi; reddedilen yok.

**Kabul edilip bu belgeye işlenenler (özet):**

| Bulgu | Değişiklik |
| --- | --- |
| G-1 kısmi çözüm kümesi `CERTIFIED` olabiliyordu | İstenen özellikleri soru türü belirler; tamlık yoksa "doğrulanmış adaylar" (§6.5) |
| G-2, G-I8, G-Z12b bağımsız iki yol tanımsız | Tanım, politika dosyası, ODE için ayrı kütüphane (§6.4, §6.11) |
| G-3 köprü güven tabanında değildi | Köprü, ayrıştırıcı güven tabanında; denetleyici doğruladığını geri yazar (§6.3) |
| G-4, G-Z4, G-Z12c denetleyici kapsamı envanterden önce sabitleniyordu | Kapsam F0'daki envanter tablosundan türer (§6.5) |
| G-5 ajan `CONFIRMED` üretebiliyordu | `AGENT_ASSERTED` (§6.7) |
| G-6 ajan kaynaklı değer Sentinax kapısını geçebiliyordu | Kapı köken de ister (§6.11) |
| G-7 çekirdek saflığı ile alt süreç çelişiyordu | `rigor.runner`; kaynak olayları girdi (§6.1, §6.8) |
| G-8 S-23 ile ajan IR'ı ve dosya yolu çelişiyordu | S-23'ün yorumu; ajan IR'ı F6'ya (§2, §6.6) |
| G-9, G-Z2 onay altyapısı v1'de tetiklenmiyordu | v1'de onay yok; kurallar F6 için yazılı (§6.7) |
| G-10 denetleyicinin kendi doğruluğu zayıf sınanıyordu | Üretilmiş sahte sertifikalar, farklılık testi, mutasyon testi (§6.5) |
| G-11 tek motor, `unknown`, süre aşımı tanımsızdı | `EngineOutcome` türleri ve tablodaki yerleri (§6.4) |
| G-12, G-Z8 ölü kod ve erken genişleme | `PROVEN` dalı ve yer tutucular kaldırıldı; yalnızca dışa açılan sözleşmeler (§6.15) |
| G-13, G-I10 3.15 bağımlılık uyumu | F0'da bütün bağımlılıklar; olmazsa sahip kararı (§5.3) |
| G-14 olay kaydı bütünlüğü | Kalıcı olay kaydı v1'den çıktı; F6 planının giriş maddesi |
| G-15 ret kodları iki yerde farklı | Tek liste (§6.4.1) |
| G-Z1 iş modeli v1'e ağır | Eşzamanlı araçlar; iş modeli F6 (§6.8) |
| G-Z3 `verify-report` ile `replay` aynı iş; `RIGOR_DEPTH` v1'de gereksiz | Tek `rigor verify`; `RIGOR_DEPTH` F6 |
| G-Z5 kalıcı oturum ve şablon deposu v1'de gereksiz | Durumsuz çağrı; şablonlar F10 (K18) |
| G-Z6 araç tekrarları | `sys.modules` testi yalnızca denetleyicide; `pip-audit` kurulu araç değil |
| G-Z7 `DomainPack` erken soyutlama | F13 (§6.11) |
| G-Z10 iki köken sözlüğü | Tek köken kaydı (§6.6) |
| G-Z11 geniş CLI ve MCP yüzeyi | v1 yüzeyi daraldı (§7.1) |
| G-I1 altın set tanımsız | §6.16 |
| G-I2 ağ engeli düzeneği kurulmuyordu | §6.14, F0 |
| G-I9 denetleyici izin listesi uygulanamazdı | İzin listesi dosyası (§6.5) |
| G-I12 `Table` ve aralık düğümü K-1'den sonra IR'ı değiştiriyordu | F1 veri modelinde; sonrası `schema_version` (§6.15) |

Faz planına giden bulgular (G-I3 … G-I7, G-I11, G-I13 … G-I15) planın kendisine işlendi.

**Kısmen kabul edilenler:**

- **G-Z3 tehdit modeli tablosu README'de iki cümleye insin:** tablo bu belgede kalır; README'de kısa hali olur.
  Gerekçe: S-26'nın "açıkça yazılır" şartı, hangi düzeyde neyin korunduğunun yazılmasıyla karşılanır.
- **G-Z4 denetleyiciden birim tablosu çıkarılsın:** kesin karar F0 envanterine bırakıldı. R1 (birim dönüşümü) bir
  v1 kabul hesabıdır; katsayıyı pint verirse `CERTIFIED`'ın güveni pint'e geçer.
- **G-Z6 `mypy` kapsamı yalnızca denetleyici ve etiketler olsun:** kapsam güven tabanının tamamıdır (§6.3), çünkü
  ayrıştırıcı ve köprü de etiketin doğruluğunu belirler.
