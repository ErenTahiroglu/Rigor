## Bölüm I — Yönetici özeti

Önerim: Rigor, matematiksel kanıtın durumunu problem yorumunun, girdi kaynağının ve fiziksel gerçekliğin doğrulanmasından ayırmalıdır. Kullanıcının API anahtarının veya ikinci bir LLM ailesine erişiminin bulunmaması, bağımsız doğrulayıcı tarafından kabul edilmiş matematiksel kanıtı zayıflatmaz. Buna karşılık, doğal dildeki sorunun doğru matematiksel ifadeye çevrildiğine ilişkin eldeki kanıtı sınırlayabilir. Formal kanıtın geçerliliği ile kanıtlanan ifadenin amaçlanan anlamı arasındaki ayrım, Lean’in resmî doğrulama rehberinde de açıkça yapılır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

Ana örnek için önerdiğim kullanıcı metni şudur:

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Matematiksel durum: KANITLANDI — belirtilen birim tanımına göre  
> Uluslararası foot tanımıyla (1 ft = tam 0,3048 m), bu eşitliğin matematiksel sertifikası çözücüden bağımsız bir doğrulayıcı tarafından kontrol edildi; sonuç yuvarlanmış değildir.  
> Kapsam: Bu kanıt, verilen 8000 ft değerinin metre karşılığını doğrular; değerin kaynaktan doğru alındığını, sorunun doğru yorumlandığını veya gerçek bir yüksekliği doğru temsil ettiğini doğrulamaz.

Buradaki dönüşüm katsayısı uluslararası foot için tanım gereği kesindir; tarihsel US survey foot ise farklı bir rasyonel katsayıya sahiptir. Dolayısıyla kesinlik, hangi birim tanımının kullanıldığına bağlıdır. [nist](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf)

### Mimari karar

B yaklaşımını veri modeli, C yaklaşımını kullanıcı arayüzü olarak öneriyorum:

- İçeride ayrı güven boyutları tutulmalı.
- Kullanıcıya kapsamı belirtilmiş matematiksel etiket gösterilmeli.
- Doğal dil yorumu, kullanıcı onayı, kaynak kökeni ve fiziksel geçerlilik ayrı satırlarda açıklanmalı.
- `PROVEN`, genel bir “her şey doğru” seviyesi değil, kimliği belirli matematiksel iddianın kanıt durumu olmalı.
- `CROSS_VALIDATED`, gerçekten bağımsız yöntem karşılaştırması yapılmış sonuçlar için kullanılmalı; “sertifika var ama LLM yok” anlamına gelmemeli.
- `REFUSED`, doğrulanmamış bir sayının güvenilir cevap olarak yayımlanmasını engellemeli.

Bu, literatürün zorunlu kıldığı tek arayüz değildir; formal doğrulamadaki kapsam ayrımından ve güven iletişimi araştırmalarından türettiğim mimari öneridir. HCI literatürü, açıklama eklemenin tek başına aşırı güveni gidermediğini; bazı durumlarda kullanıcıların aktif değerlendirmeye yönlendirilmesi gerektiğini gösterir. Bu nedenle önerilen Türkçe metnin kullanıcılarla ayrıca sınanması gerekir. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### En önemli iki risk

1. Yanlış `PROVEN`: Sertifika başka bir ifadeye aitken, kontrol edilmemişken veya yanlış yorumlanan sorunun cevabıymış gibi sunulurken “KANITLANDI” yazılması.
2. Kanıtın yanlış küçümsenmesi: Bağımsız kontrol edilmiş kesin matematiksel eşitliğin, yalnızca LLM konsensüsü yok diye “yaklaşık”, “şüpheli” veya salt deneysel destek düzeyinde gösterilmesi.

Birinci risk en kritik güvenlik hatasıdır. İkinci risk de güven kalibrasyonu hatasıdır: kullanıcıya kanıtın gerçekte sağladığından daha az güven gösterir.

## Bölüm II — Rigor’un mevcut durumu

### 2.1. Doğrulanan depo durumu ve inceleme sınırı

GitHub bağlantısı üzerinden 10 Kasım 2026 tarihinde şu dal uçlarını doğruladım:

| Dal | İncelenen commit SHA | Durum |
|---|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` | İlk tasarım belgeleri, README, lisans ve araştırma kanıt betiği |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` | K24–K26 genişletmeleri, mimari yol haritası ve Faz 1 TDD planı |

GitHub sorguları issue veya pull request döndürmedi. `development` geçmişinde `main` sonrasındaki değişiklikler şunlardı:

- `52816e6…`: alandan bağımsızlık, kapsam matrisi, desteklenmeyen matematik için ret.
- `fea88dd…`: alan uyarlaması ve Lean 4 + Mathlib’in v1’e alınması.
- `c6bea6f…`: plan öncesi doğrulama düzeltmeleri.
- `ca68915…`: F1–F9 yol haritası ve Faz 1 planı.

Önemli yöntemsel sınırlama: GitHub aracı uzun tasarım dosyasının içeriğini keserek döndürdü. README, Handoff, güncel araştırma notları ve yol haritası okunabildi; tasarımın §4.1–§4.5 bölümleri doğrudan görüldü. Ancak §6.4–§6.8’in tamamını kesintisiz okuyamadım. Kod aramasıyla bazı parçaları ve özet kutusu sözleşmesini doğruladım. Bu nedenle aşağıda bu bölümler için verdiğim metinler, mevcut paragrafların eksiksiz satır denetimi değil, doğrulanabilen mimariyle uyumlu değişiklik önerileridir.

GitHub bağlantısı sonuçları bu oturumda kaynak numarası üretmediğinden depo bulgularına uydurma atıf numarası vermiyorum. Dosya yolları ve commit SHA’ları incelemenin denetlenebilir kimlikleridir.

### 2.2. Proje uygulanmış bir ürün değil

`main` README’si açıkça tasarım aşamasını ve henüz ürün kodu bulunmadığını söylüyor. Güncel yol haritası da `src/rigor/…` yapısını ve F1–F9 çıkış ölçütlerini planlıyor.

Dolayısıyla:

- SymPy/Pint/FLINT ile yapılmış yerel deneyler, çalışan Rigor ürününün kabul testi değildir.
- Araştırma kanıt betiği, SDK/MCP güvence zincirinin uygulanmış olduğunu göstermez.
- Planlanan `Conditions`, `Outcome`, `Provenance`, sertifika ve rapor bileşenleri mevcut ürün kabiliyeti olarak sunulmamalıdır.

### 2.3. Sahip kararı, tasarımcı kararı ve onay durumu

Handoff Bölüm 1, önceki konuşmanın bağlayıcı sahip kararlarını ayırıyor. Özellikle hibrit problem uzayı, gecikmeden önce kesinlik, SDK + MCP ve eksik parametrede fail-closed korunması gereken hedeflerdir.

Tasarım belgelerinde ise durum değişmiştir:

- `main`: “TASLAK — sahibin onayını bekliyor.”
- `development`: “ONAYLANDI — K24–K26 ile genişletildi.”
- Buna rağmen dosya içindeki okuma kuralı, “Tasarımcı kararı” maddelerinin ayrıca kontrol edilmesi gerektiğini söylemeye devam ediyor.

Burada belge yönetişimi belirsizliği vardır. Dosya başlığındaki genel onayın bütün tasarımcı kararlarını tek tek onayladığını varsaymak doğru olmaz. Güven politikasını değiştirmek için açık bir karar kaydı öneriyorum.

### 2.4. Mevcut etiket politikasının güçlü yanları

Mevcut tasarım şu güvenlik hedeflerini doğru yönde kuruyor:

- Hesap hatası ile formülasyon hatasını ayırıyor.
- Kullanıcıya söylenmemiş varsayımları yasaklıyor.
- Ajanın kendi onayını kullanıcı onayı gibi göstermesini engellemeyi amaçlıyor.
- Fiziksel modelin gerçekliğini matematiksel doğrulamanın dışında tutuyor.
- Tek bir sonucun arkasındaki koşulları raporda görünür kılıyor.
- Yanlış `KANITLANDI` üretimini en kötü başarısızlık kabul ediyor.
- Çekirdeğin LLM katmanına bağımlı olmamasını planlıyor.
- Deterministik Türkçe/İngilizce anlatım iskeletini Faz 1’e yerleştiriyor.

Son iki madde, API anahtarsız çalışma için özellikle değerlidir.

### 2.5. Düzeltilmesi gereken sınıflandırmalar

| Mevcut karar | Sorun | Önerilen düzeltme |
|---|---|---|
| `PROVEN` için ≥2 model ailesi | Matematiksel kanıt ile yorum desteğini birleştiriyor | Model ailesi koşulu yalnızca yorum boyutuna taşınmalı |
| Tek IR en fazla `CROSS_VALIDATED` | Doğrudan formal tanımı gereksiz biçimde LLM’ye bağımlı kılıyor | Formal iddia bağımsız kontrolle `PROVEN` alabilmeli |
| Sertifikanın “var” olması | Kontrol edilebilirlik ile gerçekten kontrol edilmişlik ayrılmıyor | Kabul edilmiş doğrulama olayı şart olmalı |
| Sertifikalı tek aile sonucu `CROSS_VALIDATED` | Gerçek çapraz yöntem bulunmadığında etiket yanlış şey söylüyor | Sertifika ve yorum durumu ayrı yazılmalı |
| Dosya hash’i ve konumuyla “okumanın doğruluğu” | Hash, yanlış hücrenin seçilmesini veya anlamsal çıkarım hatasını dışlamaz | Bütünlük, konum ve çıkarım sadakati ayrılmalı |
| Kütüphane modelinin “güvenilir varlık” olması | Örnek testleri evrensel doğruluk veya fiziksel uygunluk kanıtı değildir | Doğrulanan özellikler ve kullanım koşulları belirtilmeli |

