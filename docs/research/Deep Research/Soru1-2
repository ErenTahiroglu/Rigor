# Rigor — Deep Research III  
## Açık mimari kararların uzlaştırılması ve geliştirmeye esas karar önerisi

Bu aşamadaki önerim, önceki iki rapordan önemli ölçüde farklıdır:

**KANITLANDI** üst sonuç etiketi, sahibin yeni onayı olmadan yalnızca matematiksel alt iddianın etiketi olarak yeniden tanımlanmamalıdır. `concepts_brief.md` içindeki Karar 5 bağlayıcıdır: yalnızca ücretsiz modellerle değerlendirilen sonuç bu etiketi alamaz. Buna karşılık, denetlenmiş matematiksel sertifikanın gücü de saklanmamalı veya “yaklaşık hesap” gibi gösterilmemelidir. [concepts_brief.md]

Bu iki gerekliliği birlikte karşılayan en güçlü seçenek şudur:

- Üst düzey sonuç etiketi ile matematiksel sertifika durumu ayrılır.
- `PROVEN / KANITLANDI`, Rigor’un bütün zorunlu güvence koşullarının tamamlandığı sonuçlar için korunur; doğal dil niyetinin matematiksel olarak ispatlandığı iddia edilmez.
- Yeni `CERTIFIED / SERTİFİKA DOĞRULANDI` etiketi, matematiksel iddiası kabul edilmiş fakat tam hakemlik koşulları tamamlanmamış sonuçlar için kullanılır.
- `CROSS_VALIDATED / ÇAPRAZ DOĞRULANDI`, gerçekten ayrı hesaplama yöntemleri karşılaştırılmışsa kullanılır.
- Bunlar tek bir “doğruluk olasılığı merdiveni” olarak sunulmaz.
- Faz 1’de `PROVEN` verilmez. Bağımsız sertifika denetimi gerçekten eklendiği ölçüde `CERTIFIED` verilebilir.

Bu etiket seçimi bir bilimsel zorunluluk değil, bağlayıcı kararlar ve teknik kanıtlarla uyumlu bir tasarım tercihidir. Özellikle “HESAP KANITLI” yerine “SERTİFİKA DOĞRULANDI” adını öneriyorum: ikincisi yapılan kontrolü adlandırır ve bütün problemin doğru olduğu çağrışımını bir miktar sınırlar. Bunun Türkçe kullanıcılarla doğrulandığını iddia etmiyorum.

## 1. İnceleme kapsamı, kanıt hiyerarşisi ve sınırlamalar

### 1.1. Birincil girdiler

`concepts_brief.md` eksiksiz okundu. Belge, altı sahip kararını bağlayıcı; uzlaştırma taslağını ve altı sorunun çözümünü ise açık olarak tanımlıyor. Red Team görüşleri bu raporda bağımsız iddialar olarak ele alındı. [concepts_brief.md]

Önceki iki araştırma raporu bu konuşmada mevcut. Bunları değerlendirdim; ancak belgede anılan depodaki `docs/research/Deep Research/1` dosyasının ayrı bir kopyasını okumuş olduğumu iddia etmiyorum.

### 1.2. Doğrulanan GitHub sürümleri

10 Kasım 2026 tarihindeki yeniden kontrolde:

| Dal | Commit SHA | Önceki aşamaya göre |
|---|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` | Değişmedi |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` | Değişmedi |

İncelenen geliştirme belgelerinin Git blob kimlikleri:

| Belge | Blob SHA |
|---|---|
| README | `5be11d62e714b111143acdb91d5709a33147d520` |
| Handoff | `1a1006c3e2c4d2eaab59d982b6d2f597de74a848` |
| Tasarım belgesi | `a509f1287726fe8922b0d7a46fbf18e5b4d55896` |
| Araştırma notları | `a27db81739851ac17bc9afbd85b82368ad357cff` |
| Faz 1 planı | `8bed859fe37cd80dc1500fb92b9dcdeeabe1b741` |
| Yol haritası | `97afa66e18678bf43b758bd6ced844e46fd949e9` |

GitHub sonuçları bu oturumda numaralı kaynak kimliği üretmediğinden bunlara uydurma atıf eklemiyorum. Yukarıdaki commit ve blob kimlikleri depo bulgularının denetim dayanağıdır.

### 1.3. Kapatılamayan erişim açığı

Uzun tasarım ve Faz 1 dosyalarının araç yanıtları yine kesildi. Bu turda kod aramasıyla şu hükümler ayrıca doğrudan görüldü:

- §6.3’te çözüm noktasında sembolik Jakobiyen rank kontrolü.
- §6.4’te varsayılan üç aday IR, birbirlerinin çıktısını görmeme ve değişken hizalama.
- §6.7’de deterministik iskelet ve başarısız sadeleştirmede iskelete dönüş.
- §8.2’de açık model kimliği, fallback yasağı, semantik önbellek yasağı ve aynı ham yanıtı reddetme kuralı.

Buna rağmen §6.3–§6.8’in tamamı ile Faz 1’in kesilen son kısmının eksiksiz satır denetimi tamamlanmış değildir. Özellikle `confirm_uniqueness` için arama sonuç vermedi; GitHub kod aramasının `main` üzerinden sonuç vermesi, geliştirme dalındaki plan için bu yokluğu kanıtlamaz.

Bu sınırlama, “bütün belge hükümleri doğrudan doğrulandı” başarı ölçütünü açık bırakıyor. Aşağıdaki öneriler bunu saklamadan hazırlanmıştır.

### 1.4. Kullanılan kanıt sınıfları

- DOĞRULANDI: Birincil kaynak veya doğrudan görülen teknik hüküm.
- DESTEKLENİYOR: Kanıtlar yön gösteriyor; genel garanti yok.
- TASARIM TERCİHİ: Gerekçeli mimari seçim.
- BELİRSİZ: Yeterli kanıt veya tanım yok.
- SAHİP ONAYI GEREKLİ: Bağlayıcı tercih veya mevcut sözleşme değişiyor.

Bu sınıflar bir güven yüzdesi veya birbirinin yerine geçen etiketler değildir.

## 2. Önceki rapor ile Red Team arasındaki anlaşmazlıklar

### 2.1. Red Team’in haklı olduğu noktalar

