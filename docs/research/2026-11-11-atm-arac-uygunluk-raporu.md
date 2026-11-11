# AI-Toolchain-Manager araçlarının Rigor'a uygunluğu

Tarih: 2026-11-11. İncelenen kaynak: AI-Toolchain-Manager'ın `development` dalındaki altı katalog dosyası, toplam **23 kayıt**. Bu rapor bir seçim önerisidir; kurulum, etkinleştirme veya mimari karar değişikliği değildir.

**Önerim:** Gitleaks'i mevcut geliştirme zincirinde tut; EGM ve Superpowers'ı kullanıcının isteğe bağlı çalışma araçları olarak kullan; kod gezintisinde codebase-memory'yi sürdür. Kod oluştuktan sonra Cloudflare security-audit-skill'i sınırlı güvenlik incelemeleri için değerlendir. MarkItDown'ı F9'a, Exa'yı çekirdek dışı araştırma ihtiyacına bırak. Katalogdan v1 matematik çekirdeğine yeni çalışma anı bağımlılığı eklemeyi önermiyorum.

## Değerlendirme dayanağı

Rigor henüz tasarım aşamasında. Güncel sözleşme, README'nin eski akış anlatımından önce gelen [2026-11-11 mimarisi](../design/2026-11-11-rigor-mimari.md) ve [faz planı](../plans/2026-11-11-rigor-faz-plani.md). Özellikle:

- v1 çalışma anında ağ ve model çağrısı yok; doğal dil F6, belge okuma F9, Lean F12.
- Sertifikayı çözücüden bağımsız, küçük bir denetleyici kabul edecek. Bir ajanın incelemesi matematiksel sertifika yerine geçmez.
- Proje ayarı eklenti, kanca veya MCP sunucusunu otomatik açmayacak. İsteğe bağlı geliştirici araçları kullanıcı tercihi olarak kalacak.
- Aynı işi yapan araçları yığmak yerine ölçülebilir katkısı olan biri seçilecek.
- v1 hedefi macOS ve Linux. ATM kayıtlarındaki macOS/Windows ve ajan uyumluluk satırları Linux veya bütün MCP istemcileri için kanıt sayılmaz.

Mimari §5 zaten Gitleaks, Superpowers, EGM, codebase-memory, Graphify ve Betterleaks hakkında seçim içeriyor. Aşağıdaki öneriler bu kararları dikkate alıyor; aynı araçları yeni keşifmiş gibi sunmuyor.

**Kanıt sınırı:** ATM bir test edilmiş araç listesi değil. Kayıtlar yayıncı beyanına dayanıyor; Claude-Mem ve Ruflo ayrıca karantinada. Altı katalog dosyasının tamamını okudum. Güçlü adaylarda yayıncının README'sini de kontrol ettim: Gitleaks, EGM, Superpowers, codebase-memory, Cloudflare security-audit-skill, MarkItDown ve Ponytail. Diğer araçlara ilişkin teknik özetler ATM'nin sabitlenmiş kaynak kayıtlarına dayanıyor. Bu incelemede araçları kurmadım, benchmark veya bağımsız ağ/gizlilik testi yapmadım.

## Öncelikli seçimler

### 1. Gitleaks — şimdi kullan; geliştirme aracı

**Neden uygun?** Rigor'un açık deposuna yanlışlıkla anahtar, özel yapılandırma veya test verisine gömülü sır eklenmesini yakalamaya yardımcı olur. Matematiksel doğruluk sağlamaz; yayın sürecindeki farklı bir riski azaltır. Yerel Git geçmişi ve dosya taraması Rigor'un ağsız geliştirme yaklaşımına uyar.

**Kullanım:** Mevcut mimarideki gibi commit/push öncesi elle, sırları tamamen maskeleyen `--redact` ile. Matematik paketinin çalışma anına eklenmez; otomatik kanca zorunlu değildir. Sentetik bir sırın yakalanması ve çıktıda maskelenmesi ilk kabul kontrolü olabilir.