Özellikle README’de geçen `unsat çekirdeği`, tek başına bir `unsat` ispat sertifikası değildir. Bir çekirdek, çelişkili olduğu iddia edilen alt kümeyi gösterir; alt kümenin çelişkili olduğunun ayrıca kanıtlanması veya güvenilen mekanizmayla doğrulanması gerekir. Sertifika denetleme literatürü, kanıt nesnesinin asıl formüle karşı kontrolünü esas alır. [link.springer](https://link.springer.com/article/10.1007/s10817-019-09525-z)

## Bölüm III — Bilimsel temeller

### 3.1. Matematiksel sertifika neyi garanti eder?

Bir sertifika doğrulama sözleşmesi en az şu bileşenleri içerir:

\[
\operatorname{Check}(A,P,C)=\operatorname{ACCEPT}
\]

Burada:

- \(A\): varsayımlar, tanımlar ve mantıksal bağlam.
- \(P\): kanıtlanacak tam matematiksel önerme.
- \(C\): sertifika veya kanıt nesnesi.

Garanti, doğrulayıcının sağlamlığı ve açık güven varsayımları altında \(A\vdash P\) olmasıdır. Çözücünün “doğru” demesiyle, doğrulayıcının belirli bir kanıtı belirli bir önermeye karşı kabul etmesi aynı kanıt türü değildir. Proof-carrying code ve doğrulanmış SAT sertifika denetleyicileri bu ayrımı somutlaştırır. [link.springer](https://link.springer.com/article/10.1007/s10817-019-09525-z)

Rigor örneğinde doğrulanacak ifade:

\[
8000 \times \frac{381}{1250}=\frac{12192}{5}
\]

ve gösterim eşitliği:

\[
\frac{12192}{5}=\frac{24384}{10}=2438{,}4.
\]

Birim katmanı ise `ft` sembolünün bu işlemde uluslararası foot anlamına geldiğini bağlamalıdır. Katsayının bu tanıma karşılığı NIST tarafından tam olarak verilir. [nist](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf)

Bu ispat şunları söylemez:

- Kaynak belgede gerçekten 8000 yazıyordu.
- Kaynak “en az” diyordu ve rapor bunu doğru taşıdı.
- İrtifa yerden mi, deniz seviyesinden mi ölçülüyor?
- Gerçek roket bu yüksekliğe çıktı.
- Sensör doğru çalıştı.

### 3.2. Trusted computing base: garanti hangi yazılıma dayanır?

Bağımsız kontrol, güveni ortadan kaldırmaz; daha küçük ve açık bir güven tabanına taşır. Bu taban örneğe göre şunları içerebilir:

- Doğrulayıcının mantığı ve uygulaması.
- Kanonik ifade/IR okuyucusu.
- Birim tanımlarının bağlanması.
- Aksiyom ve bağımlılık politikası.
- Raporun doğrulanmış iddiaya bağlanması.
- Çalışma ortamının ilgili doğruluk varsayımları.

Lean’in resmî rehberi, en güçlü kontrol yolunda dahi mantığın sağlamlığı, araç bağlantılarının doğruluğu, yalıtım ve bütün denetleyicileri aynı anda etkileyen hata bulunmaması gibi varsayımların kaldığını açıkça belirtir. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

“Çözücüden bağımsız doğrulayıcı” için yalnızca ayrı bir fonksiyon adı yeterli değildir. Doğrulayıcı:

1. Sonucu çözücünün başarı bayrağından devralmamalı.
2. İddianın tam içeriğini yeniden okumalı.
3. Sertifikayı bu iddiaya karşı denetlemeli.
4. Hangi ortak bağımlılıkları kullandığını açıklamalıdır.

Farklı uygulamalarla ikinci denetim ek güven sağlayabilir; fakat aynı kütüphane veya yanlış birim kaydı ortak hata kaynağı olarak kalabilir. Lean’in bağımsız `nanoda` denetleyicisini de kullanan comparator yaklaşımı bu savunma derinliğine örnektir. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### 3.3. Sertifikanın varlığı, kontrolü ve güvenilir kontrolü

| Durum | Söylenebilecek ifade | Söylenemeyecek ifade |
|---|---|---|
| Çözücü sertifika üretti | “Sertifika üretildi.” | “Kanıtlandı.” |
| Sertifika biçimsel olarak okunabildi | “Sertifika okunabildi.” | “Matematiksel olarak geçerli.” |
| Denetleyici kabul etti | “Belirtilen denetleyici kabul etti.” | Denetleyici politikası bilinmiyorsa koşulsuz güven |
| Onaylı denetleyici, doğru iddiaya karşı kabul etti | “Belirtilen iddia kanıtlandı.” | Problem niyeti ve gerçek dünya da doğrulandı |
| Kullanıcı başka ortamda yeniden kontrol etti | “Bu ortamda yeniden doğrulandı.” | Bütün yazılım/donanım riskleri ortadan kalktı |

Lean rehberinin derleme, aksiyom denetimi, yeniden kontrol ve güvenilir challenge ifadesine karşı comparator kontrolünü ayrı katmanlar olarak ele alması bu ayrımı destekler. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### 3.4. Sertifika, kriptografik sertifika değildir

Matematiksel sertifika, bir önermenin neden geçerli olduğuna ilişkin kontrol edilebilir kanıttır.

Buna karşılık:

- Hash: belirli bayt dizisinin parmak izidir.
- Dijital imza: anahtar yönetimi ve doğrulama koşulları altında bütünlük ve imzalayan anahtara ilişkin güven sağlar.
- Kimlik sertifikası: anahtar–kimlik bağını destekler.
- Matematiksel ispat: belirtilen matematiksel özelliği destekler.

Proof-carrying code’un temel özelliği, kaynağın kimliğini bilmeden belirli özellikleri doğrulayabilmesidir; özgün çalışma bunu kriptografi veya dış otorite gerektirmeyen bir kontrol olarak tanımlar. Ancak bu, kanıt kapsamı dışında kalan bütün kötü niyetli davranışların dışlandığı anlamına gelmez. [dl.acm](https://dl.acm.org/doi/10.1145/263699.263712)

### 3.5. Altı güven sınırı

| Sınır | Garanti edilebilen | Yalnızca desteklenen | Doğrulanmayan |
|---|---|---|---|
| A — Matematik | Açık varsayımlar altında tam önerme | İkinci motorla ek hata yakalama | Kaynağın amacı |
| B — Formülasyon | Formal ifadeler arasındaki kanıtlanmış denklik | Bağımsız yorum, kaynak eşlemesi, insan incelemesi | Serbest doğal dil niyetinin koşulsuz doğruluğu |
| C — Girdi/tanım | Kullanılan değerler, birim kimlikleri, kayıtlı dosya sürümü | Kaynak otoritesi, çıkarım sadakati, doğrudan onay | Ölçümün gerçekliği |
| D — Gerçek dünya | Modelden çıkan matematiksel sonuç | Deneysel model geçerliliği çalışmaları | Gerçek uçuş başarısı |
| E — Sertifika | Doğru iddiaya bağlı kabul edilmiş kontrol | Ek bağımsız denetleyiciler | Denetleyicinin hatasızlığına koşulsuz garanti |
| F — Yazılım/kaynak | Ayrı mekanizmalarla doğrulanmış özellikler | Paket kökeni, imza, yeniden üretim | Salt matematiksel kanıttan uygulamanın iyi niyetli oluşu |

Bu tablodaki temel ayrımlar formal kanıt rehberindeki “ispatın geçerliliği–ifadenin anlamı” ayrımına, PCC’nin özellik–köken ayrımına ve GUM’un matematiksel model–ölçüm belirsizliği ayrımına dayanır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### 3.6. Kesin aritmetik ile doğrulanmış sayısal yaklaşım

| Yöntem | Doğrulanabilen iddia | Kullanıcıya uygun ifade |
|---|---|---|
| Kesin rasyonel aritmetik | \(x=p/q\) | “Sonuç tamdır; yuvarlanmış değildir.” |
| Sembolik ispat | Varsayımlar altında özdeşlik/teorem | “Bu ifade belirtilen varsayımlarla kanıtlandı.” |
| Doğrulanmış aralık/top hesabı | \(x\in[a,b]\) | “Gerçek matematiksel değer bu aralıktadır.” |
| Sertifikalı yuvarlama analizi | Belirli işlem ve hata sınırı | “Hesaplama hatası belirtilen sınırı aşmaz.” |
| İki sayısal yöntem + yakınsama | Deneysel sayısal uyuşma | “Yöntemler belirtilen toleransta uyuştu; kesin hata sınırı kanıtlanmadı.” |

FLINT/Arb top aritmetiği, uygun işlemler için tam matematiksel değeri kapsayan aralıklar üretir. Ancak bu, gösterilen orta noktanın tam değer olduğu anlamına gelmez. Ayrıca seri kesme veya ayrıklaştırma hatası, yalnızca aritmetik yuvarlama hesabıyla otomatik olarak kapsanmış olmaz; ilgili hata sınırı ayrıca eklenmelidir. [flintlib](https://flintlib.org/doc/guide/types/ball-arithmetic.html)

Sonuç: Aynı üst `PROVEN` ailesi kullanılabilir, fakat alt tür zorunlu olmalıdır:

- `PROVEN / EXACT_VALUE`: tam değer kanıtlandı.
- `PROVEN / ENCLOSURE`: aralıkta bulunma kanıtlandı.
- `PROVEN / PROPERTY`: eşitsizlik, özdeşlik veya başka özellik kanıtlandı.

İkinci türde “değer matematiksel olarak kesin” değil, “hata sınırı kanıtlı” veya “aralık kanıtlandı” yazılmalıdır.

Arb kullanmak tek başına Rigor’un bağımsız sertifika şartını karşılamaz. Ayrı denetleyici bulunmuyorsa güven tabanına Arb uygulaması da girer; rapor bunu bağımsız küçük kanıt denetimiyle eşitlememelidir. FLINT’in kendi garanti belgesi de işlem türlerini ve uygulama varsayımlarını ayırır. [flintlib](https://flintlib.org/doc/guide/correctness/guarantees.html)

### 3.7. LLM konsensüsü, öz güven ve insan onayı

Bunlar aynı kanıtın daha güçlü veya daha zayıf sürümleri değildir; farklı sorulara cevap verir:

| Kanıt türü | Cevap verdiği soru |
|---|---|
| LLM’nin “eminim” demesi | Model hangi güven ifadesini üretiyor? |
| Çoklu model uzlaşması | Modeller aynı yoruma/cevaba mı yöneldi? |
| Formal denklik | İki formal ifade belirtilen anlamda eşdeğer mi? |
| İnsan onayı | Kullanıcı gösterilen tanımı kabul etti mi? |
| Sertifika kontrolü | Bu formal önerme geçerli mi? |

Çoklu model yöntemleri bazı deneylerde başarıyı artırabilir; ancak güven kalibrasyonu veri kümesine ve yönteme bağlıdır. İyileşme, formal ispat eşdeğerliği oluşturmaz. Güncel çalışmalar, ajanlar arasındaki bağımlılığın güven birleşimini aşırı iyimser yapabildiğini de gösterir. [arxiv](https://arxiv.org/html/2509.14034v1)

Bu nedenle “farklı aile” ifadesi operasyonel çeşitlilik göstergesidir; istatistiksel hata bağımsızlığının kanıtı değildir.

NIST AI RMF, güvenilirliği bağlam, ölçüm ve risk yönetimiyle ele alır; bir sistemin bütün güven boyutlarını tek kanıt mekanizmasına indirgemeyi desteklemez. NIST’in şeffaflık, açıklanabilirlik ve yorumlanabilirliği ayrı kavramlar olarak ele alması Rigor’un ayrı kayıt yaklaşımıyla uyumludur; fakat belirli Türkçe rozetleri zorunlu kılmaz. [tsapps.nist](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936225)

### 3.8. Birim standardı ve ölçüm belirsizliği

Uluslararası foot:

\[
1\ \mathrm{ft}=\frac{381}{1250}\ \mathrm{m}.
\]

US survey foot:

\[
1\ \mathrm{ft}_{US}=\frac{1200}{3937}\ \mathrm{m}.
\]

İkisi de kendi tanımı altında kesin olabilir, fakat aynı birim değildir. NIST, US survey foot kullanımını tarihsel ve eski uygulamalar dışında bırakmış olsa da eski verilerde bu ayrım hâlâ önemlidir. [nist](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf)

UCUM, makineler arasında birimlerin belirsiz olmayan anlamlarla iletilmesine odaklanır. Rigor da görünür `ft` yazısından ayrı bir birim kimliği, sürümlü tanım ve kaynak kaydı tutmalıdır. [ucum](https://ucum.org/ucum)

Ölçüm belirsizliği ise dönüşümle yok olmaz. \(y=cx\) ve \(c\) kesin olduğunda, uygun ölçüm modeli altında:

\[
u(y)=|c|u(x).
\]

Yani kesin katsayı yeni katsayı belirsizliği eklemez; girdi belirsizliğini ölçekler. “8000 ft ölçüldü” ifadesini “tam 8000 ft fiziksel gerçek” diye yorumlamak doğru değildir. GUM, ölçüm sonucunun belirsizliğiyle birlikte ifade edilmesini ve belirsizlik bileşenlerinin açıklanmasını esas alır. [bipm](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf)

## Bölüm IV — Alternatiflerin karşılaştırılması

### 4.1. Karar matrisi

Aşağıdaki puanlar deneysel ölçüm değil, bu araştırmaya ait mimari değerlendirmedir. Ölçek: 1 zayıf, 5 güçlü. “Karmaşıklık” satırında 5 daha düşük uygulama/test yükünü ifade eder.

| Ölçüt | A — Mevcut | B — Çok boyutlu | C — Kapsamlı hibrit |
|---|---:|---:|---:|
| Yanlış kesinlik iddiasını önleme | 3 | 5 | 4 |
| Matematiksel sertifikayı doğru temsil | 2 | 5 | 5 |
| Formülasyon hatasını saklamama | 4 | 5 | 5 |
| Anahtarsız/LLM’siz çalışma | 2 | 5 | 5 |
| Uzman olmayan için anlaşılabilirlik | 3 | 3 | 5 |
| Mevcut mimariyle uyum | 5 | 3 | 4 |
| Uygulama ve test kolaylığı | 5 | 2 | 3 |
| Yeni motorlara genişleme | 2 | 5 | 5 |

Toplam puan vermiyorum: yanlış `PROVEN` riskinin ağırlığıyla uygulama kolaylığının ağırlığı eşit değildir.

### 4.2. A yaklaşımı ne zaman savunulabilir?

Mevcut etiket şu anlamda açıkça tanımlanırsa savunulabilir:

> “Bu işlem Rigor’un uçtan uca yayın politikasındaki bütün kapılardan geçti.”

Bu bir süreç uygunluğu etiketidir. Matematiksel kanıt gücünün doğrudan etiketi değildir.

Avantajı, semantik belirsizliği görünür tutmasıdır. Dezavantajı, “ÇAPRAZ DOĞRULANDI” başlığı altında hem sertifikasız simülasyonu hem kesin sertifikalı hesabı toplamasıdır. Üstelik tek sertifika ve tek denetleyici bulunan durumda gerçek çapraz yöntem yoksa bu adlandırma olgusal olarak da uygun değildir.

### 4.3. B yaklaşımının sorunu

Uzman raporu için en dürüst modeldir; fakat kullanıcıya sekiz ayrı durum göstermek bilgi yükü yaratır. Bu yüzden tam vektör ayrıntı tablosunda, kısa kapsam özeti ise kutuda olmalıdır.

HCI bulguları, daha fazla açıklamanın otomatik olarak daha iyi karar anlamına gelmediğini gösterir. Bu, çok boyutlu iç kayıt ile sade dış sunumun ayrılmasını destekleyen bir tasarım gerekçesidir; seçilen kutunun deneysel olarak üstün olduğunu kanıtlamaz. [arxiv](https://arxiv.org/pdf/2102.09692.pdf)

### 4.4. Önerilen hibritin anlamı

Önerilen C, mevcut üç etiketin anlamını hiç değiştirmeden yanına küçük dipnot eklemek değildir.

Şu değişiklik gereklidir:

- `PROVEN`: kapsamı belirtilmiş matematiksel iddia kabul edilmiş kanıtla doğrulandı.
- `CROSS_VALIDATED`: kapsamı belirtilmiş sonuç bağımsız yöntemlerle desteklendi; ilgili formal kanıt yok.
- `REFUSED`: istenen cevap yayımlanmadı.
- `NEEDS_INPUT`, `NEEDS_CONFIRMATION`, `VERIFICATION_PENDING`: sonuç etiketi değil, işlem durumudur.

Böylece kanıt gücü ile iş akışının tamamlanması ayrılır.

### 4.5. Kritik sorunun kesin cevabı

LLM konsensüsü yok diye uçtan uca cevabın yayımlanmasını sınırlandırmak şu koşullarda doğru güvenlik önlemidir:

- Doğal dilde iki veya daha fazla sonuç değiştiren yorum vardır.
- Tek ajanın kaynak metni doğru aktardığı doğrulanmamıştır.
- Model seçimi veya büyüklük eşlemesi çözülmemiştir.
- Zorunlu doğrudan insan onayı yoktur.
- Yüksek riskli kullanım politikası bağımsız semantik inceleme gerektirir.

Fakat aynı nedenle kabul edilmiş matematiksel ispatın durumunu düşürmek şu koşullarda yanlıştır:

- Kanıtlanan önerme açık ve sabittir.
- Kullanılan tanımlar bellidir.
- Sertifika doğru önermeye bağlanmıştır.
- Onaylı bağımsız denetleyici kabul etmiştir.
- Yorum belirsizliği ayrı gösterilmektedir.
- Özellikle doğal dil bulunmayan doğrudan formal IR söz konusudur.

Doğru politika: “matematik kanıtlı, amaçlanan soruya uygunluğu henüz onaylanmadı.” Yanlış politika: “LLM yok, dolayısıyla bu eşitliğin matematiksel kanıtı daha zayıf.”

Bu ayrımın temeli, formal ispatın geçerliliğiyle teorem ifadesinin anlamının farklı sorular olmasıdır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

## Bölüm V — Özet kutusu tasarımları

Aşağıdaki kutular doğrudan rapora yerleştirilebilecek tasarım önerileridir. Ortak varsayım, belirtilen eşitliğin bağımsız denetleyici tarafından gerçekten kabul edilmiş olmasıdır. Uluslararası foot katsayısının kesinliği NIST tanımına dayanır. [nist](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf)

### 5.1. Alternatif 1 — Mevcut politikayı değiştirmeyen geçiş metni

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Genel etiket: ÇAPRAZ DOĞRULANDI  
> Uluslararası foot tanımına göre dönüşümün kesin matematiksel sertifikası bağımsız denetleyicide kabul edildi; genel etiket, formülasyon bağımsızlığına ilişkin Rigor koşulu sağlanmadığı için sınırlıdır.  
> Bu kontrol, 8000 değerinin kaynaktan doğru alındığını veya gerçek bir yüksekliği gösterdiğini doğrulamaz.

- Doğrulanan: Tam dönüşüm eşitliği.
- Doğrulanmayan: Kaynak, niyet ve fiziksel gerçeklik.
- Yanlış anlama: “Çapraz doğrulandıysa yalnızca yaklaşık doğrudur.”
- Önleyici ifade: “Kesin matematiksel sertifikası … kabul edildi.”
- Dezavantaj: Genel etiket ile matematiksel açıklama gerilimlidir.
- Kullanım koşulu: Gerçekten mevcut `CROSS_VALIDATED` şartları da sağlanmış olmalı. İki bağımsız yöntem yoksa bu etiket kullanılmamalıdır.

### 5.2. Alternatif 2 — Matematik odaklı kısa kutu

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Matematiksel durum: KANITLANDI — uluslararası foot tanımına göre  
> Dönüşüm tamdır; matematiksel sertifika bağımsız doğrulayıcı tarafından kontrol edildi.  
> Bu kanıt yalnızca dönüşümü kapsar; kaynak değerini, problem yorumunu ve gerçek yüksekliği doğrulamaz.

- Doğrulanan: Kesin eşitlik.
- Doğrulanmayan: Kaynak–soru–gerçeklik zinciri.
- Yanlış anlama: Bütün sorunun doğrulandığı sanılabilir.
- Önleyici ifade: “Yalnızca dönüşümü kapsar.”
- Dezavantaj: Birim tanımının katsayısı kutuda görünmez.

### 5.3. Alternatif 3 — İki kısa güven açıklaması

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Etiket: KANITLANDI — birim dönüşümü  
> Neye güvenebilirsiniz? Uluslararası foot için 1 ft = tam 0,3048 m alınarak yapılan hesabın eşitliği bağımsız kontrol edildi; sonuç yuvarlanmış değildir.  
> Neyi kanıtlamaz? 8000 ft değerinin doğru kaynaktan geldiğini, sorunun doğru yorumlandığını veya gerçek bir yüksekliği temsil ettiğini.

- Doğrulanan: Tanımı belirtilmiş dönüşüm.
- Doğrulanmayan: Üç dış kapsam.
- Yanlış anlama: “Güvenebilirsiniz” ifadesi genel güvene yayılabilir.
- Önleyici ifade: Güvenilecek iddiayı hemen adlandırmak.
- Dezavantaj: Soru başlıkları her raporda tekrarlandığında uzun görünebilir.

### 5.4. Alternatif 4 — Açık çok boyutlu kutu

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Matematik: KANITLANDI — uluslararası foot tanımına göre kesin dönüşüm; sertifika bağımsız kontrolden geçti.  
> Problem yorumu: Bağımsız incelenmedi.  
> Girdi: Hesap, verilen 8000 ft değeri için geçerlidir; kaynak doğruluğu incelenmedi.  
> Gerçek dünya: Yükseklik ölçümü veya uçuş başarısı doğrulanmadı.

- Doğrulanan: Matematik boyutu.
- Doğrulanmayan: Diğer boyutlar açıkça listelenir.
- Yanlış anlama: “İncelenmedi” ifadesi matematiksel kanıtı da şüpheli gösterebilir.
- Önleyici ifade: Her durumun kendi başlığında verilmesi.
- Dezavantaj: Basit dönüşüm için fazla ayrıntılıdır; karmaşık mühendislikte uygundur.

### 5.5. Alternatif 5 — Yorum onayı bekleyen durum

> Hesaplanan eşitlik: 8000 ft = 12192/5 m = 2438,4 m  
> Matematiksel durum: KANITLANDI — uluslararası foot tanımına göre  
> Yanıt durumu: ONAY BEKLİYOR  
> Dönüşümün sertifikası bağımsız kontrol edildi; ancak bu hesabın sorduğunuz işlemi temsil ettiği henüz onaylanmadı.  
> Onaylanacak işlem: “8000 uluslararası foot değerini metreye çevir.”

- Doğrulanan: Formal eşitlik.
- Doğrulanmayan: Kullanıcının amaçladığı işlemle eşleme.
- Yanlış anlama: Matematiksel `KANITLANDI` görüldüğü için onay adımı atlanabilir.
- Önleyici ifade: Ayrı “Yanıt durumu” ve somut onay metni.
- Dezavantaj: Nihai cevap değil, ara rapordur.

### 5.6. Alternatif 6 — Önerilen dengeli kutu

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Matematiksel durum: KANITLANDI — belirtilen birim tanımına göre  
> Uluslararası foot tanımıyla (1 ft = tam 0,3048 m), bu eşitliğin matematiksel sertifikası çözücüden bağımsız bir doğrulayıcı tarafından kontrol edildi; sonuç yuvarlanmış değildir.  
> Kapsam: Bu kanıt, verilen 8000 ft değerinin metre karşılığını doğrular; değerin kaynaktan doğru alındığını, sorunun doğru yorumlandığını veya gerçek bir yüksekliği doğru temsil ettiğini doğrulamaz.

- Doğrulanan: Tanımı, değeri ve tam gösterimi belli eşitlik.
- Doğrulanmayan: Kaynak, yorum ve gerçeklik.
- Yanlış anlama: “Bağımsız” sözcüğü denetleyicinin tüm yazılım risklerinden bağımsız olduğu sanılabilir.
- Önleyici ifade: “Çözücüden bağımsız” diyerek bağımsızlığın türünü belirtmek.
- Dezavantaj: Tek cümlelik mevcut tasarımdan uzundur.
- Karar: Varsayılan kullanıcı kutusu olarak bunu öneriyorum.

### 5.7. İfade politikası

| Soru | Karar |
|---|---|
| “Matematiksel olarak kesin” ne zaman? | Tam değer/eşitlik kanıtlanmışsa; yaklaşık orta nokta için değil |
| “KANITLANDI” tek başına yeterli mi? | Hayır; kanıtlanan iddia veya kapsam hemen yanında olmalı |
| “Doğrulama kapsamı” gerekli mi? | Evet; en az bir kısa kapsam cümlesi |
| “LLM doğrulaması yapılmadı” yazılmalı mı? | Varsayılan özet uyarısı olmamalı; yapılan işi değil, kullanılan teknolojiyi öne çıkarıyor |
| “Doğal dil yorumu bağımsız doğrulanmadı” daha mı iyi? | Evet, gerçekten doğal dil yorumu varsa; “bağımsız incelenmedi” formal garanti çağrışımı açısından daha temkinli |
| Doğrudan IR’de ne yazmalı? | “Doğal dil çevirisi yok; verilen formal ifade kontrol edildi.” |
| Tek cümle yeterli mi? | Varsayılan olarak hayır; kanıt ve kapsam için iki kısa açıklama öneriyorum |
| Karmaşıklığa göre uzunluk değişebilir mi? | Evet; içerik kuralları sabit, görünür ayrıntı sayısı risk ve bağımlılığa göre değişmeli |

Türkçe sözcüklerin kullanıcılar üzerindeki kesin etkisini bu kaynaklarla belirleyemem. “Kanıtlandı” veya “kesin” kelimesinin bütün kullanıcılarca aynı yorumlandığını iddia etmiyorum. Bu ifadeler kullanıcı çalışmasıyla doğrulanması gereken tasarım seçimleridir. Açıklamaların aşırı güveni tek başına önlememesi yönündeki bulgular, bu sınamayı gerekli kılar. [arxiv](https://arxiv.org/pdf/2102.09692.pdf)

## Bölüm VI — Adversarial test sonuçları

Bunlar çalıştırılmış ürün testleri değil, önerilen politikanın masa başı güvenlik değerlendirmesidir.

| Senaryo | Önerilen durum/etiket | Kullanıcıya gösterilecek özet ve davranış |
|---|---|---|
| Kesin dönüşüm, LLM yok | `PROVEN / EXACT_VALUE` | “Birim dönüşümü kanıtlandı; kaynak ve problem yorumu doğrulanmadı.” Yapılandırılmış işlem açıksa LLM aranmaz. |
| Kesin sertifika, tek LLM ailesi | Matematik `PROVEN`; yorum `SINGLE_SOURCE` | “Hesap kanıtlandı; doğal dil yorumu tek kaynaktan geldi.” Gerekli doğrudan onay alınır. |
| Kesin sertifika, iki LLM ailesi | Matematik `PROVEN`; yorum `MULTI_SOURCE_AGREEMENT` | “Hesap kanıtlandı; bağımsız üretilen yorumlar aynı formal ifadede uyuştu.” Niyet garantisi verilmez. |
| Yanlış girdi, doğru hesap | Koşullu matematik `PROVEN` | “Verilen girdiye göre hesap kanıtlandı; girdinin gerçekliği doğrulanmadı.” Yanlışlık biliniyorsa cevap yayımlanmaz, düzeltme istenir. |
| Yanlış fiziksel model, doğru matematik | Model-içi matematik `PROVEN`; uygulama `BLOCKED` | “Bu modele göre hesap kanıtlandı; modelin bu kullanım için uygun olmadığı belirlendi.” Mühendislik cevabı olarak sunulmaz. |
| Sertifikasız ODE simülasyonu | Şartlar sağlanırsa `CROSS_VALIDATED` | “İki yöntem belirtilen toleransta uyuştu; kesin hata sınırı kanıtlanmadı.” |
| Sertifika üretildi, kontrol edilmedi | `VERIFICATION_PENDING` | “Sertifika henüz kontrol edilmedi; doğrulanmış sonuç hazır değil.” `PROVEN` yasak. |
| Sertifika kontrolü başarısız | `REFUSED / CERTIFICATE_FAILED` | “Sonuç doğrulanamadı; sertifika kontrolü başarısız.” Otomatik `CROSS_VALIDATED`e düşürülmez. |
| Ajanın ilettiği kullanıcı onayı | Onay `UNVERIFIED`; yanıt `NEEDS_CONFIRMATION` | “Kullanıcı onayı doğrudan alınmadı.” Matematik kaydı korunur; kullanıcı adına onay varsayılmaz. |
| Geçerli sertifika, değiştirilmiş sonuç | `BLOCKED / ARTIFACT_MISMATCH` | “Gösterilen sonuç doğrulanan kayıtla eşleşmiyor.” Başlık yeniden üretilemezse yayımlanmaz. |
| Belirsiz foot standardı | `NEEDS_INPUT` | “Uluslararası foot mu, tarihsel US survey foot mu kullanılıyor?” Sessiz seçim yapılmaz. |
| Doğrudan formal IR | Kontrol başarılıysa `PROVEN` | “Verilen formal ifade kanıtlandı; doğal dil çevirisi yapılmadı.” LLM konsensüsü gerekmez. |
| Onaylı şablonun yeni girdilerle kullanımı | Yeni kontrol geçerse `PROVEN`; değilse bekleme/ret | “Şablonun bu girdilerle ürettiği iddia yeniden doğrulandı.” Eski sertifika yeni sayılara aktarılmaz. |
| Kaynak metin yanlış yorumlanmış, sertifika geçerli | İstenen cevap `REFUSED / FORMULATION_MISMATCH` | “Hesap kendi ifadesi için geçerli; kaynakta sorulan işlemi temsil etmiyor.” Yanlış yorumlanmış sayı cevap kutusundan kaldırılır. |

### 6.1. En tehlikeli örnek: doğru dönüşüm, yanlış eşitsizlik

Kaynak:

> “En az 8000 ft.”

Yanlış formalizasyon:

\[
h\leq8000\ \mathrm{ft}.
\]

Rigor bu eşiği kusursuz biçimde metreye çevirebilir. Ancak şu iki iddia farklıdır:

1. \(8000\ \mathrm{ft}=2438{,}4\ \mathrm{m}\).
2. Kaynak şartı \(h\leq2438{,}4\ \mathrm{m}\) demektir.

Birincinin sertifikası ikincisini kanıtlamaz. Doğru rapor davranışı:

> Yanıt verilmedi: Kaynakta “en az” yazarken formal ifadede “en fazla” kullanılmış. Birim dönüşümü doğru olsa da bu sonuç kaynak koşulunun cevabı olarak kullanılamaz.

Geçerli matematiksel alt kanıt denetim ekinde kalabilir. Fakat kullanıcıya istenen cevabın yanında yeşil veya koşulsuz `KANITLANDI` verilmez. Bu, ispatın geçerliliği ile ifadenin anlamını ayırma ilkesinin doğrudan uygulamasıdır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### 6.2. Rapor bütünlüğünün sınırı

İç sistemde rapor, kanıt kaydından deterministik üretilebilir ve değişiklik denetlenebilir. Ancak dışarı çıkarılmış HTML/Markdown/PDF’nin daha sonra değiştirilmediği, matematiksel sertifikadan tek başına anlaşılmaz.

Bu nedenle dış doğrulama:

- Yalnızca ekli sertifikayı değil,
- Sertifikanın bağlı olduğu önermeyi,
- Görünür sayı ve birimleri,
- Gösterilen kapsam ve etiketi

birlikte kontrol etmelidir. Bu, PCC’de kanıtın gerçek nesneye ve amaçlanan politikaya bağlı olması gereğine benzer; kaynak kimliğini doğrulamak ise ayrı meseledir. [people.eecs.berkeley](https://people.eecs.berkeley.edu/~necula/Papers/marktoberdorf.pdf)

## Bölüm VII — Önerilen mimari sözleşme

Aşağıdaki sözleşme araştırmadan türetilen öneridir; mevcut uygulanmış davranış değildir.

### 7.1. Güven boyutları

| Boyut | Kaydedilecek anlam | Örnek durumlar |
|---|---|---|
| `math_evidence` | Formal iddianın kanıt gücü | `PROVEN`, `CROSS_VALIDATED`, `UNVERIFIED`, `FAILED` |
| `claim_kind` | Kanıtlanan şeyin türü | `EXACT_VALUE`, `ENCLOSURE`, `PROPERTY`, `OPTIMALITY` |
| `formulation` | Kaynak/niyet ile formal ifade ilişkisi | `FORMAL_DIRECT`, `TEMPLATE_BOUND`, `SINGLE_SOURCE`, `MULTI_SOURCE_AGREEMENT`, `AMBIGUOUS`, `MISMATCH` |
| `input_origin` | Değerin nereden ve nasıl geldiği | `USER_DIRECT`, `USER_FILE`, `VIA_AGENT_UNVERIFIED` |
| `definition_basis` | Birim, model ve semantik tanımlar | `RESOLVED`, `AMBIGUOUS`, `UNSUPPORTED` |
| `approval` | Kimin, hangi tanımı, hangi kanalda kabul ettiği | `DIRECT`, `UNVERIFIED_RELAY`, `MISSING`, `REJECTED`, `NOT_REQUIRED_BY_PROFILE` |
| `world_validation` | Fiziksel/ampirik uygunluğun durumu | `NOT_ASSESSED`, `EXTERNAL_EVIDENCE`, `OUTSIDE_VALIDITY` |
| `artifact_binding` | Kanıt–iddia–sonuç–rapor bağlantısı | `MATCHED`, `MISMATCH`, `NOT_CHECKED` |

`world_validation=EXTERNAL_EVIDENCE`, fiziksel gerçeklik ispatlandı anlamına gelmez; ilgili deneysel kanıtın kayda bağlandığını ifade eder. Ölçüm ve model belirsizliği ayrıca korunur. [bipm](https://www.bipm.org/documents/20126/2071204/JCGM_100_2008_E.pdf)

### 7.2. Sertifika yaşam döngüsü

| Olay/durum | Sonuç |
|---|---|
| `CERTIFICATE_CREATED` | Kanıt durumu yükselmez |
| `CHECK_STARTED` | `VERIFICATION_PENDING` |
| `CHECK_ACCEPTED` | Diğer zorunlu koşullar sağlanırsa `PROVEN` |
| `CHECK_REJECTED` | `FAILED`; cevap `REFUSED` |
| `CHECK_ERROR` | İşlem hatası; `PROVEN` yok |
| `CHECK_TIMEOUT` | Eksik kontrol; yanlışlık kanıtı değildir |
| `CHECKER_UNSUPPORTED` | Desteklenmeyen sertifika; `PROVEN` yok |
| `CLAIM_CHANGED` | Eski kabul yeni iddiaya uygulanamaz |
| `REPORT_BINDING_MISMATCH` | Rapor yayımlanmaz |
| `CHECKER_POLICY_INVALIDATED` | Yeniden kontrol gerekir |

`REJECTED`, mutlaka matematiksel önermenin yanlış olduğunu göstermez; bozuk veya geçersiz sertifika da olabilir. `TIMEOUT`, `MISSING` ve `UNSUPPORTED` ise başarısız ispat denetimiyle aynı sınıfa konulmamalıdır.

### 7.3. `PROVEN` için makinece değerlendirilebilir koşullar

Matematiksel iddia düzeyinde bütün koşullar gerekli olmalıdır:

1. İddianın kanonik kimliği ve tam içeriği mevcut.
2. Değişken alanları, birimler, tanımlar ve varsayımlar çözülmüş.
3. Sertifika bu iddia ve bu girdiler için üretilmiş.
4. Onaylı sertifika türü kullanılmış.
5. Denetleyici kimliği, sürümü ve politika sürümü kayıtlı.
6. Denetleyici gerçek kontrol sonucu `ACCEPT` üretmiş.
7. İzin verilmeyen aksiyom veya güven kaçamağı yok.
8. Sonuç, birim ve gösterim doğrulanan iddiayla eşleşiyor.
9. Rapordaki “tam”, “aralık”, “optimum” gibi sözcükler kanıt türüne uyuyor.
10. Sonradan değişiklik veya geçersizleştirme kaydı yok.

Bunlara ek olarak kullanıcıya istenen sorunun cevabı olarak yayımlama kapısı bulunmalıdır:

- Çözülmemiş yorum belirsizliği yok.
- Bilinen kaynak–formülasyon uyuşmazlığı yok.
- Kullanım profili gerektiriyorsa doğrudan onay var.
- Kullanım açısından zorunlu model geçerlilik koşulları sağlanıyor.
- Kritik eksik bilgi yok.

Bu kapı başarısızsa matematiksel alt iddianın `PROVEN` kaydı silinmez; fakat “sorunuzun cevabı” olarak yayımlanmaz.

### 7.4. Kanıtın iddia türüne uygunluğu

Geri ikame her iddia için yeterli değildir:

- Bir kökün denklemi sağladığını göstermek, bütün köklerin bulunduğunu göstermez.
- Uygun bir çözüm bulmak, optimum olduğunu göstermez.
- KKT koşullarını sağlamak, gerekli küresellik koşulları olmadan küresel optimum garantisi vermez.
- Bir aralığın sıfırı içermesi, ifadenin sıfıra eşit olduğunu göstermez.
- Ayrıklaştırılmış denklemi çözmek, sürekli ODE/PDE çözümünün hata sınırını kanıtlamaz.

Bu nedenle sertifika kabul kaydı yalnızca “geçti” değil, hangi özelliğin geçtiğini taşımalıdır. FLINT belgeleri de aralık kapsamasının eşitlik kanıtıyla aynı olmadığını ve kesme hatalarının ayrıca ele alınması gerektiğini açıklar. [flintlib](https://flintlib.org/doc/tutorials/numerics/series.html)

### 7.5. `CROSS_VALIDATED` sözleşmesi

Bu etiket için:

- En az iki kayıtlı yöntem bulunmalı.
- Bağımsızlık gerekçesi belirtilmeli.
- Aynı formal problemi ve aynı girdileri çözdükleri doğrulanmalı.
- Karşılaştırma metriği ve tolerans önceden belirlenmiş olmalı.
- Uyuşma ve sınır testleri geçmiş olmalı.
- Formal ispat bulunmadığı açıkça yazılmalı.

“İki yöntem” otomatik olarak bağımsız değildir. Aynı algoritmanın iki sarmalayıcısı veya aynı yanlış IR’ın iki motoru, farklı hata türlerine karşı sınırlı koruma sağlar.

### 7.6. LLM’siz açıklama üretimi

Önerilen özet üreticisi tamamen deterministik olabilir:

- `EXACT_VALUE`: “Sonuç tamdır; yuvarlanmış değildir.”
- `ENCLOSURE`: “Matematiksel değerin bu aralıkta bulunduğu kanıtlandı.”
- `CHECK_ACCEPTED`: “Sertifika … tarafından kontrol edildi.”
- `SINGLE_SOURCE`: “Doğal dil yorumu tek kaynaktan geldi.”
- `FORMAL_DIRECT`: “Verilen formal ifade kontrol edildi; doğal dil çevirisi yapılmadı.”
- `VIA_AGENT_UNVERIFIED`: “Bu değer ajan tarafından iletildi; kullanıcıdan doğrudan alındığı doğrulanmadı.”
- Fiziksel büyüklük: “Bu hesap gerçek ölçümü veya fiziksel modelin uygunluğunu doğrulamaz.”

LLM yalnızca isteğe bağlı geniş açıklama üretebilir. Etiketi, kritik kapsam cümlesini veya “tam/aralık” ayrımını değiştirememelidir.

Bu yaklaşım, mevcut yol haritasındaki deterministik anlatım iskeletiyle uyumludur.

### 7.7. Özet–kanıt tablosu tutarlılık kuralları

1. Kutudaki her sayı bir kanıt kaydındaki sonuç alanına bağlanmalı.
2. Birim ve tanım aynı kayıt kimliğinden gelmeli.
3. “Bağımsız kontrol edildi” yalnızca bağımsızlık koşulu kayıtlıysa yazılmalı.
4. “Kullanıcı onayladı” yalnızca ilgili formal tanıma bağlı doğrudan onay varsa yazılmalı.
5. “Kaynak doğrulandı” hash varlığı nedeniyle üretilememeli.
6. `ENCLOSURE` sonucunda orta nokta tam sonuç gibi gösterilememeli.
7. Özet ile ayrıntı tablosu çelişirse rapor oluşturma başarısız olmalı.
8. Dil değişimi güven durumunu değiştirmemeli.
9. Yeniden oynatma, eski etiketi kopyalamak yerine güncel politika altında yeniden değerlendirmeli.
10. Politika değişikliği ve eski/yeni karar farkı kayda geçirilmeli.

### 7.8. `PROVEN` verilmesinin kesinlikle yasak olduğu durumlar

İddia düzeyinde:

- Sertifika yalnızca üretilmiş, kontrol edilmemiş.
- Denetleyici reddetmiş, hata vermiş veya tamamlanmamış.
- Sertifika farklı iddiaya/girdiye ait.
- Birim veya matematiksel alan belirsiz.
- İzin verilmeyen aksiyom veya kontrol atlatma yolu var.
- Yalnızca çözücü başarı bayrağı, LLM onayı veya `unsat_core` var.
- Yalnızca yakınsama veya motor uyuşması var.
- Gösterilen sayı/iddia sertifikadan farklı.
- Aralık kanıtı tam değer iddiasına yükseltilmiş.

İstenen cevabın etiketi olarak ayrıca:

- Bilinen yanlış problem yorumu.
- Çözülmemiş sonuç değiştirici belirsizlik.
- Gerekli insan onayının ajan tarafından taklit edilmesi.
- Bilinen kullanım alanı dışı fiziksel modelin uygunmuş gibi sunulması.

### 7.9. Kabul ve regresyon testleri

| Test | Beklenen sonuç |
|---|---|
| Aynı sertifika ve IR, LLM erişimi 0/1/2 aile | Matematiksel durum değişmez; yalnızca yorum kaydı değişir |
| Resmî CLI erişimi var, API anahtarı yok | Anahtar yokluğu nedeniyle yetenek yok sayılmaz |
| 8000 uluslararası ft dönüşümü | Tam kesir ve tam ondalık; kabul edilmiş kontrolle `PROVEN / EXACT_VALUE` |
| 8000 US survey ft | Farklı tanım kimliği ve farklı sonuç; eski sertifika geçmez |
| Girdi 8000’den 8001’e değişir | Eski kabul yeni girdiye uygulanamaz |
| Sertifika mevcut, kontrol yok | `PROVEN` üretilemez |
| Denetleyici `REJECT` döndürür | Güvenilir cevap yok; otomatik çapraz doğrulamaya düşüş yok |
| “En az” → `≤` mutasyonu | Kaynak–formülasyon uyuşmazlığı; cevap engellenir |
| Ajan “kullanıcı onayladı” der | Doğrudan onay kaydı oluşmaz |
| Rapor değeri değiştirilir | Bağlantı kontrolü başarısız |
| Aralık sertifikası | “Tam değer” metni üretilemez |
| Dosyanın yanlış hücresi, doğru hash | Hash kontrolü kaynak çıkarımını geçmiş sayamaz |
| Şablon alan koşulu ihlal edilir | Yeniden onay veya ret; eski doğrulama miras alınmaz |
| Kaynak ve yorum bilinmiyor | “Doğru” işaretlenmez; `UNKNOWN/NOT_CHECKED` korunur |
| TR/EN aynı kayıt | Aynı güven durumu ve aynı kapsam |

Test kümesinde yanlış `PROVEN` sayısının sıfır olması zorunlu kabul ölçütü olmalıdır; fakat testte sıfır hata, bütün olası girdiler için sıfır hata kanıtı değildir. NIST’in ölçüm ve risk yönetimi yaklaşımıyla uyumlu olarak kapsam, hata türleri ve artık riskler ayrıca kaydedilmelidir. [nist](https://www.nist.gov/itl/ai-risk-management-framework)

## Bölüm VIII — Rigor’a özgü değişiklik önerileri

Aşağıdaki değişiklikler uygulama talimatı değil, proje sahibinin onayına sunulacak mimari metin önerileridir.

### 8.1. Korunacak kararlar

Şunlar korunmalıdır:

- K1/K24/K25: alan uyarlamasına açık, alan bilgisini çekirdekten ayıran yapı.
- K3/K9: SDK ve MCP’nin birinci sınıf olması.
- K4: eksik parametrede fail-closed.
- K5: yeniden üretilebilir kanıt raporu.
- K6: formülasyonun Rigor’dan veya çağıran ajandan gelebilmesi.
- K7: sade anlatım.
- K14/K15: ücretli API anahtarı varsaymama ve resmî CLI politikası.
- K18: şablon ve LLM’siz öz-denetim hedefi.
- K26: Lean arka ucunun açık güven politikasıyla eklenmesi.
- §3.2: fiziksel modelin gerçekliğinin matematiksel garanti dışında kalması.
- §3.3 A2/A4/A5/A6: gizli varsayım, anlatım sapması, jargon ve sahte kullanıcı cevabının yasaklanması.

### 8.2. §1.1 — Dürüst garanti tanımı

Mevcut “deterministik motorlar hesap hatalarını sıfırlar” ifadesi ürün garantisi olarak fazla mutlak kalıyor. Determinizm tek başına doğruluk değildir; denetleyici ve tanım bağlantısı önemlidir. Formal doğrulama araçları da kalan güven varsayımlarını açıklar. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

Önerilen metin:

> Rigor, her matematiksel sonucu açıkça belirtilmiş formal iddia ve varsayımlara bağlar. Kanıt durumu, kabul edilmiş doğrulama kayıtlarından belirlenir. Problem yorumu, girdi kökeni ve gerçek dünya geçerliliği ayrı raporlanır. Doğrulama tamamlanmadan veya gerekli bilgi sağlanmadan güvenilir sonuç yayımlanmaz.

### 8.3. §3.2 — Hedef olmayanlar

Fiziksel model ve kod denetimi kapsam sınırları korunmalı; şu hüküm eklenmeli:

> Matematiksel sertifika; kaynak verinin doğruluğu, ölçüm kalitesi, fiziksel modelin gerçekliğe uygunluğu, uygulamanın kötü amaçlı olmaması, belge bütünlüğü veya sonuç üreticisinin kimliği için kendiliğinden güvence oluşturmaz. Bu özellikler varsa ayrı kanıt mekanizmalarıyla değerlendirilir.

### 8.4. §3.3 — Anti-hedefler

A1’in özü korunmalı, kapsamı netleştirilmeli:

> A1. Yanlış veya kapsamı yanıltıcı bir iddianın KANITLANDI etiketiyle sunulması en kritik başarısızlıktır. Doğru bir alt hesabın kanıtı, yanlış yorumlanmış ana sorunun cevabını KANITLANDI yapmak için kullanılamaz.

Yeni anti-hedef:

> A7. Kabul edilmiş matematiksel kanıtın, yalnızca LLM erişimi veya model ailesi sayısı nedeniyle kanıtsız ya da yaklaşıkmış gibi raporlanması.

Bu ekleme muhafazakârlığı kaldırmaz; yanlış kapsam genişletme ile kanıtın yanlış küçümsenmesini ayırır.

### 8.5. §4.1 — Etiketler

Önerilen yeni metin:

> PROVEN, kimliği belirli matematiksel iddianın onaylı denetleyici tarafından kabul edilmiş sertifikayla doğrulandığını belirtir. Model ailesi sayısı matematiksel kanıt durumunun koşulu değildir. Her PROVEN kaydı iddia türünü ve kapsamını taşır.  
> CROSS_VALIDATED, aynı formal problemin kayıtlı bağımsız yöntemlerle karşılaştırıldığını ve belirlenmiş tolerans/test koşullarını geçtiğini belirtir; formal kanıt anlamına gelmez.  
> REFUSED, istenen cevabın yayımlanmadığını belirtir. Eksik bilgi, başarısız doğrulama ve politika engeli ayrı nedenlerle kaydedilir.

Bu, mevcut etiket anlamlarını değiştirdiği için açık sahip onayı gerektirir.

### 8.6. §4.3 — Girdi kaynağı ve onay

Önerilen ek:

> Girdi kökeni, girdinin gerçekliğinden ayrıdır. Dosya hash’i bütünlük kimliği sağlar; doğru hücrenin seçildiğini veya verinin gerçeği temsil ettiğini tek başına göstermez. SDK çağrısı veya MCP kanalı, insan onayı için otomatik kimlik kanıtı sayılmaz. Onay, gösterilen formal tanımın kimliğine ve kayıtlı doğrudan etkileşim olayına bağlanır.

Ajan onayının kullanıcı onayı sayılmaması korunmalıdır. Ancak matematiksel alt kanıt ile onay gerektiren cevap yayını ayrılmalıdır.

### 8.7. §4.4 — Tek formal IR

Önerilen değişiklik:

> Doğrudan formal IR, doğal dilden otomatik çeviri olmadığı için çoklu LLM formülasyon koşuluna tabi değildir. Matematiksel iddia sertifika kontrolünden geçerse PROVEN olabilir. IR’ın haricî kaynak veya kullanıcı niyetini temsil ettiği iddiası ayrıca değerlendirilir.

Bu değişiklik `main`deki tasarımcı kararını ve güncel Faz 1 tavanını etkiler; yeni onay gerekir.

### 8.8. §4.5 — Model kütüphanesi

Örneklerle karşılaştırma, çift giriş, birim ve geçerlilik testleri korunmalı. Şu ayrım eklenmeli:

> Kütüphane doğrulaması; kaynak aktarımı, uygulama testleri ve matematiksel özellikler için hangi kanıtların bulunduğunu listeler. Bu kayıt fiziksel modelin her kullanımda gerçeğe uygun olduğunu kanıtlamaz. Her problemde parametre bağlama, geçerlilik alanı ve yeni matematiksel sonuç ayrıca kontrol edilir.

### 8.9. §6.4 — Formülasyon ve Red Team

Önerilen hüküm:

> Çoklu model uzlaşması, formülasyon desteğidir; formal ispat değildir. Farklı model aileleri hata bağımsızlığını garanti etmez. Yorumlar kaynak metinden ayrı üretilmeli, eşleme ve denklik kayıtları korunmalı; bilinen uyuşmazlık çözümlenmeden cevap yayımlanmamalıdır.

### 8.10. §6.5 — Çözüm motorları

Önerilen hüküm:

> Motor seçimi alan adına değil, formal yapıya ve kanıtlanacak özelliğe dayanır. İki motorun uyuşması ile sertifika kabulü ayrı olaylardır. Bağımsız kontrol edilmiş sertifikalı iddia için ikinci çözücü savunma derinliği sağlayabilir; matematiksel kanıtın zorunlu tanımı değildir. Alan profilleri daha sıkı yayın koşulları koyabilir.

### 8.11. §6.6 — Sertifika

Önerilen hüküm:

> Sertifikanın üretilmesi, mevcut olması, biçimsel olarak okunması ve matematiksel olarak kabul edilmesi ayrı durumlardır. PROVEN için doğru iddiaya bağlı, sürümlü ve onaylı denetleyicinin ACCEPT olayı zorunludur. `unsat_core`, çözücü başarı bayrağı ve LLM değerlendirmesi tek başına sertifika kabulü sayılmaz.

### 8.12. §6.7 — Sade anlatım

Önerilen hüküm:

> Sonuç etiketi, kanıt türü ve kapsam cümleleri doğrulama kayıtlarından deterministik üretilir. LLM erişimi gerekli değildir. İsteğe bağlı LLM sadeleştirmesi matematiksel kapsamı genişletemez, tam değer ile hata sınırını karıştıramaz veya doğrulanmamış onay/kaynak iddiası ekleyemez.

### 8.13. §6.8 — Kanıt raporu

Önerilen değişiklik:

> Özet kutusu sonuç, kapsamı belirtilmiş matematiksel durum, kanıt dayanağı ve doğrulanmayan alanları içerir. Basit işlemlerde iki kısa açıklama yeterlidir; karmaşık mühendislikte model, girdi belirsizliği ve sayısal hata ayrı gösterilir. Özet ve ayrıntı tablosu aynı doğrulama kayıtlarından üretilir.

### 8.14. §3.4 ve yol haritası — Dolaylı etkiler

Güncel `development` tasarımındaki güvenlik tabanı, model ailesi sayısının alan paketleri tarafından gevşetilemeyeceğini söylüyor. Önerilen politika bu tabanı paket düzeyinde delmemeli; çekirdek sözleşme açık sahip kararıyla yeniden tanımlanmalıdır.

Faz 1 için önerilen değişiklik:

- “Tek IR → en fazla `CROSS_VALIDATED`” kaldırılır.
- Yerine “doğrudan IR + bağımsız kabul edilmiş sertifika → kapsamlı `PROVEN`” gelir.
- Doğal dil güvencesi F3’te genişler; matematiksel kanıt F3’e ertelenmez.
- Bütün altın testler yeni etiket semantiğine göre güncellenir.
- Eski raporlar için `policy_version` korunur.

Lean bölümü de aksiyom, güvenilir challenge ifadesi ve bağımsız kontrol koşullarıyla tutarlı tutulmalıdır. Resmî rehber bu kontrollerin ve kalan varsayımların neden ayrı kaydedilmesi gerektiğini açıklamaktadır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

## Bölüm IX — Nihai karar

Rigor için kararım: Matematiksel kanıtı ayrı tutan çok boyutlu iç model ve kapsamı açık hibrit özet kutusu kullanılmalıdır. LLM konsensüsü matematiksel kanıtın koşulu olmaktan çıkarılmalı; problem yorumuna ilişkin destek ve gerektiğinde cevap yayımlama koşulu olarak korunmalıdır.

Verilen senaryoda kullanıcının API anahtarı bulunmaması, aşağıdaki kutuya bir eksiklik uyarısı eklemek için gerekçe değildir. API anahtarı, LLM erişimi ve matematiksel doğrulama üç ayrı yetenek alanıdır. Rigor’un anahtarsız resmî CLI erişimini de “LLM yok” diye sınıflandırmaması gerekir; erişim hiç yoksa bile yerel kesin doğrulama çalışabilmelidir.

### Önerilen nihai özet kutusu

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Matematiksel durum: KANITLANDI — belirtilen birim tanımına göre  
> Uluslararası foot tanımıyla (1 ft = tam 0,3048 m), bu eşitliğin matematiksel sertifikası çözücüden bağımsız bir doğrulayıcı tarafından kontrol edildi; sonuç yuvarlanmış değildir.  
> Kapsam: Bu kanıt, verilen 8000 ft değerinin metre karşılığını doğrular; değerin kaynaktan doğru alındığını, sorunun doğru yorumlandığını veya gerçek bir yüksekliği doğru temsil ettiğini doğrulamaz.

### Her ifadenin kanıt dayanağı

| Kutudaki ifade | Gerekli somut kayıt |
|---|---|
| `8000 ft` | Formal iddiaya bağlanmış girdi değeri ve birim kimliği |
| `12192/5 m` | Kabul edilmiş sertifikanın doğruladığı rasyonel sonuç |
| `2438,4 m` | Kesir–ondalık gösterim eşitliğinin kesin kontrolü |
| `KANITLANDI` | Onaylı denetleyicinin doğru iddiaya karşı `ACCEPT` olayı |
| “Belirtilen birim tanımına göre” | Uluslararası foot tanımının açık seçimi ve sürümlü tanım kaydı |
| `1 ft = tam 0,3048 m` | NIST’in kesin uluslararası foot tanımı  [nist](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf) |
| “Çözücüden bağımsız” | Denetleyicinin çözücüden ayrı kontrol mekanizması ve bağımlılık kaydı |
| “Kontrol edildi” | Yalnızca dosya varlığı değil, tamamlanmış doğrulama sonucu |
| “Yuvarlanmış değildir” | Gösterilen sonlu ondalığın tam rasyonel değere eşitliği |
| Kaynak/yorum/gerçeklik sınırı | Sertifikanın yalnızca formal dönüşüm önermesine ait olması; bu dış iddiaların kanıta dahil edilmemesi |

Bu rapor gerçek bir Rigor oturumunun sertifikasını yeniden kontrol etmiş değildir; kullanıcı tarafından verilen “bağımsız kontrol edilmiş sertifika” varsayımı altında hangi metnin üretilebileceğini belirlemektedir.

### Genellenebileceği sınıflar

Aynı politika şu koşullarda genellenebilir:

- Kesin aritmetik ve birim dönüşümleri.
- Varsayımları açık sembolik özdeşlikler.
- Sertifikalı mantık ve eşitsizlik sonuçları.
- Tam rasyonel doğrusal cebir.
- Uygun sertifikayla doğrulanmış optimizasyon özellikleri.
- Aksiyom ve ifade denetimi yapılmış formal teoremler.

Her durumda “kanıtlandı” sözcüğü, gerçekten denetlenen özelliğe bağlanmalıdır. Formal kanıtın anlamı, kanıtlanan ifadenin ve güven varsayımlarının doğru seçilmiş olmasına bağlı kalır. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### Aynı metnin kullanılamayacağı durumlar

- Kanıt yalnızca aralık kapsamasıysa “sonuç yuvarlanmış değildir” denemez.
- ODE/PDE sonucunda yalnızca yakınsama ve yöntem uyuşması varsa kesin hata garantisi verilemez.
- Girdi ölçümse dönüşümün kesinliği ölçüm belirsizliğini kaldırmaz.
- Kaynak yorumu yanlışsa doğru alt hesap istenen cevabı meşrulaştırmaz.
- Sertifika kontrol edilmediyse “kontrol edildi” denemez.
- Raporla sertifika eşleşmiyorsa eski kabul gösterilen sonucu doğrulamaz. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

Rigor’un göstermesi gereken güven, “LLM’ler ne kadar emin?” sorusunun değil, “hangi iddia, hangi kanıtla, hangi sınırlar içinde doğrulandı?” sorusunun cevabıdır.
















# Rigor — İkinci aşama bağımsız araştırma ve mimari karar raporu

İkinci aşamanın sonucu: Önceki araştırmanın temel ayrımı doğrudur; fakat önerdiği güven sözleşmesi henüz yeterli değildir. Matematiksel kanıtı LLM konsensüsünden ayırmak gerekir. Buna ek olarak kanıtın hangi iddiayı kapsadığı, bağımlı hesaplara nasıl aktarıldığı, denetleyicinin hangi güven tabanına dayandığı ve kullanıcıya cevap olarak yayımlanıp yayımlanamayacağı ayrı değerlendirilmelidir.

En önemli değişiklik şudur: Önceki rapordaki “çok boyutlu durumlar + kapsamlı özet” önerisini, **iddia–kanıt grafiği** ve ayrı bir cevap yayımlama kararıyla tamamlıyorum. Aksi hâlde doğru bir alt hesabın kanıtı, yanlış veya yaklaşık bir üst sonuca taşınabilir. OMG’nin Structured Assurance Case Metamodel standardı, iddiaları, kanıtları ve bunların bağlantılarını ayrı temsil etmek için bağımsız bir dayanak sunar; ancak böyle bir yapı kurmanın tek başına argümanı doğru yaptığını da özellikle reddeder. [omg](https://www.omg.org/spec/SACM/2.3/PDF)

8000 ft örneğinde karar değişmiyor: doğru tanıma bağlı, bağımsız kontrol edilmiş kesin eşitlik için matematiksel durum `PROVEN` olabilir; API anahtarı veya LLM konsensüsü aranmaz. Buna karşılık bu etiket, kaynak metnin, kullanıcı niyetinin veya gerçek irtifanın doğrulandığı anlamına gelemez. Uluslararası foot katsayısının tamlığı NIST tarafından açıkça tanımlanır. [nist](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors)

## 1. Önceki araştırmanın eksik ve zayıf yönleri

### 1.1. Sistematik denetim

| Önceki bulgu veya öneri | Değerlendirme | Önem | Yanlış karar riski | İkinci aşamadaki düzeltme |
|---|---|---|---|---|
| Matematiksel ispat ile problem yorumu farklıdır | Güçlü; korunuyor | Kritik | Doğru hesabı yanlış soruya cevap yapmak | İddia kimliği ve kaynak eşlemesi ekleniyor |
| API anahtarı yokluğu matematiksel kanıtı zayıflatmaz | Doğru; korunuyor | Yüksek | Anahtarsız kullanımı gereksiz kısıtlama | Erişim, yorum desteği ve kanıt ayrı tutuluyor |
| “Sertifika var” ile “kontrol edildi” farklıdır | Doğru fakat yetersiz ayrıntılı | Kritik | Başarı bayrağıyla `PROVEN` üretmek | Kontrol olayı, güven profili ve bağımlılık kapsamı zorunlu |
| Bağımsız denetleyici gereklidir | Ana örnek için uygun; genel ifade fazla tekdüze | Yüksek | Doğrulanmış hesaplama ile bağımsız kanıt denetimini karıştırmak | Kanıt mekanizması ve TCB ayrıca sınıflandırılıyor |
| Çok boyutlu model yeterlidir | Eksik | Kritik | Yerel kanıtı hesap zincirinin tamamına yaymak | İddia–kanıt grafiği ve bileşim kuralları ekleniyor |
| Sertifika başarısızsa sonuç reddedilmeli | Güvenli başlangıç; fazla mutlak | Orta | Alternatif geçerli kanıt yolunu gereksiz engellemek | Başarısız kanıt yolu ile yanlış iddia ayrılıyor |
| HCI kaynakları önerilen kutuyu destekler | Dolaylı destek; doğrudan doğrulama yok | Yüksek | Türkçe metni bilimsel olarak doğrulanmış sanmak | Kullanıcı testi zorunlu kabul ediliyor |
| B/C yaklaşımı karar matrisi | Tasarım değerlendirmesi; deneysel sonuç değil | Orta | Öznel puanları bilimsel üstünlük sanmak | Sayısal puanlar yerine koşullu karşılaştırma |
| Bütün problem sınıflarına genelleme | Yüzeysel | Yüksek | ODE, istatistik ve optimizasyona yanlış etiket taşımak | İddia türüne göre kurallar ayrılıyor |
| Depo tasarımının incelenmesi | Kısmi | Yüksek | Okunamayan paragrafları denetlenmiş saymak | Kapsam sınırlaması korunuyor; Faz 1 planı ayrıca inceleniyor |
| Önceki öneriye adversarial test | Yararlı fakat eksik | Kritik | Boş doğruluk, sahte durum kaydı, bileşim hatası | Yeni karşı örnekler ekleniyor |

### 1.2. Önceki raporda bilimsel kanıt ile tasarım tercihi yeterince ayrılmamıştı

Şu sonuçlar doğrudan teknik dayanağa sahiptir:

- Bir formal teoremin geçerli ispatı olması, teorem ifadesinin amaçlanan anlamı taşıdığını göstermez. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
- Sertifika üreten araç ile sertifika denetleyicisi ayrılabilir; denetleyicinin kendisi de formal olarak doğrulanabilir. [cakeml](https://cakeml.org/checkers.html)
- Farklı LLM’ler aynı yanlış cevaba yönelebilir; sağlayıcı veya aile çeşitliliği hata bağımsızlığını garanti etmez. [arxiv](https://arxiv.org/html/2506.07962v1)
- Sayısal çözüm doğrulaması ile fiziksel modelin kullanım amacına göre geçerliliği farklıdır. [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)

Buna karşılık şu öneriler bilimsel zorunluluk değildir:

- Kutuda tam iki açıklama cümlesi kullanılması.
- `PROVEN` adının korunması.
- Belirli sayıda güven boyutu tutulması.
- “Kapsam dışı” ifadesinin “doğrulanmadı”dan daha iyi anlaşılması.
- Hibrit arayüzün bütün kullanıcılar için üstün olması.

Bunlar kanıta dayalı gerekçelendirilebilir tasarım tercihleridir; Rigor bağlamında deneysel olarak doğrulanmış sonuçlar değildir.

### 1.3. Önceki kaynak kullanımının düzeltilmesi

Önceki raporun önemli sınırlaması, bazı geniş iddiaları birkaç kaynak üzerinden desteklemesiydi:

- Lean rehberi, ispatın geçerliliği–ifadenin anlamı ayrımını güçlü biçimde destekler; Rigor’un bütün motorlarının güvenli olduğunu göstermez. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)
- NIST AI RMF gibi risk çerçeveleri, şeffaflık ve kapsam açıklamasını destekleyebilir; `PROVEN` için belirli teknik eşikleri belirlemez.
- Genel HCI çalışmaları, Türkçe “KANITLANDI” kutusunun yanlış anlaşılmayacağını kanıtlamaz.
- Çoklu ajan literatüründeki başarı artışları, doğal dil formülasyonunun güvenilirliği için otomatik veya evrensel sonuç değildir.

Bu raporda güncel LLM çalışmasının okunan arXiv sürümünü ampirik araştırma olarak kullanıyorum; ayrıca doğrulanmamış bir yayın statüsünü hakemli kanıt gibi sunmuyorum. [arxiv](https://arxiv.org/html/2506.07962v1)

## 2. Yeni araştırma ve ek kanıtlar

### 2.1. Yeni kritik bulgu: Geçerli ispat, içi boş bir iddiayı kanıtlıyor olabilir

Önceki rapor yanlış formalizasyonu ele aldı; fakat boş doğruluğu yeterince incelemedi.

Örneğin:

\[
(x>0\land x<0)\Rightarrow h\geq 2438{,}4.
\]

Bu önerme klasik mantıkta geçerlidir. Fakat hiçbir uygulanabilir durum için roket irtifasını desteklemez.

Vacuity literatürü, doğrulanan özelliklerin erişilemeyen veya sağlanamayan önkoşullar nedeniyle önemsiz biçimde doğru olabileceğini uzun süredir ele alır. Beer ve çalışma arkadaşlarının çalışması, başarılı doğrulamanın yanında anlamlı tanıkların ve boş doğruluk kontrollerinin önemini gösterir. [weizmann.elsevierpure](https://weizmann.elsevierpure.com/en/publications/efficient-detection-of-vacuity-in-temporal-model-checking-2/)

Rigor için yeni yükümlülük:

- Uygulanabilir bir çözüm veya mühendislik cevabı isteniyorsa varsayımların birlikte sağlanabilirliği ayrıca değerlendirilmelidir.
- “Çelişkiyi kanıtla” göreviyle “bu koşullarda sonucu hesapla” görevi karıştırılmamalıdır.
- Sağlanabilirlik bilinmiyorsa “sağlanabilir” kabul edilmemelidir.
- Genel formal teorem modunda koşullu teoremler yasaklanmamalı; fakat uygulama cevabına dönüşürken önkoşulların durumu gösterilmelidir.

Bu nedenle bütün `PROVEN` sonuçlarına tek bir evrensel “varsayımlar sağlanabilir” şartı eklemek de doğru değildir. Kural görev türüne bağlı olmalıdır.

### 2.2. Yeni kritik bulgu: Denetleyici güveni bir evet/hayır özelliği değildir

CakeML projesi şu ayrımı somutlaştırıyor:

1. Kanıt sistemi sağlam olabilir.
2. Denetleyici algoritması doğru olabilir.
3. Denetleyici uygulaması algoritmaya uygun olabilir.
4. Derlenmiş makine kodu uygulamaya uygun olabilir.
5. Girdi okuyucusu ve gerçek çalışma ortamı yine güven varsayımı olarak kalabilir.

CakeML’nin doğrulanmış denetleyicileri bu zincirin önemli kısmını makine koduna kadar doğrular; buna rağmen mantık, parser tanımları ve gerçek ortamın formal modele uygunluğu gibi varsayımları açıkça listeler. [cakeml](https://cakeml.org/checkers.html)

Dolayısıyla Rigor için:

> “Bağımsız denetleyici kabul etti” güçlü ama tamamlanmamış bir güven açıklamasıdır.

Detay raporu en az şunları belirtmelidir:

- Denetleyici kimliği ve sürümü.
- Desteklenen sertifika dili.
- Sağlamlık dayanağı.
- Parser ve sayı semantiği.
- Çözücüyle ortak bağımlılıklar.
- Derleme/çalıştırma güven varsayımları.
- Kabul edilen aksiyomlar veya yerel değerlendirme yolları.

Burada herkesçe kabul edilmiş tek bir evrensel güven derecelendirmesi bulmadım. Bu alan için Rigor’a özgü, denetlenebilir mekanizma profilleri öneriyorum; sahte güven yüzdeleri değil.

### 2.3. Yeni somut örnek: FloVer neyi kanıtlıyor, neyi kanıtlamıyor?

FloVer, sonlu hassasiyetli hesapların yuvarlama hata sınırlarını sertifika üzerinden kontrol eden, Coq ve HOL4 içinde doğrulanmış bir denetleyicidir. Çalışma, analiz aracının ürettiği sertifikayı ayrı bir denetleyiciyle kontrol etmenin gerçek hata yakalama değeri taşıdığını gösterir; Daisy analiz aracında bir bölme hatası da bulunmuştur. [ar5iv.arxiv](https://ar5iv.arxiv.org/html/1707.02115)

Fakat aynı çalışma kritik sınırlar içerir:

- Sonuçlar belirli işlem diline ve giriş aralıklarına bağlıdır.
- IEEE-754 bağlantısında sürüme/uygulamaya özgü önkoşullar bulunur.
- Makalede anlatılan HOL4 bağlantısında subnormal değerlerden kaçınma gibi ek koşullar vardır.
- Bazı çıkarılmış çalıştırılabilirler doğrulanmış derleme zincirine, bazıları doğrulanmamış çıkarım/derlemeye dayanır.
- Makaledeki sertifika lexer/parser bileşenleri ayrıca doğrulanmamış olarak açıklanır. [ar5iv.arxiv](https://ar5iv.arxiv.org/html/1707.02115)

Rigor açısından önemli sonuç:

> Bir aracın adının “formal olarak doğrulanmış” olması, bütün giriş biçimlerinin ve çalışma yollarının aynı garantiye sahip olduğunu göstermez.

Bu nedenle `checker="FloVer"` veya `engine="Arb"` alanı tek başına etiket üretmek için yeterli değildir. Kullanılan yolun önkoşulları ve TCB kapsamı da bağlanmalıdır.

### 2.4. Yeni düzeltme: ODE sonuçları doğaları gereği yalnızca çapraz doğrulanabilir değildir

Önceki raporun Rigor v1 açısından muhafazakâr ODE değerlendirmesi anlaşılabilir; fakat bunu matematiksel sınır olarak yorumlamak yanlıştır.

CAPD::DynSys, ODE çözümleri ve varyasyon denklemleri için garantili sınırlar hesaplayan doğrulanmış sayısal yöntemler içerir. Kütüphane hem olağan sayısal hesaplama hem rigorous hesaplama yolları sunar. [sciencedirect](https://www.sciencedirect.com/science/article/pii/S1007570420304081)

Bundan çıkan karar:

- `solve_ivp ×2 + yakınsama`: formal hata kanıtı değildir.
- Doğrulanmış ODE kapsaması: uygun önkoşullarla matematiksel garanti sağlayabilir.
- Doğrulanmış ODE motoru kullanmak: otomatik olarak ayrı, bağımsız kontrol edilebilir sertifika üretmek demek değildir.
- Rigor’un gelecekte ODE için `PROVEN / ENCLOSURE` desteklemesi mümkündür; fakat motorun ve bağlantının güven sözleşmesi ayrıca kurulmalıdır.

Böylece problem sınıfına göre kalıcı tavan koymak yerine mevcut kanıt mekanizmasına göre sınıflandırma yapılır.

### 2.5. Yeni bağımsız dayanak: Mühendislikte doğrulama ve geçerleme ayrımı

NASA-STD-7009B:

- Verification’ı modelin gereksinim ve spesifikasyonlara uygunluğu,
- Validation’ı modelin amaçlanan kullanım açısından gerçek dünyayı temsil etme derecesi

olarak ayırır. Ayrıca girdi, sonuç ve sonuçtan türetilen büyüklüklerdeki belirsizliklerin kaydını ister. [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)

Bu, Rigor için iki önemli düzeltme getiriyor:

1. “Fiziksel gerçeklik kapsam dışı” demek, bilinen model geçersizliğini saklamaya izin vermez.
2. Bir sonuçtan türetilen yeni niceliğe geçerken belirsizlik ve sınırlamalar izlenebilir kalmalıdır.

Rigor fiziksel model geçerlemesi yapmayabilir. Fakat modelin geçerlilik alanı dışında kullanıldığını biliyorsa bunu cevap yayımlama kararında kullanmalıdır.

### 2.6. LLM bağımsızlığı için daha güçlü ampirik kanıt

Kim ve çalışma arkadaşlarının çalışması, yüzlerce modelin cevaplarında hata korelasyonunu araştırır. İncelenen HELM verisinde iki modelin ikisi de yanlış olduğunda aynı yanlış seçeneğe yönelme ortalaması yaklaşık %60’tır; çalışma farklı sağlayıcı ve mimarilerde de korelasyon bulunduğunu bildirir. [arxiv](https://arxiv.org/html/2506.07962v1)

Sınırı önemlidir: Çalışma ağırlıkla çoktan seçmeli değerlendirmeler ve özgeçmiş puanlaması kullanır. Bu oranı Rigor’un Türkçe matematik formülasyon hatasına taşımak doğru değildir.

Desteklediği sonuç:

> İki farklı aileden oybirliği, hata bağımsızlığının veya doğru problem yorumunun kanıtı değildir.

Desteklemediği sonuç:

> Çoklu model kullanmak yararsızdır.

Aynı çalışma doğruluk ile çeşitliliğin birlikte değerlendirilmesi gerektiğini gösterir. Bu nedenle Rigor’da model ailesi sayısı bir kontrol girdisi olarak kalabilir; kanıt gücü etiketi veya otomatik doğruluk yüzdesi olmamalıdır. [arxiv](https://arxiv.org/html/2506.07962v1)

### 2.7. HCI için önceki uyarıyı daraltan yeni kanıt

Van der Bles ve çalışma arkadaşları, toplam 5.780 katılımcılı beş deneyde belirsizlik iletişimini incelemiştir. Sayısal belirsizlik açıklamalarının güven üzerindeki etkisi genellikle küçük; açık sözel belirsizlik ifadelerinin etkisi daha belirgin bulunmuştur. [pnas](https://www.pnas.org/doi/10.1073/pnas.1913678117)

Bu bulgu önceki rapordaki şu düşünceyi daraltır:

> “Doğrulanmayan alanları yazmak kullanıcıyı gereksiz şüpheye düşürür” genel bir yasa değildir.

Ancak çalışma haber benzeri metinler ve ampirik sayılar üzerinedir; matematiksel sertifika kutusu veya Türkçe `KANITLANDI` etiketi üzerinde değildir. Dolayısıyla Rigor için sonuç:

- Kapsam sınırlarını gizlememek gerekir.
- Kesin hesaba “belki yanlış” gibi belirsiz uyarılar eklemek yerine doğrulanmayan nesne açıkça adlandırılmalıdır.
- Kullanıcı testiyle ölçülmesi gereken şey genel güven artışı değil, doğru iddiaya doğru güvenin verilmesidir.

### 2.8. Yeni mimari alternatif: Güven vektörü yerine iddia–kanıt yapısı

SACM, iddiaları ve onları destekleyen kanıt/argüman bağlantılarını açık temsil eder. Standardın önemli uyarısı şudur: Böyle bir temsil, argümanın tam, geçerli veya doğru olduğunu kendiliğinden göstermez. [omg](https://www.omg.org/spec/SACM/2.3/PDF)

Rigor için bunun hafif bir uyarlamasını öneriyorum:

- Her sonuç bir veya daha fazla iddiaya bağlıdır.
- Her iddianın varsayımları ve bağımlılıkları vardır.
- Her kanıt belirli bir iddiayı veya bağlantıyı destekler.
- “Matematik”, “kaynak”, “yorum” gibi durumlar bu yapıdan türetilir.
- Rapor özeti de aynı yapıdan üretilir.

Tam SACM uygulaması veya karmaşık assurance-case editörü v1 için gerekli değildir. Fakat yalnızca sekiz bağımsız durum alanı tutmak, hesap zincirinin neden geçerli olduğunu göstermeye yetmez.

## 3. Düzeltilen ve değişen bulgular

### 3.1. Rigor’un güncel depo durumu

Bu aşamada GitHub üzerinden dal uçları yeniden kontrol edildi:

| Dal | Güncel SHA | Önceki araştırmaya göre |
|---|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` | Değişmedi |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` | Değişmedi |

Bu uçlar altında yeni bir depo değişikliği görünmüyor. Depoya yazma işlemi yapılmadı.

Yeniden okunan önemli belgeler:

- `docs/superpowers/specs/2026-11-07-rigor-design.md`
  - Git blob: `a509f1287726fe8922b0d7a46fbf18e5b4d55896`
- `docs/superpowers/plans/2026-11-07-faz-1-cekirdek.md`
  - Git blob: `8bed859fe37cd80dc1500fb92b9dcdeeabe1b741`

Güncel kök ağaç yine `.gitignore`, `Handoff`, `LICENSE`, `README.md` ve `docs/` içeriyor; planlanan `src/` ürün yapısı bulunmuyor.

Belge içindeki görevler ve test kodları uygulama kanıtı değildir. Bunları çalıştırılmış testler olarak değerlendirmiyorum.

İnceleme sınırı devam ediyor: Uzun dosyalar GitHub aracında kesiliyor. Bu aşamada Faz 1 planının önemli yeni bölümleri okunabildi; ancak tasarımın §6.4–§6.8 tamamının kesintisiz satır denetimi hâlâ yapılmış değildir. Önceki araştırmanın bu açığını kapatılmış gibi göstermiyorum.

GitHub sonuçları kaynak numarası üretmediği için depo bulgularına uydurma atıf eklemiyorum; commit ve blob kimlikleri denetim dayanağıdır.

### 3.2. Faz 1 planında yeni görülen somut sorunlar

#### A. Kanıt durumu aşırı sıkıştırılmış

Planlanan `Conditions` yapısında:

- `certificate: "formal" | "none"`
- `model_families: int`
- `paths_agree: bool`

bulunuyor.

Bu alanlar şu ayrımları temsil edemiyor:

- Sertifika üretilmiş mi, kontrol edilmiş mi?
- Hangi iddiaya ait?
- Hangi denetleyici kabul etti?
- Bağımsızlık ne tür?
- Kabul edilen özellik tam değer mi, aralık mı, yalnızca uygulanabilirlik mi?
- Bağlı alt hesaplar da kanıtlı mı?

Bu nedenle sorun yalnızca kullanıcı metni değil, veri sözleşmesidir.

#### B. Planlanan sertifika türü ile bağımsız kanıt denetimi aynı değil

Görev 10’daki sertifika planı, SymPy ile geri ikame ve `simplify` sonucuna dayanabilen satırlar içeriyor.

Bu yararlı bir doğrulama yöntemidir; fakat kendi başına küçük, çözücüden bağımsız ve sağlamlığı gösterilmiş kanıt denetleyicisi değildir. Çözüm ve kontrol aynı CAS semantiğine veya uygulamasına dayanıyorsa ortak hata olasılığı güven tabanında kalır.

Bu tespit, planlanan hesabın yanlış olduğu anlamına gelmez. “Formal certificate” adının, dayanağından daha güçlü bir garanti çağrıştırmaması gerektiğini gösterir.

#### C. Kanonik IR kimliği semantik ortamı kapsamıyor olabilir

Planlanan `ir_hash`, `Problem` nesnesinin JSON içeriğini özetliyor.

Fakat aynı JSON’daki `ft`:

- farklı birim kayıtları,
- farklı alan paketi sürümleri,
- farklı model tanımları,
- farklı matematiksel semantik

altında farklı anlam taşıyabilir.

Dolayısıyla güvenilir iddia kimliği yalnızca IR JSON’sinden oluşmamalı; semantik bağımlılık manifestini de kapsamalıdır.

#### D. Boyut kontrolü, ölçek doğruluğu değildir

Plana göre birim kapısı boyut uyumluluğunu kontrol ediyor. Bu gerekli ama yeterli değil.

Örneğin:

\[
1\ \mathrm{m}+1\ \mathrm{cm}=1{,}01\ \mathrm{m}
\]

ifadesinde iki terimin boyutu aynıdır. Sayıların ortak birime doğru normalize edilmemesi hâlinde boyut kapısı geçebilir, hesap yanlış olabilir.

Bu bir gerçekleşmiş hata bulgusu değil; planın kabul testlerinde ayrıca kapatılması gereken bir sözleşme boşluğudur.

#### E. Yapısal serbestlik derecesi tam belirlenmişliği kanıtlamaz

Eşleme tabanlı yapı analizinde:

\[
x+y=2,\qquad 2x+2y=4
\]

iki denklem ve iki değişken bakımından iyi eşleşebilir; fakat tek çözüm yoktur.

Bu nedenle DM/eşleme sonucu “yapısal olarak uygun” demektir. Teklik, tutarlılık ve gerçek rank koşulları ayrıca ele alınmalıdır. Faz 1 planının sonraki çözücü kontrolleri bu açığı kapatabilir; yapı kapısının tek başına matematiksel garanti olarak sunulmaması gerekir.

### 3.3. Önceki önerilerde açık değişiklikler

| Önceki yaklaşım | İkinci aşama kararı |
|---|---|
| Çok boyutlu alanlar yeterli temel | İddia–kanıt grafiği temel, boyutlar türetilmiş görünüm |
| Bütün matematiksel kontrol yollarını `PROVEN`/`CROSS_VALIDATED` ile karşılamak | Kanıtsız fakat yeniden hesaplanmış durum için ek kayıt gerekli |
| Sertifika başarısızlığında her durumda kesin ret | İlgili kanıt yolu reddedilir; ayrı geçerli yol varsa yeniden değerlendirme mümkün |
| `PROVEN` mevcutsa alt hesabın gücü korunur | Korunur; fakat üst cevaba otomatik aktarılmaz |
| Gelecekte ODE de genel politika içinde | Doğrulanmış ODE kapsaması açıkça desteklenebilir; sınıf temelli kalıcı tavan kaldırılır |
| “Tip-2 için matematiksel garanti yok” | Serbest doğal dil niyetine genel garanti yok; sınırlandırılmış dil/çeviri sözleşmeleri kategorik olarak dışlanmamalı |

Son satır önemli bir dil düzeltmesidir: “Hiçbir formülasyon yönteminde garanti olamaz” fazla geniştir. Güvenilir bir formal girdi veya açıkça sınırlandırılmış bir dilin tanımlı semantiğine uygun çeviri ile serbest doğal dilin kullanıcının zihnindeki niyete uygunluğu aynı iddia değildir.

## 4. Adversarial değerlendirme

Aşağıdakiler çalıştırılmış ürün testleri değil, önerilen mimariye karşı tasarlanmış karşı örneklerdir.

| Saldırı veya hata | Neden önceki politika yetmeyebilir? | Gerekli savunma |
|---|---|---|
| Çelişkili varsayımlardan sonuç ispatlamak | Sertifika gerçekten geçerli olabilir | Uygulama görevlerinde sağlanabilirlik/boş doğruluk kontrolü |
| Yaklaşık ODE çıktısını kesin rasyonelle çarpmak | Son işlem kesin diye bütün sonuç kanıtlı görünebilir | Kanıt bağımlılıklarını ve yaklaşık girdiyi korumak |
| `certificate="formal"` alanını ajan doldurur | Güven etiketi beyana dönüşür | Etiket yalnızca güvenilen denetim olaylarından üretilir |
| Kullanıcı `model_families=2` gönderir | İstemci kendine bağımsızlık atar | Sağlayıcı/model/izolasyon kanıtı adaptör katmanından gelir |
| Doğru sertifikayı farklı sayıyla göstermek | Sertifika geçerli, rapor yanıltıcı | Görünür iddia–kanıt bağlantısı |
| Aynı IR, değiştirilmiş `ft` tanımı | Hash aynı, anlam farklı | Semantik manifesti iddia kimliğine katmak |
| Bir kökü doğrulayıp “bütün çözümler” demek | Geri ikame yalnızca aday çözümü doğrular | Tamlık ve teklik iddialarını ayırmak |
| LP gevşetme sınırını MILP optimumu saymak | Sertifika farklı özelliği destekler | Tamsayılı uygulanabilirlik ve global sınır eşlemesi |
| İki motor aynı yanlış dönüştürücüyü kullanır | Uyuşma ortak hatayı yakalamaz | Ortak bağımlılık kaydı ve çapraz yöntem gerekçesi |
| Eski onayı yeni modele taşımak | Aynı şablon adı aynı anlam demek değil | Onayı formal ifade ve model sürümüne bağlamak |
| HTML içindeki kaynak metni sahte rozet içerir | Matematik doğru, görünür rapor aldatıcı | Güvenilir renderer, kaçışlama ve sabit kritik alanlar |
| Uyarı ayrıntıda, büyük `KANITLANDI` başlıkta | Teknik olarak doğru ama kapsamı yanıltıcı | Kapsamı etiketin hemen yanında göstermek |

### 4.1. Bileşimde yanlış güven örneği

Bir ODE motoru:

\[
\hat h=8000\ \mathrm{ft}
\]

tahmini üretsin. Rigor sonra kesin dönüşümü kontrol etsin:

\[
8000\times0{,}3048=2438{,}4.
\]

Şu ifade yanlış kapsamlıdır:

> “Roketin tepe irtifası 2438,4 m — KANITLANDI.”

Doğru ifade:

> “Simülasyon tahmini 2438,4 m. Birim dönüşümü kesin olarak kontrol edildi; uçuş tahmininin hata sınırı kanıtlanmadı.”

NASA’nın sonuçlardan türetilen niceliklerde de belirsizlik izlenebilirliği istemesi bu ayrımı bağımsız olarak destekler. [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf)

### 4.2. Kanıt başarısızlığı için önceki aşırı sert kuralın düzeltilmesi

Bozuk bir sertifika, iddianın yanlış olduğunu kanıtlamaz. FloVer çalışması da doğru sınırların kullanılan aşırı yaklaşım nedeniyle bazen doğrulanamayabileceğini açıklar. [ar5iv.arxiv](https://ar5iv.arxiv.org/html/1707.02115)

Bu nedenle:

- Bir kanıt yolu reddedilirse o yol kullanılamaz.
- Ayrı ve onaylı başka bir yol aynı iddiayı gerçekten doğrularsa sonuç yeniden değerlendirilebilir.
- Ancak geçerli görünen kanıtla somut karşı örnek çatışıyorsa sistem durmalıdır.
- Ret sonucunu sessizce yok sayıp iki sayısal cevabın uyuşmasına dayanarak yayın yapmak yasaktır.

Bu ayrım güvenlikten ödün vermez; “kanıt bulunamadı” ile “iddia yanlış”ı karıştırmaz.

## 5. Mimari alternatiflerin yeniden karşılaştırılması

| Yaklaşım | Güçlü yanı | Temel zayıflığı | Karar |
|---|---|---|---|
| A — Mevcut üç etiket, mevcut anlamlarıyla | En düşük geçiş maliyeti | Kanıt, yorum ve süreç uygunluğunu karıştırıyor | Yalnızca geçiş dönemi |
| B — Düz çok boyutlu durum kaydı | Güven sınırları görünür | Bağımlı hesapların bileşimini tek başına açıklamaz | Gerekli ama yetersiz |
| C — Kapsamlı hibrit kutu | Kullanıcıya sade sunum | Alt kayıt hatalıysa düzgün metin yanlış güven üretir | Arayüz olarak uygun |
| D — İddia–kanıt grafiği + yayın kararı + sade kutu | Kapsam, bileşim ve izlenebilirlik birlikte çözülür | Şema ve test yükü daha yüksek | Nihai öneri |
| E — Her şeyi tek süreç uygunluğu etiketiyle gösterme | Mevcut politika korunabilir | Matematiksel kanıtın niteliği ayrı açıklanmadıkça yanıltıcı | Geçici uyumluluk seçeneği |

D yaklaşımının kavramsal dayanağı SACM’nin iddia–kanıt ayrımıdır. Ancak Rigor’a özgü sadeleştirme, etiketler ve yayın kuralları bu raporun tasarım önerisidir; standart tarafından zorunlu tutulmaz. [omg](https://www.omg.org/spec/SACM/2.3/PDF)

### Mevcut tasarım korunabilir mi?

Evet, geçici olarak:

- Eski `label`, `legacy_workflow_label` olarak saklanır.
- Yanına gerçek `math_evidence` eklenir.
- Kullanıcı kutusunda “genel güven seviyesi” yerine matematiksel kanıt açıkça gösterilir.
- Aynı veri için iki etiketin neden farklı olduğu ayrıntıda açıklanır.

Fakat kalıcı olarak `CROSS_VALIDATED` sözcüğünü “kanıt var ama LLM bağımsızlığı yok” anlamında kullanmayı önermiyorum.

## 6. Rigor için nihai önerilen güven politikası

### 6.1. Üç ayrı karar alanı

#### A. İddia

Tam olarak ne söyleniyor?

Örnekler:

- Tam değer.
- Aralık kapsaması.
- Tek çözüm.
- Bütün çözümler.
- Uygulanabilir çözüm.
- Global optimum.
- Belirli varsayımlar altında eşitsizlik.
- Bir istatistiksel yöntemin kapsama özelliği.

#### B. Kanıt

Bu iddiayı ne destekliyor?

| Durum | Anlam |
|---|---|
| `PROVEN` | İddia, onaylı ispat/sertifika kontrol yolu üzerinden kabul edildi |
| `RECOMPUTED` | Açık sayısal semantik altında deterministik yeniden hesap yapıldı; gerekli formal kanıt yolu yok |
| `CROSS_VALIDATED` | Kayıtlı ayrı yöntemler belirlenmiş karşılaştırma koşullarında uyuştu |
| `UNVERIFIED` | Bu iddia için yeterli kontrol yok |

`RECOMPUTED` yeni bir öneridir. `CROSS_VALIDATED` ile tek bir deterministik hesaplamayı aynı sınıfa zorlamamak için gereklidir. Bu durumların tek boyutlu bir olasılık sıralaması olduğu varsayılmamalıdır.

#### C. Cevap yayımlama

| Durum | Anlam |
|---|---|
| `READY` | İstenen cevap yayımlanabilir |
| `NEEDS_INPUT` | Sonucu etkileyen bilgi eksik |
| `NEEDS_CONFIRMATION` | Gerekli doğrudan onay bekleniyor |
| `BLOCKED` | Çatışma, başarısız zorunlu kontrol veya bütünlük sorunu var |
| `REFUSED` | İstenen cevap verilmiyor; neden açıklanıyor |

Böylece `REFUSED`, matematiksel kanıtın rakibi olmaktan çıkar. Bir alt eşitlik kanıtlı olabilir, fakat istenen mühendislik cevabı reddedilebilir.

### 6.2. `PROVEN` için zorunlu sözleşme

Bir iddia ancak şu koşullarla `PROVEN` olabilir:

1. Tam iddia ve görev türü sabittir.
2. Varsayımlar, alanlar ve tanımlar açıktır.
3. Semantik bağımlılıklar sürümlü manifestte kayıtlıdır.
4. Kanıt nesnesi veya ispat denetim yolu bu iddiaya bağlıdır.
5. Güvenilen denetim katmanı gerçekten kabul olayı üretmiştir.
6. Kullanılan yolun bütün önkoşulları karşılanmıştır.
7. Yasaklı aksiyom veya kontrol atlatması yoktur.
8. İddianın bağlı olduğu matematiksel sonuçlar kanıt zincirinde kapsanmıştır veya açık varsayım olarak gösterilmiştir.
9. Görünür rapor aynı iddiayı ifade etmektedir.
10. Çözülmemiş kanıt–karşı örnek çatışması yoktur.

“Bağımsız kontrol edildi” ayrıca bir niteliktir: Her `PROVEN` yolunun bağımsız ikinci uygulamayla kontrol edildiği otomatik varsayılmaz. Ana örnekte bu nitelik vardır.

### 6.3. LLM bağımsızlığı yetersizse uygulanacak kural

- Matematiksel kanıt durumu değişmez.
- Kaynak/niyet eşlemesinin durumu ayrı tutulur.
- Yorum belirsizliği varsa kullanıcıya sorulur.
- Yüksek riskli kullanım profili bağımsız semantik inceleme istiyorsa yayın bekletilir.
- Bu inceleme yalnızca LLM olmak zorunda değildir; doğrudan formal tanım, denetlenmiş şablon veya yetkin insan incelemesi alternatif olabilir.
- LLM oybirliği, bilinen kaynak uyuşmazlığını geçersiz kılamaz.

### 6.4. API anahtarı, LLM erişimi ve bağımsız formülasyon

Bunlar ayrı alanlardır:

| Durum | Sonuç |
|---|---|
| API anahtarı yok, resmî CLI erişimi var | LLM erişimi var olabilir; kimlik ve izolasyon ayrıca kontrol edilir |
| API anahtarı var, tek aile kullanılıyor | Erişim var; aile çeşitliliği yok |
| LLM yok, doğrudan formal IR var | Doğal dil çeviri adımı yok; matematiksel ispat engellenmez |
| Birden çok aile var, aynı aday birbirine gösterilmiş | Çeşitlilik var; bağımsız üretim iddiası sınırlı |
| LLM yok, belirsiz serbest metin var | Sessiz yorum yok; yapılandırılmış giriş veya kullanıcı açıklaması gerekir |

Bu oturumda resmî CLI’ların fiilî çalışması veya abonelik yetkileri sınanmadı. Dolayısıyla belirli CLI sürümünün Rigor adaptörüyle gerekli izolasyonu sağladığı sonucunu vermiyorum.

### 6.5. Hesap zinciri için bileşim kuralı

Etiketler sayısal minimum alınarak birleştirilmemelidir.

Doğru kural:

> Üst iddianın kanıtı, bağımlı iddiaları ve geçiş kurallarını kapsamalıdır.

Örneğin:

- Kanıtlı \(x\in[a,b]\).
- Kanıtlı \(c>0\).
- Kanıtlı dönüşüm kuralı \(y=cx\).

Bunlardan \(y\in[ca,cb]\) kanıtlanabilir. Fakat aralığın orta noktası tam gerçek değer olarak sunulamaz.

Aynı şekilde bir örneklem ortalamasının tam aritmetik hesabı kanıtlanabilir; bu, popülasyon ortalamasının bilindiğini göstermez. İstatistiksel yöntem hakkında formal bir teorem de kanıtlanabilir; o teoremin varsayımlarının gerçek veri üretiminde sağlandığı ayrı sorudur.

### 6.6. Kullanıcı veya ajan etiketi yükseltememeli

- İstemci `PROVEN` alanını belirleyemez.
- `USER_DIRECT` yalnızca istemcinin beyanıyla üretilemez.
- Denetleyici kaydı dışarıdan alınırsa yeniden kontrol veya ayrı güven politikası gerekir.
- Deneysel motor eklentisi başarı olayı taklit ederek çekirdek kanıt kaydı oluşturamaz.
- Yerel makinenin tamamını kontrol eden saldırgana karşı salt yerel etiket mekanizmasının mutlak güven sağladığı iddia edilmez.

Burada hedef, kötü amaçlı yerel yöneticiye karşı imkânsız bir garanti değil; çağıran ajan, bozuk oturum kaydı ve güvenilmeyen motor çıktısına karşı açık sınırdır.

## 7. Özet kutusunun nihai tasarımı

Önceki kutuyu kısaltıyor ve “matematiksel durum” yerine kanıtlanan nesneyi doğrudan adlandırıyorum.

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m  
> Dönüşüm eşitliği: KANITLANDI  
> Uluslararası foot tanımı kullanıldı: 1 ft = tam 0,3048 m. Bu eşitliğin kanıtı, hesabı yapan çözücüden bağımsız bir doğrulayıcı tarafından kabul edildi; 2438,4 m yuvarlanmış bir sonuç değildir.  
> Kapsam dışı: 8000 ft değerinin kaynak metinden doğru aktarılması, bu işlemin asıl soruyu doğru temsil etmesi ve gerçek bir yüksekliğin ölçümü. Bu kanıt bu alanları doğrulamaz.

Uluslararası foot tanımı ve katsayının tamlığı NIST’e dayanır. `2438,4` gösteriminin tamlığı ise şu rasyonel eşitliğe dayanır:

\[
8000\cdot\frac{381}{1250}
=\frac{12192}{5}
=\frac{24384}{10}.
\]

 [nist](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors)

### Kutunun kullanılma koşulları

Bu metin yalnızca:

- Uluslararası foot seçimi açık veya doğrudan yapılandırılmış girdide belirtilmişse,
- Sertifika gerçekten bağımsız denetleyicide kabul edilmişse,
- Sertifika görünen eşitliğe bağlıysa,
- Gösterim eşitliği kontrol edilmişse,
- Bilinen kaynak/yorum uyuşmazlığı gizlenmiyorsa

kullanılmalıdır.

Kaynakta yanlış aktarım biliniyorsa genel “kapsam dışı” metni yeterli değildir. Yerine somut hata yazılmalıdır:

> Yanıt verilmedi: Dönüşüm hesabı geçerli, ancak kullanılan 8000 ft değeri kaynak metinle uyuşmuyor.

Gerekli kullanıcı onayı eksikse ana sonuç başlığına ayrıca:

> Yanıt durumu: Onay bekliyor.

eklenir. Matematiksel alt kanıtın varlığı onay gereksinimini ortadan kaldırmaz.

### Her ifadenin kanıt dayanağı

| İfade | Somut dayanak |
|---|---|
| `8000 ft` | Girdi kaydı ve açık birim kimliği |
| `12192/5 m` | Kabul edilmiş tam değer iddiası |
| `2438,4 m` | Kesir–ondalık eşitlik kontrolü |
| “Uluslararası foot” | Sürümlü birim tanımı ve kaynak kaydı |
| “Bağımsız doğrulayıcı” | Çözücüden ayrı kontrol yolu ve bağımlılık manifesti |
| “Kabul edildi” | Gerçek denetim olayı; yalnızca sertifika dosyası değil |
| “Yuvarlanmış değildir” | Gösterilen ondalığın tam rasyonele eşitliği |
| Kapsam dışı satırı | Kanıtlanan önermede bulunmayan dış iddiaların açık ayrımı |

Bu rapor gerçek bir Rigor sertifikasını çalıştırıp doğrulamış değildir; kullanıcının verdiği bağımsız kabul edilmiş sertifika senaryosu için raporlama sözleşmesini belirlemektedir.

## 8. Uygulama ve kabul kriterleri

### 8.1. Yeni ve kritik regresyon testleri

| Test | Beklenen davranış |
|---|---|
| Aynı kanıt, 0/1/2 LLM ailesi | Matematiksel durum değişmez |
| Çelişkili uygulama varsayımları | İçi boş sonuç mühendislik cevabı olarak yayımlanmaz |
| Yaklaşık ODE sonucu + kesin dönüşüm | Yalnızca dönüşüm alt iddiası `PROVEN` |
| İstemci `certificate="formal"` gönderir | Kanıt durumu yükselmez |
| İstemci `USER_DIRECT` beyan eder | Güvenilen kanal olayı yoksa doğrudan onay oluşmaz |
| Aynı IR, değişen birim kaydı | İddia kimliği veya bağımlılık kontrolü değişir; eski kabul taşınmaz |
| `1 m + 1 cm` | `1,01 m`; boyut uyumu tek başına yeterli sayılmaz |
| İki bağımlı denklem, tek çözüm iddiası | Yapısal eşleme sonucu teklik kanıtı sayılmaz |
| Bir kök bulundu | “Bütün çözümler” etiketi üretilemez |
| Aralık kanıtı | Orta nokta için “tam sonuç” yazılamaz |
| Bozuk sertifika + ayrı geçerli kanıt | Olaylar korunarak yeniden değerlendirme yapılabilir |
| Geçerli kanıt + somut karşı örnek | Çatışma; yayın engellenir |
| HTML kaynak alanında sahte etiket | Kritik arayüz alanını değiştiremez |
| Şablon aynı, model sürümü farklı | Önceki onay ve kanıt otomatik taşınmaz |
| Türkçe ondalık virgül | Görüntüleme yereli ile giriş parser’ı açıkça ayrılır |

Son test Rigor’a özgü yeni bir tutarlılık gereğidir: Faz 1 planı `"0,1"` girdisini belirsiz sayıp reddederken Türkçe rapor `2438,4` gösterebilir. Bu tek başına yanlış değildir; ancak makineye yeniden alma yolu kanonik kesir/noktalı gösterim kullanmalı veya açık yerel ayarı taşımalıdır.

### 8.2. Belgelere aktarılabilecek somut değişiklikler

| Bölüm | Önerilen hüküm |
|---|---|
| §3.3 | “Doğru alt kanıtın yanlış ana iddiayı güvenilir göstermesi kritik başarısızlıktır.” |
| §4.1 | “Matematiksel kanıt durumu, yorum desteği ve cevap yayımlama durumu ayrıdır.” |
| §4.3 | “Köken ve onay alanları çağıranın serbest beyanıyla yükseltilemez.” |
| §4.4 | “Doğrudan formal IR, doğal dil konsensüsüne tabi değildir; kaynak niyeti iddiası ayrıca değerlendirilir.” |
| §4.5 | “Model doğrulaması yeni parametre bağlamasının ve kullanım alanının doğruluğunu otomatik devretmez.” |
| §6.2 | “İddia kimliği IR ile birlikte birim/model/semantik manifestini kapsar.” |
| §6.3 | “Yapısal uygunluk, tutarlılık, sağlanabilirlik ve teklik farklı kontrollerdir.” |
| §6.5 | “Motor sınıfı değil, kanıtlanan özellik ve kullanılan doğrulama yolu etiketin temelidir.” |
| §6.6 | “Sertifika kabulü iddia, önkoşul, denetleyici profili ve bağımlılıklara bağlanır.” |
| §6.7–§6.8 | “Kritik özet alanları aynı kanıt kaydından deterministik üretilir; bilinen sorunlar genel feragat metniyle gizlenemez.” |
| §6.9 | “Şablon onayı yalnızca kapsamı, sürümü ve geçerlilik koşulları eşleştiğinde yeniden kullanılabilir.” |
| §6.11 | “Güvenilir challenge ifadesi, aksiyom politikası ve yalıtılmış kanıt kontrolü korunur.” |

Lean’in güncel resmî rehberi, güvenilir challenge ifadesine karşı kontrolü ve kötü amaçlı olabilecek ispatların yalıtılmış değerlendirilmesini özellikle destekler. [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/)

### 8.3. Sahip onayı gerektiren kararlar

Açık onay gerektirir:

- `PROVEN` anlamının süreç uygunluğundan matematiksel iddia durumuna ayrılması.
- Tek aile/tek IR tavanının kaldırılması.
- `RECOMPUTED` durumunun eklenmesi.
- `REFUSED`ın yayın kararına taşınması.
- Faz 1 testlerinin yeni semantiğe göre değiştirilmesi.
- §3.4 güvenlik tabanının model ailesi sayısı yerine yeni kanıt/politika sözleşmesine göre yeniden tanımlanması.

Korunabilir:

- Fail-closed.
- Gizli varsayım yasağı.
- Sahte kullanıcı onayı yasağı.
- SDK + MCP.
- LLM’siz çekirdek.
- Sürümlü model kütüphanesi.
- Sade ve yeniden üretilebilir rapor.
- Fiziksel model geçerliğini matematiksel kanıtla eşitlememe.

Genel “ONAYLANDI” başlığı ile hâlâ “Tasarımcı kararı” diye işaretli maddeler arasındaki yönetişim belirsizliği devam ediyor. Bunları sessizce sahip kararı saymamak gerekir.

### 8.4. Kullanıcı testi kabul ölçütleri

Başarı ölçütü “kullanıcı daha çok güvendi” olmamalıdır.

Ölçülmesi gerekenler:

- Tam dönüşümü doğru kabul ediyor mu?
- Sertifikanın 8000 değerinin kaynağını doğrulamadığını anlıyor mu?
- Kesin dönüşümü gerçek uçuş başarısıyla karıştırıyor mu?
- Aralık kanıtını tam değer sanıyor mu?
- Bilinen yorum hatası varken sonucu kullanmaktan kaçınıyor mu?
- LLM yokluğunu aritmetik hatası göstergesi sanıyor mu?

Mevcut kutu, önerilen kutu ve etiketsiz açıklama karşılaştırılabilir. Ancak örneklem büyüklüğü, hata toleransı ve kabul eşiği bir pilot çalışma ve güç analiziyle belirlenmelidir; bu rapor keyfî bir başarı yüzdesi önermiyor. Belirsizlik iletişimi araştırmasının bağlama bağlı sonuçları da doğrudan Rigor kullanıcı testinin yerini tutmaz. [pnas](https://www.pnas.org/doi/10.1073/pnas.1913678117)

## 9. Kalan belirsizlikler

1. Tam belge denetimi tamamlanmadı. Uzun dosyaların kesilmesi nedeniyle §6.4–§6.8’in eksiksiz metni hâlâ incelenemedi.
2. Bağımsız kesin aritmetik denetleyicisi seçilmedi. Sertifika dili, parser ve sayı semantiği için ayrı teknik karar gerekir.
3. Rigor ürün testi yapılmadı. Depo tasarım/plan aşamasında; burada önerilen testler çalıştırılmış sonuçlar değildir.
4. Türkçe kutunun anlaşılabilirliği doğrulanmadı. Önerilen metin yayın adayıdır.
5. LLM konsensüsünün Rigor görevlerindeki katkısı ölçülmedi. Genel korelasyon bulguları Rigor’a özgü hata oranı vermez. [arxiv](https://arxiv.org/html/2506.07962v1)
6. CLI izolasyonu denenmedi. Model kimliği, ortak bellek, araç erişimi ve istem değişikliği adaptör testleriyle incelenmeli.
7. Doğrulanmış sayısal motor entegrasyonu seçilmedi. CAPD veya başka motorun Rigor için uygunluğu; lisans, kapsanan matematik, TCB ve bağımsız kontrol açısından ayrıca incelenmeli. [sciencedirect](https://www.sciencedirect.com/science/article/pii/S1007570420304081)
8. Tam saldırgan yerel ortam kapsamı belirlenmedi. Yerel makinenin tamamen ele geçirilmesine karşı rapor etiketinin güvence sınırı açık yazılmalı.

## 10. Birinci ve ikinci araştırma arasındaki net ilerleme

### Elde edilen yeni bilgiler

- Bağımsız denetleyiciye ek olarak parser, derleme zinciri ve yürütme varsayımlarının somut etkisi ortaya kondu.
- FloVer üzerinden gerçekten doğrulanmış sertifika kontrolünün hem değeri hem sınırları gösterildi.
- Geçerli fakat içi boş kanıtlar için yeni yayın kontrolü eklendi.
- Kesin alt hesapların yaklaşık veya yanlış üst sonuçları “aklaması” için bileşim kuralları geliştirildi.
- ODE için kalıcı `CROSS_VALIDATED` tavanı yerine kanıt mekanizmasına bağlı politika netleştirildi.
- Düz güven vektörünün yetersizliği belirlenip iddia–kanıt yapısı önerildi.
- Faz 1 planında kanıt durumunun aşırı sıkıştırılması, semantik hash kapsamı ve birim ölçeği test boşlukları tespit edildi.
- Kullanıcı/ajan tarafından güven durumu yükseltme tehdidi sözleşmeye eklendi.

### Değişen kararlar

- Önceki hibrit model, artık tek başına nihai mimari değil; iddia–kanıt yapısının kullanıcı görünümüdür.
- Üç mevcut sınıf bütün kayıt durumlarını karşılamıyor; `RECOMPUTED` ve ayrı yayın durumları gerekiyor.
- Sertifika başarısızlığı, iddia yanlışlığıyla eşitlenmiyor.
- “Bağımsız kontrol” bütün kanıt yollarının tek biçimi değil; açıkça raporlanan mekanizma niteliğidir.
- Nihai kutu genel “matematiksel durum” yerine “dönüşüm eşitliği”ni etiketliyor.

### Karar ve kanıt matrisi

| Önemli öneri | Dayanak | Kanıt gücü | Alternatif | Kalan risk |
|---|---|---|---|---|
| Kanıt ile problem anlamını ayır | Lean resmî doğrulama rehberi  [lean-lang](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) | Güçlü teknik dayanak | Tek süreç etiketi | Kullanıcı kapsamı yine genelleyebilir |
| LLM ailesini matematiksel kanıt koşulu yapma | Kanıt denetleme mimarisi; LLM korelasyon araştırması  [cakeml](https://cakeml.org/checkers.html) | İlke güçlü; LLM etkisi görev bağımlı | Sıkı yayın profili | Semantik hata devam eder |
| İddia–kanıt bağlantılarını kaydet | SACM  [omg](https://www.omg.org/spec/SACM/2.3/PDF) | Güçlü temsil standardı; doğruluk garantisi değil | Düz güven alanları | Hatalı bağlantı kuralları |
| Boş doğruluğu uygulama görevlerinde kontrol et | Vacuity literatürü  [weizmann.elsevierpure](https://weizmann.elsevierpure.com/en/publications/efficient-detection-of-vacuity-in-temporal-model-checking-2/) | Güçlü formal yöntem temeli | Yalnızca insan incelemesi | Genel kontrol tamamlanamayabilir |
| TCB ve önkoşulları açıkça sürümle | CakeML, FloVer  [cakeml](https://cakeml.org/checkers.html) | Güçlü teknik ve formal dayanak | Araç adına güvenme | Parser/ortam sınırları |
| Kesin değer ile hata sınırını ayır | FloVer  [ar5iv.arxiv](https://ar5iv.arxiv.org/html/1707.02115) | Güçlü matematiksel dayanak | Ortak `PROVEN` + alt tür | Kullanıcı orta noktayı tam sanabilir |
| ODE’ye kalıcı sınıf tavanı koyma | CAPD  [sciencedirect](https://www.sciencedirect.com/science/article/pii/S1007570420304081) | Doğrulanmış sayısal yöntemlerin varlığı güçlü | v1’de desteklememe | Entegrasyon ayrıca doğrulanmalı |
| Türetilmiş niceliklerde belirsizliği koru | NASA-STD-7009B  [standards.nasa](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) | Güçlü mühendislik standardı | Manuel rapor incelemesi | Bağımlılık kaybı |
| Foot tanımını açık bağla | NIST SP 811  [nist](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors) | Birincil resmî tanım | Kullanıcıya her seferinde sorma | Kaynak standardı belirsiz olabilir |
| Kapsamı açık Türkçe kutu kullan | HCI deneyleri + tasarım çıkarımı  [pnas](https://www.pnas.org/doi/10.1073/pnas.1913678117) | Dolaylı ampirik destek | Daha kısa/çok boyutlu kutu | Türkçe kullanıcı testi eksik |
| `RECOMPUTED` ve ayrı yayın kararı ekle | Yukarıdaki ayrımların mimari sentezi | Tasarım önerisi | Eski alanları uyumluluk için koruma | Şema ve geçiş maliyeti |

Nihai karar: Rigor, “sonuç ne kadar güvenilir?” sorusuna tek bir genel seviye vermemeli. Önce hangi iddianın hangi kanıtla doğrulandığını belirlemeli; sonra o iddianın kullanıcının sorusuna cevap olarak yayımlanıp yayımlanamayacağına karar vermelidir.

8000 ft örneğinde kanıtlanan şey dönüşüm eşitliğidir. API anahtarı bulunmaması bu kanıtı azaltmaz. Kaynak, yorum ve gerçek dünya iddiaları ise ancak kendi kanıtları varsa doğrulanmış sayılabilir.