| İtiraz | Karar | Gerekçe |
|---|---|---|
| Önceki rapor yeni altı kararı bilmiyordu | DOĞRULANDI | Yeni ana girdi artık bu kararları içeriyor.  [concepts_brief.md] |
| Faz 1’e `PROVEN` önermek mevcut tavanı değiştiriyordu | DOĞRULANDI | Faz 1 planı Red Team yokken `PROVEN`ı açıkça yasaklıyor. |
| Bağımsız denetleyici kutusu mevcut Faz 1 kabiliyeti gibi yazılamaz | DOĞRULANDI | Görülen Görev 10, SymPy tabanlı geri ikame içeriyor; ayrı küçük denetleyici göstermiyor. |
| Deterministik sade anlatım yeni öneri değildi | DOĞRULANDI | §6.7 parçaları ve yol haritası bunu zaten içeriyor. |
| Büyük `KANITLANDI` başlığına genel feragat eklemek yeterli savunma değildir | DESTEKLENİYOR | HCI kanıtı, açıklamanın aşırı güveni tek başına gidermediğini gösteriyor.  [arxiv](https://arxiv.org/html/2102.09692v1) |
| Grafik ve çok sayıda durum v1 için ağır olabilir | TASARIM TERCİHİ | Fayda–maliyet dengesi var; tam SACM zorunluluğu yok. |

Önceki raporun “yapısal eşleme tekliği kanıtlamaz” önermesi matematiksel olarak doğruydu. Fakat bunu Rigor’da teklik kontrolü hiç yokmuş gibi yorumlamak yanlıştı. §6.3’te rank kontrolü bulunduğu bu turda doğrudan doğrulandı. Bu nedenle eleştiriyi “eksik özellik” olarak geri çekiyorum; yalnızca bu kontrollerin test kapsamının incelenmesi gereği kalıyor.

### 2.2. Red Team’in aşırı veya eksik yorumladığı noktalar

#### “Anahtarsız kullanıcı artık ücretsiz heyet sahibidir”

Bu, hedeflenen deneyim olabilir; teknik olarak garanti değildir.

Groq hızlı başlangıcı API anahtarı oluşturulmasını istiyor. Ücretsiz katman da kimlik doğrulama, kota ve erişim koşullarına bağlı. OpenRouter API’si de anahtar kullanıyor ve ücretsiz modeller için ayrı limitler uyguluyor. Dolayısıyla ücretsiz erişim, anahtarsız erişim değildir. [console.groq](https://console.groq.com/docs/quickstart)

Sonuç: Karar 2, “her kurulumda ücretsiz heyet kesin vardır” şeklinde uygulanamaz. “Erişilebilen ve kullanıcı tarafından yetkilendirilmiş heyet çalıştırılır; yoksa bu durum açıkça raporlanır” şeklinde uygulanmalıdır.

#### “Buçinca çalışması önceki kutunun yanlış olduğunu kanıtlıyor”

Çalışma, 199 katılımcıyla belirli karar destek görevlerinde bilişsel zorlayıcı adımların basit açıklamalara göre aşırı güveni azaltabildiğini gösteriyor. Rigor’daki belirli Türkçe kutuyu veya tek başına bir onay düğmesini sınamıyor. Üstelik müdahaleler aşırı güveni tamamen ortadan kaldırmıyor. [arxiv](https://arxiv.org/html/2102.09692v1)

Sonuç: Önceki kutuya güçlü bir risk itirazıdır; belirli alternatifin deneysel doğrulaması değildir.

#### “Hakemler oylamıyor; bu yüzden korelasyon eleştirisi geçersiz”

Rigor’un ayrı formülasyon + formal denklik yaklaşımı, çıplak cevap oylamasından daha güçlüdür. Ancak üç model de aynı yanlış yorumu üretirse denklik denetleyicisi onların birbirine eşdeğer olduğunu doğru biçimde gösterebilir. Bu, kaynak niyetine uygunluğu kanıtlamaz.

Formülasyonlar arası eşdeğerlik ile doğal dil açıklamasına uygunluk farklı iddialardır. SOVER da formal eşdeğerlik kontrolünde değişken eşlemesini ayrı bir adım olarak ele alır; yanlış veya eksik eşleme hata kaynağı olarak kalır. [aclanthology](https://aclanthology.org/2026.findings-emnlp.1886/)

#### “Örnek kutudaki üç ücretsiz model ve kullanıcı onayı”

Bu bilgiler yalnızca gerçekten kaydedilmişse yazılabilir. Anahtarı olmayan kullanıcı örneğine otomatik eklenemez. Dosyadaki kutu bir taslak senaryodur; gerçekleşmiş olay kaydı değildir. [concepts_brief.md]

### 2.3. Kaynak atfı anlaşmazlıklarının çözümü

- arXiv `2509.14034`, Lin ve Hooi’nin *Enhancing Multi-Agent Debate System Performance via Confidence Expression* çalışmasıdır. Kalibre edilmiş güven ifadelerinin belirli tartışma düzeneklerinde başarıyı artırmasını araştırır. Önceki raporda ona yüklenen genel “korelasyon güven birleşimini aşırı iyimser yapar” iddiasının doğrudan kaynağı olarak kullanılmamalıdır. [arxiv](https://arxiv.org/html/2509.14034v1)
- arXiv `2506.07962`, Kim ve arkadaşlarının *Correlated Errors in Large Language Models* çalışmasıdır. %60 değeri HELM verisinde iki modelin de yanlış olduğu durumlarda aynı yanlış cevaba yönelme ortalamasıdır; bütün görevler için hata oranı değildir. İkinci rapor bu sınırı zaten belirtmişti; brief’in bunu hâlâ genel ortalama diye sunulmuş sayması ikinci raporu eksik okuyor. [concepts_brief.md]

## 3. Açık konular envanteri

| Konu | Çatışma | Önem | Önerilen karar | Kalan belirsizlik |
|---|---|---:|---|---|
| `KANITLANDI` kapsamı | Matematik etiketi / tam süreç etiketi | Kritik | Tam süreç etiketi korunur; sertifika ayrı gösterilir | Sahibin kapsam onayı |
| Sertifikalı ama eksik heyetli sonuç | `CROSS_VALIDATED` adı yanlış olabilir | Kritik | `CERTIFIED` eklenir | Türkçe adın anlaşılabilirliği |
| Ücretsiz–ücretli ayrımı | Ürün politikası / bilimsel kalite | Yüksek | Karar 5 korunur; fiyat doğruluk kanıtı sayılmaz | “Ücretli”nin operasyonel tanımı |
| Tamamen erişimsiz kullanıcı | Ücretsiz heyetin varsayılması | Yüksek | Yerel kontrollere devam; heyet yokluğu açık | Doğal dil desteğinin kapsamı |
| Toplayıcı bağımsızlığı | Model etiketi / gerçek yürütme | Kritik | Sıkı adaptör sözleşmesi | Sunucu beyanına güven sınırı |
| Önbellek | Her tür cache bağımsızlığı bozar mı? | Yüksek | Yanıt cache’i ile prompt cache’i ayrılır | Sağlayıcı uygulama ayrıntıları |
| Faz 1 denetleyicisi | Geri ikame / bağımsız sertifika | Kritik | Kabiliyet abartılmaz; küçük rasyonel denetleyici sınırlı ek | Uygulama ve test |
| Bileşim | Kesin alt adımın üst sonucu yükseltmesi | Kritik | Bağımlı girdi niteliği korunur | Karma zincir kapsamı |
| Tam güven grafiği | İzlenebilirlik / tek geliştirici yükü | Orta | v1’de düz kayıt + bağımlılık kimlikleri | İleride genişleme |
| DeepSeek Harness | Olası fayda / yeni çalışma zamanı riski | Orta | Çekirdek bağımlılık değil; sonra opsiyonel istemci | İzolasyon testi ve şartlar |

## 4. Kaynak denetimi: Hangi kaynak hangi kararı gerçekten destekliyor?

| Kaynak ve kimlik | Doğrulanan bulgu | Rigor’da etkilediği karar | Desteklemediği iddia |
|---|---|---|---|
| NIST SP 811, Ek B | Uluslararası foot tam `0,3048 m`; survey foot farklıdır | Tanım kimliği ve kesin dönüşüm | Kaynak değerin gerçekliği  [nist](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors) |
| BIPM SI Brochure, §5.4.5 | Ölçüm değeri ve belirsizliği birlikte ifade edilir | Kesin dönüşüm ölçüm belirsizliğini kaldırmaz | Foot için asıl tarihsel tanım kaynağı olduğu  [bipm](https://www.bipm.org/documents/20126/41483022/SI-brochure-9-EN.pdf) |
| CakeML, *Verified Proof Checking* | Denetleyici ve derleme zinciri doğrulanabilir; TCB kalır | Denetleyici profili ve kalan varsayımlar | Her ayrı programın otomatik güvenilirliği  [cakeml](https://cakeml.org/checkers.html) |
| Becker vd., FloVer, FMCAD 2018 | Sonlu hassasiyet hata sınırları sertifikayla kontrol edilir | Tam değer / hata sınırı ayrımı | Bütün sayısal yöntem ve parser’ların kapsandığı  [rmonat](https://rmonat.fr/data/pubs/2018/fmcad18.pdf) |
| Kapela vd., CAPD::DynSys, DOI `10.1016/j.cnsns.2020.105578` | ODE çözümleri için garantili sınırlar hesaplanabilir | Gelecekte doğrulanmış ODE yolu mümkün | Her CAPD çağrısının rigorous olduğu veya bağımsız sertifika ürettiği  [capd.ii.uj.edu](http://capd.ii.uj.edu.pl/html/index.html) |
| OMG SACM 2.3 | İddia, kanıt ve argüman bağlantıları ayrı temsil edilir | Hafif izlenebilirlik modeli | SACM kullanımının argümanı doğru yaptığı veya v1’de zorunlu olduğu  [omg](https://www.omg.org/spec/SACM/2.3/PDF) |
| NASA-STD-7009B, 2024 | Verification, validation ve kullanım güvenilirliği ayrılır | Model-içi hesap ile fiziksel geçerlilik ayrımı | Rigor’un NASA uygunluğu veya gerçek uçuş garantisi  [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) |
| Van der Bles vd., PNAS 2020 | Belirsizlik açıklamasının güven etkisi biçime ve bağlama bağlı | Somut kapsam açıklaması; gereksiz genel şüphe dili yok | Türkçe kutunun doğrulanmış UX sonucu  [pnas](https://www.pnas.org/doi/10.1073/pnas.1913678117) |
| Buçinca vd., DOI `10.1145/3449287` | Bilişsel müdahaleler bazı görevlerde aşırı güveni azaltır | Aktif tanım incelemesini koruma | “Onayla” düğmesinin tek başına yeterliliği  [arxiv](https://arxiv.org/html/2102.09692v1) |
| Kim vd., arXiv `2506.07962v1` | Farklı modellerde de ilişkili hata vardır | Aile çeşitliliği gerekli kontrol olabilir, garanti değil | Rigor’a özgü hata oranı veya ücretsiz model üstünlüğü  [arxiv](https://arxiv.org/html/2506.07962v1) |
| Lin–Hooi, arXiv `2509.14034v1` | Belirli kalibrasyon ve tartışma düzenekleri benchmark başarısını artırabilir | Gelecekte deneysel hakemlik değerlendirmesi | Formal ispat veya fiyat temelli güvence  [arxiv](https://arxiv.org/html/2509.14034v1) |
| Lean, *Validating a Lean Proof* | İspatın geçerliliği, ifade anlamı ve saldırgan kanıt kontrolü ayrılır | Sabit iddia, aksiyom politikası, yalıtım | Doğal dil niyetinin ispatlanmışlığı  [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) |
| Microsoft Z3 Guide | `unsat_core`, sağlanamayan adlandırılmış iddiaların alt kümesidir | Çekirdek ile ispat nesnesini ayırma | Çekirdeğin bağımsız denetlenmiş ispat olduğu  [microsoft.github](https://microsoft.github.io/z3guide/docs/logic/propositional-logic/) |
| SOVER, ACL Anthology | Formalizasyonlar arası eşdeğerlik, eşleme ve çözücü kontrolleriyle sınanabilir | Rigor heyetini cevap oylamasından ayırma | Kaynak metnin niyetinin koşulsuz doğruluğu  [aclanthology](https://aclanthology.org/2026.findings-emnlp.1886/) |

FloVer’in 2018 sürümünde doğrulanmış ve doğrulanmamış çalıştırılabilir yollar ile doğrulanmamış parser bileşenleri ayrı açıklanır. Bu ayrıntı, “araç formal doğrulanmış” ifadesinin bütün entegrasyon yoluna otomatik aktarılmaması gerektiğini gösterir. [rmonat](https://rmonat.fr/data/pubs/2018/fmcad18.pdf)

## 5. `KANITLANDI` çelişkisinin çözümü

### 5.1. İki ayrı iddia

Örnek için matematiksel iddia:

\[
8000\cdot\frac{381}{1250}=\frac{12192}{5}.
\]

Kullanıcıya verilen cevap iddiası ise daha geniş olabilir:

> “Bu sayı, sizin kaynak metninizdeki şartın veya mühendislik sorunuzun doğru cevabıdır.”

Birinci iddia kesin ispatla desteklenebilir. İkinci iddia; kaynak çıkarımı, birim seçimi, model seçimi, eşitsizlik yönü, kullanıcı niyeti ve onay zincirini de içerir. Formal ispat rehberi de teoremin geçerliliği ile ifadenin anlamını açıkça ayırır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

Dolayısıyla önceki raporun matematiksel ayrımı doğru, `KANITLANDI` sözcüğünün ürün içindeki anlamını sahip onayı olmadan değiştirmesi uygun değildi.

### 5.2. Alternatiflerin karşılaştırılması

| Seçenek | Güvenlik | Bilgiyi doğru taşıma | Kullanılabilirlik | Maliyet/uyum | Karar |
|---|---|---|---|---|---|
| A — Üç etiket aynen | Üst tavanı korur | Sertifikalı ama çaprazlanmamış sonuçta adlandırma sorunlu | Basit | En düşük geçiş maliyeti | Geçici çözüm |
| B — Ara etiket | Kapsam iyi tanımlanırsa güçlü | Eksik sertifika/heyet kombinasyonunu taşır | Bir yeni kavram | Orta | Gerekli parça |
| C — Tam çok boyutlu görünüm | Ayrımlar güçlü | En ayrıntılı | Basit işlerde ağır | Daha yüksek | Ayrıntı raporuna uygun |
| D — Üst etiket + zorunlu kanıt/yorum satırı | Riskleri birlikte sınırlar | Kayıp az | Dengeli | Mevcut mimariye yakın | Önerilen |
| E — Etiket yerine yalnızca kontrol listesi | Yanlış sıralama azalır | Çok açık olabilir | Hızlı tarama zorlaşır | Düşük–orta | API/uzman görünümü alternatifi |

Önerim D+B’dir; içeride sınırlı çok boyutlu kayıt tutulur.

### 5.3. Bilimsel bir sıralama var mı?

Şu sıra evrensel olarak savunulamaz:

\[
\text{ÇAPRAZ DOĞRULANDI}<\text{HESAP KANITLI}<\text{KANITLANDI}.
\]

Çünkü:

- Kesin sertifikalı bir alt hesap, yorum bakımından zayıf olabilir.
- Çok iyi incelenmiş bir ODE modeli, matematiksel hata sınırı bakımından sertifikasız olabilir.
- Daha pahalı heyet aynı yanlış yorumu paylaşabilir.
- Tek bir formal iddia için kabul edilmiş kanıt, modellerin fiyatından bağımsızdır.

Bu nedenle etiketler “kontrol kategorisi” olarak tanımlanmalıdır. `PROVEN`, `CERTIFIED` koşullarına ek süreç koşulları isteyebilir; bu mantıksal koşul ilişkisi, diğer bütün etiketlerin tek boyutlu doğruluk sıralaması olduğu anlamına gelmez.

### 5.4. Üst etiketin dürüst anlamı

Önerilen tanım:

> `PROVEN`, belirtilen formal tanıma ilişkin matematiksel kanıtın kabul edildiğini ve Rigor’un sürümlü tam güvence politikasındaki zorunlu formülasyon, kullanıcı onayı, köken ve heyet kontrollerinin tamamlandığını belirtir. Doğal dil niyetinin, giriş verisinin gerçekliğinin veya fiziksel modelin gerçek dünyaya uygunluğunun matematiksel olarak ispatlandığı anlamına gelmez.

Bu tanım Karar 5’i korur; buna rağmen “uçtan uca mutlak doğruluk” gibi desteklenemeyen bir vaat üretmez. Çoklu model ve insan incelemesi artık riski azaltabilir, fakat bütün bilinmeyen formülasyon hatalarını dışlayamaz. [arxiv](https://arxiv.org/html/2102.09692v1)

## 6. Altı açık sorunun çözüm matrisi

Aşağıdaki seçimler, bağlayıcı kararların uygulanma önerileridir; onaylanmış yeni sözleşme değildir.

| Soru | Alternatif 1 | Alternatif 2 | Öneri ve gerekçe |
|---|---|---|---|
| 1 — Kesin sertifika, eksik heyet | Mevcut `CROSS_VALIDATED` + açıklama | `CERTIFIED` + ayrı heyet durumu | İkincisi: yapılmayan çapraz kontrolü iddia etmez |
| 2 — Heyet bileşimi | İki ücretli aile zorunlu | En az bir uygun ücretli/abonelik hakemi + aile çeşitliliği | İkincisi başlangıç için daha erişilebilir; fiyat değil görev yeterliği ayrıca test edilir |
| 3 — Hiç erişimi olmayan kullanıcı | Kurulumda ücretsiz API hesabı zorunlu | Yerel başlangıç, sonra isteğe bağlı erişim | İkincisi: güvenilir anahtarsız kullanım korunur |
| 4 — Anahtar isteme | İlk kurulumda bütün anahtarları sor | İsteğe bağlı erişim ekranı, ilk kullanımda ayrıntılı izin | İkincisi: daha az sır ve veri riski |
| 5 — Toplayıcı katkısı | Üst heyete hiçbir zaman sayma | Sıkı adaptör yeterlik testiyle say | İkincisi, varsayılan kapalı: esneklik var, sessiz güven yok |
| 6 — Faz | Tam heyeti Faz 1’e al | Faz 1 sözleşme + çekirdek; F1.5/F3 gerçek heyet | İkincisi: güven sözleşmesi erken, entegrasyon yükü kademeli |

### 6.1. Soru 1 — Anahtarsız kesin sertifikalı sonuç

TASARIM TERCİHİ:

- Bağımsız denetlenmiş sertifika varsa `CERTIFIED`.
- Tam heyet yoksa `PROVEN` yok.
- Aynı sonuç ücretsiz heyetle değerlendirilmişse Karar 5 gereği yine `PROVEN` yok.
- Doğrudan formal IR’de doğal dil çevirisi “uygulanamaz” olarak kaydedilir; bu, ücretsiz/ücretli politika kapısını gizlice atlatmaz.
- Faz 1’de yalnızca aynı CAS ile kontrol varsa bağımsız denetim ifadesi kullanılmaz.

Doğrudan IR’nin matematiksel kanıtını LLM’ye bağlamamak bilimsel olarak doğrudur. Üst ürün etiketini yine de tam heyete bağlamak ise sahip politikasıdır. Bu iki karar aynı şey değildir.

### 6.2. Soru 2 — Ücretsiz, ücretli ve karma heyet

#### Fiyat yerine hangi özellikler ölçülmeli?

En az:

- Kaynak metinden bütün zorunlu koşulları çıkarma.
- Birim ve referans çerçevesi doğruluğu.
- Eksik parametreyi uydurmama.
- Yapılandırılmış IR üretme.
- Karşı örnekleri doğru yorumlama.
- Aynı hatayı diğer üyelerle paylaşma oranı.
- İngilizce ve Türkçe görev başarısı.
- Kaynak span eşlemesi.

HELM, model yeteneklerinin görev ve değerlendirme biçimine bağlı olduğunu gösterir; eski model kümelerindeki açık/kapalı farkları güncel ücretsiz/ücretli hizmet ayrımına çevrilemez. Fiyatın kendisinin doğruluk sertifikası olduğuna ilişkin kanıt yoktur. [arxiv](https://arxiv.org/html/2211.09110v1)

#### Önerilen görev paylaşımı

1. Yerel matematik katmanı önce yapıyı, birimleri, alan yükümlülüklerini ve desteklenen motorları analiz eder.
2. Bağımsız formülatörler kaynak problemden aday üretir; ilk adayın formülünü veya cevabını görmez.
3. Ücretli model varsa yalnızca “son söz sahibi” yapılmaz; bağımsız aday üreticisi veya kör kaynak–IR denetçisi olur.
4. Z3/SymPy gibi araçlar adayların belirtilen eşleme altında denkliğini denetler.
5. Ayrışma oylamayla bastırılmaz; soru, karşı örnek veya yeniden inceleme doğurur.
6. Formülasyon değişirse hesap ve sertifika yeniden üretilir.

Bu sıra, “önce matematik analizi, sonra heyet” kararını korurken ilk çözümün bütün heyeti aynı cevaba sabitlemesini önler.

#### Ücretsiz çoğunluk ile tek ücretli model çatışırsa

- Ücretli model otomatik kazanmaz.
- Ücretsiz çoğunluk otomatik kazanmaz.
- Bir somut karşı örnek bütün oy sayılarından daha değerlidir.
- Denklik veya kaynak eşlemesi çözülemiyorsa `NEEDS_INPUT`/ret.
- Ücretli modelin hatalı olduğu belirlenirse ücretli katılımın varlığı üst etiketi kurtarmaz.

#### Üst heyet için önerilen başlangıç koşulları

SAHİP ONAYI GEREKLİ:

- Varsayılan üç bağımsız aday üretimi korunur.
- En az iki farklı model ailesi.
- En az bir, görev testlerini geçmiş ücretli hizmet/abonelik erişimli üye.
- Kör üretim, sabit model kimliği ve kayıtlı adaptör.
- Bütün zorunlu denklik ve kaynak kontrolleri tamam.
- Çözülmemiş tek bir itiraz yok.
- Doğrudan kullanıcı onayı.
- Kabul edilmiş matematiksel sertifika.

Bu sayılar bilimsel optimum olarak sunulmuyor; mevcut tasarıma yakın muhafazakâr başlangıç tercihidir.

“Ücretli”nin ne anlama geldiği hâlâ bağlayıcı biçimde tanımlanmamış durumda. Aynı model ücretsiz krediyle çağrılırsa matematik veya model yeteneği değişmez. Karar 5’in fiyatlandırma modu mu, model yeterliği mi, erişim planı mı istediği sahibin açıklamasını gerektiriyor.

### 6.3. Soru 3 — Hiç anahtarı ve aboneliği olmayan kullanıcı

DOĞRULANDI: Ücretsiz uzaktan API erişimi her zaman mevcut değildir; anahtar, hesap, kota, coğrafya ve hizmet koşulları söz konusu olabilir. Groq belgeleri anahtar oluşturmayı ve organizasyon düzeyinde limitleri açıkça tanımlar. [console.groq](https://console.groq.com/docs/quickstart)

Önerilen ilk kullanım:

1. Yerel ön kontrol çalışır; ağ kullanımı henüz açılmaz.
2. Kullanıcıya “yerel matematik”, “mevcut erişimi bağla”, “ücretsiz erişim kur” seçenekleri gösterilir.
3. Yerel modda yapılandırılmış giriş, doğrudan IR, onaylı dönüşüm işlemleri, birim kontrolü ve desteklenen hesaplar çalışır.
4. Mevcut sertifika bağımsız kontrol edilebiliyorsa LLM olmadan denetlenir.
5. Serbest doğal dil güvenilir biçimde ayrıştırılamıyorsa kullanıcı yapılandırılmış forma yönlendirilir.
6. Uzak heyet erişilemiyorsa yerel sonuç kaybolmaz; heyet durumu “uygulanmadı” olur.
7. Kullanıcı ücretli hizmete zorlanmaz.

Ulaşılabilecek kategoriler:

| Erişim | Ulaşılabilecek durum |
|---|---|
| Tamamen çevrimdışı, bağımsız sertifika denetimi var | `CERTIFIED` |
| Tamamen çevrimdışı, gerçekten ayrı sayısal yollar var | Şartlarıyla `CROSS_VALIDATED` |
| Tek hesap, yeterli kanıt/karşılaştırma yok | Nihai güvenli sonuç yok; tanı çıktısı |
| Ücretsiz heyet + kabul edilmiş sertifika | `CERTIFIED`; üst heyet politikası eksik |
| Uygun karma heyet + bütün kapılar | Onaylanan politika altında `PROVEN` |

Tamamen ücretsiz yerel model çalıştırmak da donanım ve model lisansı açısından koşulludur; “yerel” olması anlamsal doğruluğu kanıtlamaz.

### 6.4. Soru 4 — Ücretli anahtar ne zaman istenmeli?

Önerilen politika:

- Kurulumda bir kez isteğe bağlı erişim sorusu.
- Anahtarın kendisi sohbet veya rapor içine istenmez.
- Anahtarı kullanmadan önce sağlayıcı, veri kapsamı, amaç, bütçe ve yeniden deneme sayısı gösterilir.
- Var olan anahtarın bulunması otomatik kullanım izni sayılmaz.
- Yeni sağlayıcıya geçiş veya ek maliyet önceden onaylanır.
- Varsayılan uzak kullanım bütçesi sıfırdır; kullanıcı artırır.
- Ücretli çağrı reddedilirse yerel çalışma devam eder.

Güvenlik sözleşmesi:

- İşletim sistemi kimlik kasası veya uygun sır deposu.
- En az yetki.
- Log ve raporlarda maskeleme.
- Ajan alt süreçlerine bütün ortam değişkenlerini aktarmama.
- Anahtarı model istemine koymama.
- Döndürme/iptal desteği.
- Sağlayıcı ve model başına bütçe.
- Kota hatasında sessiz ücretli fallback yasağı.

Bunların genel güvenlik dayanağı OWASP’ın en az yetki, yaşam döngüsü, denetim, güvenli taşıma ve sır ifşasını azaltma önerileridir. Yerel Rigor için tam kurumsal Vault altyapısı zorunlu değildir. [cheatsheetseries.owasp](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

Maliyet tavanı da mutlak garanti gibi sunulmamalı: sağlayıcı fiyatı ve token muhasebesi değişebilir. Rigor ön tahmin, üst çıktı sınırı, yerel bütçe rezervasyonu ve mümkünse sağlayıcı tarafı harcama limiti kullanmalıdır.

### 6.5. Soru 5 — Toplayıcılar ve bağımsızlık

Yeni ve önemli bulgu: Önceki belgelerdeki “önbellek yok” kuralı fazla geniştir.

- Prompt/KV önbelleği, aynı giriş önekinin hesaplamasını yeniden kullanır.
- Yanıt önbelleği, yeni üretim yapmadan eski cevabı döndürür.

Groq belgeleri prompt caching’in giriş işlemesini hızlandırdığını, cevap üretiminin normal devam ettiğini belirtir. OpenRouter belgeleri yanıt önbelleğinin sağlayıcıya hiç gitmeden cevabı geri döndürebildiğini açıkça ayırır. [console.groq](https://console.groq.com/docs/prompt-caching)

Sonuç:

- Prompt caching tek başına bağımsız hakemliği bozmuş sayılmamalı.
- Semantik veya tam yanıt cache’i yeni hakem üretimi sayılmamalı.
- Gizlilik politikası prompt cache için ayrıca değerlendirilmelidir.

#### Bir diğer kritik bulgu: Benzersiz generation ID yeterli değil

OpenRouter her cache hit için yeni generation ID verebiliyor. Dolayısıyla farklı iki ID, iki bağımsız model üretiminin kanıtı değildir. [openrouter](https://openrouter.ai/docs/guides/features/response-caching)

#### Üst etikete katkı için gerekli adaptör sözleşmesi

| Alan | Gerekli kontrol |
|---|---|
| Model | Açık model kimliği; `auto` veya rastgele ücretsiz router yok |
| Aile | Kuratörlü model–aile eşlemesi; sağlayıcı sayısı aile sayısı değildir |
| Sağlayıcı | Açık izinli endpoint; gereken sürüm/quantization kaydı |
| Fallback | Model ve sağlayıcı fallback’i kapalı veya aynı politika altında yeniden değerlendirilmiş |
| Parametreler | Gerekli parametre desteği zorunlu |
| İstem | Sıkıştırma, içerik çıkarma ve otomatik semantik onarım kapalı |
| Yanıt cache | Açıkça kapalı; cache hit tespit edilirse yeni aday sayılmaz |
| Kayıt | İstek özeti, istenen/dönen model, provider, upstream ID, cache durumu |
| Gizlilik | İzinli veri politikası ve kullanıcı onayı |
| Yeterlik | Adaptörün negatif ve entegrasyon testleri geçmiş |

OpenRouter `allow_fallbacks` için varsayılan `true`, `require_parameters` için varsayılan `false` bildiriyor. Sıkı Rigor kullanımı bunları varsayılan bırakamaz. [openrouter](https://openrouter.ai/docs/guides/routing/provider-selection)

Bağlam sıkıştırma bazı endpointlerde varsayılan olabildiğinden yalnızca “plugin eklemedim” demek yeterli değildir; açık kapatma gerekir. [openrouter](https://openrouter.ai/docs/guides/features/message-transforms)

Yanıt cache’i de preset üzerinden açılabilir; resmî belgede istek düzeyindeki `X-OpenRouter-Cache: false` kapatması tanımlıdır. [openrouter](https://openrouter.ai/docs/guides/features/response-caching)

#### Model kimliğini gerçekten kanıtlayabilir miyiz?

Generation metadatası model, provider ve upstream ID gibi bilgiler sağlar. Bunlar yararlı denetim kayıtlarıdır; model ağırlıklarının kriptografik uzaktan doğrulaması değildir. [openrouter](https://openrouter.ai/docs/api/api-reference/generations/get-request-&-usage-metadata-for-a-generation)

Bu nedenle üst heyete katkı, “güvenilen hizmetin kaydı” düzeyindedir. Rigor, toplayıcıya hiç güvenmeden gerçek model kimliğini kanıtladığını söylememelidir.

#### Mevcut aynı-yanıt reddi düzeltilmeli

§8.2’deki “iki ham yanıt bayt bayt aynıysa ikisini reddet” kuralı güvenli ama aşırı kısıtlayıcıdır. Basit bir dönüşüm için iki bağımsız model aynı kısa JSON’u üretebilir.

Öneri:

- Aynı içerik bir denetim sinyali olsun.
- Tek başına cache veya bağımlılık kanıtı sayılmasın.
- Yeni üretim kayıtları, cache metadatası ve model kimlikleri esas alınsın.
- Belirsiz adaptör üst heyete katkı vermesin.

### 6.6. Soru 6 — Heyetin fazı

Önerim aşamalı mimaridir:

| Aşama | Yapılacaklar | En yüksek sonuç |
|---|---|---|
| F1 | Mevcut IR, kapılar, deterministik rapor; sertifika durumu ayrımı; sahte heyet testleri | `CERTIFIED` yalnızca gerçek denetleyiciyle; aksi hâlde şartlı `CROSS_VALIDATED` |
| F1.5 | Dar rasyonel sertifika denetleyicisi; erişim/izin sözleşmesi; bir doğrudan API adaptörü | Üst etiket hâlâ kapalı olabilir |
| F2 | Roket veri/model katmanı ve bileşim kuralları | Kanıt türüne göre |
| F3 | Bağımsız formülasyon, hizalama, denklik, onay ve yeterliği geçmiş karma heyet | `PROVEN` açılabilir |
| Sonraki | Ek sağlayıcılar, toplayıcılar, CLI yeterliği, şablonlar, Lean | Kapsama göre |

F1.5 yeni bir teslimat bölümü önerisidir; bağlayıcı takvim değişikliği değildir.

Bu yaklaşım çekirdeğe LLM bağımlılığı sokmaz. Aynı zamanda erişim ve kayıt şemasını F3’e kadar tamamen erteleyip mimari borç oluşturmaz.

## 7. Sertifika ve bileşim güvenliğinin nihai sözleşmesi

### 7.1. `unsat_core` ne değildir?

Z3 rehberi çekirdeği, birlikte sağlanamayan adlandırılmış iddiaların alt kümesi olarak tanımlar. Bu, denetlenebilir türetim adımlarından oluşan ispatla aynı nesne değildir. [microsoft.github](https://microsoft.github.io/z3guide/docs/logic/propositional-logic/)

Önerilen ayrım:

- `diagnostic_core`: Açıklama ve hata yerelleştirme.
- `solver_unsat_claim`: Çözücünün sonucu.
- `checked_unsat_proof`: Onaylı denetleyicinin kabul ettiği kanıt.

Yalnızca sonuncusu bağımsız denetlenmiş ispat ifadesine dayanak olabilir. CakeML’nin SAT/PB denetleyicileri bu ayrı kontrol mimarisinin somut örnekleridir. [cakeml](https://cakeml.org/checkers.html)

### 7.2. Üretim ve kontrol ayrı durumlar olmalı

Asgari kayıt:

| Alan | İçerik |
|---|---|
| `claim_kind` | Tam değer / aralık / özellik / teklik / optimum |
| `certificate_kind` | Kullanılan sertifika biçimi |
| `check_status` | Yok / üretildi / kabul / ret / tamamlanamadı |
| `checker_profile` | Denetleyici kimliği, sürümü, güven varsayımları |
| `claim_id` | Kontrol edilen formal iddia |
| `dependencies` | Matematiksel alt iddialar ve semantik manifest |

Sadece üç alan, `formal/none` ikilisinden daha iyidir; fakat yanlış iddiaya ait sertifikayı engellemek için kimlik ve denetleyici bağlantısı da gerekir.

### 7.3. Tam değer, aralık ve özellik aynı ailede olabilir mi?

Evet, aynı “kabul edilmiş matematiksel kanıt” ailesinde olabilirler; aynı iddia gibi sunulamazlar.

- Tam değer: “Bu değer tamdır.”
- Aralık: “Matematiksel değer bu aralıkta bulunur.”
- Özellik: “Belirtilen eşitsizlik/koşul sağlanır.”
- Optimum: “Uygulanabilirlik ve global sınır koşulları doğrulandı.”

Aralık orta noktası tam değer değildir. FloVer gibi hata sınırı sertifikaları da tam reel sonuçla aynı şeyi kanıtlamaz. [rmonat](https://rmonat.fr/data/pubs/2018/fmcad18.pdf)

### 7.4. Aynı araçla çözüm ve kontrol

Aynı SymPy kurulumuyla çözüm üretip geri ikame yapmak yararlı hata yakalama sağlayabilir. Fakat ortak uygulama hatası ve ortak yanlış derleme riski kalır.

Bu nedenle:

- “Geri ikame kontrolü geçti” denebilir.
- Gerçekten ayrı değilse “çözücüden bağımsız denetleyici kabul etti” denemez.
- `CERTIFIED` için kabul edilen denetleyici profili tanımlanmalıdır.
- Küçük bağımsız denetleyici her matematik sınıfında evrensel zorunluluk değildir; bağımsız denetlenebilir sertifika vaadi verildiğinde zorunludur.
- Güvenilir formal çekirdek de uygun profilde kanıt kontrolü sağlayabilir; her teorem için ikinci farklı uygulama şart koşmak bilimsel zorunluluk değildir. [cakeml](https://cakeml.org/checkers.html)

### 7.5. Yaklaşık ve kesin adımların birleşimi

Bir ODE tahmini \(\hat h=8000\ \mathrm{ft}\) ise:

\[
0{,}3048\hat h=2438{,}4\ \mathrm{m}
\]

hesabı tam yapılabilir. Ancak bu yalnızca tahminin birim dönüşümünü doğrular; gerçek çözümün veya gerçek uçuşun 2438,4 m olduğunu kanıtlamaz.

“En zayıf halka” sözü tek başına yeterli değildir:

- Yaklaşık değer kanıtlı bir aralıkla taşınırsa sonraki aralık da kanıtlanabilir.
- Sertifikasız tahmin tam sayıya dönüştürülerek kanıtlı girdiye çevrilemez.
- Çıktı iddiası, hangi bağımlılıkları kullandığına göre değerlendirilir.
- Bağımsız olarak kanıtlanmış bir özellik, kullanılmayan zayıf bir alt hesabın durumundan etkilenmeyebilir.

NASA standardının girdi kökeni, model belirsizliği ve türetilmiş sonuçların güvenilirliğini ayrı ele alması bu ayrımı destekler. [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)

### 7.6. IR kimliği ve rapor bütünlüğü

Tek bir büyük hash yerine üç bağlantılı kimlik öneriyorum:

1. Matematiksel iddia: normalize IR, varsayımlar, sayı/birim semantiği, model tanımları.
2. Kanıt çalıştırması: iddia kimliği, sertifika, denetleyici ve ortam sürümleri.
3. Rapor: kanıt kaydı, gösterilen sonuçlar, kaynak ve onay kayıtları.

Dosya hash’i bütünlüğü destekler; doğru hücreyi seçmeyi veya verinin gerçekliğini ispatlamaz. Aynı şekilde bu kimlikler imza veya kimlik doğrulama değildir.

## 8. Önerilen nihai güven modeli

### 8.1. Etiketler

| Etiket | Kesin anlam | Zorunlu kanıt |
|---|---|---|
| `PROVEN / KANITLANDI` | Onaylı formal tanıma göre matematiksel kanıt ve tam Rigor güvence politikası tamam | Kabul edilmiş sertifika + bütün süreç kapıları + Karar 5 koşulu |
| `CERTIFIED / SERTİFİKA DOĞRULANDI` | Gösterilen formal matematiksel iddiaya ait sertifika kabul edildi; tam süreç koşulları eksik olabilir | Onaylı denetleyici, doğru iddia ve kapsam bağlantısı |
| `CROSS_VALIDATED / ÇAPRAZ DOĞRULANDI` | Kayıtlı ayrı yöntemler belirlenmiş tolerans/testlerde uyuştu | Gerçek yöntem karşılaştırması; formal kanıt iddiası yok |
| `REFUSED / REDDEDİLDİ` | İstenen cevap verilmedi | Neden ve gerekli düzeltme |

`NEEDS_INPUT` ve `NEEDS_CONFIRMATION` mevcut oturum durumları olarak kalır. v1’e ikinci tam durum makinesi veya genel SACM altyapısı eklemeyi önermiyorum.

Tek hesap yapılıp ne sertifika ne gerçek çapraz kontrol varsa güvenli nihai sayı yayımlanmaz; tanı çıktısı ve eksik kontrol açıklaması verilir. `RECOMPUTED` ayrı kullanıcı etiketi bu sürüm için gerekli değildir.

### 8.2. Deterministik karar sırası

1. Bilinen kaynak/yorum çatışması, rapor uyuşmazlığı veya başarısız zorunlu kontrol varsa dur.
2. Eksik bilgi veya zorunlu onay varsa mevcut oturum durumuna dön.
3. Tam kapsamlı kabul edilmiş matematiksel kanıt ve tam heyet politikası varsa `PROVEN`.
4. Kanıt kabul edilmiş ama tam heyet politikası eksikse `CERTIFIED`.
5. Kanıt yok; gerçek çapraz hesap ve sınır testleri tamam ise `CROSS_VALIDATED`.
6. Aksi hâlde `REFUSED`.

Bir sertifika reddi, önermenin yanlış olduğunu otomatik göstermez. Başka geçerli kanıt yolu yeniden denenebilir; fakat çatışan kanıt ve karşı örnek varsa yayın engellenir. FloVer de aşırı yaklaşım nedeniyle bazı doğru sınırların kendi yöntemiyle doğrulanamayabileceğini açıklar. [rmonat](https://rmonat.fr/data/pubs/2018/fmcad18.pdf)

### 8.3. Zorunlu özet alanları

Her nihai kutu:

- Sonuç ve etiket.
- Matematiksel olarak ne kontrol edildi?
- Problem yorumu hangi yöntemle incelendi?
- En önemli kapsam sınırı.

“Üç model gördü”, “ücretli model kullandı” gibi tek başına bilgi taşımayan rozetler kullanılmaz. “Kullanıcı onayladı” ifadesi yalnızca doğrudan olay kaydı varsa üretilir.

## 9. Adversarial değerlendirme

| Senaryo | Etiket/davranış | Kullanıcı açıklaması ve gerekli kanıt |
|---|---|---|
| Yanlış “en az/en fazla”, doğru dönüşüm | Biliniyorsa ret | “Hesap geçerli, kaynak koşulunu temsil etmiyor.” Kaynak–IR eşlemesi gerekir |
| Yanlış kütle girdisi, doğru toplam | Koşullu `CERTIFIED`; yanlışlık biliniyorsa ret | “Verilen kütlelere göre toplam doğrulandı; tartım doğruluğu doğrulanmadı.” |
| Bağımlı modeller aynı formülü üretir | Üst heyet kapısı geçmez | Ayrı oturum/model kayıtları; aile sayısı beyana dayanamaz |
| Ücretli üyeler aynı hatayı yapar | Otomatik koruma yok | `PROVEN` da niyet garantisi değildir; kapsam ve aktif onay korunur |
| Ücretsiz doğru, ücretli yanlış | Ayrışma → soru/ret | Ücretli üye veto otoritesi değil; somut kanıt esas |
| Statik marjinde yanlış eksen veya CP/CG karışması | Kaynak/model çatışması → ret | Doğru bölme işlemi hatalı fiziksel bağlamı kurtarmaz |
| Geçersiz Barrowman kullanım alanı | Mühendislik cevabı engellenir | “Model bu koşullarda doğrulanmış değil.” Genel feragat yeterli değil |
| Sertifika üretildi, kontrol yok | `CERTIFIED`/`PROVEN` yasak | “Sertifika henüz denetlenmedi.” |
| İki ODE yöntemi yakınsar, formal sınır yok | `CROSS_VALIDATED` | “Yöntemler uyuştu; kesin hata sınırı yok.” |
| Yaklaşık ODE + kesin dönüşüm | Üst sonuç en fazla mevcut sayısal destek | Kesinlik yalnızca dönüşüm alt adımına ait |
| LP uygun çözüm, optimum kanıtı yok | Optimum için `CERTIFIED` yok | Primal/dual sınır ve amaç eşitliği gerekir |
| MILP’de yalnızca LP dual sınırı | Optimum iddiası reddedilir | Tamsayılı uygulanabilirlik ve global bound ilişkisi gerekir |
| Finansal ücret hesabı | Kanıt kapsamına göre `CERTIFIED`/`PROVEN` | Oran, nominal, varlık birimi, yuvarlama modu açık; borsa kaynağı ayrı |
| Ajan sahte onay iletir | Onay bekle/ret | Yerel güvenilen onay kanalı gerekir |
| Toplayıcı model değiştirir | Yanıt heyetten çıkarılır | Kalan üyelerle eşik yeniden değerlendirilir; sessiz devam yok |
| Sertifika sonrası sonuç değiştirilir | Rapor engellenir | Görünür sayı–iddia–sertifika bağlantısı kontrol edilir |
| Doğrudan IR, doğal dil yok | Kanıt varsa `CERTIFIED` | “Verilen formal ifade kontrol edildi”; kaynak niyeti varsayılmaz |
| Şablon yeni aralık/modelde kullanılır | Yeniden kontrol veya soru | Eski onay yeni geçerlilik alanına taşınmaz |

Bu tablo çalıştırılmış test sonucu değil, uygulanacak negatif test sözleşmesidir.

Fark edilmemiş formülasyon hatasını hiçbir etiket sistemi tek başına ortadan kaldırmaz. Red Team’in bu riski öne çıkarması haklıdır; fakat ücretli heyet eklenince riskin sıfırlandığı sonucu da desteklenmez. [arxiv](https://arxiv.org/html/2506.07962v1)

## 10. Doğrudan kullanılabilir rapor özetleri

Aşağıdaki metinler rapor şablonlarıdır. Gerçek Rigor çalıştırması yapılmadı. İkinci örnekteki sayılar yalnızca açıklayıcı test girdileridir.

### 10.1. Kesin birim dönüşümü — heyet yok, bağımsız sertifika kabul edilmiş

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Etiket: SERTİFİKA DOĞRULANDI  
> Hesap: Uluslararası foot tanımıyla (1 ft = tam 0,3048 m) bu eşitlik çözücüden bağımsız denetleyicide doğrulandı. 2438,4 m yuvarlanmış bir sonuç değildir.  
> Problem yorumu: Bağımsız hakem incelemesi yapılmadı; Rigor’un KANITLANDI koşulları tamamlanmadı.  
> Sınır: Bu kontrol, verilen 8000 ft değerinin dönüşümünü kapsar; değerin kaynaktan doğru alındığını veya gerçek bir yüksekliği doğru ölçtüğünü göstermez.

Foot tanımı NIST’e dayanır; tam ondalık gösterim rasyonel eşitlikle doğrulanabilir. [nist](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors)

Ücretsiz heyet gerçekten çalıştıysa yalnızca yorum satırı değişir:

> Problem yorumu: Üç ücretsiz modelin birbirini görmeden ürettiği ifadelerin denkliği kontrol edildi ve tanım doğrudan kullanıcı tarafından onaylandı. Yalnızca ücretsiz heyet kullanıldığı için KANITLANDI koşulu sağlanmadı.

Bu satırdaki her olayın kaydı yoksa metin üretilemez.

### 10.2. Karmaşık mühendislik — statik marjin

Açıklayıcı girdiler: \(X_{CP}=1{,}8\ \mathrm m\), \(X_{CG}=1{,}6\ \mathrm m\), \(D=0{,}1\ \mathrm m\). Eksen ve referans yönü onaylıdır. Tam heyet ve hesap kanıtı gerçekten tamamlanmış kabul edilirse:

> Sonuç: Statik marjin = 2 kalibre  
> Etiket: KANITLANDI — onaylı modele ve girdilere göre  
> Hesap: \((X_{CP}-X_{CG})/D\) işlemi, verilen değerlerle tam olarak 2 verir. Bu hesap ve seçilen aralık koşulu için kanıt kontrolü tamamlandı.  
> Problem yorumu: Koordinat yönü, CP/CG eşlemesi ve model kullanımı bağımsız formülasyon denetiminden geçti; tanım doğrudan onaylandı ve tam heyet koşulları sağlandı.  
> Sınır: CP değerinin aerodinamik doğruluğu, ölçüm belirsizlikleri ve gerçek uçuş kararlılığı bu aritmetik kanıtla doğrulanmış olmaz.

CP değeri yaklaşık model çıktısıysa, “statik marjin tam 2” yalnızca o sayısal girdiye koşullu bir hesap iddiasıdır; fiziksel marjin için belirsizlik veya aralık ayrıca taşınır. Model ve gerçek sistem ayrımı NASA yaklaşımıyla uyumludur. [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)

### 10.3. Formal sertifikasız rampa çıkış simülasyonu

> Sonuç: Rampa çıkış hızı — aşağıdaki sayısal aralıkta  
> Etiket: ÇAPRAZ DOĞRULANDI  
> Hesap: Raporlanan iki sayısal yöntem, kayıtlı tolerans içinde uyuştu ve adım küçültme testlerini geçti. Kesin hata sınırı sağlayan formal sertifika bulunmuyor.  
> Problem yorumu: İtki tablosu, değişken kütle, sürükleme, ray sürtünmesi ve başlangıç koşulları onaylanan modelden alındı.  
> Sınır: Bu uyuşma gerçek rampadan çıkış hızını veya yarışma eşiğinin kesin sağlandığını kanıtlamaz.

Gerçek bir çalıştırma olmadan sayısal hız veya aralık uydurmadığım için kutuda örnek sonuç değeri vermiyorum. Ürün, bu alanı doğrulama kaydından doldurmalıdır.

## 11. DeepSeek Harness değerlendirmesi

### 11.1. Kimlik artık belirsiz değil

DOĞRULANDI: İncelenen ürün DeepSeek’in resmî `deepseek-ai/deepseek-harness` deposundaki `dsh` aracıdır. Resmî site ve depo README’si bunu Cordis tabanlı, “everything is a plugin” mimarisine sahip açık kaynak agent harness olarak tanımlar. Bu, DeepSeek-Prover veya yalnızca genel “evaluation harness” kavramı değildir. [deepseek](https://www.deepseek.com/en/harness/)

Depodan okunan README blob’u: `7941e30f7bdca9391befe39b9115d211157fa42d`. README hızlı değişen developer preview ve kırıcı değişiklik uyarısı içeriyor. Ayrıntılı kaynak kod güvenlik denetimi yapılmadı.

### 11.2. Rigor’a olası katkı

| Ölçüt | Değerlendirme |
|---|---|
| Çoklu ajan koordinasyonu | Resmî sitede ekip/alt ajan yetenekleri var; Rigor bağımsızlığı ayrıca sınanmalı |
| Model izolasyonu | Oturum/eklenti ayrımı, güvenlik izolasyonu kanıtı değildir |
| Yapılandırılmış IR | Bir adaptörle mümkün olabilir; Rigor şemasına uygunluğu gösterilmedi |
| Karşı örnek üretimi | Araç çağırma yararlı olabilir; matematiksel denetleyicinin yerine geçmez |
| Denetlenebilirlik | İz ve araç çağrısı görünürlüğü olumlu |
| Yerel çalışma | Arayüz yerel çalışabilir; model çıkarımı zorunlu olarak yerel değildir |
| Anahtarsızlık | Resmî model yolu hesap gerektirir; özel model yolu kullanıcının erişimini gerektirir |
| Maliyet | Açık kaynak yazılım ücretsiz olabilir; model çağrıları ücretsiz sayılmaz |
| Güvenlik/bakım | Yeni Node/eklenti çalışma zamanı, araç yetkileri ve hızlı değişim yükü |
| v1 değeri | Çekirdeğe alınmasını haklı çıkaracak ölçülmüş fayda yok |

Resmî Harness şartları, varsayılan model hizmetleri için hesap ve ön ödeme gereksinimini belirtiyor. Özel model modunda API’yi kullanıcı sağlar. Dolayısıyla Harness, hiçbir erişimi olmayan kullanıcıya otomatik ücretsiz hakem heyeti çözümü değildir. [deepseek](https://www.deepseek.com/en/harness/terms-of-use/)

Resmî şartlar ayrıca sandbox ve izin kontrollerinin tam izolasyon garantisi vermediğini, hizmetin üretim için tamamen güvenli kabul edilmemesi gerektiğini açıklıyor. [deepseek](https://www.deepseek.com/en/harness/terms-of-use/)

### 11.3. Karar

TASARIM TERCİHİ: Faz 1 çekirdeğine entegrasyon önermiyorum.

Daha sonra:

- Rigor’u MCP üzerinden çağıran opsiyonel istemci,
- ya da yeterliği sınanmış bir formülatör adaptörü

olarak değerlendirilebilir.

Rigor’un anahtarlarını, kullanıcı onay yetkisini veya etiket kararını Harness’e devretmek önerilmez. Eklenti sayısı veya ajan koordinasyonu, matematiksel bağımsızlık kanıtı değildir.

## 12. Tasarım belgelerine aktarılabilecek karar metinleri

Aşağıdaki metinler öneridir; henüz sahip onayı alınmış değişiklik değildir.

### K14 — Yeni metin önerisi

> Rigor’un hedef kullanıcısının ücretli veya ücretsiz API anahtarı ya da AI aboneliği olmayabilir. Yerel matematik ve desteklenen kanıt kontrolleri uzak LLM erişimine bağımlı değildir. Ücretsiz API’ler erişim ve kullanıcı izni varsa kullanılabilir; kullanıcıda mevcut ücretli API veya resmî abonelik erişimi isteğe bağlı olarak bağlanır. Ücretli erişim satın almak zorunlu değildir.

Bu değişiklik yeni Karar 1–3’ü depoya aktarır. [concepts_brief.md]

### K15 — Yeni metin önerisi

> Abonelik erişimleri yalnızca sağlayıcının izin verdiği resmî istemcilerle kullanılır. Doğrudan API’ler ve API toplayıcıları opsiyonel adaptörlerdir. Her adaptör model kimliği, aile, fallback, içerik dönüşümü, yanıt önbelleği ve gizlilik koşulları için sürümlü yeterlik sözleşmesini sağlamalıdır. Başarısız veya belirsiz adaptör üst heyet koşuluna katkı veremez.

Toplayıcının listeye alınması, otomatik üst güven yeterliği değildir.

### §4.1 — Etiket sözleşmesi

> PROVEN, kabul edilmiş matematiksel kanıtın yanında tam Rigor güvence politikasının sağlandığını gösterir. Yalnızca ücretsiz heyetle PROVEN verilemez.  
> CERTIFIED, tam kimliği belirli matematiksel iddiaya ait sertifikanın onaylı denetleyicide kabul edildiğini, tam heyet koşullarının ise sağlanmamış olabileceğini gösterir.  
> CROSS_VALIDATED, gerçek ayrı yöntem karşılaştırmasının başarıyla tamamlandığını gösterir.  
> Etiketler genel doğruluk yüzdesi veya tek boyutlu kalite sırası değildir.

### §4.3 — Köken ve onay

> `model_families`, onay kaynağı ve girdi kökeni çağıran ajanın beyanıyla yükseltilemez. Güvenilen adaptör ve onay kanalı olaylarından türetilir. Dosya bütünlüğü, çıkarım sadakati ve fiziksel veri doğruluğu ayrı kavramlardır.

### §4.4–§4.5 — Doğrudan IR ve model kütüphanesi

> Doğrudan IR’de doğal dil çevirisi uygulanmaz. Matematiksel sertifika durumu LLM sayısından bağımsızdır; üst sonuç etiketi ise tam politika koşullarına tabidir. Kütüphane modelinin önceki doğrulaması yeni girdilerin, bağlamanın ve geçerlilik alanının kontrolünü kaldırmaz.

### §6.4 — Heyet

> Matematiksel ön analizden sonra formülatörler kaynak problemden birbirlerinin adaylarını görmeden IR üretir. Ön çözüm ve aday formüller bağımsız üretimi etkileyecek biçimde paylaşılmaz. Denklik ve değişken eşleme kontrolleri tamamlanır; ayrışma oy çokluğuyla bastırılamaz. Formülasyon değişirse çözüm ve sertifika yeniden çalıştırılır.

### §6.5–§6.6 — Motor ve sertifika

> Çözücü iddiası, geri ikame kontrolü, bağımsız sertifika kabulü ve sayısal uyuşma ayrı kaydedilir. `unsat_core` tanısal varlıktır; tek başına bağımsız ispat sertifikası sayılmaz. Her kabul kaydı iddia türü, iddia kimliği, denetleyici profili ve bağımlılıkları içerir.

### §6.7–§6.8 — Anlatım ve rapor

> Kritik etiket, sayı, birim, kanıt kapsamı ve heyet durumu doğrulama kayıtlarından deterministik üretilir. İsteğe bağlı LLM sadeleştirmesi bunları değiştiremez. Özet kutusu genel bir feragat yerine somut olarak neyin kontrol edildiğini ve neyin kontrol edilmediğini açıklar. Gerçekleşmemiş heyet veya kullanıcı onayı metne eklenemez.

### §8.2 — Erişim sözleşmesi

> Yanıt cache’i, semantik cache ve prompt/KV cache ayrı değerlendirilir. Yeni hakem üretimi sayılan yanıtlarda yanıt cache’i kullanılamaz. Prompt cache tek başına bağımsızlık ihlali sayılmaz. Benzersiz istek/generation ID tek başına yeni üretim kanıtı değildir. Aynı metin tek başına bağımlılık kanıtı değildir. Model/provider fallback’i, sıkıştırma ve parametre yok sayma davranışı açıkça denetlenir.

Bu düzeltme OpenRouter ve Groq’un resmî cache ayrımlarıyla destekleniyor. [console.groq](https://console.groq.com/docs/prompt-caching)

## 13. Uygulama ve test stratejisi

### 13.1. Faz 1’e alınması gereken asgari değişiklikler

1. `certificate="formal"|"none"` yerine açık kontrol kaydı.
2. `CERTIFIED` etiketi ve ayrı matematiksel kapsam.
3. `PROVEN`ın F1’de kapalı kalması.
4. İstemcinin onay/heyet durumunu doğrudan belirleyememesi.
5. İddia–sertifika–rapor bağlantısı.
6. Semantik manifest.
7. Basit bağımlılık kimlikleri; tam grafik altyapısı değil.
8. Mevcut deterministik anlatımın korunması.

Dar bir rasyonel denetleyici eklenirse yalnızca desteklediği işlemler için bağımsız kontrol söylenmeli. SymPy, SMT, Arb, ODE ve optimizasyonun tamamına tek seferde bağımsız denetleyici yazmak F1 hedefi yapılmamalıdır.

### 13.2. Kabul ve negatif testler

| Test | Zorunlu sonuç |
|---|---|
| Ücretsiz heyet + geçerli sertifika | `CERTIFIED`, hiçbir yolda `PROVEN` değil |
| Ücretli anahtar mevcut ama kullanım izni yok | Uzak çağrı yok |
| Ücretli üye var, aile çeşitliliği yok | Tam heyet kapısı geçmez |
| API anahtarı yok, resmî CLI yetkisi var | “LLM yok” diye yanlış sınıflanmaz |
| Bütün uzak erişim yok | Yerel desteklenen görevler çalışır |
| Ücretsiz API 429 döner | Kontrollü bekleme/erişim eksikliği; sessiz ücretli geçiş yok |
| Aynı model iki sağlayıcıda | İki aile sayılmaz |
| Yanıt cache HIT, yeni generation ID | Yeni hakem üretimi sayılmaz |
| Prompt cache var, yeni model üretimi var | Otomatik bağımsızlık reddi yok |
| İki bağımsız kısa JSON aynı | Tek başına sahtecilik kararı yok |
| Toplayıcı model değiştirir | Yanıt üst heyetten çıkarılır |
| Sıkıştırma bir koşulu siler | Yanıt reddedilir |
| Ajan `USER_DIRECT` gönderir | Güvenilen onay olayı oluşmaz |
| Sertifika yalnızca üretildi | `CERTIFIED` verilmez |
| `unsat_core` tek kanıt | Bağımsız ispat ifadesi verilmez |
| Aralık sertifikası, orta nokta sonuç | “Tam değer” metni üretilemez |
| Yaklaşık CP veya ODE girdisi | Üst fiziksel sonuç tam değer gibi sunulmaz |
| Birim/model sürümü değişir | Eski kabul otomatik taşınmaz |
| Rapor sayısı değiştirilir | Bağlantı kontrolü başarısız |
| Teklik kontrolü yokken bütün çözüm iddiası | İddia reddedilir |
| Heyet bir koşulu ortak atlar | Altın test kaynak–IR eşleme hatasını yakalamalı |

Altın testlerde sıfır yanlış `PROVEN` zorunlu çıkış ölçütüdür. Fakat sonlu testte sıfır hata, bütün olası girdiler için sıfır hata ispatı değildir.

## 14. Sahip onayı gereken kararlar ve kalan sorular

### Bilimsel/teknik olarak kapanabilen noktalar

- Matematiksel sertifika, model fiyatından bağımsız güven sağlayabilir.
- Denetlenmiş ispat ile `unsat_core` aynı şey değildir.
- Sertifika üretimi ile kabulü ayrı olaydır.
- Prompt cache ile yanıt cache aynı değildir.
- Generation ID bağımsız üretim kanıtı değildir.
- Formalizasyonlar arası denklik, kaynak niyetine uygunluk garantisi değildir.
- Kesin alt işlem yaklaşık üst sonucu kesinleştirmez. [cakeml](https://cakeml.org/checkers.html)

### Sahip onayı gerektiren tercihler

- `CERTIFIED / SERTİFİKA DOĞRULANDI` adının eklenmesi.
- `PROVEN`ın tam süreç etiketi olarak korunmasının açık metni.
- Üst heyette bir mi, iki mi ücretli/abonelik erişimli ailenin gerekeceği.
- Ücretsiz kredi ve promosyon erişiminin Karar 5 bakımından durumu.
- Toplayıcıların yeterlik testinden sonra üst heyete katkı verebilmesi.
- F1.5 biçimindeki dar denetleyici ve erişim dilimi.
- Tam grafik, `RECOMPUTED` ve ikinci durum makinesinin v1’den çıkarılması.

### Bu araştırmada kapanmayanlar

- Türkçe etiketlerin kullanıcılar üzerindeki etkisi.
- Rigor görevlerinde hangi somut model heyetinin en iyi olduğu.
- CLI ve Harness izolasyonunun fiilî testi.
- Tasarım ve Faz 1 dosyalarının kesilen kısımlarının eksiksiz satır denetimi.
- Uzak hizmetin gerçek model yürütmesini sunucu beyanından bağımsız doğrulama.

Bunlar varsayımla doldurulmamalıdır.

## 15. Önceki iki araştırmaya göre net ilerleme ve nihai karar

Bu aşamada:

1. Önceki raporun `KANITLANDI`ı tek başına matematik etiketine dönüştürme önerisi, yeni bağlayıcı kararlar altında geri çekildi.
2. Red Team’in “anahtarsız kullanıcıda ücretsiz heyet vardır” varsayımı reddedildi.
3. `2509.14034` kaynağına yüklenen iddia düzeltildi.
4. `2506.07962` içindeki %60’ın kapsamı kesinleştirildi.
5. Rigor heyetinin çıplak cevap oylaması olmadığı doğrudan doğrulandı.
6. Aynı araçla geri ikame ile bağımsız denetleyici ayrımı korundu.
7. Cache türleri, yeni generation ID ve aynı JSON’a ilişkin üç yeni somut tasarım hatası ortaya çıkarıldı.
8. DeepSeek Harness’in resmî kimliği doğrulandı; ücretsiz erişim çözümü veya F1 çekirdek bağımlılığı olarak önerilmedi.
9. Önceki ağır güven grafiği önerisi, v1 için daha küçük kayıt sözleşmesine indirildi.
10. Karar 5’i koruyup matematiksel kanıtı küçümsemeyen dört kategorili hibrit öneri hazırlandı.

Nihai öneri: `PROVEN` korunmalı; fakat açıkça sürümlü tam Rigor güvence politikasının etiketi olarak tanımlanmalıdır. Tam hakemlikten geçmemiş ama sertifikası gerçekten kabul edilmiş sonuç `CERTIFIED / SERTİFİKA DOĞRULANDI` almalıdır. Özet kutusunda matematiksel kesinlik ve problem yorumunun durumu ayrı yazılmalıdır. `CERTIFIED` ile `CROSS_VALIDATED` arasında genel doğruluk sıralaması kurulmalıdır diye bir bilimsel zorunluluk yoktur.

### Kararı kilitlemek için sizden gereken yanıt

1. Karar 5’teki “ücretli model” koşulunu nasıl uygulayalım:  
   **A)** Görev yeterliği test edilmiş, normalde ücretli/abonelikle erişilen modelin heyete katılması; ücretsiz krediyle çağrı da sayılır.  
   **B)** İlgili hakem çağrısının gerçekten ücretli bir erişim planından yapılması gerekir.

2. `PROVEN`ı tam süreç etiketi olarak koruyup, eksik heyetli denetlenmiş sonuçlar için `CERTIFIED / SERTİFİKA DOĞRULANDI` eklenmesini onaylıyor musunuz?

Ayrıca eksiksiz satır denetimini kapatmak için tasarım belgesiyle Faz 1 planını dosya olarak eklemeniz gerekiyor; GitHub aracındaki kesilen metni üçüncü kez tam okunmuş saymak doğru olmaz.










# Rigor — Deep Research IV  
## Önceki önerinin güvenlik denetimi ve uygulanabilir mimari sözleşme

Bu aşamanın temel sonucu: Önceki rapordaki dört etiketli hibrit öneri uygulanabilir bir adaydır, fakat tek başına yeterli değildir. Etiket kararından önce üç bağlantı güvenceye alınmalıdır:

1. Kullanıcının onayladığı formal ifade ile denetleyicinin kontrol ettiği ifade aynı olmalı.
2. Denetleyicinin kabul ettiği sonuç ile raporda gösterilen sonuç aynı olmalı.
3. Etiketi üretirken kullanılan kanıt, onay ve heyet kayıtları hâlâ aynı sürüme ait olmalı.

Bu bağlantılardan biri eksikse, geçerli bir matematiksel sertifika bile yanlış cevabın yanında güven etiketi üretebilir. Derleyici doğrulama literatüründeki *semantic preservation* ve *translation validation* ayrımı, önceki raporun eksik bıraktığı bu ara bağlantı için güçlü bir teknik dayanak sağlıyor. [inria.hal](https://inria.hal.science/inria-00360768v1/document)

Bu turda ayrıca iki somut yeni sonuç elde edildi:

- MCP’de API anahtarının normal form elicitation ile istenmesi yasaktır; URL modundaki `accept` yanıtı da kimlik doğrulama veya anahtar bağlama işleminin tamamlandığını göstermez. Önceki erişim önerisi bu protokol ayrıntısıyla tamamlanmalıdır. [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)
- DeepSeek Harness’in alt ajanları varsayılan olarak Rigor’un ihtiyaç duyduğu bağımsız hakemler değildir. Bağlam mirası, ortak çalışma dizini, ajanlar arası mesajlaşma ve değiştirilebilir eklenti politikaları açıkça yönetilmelidir. Bu sonuç artık yalnızca ürün tanıtımına değil, sabitlenmiş mimari belgelere ve incelenen kaynak koduna dayanıyor. [github](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/subsystems/subagent.md)

Önceki raporun sonunda sorulan etiket ve “ücretli model” tercihleri henüz cevaplanmadı. Bunları onaylanmış saymıyorum. `concepts_brief.md` içindeki altı bağlayıcı karar, özellikle yalnızca ücretsiz modellerle `KANITLANDI` verilmemesi koşulu korunuyor. [concepts_brief.md]

## I. Önceki araştırmanın eksiklik denetimi

### 1.1. Önem sırasına göre açıklar

| Öncelik | Önceki rapordaki eksik | Yanlış karar riski | Bu aşamadaki sonuç |
|---|---|---|---|
| Kritik | Sertifikanın doğru IR’dan türetildiği yeterince tanımlanmamıştı | Yanlış çevrilmiş ifadeyi kusursuz denetlemek | Çeviri/normalizasyon bağı ayrı yükümlülük yapılıyor |
| Kritik | Onay, hesap ve rapor arasındaki sürüm değişimi ele alınmamıştı | Eski onayla yeni sonucu yayımlamak | Değişmez problem anlık görüntüsü ve geçersizleştirme kuralları |
| Kritik | `USER_DIRECT` ile gerçek insan onayı arasındaki güven sınırı eksikti | İstemci veya ajan tarafından sahte onay | Onay kanalının güveni ve iddia bağlantısı ayrılıyor |
| Kritik | `CERTIFIED` için “onaylı denetleyici” yeterince operasyonel değildi | Bir başarı bayrağını kanıt kabul etmek | Desteklenen dil, önkoşullar, çıkış durumu ve kayıt sözleşmesi |
| Yüksek | Heyet ölçümü yalnızca yanlış `PROVEN=0` etrafında kurulmuştu | Her şeyi reddeden ama yararsız sistem | Risk–kapsama ve yanlış oybirliği ölçümleri |
| Yüksek | Tekrar deneyerek oybirliği bulmanın etkisi yoktu | Seçilmiş son turu bağımsız uzlaşma sanmak | Bütün girişimler kayıtlı; anlaşmazlık silinmiyor |
| Yüksek | Harness değerlendirmesi çoğunlukla belge/ürün düzeyindeydi | Alt ajanı bağımsız hakem saymak | Bağlam, çalışma dizini, mesaj ve yürütme kaynakları incelendi |
| Yüksek | JSON şeması ve hash için dil-arası ayrıntılar eksikti | Aynı görünen kaydı farklı anlamak | Tekrarlı anahtar, büyük sayı ve kanonikleştirme sözleşmesi |
| Yüksek | Matematiksel alanın motorlara korunarak taşınması yeterince sınanmamıştı | Rasyonel problem için reel çözümü kabul etmek | Alan-koruma testleri ve destek sınırları |
| Orta | Yeni etiketin UX üstünlüğü ima edilebilirdi | “Sertifika”yı kimlik veya bütün problem güvencesi sanmak | İsim tercihi deneysel olarak açık bırakılıyor |
| Orta | F1.5 önerisinin kapsamı sınırsız büyüyebilirdi | Tek geliştirici için yeni genel ispat altyapısı | Dar, açık işlem diline sınırlandırılıyor |

### 1.2. Önceki araştırmadaki bir yazım çelişkisi

Önceki raporun sonuç cümlesinde “`CERTIFIED` ile `CROSS_VALIDATED` arasında genel doğruluk sıralaması kurulmalıdır diye bir bilimsel zorunluluk yoktur” ifadesi dil bakımından gereksiz derecede dolaylıydı.

Doğru ve açık hüküm şudur:

> Bu etiketler arasında evrensel bir doğruluk olasılığı sıralaması yoktur. Varsa koşul içerme ilişkileri, açık mantıksal sözleşmelerden gelir; fiyat, rozet veya isimden gelmez.

Bu turda etiket sayısını artırmıyorum. Asıl eksik, daha fazla rozet değil; mevcut kaydın doğru iddiaya bağlanmasıdır.

### 1.3. İnceleme durumu ve sınırlar

Rigor dal uçları yeniden doğrulandı:

| Dal | Commit SHA |
|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` |

Önceki araştırmadan sonra bu dal uçlarında değişiklik yok.

Yeniden okunan geliştirme belgeleri:

- Tasarım: blob `a509f1287726fe8922b0d7a46fbf18e5b4d55896`
- Faz 1 planı: blob `8bed859fe37cd80dc1500fb92b9dcdeeabe1b741`
- Yol haritası: blob `97afa66e18678bf43b758bd6ced844e46fd949e9`

Kök ağaçta ürünün planlanan `src/` yapısı bulunmuyor. Dolayısıyla aşağıdaki değerlendirme uygulama denetimi değil, tasarım ve plan denetimidir. Plan içindeki test kodlarının varlığı, bunların çalıştırıldığı anlamına gelmez.

Önemli açık devam ediyor: GitHub aracı uzun tasarım ve Faz 1 dosyalarını keserek döndürüyor; doğrudan web erişimi de bu iki dosyayı getiremedi. Bu nedenle §6.4–§6.8 ile planın kesilen son kısmının eksiksiz satır denetimi bu aşamada da tamamlanamadı. Bunu kapanmış bir eksik olarak göstermiyorum.

## II. Yeni araştırma bulguları

### 2.1. Kanıt denetlemek, çeviriyi doğrulamak değildir

#### Yeni iddia

Rigor’da iki farklı doğrulama problemi bulunuyor:

\[
F \xrightarrow{\text{çeviri/normalizasyon}} P
\]

ve

\[
\operatorname{Check}(P,C)=\operatorname{ACCEPT}.
\]

Burada \(F\), kullanıcıya gösterilen formal IR; \(P\), motorun veya sertifika denetleyicisinin anladığı önerme; \(C\), sertifikadır.

İkinci işlem doğru çalışırken ilk işlem yanlış olabilir.

#### Kanıt

Leroy’nin *A formally verified compiler back-end* çalışması, doğrulanmamış bir dönüştürücünün çıktısının ayrı bir doğrulayıcıyla kontrol edilmesini açıkça ayırır. Özellikle §2.2, doğrulayıcının da yanlış olabileceğini ve formal garanti için onun sağlamlık özelliğinin gerektiğini belirtir. §2.3 ise bileşimin geçerliliğini ara dillerin semantiği ve geçiş ilişkileri üzerinden kurar. [inria.hal](https://inria.hal.science/inria-00360768v1/document)

#### Rigor’a etkisi

Önceki rapordaki “iddia hash’i eşleşti” şartı tek başına yeterli değildir. Hash yanlış çevrilen kaydı da tutarlı biçimde tanımlayabilir.

Asgari iki seçenek vardır:

- Bütün derleyicileri formal olarak doğrulamak.
- Dar desteklenen parçalarda, her dönüşümü bağımsız biçimde kontrol etmek veya denetleyicinin özgün IR’ı doğrudan yorumlamasını sağlamak.

Tek geliştirici için ikinci seçenek daha uygundur. Ancak bu, her matematik sınıfında kolay olduğu anlamına gelmez.

#### Desteklemediği sonuç

Bu literatür Rigor’un derleyicilerinde fiilî hata bulunduğunu göstermiyor. Yeni bir güven yükümlülüğünü ortaya koyuyor.

***

### 2.2. Faz 1’de matematiksel alanın korunması ayrıca sınanmalı

Görülen planda `NumberDomain` içinde `integer`, `rational`, `real`, `decimal` bulunuyor. Aynı plandaki motor eşlemeleri ise özellikle `integer → Int/integer=True`, diğer durumlar için `Real/real=True` yolunu tarif ediyor.

Bu bir uygulanmış hata bulgusu değildir; fakat şu karşı örneğin test edilmesini gerektirir:

\[
\exists x\in\mathbb Q:\quad x^2=2.
\]

Reel çözücü \(\sqrt2\) bulabilir. Geri ikame de \(x^2=2\) eşitliğini doğrulayabilir. Fakat bu, rasyonel alandaki varlık iddiasını doğrulamaz.

Ayrım yönlüdür:

- Bütün reeller için kanıtlanan bir özellik, uygun koşullarda rasyoneller için de geçerlidir.
- Reel alanda bulunan bir çözüm, rasyonel çözüm değildir.
- Reel gevşetmede uygulanabilirlik, tamsayılı veya rasyonel uygulanabilirlik değildir.

SymPy’nin resmî varsayım belgesi, `integer`, `rational`, `real` gibi alanların hesap davranışını etkilediğini ve varsayımları farklı sembollerin farklı nesneler olduğunu açıkça gösterir. [docs.sympy](https://docs.sympy.org/latest/guides/assumptions.html)

Somut değişiklik:

> Motor adaptörü yalnızca ifadeyi çevirmemeli; alan üyeliğinin, tanım koşullarının ve hedefteki nicelemenin nasıl korunduğunu da belirtmelidir. Koruyamadığı iddia türünü desteklemiyor saymalıdır.

Finans için de benzer bir sınır vardır: girdileri kesin rasyonel okumak, `Decimal` hassasiyet ve yuvarlama semantiğinin doğru modellendiğini tek başına göstermez.

***

### 2.3. `UNKNOWN`, kütüphane kabulü ve ispat kabulü farklıdır

SymPy’nin varsayım sistemi üç değer döndürür: `True`, `False`, `None`. Belge `None` değerinin bilinmeyen olduğunu ve bunun bir kütüphane hatası olmadığını özellikle açıklar. Bazı kütüphane fonksiyonları sembolik çalışmaya izin vermek için `None` durumunu reddetmez. [docs.sympy](https://docs.sympy.org/latest/guides/assumptions.html)

Rigor için bunun sonucu farklı olmalıdır:

- Bir kütüphane fonksiyonunun ifadeyi oluşturabilmesi, alan önkoşulunun doğrulandığı anlamına gelmez.
- `not False` ile `True` aynı değildir.
- “Aksine kanıt yok” durumu `PASS` yapılamaz.
- Geri ikame ve tanım alanı kontrolleri, orijinal IR’daki yükümlülükleri korumalıdır.

Örneğin:

\[
\frac{x}{x}=1
\]

eşitliği \(x\neq0\) koşuluna bağlıdır. Sadeleştirme sonucu 1 elde edilmesi, \(x=0\) noktasının görevden sessizce çıkarılmasına izin vermez.

Mevcut planda alan yükümlülükleri zaten düşünülmüş durumda. Yeni öneri “bu özellik yok” değildir; bu yükümlülüklerin sadeleştirme ve motor dönüşümü boyunca kaybolmadığının kabul ölçütü yapılmasıdır.

***

### 2.4. Hash sözleşmesinde iki yeni somut ayrıntı

#### A. Tekrarlı JSON anahtarları

Python’un varsayılan JSON okuyucusu tekrarlanan anahtarları kabul eder ve son değeri kullanır. Örneğin aynı nesnede iki `value` alanı bulunabilir; farklı araçlar bunu farklı yorumlayabilir. [docs.python](https://docs.python.org/3/library/json.html)

RFC 8785/JCS ise tekrarlı nesne anahtarlarını yasaklar. [rfc-editor](https://www.rfc-editor.org/rfc/rfc8785.html)

Rigor açısından:

> Pydantic şemasının bilinmeyen alanları reddetmesi, JSON çözümleme sırasında zaten kaybedilmiş tekrarlı anahtarları yakalamaz. Kontrol parser sınırında yapılmalıdır.

#### B. Büyük ve kesin sayılar

JCS’nin normal JSON sayı yolu IEEE-754 double temsilini esas alır. Daha yüksek hassasiyet veya büyük tamsayılar için string kullanımı önerilir. Ayrıca JCS’nin sıralama ve Unicode kuralları, yalnızca “JSON’ı anahtara göre sırala” demekten daha ayrıntılıdır. [rfc-editor](https://www.rfc-editor.org/rfc/rfc8785.html)

Rigor’un plandaki kesin sayı stringleri doğru yöndedir. Ancak şu sözleşme eklenmelidir:

- Matematiksel sayı stringleri hiçbir ara adaptörde JavaScript `Number`a çevrilmez.
- Kanonik biçim açıkça sürümlenir.
- Aynı rasyonelin yazım çeşitlerinin kimlik bakımından nasıl ele alındığı tanımlanır.
- “Python’da deterministik JSON” ile “RFC 8785 uyumlu JCS” aynı şeymiş gibi adlandırılmaz.

JCS’ye geçmek zorunlu değildir. Daha basit bir Rigor kanonik biçimi de seçilebilir; yeter ki tam tanımlı ve dil-arası test edilmiş olsun.

***

### 2.5. Onay–kontrol–rapor aralığı bir TOCTOU problemidir

MITRE CWE-367, bir kaynak kontrol edildikten sonra kullanıma kadar değişebiliyorsa kontrol sonucunun geçersizleşebileceğini tanımlar. [cwe.mitre](https://cwe.mitre.org/data/definitions/367.html)

Rigor örneği:

1. Kullanıcı sürüm A’yı onaylar.
2. Ajan veya şablon sistemi birim/model bağlamasını değiştirir.
3. Hesap sürüm B üzerinden yapılır.
4. Eski onay ve yeni sertifika aynı raporda birleştirilir.

Dosya veya bellek nesnesi düzeyinde bütün parçalar ayrı ayrı “geçerli” görünebilir; fakat birlikte aynı problemi temsil etmezler.

Yeni zorunlu kural:

> Onaydan sonra hesaplanan problem değişmez bir anlık görüntü olmalıdır. Anlamı etkileyen değişiklik yeni problem sürümü oluşturur; ilgili onay, heyet ve kanıt kayıtları yeni sürüme otomatik taşınmaz.

Bu, yeni bir dağıtık sistem altyapısı gerektirmez. Sürümlü kayıt ve tutarlı anlık görüntü yeterli başlangıçtır.

***

### 2.6. MCP’de `accept` yanıtı bütün onay türleri için aynı değildir

Güncel resmî elicitation spesifikasyonundan iki karar doğrudan çıkıyor:

- API anahtarı, parola ve token normal form modunda istenemez.
- URL modunda `action: "accept"`, kullanıcının etkileşime geçmeyi kabul ettiğini gösterir; dış işlemin tamamlandığını göstermez. Sunucu tamamlanmayı kendi tarafında kontrol etmelidir. [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)

Ayrıca spesifikasyon istemcinin bildirdiği kullanıcı kimliğine doğrulamadan güvenilmemesini söyler. MCP güvenlik belgesi de durum tanıtıcısına sahip olmanın kimlik doğrulama olmadığını vurgular. [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)

Rigor için üç ayrı kayıt gerekir:

1. Matematiksel tanımı onaylama.
2. Uzak sağlayıcıya veri gönderimine izin verme.
3. Sağlayıcı erişimini başarıyla bağlama.

Biri diğerinin yerine kullanılamaz.

Önceki raporun “güvenilen kanal olayı” önerisi doğru yöndeydi; fakat MCP formundan gelen her `accept` olayını koşulsuz insan onayı saymak hâlâ yanlıştır. Rigor, istemci/host uygulamasının güvenini açıkça varsaymak veya daha güçlü bir bant dışı onay yolu kullanmak zorundadır.

***

### 2.7. Heyet başarısını yalnızca oybirliğiyle ölçmek yetersiz

Bu turda okunan yeni bir hakemli çalışma, LLM topluluklarında hata korelasyonu, üye yeterliği ve topluluk büyüklüğünün ayrı değerlendirilmesi gerektiğini gösteriyor. Çalışmanın teorik sonuçları değiştirilebilirlik ve belirli ortak korelasyon varsayımlarına bağlı; küçük MMLU uygulaması farklı ailelerin bağımsızlığa eşit olmadığını gösteriyor. [link.springer](https://link.springer.com/article/10.1007/s44564-026-00040-z)

Önemli sınır: Bu sonuçları Rigor’un formal denklik katmanına doğrudan bir hata yüzdesi olarak taşımak doğru değildir.

Daha doğrudan yeni deneysel bulgu, Batra ve arkadaşlarının çalışmasıdır:

- Üç açık ağırlıklı model ayrı ayrı inceleniyor.
- Tartışma, aynı hesap bütçeli bağımsız yeniden düşünme koşuluyla karşılaştırılıyor.
- Bazı doğruluk kazanımları küçük kalırken yanlış oybirliği artabiliyor.
- Çalışma üç aynı-model ajanıyla yürütülüyor; heterojen Rigor heyetini doğrudan sınamıyor. [arxiv](https://arxiv.org/html/2610.35930v1)

Mimari etkisi:

- Rigor’un kör ilk formülasyonları korunmalı.
- Sonradan birbirini görerek uzlaşmış adaylar, ilk kör adaylar gibi sayılmamalı.
- “Ayrışmadılar” ile “doğru yorumladılar” ayrı ölçülmeli.
- Model ailesi sayısı, tek başına bağımsızlık ölçümü değildir.

***

### 2.8. Yeni değerlendirme açığı: Sıfır yanlış etiket, sıfır yararlılık pahasına elde edilebilir

Geifman–El-Yaniv’in seçici sınıflandırma çalışması, hata riskinin kabul edilen örnekler üzerinde; kapsamanın ise ne kadar örneğe cevap verildiği üzerinden değerlendirilmesini açıkça ayırır. Çalışmanın garantileri belirli sınıflandırma ve örnekleme varsayımlarına bağlıdır; Rigor’a hazır istatistiksel garanti sağlamaz. [proceedings.neurips](https://proceedings.neurips.cc/paper_files/paper/2017/file/4a8423d5e91fda00bb7e46540e2b0cf1-Paper.pdf)

Rigor için alınacak ders:

- Yanlış `PROVEN` sayısı tek başına yeterli başarı ölçütü değildir.
- Hangi görevlerin reddedildiği de ölçülmelidir.
- Formülasyon hatası oranı, yayımlanan sonuçlarda ayrıca ölçülmelidir.
- Eşdeğer ama farklı yazılmış doğru formülasyonların gereksiz reddi izlenmelidir.
- Ücretli ve ücretsiz heyetler, aynı görevlerde ve aynı bütçe koşullarında karşılaştırılmalıdır.

Bu, güven yüzdesi üretme önerisi değildir. Sistem düzeyi değerlendirmede risk ve kapsamanın birlikte raporlanmasıdır.

### 2.9. Yeni Harness bulguları: Alt ajan olmak bağımsız hakem olmak değildir

İnceleme sabitlendi:

- Dal: `master`
- Commit: `fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159`
- Commit tarihi: 4 Kasım 2026
- Commit mesajı: `0.2.2-rc.1` sürüm dalının birleştirilmesi

İncelenen birincil belgeler ve kaynaklar:

- `SAFETY.md`
- `docs/architecture.md`
- `docs/subsystems/subagent.md`
- `packages/core/tools/src/executor.ts`
- `packages/core/tools/src/pipeline.ts`
- `packages/core/tools/tests/execution-mode.spec.ts`

#### Somut bulgular

| Bulgu | Rigor açısından anlamı |
|---|---|
| Alt ajan çalışma dizini belirtilmezse ebeveynin etkin dizinini alır | Aynı dosyalardan önceki adayları okuyabilir |
| `fork` ve varsayılan kompozisyon mirası vardır | Temiz başlangıç varsayılamaz |
| Ajanlar dallar arasında mesajlaşabilir | Kör üretim ayrıca uygulanmalı |
| `inheritsParentContext` tanımlayıcı bir alan; servisçe doğrulanan tam izolasyon yetkisi değil | Tek bir flag bağımsızlık kanıtı olamaz |
| `outputSchema` desteği backend’e bağlıdır; şema talebi başarılı çıktı garantisi değildir | `completed` ve geçerli yapılandırılmış çıktı birlikte kontrol edilmeli |
| Model adaptörü, araç kaydı, oturum kaydı ve döngü eklentilerle değiştirilebilir | Harness konfigürasyonu güven tabanının parçasıdır |
| Python SDK normal Harness çalışma zamanını başlatır | “Python arayüzü var” ek çalışma zamanı yükünü kaldırmaz |

Bu hükümler doğrudan sabitlenmiş alt ajan ve mimari belgelerinde yer alıyor. [github](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/subsystems/subagent.md)

#### Kaynak kodundan ek bulgu

İncelenen `pipeline.ts` içinde:

- Çağrı girdileri kopyalanıp donduruluyor.
- Çıktı değeri şemayla doğrulanıyor.
- Ön/son yürütme eklenti noktaları bulunuyor.
- Son yürütme katmanı içerik veya değer üzerinde tanımlı değişiklik yapabiliyor.
- Onay gerektiren bir karar için onay servisi yoksa ret yolu bulunuyor.
- Fakat bu, her araç çağrısının zorunlu insan onayından geçtiği anlamına gelmiyor.

Bu davranış bir güvenlik açığı ilanı değildir; güvenilen eklenti mimarisinin sonucudur. Rigor açısından kritik olan, şeması geçerli bir tool sonucunun ve ekranda gösterilen metnin aynı güvence nesnesi olmadığını fark etmektir.

Okunan `execution-mode.spec.ts` ise esas olarak paralel/özel yürütme sınıflandırmasını ve bazı şema görünürlüğü kurallarını sınar. Bu dosya, bütün Harness izin sisteminin veya Rigor hakem izolasyonunun doğrulandığını göstermez.

Harness’in kendi güvenlik belgesi de güvenlik denetimi yapılmadığını ve tek güvenlik kontrolü olarak kullanılmaması gerektiğini açıkça söyler. [github](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/SAFETY.md)

## III. Çelişkilerin çözümü

### 3.1. Artık teknik olarak çözülebilenler

| Anlaşmazlık | Sonuç |
|---|---|
| Sertifika gücü model fiyatından etkilenir mi? | Aynı formal iddia ve aynı geçerli kanıt için hayır |
| Karar 5 bu nedenle yok sayılabilir mi? | Hayır; üst ürün etiketi için bağlayıcı politika olarak kalır |
| Heyet formal denklik kullanıyorsa ortak hata sorunu biter mi? | Hayır; aynı yanlış yoruma denk adaylar üretilebilir |
| `CERTIFIED` yeni bir doğruluk yüzdesi midir? | Hayır; belirli kanıt kontrolünün kategorisidir |
| Harness’in çoklu ajan özelliği bağımsız hakemlik sağlar mı? | Kendiliğinden sağlamaz |
| Form elicitation ile API anahtarı toplanabilir mi? | Güncel MCP sözleşmesinde hayır |
| URL elicitation `accept` erişim tamamlandı demek mi? | Hayır |
| Eski onay yeni problem sürümüne taşınabilir mi? | Açık kapsamlı bir yeniden kullanım kuralı olmadan hayır |

Bu sonuçlar formal doğrulama, MCP ve Harness’in birincil belgeleriyle destekleniyor. [inria.hal](https://inria.hal.science/inria-00360768v1/document)

### 3.2. Gerçek uzlaşma olmayan nokta

Şu iki ürün tercihi aynı değildir:

- `KANITLANDI`, yalnızca formal matematiksel iddianın kanıt durumudur.
- `KANITLANDI`, matematiksel kanıtla birlikte tam Rigor süreç koşullarının tamamlandığını gösterir.

Bilimsel kaynaklar bu isimlendirme tercihini tek başına çözmez. Önceki rapor ikinci seçeneği önerdi; sahibi henüz onaylamadı.

Dolayısıyla bu araştırma ilk seçeneği “yanlış matematik” diye reddetmiyor. Yeni bağlayıcı kararlar, mevcut ürün anlamı ve kullanıcıda kapsam genellemesi riski nedeniyle ikinci seçeneği daha uygun buluyor.

### 3.3. Red Team’in hâlâ sınırlandırılması gereken iddiası

“Daha üst heyet uygulanırsa fark edilmemiş formülasyon hatası artık güvenli biçimde elenir” sonucu desteklenmiyor.

Üst heyet hata yakalama ihtimalini artırabilir; fakat bunun gerçek katkısı görev, model, bağlam ve yöntem üzerinden ölçülmelidir. Yeni korelasyon ve tartışma çalışmaları da bu sınırı güçlendiriyor. [link.springer](https://link.springer.com/article/10.1007/s44564-026-00040-z)

Bu nedenle `PROVEN` tanımı, bütün kullanıcı niyetinin matematiksel olarak kanıtlandığı izlenimini vermemelidir.

## IV. Düzeltilen sonuçlar

### Korunanlar

- Matematiksel kanıt, problem yorumu ve fiziksel geçerlilik ayrımı.
- Ücretsiz erişimin her zaman mevcut olmadığı.
- Yalnızca ücretsiz heyet için üst etiket yasağının korunması.
- `unsat_core` ile denetlenmiş ispatın ayrılması.
- Aynı CAS ile kontrolün bağımsız denetleyici diye sunulmaması.
- Faz 1’de `PROVEN`ın kapalı kalması.
- Harness’in çekirdek bağımlılık yapılmaması. [concepts_brief.md]

### Güçlendirilenler

- İddia kimliği artık yalnızca hash değil; semantik alan ve dönüşüm yükümlülüğü içeriyor.
- Onay artık yalnızca kim tarafından değil, hangi problem sürümüne verildiğiyle tanımlanıyor.
- Heyet bağımsızlığı artık yalnızca model ailesi değil; bağlam, dosya, mesaj ve tekrar deneme düzeniyle ele alınıyor.
- Başarı ölçümü artık yanlış etiket sayısının yanında kapsama ve yanlış oybirliğini de içeriyor.

### Değiştirilenler

- Önceki raporda `CERTIFIED` için önerilen kabul kaydı, çeviri/normalizasyon bağını kapsamadan yeterli sayılmıştı. Artık yeterli değil.
- “Bağımsız denetleyici” ifadesinin kendisi, denetleyici uygulamasının formal olarak doğrulanmış olduğu anlamına gelmiyor. Bu iki özellik ayrı kaydedilmeli. [inria.hal](https://inria.hal.science/inria-00360768v1/document)
- Kullanıcının onayladığı varsayım, doğrulanmış fiziksel gerçek gibi ele alınmamalı.
- Haricî ajanın yeniden anlattığı rapor, Rigor’un kanonik raporuyla aynı güvenceye sahip kabul edilmemeli.

### Geri çekilen bir varsayım

Yeni bir etiketin adının “SERTİFİKA DOĞRULANDI” olması, kullanıcıdaki yanlış kapsam genellemesini çözdüğü için seçilmiş değildir. Bu bir aday metindir. “Sertifika” kelimesi de kriptografik imza veya kurum onayı gibi yanlış anlaşılabilir.

Bu nedenle arayüzde “matematiksel sertifika” ifadesi ve açık kapsam cümlesi korunmalıdır. İsim değişikliği, kullanıcı çalışmasının yerine geçmez.

## V. Adversarial değerlendirme

Aşağıdaki karşı örnekler çalıştırılmış ürün testleri değil, önerilen mimariye karşı tasarlanmış test sözleşmeleridir.

| Karşı örnek | Risk | Gerekli değişiklik |
|---|---|---|
| Onaylı IR’de katsayı `0,3048`, denetleyiciye giden ifadede başka katsayı | Geçerli ama yanlış ifadeye ait kanıt | Denetleyici özgün IR’ı veya doğrulanmış dönüşümünü kontrol etmeli |
| Rasyonel değişken reel motora aktarılıyor | Reel çözüm yanlış alanda kabul edilir | Alan-koruma yükümlülüğü |
| Sadeleştirme `x/x` alan koşulunu düşürüyor | Tanımsız noktada özdeşlik iddiası | Orijinal IR alan koşulları korunmalı |
| `None` sonucu “ihlal yok” diye geçiyor | Bilinmeyen, kanıtlı sayılır | Üç değerli kararın açık eşlenmesi |
| JSON’da aynı `value` iki kez var | Farklı parser’lar farklı iddia görür | Tekrarlı anahtarların parser sınırında reddi |
| Büyük tamsayı TypeScript tarafında `Number`a çevriliyor | Tam girdide sessiz yuvarlama | Matematiksel sayılar kanonik string |
| Kullanıcı sürüm A’yı onaylıyor, rapor B’yi gösteriyor | Eski onayla yeni cevap | Değişmez snapshot ve revizyon kontrolü |
| Heyet ayrışıyor; sistem uygun üç cevap bulana kadar tekrar ediyor | Seçilmiş oybirliği | Bütün girişimler kayıtlı; ayrışma silinmez |
| Harness child ebeveynin aday dosyasını okuyor | Görünürde kör üretim | Ayrı okuma alanı ve araç yetkisi |
| Harness `fork` önceki gerekçeyi miras alıyor | Bağımsızlık yanılsaması | Kör üretimde geçmişsiz başlangıç |
| Onay servisi “izin verdi” diye matematik tanımı onaylanmış sayılıyor | Yetki türleri karışır | Tool izni, veri paylaşımı ve tanım onayı ayrı |
| Uzak tool çıktısı doğru, sonraki eklenti metni değiştiriyor | Teknik doğru, görünür rapor yanlış | Kanonik sonuç ayrı doğrulanabilir olmalı |
| Sonlu testlerde hiç yanlış `PROVEN` yok ama her şey reddediliyor | Yararsız güvenli sistem | Risk–kapsama ölçümü |
| Kanıt dosyası aşırı derin/çok büyük | Denetleyici kaynak tüketimi | Boyut, derinlik ve çalışma bütçesi |
| Denetleyici zaman aşımına uğruyor, sistem “muhtemelen doğru” diye devam ediyor | Başarısız kontrol güvene dönüşür | `INCOMPLETE`; `ACCEPT` yerine geçmez |

Python belgeleri güvenilmeyen JSON’un CPU/bellek tüketimini ve varsayılan parser davranışlarını açıkça uyarır. Bu nedenle sertifika ve IR doğrulaması yalnızca matematiksel değil, kaynak güvenliği bakımından da sınırlanmalıdır. [docs.python](https://docs.python.org/3/library/json.html)

### 5.1. Karmaşık mühendislik örneği: Yanlış referans çerçevesi

Bir statik marjin hesabında:

\[
SM=\frac{X_{CP}-X_{CG}}{D}
\]

işlemi doğru olabilir. Fakat CP ve CG farklı referans noktalarından ölçülmüşse çıkarma fiziksel olarak amaçlanan büyüklüğü temsil etmez.

Birim kapısı bunu yakalamayabilir: iki değer de metre cinsindedir.

Gerekli kontrol yalnızca boyut değil; koordinat referansı ve yönüdür. Bu, formal IR/model bağlamasında bulunmalı ve onay metninde gösterilmelidir.

### 5.2. Finans örneği: Tam değer, yanlış işlem sırası

Bir ücret:

\[
\text{oran}\times\text{nominal}
\]

olarak kesin hesaplanabilir. Ancak sistem önce miktarı yuvarlaması gerekirken önce ücreti yuvarlıyorsa, her çarpma doğru olsa bile işlem semantiği yanlıştır.

Bu nedenle `Decimal` veya rasyonel aritmetik kullanımı tek başına finansal sonucun doğruluğunu göstermez. Yuvarlama noktası, modu ve hangi varlık biriminde yapıldığı iddianın parçasıdır.

### 5.3. Yanlış soyut “en zayıf halka” kuralı

Bütün alt sonuçların en düşük etiketini üst sonuca vermek de her zaman doğru değildir.

Örneğin yaklaşık bir ara hesap kullanılmadan başka bir özellik doğrudan kanıtlanmış olabilir. Bu durumda kullanılmayan zayıf dalın etiketi üst iddiayı düşürmemelidir.

Doğru kural:

> Üst iddia, gerçekten bağlı olduğu varsayım ve kanıtlarla değerlendirilir.

Bu, genel bir grafik altyapısını v1’de zorunlu kılmaz; fakat hangi girdilerin hangi iddiada kullanıldığı kaydedilmelidir.

## VI. Nihai mimari öneriler

### 6.1. Önceki dört kategoriyi koru, kararı doğrudan olaylara bağla

Önerilen kategoriler değişmiyor:

| Kategori | Anlam |
|---|---|
| `PROVEN` | Matematiksel kabul + sürümlü tam Rigor politika koşulları |
| `CERTIFIED` | Belirtilen matematiksel iddiaya ait kabul edilmiş sertifika |
| `CROSS_VALIDATED` | Gerçek ayrı yöntem karşılaştırması |
| `REFUSED` | İstenen cevap yayımlanmadı |

Ancak istemci şu alanları doğrudan belirleyememeli:

- `certificate_accepted`
- `user_confirmed`
- `model_families`
- `full_panel_passed`
- sonuç etiketi

Bunlar doğrulama ve onay kayıtlarından türetilmelidir.

Bu, in-process Python kullanıcısına karşı mutlak yetki ayrımı anlamına gelmez. Kullanıcı Rigor sürecinin veya dosyalarının tamamını değiştirebiliyorsa, salt bir enum bunu engelleyemez. Tehdit modeli açıkça şunu hedeflemelidir:

- Güvenilmeyen model çıktısı.
- Güvenilmeyen uzak motor cevabı.
- Sınırlı yetkili çağıran ajan.
- Bozuk veya yanlış bağlanmış oturum kaydı.

Tamamen ele geçirilmiş yerel işletim sistemi için matematiksel etiketin bütünlük garantisi verdiği iddia edilmemelidir.

### 6.2. Küçük bir sonuç paketi yeterli

Yeni servisler ve ikinci bir genel durum makinesi yerine, mevcut `Outcome`, `Conditions`, `Certificate` ve oturum kaydı genişletilebilir.

Asgari içerik:

| Kayıt | Gerekli alanlar |
|---|---|
| Problem | Kanonik IR, semantik sürüm, birim/model tanımları, problem revizyonu |
| İddia | Hedef özellik ve çıktı büyüklükleri |
| Kanıt | Tür, kontrol durumu, denetleyici profili, bağlı iddia |
| İnceleme | Adaylar, eşleme/denklik sonuçları, model/adaptör kayıtları |
| Onay | Onay türü, kanal, problem revizyonu |
| Yayın kararı | Politika sürümü, geçti/eksik/başarısız koşullar |
| Rapor | Aynı sonuç paketinden türetilmiş görünüm |

Bu bir SACM uygulaması veya veritabanı grafiği değildir. Yalnızca kanıtın yanlış nesneye bağlanmasını önleyecek asgari ilişkisel kayıttır.

### 6.3. Kritik kapılar üç durumlu olmalı

Her zorunlu kapı:

- `PASS`
- `FAIL`
- `UNKNOWN/INCOMPLETE`

üretmelidir.

Ayrıca `NOT_APPLICABLE`, yalnızca politika o görev türü için izin veriyorsa kullanılmalıdır.

Kurallar:

- `UNKNOWN`, `PASS` değildir.
- Eksik heyet, başarısız matematik kontrolüyle aynı değildir.
- Tamamlanmamış kanıt denetimi, yanlış önerme kanıtı değildir.
- Başarısız zorunlu matematik kontrolü sessizce daha düşük bir güven kategorisine düşürülerek geçilemez.
- Ayrı geçerli kanıt yolu bulunursa bütün olaylar korunarak yeniden karar verilebilir.

### 6.4. Formülasyon hakemliği iki aşamalı olmalı

Önerilen düzen:

1. Kör aday üretimi.
2. Adayların kapatılması: sonradan değiştirilmemiş ilk sürümler saklanır.
3. Kaynak kapsamı, değişken eşlemesi ve formal denklik.
4. Varsa karşı örnek ve itiraz incelemesi.
5. Gerekli kullanıcı açıklaması.
6. Yeni problem sürümü oluştuysa tekrar hesap.

Sonradan tartışmayla oluşan fikir birliği, ilk kör oybirliği diye kaydedilmez. Bütün denemeler ve başarısız adaylar korunur.

Bu, çoklu ajan tartışmasını bütünüyle yasaklamaz; onun kanıt türünü doğru adlandırır. Yeni deneyler, tartışmayla oluşan uzlaşmanın bağımsız destek gibi sayılmaması gerektiğini güçlendiriyor. [arxiv](https://arxiv.org/html/2610.35930v1)

### 6.5. Doğrudan formal IR, gerçek bir alternatif olmaya devam etmeli

Doğal dil yoksa “doğal dil çevirisi” kapısı uygulanamaz olabilir. Ancak:

- Alan ve birim semantiği yine kontrol edilir.
- Kullanıcının istediği hedef ile kanıtlanan özellik aynı olmalıdır.
- Karar 5’e ilişkin üst etiket politikası sahibin onayı olmadan atlanmaz.
- Matematiksel kanıtın gücü LLM yok diye zayıfmış gibi gösterilmez.

Bu ayrım önceki bilimsel sonucu korur; ürün etiketinin yeniden tanımını dayatmaz.

### 6.6. Harness için karar: İstemci olabilir, güven otoritesi olmamalı

Yeni kaynak incelemesinden sonra karar daha güçlü gerekçelendirilmiştir:

- Rigor çekirdeği Harness içinde eklenti olarak eritilmemeli.
- Harness, Rigor’u çağıran isteğe bağlı istemci olabilir.
- Rigor’un kanıt ve etiket kararı Harness ajanının yazdığı metinden alınmamalı.
- Kör formülasyon için ayrı geçmiş, sabit model, sınırlı dosya erişimi ve ajanlar arası mesaj yasağı gerekir.
- `fork`, bağımsız üretim yolu olarak varsayılan kabul edilmemeli.
- `completed` durumuna ek olarak geçerli yapılandırılmış çıktı aranmalı.
- Harness’in model/tool/oturum eklenti kompozisyonu kaydedilmeli; sonradan değişirse adaptör yeterliği yeniden değerlendirilmeli.
- Kullanıcının anahtarları ve Rigor’un onay yetkisi aynı geniş yetkili ajan sürecine gereksiz yere verilmemeli.

Harness’in modülerliği bu entegrasyonu kolaylaştırabilir; aynı modülerlik güven tabanını da büyütür. Mimari belge her temel parçanın değiştirilebilir olduğunu açıkça belirtir. [github](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/architecture.md)

## VII. Rigor’a özgü uygulanabilir değişiklikler

### 7.1. Mevcut mimaride korunacaklar

- Alan bağımsız çekirdek.
- SDK ve ince MCP kabuğu.
- Tipli IR ve güvenilmeyen metni `eval` yoluyla işlememe.
- Birim, yapı ve alan kapıları.
- Deterministik anlatım ve rapor.
- Kaynak/onay kökeni.
- Tek formülasyonlu Faz 1’de `PROVEN` yasağı.
- Fiziksel modelin gerçekliğini matematiksel kanıtla eşitlememe.
- Ücretsiz-only üst etiket sınırı. [concepts_brief.md]

### 7.2. Uygulama durumu

| Bileşen | Depoda doğrulanan durum | Bu raporun önerdiği ek |
|---|---|---|
| Formal IR | Planlanmış şema | Alan/semantik koruma sözleşmesi |
| Birim sistemi | Pint + kesin sayı planı | Birim tanımı manifesti ve ölçek testleri |
| Sertifika | SymPy geri ikame ve tür kayıtları planı | Açık kabul olayı ve iddia bağlantısı |
| Bağımsız denetleyici | Görülen F1 kısmında genel bir denetleyici yok | Dar rasyonel alt dil |
| Heyet | F3 planı | Kör sürüm kaydı ve bütün denemelerin saklanması |
| Adaptör | F3 planı | Sürüm/yetki/bağlam sözleşmesi |
| SDK/MCP | F1 planı | Onay türlerinin ve sır kanalının ayrılması |
| Rapor | F1 deterministik plan | Aynı değişmez sonuç paketinden üretim |
| Harness | Rigor’a uygulanmış entegrasyon görülmedi | Sonraki aşamada opsiyonel istemci |

### 7.3. Tasarım belgesine eklenecek somut hükümler

Aşağıdakiler onaylanmış değişiklik değil, karar metni önerileridir.

#### §4.1 — Etiketin kanıt kaydıyla bağı

> Sonuç etiketi, çağıranın gönderdiği güven alanlarından değil, bağlı ve sürümlü kontrol kayıtlarından türetilir. Bilinmeyen veya tamamlanmamış zorunlu koşul geçti sayılamaz. Matematiksel kabul, tam süreç uygunluğu ve yöntem karşılaştırması ayrı kanıt türleridir.

#### §4.3 — Onayın kapsamı

> Her onay; onay türüne, problem revizyonuna ve güvenilen etkileşim kanalına bağlanır. Matematiksel tanım onayı, veri paylaşımı izni ve sağlayıcı erişimi bağlama işlemi birbirinin yerine geçmez. Anlamı etkileyen problem değişikliği ilgili onayı geçersiz kılar.

#### §6.2 — Semantik koruma

> IR’dan motor veya sertifika diline yapılan çeviri; sayı alanı, tanım koşulları, birim ölçeği, referans çerçevesi ve hedef özelliği korumalıdır. Adaptör desteklemediği semantik için sessiz gevşetme yapamaz. Sadeleştirme, orijinal IR’ın alan yükümlülüklerini ortadan kaldıramaz.

#### §6.3 — Üç değerli kontroller

> Kütüphane kontrollerinin bilinmeyen sonucu, zorunlu koşulun sağlandığı anlamına gelmez. `PASS`, `FAIL` ve `UNKNOWN/INCOMPLETE` ayrılır. Kaynak veya model varsayımının kullanıcı tarafından onaylanması, varsayımın fiziksel gerçekliğinin doğrulanması sayılmaz.

#### §6.4 — Heyet ve yeniden denemeler

> İlk kör adaylar değişmez biçimde saklanır. Tartışma sonrası uzlaşma ilk bağımsız oybirliği olarak raporlanamaz. Sistem yalnızca uyuşan son adayları seçerek önceki ayrışmaları gizleyemez. Üst heyet ölçümü hata, kapsama ve yanlış oybirliğini birlikte içerir.

#### §6.6 — Kanıtlanan iddia

> Bir sertifikanın kabulü yalnızca kontrol edilen tam iddia için geçerlidir. Denetleyiciye sunulan iddianın onaylı IR’dan doğru türetildiği güvenceye alınmalıdır. Denetleyicinin bağımsız olması ile denetleyici uygulamasının formal olarak doğrulanmış olması ayrı niteliklerdir.

#### §6.7–§6.8 — Rapor görünümü

> Kritik sonuç, birim, iddia türü ve etiket aynı değişmez sonuç paketinden üretilir. Haricî ajan tarafından yeniden yazılan özet, Rigor’un kanonik raporunun yerine geçmez. Rapor, kaynak gerçekliği veya bütün problem doğruluğu için kanıt dışı bir kapsam oluşturamaz.

#### §8.2 — Sır ve onay kanalı

> API anahtarları normal MCP form elicitation veya model konuşması üzerinden toplanmaz. Uygun URL modu veya ayrı güvenli yerel yapılandırma kullanılır. URL etkileşimine `accept` yanıtı, erişimin bağlandığına dair tamamlanma kaydı değildir. Sırlar istemciye veya model bağlamına geri aktarılmaz.

Bu son hüküm güncel MCP sözleşmesinin doğrudan gereğidir. [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)

### 7.4. Faz planında en küçük güvenli değişiklik

Yeni genel framework yerine:

- F1: sıkı parser, üç durumlu kontroller, problem revizyonu, kanıt/rapor bağlantısı.
- F1 sonu veya dar F1.5: yalnızca kesin rasyonel ifadeler için bağımsız kontrol yolu.
- F2: model/koordinat bağlaması ve aralıklı girdilerin bileşimi.
- F3: heyet kayıtları, kör üretim, adaptör yeterliği ve risk–kapsama ölçümü.
- Sonraki: Harness istemcisi ve daha genel kanıt motorları.

K2’deki “gecikme öncelik değil” kararı, güvenilmeyen girdiye sınırsız kaynak vermek anlamına gelmemeli. Kaynak sınırına ulaşmak yanlış veya yaklaşık sonuç üretmez; tamamlanmamış kontrol durumu üretir.

## VIII. Kabul kriterleri ve test planı

### 8.1. Öncelikli yeni testler

| Test | Kabul kriteri |
|---|---|
| Onaylı IR ile denetlenen ifade farklı | Etiket yayımlanmaz |
| Rasyonel değişken için \(\sqrt2\) çözümü | Rasyonel çözüm kabul edilmez |
| Reel evrensel teoremden rasyonel özel duruma geçiş | Yalnızca tanımlı güvenli kural altında kabul |
| \(x/x\) sadeleştirmesi, \(x=0\) | Alan ihlali korunur |
| SymPy koşulu `None` | Zorunlu kapı geçmez |
| JSON tekrarlı anahtar | Şema öncesinde ret |
| Büyük tamsayı Python→TypeScript→Python | Matematiksel değer değişmez |
| Problem onaydan sonra değiştirilir | Eski onay ve ilgili kanıt yeni sürüme taşınmaz |
| URL elicitation kabul, dış işlem tamamlanmadı | Erişim “bağlandı” sayılmaz |
| Ajan normal tool izni alır | Matematiksel tanım onayı oluşmaz |
| Heyet önce ayrışır, sonra uyuşur | İlk ayrışma kayıtta kalır |
| Bütçe bitince eksik aday atılır | Heyet eşiği sessizce düşürülmez |
| Harness child önceki aday dosyasını okuyabilir | Kör üretim yeterliği başarısız |
| Harness sonucu `max-tokens` ile biter | Kısmi yapı geçerli aday sayılmaz |
| Tool değeri doğru, görünür metin değiştirilmiş | Kanonik raporla eşleşme kontrolü başarısız |
| Çok büyük/derin sertifika | Kontrollü sonlandırma; başarıya dönüşmez |
| Rapor ve ayrıntı tablosu farklı durum gösterir | Rapor üretimi başarısız |

### 8.2. Etiket mantığı için değişmezler

Aşağıdaki özellikler bütün desteklenen görevlerde sınanmalıdır:

- Eksik bir zorunlu kanıt alanını silmek etiketi yükseltemez.
- Ücretli erişim eklemek matematiksel kabul kaydını değiştiremez.
- İlgisiz bir düşük güvenceli dal, kullanılmayan bir kanıtı bozmaz.
- Yaklaşık bir girdiye “exact” etiketi eklemek onu gerçek tam değere dönüştüremez.
- Dil değişimi matematiksel ve süreç durumunu değiştiremez.
- Eski rapor yeniden açıldığında eski politika ve güncel yeniden değerlendirme ayrılır.
- Denetleyici çökmesi veya zaman aşımı `ACCEPT` olamaz.
- Aynı belgenin yalnızca sayı gösterimi değişirse, gösterim eşitliği ayrıca kontrol edilir.

### 8.3. Heyet değerlendirmesi

Asgari karşılaştırmalar:

1. Tek model.
2. Aynı aileden birkaç bağımsız çağrı.
3. Farklı aileler, kör üretim.
4. Aynı adaylar üzerinde tartışma.
5. Ücretsiz heyet.
6. Aynı bütçe sınırında karma heyet.

Ölçümler:

- Kaynak koşulu atlama.
- Yanlış birim/çerçeve bağlama.
- Yanlış oybirliği.
- Doğru azınlığın bastırılması.
- Gereksiz ret.
- Yayımlanan sonuçlarda semantik hata.
- Görev kapsaması ve maliyet.

Test görevleri yalnızca birim dönüşümü değil; kütle bütçesi, CP/CG referansı, rampa çıkışı, tamsayılı optimizasyon ve finansal yuvarlama sırası içermelidir.

Bu ölçümlerden vaka başına sahte güven yüzdesi türetilmemelidir. Seçici sınıflandırma literatüründeki istatistiksel garantiler, uygun örnekleme ve yöntem koşulları olmadan Rigor’a taşınamaz. [proceedings.neurips](https://proceedings.neurips.cc/paper_files/paper/2017/file/4a8423d5e91fda00bb7e46540e2b0cf1-Paper.pdf)

### 8.4. Deneysel durum

Bu raporda:

- Rigor veya Harness kurulmadı.
- Test çalıştırılmadı.
- Yeni kod yazılmadı.
- Depo değiştirilmedi.
- Kaynak ve test dosyaları okundu.
- Negatif testler ve sözleşmeler tasarlandı.

Dolayısıyla “test geçti” değil, “test gereği belirlendi” sonucu veriyorum.

## IX. Açık kalan kararlar

### 9.1. Sahip onayı gerektirenler

| Karar | Durum | Öneri |
|---|---|---|
| `CERTIFIED` eklenmesi | Açık | Dört kategorili hibrit aday korunsun |
| Türkçe adı | Açık | “Matematiksel sertifika doğrulandı” ifadesi denensin |
| `PROVEN`ın tam süreç anlamı | Açık | Mutlak niyet doğruluğu değil, sürümlü politika uygunluğu |
| Ücretli modelin operasyonel tanımı | Açık | Gerçek ödeme tutarı yerine açık erişim/yeterlik tanımı; Karar 5 yine korunur |
| Bir veya iki ücretli aile | Açık | Bilimsel zorunluluk değil; görev ve bütçe değerlendirmesi |
| Dar bağımsız denetleyicinin fazı | Açık | Genel ispat sistemi değil, küçük rasyonel alt dil |
| Harness’in rolü | Açık | Sonraki aşamada istemci/adaptör; çekirdek otorite değil |

Bu konular yeni araştırmayla sahibin yerine karara bağlanamaz. Önceki sorulara cevap gelmediği için bunları yeniden yorumlayıp onaylanmış saymıyorum. [concepts_brief.md]

### 9.2. Kanıtla henüz kapanmayanlar

- Kesilen Rigor belge bölümlerinin eksiksiz satır denetimi.
- Dar denetleyicinin gerçek uygulaması ve bağımsız incelemesi.
- Türkçe özetin kullanıcılarca anlaşılması.
- Rigor’a özgü model/heyet kıyaslaması.
- Harness izolasyon profilinin fiilî saldırı testi.
- Sağlayıcının gerçek model yürütmesini sunucu beyanından bağımsız doğrulamak.
- Politika ve denetleyici sürümü değişince eski raporların kullanıcıya nasıl gösterileceği.

### 9.3. Özet kutusu için güncellenmiş aday

Aşağıdaki kutu, yalnızca bağımsız denetim gerçekten yapılmışsa kullanılabilecek tasarım adayıdır:

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Durum: MATEMATİKSEL SERTİFİKA DOĞRULANDI  
> Doğrulanan işlem: Uluslararası foot tanımıyla (1 ft = tam 0,3048 m) verilen değerin metreye çevrilmesi. Denetleyici bu eşitliği kabul etti; 2438,4 m yuvarlanmış değildir.  
> Problem incelemesi: Tam hakemlik koşulları tamamlanmadı.  
> Sınır: Bu kanıt, 8000 ft değerinin kaynaktan doğru alındığını, asıl sorunun doğru yorumlandığını veya gerçek bir yüksekliğin doğru ölçüldüğünü göstermez.

Burada önceki metne göre küçük ama önemli değişiklik vardır: Etiketin hemen altında “doğrulanan işlem” açıkça yazılıyor. Yalnızca “sertifika var” denmiyor.

Gerçekte onay veya yorum incelemesi eksikse durum buna göre gösterilmelidir. Kaynak hatası biliniyorsa genel kapsam cümlesi yerine somut hata yazılır. Mevcut Faz 1’in aynı CAS kontrolü için bu bağımsız sertifika kutusu kullanılamaz.

## X. Önceki araştırmaya göre gerçek ilerleme

### 10.1. Yeni olarak ne öğrendik?

- Kanıt kontrolü ile IR→önerme dönüşümünün doğruluğu ayrı güven yükümlülükleri.
- Aynı problem sürümüne bağlanmamış onay ve sertifika, birlikte yanlış güven üretebilir.
- Güncel MCP’de sır toplama kanalı ve URL `accept` semantiği önceki tasarımın açıklığa kavuşturması gereken somut protokol kuralları.
- JSON şeması tek başına tekrarlı anahtar, büyük sayı ve dil-arası kanonikleştirme problemini çözmez.
- Harness’in gerçek alt ajan API’si; bağlam mirası, dosya ortamı ve mesajlaşma nedeniyle ek izolasyon gerektiriyor.
- Çıktı şeması, görünen raporun sonradan değişmediği anlamına gelmiyor.
- Heyetin başarısı yanlış etiket kadar kapsama ve yanlış oybirliği üzerinden de ölçülmeli.

### 10.2. Önceki araştırmada ne yanlıştı veya eksikti?

- `CERTIFIED` kabul koşulu, onaylı IR ile kontrol edilen iddia arasındaki bağlantıyı yeterince tanımlamıyordu.
- “Güvenilen onay olayı” ifadesi hangi onayın neyi tamamladığını yeterince ayırmıyordu.
- Etiket adının değiştirilmesinin UX sorununu çözdüğünü varsaymaya elverişli dil vardı.
- Dar F1.5 önerisinin kesin destek sınırı yeterince çizilmemişti.
- Harness’in entegrasyon maliyeti belirtilmişti; fakat gerçek bağlam ve eklenti davranışı incelenmemişti.
- Sıfır yanlış `PROVEN` ölçütü, yararsız aşırı ret davranışını ayırt etmiyordu.

### 10.3. Hangi anlaşmazlıklar artık çözüldü?

- “Formal denklik varsa anlamsal ortak hata biter” görüşü geçerli değil.
- “Alt ajan ayrıysa bağımsızdır” görüşü geçerli değil.
- “API erişimi için `accept` yeterlidir” görüşü geçerli değil.
- “Kanonik hash varsa doğru iddia kontrol edilmiştir” görüşü geçerli değil.
- “Etiketleri tek bir güven sırasına dizmek gerekir” bilimsel zorunluluk değil.

Buna karşılık ücretli erişimin tanımı ve `KANITLANDI` kelimesinin ürün içindeki kapsamı hâlâ sahip kararıdır.

### 10.4. Karar matrisi

| Konu | Deep Research III | Deep Research IV | Kanıt/karar türü |
|---|---|---|---|
| Etiketler | Dört kategorili hibrit | Korunuyor; onaylanmış sayılmıyor | Tasarım tercihi / sahip onayı |
| Sertifika kabulü | İddia ve denetleyici kaydı | Buna çeviri/semantik koruma bağı ekleniyor | Formal yöntem dayanağı  [inria.hal](https://inria.hal.science/inria-00360768v1/document) |
| Onay | Güvenilen kanal olayı | Tür + problem revizyonu + kanal güveni | Protokol ve güvenlik dayanağı  [modelcontextprotocol](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation) |
| Hash | Semantik manifest | Sıkı parser ve dil-arası kanonik biçim | Resmî teknik belge  [rfc-editor](https://www.rfc-editor.org/rfc/rfc8785.html) |
| Alan semantiği | Genel önkoşul kontrolü | Niceleme ve alan-koruma testleri | Araç belgesi + matematiksel karşı örnek  [docs.sympy](https://docs.sympy.org/latest/guides/assumptions.html) |
| Heyet | Kör üretim, denklik | İlk adaylar ve bütün tekrarlar korunuyor | Ampirik destek + tasarım çıkarımı  [arxiv](https://arxiv.org/html/2610.35930v1) |
| Başarı ölçümü | Yanlış etiket ve altın testler | Risk, kapsama, yanlış oybirliği | Hakemli yöntem dayanağı  [proceedings.neurips](https://proceedings.neurips.cc/paper_files/paper/2017/file/4a8423d5e91fda00bb7e46540e2b0cf1-Paper.pdf) |
| Harness | Opsiyonel istemci | Gerçek izolasyon profili olmadan hakem sayılmaz | Sabitlenmiş birincil belgeler  [github](https://github.com/deepseek-ai/deepseek-harness/blob/fcc0ad462172522aaf5c93a7b2e01f6b9f0b0159/docs/subsystems/subagent.md) |
| Faz 1 | Dar denetleyici önerisi | Desteklenen alt dil ve parser/alan sınırları öncelikli | Mühendislik tercihi |
| Nihai rapor | Kanıttan deterministik üretim | Haricî yeniden anlatım kanonik rapordan ayrılıyor | Kaynak incelemesi ve güvenlik çıkarımı |

### Nihai karar

Rigor’un geliştirilmesine başlanmasını en çok kolaylaştıran adım, etiket tartışmasını bir kez daha genişletmek değil; küçük ve denetlenebilir bir güven sözleşmesini kilitlemektir:

- Değişmez problem sürümü.
- Açık sayı/birim/alan semantiği.
- Doğru iddiaya bağlı kanıt kabulü.
- Türü ve kapsamı belli onay.
- Kayıtlardan deterministik etiket.
- Aynı kayıttan üretilen kanonik rapor.
- Kör formülasyon ile sonradan tartışmanın ayrılması.
- Haricî ajan ve Harness’in güven otoritesi olmaması.

Bu teknik sözleşmeler, `CERTIFIED` adının nihai seçimi ve ücretli heyetin ayrıntıları beklenirken de hazırlanabilir. Fakat yeni etiketler veya üst heyet eşikleri, sahibin açık onayı olmadan mevcut sözleşmenin yerine geçirilmemelidir.

Bu aşamada “nihai mimari doğrulandı” demek doğru olmaz. Daha dar ve savunulabilir sonuç şudur: Yanlış güven üretebilecek birkaç önemli bağlantı hatası artık açık sözleşme ve negatif testlere dönüştürüldü; kalan ürün tercihleri ve uygulama kanıtları da belirgin biçimde ayrıldı.