**Maliyet ve sınır:** Düşük entegrasyon maliyeti; yanlış pozitiflerin yönetimi gerekir. Yayıncı yeni özellik geliştirmesini durdurduğunu, güvenlik yamalarını sürdüreceğini belirtiyor. Bu, mevcut ihtiyacı karşılayan aracı hemen değiştirme gerekçesi değil. Betterleaks'e geçiş ancak Rigor örneklerinde ölçülmüş faydayla yapılmalı. [Yayıncı belgesi](https://github.com/gitleaks/gitleaks/blob/master/README.md)

### 2. EGM / Elephant-Goldfish Model — kritik tasarım geçişlerinde kullan

**Neden uygun?** Rigor'un en pahalı hataları, yanlış etiket kapsamı, çözücü ile denetleyicinin ortak varsayımı veya onaylanan IR'ın sonradan değişmesi gibi tasarım hataları olabilir. Önceki konuşmayı görmeyen incelemeciler belgeyi ve referansları sorgulayarak bu tür boşlukların bulunmasına yardımcı olur.

**Kullanım:** Mevcut K-1…K-4 kapılarındaki inceleme rolü korunur. Örneğin K-1'de sertifika kapsamı ve bağımsız denetleyici; K-3'te izin, veri çıkışı ve maliyet; K-4'te yeterlik ve `PROVEN` koşulları incelenir. Faz planındaki ajan sayısı/model sınırı ayrıca geçerlidir.

**Maliyet ve sınır:** Model çağrısı ve inceleme süresi gerektirir. Taze bağlam, farklı model ailesi veya matematiksel bağımsızlık demek değildir. EGM değerlendirmesi `CERTIFIED` üretmez ve F8'deki yeterlikli heyetin yerine geçmez. İnceleme belgeleri ev sahibi ajanın sağlayıcısında işlenir; bu geliştirici faaliyeti v1 motorunun ağ politikasından ayrı tutulur. [Yayıncı belgesi](https://github.com/google/elephant-goldfish-model/blob/main/README.md)

### 3. Superpowers — isteğe bağlı geliştirme yöntemi olarak kullan

**Neden uygun?** Tasarımdan küçük uygulama adımlarına geçiş, hata ayıklama ve tamamlamadan önce doğrulama Rigor'a yarar sağlar. Özellikle yanlış sertifika, sıfıra bölme, negatif bölenli `mod` ve onay sonrası IR değişimi gibi örnekleri başarısız testten başlayarak ele almak için uygundur.

**Kullanım:** Kullanıcı düzeyinde planlama, uygulama ve hata ayıklama yardımcısı. Projenin mimarisini, kabul ölçütlerini ve faz sırasını esas almalı. Superpowers'ın süreç incelemeleri ile EGM'nin kapı incelemeleri aynı işi tekrar ettirmemeli.

**Maliyet ve sınır:** Süreç yükü orta; her küçük değişikliğe tam plan/inceleme akışı uygulamak gereksiz olabilir. Yayıncı otomatik beceri tetikleme ve zorunlu iş akışları tarif ediyor; bunların Rigor'un yerel kurallarıyla uyumu seçilen sürümde kontrol edilmeli. Ürünün doğruluk garantisi bu eklentiye bağlanmamalı. [Yayıncı belgesi](https://github.com/obra/superpowers/blob/main/README.md)

### 4. codebase-memory-mcp — mevcut kod gezintisinde kullan; kod büyüdükçe faydası artar

**Neden uygun?** İleride `kernel`, etiket kararı, derleyiciler ve MCP iş modeli arasındaki ilişkileri bulmak; değişikliğin hangi çağrıları etkileyebileceğini incelemek için uygun. Bu oturumda Rigor indekslendi ve belge bölümleri bulundu; ilgili üç belge için kayıtlı kapsam sorunu bildirilmedi. Bu gözlem genel işlev veya ağsızlık sertifikası değildir.

**Kullanım:** Kullanıcının mevcut talimatına uygun olarak yapısal keşifte kullanılır; ilgili dosyaların kapsam/tazelik kontrolü ve gerektiğinde doğrudan kaynak okumasıyla birlikte. Bugün üretim kodu bulunmadığından kod çağrı grafiğinin değeri sınırlı.

