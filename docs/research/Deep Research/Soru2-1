# Rigor — Model yeterliği, benchmark güvenilirliği ve karma heyetin güvence koşulları

## Karar özeti

Üç üyeli bir Rigor heyetinin `KANITLANDI` etiketine katkı verebilmesi için varsayılan olarak **üç üyenin de** ilgili görev kapsamı, erişim yolu ve çağrı ayarları için geçerli yeterlik kaydı bulunmasını öneriyorum. Buna en az iki farklı model ailesi ve heyet düzeyinde ayrı bir ortak-hata değerlendirmesi eklenmelidir.

Bu, “üç yeterlikli modelin bilimsel olarak hatasız olduğu gösterildi” anlamına gelmez. Bir, iki veya üç kayıt arasında evrensel olarak en iyi eşiği belirleyen doğrudan Rigor deneyi bulunmuyor. Üç kayıt önerisinin dayanağı, üst güvence sürecindeki her zorunlu üyenin ölçülmüş ve izlenebilir olmasını istemektir. Gerçek güvenlik katkısı ayrıca ölçülmelidir; aile çeşitliliği veya bireysel başarı, ortak hataları dışlamaz. [arxiv](https://arxiv.org/html/2506.07962v1)

Diğer temel önerilerim:

- Yeterlik dosyası kullanılmalı; fakat dosya bir model onayı değil, kapsamı ve tarihi belli ölçüm kanıtlarını indekslemelidir.
- `rigor qualify` benzeri bir komutun dosya yazması tek başına güven sağlamaz.
- Başlangıç yeterliği, dar tanımlanmış her profil için 300 ana test, 60 eşli/metamorfik ek test ve 40 bağımsız gerçek-dünya/adversarial testten oluşan 400 istemlik bir kabul paketiyle ölçülebilir.
- Bu büyüklük ve aşağıdaki geçme eşikleri bilimsel standart değil, açık gerekçeli başlangıç politikasıdır.
- Varsayılan kayıt süresi için 30 gün öneriyorum; bilinen model, erişim yolu veya ayar değişikliği bu süreyi beklemeden yeniden ölçüm gerektirmelidir.
- Aynı yeterlik ve çalışma koşullarına sahip ücretsiz erişim, matematiksel veya formülasyon kanıtı bakımından düşük sayılmamalıdır. Ancak eski Karar 5’in bütünüyle kaldırılması ayrı ve açık bir sahip kararı olarak kaydedilmelidir. Yeni brief’teki tasarımcı yorumu, bu değişikliği kendiliğinden yapmış sayılmaz. [concepts_brief.md]

***

# I — Önceki araştırmanın eksiklikleri

## 1.1. Güncel karar durumunu doğru okumak

Bu turda eklenen yeni `concepts_brief.md` tam olarak incelendi. Önceki sürümden farklı olarak:

- Soru 1 kapanmış.
- Dört kategori benimsenmiş: `PROVEN`, `CERTIFIED`, `CROSS_VALIDATED`, `REFUSED`.
- Model yeterliğinin ölçülmesi ve model–düşünme düzeyi ilişkisi sahip kararı olmuş.
- Güçlü model ücretsiz erişimde sunulursa katkısının aynı sayılması yeni sahip kararı olarak kaydedilmiş.
- Yeterlik dosyasının teknik koşulları, test büyüklüğü, geçme eşiği, kayıt süresi ve gereken yeterlikli üye sayısı hâlâ açık.
- Soru 1 altındaki dokuz tasarımcı kararı ayrıca onaylanmış kabul edilmiyor. [concepts_brief.md]

Dolayısıyla bu rapor etiket sistemini yeniden açmıyor; yeterlik mekanizmasının bu sisteme nasıl güvenilir girdi vereceğini araştırıyor.

## 1.2. Hedeflenen yeni eksikler

| Eksik | Önem | Neden kritik? |
|---|---|---|
| “Model seti geçti” ifadesinin kapsamı belirsizdi | Kritik | Dar testten bütün matematiğe yeterlik aktarılabilir |
| Örneklem ve hata belirsizliği sayısallaştırılmamıştı | Kritik | Sıfır gözlenen hata, sıfır gerçek hata sanılabilir |
| Bireysel yeterlik ile heyet yeterliği ayrılmamıştı | Kritik | Aynı yanlış yorumu paylaşan güçlü modeller seçilebilir |
| Parametrik üretimin ezberi önlediği fazla güçlü söylenmişti | Yüksek | Şablon ailesine aşırı uyum gözden kaçabilir |
| Açık–gizli başarı farkı doğrudan ezber göstergesi sayılabilirdi | Yüksek | Zorluk veya dağılım farkı yanlış suçlamaya dönüşebilir |
| Ölçüm komutu ile güvenilir kayıt aynı şey gibi görülebilirdi | Kritik | Ajan sahte çıktı üretebilir veya kayıt değiştirilebilir |
| Kayıt süresi için dayanak yoktu | Yüksek | Süresi dolmamış fakat değişmiş modele güvenilebilir |
| Sağlayıcıya özgü düşünme ayarları ortak ölçeğe indirgeniyordu | Yüksek | `high` gibi aynı adlar farklı çalışma koşullarını saklar |
| Bir veya iki yeterlikli üyeyle üst etiketin gerekçesi yoktu | Kritik | Ölçülmemiş üyeler güvence sürecinin parçası sayılır |
| Fiyat politikasıyla yeni eşit-katkı kararı arasında açık değişiklik kaydı yok | Yüksek | Eski karar sessizce silinebilir |

## 1.3. Güncel depo incelemesi

Dal uçları yeniden doğrulandı:

| Dal | Commit SHA |
|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` |

İncelenen belge sürümleri:

| Belge | Git blob SHA |
|---|---|
| Tasarım belgesi | `a509f1287726fe8922b0d7a46fbf18e5b4d55896` |
| Faz 1 planı | `8bed859fe37cd80dc1500fb92b9dcdeeabe1b741` |
| Yol haritası | `97afa66e18678bf43b758bd6ced844e46fd949e9` |
| Araştırma notları | `a27db81739851ac17bc9afbd85b82368ad357cff` |

Depo uçları önceki turdan değişmemiş. Yeni brief de sahip kararlarının henüz tasarım belgesine işlenmediğini açıkça söylüyor. Bu nedenle dört kategori ve yeterlik kararları ile GitHub’daki eski üç kategorili sözleşme arasında belge senkronizasyonu gerekiyor. [concepts_brief.md]

İnceleme sınırı korunuyor: Uzun tasarım ve Faz 1 dosyaları araçta kesiliyor. Görülen hükümler, yol haritası ve araştırma notları incelendi; kesilen bütün paragrafların eksiksiz satır denetimi yapılmış sayılmıyor. Planlanan testler çalıştırılmadı, model çağrısı yapılmadı, depo değiştirilmedi.

***

# II — Yeni bilimsel bulgular

## 2.1. GSM-Symbolic neyi gösteriyor, neyi göstermiyor?

İncelenen sürüm: Mirzadeh ve arkadaşları, `arXiv:2410.05229v2`.

Çalışma:

- GSM8K’den 100 şablon oluşturuyor.
- Her şablondan 50 örnek üreterek farklı gerçekleştirimler üzerindeki başarı değişimini inceliyor.
- Sayısal değer, özel ad, koşul sayısı ve ilgisiz görünen ek bilgi müdahalelerini ayırıyor.
- Şablonların geçerliliği için otomatik kontroller ve şablon başına rastgele örneklerde insan incelemesi uyguluyor. [arxiv](https://arxiv.org/html/2410.05229v2)

Rigor için desteklediği sonuç:

> Tek sabit problem kümesindeki başarı, aynı muhakeme yapısının farklı sayısal ve dilsel gerçekleştirimlerindeki dayanıklılığı yeterince göstermez.

Desteklemediği sonuçlar:

- Parametrik şablonlar bütün ezberi önler.
- Testi geçen model gerçek mühendislik şartnamelerini doğru yorumlar.
- Belirli bir Rigor modelinin yeterliği bu makaledeki eski model sonuçlarından çıkarılabilir.
- Çalışmanın “LLM’ler gerçek mantıksal muhakeme yapamıyor” yorumu, bütün modeller ve bütün görevler için kanıtlanmış teoremdir.

Brief’teki “%65’ten fazla düşüş” ifadesi de genellenmemeli. Makale belirli model ve GSM-NoOp deneyleri için çok büyük düşüş bildiriyor; bu, her modelin her ilgisiz cümlede aynı ölçüde bozulduğu anlamına gelmiyor. [arxiv](https://arxiv.org/html/2410.05229v2)

## 2.2. LiveBench’in güncel adı bile önemli bir düzeltme içeriyor

İncelenen `arXiv:2406.19314v2` başlığı “Contamination-Limited”dır; “contamination-free” iddiasından daha sınırlıdır.

Yöntem:

- Güncel kaynaklardan yeni sorular.
- Nesnel referans cevaplarla otomatik değerlendirme.
- Düzenli yenileme.
- İncelenen planda soruların yaklaşık altıda birinin her güncellemede değiştirilmesi.
- Yeni soruların bir süre özel tutulup sonra yayımlanması.
- Kategori bazında sonuçlar ve açık yeniden üretim kayıtları. [arxiv](https://arxiv.org/html/2406.19314v2)

Ancak Rigor’a doğrudan alınmaması gereken bir özellik var: LiveBench bazı görevlerde modelden bilmediğinde en iyi tahminini vermesini istiyor. Rigor’un eksik parametrede soru sorma hedefi bununla aynı değil. Bu nedenle LiveBench puanı Rigor yeterliği yerine geçemez. [arxiv](https://arxiv.org/html/2406.19314v2)

Rigor açısından alınacak olan, benchmark’ın görevleri değil; yenileme, referans kalitesi, kategori ayrımı ve açık değerlendirme yöntemidir.

## 2.3. Parametrik üretim, şablon ailesine aşırı uyumu ortadan kaldırmaz

ConStat çalışması üç farklı genelleme sorununu ayırıyor:

1. Aynı örneğin yeniden ifade edilmiş biçimine genelleme.
2. Aynı dağılımdan yeni örneklere genelleme.
3. Aynı görevi ölçen başka benchmark’a genelleme.

Çalışma, yalnızca yeniden ifade etmenin bazı kontaminasyon biçimlerini ortaya çıkarmaya yetmediğini; benchmark zorluğunun da karşılaştırmada düzeltilmesi gerektiğini gösteriyor. [arxiv](https://arxiv.org/html/2405.16281)

Bu nedenle brief’teki iki ifade düzeltilmelidir:

- “Depoda sızacak cevap anahtarı olmaz”: Fazla güçlüdür. Açık şablon ve referans IR, cevap üretme kuralını zaten açığa çıkarır.
- “Açık ve gizli başarı farkı ezberin göstergesidir”: Tek başına yeterli değildir. Gizli küme daha zor, daha uzun veya farklı alanlı olabilir.

ConStat’ın kendisi de referans model ve referans benchmark seçimine dayanır; onun testini çalıştırmak bütün kontaminasyonu dışlamaz. [arxiv](https://arxiv.org/html/2405.16281)

## 2.4. Gizli set tekrar kullanıldıkça kendisi de geliştirme verisine dönüşebilir

Dwork ve arkadaşlarının adaptif veri analizi çalışmaları, bir holdout kümesinin sonuçlara bakılarak tekrar tekrar kullanılmasıyla aşırı uyum oluşabileceğini gösterir. Sorular gizli kalsa bile prompt, model ve eşik seçimleri gizli sonuçlara göre ayarlanıyorsa bağımsız son değerlendirme bozulabilir. [arxiv](https://arxiv.org/html/1506.02629)

Rigor için sonuç:

- Geliştirme seti ile kabul seti ayrılmalı.
- Kabul başarısızlıkları görüldükten sonra yapılan düzeltme yeni bir kabul çalıştırması gerektirir.
- Aynı gizli kümeyi sınırsız tekrar kullanıp yalnızca en iyi sonucu saklamak yasak olmalı.
- v1’de karmaşık diferansiyel mahremiyetli holdout altyapısı şart değil; yeni kabul kümeleri ve bütün denemelerin kaydı daha uygulanabilir.

## 2.5. Bireysel yeterlik, ortak hatayı ölçmez

Kim ve arkadaşlarının geniş model çalışması, farklı aile ve sağlayıcılarda da ortak yanlış cevaplar bulunduğunu gösteriyor. Bununla birlikte yöntem esas olarak çoktan seçmeli cevaplar ve özgeçmiş değerlendirmeleri üzerine kurulu; Rigor’un açık uçlu formalizasyon heyetine doğrudan hata oranı vermez. [arxiv](https://arxiv.org/html/2506.07962v1)

Rigor’a aktarılabilen sonuç:

> Ortak hata ölçülmelidir; yalnızca aile adından hesaplanmamalıdır.

Aktarılamayan sonuç:

> Üç modelin her birinin hata oranı \(p\) ise heyetin hata oranı \(p^3\) olur.

Bu çarpım, gerekli bağımsızlık varsayımı olmadan kullanılamaz.

## 2.6. Düşünme bütçesi yeterlik anahtarının parçasıdır

Snell ve arkadaşlarının test-time compute çalışması, daha fazla hesaplamanın etkisinin görev zorluğuna, kullanılan yönteme ve temel modele bağlı olduğunu gösterir. Bazı arama düzenlerinde daha fazla hesaplama, doğrulayıcının hatalı sinyallerine aşırı optimizasyon nedeniyle performansı azaltabilir. [arxiv](https://arxiv.org/html/2408.03314v1)

Bundan şu sınırlı sonuç çıkar:

- Model kimliği tek başına yeterlik nesnesi değildir.
- Düşünme bütçesi ve çıktı sınırı kaydedilmelidir.
- Daha yüksek ayarda geçmenin daha düşük ayara taşınması uygun değildir.
- Daha düşük ayarda geçmenin daha yüksek ayara otomatik taşınması da ölçülmüş bir monotonluk ilişkisi değildir.

Bu makale güncel sağlayıcıların `low/medium/high` ayarlarını bire bir karşılaştırmıyor. Ortak beş seviyeli evrensel ölçek için dayanak oluşturmuyor.

***

# III — Model yeterliği ölçüm tasarımı

## 3.1. Ölçülen nesne “model” değil, formülasyon yapılandırmasıdır

Önerilen yeterlik nesnesi:

> Belirli model kimliği + erişim yolu + sağlayıcı + çağrı ayarları + Rigor formülasyon prompt’u/adaptörü + görev kapsamı + dil.

Örneğin “Model X yeterli” yerine:

> “Bu modelin bu erişim ve çağrı yapılandırması, Türkçe doğrusal kaynak tahsisi problemlerini IR’a çevirme profilinin v3 kabul testini geçti.”

Bu, modelin bütün matematiğe yeterli olduğu iddiasını önler.

## 3.2. Tek genel puan kullanılmamalı

Ortak bir altyapı kurulabilir; fakat yeterlik kapsamları ayrılmalı:

| Profil | Öncelikli hata türleri |
|---|---|
| Birimler ve nicelik çıkarımı | Standart seçimi, ölçek, ofset, ölçüm–tam değer ayrımı |
| Cebir ve eşitsizlik formülasyonu | Alan, işaret, niceleme, en az/en fazla |
| Mantık ve kısıt sistemleri | İmplication yönü, bütünlük, çelişki, eksik koşul |
| Optimizasyon | Amaç, uygulanabilirlik, tamsayılılık, sınırlar, reformülasyon |
| Mühendislik model bağlama | Referans çerçevesi, model seçimi, geçerlilik aralığı |
| Finansal hesaplama | Zaman bazı, para/varlık birimi, yuvarlama sırası, oran tanımı |

Dil de kapsamdır. İngilizce profili geçen model Türkçe profili geçmiş sayılmamalıdır.

Birleşik profil mümkün olabilir; fakat alt profil sonuçları ayrıca verilmelidir. “300 soruda geçti” denilerek 15 optimizasyon sorusundan optimizasyon yeterliği çıkarılamaz.

## 3.3. Matematiksel işlem ile formülasyonu ayırma

Formülatöre mümkün olduğunca şu çıktı sözleşmesi verilmeli:

- `FORMULATE`: Kaynak destekli IR.
- `ASK`: Hangi sonuç değiştirici bilgi eksik?
- `REFUSE_UNSUPPORTED`: Hangi yapı destek dışında?
- Her nicelik ve kısıt için kaynak eşlemesi.

Son sayının doğruluğu tek başına geçme ölçütü olmamalıdır.

Örnek: `en az` yerine `en fazla` yazan iki formül, belirli verilerde aynı sayıyı verebilir. Noktasal cevap kontrolü bu hatayı kaçırır.

Formülasyon değerlendirmesi:

1. Şema ve alan geçerliliği.
2. Nicelik/kısıt tamlığı.
3. Birim ve referans eşlemesi.
4. Referans formalizasyona uygun denklik.
5. Gerektiğinde karşı örnek.
6. Eksik bilgiye doğru tepki.

## 3.4. Soru sorma davranışının puanlanması

| Gerçek durum | Model davranışı | Değerlendirme |
|---|---|---|
| Problem tam | Doğru IR | Başarılı formülasyon |
| Problem tam | Gereksiz soru | Güvenli ama kullanışlılık kaybı |
| Problem eksik | Eksikliği doğru bulup soru | Başarılı güvenlik davranışı |
| Problem eksik | Eksik bilgiyi uydurup IR | Kritik hata |
| Problem destek dışında | Açık destek sınırı | Başarılı kapsam davranışı |
| Problem destek dışında | Destek varmış gibi çözüm | Kritik hata |
| Değerlendirici kararsız | Herhangi | Otomatik geçme/kalma değil; değerlendirme eksik |

Modelin kendi “eminim” ifadesine göre hata ağırlığı verilmemeli. Esas ölçüt, yanlış formülü nihai kullanılabilir aday olarak sunup sunmadığıdır.

## 3.5. Kritik hata tanımı önceden dondurulmalı

Önerilen kritik hata sınıfları:

- Kaynakta bulunmayan sonuç değiştirici varsayım.
- Eşitsizlik/amaç yönünün değişmesi.
- Birim, alan veya referans çerçevesi hatası.
- Zorunlu kısıtın atlanması.
- Eksik parametreyi sessiz doldurma.
- Desteklenmeyen yapı için doğrulanmışmış gibi aday üretme.
- Kaynak kapsamını değiştirerek denklik elde etme.

Şema biçim hatası her zaman kritik semantik hata değildir. Ancak görev tamamlanmamış sayılır. API kotası veya ağ hatası da modelin matematiksel hatası değildir; testin tamamlanmasını engeller.

## 3.6. Önerilen test paketi

TASARIM TERCİHİ — başlangıç kabul paketi:

| Bileşen | İstem sayısı | Amaç |
|---|---:|---|
| Ana ölçüm | 300 | Tanımlı profil dağılımında formülasyon ve doğru eylem |
| Eşli/metamorfik ekler | 60 | Anlam değişimi ve anlam korunumu duyarlılığı |
| Bağımsız gerçek-dünya/adversarial küme | 40 | Şablon dışına aktarım |
| Toplam | 400 | Profil başına kabul çalıştırması |

Önce ayrı bir 50 soruluk pilot öneriyorum. Pilot hata ayıklama ve aday eleme içindir; kabul kaydına yeterli sayılmamalıdır.

Ana ölçümün başlangıç dağılımı:

- %70 tam tanımlı problemler.
- %20 eksik/belirsiz problemler.
- %10 destek dışı veya yanlış görev türü.

Bu oranlar bilimsel standart değildir. Kullanım verisi elde edilince değiştirilmelidir. Tam belirli sayılarda tabakalı örnekleme yapılırsa istatistikler tabakaya göre hesaplanmalı; bütün sorular otomatik olarak tek özdeş Bernoulli örneği sayılmamalıdır.

Altmış ek istem, ana kümedeki bazı problemlerin türevleri olabilir. Bunlar 60 yeni bağımsız problem ailesi gibi sayılmaz.

## 3.7. Başlangıç geçme kriteri

Önerim:

1. Dört yüz istemin tamamında, referansı doğrulanmış sıfır kritik semantik hata.
2. Ana testte tam tanımlı problemler için doğru IR üretme oranının tek taraflı %95 alt güven sınırı en az %80.
3. Eksik/belirsiz problemlerde doğru açıklama isteme oranının tek taraflı %95 alt sınırı en az %90.
4. Destek dışı sentinel görevlerde sessiz destek iddiası yok.
5. Eşli testlerde anlam değiştiren mutasyonun gözden kaçması veya anlam koruyan mutasyonda kritik sapma yok.
6. Açıklanamayan değerlendirme/altyapı eksikleri varken `PASS` yok.

Buradaki %80 ve %90 eşikleri “matematiksel güven oranı” değildir. İlki her şeye soru soran modelin geçmesini, ikincisi eksik problemde tahmin üretmenin normalleşmesini engelleyen başlangıç kullanılabilirlik/güvenlik hedefleridir. Bu değerlerin Rigor için optimum olduğunu gösteren deney yoktur; sahip onayı gerekir.

Örneğin tek tek %95 alt sınırlar kullanıldığında:

- 210 tam problemde en az 178 doğru IR, %80 alt sınır koşulunu sağlar.
- 60 belirsiz problemde en az 59 doğru soru, %90 alt sınır koşulunu sağlar.

Bunlar ayrı koşulların örnek hesaplarıdır; bütün kriterlerin birlikte %95 güvenle doğrulandığı anlamına gelmez.

## 3.8. Sıfır hata istatistiği

Sabit yapılandırma ve dağılım altında, bağımsız ve özdeş Bernoulli denemeleri varsayımıyla sıfır gözlenen hata için tek taraflı %95 üst sınır:

\[
p_U=1-0{,}05^{1/n}.
\]

Bu, \(3/n\) yaklaşımının tam binom karşılığıdır. NIST, özellikle küçük örneklem veya az hata durumunda binom dağılımına dayalı sınırların kullanımını açıklar. [itl.nist](https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbici.htm)

Araştırma kapsamında hesaplanan değerler:

| Bağımsız deneme | Gözlenen hata | Tek taraflı %95 üst sınır |
|---:|---:|---:|
| 30 | 0 | %9,503 |
| 50 | 0 | %5,816 |
| 100 | 0 | %2,951 |
| 200 | 0 | %1,487 |
| 300 | 0 | %0,994 |
| 500 | 0 | %0,597 |
| 1.000 | 0 | %0,299 |
| 3.000 | 0 | %0,100 |

Bu tablo:

- “Modelin gerçek hata oranı kesin bu değerin altında” demez.
- Vaka başına güven yüzdesi değildir.
- Yeni mühendislik dağılımına otomatik taşınmaz.
- Aynı şablonun yüzlerce varyantını bağımsız yeni şablon ailesi saymaya izin vermez.

Üç yüz soru önerisinin gerekçesi, ideal varsayımlarda yaklaşık %1 düzeyindeki hatayı ayırt etmeye başlayan makul bir tarama bütçesi olmasıdır. Bu, %1 formülasyon hatasının roket veya finans kullanımı için kabul edilebilir olduğu anlamına gelmez. Yeterlik yalnızca üyelik önkoşuludur; vaka kontrollerinin yerine geçmez.

### Sıfırdan fazla hata

| Sonuç | Tek taraflı %95 üst hata sınırı |
|---|---:|
| 1/100 | %4,656 |
| 1/300 | %1,571 |
| 3/300 | %2,564 |
| 5/300 | %3,472 |
| 1/1.000 | %0,473 |

Bu değerler kritik hata toleransını artırma önerisi değildir; gözlenen hata sayısı ile istatistiksel belirsizliğin ilişkisini gösterir.

### Daha sıkı iddiaların maliyeti

Sıfır hatayla şu üst sınırlara ulaşmak için gereken yaklaşık değil, hesaplanmış asgari örneklemler:

| Hedef üst hata sınırı | Gerekli \(n\), tek taraflı %95 |
|---:|---:|
| %5 | 59 |
| %2 | 149 |
| %1 | 299 |
| %0,1 | 2.995 |
| %0,01 | 29.956 |

Bunlar da aynı örnekleme varsayımlarına bağlıdır.

## 3.9. Sıfır toleransın yanlış ret maliyeti

Üç yüz denemede sıfır hata şartının geçilme olasılığı:

| Varsayımsal gerçek hata oranı | Testten sıfır hatayla geçme olasılığı |
|---:|---:|
| %0,1 | %74,07 |
| %0,5 | %22,23 |
| %1 | %4,90 |
| %2 | %0,233 |
| %5 | Yaklaşık %0,000021 |

Dolayısıyla sıfır tolerans, çok düşük ama sıfır olmayan hata oranına sahip modelleri de sıklıkla eler. Bu bilinçli muhafazakârlıktır; “başarısız olduysa model genelde kötüdür” sonucu değildir.

Geçmeyen modeli geçirmek için aynı testi farklı tohumlarla tekrar edip yalnızca başarılı denemeyi saklamak yasak olmalıdır. Adaptif tekrarlar klasik tek-test güven yorumunu bozar. [arxiv](https://arxiv.org/html/1506.02629)

## 3.10. Çoklu model ve profil ölçümleri

Üç modelin her birine ayrı %95 sınır vermek, üçünün birlikte %95 güvenle aynı sınır altında olduğunu göstermez.

Örneğin Bonferroni ile üç iddia için toplam %95 kapsama hedeflenirse:

- Her biri 300 sıfır hatalı testte üst sınır yaklaşık %1,356 olur.
- Her birinde %1 üst sınıra ulaşmak için 408 sıfır hatalı deneme gerekir.

Otuz yapılandırmada aynı toplu iddia için gereken sayı 637’ye çıkar.

Rigor’un v1’de bütün bu kombinasyonlara tek bir istatistiksel “güvenilir model listesi” iddiası vermesini önermiyorum. Her ölçümün sınırı ayrı verilmeli; toplu garanti iddiası yapılacaksa çoklu karşılaştırma açıkça ele alınmalıdır.

İstatistik tablolarının hesap ayrıntıları CSV hesap ekinde sunulmuştur; bunlar model deney sonucu değil, örneklem tasarımı hesaplarıdır.

***

# IV — Yeterlik kayıt sistemi

## 4.1. Dosya kullanılmalı mı?

Evet. Ancak iki nesne ayrılmalıdır:

1. Ölçüm kanıt paketi.
2. Bu paket üzerinden hesaplanan yeterlik kararı.

Dosyada yalnızca `qualified: true` bulunması yeterli değildir.

Önerilen kayıt grupları:

| Grup | İçerik |
|---|---|
| Kimlik | İstenen model, dönen model, varsa snapshot/revision, sağlayıcı |
| Erişim | Doğrudan API/CLI/toplayıcı, endpoint ve adaptör sürümü |
| Yapılandırma | Sağlayıcının özgün düşünme ayarı, çıktı sınırı, sampling, araç/bellek durumu |
| Yerel model | Ağırlık ve tokenizer kimliği/hash’i, quantization, runtime |
| Görev kapsamı | Rol, dil, problem türü, uzunluk ve destek sınırları |
| Test | Test/generator/reference/evaluator sürümü, tohum, örnek listesi |
| Sonuç | Hata türleri, pay/payda, aralıklar, eksik çağrılar, bütün denemeler |
| Köken | Kim/nerede/hangi komut ve kod sürümüyle çalıştırdı |
| Geçerlilik | Başlangıç, son tarih, iptal nedeni, bağlı politika sürümü |
| Kanıt | Ham istem/çıktı özetleri ve erişilebilir denetim kayıtları |

Fiyat ve kota kaydedilebilir; yeterlik anahtarının matematiksel kısmı değildir. Ancak ücretsiz plan daha düşük çıktı sınırı veya farklı model yolu uyguluyorsa bu fark yapılandırmaya yansır.

## 4.2. Model kimliğinin güven kaynağı

Tercih sırası:

- Yerel modelde ağırlık/tokenizer dosyalarının doğrudan kimliği.
- Sağlayıcının belgelenmiş snapshot/revision kimliği.
- Dönen model ve provider metadatası.
- İstenen alias.

Bunlar aynı kanıt gücünde değildir.

Uzak API’nin döndürdüğü model adı, ağırlıkların bağımsız kriptografik kanıtı değildir. Alias aynı kalırken model değişirse bunu kesin olarak tespit eden genel bir istemci yöntemi yoktur. Kayıt bu sınırı saklamamalıdır.

Davranışsal sentinel testleri bazı değişimleri gösterebilir; geçmeleri değişim olmadığını kanıtlamaz.

## 4.3. Sağlayıcıya özgü düşünme ayarları

Ortak bir `low < medium < high < xhigh < max` semantiği varsayılmamalı.

Kaydedilecekler:

- Sağlayıcının gerçek parametre adı.
- Gönderilen özgün değer.
- Varsa reasoning token bütçesi.
- Maksimum çıktı.
- Sağlayıcının döndürdüğü kullanım/ayar bilgisi.
- Varsayılan kullanıldıysa “varsayılan” olduğu ve ölçüm tarihi.

Bir adaptör desteklenmeyen düşünme ayarını sessizce yok sayıyorsa o yapılandırma eşleşmiş sayılmamalıdır.

Brief’teki yerel istemci/model tablosunu bu oturumda sahibin makinesinde doğrulamadım. Belge içi ortam kaydı olarak ele alıyorum; bu modellerin çağrıldığını veya yeterli bulunduğunu söylemiyorum. [concepts_brief.md]

## 4.4. `rigor qualify` nasıl doğrulanabilir?

Komutun ürettiği paket:

1. Sabit test planını kaydeder.
2. Bütün planlanan çağrıları ve sonuçlarını listeler.
3. Ham çıktıları değerlendirme sonucundan ayırır.
4. Referans ve evaluator sürümlerini bağlar.
5. Sonuçları yeniden puanlamaya izin verir.
6. Yeterlik kararını kabul politikasından yeniden türetir.
7. Eksik veya başarısız girişimleri gizlemez.

“Replay” iki anlama ayrılmalı:

- Saklanan çıktıyı yeniden puanlamak: İyi tasarlanırsa deterministik olabilir.
- Modeli yeniden çağırmak: Aynı tohumda bile uzak hizmet ve model değişimleri nedeniyle aynı çıktıyı garanti etmez.

## 4.5. Tehdit modeli

| Saldırgan/arıza | Hedeflenen güvence |
|---|---|
| Yanlışlıkla dosya düzenleme | Hash ve şema kontrolüyle tespit |
| Ajanın sahte kayıt göndermesi | Ajan beyanı yeterlik sayılmaz; güvenilen kayıt deposu |
| Ajanın kayıt dizinine yazabilmesi | Yetki ayrımı veya imza gerekir; yalnızca komut adı yetmez |
| İndirilen kaydın değiştirilmesi | Güvenilen imza/attestation doğrulaması |
| Eski imzalı kaydın geri getirilmesi | Süre, iptal ve politika sürümü kontrolü |
| Sağlayıcının aynı kimlikte model değiştirmesi | Kısmen sentinel/yeniden ölçüm; tam dışlama yok |
| Bakımcının yanlış veya seçilmiş sonuç yayımlaması | Şeffaf paket ve bağımsız tekrar; imza bunu düzeltmez |
| Tam yetkili yerel saldırgan | Değiştirilmiş Rigor’un dürüst etiket vereceği garanti edilemez |

### Hash, imza ve append-only log ne sağlar?

- Hash: İçerik kimliği; tek başına köken veya doğruluk değil.
- Dijital imza: Güvenilen anahtarla köken/bütünlük; testin doğru yapıldığını göstermez.
- Yerel append-only log: Kazaya ve basit bozulmaya karşı yararlı; aynı yetkili saldırganın yeniden yazmasını tek başına engellemez.
- Haricî şeffaflık kaydı: Silme/değiştirmeyi daha görünür kılabilir; v1 için zorunlu değil.
- Yeniden puanlanabilir paket: Sonuç hesabını denetlemeyi sağlar; uzak modelin gerçekten o olduğu yine hizmet güvenine bağlıdır.

GitHub’ın kendi attestation belgesi de köken kanıtının artefaktın güvenli olduğu garantisi olmadığını açıkça belirtir. [docs.github](https://docs.github.com/en/actions/concepts/security/artifact-attestations)

## 4.6. Bakımcı ve yerel kayıt ayrımı

Önerilen iki katman:

- Dağıtımla gelen, doğrulanabilir bakımcı kayıt paketi.
- Kullanıcının güvenilen yerel evaluator süreciyle oluşturduğu kayıt paketi.

Yerel kayıt otomatik olarak bilimsel bakımdan daha zayıf değildir. Aynı ölçümü daha güncel erişim yolunda yapmış olabilir. Fark köken ve güven varsayımıdır.

Rapor şu ayrımı göstermeli:

> “Bu yeterlik kaydı bakımcı tarafından dağıtıldı.”

veya

> “Bu yeterlik kaydı bu makinede yapılan ölçümden türetildi; dışarıdan bağımsız olarak doğrulanmış yürütme kökeni yok.”

Normal çağıran ajan, yerel kayıt ekleme veya güven politikasını değiştirme yetkisine sahip olmamalı. Ancak aynı kullanıcı hesabında tam shell erişimi verilen ajan için bunun yalnızca uygulama içi yasaklarla sağlanamayacağı belirtilmelidir.

## 4.7. Süre ve yeniden ölçüm

TASARIM TERCİHİ — başlangıç varsayılanı:

- 30 gün tam yeterlik geçerliliği.
- Bilinen model/snapshot, quantization, sağlayıcı, erişim yolu, düşünme ayarı, prompt veya evaluator değişikliğinde derhâl eşleşme iptali.
- Sürüm sabitlenemeyen uzak modellerde haftalık küçük sentinel paketi.
- Sentinel geçişi 30 günlük süreyi uzatmaz.
- Kritik sentinel hatası ilgili kaydı askıya alır ve tam yeniden ölçüm gerektirir.
- Yalnızca stil/byte değişimi model değişimi kanıtı sayılmaz.

Otuz günün bilimsel olarak doğru süre olduğunu gösteren genel kanıt yoktur. Bu, fark edilmeyen değişime maruz kalma süresiyle ölçüm maliyeti arasında muhafazakâr operasyonel tercihtir. Daha sonra sağlayıcı bazında gözlenen değişim ve başarısızlık verisiyle güncellenmelidir.

***

# V — Ezber ve benchmark güvenliği

## 5.1. Yöntemlerin karşılaştırılması

| Yöntem | Gücü | Sınırı | Rigor’daki rolü |
|---|---|---|---|
| Statik açık set | Hata ayıklama ve tekrar üretim | Ezber/aşırı uyum | Geliştirme |
| Parametrik üretim | Doğrudan cevap ezberini azaltır | Şablon ailesi öğrenilebilir | Ana ölçümün bir parçası |
| Dilsel/metamorfik dönüşüm | Anlam korunumu dayanıklılığı | Dönüşüm anlamı bozabilir | Eşli kontrol |
| Karşıt çift | İnce koşula duyarlılık | Sadece seçilen hata türlerini ölçer | Zorunlu |
| Adversarial set | Bilinen tehlikeli hatalara odaklanır | Gerçek frekansı temsil etmez | Zorunlu stres kapısı |
| Gizli aileler | Açık şablona uyumu sınar | Bakımcıya güven ve sızıntı | Kabul payı |
| Gerçek şartname/iş kaydı | Ekolojik geçerlilik | Pahalı ve referansı zor | Zorunlu aktarım kontrolü |
| Zamansal yenileme | Eski set etkisini azaltır | Tüm kontaminasyonu dışlamaz | Sürekli bakım |

Bu kombinasyonun dayanağı GSM-Symbolic’in varyasyon bulguları, LiveBench’in yenileme yaklaşımı ve ConStat’ın farklı genelleme katmanlarını ayırmasıdır. [arxiv](https://arxiv.org/html/2410.05229v2)

## 5.2. Referans formalizasyonun kendisi nasıl denetlenmeli?

“IR’dan metin üretildi, doğru cevap yapım gereği bilinir” ancak üreticinin doğru olduğu koşuluyla doğrudur.

Önerilen süreç:

1. Şablonun amaçlanan semantiği yazılır.
2. Referans IR bağımsız ikinci incelemeden geçer.
3. Sayısal/alan koşulları generator’da korunur.
4. Metin örnekleri insan tarafından kontrol edilir.
5. Hatalı IR mutasyonlarının evaluator tarafından reddedildiği sınanır.
6. LLM üretici veya paraphraser kullanıldıysa onun metni de referansla karşılaştırılır.
7. Aynı renderer’dan üretilen bütün metinlerin başarıyla geri çevrilmesi, bağımsız doğal dil yeterliği kanıtı sayılmaz.

Örneğin rastgele sayı değişimi bölünebilirliği, tekliği veya fiziksel geçerliliği bozabilir. Cümle sırasını değiştirmek zamansal işlem sırasını değiştirebilir. “Alakasız” cümle gerçekte model seçimini etkileyebilir.

GSM-Symbolic’in şablonlarda alan koşulları ve insan incelemesi kullanması, rastgele değiştirme işleminin kontrolsüz yapılmadığını gösterir. [arxiv](https://arxiv.org/html/2410.05229v2)

## 5.3. Açık–gizli farkının doğru yorumu

Fark bulunursa önce şu sorular sorulmalıdır:

- Zorluk eşlenmiş mi?
- Aynı dil ve uzunluk aralığı mı?
- Aynı problem türü mü?
- Açık sorular geliştirme sırasında kullanılmış mı?
- Referans hatası var mı?
- Model yalnızca belirli çıktı biçiminde mi başarısız?
- Gizli setin aileleri gerçekten yeni mi?

Tek başına fark, eğitim verisine sızıntının ispatı değildir. ConStat’ın zorluk düzeltmesi ve referans modellere ihtiyaç duyması tam bu nedenle önemlidir. [arxiv](https://arxiv.org/html/2405.16281)

## 5.4. Gizli test bakımcısının güven sorunu

Gizli seti bakımcının kontrol etmesi yeni bir güven bağı oluşturur. Çözüm seti tamamen gizlemek değil, denetim düzeylerini ayırmaktır:

- Test planı, rubrik ve dağılım açık.
- Gizli örneklerin bütünlüğü önceden taahhüt edilir.
- Sorular gecikmeli yayımlanır veya bağımsız denetçiye açılır.
- Bütün denemeler ve başarısızlıklar saklanır.
- Üçüncü taraflar aynı generator ve evaluator ile kendi bağımsız kabul kümelerini üretebilir.

Bir hash taahhüdü, bakımcının kümeyi sonradan değiştirmediğini destekler; kümeyi adil seçtiğini kanıtlamaz. Ayrıca küçük ve tahmin edilebilir özel kümelerde doğrudan örnek hash’leri bilgi sızdırabilir; yayımlanan taahhüdün biçimi dikkatle seçilmelidir.

## 5.5. Önerilen zorunlu kombinasyon

Her yeterlik paketinde:

- Açık geliştirme kümesinden ayrı kabul örnekleri.
- Sayısal ve birim varyasyonları.
- Anlam değiştiren karşıt çiftler.
- Anlam koruyan dilsel/metamorfik örnekler.
- Eksik bilgi ve destek dışı örnekler.
- En az bir şablon-aile dışı/gizli pay.
- Bağımsız yazılmış gerçek-dünya problemleri.
- Sürümlü referans ve evaluator.
- Tekrarlı kabul denemelerinin tamamının kaydı.

Bu, ezberi azaltan uygulanabilir kombinasyondur; “kontaminasyonsuz” garantisi değildir.

***

# VI — Karma heyet karar matrisi

## 6.1. Seçenekler

| Seçenek | Güvenlik ve kanıt | Kullanıcı/ücretsiz erişim | Maliyet ve bakım | Ana risk |
|---|---|---|---|---|
| A — Bir yeterlikli üye | İki zorunlu üyenin yeterliği bilinmiyor | En erişilebilir | Düşük | Üst süreçte ölçülmemiş iki bileşen |
| B — İki yeterlikli üye | İki ölçülmüş aile mümkün | Orta erişilebilir | Orta | Üçüncü üye filtre etkisi ve kapsamı belirsiz |
| C — Üç yeterlikli üye | Bütün zorunlu üyeler için ölçüm var | Erişim zorlaşabilir | Daha yüksek | Ortak hata yine mümkün |
| D — Heyet yeterliği | Ortak hata ve pipeline etkisini doğrudan ölçer | Hazır heyetlerle yönetilebilir | Ek değerlendirme | Bireysel kapsam yerine geçirilirse yeni kombinasyonlar belirsiz |
| E — Uyarlanabilir | Göreve göre maliyet azaltılabilir | Esnek | Karmaşık politika | Riski yanlış sınıflayıp güven koşulunu gevşetme |

Önerim C+D’dir: üç bireysel kayıt ve ayrıca heyet düzeyinde ölçüm.

E yaklaşımı daha sonra düşünülebilir; ilk sürümde risk sınıflandırıcısı ekleyerek güven tabanını büyütmek istemiyorum.

## 6.2. Neden varsayılan üç?

Mühendislik gerekçeleri:

- “Üç üyeli yeterliği denetlenmiş heyet” ifadesi gerçekten bütün üyeler için geçerli olur.
- Üçüncü modelin görevi, veri yolu ve ayarı belirsiz bırakılmaz.
- Yerine model koyma ve model sürümü değişimi daha açık yönetilir.
- Yeterliksiz üyeyi doğru cevap verdiği tek örneğe bakarak yeterli sayma hatası önlenir.
- Güçlü ücretsiz üye de aynı koşullarla katkı verebilir.

Fakat bu, iki kayıtlı üye + ölçülmemiş üçüncü üyeden her durumda daha düşük ortak hata üreteceğine dair teorem değildir.

### Önemli karşı örnek

İlk iki modelin oybirliğiyle kabul ettiği 1.000 örneğin 900’ü doğru, 100’ü yanlış olsun. Üçüncü model bütün 100 yanlış adayı, fakat yalnızca 90 doğru adayı kabul etsin.

- Yanlış kabul sayısı 100’den artmaz.
- Fakat yayımlanan 190 sonuç içindeki yanlışlık oranı %52,6’ya çıkar.

Bu, açıklayıcı yapay bir örnektir; ölçülmüş Rigor sonucu değildir.

Dolayısıyla ek oybirliği filtresi, yanlış sonuç kümesini küçültebilirken yayımlanan sonuçlardaki koşullu hata oranını kötüleştirebilir. Üçüncü üyenin yeterliği ve ortak hata davranışı bu yüzden ayrı önem taşır.

## 6.3. Bilimsel olarak ne söylenebilir?

- Bireysel yeterlikler ortak hatanın çarpımı değildir.
- Farklı aileler ortak hatayı dışlamaz.
- Üçüncü üye eklemek doğru cevapları gereksiz reddedebilir.
- En iyi üye sayısı görev ve model kombinasyonuna bağlı olabilir.
- Doğrudan Rigor deneyi olmadan “iki yeterlidir” veya “üç güvenlidir” istatistiksel sonucu verilemez. [arxiv](https://arxiv.org/html/2506.07962v1)

Bu belirsizlik altında üç kayıt, üst etiket için en savunulabilir başlangıç denetim şartıdır. Daha sonra B ve C aynı görevlerde, aynı ilk iki model ve aynı kabul politikasıyla karşılaştırılmalıdır.

## 6.4. Yeterliksiz üçüncü üye doğru formülde birleşirse

Varsayılan politika:

- Üç üyeli üst heyetin yeterlik koşulu sağlanmaz.
- Matematiksel sertifika ve diğer yayın koşulları varsa `CERTIFIED` mümkün olabilir.
- Eksik olan “üçüncü üyeye ait geçerli kapsamlı yeterlik kaydı” açıkça yazılır.
- Bu tek doğru vaka, yeterlik kaydının yerine geçmez.

Yeterliksiz model danışman veya deneysel aday olarak çalışabilir; üst heyetin zorunlu üyesi sayılmamalıdır. Onun somut karşı örneği yine incelenir. Yeterliksiz olması, doğru bir itirazın görmezden gelinmesini haklı çıkarmaz.

## 6.5. Bir yeterlikli üye ayrışırsa

Diğer ikisi aynı formülü üretse de çoğunluk kararı verilmez.

- Önce eşleme ve formal denklik kontrol edilir.
- Eşdeğer farklı yazımlar ayrışma sayılmaz.
- Gerçek semantik fark varsa kullanıcıya soru veya karşı örnek sunulur.
- Ücret, yeterlik puanı veya ikiye bir çoğunluk bu farkı otomatik kapatmaz.
- Çözülemeyen ayrışmada `PROVEN` verilmez.

Bu, mevcut ayrışmada soru sorma politikasını korur.

## 6.6. Heyet düzeyinde ek test nasıl yapılmalı?

### Ölçümler

\(A\): Adayların, Rigor eşleme/denklik sürecinde aynı formalizasyonda birleşmesi.

\(E\): Birleşilen formalizasyonun bağımsız referansa göre yanlış olması.

Raporlanacaklar:

\[
P(A),\qquad P(A\cap E),\qquad P(E\mid A).
\]

Sonuncunun paydası yalnızca kabul edilen/uyuşan görevlerdir. Örneğin 300 görevin yalnızca 30’unda oybirliği varsa, sıfır yanlış kabulün koşullu hata sınırı için \(n=300\) değil, \(n=30\) önemlidir.

Ek olarak:

- Ortak atlanan kısıtlar.
- Aynı yanlış birim/referans seçimi.
- Doğru azınlığın varlığı.
- Gereksiz ret.
- Geçerli eşdeğerliklerin reddi.
- Değişken hizalama hatası.
- `UNKNOWN` denklik sonucu.

### Uygulanabilir başlangıç

- Aynı kabul görevlerinde üç modelin kör çıktıları saklanır; bireysel ölçümlerden ortak-hata analizi tekrar çağrı gerektirmeden yapılır.
- İlk heyet kabulünde ayrıca 100 yeni heyet görevi çalıştırılır.
- Heyet yapılandırması, model kayıt kimlikleri, eşleme/denklik sürümü ve retry politikasıyla bağlanır.
- Yeni bir üye veya ayar değişirse eski heyet kaydı otomatik geçmez.

Bu 100 yeni görev, güçlü bir evrensel istatistiksel garanti değildir; bağımsız sistem aktarım kontrolüdür. Kapsama düşükse üst etiketin semantik güvenilirliği hakkında güçlü oran iddiası yapılmamalıdır.

***

# VII — KANITLANDI için önerilen koşullar

Soru 1’in kapandığını kabul ederek dört kategoriyi koruyorum. Yeni öneri, `PROVEN`ın heyet kapısını ayrıntılandırmaktır. [concepts_brief.md]

## 7.1. Önerilen tam koşullar

`PROVEN` için bütün koşullar:

1. Tam iddia ve onaylı problem revizyonu belli.
2. Matematiksel kanıt kabul edilmiş.
3. Kanıtlanan iddia ile raporlanan sonuç eşleşiyor.
4. Üç zorunlu formülatörün her birinin ilgili kapsam için geçerli yeterlik kaydı var.
5. Kayıtlar gerçek çalışma model/yol/ayarlarıyla eşleşiyor.
6. En az iki farklı aile var; tercihen üç farklı aile, fakat aile sayısı bağımsızlık ispatı diye sunulmuyor.
7. Kör aday üretimi ve bağlam izolasyonu koşulları sağlanmış.
8. Adayların gerekli denklik/eşleme kontrolleri tamam.
9. Çözülmemiş kaynak veya formülasyon ayrışması yok.
10. İlgili heyet yapılandırmasının sistem düzeyi kabul kaydı var.
11. Doğrudan kullanıcı onayı ve köken koşulları mevcut politika altında sağlanmış.
12. Eski Karar 5/yeni eşit-katkı kararının açıklaştırılmış politika koşulu sağlanmış.
13. Bilinen model geçersizliği, kaynak çatışması veya rapor bütünlüğü problemi yok.

Yeterlik, bu listedeki yalnızca bazı önkoşulları karşılar. Sertifika, kullanıcı onayı veya vaka incelemesinin yerine geçmez.

## 7.2. Fiyat çelişkisinin dürüst uzlaştırılması

Yeni sahip kararı iki şeyi açıkça söylüyor:

- Yeterlik ölçülecek.
- Güçlü ücretsiz modelin katkısı aynı sayılacak. [concepts_brief.md]

Bundan “ücretsiz yeterlikli üye, ücretli yeterlikli üyeden az sayılmaz” sonucu çıkar.

Fakat şu sonucun bağlayıcı olduğu henüz açık değildir:

> “Üç yeterlikli ücretsiz üyeden oluşan heyet artık üst etiketi alabilir.”

Çünkü eski Karar 5 bunu yasaklıyor; brief’teki bu yasağı yeterlik şartına dönüştürme metni tasarımcı yorumu olarak işaretli. [concepts_brief.md]

Önerdiğim açık değişiklik:

> Karar 5’in yeni sözleşmesi: `KANITLANDI` için gerekli bütün üyelerin görev kapsamına uygun, geçerli yeterlik kaydı bulunmalıdır. Erişimin ücretli veya ücretsiz olması tek başına yeterliği artırmaz veya azaltmaz. Kota ve erişilebilirlik ayrıca raporlanır.

Bu yeni metin onaylanırsa tamamen ücretsiz ama yeterlikli heyet `PROVEN`a ulaşabilir. Onaylanmadan eski ücretsiz-only engeli sessizce kaldırılmamalıdır.

## 7.3. Kota ve kesilmiş çıktı

Kota düşükse:

- Bekleme veya tamamlanamama oluşur.
- Başka modele sessiz geçiş yapılmaz.
- Kesilmiş çıktı geçerli aday sayılmaz.
- Tamamlanmamış heyet tam heyet sayılmaz.

Aynı gerçek model ve çalışma koşullarında daha düşük kota, kabul edilmiş bir matematiksel kanıtı zayıflatmaz. Ancak plan değişikliği model, reasoning veya çıktı sınırını da değiştiriyorsa yeni yapılandırmadır.

## 7.4. Özet kutusunda yeterlik nasıl ifade edilmeli?

Önerilen satır:

> Problem incelemesi: Bu görev kapsamında ölçülmüş üç yapılandırma, birbirlerinin adaylarını görmeden formülasyon üretti; eşleme ve denklik kontrolleri tamamlandı. Yeterlik kayıtları tarihli test sonuçlarıdır, bu yorumun hatasızlığının kanıtı değildir.

“Üç onaylı yapay zekâ sonucu doğruladı” ifadesi kullanılmamalıdır.

Yeterlik eksikse:

> Problem incelemesi: Üçüncü üyenin bu görev ve erişim ayarları için geçerli yeterlik kaydı yok; tam heyet koşulu sağlanmadı.

Gerçekleşmeyen test, onay veya heyet olayı kutuya yazılmaz.

***

# VIII — Açık çelişkiler ve kalan riskler

## 8.1. Adversarial senaryolar

| Senaryo | Sistem davranışı | Eksik/gerekli kanıt |
|---|---|---|
| Üçü yeterlikli, aynı yanlış formül | Biliniyorsa ret ve kapsamlı kayıt incelemesi; fark edilmezse yanlış `PROVEN` riski kalır | Vaka semantiği yeterlikle kanıtlanmaz |
| İki yeterlikli yanlış, üçüncü doğru | Çoğunluk yok; ayrışma → soru/karşı örnek | Kaynak–IR çözümü |
| Bir yeterlikli, iki yeterliksiz doğru | Varsayılan üst etiket yok; şartları varsa `CERTIFIED` | İki bireysel kayıt ve heyet yeterliği |
| Üçü eşdeğer farklı formüller | Denklik doğru kurulursa uyuşma | Değişken/alan/amaç eşlemesi |
| Sağlayıcı aynı isim altında model değiştirir | Bilinen değişimde kayıt iptali; gizli değişimde artık risk | Snapshot veya yeni ölçüm |
| Kullanıcı dosyayı düzenler | İmza/hash/sürüm doğrulaması başarısızsa kullanma | Güvenilen köken |
| Ajan sahte yerel kayıt üretir | Ajan çıktısı yeterlik sayılmaz | Güvenilen evaluator ve kayıt yetkisi |
| Şablonu öğrenip gerçek problemde bozulur | Aktarım kümesinde kalma; dar kapsam | Aile dışı ve gerçek-dünya kanıtı |
| Açıkta iyi, gizlide kötü | Otomatik “ezber” hükmü yok; fark analizi ve kabul başarısızlığı | Zorluk/dağılım kontrolü |
| High geçti, low başarısız | Low için yeterlik yok | Ayar eşleşmesi |
| Başka erişim yoluna kayıt taşınıyor | Varsayılan ret | Yeni yol ölçümü veya onaylı köprü testi |
| Üç sağlayıcı, tek aile | Aile koşulu geçmez | Model soy bilgisi |
| Toplayıcı farklı modele yönlendirir | Aday/yeterlik eşleşmesi reddedilir | Gerçek dönen model ve rota |
| Geçerli sertifika, yanlış soru yorumu | Bilinen hatada cevap engellenir | Kaynak uygunluğu; sertifika bunu kurtarmaz |
| Yeterlik geçerli, problem sürümü değişmiş | Eski onay/kanıt bağları kullanılamaz | Yeni revizyon kayıtları |

Özellikle ilk satır önemlidir: Önerilen sistem yanlış `PROVEN`ı imkânsız kılmaz. Onu azaltmayı ve hangi kanıtların mevcut olduğunu doğru söylemeyi amaçlar.

## 8.2. Başka açık teknik sorunların yeterlikle ilişkisi

| Sorun | Öncelik | Yeterlik sistemine etkisi |
|---|---|---|
| `rational/decimal → real` semantik kaybı | Kritik | Evaluator yanlış modeli doğru sayabilir; önce düzeltilmeli |
| Tekrarlı JSON anahtarı | Kritik | Hem aday hem kayıt farklı okunabilir |
| `unsat_core`ın ispat sayılması | Kritik | Yeterlik referansı ve vaka sertifikası yanlış güçlenir |
| Problem revizyonu bağlantısı | Kritik | Doğru model yanlış sürüm için kullanılır |
| MCP sır toplama | Yüksek | Ölçüm komutu anahtarları model bağlamına taşımamalı |
| Yanıt/prompt cache ayrımı | Yüksek | Kayıt yeni üretim yerine eski cevapları ölçebilir |
| Aynı ham çıktıların reddi | Orta | Doğru kısa IR’lar yanlışlıkla elenir |
| Elicitation yokluğu | Yüksek | Sahte doğrudan onay üretilmemeli |
| Bağımsız denetleyici fazı | Kritik | `CERTIFIED`ın gerçek kullanılabilirliğini belirler |

Bunlar modellerin sınavıyla çözülemez. Yanlış evaluator’ı bütün modellerin tutarlı biçimde geçmesi mümkündür.

Soru 1 altında brief’in önerdiği “kesin yeniden hesap ile sertifika ayrımı” makul bir teknik yönelimdir; ancak “kesin işlem” tek başına yeterli değildir. Doğru iddia, özgün IR semantiği ve denetleyici sağlamlığı bağlantıları da korunmalıdır. Aynı tanım tablosunu paylaşmak ortak bağımlılıktır; aritmetik denetimin bağımsızlığı ile normatif tanım kaynağının güveni ayrı yazılmalıdır.

## 8.3. Kalan sahip kararları

Açık onay gerektirenler:

- Üç bireysel yeterlik kaydı varsayılanı.
- Heyet düzeyinde ek kabul testi.
- 400 istemlik başlangıç paketi ve geçme eşikleri.
- 30 günlük varsayılan süre.
- Yerel ölçüm paketlerinin hangi varsayılan güven politikasıyla kabul edileceği.
- Eski Karar 5’in yeterlik temelli metinle değiştirilmesi.
- Başka erişim yoluna sınırlı köprü testiyle aktarımın ileride mümkün olup olmayacağı.

Soru 3–6 kapsamındaki erişim, anahtar isteme, toplayıcı kabulü ve faz ayrıntılarını onaylanmış yeni sahip kararı gibi sunmuyorum.

***

# IX — Rigor tasarım belgesine önerilen değişiklikler

## 9.1. §4.1 — Üst etiketin heyet koşulu

Eski kural: Oybirliği ve en az iki model ailesi; yeterlik kaydı tanımlı değil.

Önerilen metin:

> Üç üyeli zorunlu heyetin her üyesi, ilgili görev kapsamı, dil, erişim yolu ve çağrı yapılandırması için geçerli yeterlik kaydına sahip olmalıdır. En az iki farklı aile bulunmalıdır. Bireysel yeterlik ve oybirliği, formalizasyonun kaynak niyetine uygunluğunun matematiksel kanıtı değildir. Heyet yapılandırması ayrıca sürümlü sistem kabul koşullarını sağlamalıdır.

## 9.2. Yeni §4.6 — Yeterlik kaydı

> Yeterlik kaydı bir modelin genel onayı değil, belirli bir formülasyon yapılandırmasının tarihli ölçüm kaydıdır. Karar; test planı, sonuç paketi ve kabul politikası üzerinden yeniden türetilebilir. Kayıt kökeni, kapsamı, ayarları, geçerlilik süresi ve iptal durumu raporlanır.

Bu bölüm numarası öneridir; mevcut belgede yeni numaranın çakışmadığı ayrıca kontrol edilmelidir.

## 9.3. §6.4 — Üye seçimi ve ayrışma

> Üye seçimi görev profiliyle eşleşen kayıtlardan yapılır. Yeterliksiz üye zorunlu üst heyet üyesi sayılamaz. Ayrışma çoğunlukla kapatılamaz. Geçerli eşdeğer formüller aynı sınıfta sayılır; belirsiz eşleme veya denklik sonucu kabul değildir. Bütün ilk kör adaylar ve yeniden denemeler saklanır.

## 9.4. §8.2 — Yapılandırma kimliği

> Yeterlik, model alias’ına tek başına bağlanmaz. İstenen ve dönen model kimliği, sağlayıcı, erişim yolu, adaptör, sağlayıcıya özgü düşünme ayarı ve çıktı sınırı kaydedilir. Varsayılan olarak başka yol veya ayara taşınmaz. Fallback ya da model değişikliği eşleşmeyi yeniden değerlendirmeyi gerektirir.

## 9.5. §9 — Model ve heyet değerlendirmesi

> Geliştirme ve kabul kümeleri ayrıdır. Parametrik, karşıt, metamorfik ve bağımsız gerçek-dünya örnekleri birlikte kullanılır. Referans formalizasyon ve evaluator ayrıca doğrulanır. Kritik hatalar, yararlı kapsama, doğru soru sorma ve ortak yanlış formalizasyon ayrı ölçülür. İstatistiksel aralıklar örnekleme varsayımları ve gerçek paydalarıyla verilir.

## 9.6. K14/K15 ve Karar 5

K14/K15’e yeterlik ile erişimin ayrı olduğu eklenebilir. Ancak aşağıdaki değişiklik açık sahip onayı gerektirir:

> Üst heyete katkı, erişimin fiyatına değil, eşleşen yeterlik ve çalışma koşullarına dayanır. Eşdeğer yeterlikli ücretsiz erişim eşit katkı verir. Yalnızca ücretsiz heyet için önceki ayrı engel, bu yeni politika yürürlüğe alındığında kaldırılır.

Bu, eski kararı sessizce değiştirmek yerine açık sürüm geçişi sağlar.

## 9.7. Faz planı

| Faz | Önerilen ek |
|---|---|
| F1 | Kayıt şeması, sıkı parser, problem revizyonu, sahte kayıt negatif testleri |
| F2 | Alan profillerinin kaynak ve referans formalizasyonları |
| F3 öncesi | `qualify` runner, evaluator doğrulaması, ilk bireysel ölçümler |
| F3 | Gerçek heyet kabulü ve yeterlik kapısının `PROVEN`a bağlanması |
| F4+ | Süre/iptal, yeni model ekleme, zaman içindeki değişim analizi |
| F9 | Bağımsız yeniden puanlama, gizli/gerçek görev kabulü |

Böylece yeterlik dosyası F1’de boş bir güven listesi olarak üst etiketi açmaz. Gerçek model ölçümleri ve heyet kabulü tamamlanmadan F3’te de üst etiket açılmamalıdır.

***

# X — Nihai karar önerisi

| Soru | Doğrudan cevap | Kanıt ve sınır |
|---|---|---|
| Yeterlik kayıt dosyası kullanılmalı mı? | Evet; ölçüm paketlerinin indeksi olarak | İzlenebilirlik tercihi; genel model doğruluğu onayı değil |
| Yalnızca ölçüm komutunun oluşturması yeterli mi? | Hayır | Köken, bütünlük, yeniden puanlama ve yetki sınırı gerekir; imza da test doğruluğunu garanti etmez.  [docs.github](https://docs.github.com/en/actions/concepts/security/artifact-attestations) |
| Ezbere karşı zorunlu bileşenler? | Parametrik + karşıt/metamorfik + aile dışı/gizli + gerçek-dünya + yenileme | Hiçbiri tek başına yeterli değil.  [arxiv](https://arxiv.org/html/2410.05229v2) |
| Kaç problem? | Profil başına 300 ana + 60 ek çift/metamorfik + 40 bağımsız aktarım = 400 istem | Mühendislik varsayılanı; 400 bağımsız deneme iddiası değil |
| Geçme kriteri? | Sıfır doğrulanmış kritik hata; doğru IR ve doğru soru için ayrı alt sınırlar; eksik değerlendirmede geçiş yok | Eşikler sahip onayına tabi; vaka garantisi değil |
| Kayıt süresi? | Başlangıçta 30 gün; bilinen değişimde derhâl iptal | Bilimsel sabit değil; sentinel süreyi otomatik uzatmaz |
| Üç üyede kaç yeterlikli model? | Üçü de | Ölçülmemiş zorunlu üye bırakmayan muhafazakâr tercih; hatasızlık teoremi değil |
| Farklı aile şartı? | En az iki aile zorunlu; üç tercih edilebilir | Mevcut tasarımla uyumlu; hata bağımsızlığı garantisi değil.  [arxiv](https://arxiv.org/html/2506.07962v1) |
| Heyet ayrıca test edilmeli mi? | Evet | Ortak yanlış formalizasyon ve koşullu kabul hatası bireysel puandan çıkmaz |
| Kayıtsız model katılabilir mi? | Deneysel/danışman olarak evet; zorunlu üst heyet üyesi olarak hayır | Doğru tek vaka yeterlik yerine geçmez; somut itiraz yine incelenir |
| Hangi faz? | Şema F1; ölçüm altyapısı F3 öncesi; gerçek yeterlik ve heyet kapısı F3 | Mevcut yol haritasına sınırlı ek |
| Tamamen ücretsiz yeterlikli heyet üst etikete ulaşmalı mı? | Teknik olarak evet öneriyorum; eski Karar 5’in açık değişikliği şart | Yeni eşit-katkı kararı korunur; eski yasak sessizce silinmez.  [concepts_brief.md] |

## Sonuç

Rigor için önerdiğim varsayılan, üç yeterlikli üyeden oluşan, en az iki aile içeren, kör formülasyon üreten ve ayrıca birlikte değerlendirilmiş bir heyettir.

Ancak yeterlik kaydının dürüst anlamı şu olmalıdır:

> “Bu yapılandırma, belirtilen tarihte, belirtilen görev kapsamı ve test sürümünde tanımlı kabul koşullarını sağladı.”

Şu olmamalıdır:

> “Bu model matematiksel problemleri doğru yorumlar.”

Araştırmadaki en önemli ilerleme, “tik”i bir güven rozeti olmaktan çıkarıp sınırları, kökeni, örneklem belirsizliği ve görev kapsamı belli bir ölçüm kaydına dönüştürmektir. `KANITLANDI` ise ancak bu kayıtların yanında vaka düzeyindeki formal kanıt, bağımsız formülasyon kontrolleri, doğrudan onay ve aynı problem sürümüne bağlı rapor koşulları da sağlandığında kullanılmalıdır.








# Rigor — İkinci aşama bağımsız denetim ve mimari karar raporu

## Yönetici kararı

Önceki raporun ana yönünü koruyorum: Üç üyeli zorunlu heyette `KANITLANDI` için varsayılan olarak üç üyenin de ilgili kapsamda geçerli yeterlik kaydı bulunmalıdır. Ancak bu koşul, üçlü heyetin iki üyeden daha güvenilir olduğunun bilimsel ispatı değildir. Eklediği güvence, bütün zorunlu üyelerin ölçülmüş ve izlenebilir olmasıdır. Gerçek ortak-hata davranışı heyet düzeyinde ayrıca ölçülmelidir.

Bu araştırma önceki rapora dört önemli düzeltme getiriyor:

1. **400 istem**, kendi başına istatistiksel olarak gerekçelendirilmiş bir yeterlik standardı değildir. Üç yüz ölçüm örneği ile yüz davranış/stres örneğinin kanıt rolleri ayrılmalıdır.
2. Önceki çoklu karşılaştırma uyarısı eksik sınıflandırılmıştı: “Bütün önceden belirlenmiş koşullar geçmeli” türündeki birleşik kabul kararı ile “bütün güven aralıkları eşzamanlı kapsasın” iddiası aynı değildir. Her kapı için otomatik Bonferroni uygulamak gerekmez. [doi](https://doi.org/10.1214/ss/1032280304)
3. Referans formalizasyon ve değerlendirici yeterince güvenilir değilse, model yeterlik puanı gerçekte yanlış değerlendiriciyle uyumu ölçebilir. Bu nedenle model testinden önce değerlendirici kabulü gerekir.
4. Geçerli imza, güncel yeterlik anlamına gelmez. Eski ama geçerli imzalı kayıtların geri getirilmesi ve kayıt–test–politika sürümlerinin karıştırılması ayrıca engellenmelidir. [theupdateframework.github](https://theupdateframework.github.io/specification/latest/)

Yeni öneri, daha büyük bir sistem kurmak değildir. Mevcut kayıt önerisine üç küçük fakat kritik sözleşme eklemektir:

- Ölçümün neyi tahmin ettiği açıkça yazılır.
- Değerlendiricinin kendisi kabul testinden geçer.
- Yeterlik kararı yalnızca imzaya değil; kapsam, güncellik, iptal ve çalışma anı eşleşmesine de bağlıdır.

***

# I. Önceki araştırmanın eksiklik envanteri

## 1.1. Önceki sonucun doğru kaydı

Bir önceki rapor iki değil, üç yeterlikli üye önermişti. Bu rapor o öneriyi yeniden sınadı.

Güncel `concepts_brief.md` ise:

- Soru 1’in kapandığını,
- Dört etiketin benimsendiğini,
- Model yeterlik ölçümünün sahip kararı olduğunu,
- Güçlü ücretsiz modelin katkısının eşit sayılacağını,
- Fakat kayıt koşulları, eşikler, süre ve karma heyet ayrıntılarının açık olduğunu

belirtiyor. Bu ayrımı koruyorum. [concepts_brief.md]

## 1.2. Eksiklik tablosu

| Önem | Önceki sonuç | Dayanak ve durumu | Eksik kalan nokta | Rigor’a etkisi | Gerekli düzeltme |
|---|---|---|---|---|---|
| Kritik | Profil başına 400 istem önerildi | GSM-Symbolic, LiveBench, binom hesapları yöntemi destekliyor; tam sayıyı değil | Hedef hata düzeyi ve kabul/ret maliyetleri belirlenmeden sayı seçildi | Bütçe önerisi güvence standardına dönüşebilir | Örnekleme planı ile kabul politikasını ayır |
| Kritik | Sıfır kritik hatayla yeterlik verilebilir | Sabit örneklem binom sınırı koşullu olarak doğru | Değerlendiricinin yanlış etiketleri ölçülmedi | Yanlış model geçebilir; doğru model kalabilir | Önce referans/evaluator kabulü |
| Kritik | Üç bireysel kayıt + heyet testi | Ortak hata literatürüyle destekleniyor | Üçüncü kaydın ek güvenlik kazancı ölçülmedi | Süreç tamlığı, hata azalması sanılabilir | Aynı görevlerde eşlenmiş iki/üç üye karşılaştırması |
| Yüksek | Çoklu ölçümlerde düzeltme gerekebilir | Eşzamanlı güven aralıkları için doğru | Birleşik “hepsi geçmeli” kararı ayrı ele alınmadı | Gereksiz örneklem ve çağrı maliyeti | Intersection–union ayrımını uygula |
| Yüksek | Parametrik + metamorfik test kombinasyonu önerildi | Sağlam genel dayanak var | İlişkileri sağlayan sistematik yanlışlar ele alınmadı | Tutarlılık doğruluk sanılabilir | Mutlak referans noktaları ve negatif örnekler |
| Yüksek | Gizli/gerçek pay yeterliği güçlendirir | Doğru yön | Kaynak belge ve şablon ailesi sızıntısı ayrıntısız | Aynı belgenin türevleri iki kümeye dağılabilir | Kaynak/aile düzeyinde ayrım |
| Kritik | Komut + paket + imza kayıt güveni sağlar | Köken ve bütünlük bakımından doğru | Rollback, freeze ve mix-and-match eksikti | İptal edilmiş kayıt yeniden etkinleşebilir | Sürümlü güncellik manifesti |
| Yüksek | Kayıt 30 gün geçerli olsun | Açık tasarım tercihi olarak verilmişti | Otuz günün davranışsal güvenilirlik dayanağı yok | Süre dolmamış kayıt “model değişmedi” sanılabilir | İdari süre ile model sürekliliğini ayır |
| Yüksek | Başka erişim yoluna aktarım varsayılan kapalı | Korunmalı | Aktarımın gelecekte nasıl kanıtlanacağı yok | Aynı ad farklı davranışı saklayabilir | Ayrı köprü değerlendirmesi; eşdeğerlik varsayma |
| Orta | Tek geliştirici için hafif kayıt sistemi | Uygun | Çok sayıda profil/ayarın bakım yükü yeterince sınırlandırılmadı | Ölçüm matrisi yönetilemez | Önce gerçekten kullanılacak üç yapılandırma |
| Orta | Her yeni test sürümünde yenileme | Genel olarak makul | Yazım düzeltmesiyle semantik değişim ayrılmadı | Gereksiz tam tekrarlar | Etki sınıflı geçersizleştirme |

Düşük önem düzeyindeki adlandırma ve görünüm tercihlerini bu turda yeniden açmıyorum. Yanlış `KANITLANDI`, yanlış yeterlik ve yanlış benchmark yorumunu önleme önceliklidir.

***

# II. Yeni bilimsel ve teknik kanıtlar

## 2.1. Davranış testleri, genel başarı oranından farklı bir kanıt türüdür

Ribeiro ve arkadaşlarının ACL 2020 CheckList çalışması üç test türünü ayırır:

- Minimum işlevsellik,
- Değişmezlik,
- Yönlü beklenti.

Çalışma, yüksek benchmark başarısına rağmen olumsuzlama, zaman sırası, anlamsal roller ve karşılaştırmalarda ciddi hatalar bulur. Ayrıca test hazırlayan kullanıcılarla deney yapar. Bu, önceki rapordaki karşıt ve metamorfik test önerisini güçlendirir. [aclanthology](https://aclanthology.org/2020.acl-main.442.pdf)

Fakat aynı çalışma, bu testlerden geçmenin ilgili özelliğin eksiksiz sağlandığını göstermediğini açıkça söyler.

### Rigor’a yeni etkisi

İki ayrı değerlendirme çıktısı tutulmalı:

1. Tanımlı bir dağılımdan örneklenmiş görevlerde ölçülen başarı/hata.
2. Önceden belirlenmiş tehlikeli davranışlara yönelik stres testlerinin sonucu.

İkincisini birincinin örneklemine ekleyerek tek bir “genel hata olasılığı” hesaplamak doğru değildir.

## 2.2. Metamorfik tutarlılık, mutlak doğruluk değildir

Chen ve arkadaşlarının ACM Computing Surveys incelemesi, metamorfik ilişkileri hedef fonksiyonun gerekli özellikleri olarak tanımlar. “Gerekli” olmaları “yeterli” oldukları anlamına gelmez. [dl.acm](https://dl.acm.org/doi/10.1145/3143561)

Somut Rigor karşı örneği:

Yanlış bir dönüşüm fonksiyonu

\[
f(x)=0{,}3x
\]

şu ilişkileri sağlar:

\[
f(a+b)=f(a)+f(b),\qquad f(ka)=kf(a).
\]

Yani toplamsallık ve ölçekleme testlerini geçebilir; yine de uluslararası foot dönüşümü için yanlıştır.

Benzer şekilde, bir model her iki karşıt problemde de tutarlı fakat yanlış bir yorum üretebilir.

### Yeni karar

Metamorfik testlerde en az üç unsur bulunmalı:

- İlişkinin kendisi,
- İlişkinin geçerli olduğu önkoşullar,
- Bağımsız mutlak referans örnekleri.

Metamorfik testler referans doğrulamasının yerine değil, yanına konulmalıdır.

## 2.3. Rastgele test üretiminde asıl kontrol noktası dağılımdır

QuickCheck’in temel yaklaşımı, özelliklerin çok sayıda rastgele örnekte sınanması ve özel veri üreticilerinin tanımlanmasıdır. Resmî kaynak, üretilen test verisinin dağılımını gözlemlemeyi de araç tasarımının parçası sayar. [cse.chalmers](https://www.cse.chalmers.se/~rjmh/QuickCheck/)

Rigor’a etkisi:

- Bir generator’ın 10.000 örnek üretmesi, 10.000 anlamlı farklı durum kapsadığı anlamına gelmez.
- Sınır değerleri, dejenerasyonlar, tam bölünme, işaret değişimi ve belirsiz birim durumları üretimde gerçekten görülmelidir.
- “Rastgele” sözcüğü örneklem uygunluğunun kanıtı değildir.
- Üretici sürümü ve dağılımı yeterlik kaydının parçasıdır.

Bu, önceki raporun “tohum saklansın” önerisini tamamlar: Tohum, yanlış veya dar bir dağılımı da kusursuz tekrar üretir.

## 2.4. Gerçek dünyaya aktarım için kaynak düzeyinde ayrım gerekir

Koh ve arkadaşlarının ICML 2021 WILDS çalışması, dağılım kaymasını yalnızca rastgele train/test ayrımıyla değil; hastane, kamera, ülke, zaman, kullanıcı ve kod deposu gibi kaynak alanları üzerinden kurar. Çalışmada standart modellerin dağılım dışı başarımı, dağılım içi başarımından belirgin biçimde düşer. [proceedings.mlr](https://proceedings.mlr.press/v139/koh21a/koh21a.pdf)

Bu kaynak LLM formalizasyonu veya Rigor için bir hata oranı vermez. Desteklediği yöntemsel sonuç şudur:

> Aynı kaynak belgeden türetilen örnekleri farklı kümelere dağıtmak, gerçek kaynak-dışı genelleme testi değildir.

### Rigor’a etkisi

Ayrım birimleri şunları içermeli:

- Şablon ailesi,
- Kaynak şartname/belge,
- Yazar veya hazırlayıcı,
- Model/standart sürümü,
- Problem alanı,
- Dil ve metin uzunluğu.

Aynı şartnamenin farklı paragraflarından türeyen çok benzer problemler, bağımsız dış doğrulama kanıtı olarak sayılmamalıdır.

## 2.5. İstatistiksel olarak önemli düzeltme: “Hepsi geçmeli” ile çoklu fırsat farklıdır

Önceki raporun çoklu model/profil aralıkları hakkındaki uyarısı doğruydu; fakat kabul kararına uygulanışı eksikti.

Üç ayrı durum vardır:

### A. Bütün aralıkların aynı anda kapsaması

“Üç modelin üç güven aralığı birlikte %95 kapsama sağlasın” deniyorsa eşzamanlı çıkarım gerekir. Önceki Bonferroni örnekleri bu amaç içindi.

### B. Tek bir önceden belirlenmiş heyetin bütün kapılardan geçmesi

Her zorunlu koşul için geçerli düzey-\(\alpha\) test varsa ve başarı için hepsinin geçmesi gerekiyorsa, bu bir **intersection–union** yapısıdır. Global sıfır hipotezi “en az bir zorunlu koşul sağlanmıyor”dur.

Bu durumda yalnızca kapı sayısı arttı diye otomatik olarak \(\alpha\)’yı kapı sayısına bölmek gerekmez. Berger–Hsu bu mantığı sistematikleştirir; FDA’nın çoklu sonlanım rehberi de “bütün ortak birincil koşullar sağlanmalı” durumunu “herhangi biri yeterli” durumundan ayırır. [doi](https://doi.org/10.1214/ss/1032280304)

Bu, FDA’nın Rigor’a uygulanacak bir standardı olduğu anlamına gelmez; kullanılan matematiksel test mantığı geneldir.

### C. Çok sayıda aday arasından geçeni seçmek

Otuz model/ayar denenip geçen biri seçiliyor veya başarısız testler farklı tohumlarla tekrar ediliyorsa yeni başarı fırsatları oluşur. B durumunun koruması bunu otomatik çözmez.

### Rigor’a yeni etkisi

- Sabit bir heyetin bütün zorunlu eşiklerini test etmek için gereksiz çoklu düzeltme yapılmamalı.
- Aday seçimi, tekrar denemeler ve eşzamanlı yayın iddiaları ayrıca ele alınmalı.
- “Bütün kapılar geçti” kararı ile “bütün performans aralıkları aynı anda geçerli” ifadesi raporda ayrılmalı.
- Bu mantık, testlerin kendi örnekleme varsayımları bozuksa kurtarıcı değildir.

## 2.6. Sürekli izleme için sabit örneklem aralığı yeterli değildir

Howard ve arkadaşlarının *Annals of Statistics* çalışması, sabit bir zamanda geçerli güven aralığı ile bütün izleme zamanları boyunca geçerli confidence sequence’i ayırır. Sonuçlara sürekli bakıp uygun zamanda durmak, sabit örneklem yönteminin hata kontrolünü bozabilir. Zaman-uniform yöntemler bu esnekliği açık varsayımlar ve genellikle daha geniş sınırlar karşılığında sağlar. [arxiv](https://arxiv.org/html/1810.08240)

Rigor’a etkisi:

- İlk kabul çalıştırmasında sabit ve önceden belirlenmiş plan daha basittir.
- Ara sonuçlara bakarak “biraz daha test edelim, geçince duralım” yapılmamalı.
- Haftalık sentinel testler ayrı bir izleme politikasıdır; her hafta aynı klasik %95 sınırı hesaplayıp sınırsız devam etmek otomatik %95 yaşam döngüsü güvencesi oluşturmaz.
- v1’de genel confidence-sequence altyapısı şart değil; önceden belirlenmiş izleme ve yeniden kabul kuralları yeterli başlangıçtır.

## 2.7. Kabul örneklemi yalnızca güven aralığına göre seçilmemeli

NIST’in kabul örneklemesi yaklaşımı, bir \((n,c)\) planını yalnızca örneklem büyüklüğüyle değil:

- İyi kabul edilen performans düzeyi,
- Kötü kabul edilen performans düzeyi,
- İyi sistemi yanlış reddetme riski,
- Kötü sistemi yanlış kabul etme riski

üzerinden tasarlar. [itl.nist](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc232.htm)

Rigor’a doğrudan bir sanayi kabul standardı taşımıyorum. Alınacak yöntemsel ders:

> Önce “hangi iki performans düzeyini ne kadar ayırt etmek istiyoruz?” sorusu cevaplanmalı, sonra test büyüklüğü seçilmeli.

Önceki raporda 300 soru için sıfır hata olasılıkları verilmişti; bu doğruydu. Eksik olan, bunların bir kabul planı olarak tutarlı hedeflere bağlanmasıydı.

Örneğin sıfır hata şartıyla:

\[
P(\text{geçiş}\mid p)=(1-p)^n.
\]

Hem çok düşük ama sıfır olmayan hata oranındaki modeli çok yüksek olasılıkla geçirmek hem de biraz daha kötü modeli çok yüksek olasılıkla elemek, her seçilen \(n\) için mümkün değildir. Sıfır toleransın ölçülmüş bir yanlış-ret maliyeti vardır.

## 2.8. İmzalı yeterlik kaydı güncel kayıt demek değildir

TUF spesifikasyonu imza doğrulamasından ayrı olarak rollback, freeze ve mix-and-match saldırılarını ele alır. Sürüm, son kullanım zamanı, tutarlı snapshot ve istemcinin daha önce gördüğü sürümler bu yüzden önemlidir. [theupdateframework.github](https://theupdateframework.github.io/specification/latest/)

Rigor karşı örneği:

- Modelin yeterliği yeni bir kritik hata nedeniyle iptal edilir.
- Saldırgan veya eski önbellek, hâlâ imzası geçerli eski kaydı sunar.
- İstemci yalnızca imzayı kontrol ederse modeli yeniden yeterli sayar.

### Yeni karar

Yeterlik dosyasının güven koşulu:

> Geçerli köken + beklenen içerik + uygun sürüm + geçerli süre + bilinen iptal bulunmaması + çalışma anı eşleşmesi.

Tam TUF altyapısını v1’e kurmak zorunlu değildir. Fakat onun ele aldığı tehditler, “dosyayı imzaladık” denilerek kapatılmamalıdır.

## 2.9. Eşdeğerlik denetleyicisinin ölçtüğü ilişki açık olmalı

Bu turda EquivaMap’in yöntem metni incelendi. Okunan sürüm, belirli optimizasyon örneğinde optimal çözümlerin eşlenmesine odaklanıyor; bütün uygulanabilir kümelerin veya bütün parametre değerlerinin eşitliğini hedeflemiyor. [arxiv](https://arxiv.org/html/2502.14760)

Dolayısıyla şu ilişkiler ayrılmalı:

- Aynı sayısal cevap,
- Aynı optimal değer,
- Aynı optimal çözümün elde edilebilmesi,
- Aynı uygulanabilir karar kümesi,
- Bütün parametreler için aynı formalizasyon,
- Aynı kaynak metni temsil etme.

Örnek:

\[
F:\max x,\quad x\in\{0,1,2\}
\]

ile

\[
G:\max x,\quad x=2
\]

aynı optimumu verir. Fakat bütün uygulanabilir kararlar soruluyorsa aynı problem değildir.

Bu nedenle Rigor yeterlik evaluator’ı “aynı optimum bulundu” sonucunu genel formülasyon doğruluğu yerine kullanamaz.

Kaynak denetiminde ayrıca arama sonucunun EquivaMap’e bağladığı bir PMLR adresinin başka bir makaleyi açtığı görüldü. O adres EquivaMap kanıtı olarak kullanılmadı; yöntem değerlendirmesi doğru başlık ve yazarlarla eşleşen arXiv metnine dayandırıldı. [arxiv](https://arxiv.org/html/2502.14760)

***

# III. Önceki sonuçların yeniden değerlendirilmesi

| Önceki sonuç | Yeni değerlendirme |
|---|---|
| Üç zorunlu üye için üç bireysel kayıt | Korunuyor; süreç tamlığı gerekçesiyle |
| En az iki farklı aile | Korunuyor; istatistiksel bağımsızlık iddiası değil |
| Heyet ayrıca test edilmeli | Güçlendiriliyor; görev bazında ortak yanlış formalizasyon ölçülmeli |
| 400 istemlik paket | Bütçe/kapsam taslağı olarak korunuyor; evrensel istatistiksel yeterlik standardı değil |
| %80 doğru IR alt sınırı ve %90 doğru soru alt sınırı | Geçici kullanılabilirlik hedefleri; optimum oldukları gösterilmedi |
| Sıfır kritik hata | Muhafazakâr kabul politikası; sıfır gerçek hata anlamına gelmez |
| Çoklu ölçümlerde Bonferroni gerekebilir | Doğru ama bağlama bağlı; bütün kapıların zorunlu olduğu tek kabul için otomatik değil |
| 30 gün geçerlilik | İdari varsayılan olarak kalabilir; modelin 30 gün değişmeyeceğinin kanıtı değil |
| İmza ve köken kaydı | Korunuyor; güncellik ve iptal kontrolleri ekleniyor |
| Parametrik ve gizli testler | Korunuyor; kaynak/aile düzeyinde ayrım zorunlu hâle geliyor |
| Referans IR + denklik | Hedeflenen eşdeğerlik ilişkisi belirtilmeden yeterli değil |
| Kayıtsız üye danışman olabilir | Korunuyor; zorunlu üst heyet üyesi sayılamaz |

## Önceki sayısal hesaplar hakkında

Önceki rapordaki sıfır hata için

\[
p_U=1-\alpha^{1/n}
\]

formülü, belirtilen sabit yapılandırma ve binom örnekleme varsayımları altında doğrudur. Örneğin 300 sıfır hatalı bağımsız deneme için yaklaşık %0,994 üst sınır hesabını geri çekmiyorum. [itl.nist](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm)

Düzelttiğim şey hesap değil, onun kullanılabileceği iddiadır:

- Bu değer bütün görev sınıflarına taşınamaz.
- Davranış/stres örnekleri aynı örnekleme sürecinden gelmiyorsa toplama otomatik katılamaz.
- Aynı kaynaktan türetilmiş çok sayıda varyant, kaynak-dışı genelleme örneklemi değildir.
- Yanlış referansla elde edilen başarıya ait aralık, gerçek doğruluk aralığı değildir.

***

# IV. Açık anlaşmazlıkların çözümü

## 4.1. “Üç yeterlikli üye gerçekten daha güvenli mi?”

### Görüş A: İki yeterlikli üye yeterli olabilir

Güçlü yanı: Daha düşük maliyet ve daha fazla erişilebilirlik. Üçüncü üye yalnızca deneysel danışman olarak tutulabilir.

Zayıf yanı: “Üç üyeli zorunlu heyet” deniyorsa üçüncü üyenin göreve uygunluğu ölçülmemiş kalır.

### Görüş B: Üçünün de yeterliği olmalı

Güçlü yanı: Her zorunlu bileşen için kapsamlı kayıt vardır.

Zayıf yanı: Üç kayıt, ortak hata oranının düşük olduğunu göstermez; üçüncü üye gereksiz ret ve bakım yükü yaratabilir.

### Sonuç

Varsayılan üç kayıt önerisini koruyorum. Fakat şu iddiayı reddediyorum:

> “Üç kayıt, iki kayda göre belirli bir oranda daha güvenlidir.”

Bunu gösterecek Rigor deneyi yok.

Deneysel karşılaştırma aynı görevlerde yapılmalı:

- Aynı iki çekirdek üye,
- Aynı kör ilk adaylar,
- İki üyeli kabul,
- Üçüncü üyenin filtre olarak eklenmesi,
- Yayımlanan doğru/yanlış sonuçlar ve kapsama.

Sadece üçlü sistemin daha az cevap vermesi başarı sayılmamalıdır.

## 4.2. “Tek geliştirici için bağımsız denetim mümkün mü?”

Her test sorusunu sürekli iki uzmanla etiketlemek pahalıdır. Buna karşılık aynı generator–referans–evaluator zincirine tamamen güvenmek de ortak hata yaratır.

Önerilen denge:

- Her şablon ailesinin ve kritik dönüşümün bağımsız incelemesi.
- Otomatik üretimde alan/önkoşul doğrulamaları.
- Örneklenmiş insan incelemesi.
- Evaluator için bilerek bozulmuş formalizasyonlar.
- Bütün kritik başarısızlıkların adjudication kaydı.
- İncelenemeyen alanın kapsam dışı bırakılması.

Bu, hatasız oracle garantisi değildir; ortak hata yüzeyini makul maliyetle küçültür.

## 4.3. “Sıfır kritik hata çok mu katı?”

Sahibin yanlış `KANITLANDI`ı en kritik başarısızlık saymasıyla uyumludur. Fakat iki koşul gerekir:

1. “Kritik hata” önceden tanımlanmış olmalı.
2. Hatanın modele mi, benchmark’a mı, evaluator’a mı ait olduğu ayrılmalı.

Belirsiz bir referans yüzünden model otomatik başarısız sayılmamalı; aynı şekilde belirsiz soruyu sonradan sessizce silerek modeli geçirmek de uygun değildir.

## 4.4. Ücretsiz–ücretli çelişkisi

Bu konuda yeni kanıt eski ayrımı değiştirmiyor:

- Fiyat yeterlik ölçüsü değildir.
- Düşünme/çıktı ayarları ve gerçek hizmet yolu yeterliği etkileyebilir.
- Kota, işin tamamlanmasını etkiler; tamamlanmış kanıtın mantıksal gücünü değil.
- Yeni ücretsiz eşit-katkı kararı ile eski ücretsiz-only üst etiket yasağının birlikte nasıl uygulanacağı açık sahip kaydı gerektirir. [concepts_brief.md]

Bu rapor eski yasağı kendiliğinden kaldırmıyor.

***

# V. Model yeterliği ve benchmark tasarımı

## 5.1. Yeni asgari gereklilik: Önce ölçüm iddiası yazılmalı

Her profil için testten önce şu cümle tamamlanmalı:

> “Bu değerlendirme, şu dilde, şu uzunluk ve problem yapılarında, şu araç/bağlam koşullarıyla çalışan formülatör yapılandırmasının şu davranışlarını ölçer.”

Örneğin:

> “Türkçe kısa doğrusal kaynak tahsisi problemlerinde amaç, tamsayılılık ve kısıtların IR’a aktarılması; eksik veri varsa sonuç değiştirici sorunun sorulması.”

“Matematikte yeterli” gibi sınırsız profil kullanılmamalıdır.

NIST’in ölçüm rehberi de ölçümün iddia ettiği kavramı gerçekten yakalamasını, kullanım koşullarına benzer ortamlarda sınanmasını ve genellenebilirlik sınırlarının belgelenmesini ister. Belirli test sayısı veya Rigor eşiği belirlemez. [airc.nist](https://airc.nist.gov/airmf-resources/playbook/measure/)

## 5.2. Önceki 400 istemlik paket nasıl düzeltilmeli?

Önerilen ayrım:

### S — Ölçüm kümesi: 300 temel örnek

- Önceden tanımlı örnekleme planı.
- Tanımlı görev dağılımı.
- Paydaları açık sonuçlar.
- Uygunsa binom aralıkları.
- Tabakalı veya kümeli örneklemede buna uygun analiz.

### D — Davranış/stres kümesi: 100 ek istem

- 60 karşıt/metamorfik istem.
- 40 kaynak/aile dışı veya gerçek-dünya/adversarial istem.
- Güvenlik kapıları ve kapsam kontrolü.
- Genel hata olasılığı tahminine otomatik eklenmez.

Bu sayıların 300+100 olması başlangıç bütçe tercihidir. Şu an kaynaklar bu sayıyı Rigor için “doğru standart” olarak doğrulamıyor.

## 5.3. İki farklı birim kaydedilmeli

- Çağrı/istem sayısı.
- Bağımsız değerlendirme birimi: temel vaka, şablon ailesi veya kaynak belge.

Aynı vakanın beş parafrazı:

- Beş çalışma davranışını gösterir.
- Bir aileye karşı dayanıklılık gösterebilir.
- Beş yeni gerçek-dünya kaynak ailesi değildir.

Tek bir “etkin örneklem” sayısını tahmini korelasyonla üretip binom formülüne koymayı v1 için önermiyorum. Bunun yerine aile/kaynak bazında sonuçlar ve açık paydalar verilmeli.

## 5.4. Evaluator kabul paketi

Model ölçümünden önce evaluator şu örnekleri doğru ayırmalıdır:

| Örnek | Beklenen |
|---|---|
| Değişken ve kısıt sırası değişmiş eşdeğer IR | Kabul |
| Geçerli slack değişkenli reformülasyon | Desteklenen ilişkiyse kabul |
| Amaç yönü ters | Ret |
| Tamsayılı değişken reel yapılmış | Ret |
| Zorunlu kısıt silinmiş | Ret |
| Aynı optimumu veren fakat başka uygulanabilir kümeye sahip model | Görev ilişkisinin gerektirdiği ayrım |
| Birim ölçeği değiştirilmiş | Uygun eşleme yoksa ret |
| Belirsiz değişken eşlemesi | `INCONCLUSIVE` |
| Çözücü `unknown` | `INCONCLUSIVE`, kabul değil |
| İki formül de çelişkili | Anlamsal uygunluk varsayılmaz |
| Referans metnin kendisi belirsiz | Benchmark incelemesi |

Buradaki mutasyonlar sadece yanlışları yakalamayı değil, doğru reformülasyonların gereksiz reddini de test etmelidir.

## 5.5. Oracle hatasının istatistik üzerindeki etkisi

Gerçek kritik hata etiketi \(E\), evaluator’ın etiketi \(\hat E\) olsun.

Evaluator’ın yanlış etiketleme olasılığı \(\varepsilon\) ile sınırlandırılabiliyorsa basitçe:

\[
\left|P(E=1)-P(\hat E=1)\right|
\leq P(E\neq\hat E)
\leq\varepsilon.
\]

Bu bir risk bütçesi ayrımıdır; Rigor için \(\varepsilon\)’nin bilindiğini söylemiyorum.

Sonuç:

> Çok dar bir örneklem güven aralığı, yanlış evaluator’ın sistematik hatasını ortadan kaldırmaz.

Önceki raporun en önemli eksiklerinden biri buydu.

## 5.6. Kabul eşikleri nasıl kullanılmalı?

Önceki %80 doğru IR ve %90 doğru soru alt sınırları:

- Kullanılabilirlik hedefi olarak pilotta korunabilir.
- Genel model kabiliyeti veya güvenlik standardı diye sunulmamalı.
- Kapsamı ve risk maliyeti belli olduktan sonra gözden geçirilmeli.

Sıfır doğrulanmış kritik hata şartı da korunabilir; fakat:

- Stress başarısı ile dağılımsal ölçüm ayrılır.
- Bir kritik hata, ilgili kapsam için kabulü engeller.
- Referans/evaluator kusuru bulunursa bütün modeller için adil yeniden puanlama yapılır.
- Sadece kötü sonuç veren örnekler sonradan silinmez.
- Yeni kabul sürümü ve etkilenen eski kayıtlar açıkça işaretlenir.

## 5.7. Testin durdurulması ve yeniden deneme

v1 için en basit güvenilir yol:

- Plan ve tohum seçimi önceden sabitlenir.
- Güvenlik hatası bulununca erken başarısızlık mümkündür.
- Başarı için planın tamamlanması gerekir.
- Daha fazla örnek ekleyip geçene kadar devam edilmez.
- Yeni prompt/model/ayar yeni yapılandırmadır.
- Bütün kabul girişimleri kayıtlıdır.

İleride gerçekten uyarlanabilir örnekleme istenirse uygun sequential yöntem kullanılabilir. Confidence sequence, benchmark yanlışlığını veya dağılım kaymasını otomatik çözmez. [arxiv](https://arxiv.org/html/1810.08240)

***

# VI. Yeterlik kayıtlarının güven modeli

## 6.1. Kayıt doğruluğunu üç parçaya ayırma

1. İçerik bütünlüğü: Dosya değişmiş mi?
2. Ölçüm kökeni: Kim, hangi runner ve politika ile üretmiş?
3. Davranış sürekliliği: Bugünkü hizmet ölçülen hizmetle aynı mı?

İmza birinci ve ikinci parçayı destekleyebilir. Üçüncüyü tek başına sağlamaz.

GitHub’ın attestation belgesi de köken kanıtının artefaktın güvenli veya doğru olduğunu garanti etmediğini açıkça söyler. [docs.github](https://docs.github.com/en/actions/concepts/security/artifact-attestations)

## 6.2. Asgari v1 kayıt yapısı

| Alan grubu | İçerik |
|---|---|
| Yapılandırma | İstenen/dönen model, sağlayıcı, rota, özgün reasoning ayarı, çıktı sınırı |
| Profil | Rol, dil, yapı, uzunluk, izinli araç/bağlam |
| Ölçüm | Plan, generator, referans, evaluator ve runner sürümleri |
| Sonuç | Pay/payda, hata türleri, aralıklar, eksikler, bütün denemeler |
| Köken | Bakımcı/yerel, üretim zamanı, kanıt paketi özeti |
| Uygunluk | Kullanılan kabul politikası ve sonuç |
| Güncellik | Son tarih, iptal/askı, kayıt ve manifest sürümü |

`qualified: true` saklanabilir bir önbellek olabilir; fakat güven kararı yalnızca bu alandan alınmamalıdır.

## 6.3. Rollback ve mix-and-match koruması

Önerilen küçük ek:

- Dağıtılan kayıtlar bir sürümlü manifestte indekslenir.
- Manifest, hangi test/evaluator/politika sürümlerinin birlikte geçerli olduğunu belirtir.
- İptal edilen kayıtlar açıkça listelenir.
- İstemci daha önce gördüğü sürümden eski manifesti sessizce kabul etmez.
- Son tarih güvenilir yerel saat varsayımıyla kontrol edilir.
- İmza doğrulaması yanında beklenen köken kimliği de kontrol edilir.
- Yeni paket yayımlanması bütün eski kayıtları otomatik silmez; hangi kapsamın etkilendiği belirtilir.

Bu, TUF’un bütün mimarisini kopyalama önerisi değildir. TUF uyumlu olunmadığı hâlde “TUF güvenliği” iddiası da verilmemelidir. [theupdateframework.github](https://theupdateframework.github.io/specification/latest/)

## 6.4. Çevrimdışı davranış

İnternet yoksa:

- Mevcut kayıt kullanılabilirlik politikasına göre değerlendirilir.
- “İptal yok” yerine “son güncellemeden bu yana iptal durumu bilinmiyor” denir.
- Süresi dolmuş veya zorunlu güncellik koşulu sağlanmayan kayıt üst etikete katkı vermez.
- Matematiksel sertifika kontrolü yerelde çalışmaya devam edebilir.
- Sessiz ücretli API geçişi yapılmaz.

## 6.5. Yerel kayıt ile bakımcı kaydı

Aynı test planı ve evaluator ile üretilmiş yerel kayıt, ölçüm bakımından otomatik düşük değildir. Ancak güvenilen yürütme ve köken varsayımları farklıdır.

Öneri:

- Bakımcı kaydı: Beklenen imza/köken doğrulanır.
- Yerel kayıt: Kullanıcının güvenilen runner’ı ve yerel güven politikası altında kabul edilir.
- Dışarıya verilen raporda yerel kaydın bağımsız uzak köken doğrulamasına sahip olmadığı belirtilir.
- Tam yetkili yerel kullanıcı/ajanın sistemi değiştirerek dürüst etiket üretmesini sağlama iddiası yoktur.

Yerel hash zinciri veya yerel imza anahtarı, aynı yetkili saldırganın bütün kayıtları ve programı değiştirmesine karşı tek başına güven sağlamaz.

## 6.6. Otuz gün politikasının yeniden yorumu

Otuz gün önerisini geri çekmiyorum; anlamını daraltıyorum:

> Otuz gün bir yeniden değerlendirme takvimidir, modelin bu süre boyunca aynı kaldığının kanıtı değildir.

Geçersizleştirme tetikleyicileri:

- Model/snapshot değişikliği.
- Reasoning veya çıktı bütçesi değişikliği.
- Sağlayıcı/rota/quantization değişikliği.
- Formülasyon prompt’u veya araç bağlamı değişikliği.
- İlgili evaluator/referans kusuru.
- Doğrulanmış kritik saha hatası.
- Güvenlik veya köken ihlali.

Görünmeyen değişiklikler için artık risk kalır. Sentinel geçişi kayıt süresini otomatik uzatmamalıdır.

***

# VII. Karma heyet mimarisi

## 7.1. Beş güven türünü ayrı tutma

| Kanıt | Cevap verdiği soru |
|---|---|
| Bireysel yeterlik | Bu yapılandırma bu görev profilinde ne yaptı? |
| Aile çeşitliliği | Benzer soy/sağlayıcı tekrarları sınırlı mı? |
| Formal denklik | Adaylar belirtilen ilişki altında aynı şeyi mi ifade ediyor? |
| Heyet ölçümü | Birlikte hangi yanlışları kabul ediyorlar? |
| Matematiksel sertifika | Seçilen formal iddia geçerli mi? |

Bunların hiçbiri diğerinin yerine geçmez.

## 7.2. Yeni bağımsız destek: Ortak yanlışlar LLM’ye özgü bir sorun değil

Knight–Leveson deneyinde aynı spesifikasyondan bağımsız hazırlanan 27 program, bir milyon test üzerinde incelenmiş; birlikte hataların bağımsızlık varsayımından beklenenden fazla olduğu bulunmuştu. [computer](https://www.computer.org/csdl/journal/ts/1986/01/06312924/13rRUyuNsyG)

İzleyen NASA raporu önemli bir karşıt bulgu da içerir:

- Karşılaştırma testleri ortak yanlışları kaçırabilir.
- Buna rağmen maliyet etkin hata bulma yöntemi olabilir; çünkü aynı kusurlar her girdide birlikte tetiklenmez. [ntrs.nasa](https://ntrs.nasa.gov/api/citations/19870018000/downloads/19870018000.pdf)

Rigor için sonuç:

- “Ortak hata var, çoklu formülasyon yararsız” yanlıştır.
- “Ayrı üretildi, hatalar bağımsızdır” da yanlıştır.
- Bağımsız kaynak/refereans ve vaka kontrolleriyle birlikte çoklu formülasyon yararlı bir savunma katmanıdır.
- Bu klasik program deneyinin oranları LLM heyetine taşınamaz.

## 7.3. Bir, iki ve üç yeterlikli üye

| Politika | Eklediği güvence | Ek maliyet | Garanti etmediği |
|---|---|---|---|
| Bir kayıt | Bir üyenin ölçülmüş olması | En düşük | Diğer iki üyenin uygunluğu ve ortak hata |
| İki kayıt | İki ölçülmüş görüş | Orta | Üçüncü zorunlu bileşenin davranışı |
| Üç kayıt | Bütün zorunlu üyelerin ölçülmesi | Daha fazla test ve yenileme | Üçünün birlikte doğru yorumu |
| Üç kayıt + heyet kabulü | Ortak yanlışların doğrudan ölçülmesi | Ek held-out çalışma | Yeni dağılımda sıfır hata |

Nihai öneri: Üç zorunlu üyeli `PROVEN` sürecinde üç kayıt; en az iki aile; ayrıca heyet kabulü.

“İki kayıtlı heyet” ayrı bir düşük maliyet profili olarak çalışabilir. Ancak üç üyeli tam heyet sözleşmesinin koşullarını sağlıyormuş gibi gösterilmemelidir.

## 7.4. Heyet kabulü hangi düzeyde yapılmalı?

Heyet kaydı şunlara bağlanmalı:

- Üç bireysel kayıt kimliği.
- Görev profili.
- Kör üretim ve bağlam politikası.
- Eşleme/denklik sürümü.
- Retry ve ayrışma politikası.
- Yayın kapıları.

Bireysel testlerin ortak görevlerdeki çıktıları ilk ortak-hata analizinde kullanılabilir. Ancak heyet yapılandırması bu sonuçlara göre seçildiyse son kabul için yeni, önceden kullanılmamış görevler gerekir.

İlk aşamada 100 yeni heyet görevi hâlâ uygulanabilir bir sistem testi bütçesidir. Bunu güçlü bir ortak-hata sınırı diye sunmuyorum.

## 7.5. Heyet başarımının doğru paydası

Şunlar ayrı verilmeli:

- Bütün görevlerde yanlış oybirliği.
- Oybirliği çıkan görevlerde yanlışlık.
- Bütün zorunlu kapılardan sonra yayımlanan sonuçlarda yanlışlık.
- Kapsama ve gereksiz ret.

İlk iki ölçüm aynı değildir. Yalnızca çok kolay görevlerde oybirliği üreten sistem ile çok geniş kapsamada çalışan sistem aynı payda üzerinden değerlendirilmemelidir.

## 7.6. Problem türüne göre değişmeli mi?

Yeterlik kapsamı ve test içeriği değişmelidir. Ancak v1’de otomatik “risk sınıflayıcı” ekleyip gereken yeterlikli üye sayısını azaltmayı önermiyorum.

Daha basit politika:

- Tam üst heyet: Üç yeterlikli üye.
- Yerel/eksik heyet yolu: Mevcut `CERTIFIED` veya `CROSS_VALIDATED` koşulları.
- Görev kapsamı belirsizse soru.
- Matematiksel kanıtın gücü heyet eksikliği nedeniyle yanlış tanımlanmaz.
- Üst etiketin süreç koşulu eksikse üst etiket verilmez.

***

# VIII. Adversarial test sonuçları

Bunlar uygulamada çalıştırılmış sonuçlar değil; mimariyi zorlayan karşı örnekler ve kabul testleridir.

| Başarısızlık | Somut örnek | Etkilenen iddia | Koruma ve sınırı |
|---|---|---|---|
| Bütün üyeler aynı yanlış yorumu yapar | “En az” üçünde de `≤` olur | Problem uygunluğu | Kaynak eşleme, karşıt test, aktif onay; bilinmeyen hatayı tamamen dışlamaz |
| Benchmark iyi, şartname kötü | Kısa metinlerde geçen model çapraz atıflı şartı atlar | Kapsam genellemesi | Kaynak/uzunluk dışı test; yeni bütün belgeler için garanti değil |
| Aynı model adı, yeni model | Alias altında servis değişir | Kayıt sürekliliği | Snapshot, tetikleyici yenileme, sentinel; gizli değişim kalabilir |
| Reasoning bütçesi düşer | Ölçüm `high`, kullanım `low` | Yapılandırma eşleşmesi | Kayıt sayılmaz |
| Aynı ad farklı sağlayıcı | Quantization veya bağlam işleme farklı | Yol yeterliği | Yeni ölçüm veya ayrı köprü kabulü |
| Sahte kayıt | Ajan `passed=true` üretir | Yeterlik kökeni | Ajan beyanı yetkisiz; kayıt doğrulaması |
| Eski imzalı kayıt | İptal edilmiş paket geri sunulur | Güncellik | Manifest sürümü ve iptal kontrolü |
| Toplayıcı farklı modele yollar | Beklenen aile yerine aynı aile tekrarı | Heyet bileşimi | Dönen rota eşleşmesi; sunucu beyanı güven sınırı kalır |
| Şablon ailesi ezberi | Model yalnızca renderer kalıbında iyi | Dış geçerlilik | Aile/kaynak dışı kabul; ezbersizlik ispatı değil |
| Gizli set sızar | Aynı kabul soruları sürekli tekrar edilir | Test bağımsızlığı | Yenileme ve bütün girişim kaydı; sağlayıcıya gönderilen soru artık mutlak gizli değil |
| Geçerli sertifika, yanlış formülasyon | Yanlış kuvvet modelinin doğru çözümü | İstenen cevap | Formal kanıt yalnızca o modele ait |
| Ortak yanlış tanım | Bütün üyeler aynı yanlış CP referansını kullanır | Fiziksel/anlamsal bağlama | Bağımsız tanım kaynağı; çoklu LLM bunu kendiliğinden düzeltmez |
| Yanlış evaluator | Kısıt silinmesini eşdeğer sayar | Bireysel ve heyet yeterliği | Evaluator kabul paketi, mutation/negatif örnekler |
| Metamorfik ama yanlış | `0,3x` dönüşümü lineerlik testini geçer | Matematiksel doğruluk | Mutlak referans noktası |
| Profil taşınır | Cebir yeterliği MILP’ye uygulanır | Üyelik uygunluğu | Profil eşleşmesi |
| Yeni sette başarısızlık | Yeni finans yuvarlama vakası kritik hata verir | Kayıt geçerliliği | Önce referansı doğrula; sonra ilgili kapsamı askıya al |
| Ortak gizli bağlam | Ajanlar aynı aday dosyasını okur | Kör üretim | Dosya/mesaj yetkisi sınırı ve kayıt; yalnızca ayrı session ID yetmez |
| Doğru formül farklı yazılmış | Slack değişkenli model reddedilir | Yanlış ret | Göreve uygun eşdeğerlik; basit metin eşitliği değil |
| Model test sırasında doğru, rapor revizyonu değişir | Onay A, sonuç B | Yayın güvencesi | Problem/kanıt/onay revizyon bağı |

Özellikle yeni test sürümünde başarısızlık, eski kaydın sahte olduğunu otomatik kanıtlamaz. Yeni kapsam daha zor olabilir veya önceki bir açık ortaya çıkmış olabilir. Yine de doğrulanmış kritik hata mevcut kullanım kapsamındaysa ilgili yeterliği sürdürmek için eski başarıya sığınılamaz.

***

# IX. Rigor için uygulanabilir değişiklikler

## 9.1. Güncel depo durumu

Yeniden doğrulanan dal uçları:

| Dal | SHA |
|---|---|
| `main` | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` |
| `development` | `ca689154a8ced59cec2eef42f253c258b937b97b` |

Belge sürümleri değişmemiş:

- Tasarım: `a509f1287726fe8922b0d7a46fbf18e5b4d55896`
- Faz 1: `8bed859fe37cd80dc1500fb92b9dcdeeabe1b741`
- Yol haritası: `97afa66e18678bf43b758bd6ced844e46fd949e9`

Kök ağaçta planlanan ürün `src/` yapısı yok. Yeterlik sistemi çalışan kabiliyet değil, öneri/tasarım aşamasında.

Bu turda aynı büyük dosyaları yeniden kesilmiş içerikle “tam okunmuş” saymak yerine blob kimlikleri doğrulandı. Önceki eksiksiz olmayan bölüm denetimi sınırlaması devam ediyor. Yeni brief de kararların tasarıma henüz işlenmediğini belirtiyor. [concepts_brief.md]

## 9.2. Somut sözleşme metinleri

### §4.1 — Etiket ve yeterlik

> Yeterlik kaydı, tek başına bir sonuç etiketini belirlemez. Üst heyetin her zorunlu üyesi ilgili kapsam ve yapılandırmada geçerli kayda sahip olmalıdır. Matematiksel kanıt, formalizasyon uygunluğu, bireysel yeterlik ve heyet ölçümü ayrı koşullardır.

### Yeni yeterlik bölümü — Ölçümün anlamı

> Her yeterlik profili ölçülen davranışı, örnekleme birimini, görev dağılımını ve kapsam sınırını tanımlar. Dağılımsal ölçüm ile davranış/stres testleri ayrı raporlanır. Toplam istem sayısı, bağımsız genelleme örneklemi olarak sunulamaz.

### §6.4 — Heyet kabulü

> Heyet seçimi ölçüm sonuçlarına göre yapıldıysa son kabul yeni görevlerde yapılır. İlk kör adaylar, ayrışmalar ve yeniden denemeler korunur. Ortak yanlış formalizasyon oranı, kabul kapsaması ve yayımlanan sonuçlardaki hata ayrı ölçülür.

### §6.4 / §9 — Evaluator güvenliği

> Model yeterlik çalıştırması öncesinde referans formalizasyon, generator ve eşdeğerlik denetleyicisi için kabul kaydı bulunmalıdır. İnconclusive sonuç geçiş değildir. Aynı optimum, görev gerektirmedikçe tam formülasyon eşdeğerliği sayılmaz.

### §8.2 — Yeterlik paketlerinin güncelliği

> İmza doğrulaması yeterlik geçerliliği için tek başına yeterli değildir. Kayıt kapsamı, model/rota/ayar eşleşmesi, son tarih, iptal durumu ve uyumlu test/evaluator/politika sürümleri kontrol edilir. Bilinen eski manifest sessizce yeni kabul edilemez.

### §6.7–§6.8 — Raporlama

> “Yeterlikli” ifadesi görev kapsamı ve ölçüm tarihiyle birlikte kullanılır. Güven aralıkları vaka doğruluğu yüzdesi olarak sunulamaz. Tek bir heyetin bütün kapılardan geçmesi ile bütün performans aralıklarının eşzamanlı kapsama iddiası ayrılır.

### §9 — İstatistik planı

> Kabul planı sonuçlar görülmeden önce dondurulur. Sabit örneklem, sıralı izleme ve aday seçimi farklı analiz problemleridir. Çoklu karşılaştırma düzeltmesi, yapılan bilimsel iddiaya göre seçilir; otomatik uygulanmaz veya otomatik yok sayılmaz.

## 9.3. Kabul kriterleri

Öncelikli negatif testler:

- Doğru imza + iptal edilmiş kayıt → üst heyete katkı yok.
- Yeni kayıt + eski evaluator politikası → uyumluluk yoksa ret.
- Aynı kayıt adı + farklı reasoning ayarı → eşleşme yok.
- Eski manifestin geri gelmesi → downgrade uyarısı/ret.
- `UNKNOWN` evaluator sonucu → yeterlik geçişi yok.
- Yanlış referans bulunması → etkilenen bütün kayıtların yeniden değerlendirilmesi.
- Aynı optimum, farklı gerekli karar kümesi → görev ilişkisinin gerektirdiği ret.
- Aynı metamorfik ilişkileri sağlayan yanlış katsayı → mutlak referansta ret.
- Aynı kaynak belge iki kabul kümesinde → bağımsız dış doğrulama olarak sayılmama.
- Sonuçlara göre seçilen heyet → yeni son kabul kümesi gereği.
- Gizli testin sadece başarılı son çalıştırması saklanmış → kabul paketi eksik.

## 9.4. Tek geliştirici için maliyet ve kapsam

| Öneri | Katkı | Karmaşıklık | Çağrı maliyeti | Öncelik |
|---|---|---:|---:|---|
| Ölçüm/stres ayrımı | Yanlış istatistiksel iddiayı önler | Düşük | Yok | Hemen |
| Profil ve örnekleme manifesti | Kapsam taşmasını sınırlar | Düşük–orta | Yok | Hemen |
| Evaluator negatif paketi | Yanlış yeterliği azaltır | Orta | Çoğu yerel | Üst etiket öncesi |
| Sürümlü iptal/güncellik manifesti | Eski kayıt saldırısını azaltır | Orta | Yok | Dağıtılmış kayıt öncesi |
| Üç bireysel ölçüm | Bütün üyeleri kapsar | Orta | Yüksek | İlk gerçek heyet |
| Yeni heyet kabulü | Seçilim ve ortak hata kontrolü | Orta | Orta | `PROVEN` öncesi |
| Genel confidence-sequence altyapısı | Sürekli adaptif çıkarım | Yüksek | Değişken | v1’de ertele |
| Tam TUF dağıtımı | Güçlü güncelleme altyapısı | Yüksek | Yok | İhtiyaç oluşursa |
| Otomatik risk sınıflayıcı | Değişken heyet politikası | Yüksek | Ek | Şimdilik önerilmiyor |

Önce yalnızca gerçekten kullanılacak üç model–ayar–yol yapılandırması ve tek dar görev profili ölçülmeli. Bütün modellerin bütün reasoning seviyelerini baştan taramak gereksiz maliyet ve seçim yanlılığı yaratır.

***

# X. Kalan belirsizlikler ve sahip kararları

## 10.1. Bilimsel olarak kapanmayanlar

- Rigor’da üçüncü yeterlikli üyenin gerçek marjinal güvenlik katkısı.
- Seçilecek modellerin Türkçe şartname formalizasyon başarımı.
- Modelin aynı alias altında değişme sıklığı.
- Otuz günlük yenileme aralığının gerçek etkinliği.
- Evaluator’ın henüz ölçülmemiş yanlış kabul/ret oranı.
- Şablon dışı gerçek görevlerdeki başarım.
- Gizli testlerin ne kadar hızlı sızdığı veya öğrenildiği.
- Türkçe yeterlik/etiket açıklamasının kullanıcıda yarattığı güven.

Bunlar kaynak okuyarak tam kapanmaz; Rigor’a özgü deney gerekir.

## 10.2. Sahip onayı gerekenler

1. Üç zorunlu üyede üç geçerli bireysel kayıt.
2. Heyet düzeyinde yeni kabul çalıştırması.
3. 300 ölçüm + 100 stres paketinin ilk pilot bütçesi olması.
4. Geçici %80/%90 kullanılabilirlik hedefleri.
5. Sıfır kritik hata politikasının ilgili kapsamda sürdürülmesi.
6. Otuz günün idari yeniden ölçüm varsayılanı.
7. Eski Karar 5’in yeterlik temelli metinle açıkça değiştirilip değiştirilmeyeceği.
8. Bakımcı ve yerel kayıtlar için varsayılan güven politikası.

Soru 1’in kapandığını koruyorum. `CERTIFIED`ın Türkçe adı, dolaylı onay davranışı ve bağımsız denetleyicinin fazı gibi brief’te açık bırakılan tasarımcı maddelerini bu raporla onaylanmış saymıyorum. [concepts_brief.md]

## 10.3. Gerçek deney yapılmadan kullanılmaması gereken ifadeler

- “Üç modelle hata olasılığı şu kadar azaldı.”
- “Bu test kontaminasyonsuzdur.”
- “Kayıt 30 gün geçerli, model değişmemiştir.”
- “İmza doğrulandı, yeterlik gerçektir.”
- “400 test geçti, bu problem türünde güvenilirdir.”
- “Metamorfik testler geçti, doğru formülasyon kanıtlandı.”

Bunların yerine tarihli, kapsamlı ve somut ölçüm dili kullanılmalıdır.

***

# XI. Araştırmalar arası ilerleme raporu

## 11.1. Yeni kanıt ve karar matrisi

| Konu | Önceki rapor | Bu araştırmanın net ilerlemesi | Karar |
|---|---|---|---|
| Test büyüklüğü | 400 istem başlangıç önerisi | Ölçüm ve stres kanıtları ayrıldı; OC hedefleri gerektiği gösterildi | Sayı bütçe taslağı, evrensel standart değil |
| Çoklu testler | Bonferroni uyarısı | Eşzamanlı aralık, birleşik zorunlu kapılar ve aday seçimi ayrıldı | Gereksiz düzeltmeden kaçın |
| Metamorfik test | Zorunlu kombinasyon | Tutarlı fakat yanlış fonksiyon karşı örneği eklendi | Mutlak referansla birlikte kullan |
| Genelleme | Gizli/gerçek pay | Şablon ve kaynak belge düzeyinde ayrım | Rastgele satır ayrımı yeterli değil |
| Oracle | Referans incelemesi önerisi | Evaluator kabulü model testinin önkoşulu yapıldı | Önce ölçüm aracını denetle |
| Optimizasyon denkliği | Formal denklik genel başlığı | Optimum eşlemesi ve tam formalizasyon ilişkisi ayrıldı | Göreve özgü ilişki tanımla |
| Üç yeterlikli üye | Varsayılan üç | Süreç tamlığı ile ölçülmüş hata azalması ayrıldı | Üç korunuyor; üstünlük oranı iddiası yok |
| Ortak hata | LLM korelasyon kanıtı | Klasik bağımsız yazılım sürümleriyle bağımsız destek ve karşıt fayda bulgusu | Çoklu formülasyon yararlı, tek başına yeterli değil |
| Kayıt güvenliği | Hash/imza/köken | Rollback, freeze, mix-and-match eklendi | Güncellik manifesti gerekli |
| Yenileme | 30 gün + sentinel | İdari süre ile davranış sürekliliği ayrıldı | 30 gün geçici; değişimde erken iptal |
| Sürekli izleme | Haftalık kontroller | Sabit örneklem ile zaman-uniform çıkarım ayrıldı | v1’de önceden sabit izleme |
| Uygulanabilirlik | Çok profil olasılığı | İlk üç gerçek yapılandırma ve tek dar profil | Ölçüm matrisi sınırlanmalı |

## 11.2. Artık güvenle alınabilecek teknik kararlar

- Kayıt dosyası tek başına güven kaynağı olmayacak.
- İmza, yeterlik doğruluğu ve güncelliğiyle eşitlenmeyecek.
- Model testi başlamadan evaluator’ın pozitif ve negatif kabul paketi bulunacak.
- Ölçüm örnekleri ve davranış/stres örnekleri ayrı raporlanacak.
- Kaynak ve şablon aileleri test ayrımında korunacak.
- `UNKNOWN`, başarısızlık yok diye `PASS`e çevrilmeyecek.
- Üst heyet için üç bireysel kayıt önerisi, ölçülmüş ortak hata azalması iddiası olmadan uygulanacak.
- Son kabulte model/heyet seçimi etkisinden bağımsız yeni görevler kullanılacak.
- Profil, dil, rota ve ayar değişikliklerinde yeterlik otomatik taşınmayacak.

## 11.3. Bundan sonra gerçekten gerekli araştırma

Bir sonraki yüksek değerli adım yeni bir genel literatür turu değildir. Şu sınırlı deney planıdır:

1. Tek dar Rigor profilini tanımlamak.
2. Referans/evaluator kabul paketini bağımsız incelemek.
3. Sahipte mevcut üç gerçek yapılandırmayı aynı kör görevlerde ölçmek.
4. İki ve üç üyeli kabulün kapsama ve ortak hata farkını karşılaştırmak.
5. Seçilen heyeti yeni kaynaklardan gelen görevlerde sınamak.
6. Bir gerçek model/rota güncellemesinde kayıt eşleşme ve iptal davranışını test etmek.

Bu raporda model çağrısı, prototip veya test yürütmesi yapılmadı; kaynak ve depo incelemesi yapıldı. Bu nedenle sonuç “mimari güvenilirliği kanıtlandı” değildir.

Daha dar ve savunulabilir nihai sonuç şudur:

> Rigor’un yeterlik sistemi, modelleri doğru ilan eden bir liste değil; doğru tanımlanmış ölçümlerin, güvenilir kökenin, güncelliğin ve vaka düzeyindeki kontrollerin birlikte değerlendirildiği bir kabul mekanizması olmalıdır. Üç yeterlikli üye bu mekanizmanın varsayılan süreç şartı olabilir; fakat matematiksel sertifikadan veya doğru problem yorumunun kanıtından başka bir güven türüdür.