**Maliyet ve sınır:** Mevcut ortamda kullanım maliyeti düşük; sürüm, indeks ve kanca yönetimi ek bakım getirir. Grafik, dinamik Python çağrılarının veya bütün ilişkilerin eksiksiz kanıtı değildir. Çekirdeğin katman kuralları `import-linter` ve testlerle zorlanmalı; yalnızca grafiğe bakarak denetleyicinin bağımsız olduğu sonucuna varılmamalı. Projenin çalışması ve CI bu araca bağlı olmamalı. [Yayıncı belgesi](https://github.com/DeusData/codebase-memory-mcp/blob/main/README.md)

## Koşullu ve sonraki faz adayları

### Cloudflare security-audit-skill — kod oluştuktan sonra sınırlı güvenlik incelemesi

Cloudflare üzerinde çalışmayı gerektiren bir araç değil; kaynak kodda güven sınırlarını inceleyen ajan iş akışı. Rigor'da katı ayrıştırıcı, dev üs/derin ağaç kaynak tüketimi, dosya okuyucular, rapor yolları ve MCP onay alanları uygun inceleme konuları. K-1/K-2 öncesi odaklı inceleme için **yeni bir öneri**; mevcut fazlara zorunlu kapı eklemiyorum.

Maliyeti orta-yüksek: çoklu ajan incelemesi ve bulguların bağımsız doğrulanması gerekir. Hedef kod çalıştırılacaksa yayıncı işletim sistemiyle zorlanan ağsız sandbox, temiz ortam ve kaynak sınırları istiyor. Rigor'un kaynak sınırı mekanizması tek başına bu inceleme sandbox'ını sağlıyor sayılmaz. Kabul kontrolü: bilinen örnek kusuru bulması, düzeltilmiş sürümde aynı iddiayı geri çekmesi ve yeniden üretilebilir kaynak/test kanıtı sunması. Güvenlik bulgusu ile matematik sertifikası ayrı kalır. [Yayıncı belgesi](https://github.com/cloudflare/security-audit-skill/blob/main/README.md)

### MarkItDown — F9'da belge alımı için aday

Şartname ve makaleleri PDF/DOCX'ten araştırılabilir metne çevirmek yararlı olabilir. Ancak matematiksel anlamı, sayfa/denklem konumunu veya tabloların kesin doğruluğunu garanti etmez. Markdown'a dönüşen bir formülün doğru aktarılması ayrıca doğrulanmalıdır.

F9 kabul deneyi: kuaterniyon formülleri, alt/üst indisler, eksi işaretleri, birimler ve tablo dipnotları bulunan gerçek belgelerde kayıp/bozulma kontrolü; her çıkarımın özgün dosya özeti ve konumuyla eşlenmesi. Çıktı güvenilmeyen belge girdisi olarak ele alınmalı. XLSX/CSV sayısal verilerini Markdown üzerinden dolaştırmak yerine türleri ve hücre kökenini koruyan doğrudan okuyucular tercih edilmeli.

Yerel dönüştürme yolu, kapalı eklentiler ve kapalı bulut seçenekleriyle denenmeli. Yayıncı README'si Python 3.10–3.14 aralığını belirtiyor; Rigor'un 3.15 hedefiyle aynı ortama kurulum uyumu varsayılmamalı. Ayrı araç ortamı olası bir başlangıçtır. Entegrasyon maliyeti, dönüşümden çok köken ve doğruluk kontrollerinde; orta-yüksek. [Yayıncı belgesi](https://github.com/microsoft/markitdown/blob/main/README.md)

### Exa MCP Server — yalnızca çekirdek dışı araştırmada, ihtiyaç varsa

Birincil kaynak, formül tanımı veya güncel sağlayıcı belgesi bulmak için yararlı olabilir. Sorgular ve adresler Exa'ya gider; dolayısıyla v1 çalışma anına uygun değil. Mevcut araştırma araçları aynı ihtiyacı karşılıyorsa yeni hizmet eklenmemeli. Kullanılırsa bulunan içerik doğrudan kanıt sayılmaz: özgün kaynağı, tarih/sürümü ve ilgili tanımı saklamak gerekir. Bağlantı maliyeti düşük-orta; veri çıkışı, kota ve olası ücretler ayrıca değerlendirilir. [ATM kaydı](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-c01.json)

## 23 kaydın tamamı için karar

Aşağıdaki “önerilmez” kararları araçların genel kalitesine değil, Rigor'un bugünkü kapsamına ilişkindir. İşlev testinden geçtikleri anlamına gelmez.

| Araç | Rigor için karar | Gerekçe / yeniden değerlendirme koşulu |
| --- | --- | --- |
| Gitleaks | Şimdi; geliştirme zinciri | Yerel sır taraması; mevcut mimaride seçili. |
| EGM | Şimdi; isteğe bağlı inceleme | K-1…K-4'te tasarım varsayımlarını sorgulama; mevcut planda var. |
| Superpowers | Şimdi; isteğe bağlı yöntem | Planlama, test ve hata ayıklama; proje ayarından zorunlu açılmaz. |
| codebase-memory-mcp | Mevcut kullanım sürsün | Kaynak destekli yapısal keşif; CI veya matematiksel doğruluk dayanağı değil. |
| Cloudflare security-audit-skill | Kod sonrası pilot | Ayrıştırıcı, dosya, kaynak tüketimi ve MCP güven sınırlarına uygun. |
| MarkItDown | F9 adayı | Belge alımı yararlı; matematik aktarımı, köken ve Python 3.15 uyumu çözülmeli. |
| Exa MCP Server | Araştırmada isteğe bağlı | Kaynak keşfi; ağ kullandığından v1 motoruna eklenmez. |
| Microsoft Playwright Test / Library | Web arayüzü olursa | Tekrarlanabilir arayüz regresyonu için uygun; bugünkü SDK/CLI/MCP ve OS diyaloglarını tek başına test etmez. |
| Microsoft Playwright CLI | Web arayüzü olursa alternatif | Ajanın keşif amaçlı tarayıcı kullanımı; CLI+Skills yolu MCP'ye alternatif olabilir. |
| Microsoft Playwright MCP | Şimdilik ertele | Durumlu tarayıcı keşfi gerektiğinde; Rigor'un MCP sunucusuna protokol test aracı değildir. |
| agent-browser | Şimdilik ertele | Bugün tarayıcı tabanlı ürün yok; gelecekte Playwright seçenekleriyle karşılaştırılıp biri seçilir. |
| Anthropic Frontend Design | Arayüz tasarlanırsa | Onay ekranı/rapor arayüzünün anlaşılabilirliğine katkı sağlayabilir; çekirdek ihtiyacı değil. |
| Ponytail | Şimdilik ekleme | Küçük ve gerekli kod üretme hedefi yararlı; Superpowers ve mevcut kurallarla örtüşüyor. Ancak bakım yükünü düşürdüğü örneklerle gösterilirse ayrı pilot. |
| Karpathy-inspired guidelines | Ayrı eklenti ekleme | Basitlik ve dar değişiklik ilkeleri zaten süreçte karşılanıyor; ATM kaydı lisans belgesi ve kaynak kimliği netliği sorunu bildiriyor. |
| agentic-awesome-skills | Kaynak kataloğu olarak bakılabilir | Somut ihtiyaç için tek beceri seçilip incelenebilir; toplu kurulum Rigor'a ölçülmüş katkı sağlamaz. |
| Betterleaks | Gitleaks'e alternatif; birlikte ekleme | Aynı temel sır tarama işi. Geçiş ancak gerçek örneklerde iyileşme ve ağ özelliklerinin incelenmesiyle. |
| Graphify | Şimdi önerilmez | Mevcut grafik aracıyla örtüşme, belge anlam çıkarımında veri çıkışı ve ayrı ortam ihtiyacı. Mimari de önermiyor. |
| Understand Anything | Şimdi önerilmez | İkinci grafik/panel, bütün proje analizi, model maliyeti ve kancalar; mevcut keşfe ek katkı gösterilmedi. |
| Claude-Mem | Kapalı kalsın | Oturum gözlemlerini saklama/sıkıştırma, ek sağlayıcı ve saklama yüzeyi; ATM'de karantinada. Rigor'un sürümlü olay kaydının yerine geçmez. |
| Ruflo | Kapalı kalsın | Orkestrasyon, kanca ve daemon yükü; paket kimliği belirsizliğiyle ATM'de karantinada. F8'deki bağımsızlık/yeterlik koşullarını tek başına sağlamaz. |
| Caveman | Rigor akışına ekleme | Kısa üslup profili ayrı değerlendirilebilir; kapsam, varsayım ve ret gerekçesi kaybına izin verilemez. Proxy/sıkıştırma, gelecekte formülasyon kökeni ve bağımsızlık ölçümünü zorlaştırır. |
| Apify MCP Server | Şimdi önerilmez | Uzak Actor çalıştırma ve değişken maliyet; deterministik yerel matematik doğrulamasında somut ihtiyaç yok. |
| Strix | Şimdi önerilmez | Aktif hedef testi bugünkü yerel kütüphane/MCP ürününe uygun öncelik değil. Önce kaynak temelli güvenlik incelemesi. |

Tarayıcı araçları için önemli ayrım: Playwright Test/Library test kodu yazmak içindir; CLI ve MCP ajanın tarayıcıyı kullanma yollarıdır. Üçünü birden kurmak gerekmez. Aynı şekilde bir aracın MCP sunucusu olması, Rigor MCP'sinin şema, tekrar anahtarı, revizyon ve onay sözleşmesini sınadığı anlamına gelmez.

## Uygulama sırası ve başarı ölçütü

1. **F0–F1:** Mevcut Python kalite araçlarını ve negatif sertifika testlerini kur. Gitleaks'i mevcut kurala göre kullan; Superpowers ve codebase-memory isteğe bağlı yardımcı kalsın. Bu araçların hiçbiri pytest, Hypothesis, mypy veya import-linter'ın yerine geçmez.
2. **K-1:** EGM ile sertifika kapsamı, etiket kararı ve bağımsız denetleyici tasarımını incele. Kod hazırsa güvenlik skill'ine sınırlı bir pilot düşün; bütün depoyu kapsayan sürekli ajan çalışması başlatma.
3. **F2–F5:** MCP sözleşmesini istemci/protokol testleriyle doğrula. Rigor'un web UI'ı olmadığı sürece tarayıcı araçlarına yatırım yapma.
4. **F6–F9:** Araştırmada gerçekten eksik varsa Exa'yı, belge alımı için MarkItDown'ı ayrı pilotlarla değerlendir. Rigor'un model bağımsızlığı ve veri çıkışı kuralları korunmalı.

Bir pilotun kabulü “araç çalıştı” ile sınırlı olmamalı: Rigor'dan seçilmiş görevlerde yakaladığı hata, harcadığı zaman/model maliyeti, yanlış bulgu, yazdığı dosyalar ve ağ davranışı kaydedilmeli. Katkısı gösterilmeyen veya aynı işi tekrarlayan araç kalıcı zincire alınmamalı.

## Kaynaklar ve inceleme kapsamı

ATM `development` dalı 2026-11-11'de çevrimiçi okundu. Bağlantılar hareketli dalları gösterir; katalog içindeki `sourceSnapshot` alanları yayıncının tarihsel commit/sürüm gözlemlerini taşır. Tarihsel katalog kaydı ile yayıncının bugün okunan README'si aynı sürüm testi değildir.

- [catalog-seed.json — 9 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-seed.json)
- [catalog-candidates-1b.json — 4 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-1b.json)
- [catalog-candidates-c01.json — 3 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-c01.json)
- [catalog-candidates-c02.json — 2 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-c02.json)
- [catalog-candidates-c03.json — 4 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-c03.json)
- [catalog-candidates-c04.json — 1 kayıt](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/data/catalog-candidates-c04.json)
- [ATM README — uygulamanın ve kanıtların sınırları](https://github.com/ErenTahiroglu/AI-Toolchain-Manager/blob/development/README.md)
- [Ponytail yayıncı belgesi](https://github.com/DietrichGebert/ponytail/blob/main/README.md)

Rigor tarafında README, güncel mimari ve faz planı doğrudan okundu; codebase-memory ile belge bölümleri arandı ve üç dosyanın kapsam/tazelik sinyali kontrol edildi. Belgeler tasarım niyetini gösteriyor; henüz uygulanmış ürün davranışı olarak değerlendirilmedi.
