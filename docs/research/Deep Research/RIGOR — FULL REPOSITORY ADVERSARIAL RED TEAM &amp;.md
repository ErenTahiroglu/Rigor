<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Rigor — Bağımsız Red Team mimari denetimi

## I — Yönetici özeti

Tam depo için nihai güvence kararı: **INSUFFICIENT_EVIDENCE**.

Doğrudan incelenebilen tasarım ve uygulama sözleşmeleri için teknik değerlendirme: **ARCHITECTURE_CHANGES_REQUIRED**.

Bu ayrım önemlidir: Uygulamaya geçmeden değiştirilmesi gereken sözleşmeler doğrudan görüldü. Ancak uzun dosyaların kesilen bölümleri nedeniyle talep ettiğiniz eksiksiz denetimin tamamlandığını söylemek doğru olmaz. Aşağıdaki rapor, tamamlanmış bir bütün-depo güvence sertifikası değil; sabit commit üzerinde yürütülmüş, kapsamı açıkça belirtilmiş bir adversarial tasarım denetimidir.

### İncelenen sürümler

| Kaynak | Kimlik |
| :-- | :-- |
| `development` HEAD | `f7f86d3bf1726f65577cb0764d45d740588f9aac` |
| `main` HEAD | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` |
| Depodaki `concepts_brief.md` | Blob `d0e4e6969a8563b489552e153f398365f15bdd94`; 21.839 bayt |
| Eklediğiniz `concepts_brief.md` | 102.489 bayt; 94.327 karakter; 1.199 satır |
| İnceleme tarihi | 11 Kasım 2026 |

Ekli belge ile depodaki belge aynı sürüm değildir. Depodaki sürüm “taze gözle inceleme henüz yapılmadı” derken ekli sürüm yedi ajanlı taramayı, S-18’i ve birleşik karar kayıtlarını içeriyor. Bu nedenle ekli belgeyi HEAD’in parçası gibi değerlendirmedim. Ekli belgedeki S-18 ayrıca bu istemde doğrudan tekrarlanmış olduğundan, v1 önceliği bakımından açık kullanıcı talimatıdır.[^2_1]

### En önemli sonuçlar

1. Matematiksel kanıt, problem yorumunun doğruluğunu kanıtlamaz. Rigor bu ayrımı kavramsal olarak tanıyor; ancak etiket, onay ve provenance sözleşmeleri ayrımı güvenilir biçimde uygulayacak kadar kesin değil. Lean’in birincil doğrulama rehberi de “teoremin geçerli ispatı var mı?” ile “teorem ifadesi ne anlama geliyor?” sorularını açıkça ayırıyor.[^2_2]
2. `USER_DIRECT` mevcut tasarımda güvenilir bir kimlik doğrulama sonucu değil. SDK çağrısının doğrudan yapılması veya MCP elicitation yanıtının alınması tek başına insanın cevap verdiğini kanıtlamaz. Resmî Python SDK belgesi, elicitation isteğine bir ajanın otomatik yanıt üretebileceğini açıkça söylüyor. Bu, önceki denetimin önerdiği “elicitation varsa doğrudan kullanıcı onayı” varsayımını da zayıflatıyor.[^2_3]
3. Faz 1’in görülen sözleşmesi yeni etiket politikasını taşımıyor. `Label` üç değerli, `Conditions.certificate` yalnızca `"formal" | "none"`, yeterlik ve denetleyici kabul olayı yok. Bu haliyle uygulamak, daha sonraki fazlara güvenlik açısından önemli bir şema borcu taşır.
4. `unsat_core`, bağımsız kontrol edilmiş ispat değildir. Z3 belgeleri çekirdeği, sağlanamayan adlandırılmış iddiaların alt kümesi olarak tanımlar; ayrıca çekirdek desteği ile proof-term desteğini ayrı kabiliyetler olarak gösterir.[^2_4][^2_5]
5. Önceki denetim bazı doğru riskleri gereğinden kesin sonuçlarla birleştiriyor. Özellikle:
    - “Heyet ayrıştı” her zaman belirli bir formülasyonun yanlış olduğunun doğrudan kanıtı değildir.
    - “Üç aile” istatistiksel bağımsızlık sağlamaz.
    - “33–52 hafta” ve “10–15 hafta” doğrulanmış iş tahmini değildir.
    - “`PROVEN` kapatılırsa temel vaat kendiliğinden sağlanır” güvenlik açısından yetersizdir; yanlış `CERTIFIED` hâlâ kritik başarısızlıktır. Bu ifadelerin kaynakları ekli denetimdir; burada doğrulanmış ürün özellikleri olarak kabul edilmediler.[^2_1]

### Gerçekten sağlam olan taraflar

Doğrudan görülen belgelerde şu yönelimler korunmaya değer:

- LLM çıktısını çalıştırılabilir Python yerine tipli IR olarak kabul etmek.
- Eksik parametrede sessiz varsayımı yasaklamak.
- Matematiksel doğruluğu fiziksel model geçerliliğinden ayırmak.
- Çekirdeği alan paketlerinden ve LLM erişiminden ayırmak.
- Deterministik raporlama ve yeniden denetim hedeflemek.
- Desteklenmeyen matematikte açık ret üretmek.

Bunlar doğru güvenlik hedefleridir; henüz uygulanmış ve kabul testlerinden geçmiş güvenceler değildir.

______________________________________________________________________

## II — Depo envanteri ve inceleme kapsamı

### Yöntem ve sınırlar

GitHub’ın recursive-tree adresine erişim denemesi başarısız oldu. Bunun yerine kökten başlayarak bütün alt dizinleri salt okunur biçimde dolaştım. Dönen dizin listelerinde toplam 15 izlenen dosya bulundu.

Bu yöntemle recursive envanter çıkarıldı; ancak recursive Git Tree API yanıtı alınamadığı için onun `truncated` alanıyla bağımsız tamlık kontrolü yapılamadı.

Uzun dosyalar için içerik yanıtları kesildi. Aynı dosyaların sabit commit’e bağlı ham adreslerine erişim denemeleri de başarısız oldu. Kesilen bölümler okunmuş sayılmadı.

Aşağıdaki tabloda bütün depo dosyaları aynı HEAD’e bağlıdır. Blob sütunundaki değerler, okunabilirlik için ilk 12 karakterdir; commit kimliği yukarıda tam verilmiştir.

### Dosya kapsam tablosu

| Dosya yolu | Blob öneki | İşlev | İnceleme durumu | Etkilediği kararlar / sorunlar | İlişkili belgeler |
| :-- | :-- | :-- | :-- | :-- | :-- |
| `.claude/settings.json` | `5896ee4f6941` | Proje ajan eklentileri | Tam içerik görüldü | EGM ve Superpowers etkin; sürüm sabitleme görünmüyor | Plan, ekli brief |
| `.gitignore` | `34ce78935a7e` | Yerel veri ve sır dışlama | Tam içerik görüldü | Dışlama erişim kontrolü değildir; geçmiş sır taraması yapılmadı | K23, araştırma notları |
| `Handoff` | `1a1006c3e2c4` | Başlangıç kararları ve araştırma bağlamı | Tam içerik görüldü | Bağlayıcı karar / araştırma ayrımı doğru; bazı teknik iddialar aşırı güçlü | K1–K4, tasarım |
| `LICENSE` | `dd8dbdc24f15` | PolyForm Noncommercial 1.0.0 | Tam içerik görüldü | Genel kullanım anlatımı ticari kullanım istisnasını açık taşımalı | K22, README |
| `README.md` | `e9e6382ccd8c` | Kamuya açık vaat ve kullanım | Tam içerik görüldü | Eski üç etiket, bağımsız model söylemi; fakat revizyon uyarısı mevcut | Tasarım, brief, plan |
| `concepts_brief.md` | `d0e4e6969a85` | HEAD’deki revizyon taslağı | Tam içerik görüldü | Onaysız önerinin geçerli sayılması; ekli sürümle farklı | Raporlar, tasarım |
| `docs/research/2026-11-07-arastirma-notlari.md` | `a27db8173985` | Araştırma ve ortam kayıtları | Tam içerik görüldü | Birincil/ikincil ayrımı var; eski ve yeni notlar birlikte; kaynakların tümü yeniden doğrulanmadı | Handoff, tasarım |
| `docs/research/Deep Research/Soru1-1` | `d58cfc537097` | İlk etiket araştırmaları | Kısmi; yanıt kesildi | Matematik etiketi / süreç etiketi alternatifleri | Soru1-2, brief |
| `docs/research/Deep Research/Soru1-2` | `740827a586da` | Uzlaştırma araştırması | Kısmi; yanıt kesildi | `CERTIFIED`, TCB, toplayıcı sözleşmesi | Soru1-1, Soru2-1 |
| `docs/research/Deep Research/Soru2-1` | `a49fb13e41c4` | Yeterlik ve benchmark araştırması | Kısmi; yanıt kesildi | 300+100, üç üye, 30 gün; açıkça politika önerileri | CSV, brief |
| `docs/research/Deep Research/rigor_yeterlik_istatistik_hesaplari.csv` | `47a98083518b` | İstatistik hesap eki | 34 veri satırı görüldü; yeniden hesaplanmadı | Model deneyi değil, örneklem tasarımı hesabı | Soru2-1 |
| `docs/research/evidence/ek1_kuaterniyon_dcm_kontrol.py` | `4e705964b2f9` | Sembolik karşı örnek ve DCM kontrolü | Tam içerik görüldü; çalıştırılmadı | Matematiksel formül denetimi; özgün şartname doğrulanmadı | README, araştırma notları |
| `docs/superpowers/plans/2026-11-07-faz-1-cekirdek.md` | `8bed859fe37c` | Faz 1 TDD uygulama planı | Kısmi; Görev 10 içinde kesildi | IR, sayı türleri, kapılar, etiketler doğrudan görüldü | Tasarım, yol haritası |
| `docs/superpowers/plans/2026-11-07-rigor-yol-haritasi.md` | `97afa66e1867` | Paket mimarisi ve F1–F9 | Tam içerik görüldü | Sözleşme dondurma, finans sırası, MILP çıkış ölçütü | Faz 1, tasarım |
| `docs/superpowers/specs/2026-11-07-rigor-design.md` | `a509f1287726` | Ana mimari | Kısmi; §5.3 içinde kesildi | K1–K26, A1–A6, §4 etiket/onay hükümleri doğrudan görüldü | Bütün belgeler |

Ekli `concepts_brief.md` ayrı kaynak olarak incelendi. Özellikle “Tam tarama” ve “Kayıt” bölümleri doğrudan kontrol edildi; depodaki blob ile eşitlenmedi.[^2_1]

### Issues, PR’lar ve geçmiş

- Issue listelemesi: `totalCount=0`, sonraki sayfa yok.
- PR listelemesi: bütün durumlar için boş liste.
- `development` geçmişinde altı commit döndü.
- `main` HEAD’i bu geçmişte yer alıyor; onun ardından beş geliştirme commit’i bulunuyor.

`main` sonrasındaki commit konuları:

1. `52816e6…`: alan bağımsızlığı ve kapsam matrisi.
2. `fea88dd…`: alan uyarlaması ve Lean.
3. `c6bea6f…`: plan öncesi doğrulama düzeltmeleri.
4. `ca68915…`: yol haritası ve Faz 1 planı.
5. `f7f86d3…`: brief, araştırma raporları, gizlilik düzeni ve ajan ayarları.

Bu bir commit-konu karşılaştırmasıdır; `main...development` için bütün dosyaların satır satır diff denetimi tamamlanmış değildir.

### Kesin satır numarası sınırlaması

Ekli brief’in verdiği tasarım ve plan satır numaralarını yeni denetimin bağımsız kanıtı olarak kullanmadım. Uzun dosyaların tam bayt içeriği elde edilemediğinden aşağıdaki depo bulguları bölüm, görev, alan ve test adıyla konumlandırılmıştır.

Dolayısıyla talep ettiğiniz “her bulgu için kesin satır aralığı” koşulu karşılanmamıştır. Bu, nihai tamlık kararını sınırlar.

______________________________________________________________________

## III — Karar envanteri ve izlenebilirlik matrisi

### Otorite kuralı

Bu denetimde:

- Bu istemde açıkça verilen kararlar doğrudan kullanıcı talimatıdır.
- K ve S kayıtları, belgelerde sahip kararı olarak kaydedilen kararlardır.
- R ve Ö kayıtları onaylanmış sahip kararı sayılmadı.
- Bir raporun cevap olarak gösterilmesi, bütün alt önerilerin onayı kabul edilmedi.
- Teknik gereklilik, bir ürün tercihinin yerine geçirilmedi.

Özellikle HEAD’deki brief, yeterlik temelli yeni Karar 5 için “burada geçerli sayıldı; sahip itiraz ederse eski metin geri gelir” diyor. Bu, açık onay yerine itiraz etmeme varsayımı kullanıyor. Ekli yeni sürüm ise bunu yeniden “onay bekliyor” yapmış. Ekli sürüm bu yönetişim hatasını düzeltiyor; HEAD’deki kayıt düzelmiş değil.[^2_1]

### K1–K26 izlenebilirliği

| Karar | Kısa içerik | Gereksinim / sözleşme etkisi | Denetim sonucu |
| :-- | :-- | :-- | :-- |
| K1 | Genel amaçlı hibrit sistem | Yönlendirici, destek matrisi | Uzun vadeli hedef; v1 tam kapsam garantisi olamaz |
| K2 | Gecikmeden önce kesinlik | Kabul politikası, ret | “Mutlak kesinlik” uygulanabilir bir test ölçütüne çevrilmeli |
| K3 | SDK + MCP | Ortak çekirdek, iki adaptör | Korunmalı; SDK doğrudanlığı insan kimliği değildir |
| K4 | Eksikte sor, varsayma | `NEEDS_INPUT`, kaynak kaydı | S-12 devretme seçeneğinden ayrı tutulmalı |
| K5 | Kanıt raporu | Rapor–iddia bağı | Etiket ve gösterilen değer aynı kabul olayına bağlanmalı |
| K6 | Rigor LLM’i veya ajan IR’ı | Girdi kaynağı | Matematiksel ifade kaynağı ile kullanıcı kimliği ayrılmalı |
| K7 | Sade anlatım | Deterministik sunum | Sade anlatım semantik doğruluk kanıtı değildir |
| K8 | Roket matematiği kapsamı | Alan paketi ve kabul seti | Özgün şartname bu turda erişilmedi |
| K9 | Python ve MCP birinci sınıf | Adaptör eşdeğerliği | Aynı matematiksel sonuç farklı onay güveni taşıyabilir |
| K10 | Model kütüphanesi + kullanıcı seçimi | Model bağlama onayı | Otomatik model seçimi gizli varsayım üretmemeli |
| K11 | Python 3.15, eski sürüm uyumu | Paketleme ve CI | Sürüm/wheel iddiaları bu turda doğrulanmadı |
| K12 | A2 Orta İrtifa | Roket önceliği | Yarışma gereksinimleri bağımsız teyit edilmedi |
| K13 | Uçuş kodu denetimi yok | Kapsam sınırı | Matematik raporu uçuş yazılımı onayı sayılmamalı |
| K14 | Ücretsiz API + abonelikler | Erişim keşfi | Anahtar/abonelik/izin aynı kavram değildir |
| K15 | Resmî CLI erişimi | Adaptör ve sağlayıcı politikası | Sağlayıcı bazında yeniden açılmalı |
| K16 | Şubat 2027, ayrıntılı takvim yok | Kapsam ve çıkış kapıları | Tarih taahhüdü ile kapsam taahhüdü ayrılmalı |
| K17 | OpenRocket karşılaştırması | Karşılaştırma adaptörü | Matematik veya fizik doğruluğunun tek otoritesi olamaz |
| K18 | Şablon ve öz-denetim | Şablon geçerliliği | Parametre kapsamı ve bağımlılık değişimi yönetilmeli |
| K19 | Hakem ve öğrenme | Alarm çözümü | LLM güvenlik testini otomatik geçersiz kılamamalı |
| K20 | Botta yalnızca matematik | B1/B2 sınırı | Kodun gerçekten o formülü kullandığı kanıtlanmaz |
| K21 | Bot + Sentinax B1/B2 | Finans kabul paketi | Finans çekirdeği daha erkene alınabilir |
| K22 | Noncommercial lisans | Dağıtım/kullanım | Genel kullanıcı hedefiyle kullanım izinleri açık anlatılmalı |
| K23 | İki dal, özel veriler git dışında | Sürüm ve gizlilik | `.gitignore` gizlilik güvenlik sınırı değildir |
| K24 | Alan bağımsızlığı | İçe aktarma sınırı | AST testi tek başına tam bağımlılık güvencesi değil |
| K25 | Alan paketleriyle uyarlama | Paket arayüzü | Üçüncü taraf Python paketi veri dosyası gibi güvenilmez sayılamaz |
| K26 | Lean v1’de | Sandbox, challenge, comparator | Sonradan erteleme önerisi açık sahip onayı ister |

### Anti-hedefler

| Anti-hedef | Gerekli değişmez |
| :-- | :-- |
| A1 — Yanlış `PROVEN` yok | Bütün güven etiketlerinde yanlış kapsam ve yanlış kabul de yasaklanmalı |
| A2 — Gizli varsayım yok | Sayı alanı, birim tanımı, yuvarlama, model ve çözüm kapsamı açık |
| A3 — LLM kodu çalıştırılmaz | IR veri kalmalı; Lean istisnası ayrı yürütme güven sınırı |
| A4 — Anlatımda kayıtsız sayı yok | Sunum doğrulanmış sonuçtan türetilmeli |
| A5 — Jargon yok | Anlaşılabilirlik ölçülmeli; doğruluk yerine geçmemeli |
| A6 — Ajan kullanıcı cevabı uyduramaz | Kanal ismi değil, güvenilir onay kökeni gerekir |

### S serisi

| Kayıt | Durum ve etkisi |
| :-- | :-- |
| S-1 | Genel kullanıcı uzun vadeli hedef olarak korunur |
| S-2 | Metinsel girişte formülasyon olmadan matematik analizi başlayamaz; sıra görev türüne bağlı |
| S-3 | S-14 ile daraltılmış: ücretli erişim zorunlu değil, anahtar son seçenek |
| S-4 | Toplayıcı desteği, üst etikete katkı onayı değildir |
| S-5 | Ücretsiz heyet yasağı ile S-9 arasında açık politika uyuşmazlığı var |
| S-6 | Harness koşullu aday; zorunlu çekirdek bağımlılığı değil |
| S-7 | Kota/kapasite gerekçesi; doğruluk eşiği tanımlamaz |
| S-8 | Yeterlik ölçümü isteniyor; test büyüklüğü onaylanmış değil |
| S-9 | Güçlü ücretsiz modele eşit katkı; S-5’in nasıl değiştiği açık kayda bağlanmalı |
| S-10 | Kayıt dosyası varlığı, kayda güven koşulu değildir |
| S-11 | Doğrudan işlem ve metinsel işlem ayrımı; üç seçenek |
| S-12 | “Bilmiyorum” ile çözmeye devam; kapsam ve etiket açık karar |
| S-13 | İzinli CLI çağrısı; sağlayıcı şartlarına tabi |
| S-14 | Anahtar/`.env` son seçenek; genel `.env` okuma izni türetilmemeli |
| S-15 | Kayan izin ve harcama bildirimi; sert bütçe tanımlamıyor |
| S-16 | Toplayıcı katkısı açık bırakılıyor |
| S-17 | Gecikmede sahibin daha az ihtiyaç duyduğu özellik ertelenir |
| S-18 | v1 çatışmasında sahip önce; genel kullanıcı hedefini kaldırmaz |

Bu S kayıtlarının kaynak ve durum ayrımları ekli brief’in “Kayıt” bölümünde bulunuyor.[^2_1]

### R, Ö ve açık kararlar

- R-1: Dört etiket ve dört alanlı kutu.
- R-2: Üç yeterlikli üye, iki aile, heyet testi.
- R-3: Yapılandırmaya bağlı yeterlik.
- R-4: 300+100, pilot, başarı eşikleri.
- R-5: Değerlendiricinin önce sınanması.
- R-6: 30 gün ve değişiklikte geçersizlik.
- R-7: Danışman üye, çoğunlukla ayrışmayı kapatmama.
- R-8: Faz yerleşimi.

Bunların tamamı araştırma önerisidir. Özellikle R-2, R-4 ve R-6 bilimsel zorunluluk değildir. Ekli kayıt da bunları kalem kalem onay bekleyen öneriler olarak sınıflandırıyor.[^2_1]

Ö-1-1…Ö-1-9, Ö-2-1…Ö-2-6, Ö-3-1…Ö-3-13, Ö-4-1…Ö-4-6, Ö-5-1 ve Ö-T aynı şekilde öneri statüsündedir. “Ö-T” çok sayıda alt değişikliği tek torbaya koyuyor; ayrı onay ve test izlenebilirliği için atomik maddelere ayrılmalıdır.[^2_1]

Açık A-1…A-11 kayıtlarından A-1, S-18 ile kapanmıştır. Diğerlerinin güvenli varsayılanları XIV. bölümde veriliyor.[^2_1]

Bu matris kararların doğrudan görülen sözleşmelere eşlemesidir; kesilen belge bölümleri nedeniyle bütün gereksinim ve testlere kadar eksiksiz izlenebilirlik matrisi değildir.

______________________________________________________________________

## IV — Karar ve belge çakışmaları

| Kimlik | Çakışma | Sonuç |
| :-- | :-- | :-- |
| C-01 | Tasarım “ONAYLANDI”; okuma kuralı tasarımcı kararlarını ayrıca onay bekleyen sayıyor | Belge onayı ile madde onayı ayrılmalı |
| C-02 | Sahip kararları “değiştirilemez”; yeni sahip kararları eskilerini değiştiriyor | `supersedes` / yürürlük kaydı gerekli |
| C-03 | HEAD brief’i Ö-2-1’i onaysız geçerli sayıyor; ekli brief onay bekliyor diyor | HEAD yönetişim kaydı eski |
| C-04 | Tasarım §1.1 her olumlu sonuçta onay istiyor; S-12 onaysız devamı mümkün kılıyor | Yayın kapsamı ve onay türü yeniden tanımlanmalı |
| C-05 | Yeni `CERTIFIED`; Faz 1 üç etiketli | Etiket şeması uygulamadan önce değişmeli |
| C-06 | Etiketler sırasız; belgelerde “en az/en fazla” kullanılıyor | Kabul kümeleri veya açık politika predikatları gerekli |
| C-07 | `USER_DIRECT` SDK/elicitation kanalına bağlanmış | Kanal, insan kimliğinin kanıtı değil |
| C-08 | `rational` ve `decimal`; derleyiciler integer dışını real yapıyor | Matematiksel semantik kaybı |
| C-09 | Çözüm kümesi önerisi; `Outcome.values` tek değer sözleşmesi | `SolutionSet` veya açık aday kapsamı gerekli |
| C-10 | S-18 sahip önceliği; finans F7’de | Teknik bağımlılıktan kaynaklanmayan gecikme |
| C-11 | K26 Lean v1; yeni erteleme listesinde ilk ertelenen | Sahip onayı olmadan ertelenemez |
| C-12 | “Kod denetimi yok”; “canlıya alma kapısı” anlatımı | Raporun yazılım güvenliği onayı gibi kullanılma riski |

C-04, C-06, C-09 ve C-11’in yeni karar tarafı ekli belgededir; bunların tasarıma işlenmediği de açıkça belirtiliyor.[^2_1]

README için önemli düzeltme: Eski tabloyu hâlâ içeriyor, fakat bunu saklamıyor. Başında açık revizyon uyarısı var. Dolayısıyla “README hiçbir uyarı vermeden eski sözleşmeyi güncel sunuyor” bulgusu doğru olmaz. Sorun, uyarıya rağmen aynı sayfada güçlü eski vaatlerin bulunmasıdır.

______________________________________________________________________

## V — Matematiksel doğruluk ve sertifika denetimi

### 1. Etiketin nesnesi açık olmalı

Önerilen asgari ayrım:

- Matematiksel iddia: Tam olarak hangi önerme kontrol edildi?
- Problem yorumu: Bu önerme kullanıcının istediği şeyi temsil ediyor mu?
- Girdi kökeni: Sayılar ve koşullar nereden geldi?
- Yayın politikası: Hangi koşullarda nihai cevap gösterilebilir?

Bunun için tam bir iddia–kanıt grafiği zorunlu değil. Tek sonuç için birkaç tipli kayıt yeterlidir.

Örneğin:

> Matematiksel iddia: Uluslararası foot tanımı altında verilen değerin metre karşılığı.\
> Sertifika: Belirtilen denetleyici kabul etti.\
> Problem yorumu: Ajan tarafından çıkarıldı; insan tarafından doğrulanmadı.\
> Sınır: Kaynak belgenin eksiksiz aktarımı ve fiziksel ölçüm doğrulanmadı.

Bu ayrım formal ispatın kapsamıyla uyumludur; doğal dil niyetine ilişkin koşulsuz garanti üretmez.[^2_2]

### 2. `unsat_core` ve `unsat` ayrı kanıt türleridir

Şunlar eşit değildir:

1. Z3 `unsat` döndürdü.
2. Z3 bir unsat core döndürdü.
3. Z3 proof object üretti.
4. Uygun bir denetleyici proof object’i asıl formüle karşı kabul etti.

Birinci ve ikinci sonuçlar, solver’a güvenilen bir doğrulama yolunda kullanılabilir. Fakat “çözücüden bağımsız sertifika kontrolü” diye adlandırılamaz. Z3 belgeleri bu kabiliyetleri ayırıyor.[^2_5][^2_4]

Önceki B-3 önerisinin de düzeltilmesi gerekir: “Z3 hükmü en çok `CROSS_VALIDATED`” demek, gerçekten ikinci yöntem çalıştırılmadıysa yapılmamış çapraz doğrulama iddia eder. Güvenli davranış, mevcut dört etiket böyle bir durumu karşılamıyorsa nihai güven etiketi vermemek veya açık `solver_verdict` tanı kaydı üretmektir.[^2_1]

### 3. Çözüm üyeliği ve tamlığı

$$
f(2)=0,\qquad f(3)=0
$$

yalnızca 2 ve 3’ün kök olduğunu gösterir.

$$
\operatorname{Roots}(f)=\{2,3\}
$$

ise başka kök bulunmadığını da gerektirir.

Sertifika şu ayrımı taşımalı:

- `WITNESS_VALIDITY`: Sunulan adaylar geçerli.
- `COMPLETENESS`: Sunulan küme bütün çözümleri içeriyor.
- `UNIQUENESS`: İstenen kapsamda tek çözüm var.

Örneğin $x(x-1)=0$ için yalnızca $x=0$ geri koymasını kabul etmek, tam çözüm iddiasını doğrulamaz. Bu matematiksel karşı örnektir; Rigor üzerinde çalıştırılmış test değildir.

### 4. Sayı alanı kaybı

Faz 1 Görev 8’de:

- SymPy: integer dışı semboller `real=True`.
- Z3: integer dışı değişkenler `Real`.

Bu, `domain="rational"` için semantiği korumaz.

Karşı örnek:

$$
x\in\mathbb{Q},\quad x^2=2
$$

rasyonel çözüm içermez; reel alana genişletmek $\pm\sqrt2$ üretir.

Çözüm:

- Desteklenen alanlar motor başına açık olmalı.
- Alanı koruyamayan derleme reddedilmeli.
- Sonradan aday filtrelemek, özellikle `forall`, tutarlılık ve tamlık iddialarında genel çözüm değildir.


### 5. Decimal gerçek sayı değildir

Finansal Decimal işlemi yalnızca ondalık sayıyı rasyonel olarak okumak değildir. Hassasiyet, yuvarlama modu, işlem sırası, quantize noktaları ve istisna politikası sonucun parçasıdır.

Örneğin düşük hassasiyetli ondalık yürütmede:

$$
(1/3)\times3
$$

ile önce cebirsel sadeleştirme yapmak aynı operasyonel sonucu vermeyebilir.

Bu nedenle iki iddia ayrılmalı:

- Kesin matematiksel ifade.
- Belirtilen Decimal yürütme politikasının çıktısı.

Dar rasyonel denetleyici, bu ayrımı yapmadan finansal mutabakatı sertifikalandıramaz.

### 6. Aralık kapsama, eşitlik değildir

Bir residual aralığının sıfırı içermesi:

$$
0\in R
$$

residual’ın sıfır olduğunu kanıtlamaz.

FLINT belgeleri bunu açıkça ayırıyor: Sıfırı dışlayan aralık eşitsizliği kanıtlayabilir; sıfırı içeren aralık hem sıfırla hem küçük sıfır olmayan değerlerle uyumludur.[^2_6][^2_7]

Faz 1’in sertifika uygulama adımları kesildiğinden Rigor’un bu hatayı yaptığını doğrulamadım. Bu madde doğrulanmış uygulama açığı değil, zorunlu negatif testtir.

### 7. MILP için dual sertifika çıkış ölçütü fazla geniş

Yol haritası F8, “LP/MILP altın testleri `PROVEN` — dual sertifikalı” diyor.

LP dualitesi, uygun koşullarda LP optimumunu doğrulayabilir. MILP’nin genel tamsayılı optimumu için LP gevşetmesinin dual sertifikası tek başına yeterli değildir.

Karşı örnek:

$$
\max x,\quad 2x\le3,\quad x\in\mathbb Z_{\ge0}.
$$

LP gevşetmesinin optimumu $1{,}5$, tamsayılı optimum 1’dir. Genel MILP kabulü, tamsayılı uygunlukla birlikte küresel üst/alt sınırı kapatan ek kanıt gerektirir.

F8 çıkış ölçütü LP, MILP ve konveks KKT yollarına ayrılmalıdır. Bu karşı örnek analitiktir; solver deneyi yapılmadı.

______________________________________________________________________

## VI — Güvenlik ve tehdit modeli

### Aktör ve güven sınırı

| Aktör | Yapabilecekleri | Korunması gereken |
| :-- | :-- | :-- |
| Dürüst fakat hatalı ajan | Yanlış IR, eksik kaynak | Semantik hata ve eksik parametre yakalama |
| Yalan söyleyen araç çağırıcısı | “Kullanıcı onayladı” argümanı | Onayın çağırıcı beyanından türememesi |
| Yetki aşmaya çalışan ajan | Bütçe/sağlayıcı değiştirme | Yetki artışının ayrı güven sınırı |
| Aynı kullanıcıda shell ajanı | Dosya, ayar, alt süreç değiştirme | Uygulama içi yasakların sınırını kabul etmek |
| Yerel saldırgan | Rapor, kayıt, ikili değiştirme | Güvenilir doğrulayıcı/anahtar ayrımı |
| Güvenilmeyen belge | Prompt injection, kaynak yanıltma | Veri–talimat ayrımı ve kaynak bağlama |
| Harici sağlayıcı | Yanlış model kimliği, değişen davranış | Hizmet beyanının kanıt gücünü sınırlamak |

### Kritik yeni sonuç: elicitation insan onayı kanıtı değildir

Resmî Python SDK metni, istemcinin ajan olması halinde kullanıcıya sormak yerine otomatik yanıt üretebileceğini söylüyor. Claude SDK belgeleri de elicitation hook’larının yanıtı programatik işleyebilmesini ve değiştirebilmesini belgeliyor.[^2_8][^2_3]

Dolayısıyla:

```text
channel == "elicitation" → USER_DIRECT
```

güvenli bir genel kural değildir.

Daha doğru kayıt:

```text
transport_channel
responding_principal
human_presence_evidence
trusted_ui_identity
challenge_binding
```

Bunların hepsi her platformda kanıtlanamaz. Kanıtlanamıyorsa rapor bunu açıkça söylemeli.

### SDK doğrudanlığı da kimlik değildir

Faz 1 testinde:

```python
USER = Provenance(K.USER_DIRECT, "sdk")
```

üretiliyor. SDK’yı bir ajan da çağırabilir. Çağıran kodun provenance nesnesi oluşturabilmesi, insan kimliği doğrulaması değildir.

Güvenlik açısından önemli olgular normal kullanıcı verisi gibi alınmamalı; güvenilen onay adaptörü tarafından üretilmeli. Aynı kullanıcı hesabında tam shell saldırganına karşı bunun da sınırlı olduğu belirtilmeli.

### Hash ve imza sınırı

SHA-256 içerik kimliği sağlar; yazarı veya kullanıcı onayını doğrulamaz. Aynı yetkili saldırgan içerikle hash’i birlikte değiştirebilir.

HMAC/imza ancak saldırganın anahtara ve imzalama yetkisine erişemediği bir güven sınırı varsa fayda sağlar. “Anahtar proje dizini dışında” tek başına yeterli değildir; aynı OS kullanıcısındaki ajan keychain erişimini veya imzalama servisini kullanabiliyorsa sınır yine aşılabilir.

### Dört ayrı izin

1. Matematiksel tanımı kabul etme.
2. İş akışını devretme.
3. Belirli veriyi belirli sağlayıcıya aktarma.
4. Belirli kaynak/bütçeyi harcama.

Birinci izin diğer üçünü, “devral” izni de eksik değer uydurmayı kapsamaz.

### Uzun işler

Asgari iş sözleşmesi:

- Kalıcı `job_id`.
- Kimliği belirli problem snapshot’ı.
- Tek yürütme sahibi veya lease.
- Çağrı öncesi atomik bütçe rezervasyonu.
- İptal ve yeniden başlatma semantiği.
- Tekrarlanan istekte idempotency.
- Sağlayıcı/model değişirse yeniden yeterlik değerlendirmesi.
- Ağ sonucu belirsizse aynı ücretli çağrıyı kör tekrar etmeme.

Ayrı süreç veya kilit dosyası tek başına bu koşulları sağlamaz.

______________________________________________________________________

## VII — LLM ve hakem heyeti mimarisi

### Yeterlik eşiklerinin anlamı

300+100, üç üye, iki aile ve 30 gün:

- Bilimsel doğruluk garantileri değil.
- Belirli dağılım ve çalışma koşullarına bağlı kabul politikaları.
- Vaka başına doğruluk yüzdesi değil.
- Doğal dil niyetinin ispatı değil.

CSV’nin 34 satırı bu turda yeniden hesaplanmadı. Önceki belgenin “bütün satırlar yeniden hesaplandı” beyanı yeni denetimin hesap kanıtı sayılmadı.[^2_1]

Sıfır hata için kullanılan:

$$
p_U=1-\alpha^{1/n}
$$

ifadesi sabit yapılandırma, uygun örnekleme ve bağımsız Bernoulli denemeleri varsayar. Şablon varyantlarını, tabakalı görevleri ve adaptif tekrarları aynı bağımsız örnekler gibi saymak bu yorumu bozar.

### İki aşamalı kabul önerisi de yeniden tasarlanmalı

Önceki öneri, ilk 300’de bir hata olursa yeni 300’de sıfır hata ile geçişi mümkün kılıyor. Önceden belirlenmiş olması, tek aşamalı testin güven sınırlarını kendiliğinden korumaz.

Gerekli olan:

- Bütün durdurma ve kabul yollarının tanımı.
- Her gerçek hata oranında kabul olasılığı.
- Hangi istatistiksel iddianın raporlandığı.
- İlk hatanın silinmemesi.
- Kritik hata sınıfına göre güvenlik politikası.

Bu plan kullanılabilir; fakat eski “300 sıfır hata” yorumu yeni plana aynen taşınamaz.

### Aile çeşitliliği ve ortak hata

Ayrı sağlayıcı, ayrı model ailesi demek değildir. Ayrı model ailesi de hata bağımsızlığı demek değildir.

Rigor için ölçülmesi gereken olay:

> Aynı problemde bütün zorunlu formülatörlerin aynı yanlış semantiği üretmesi ve sonraki kapıların bunu kaçırması.

Önceki M-22’nin sayısal korelasyon aktarımı bu turda makalenin kendisinden yeniden doğrulanmadı. “Üç üye ≈1,7 bağımsız üye” Rigor’un güvence hesabında kullanılmamalı.[^2_1]

### Sağlayıcı koşulları

| Sağlayıcı | Doğrudan doğrulanan | Desteklenmeyen genelleme | Mimari sonuç |
| :-- | :-- | :-- | :-- |
| Anthropic | Hukuki sayfa geliştiricilere API anahtarı yolunu öneriyor; kullanıcı adına abonelik üzerinden yönlendirmeyi yasaklıyor; değiştirilmemiş Claude Code’a kullanıcının kendi girişi için istisna açıklıyor | Her yerel `claude -p` sarmalayıcısının kesin yasak veya kesin serbest olduğu | Rigor kullanım modeli için açık uygunluk değerlendirmesi; varsayılan otomatik açılmamalı [^2_9] |
| OpenAI | `codex exec` betik/CI için belgeli; kaydedilmiş CLI kimliğini kullanabiliyor; public/OSS uyarısı belirli ChatGPT-managed CI/CD akışında | “Açık kaynak araç Codex aboneliği kullanamaz” genel sonucu | Yerel otomasyon ile CI kimlik dosyası taşımasını ayır [^2_10] |
| OpenAI | Sign in with ChatGPT için app-server entegrasyonu da belgeleniyor | Her uygulamanın koşulsuz uygun olduğu | Yetkilendirilmiş entegrasyon yolu ayrıca değerlendirilmeli [^2_11] |
| Google | Headless mod ve mevcut kimlik kullanımı belgeli; OAuth üzerine üçüncü taraf piggyback yasak | CLI’ı her başsız çağırmanın kesin izinli olduğu | API yolu güvenli varsayılan aday; sarmalayıcı ayrımı açıklığa kavuşturulmalı [^2_12][^2_13][^2_14] |

Önceki B-5’teki OpenAI yorumu bu nedenle daraltılmalıdır: CI uyarısını bütün yerel açık kaynak entegrasyonlarına yaymak kanıtın kapsamını aşar.

Bu bir hukuki uygunluk görüşü değildir. İncelenen sayfalar teknik ve politika belgeleridir; bütün bağlantılı hizmet sözleşmeleri, ülke ve hesap türleri bakımından tam hukuki inceleme tamamlanmadı.

### DeepSeek Harness

Gerçek proje `deepseek-ai/deepseek-harness` ve ürün adı `dsh`’dir. DeepSeek’in resmî sayfası bunu Cordis tabanlı, eklenti mimarili, masaüstü veya web arayüzüyle çalışan bir ajan harness’i olarak tanımlıyor. Matematiksel sertifika çekirdeği veya bağımsız theorem checker olarak tanımlamıyor.[^2_15][^2_16]

Rigor açısından olası rolü:

- İsteğe bağlı istemci.
- Kullanıcı etkileşim kabuğu.
- İş akışı ve eklenti entegrasyonu.

Öneri: Güven çekirdeğine alınmasın. “Harness var” gerekçesiyle model bağımsızlığı, güvenilir onay veya ispat güvencesi türetilmesin.

______________________________________________________________________

## VIII — Teknik sözleşmeler ve uygulamaya hazırlık

### Asgari sonuç sözleşmesi

Aşağıdaki yapı öneridir; onaylanmış mevcut karar değildir:

```text
ProblemSnapshot
  schema_version
  semantic_policy_id
  canonical_bytes_hash
  source_manifest_hash

Claim
  problem_snapshot_id
  goal_kind
  domain
  assumptions
  result_scope

CheckReceipt
  claim_hash
  certificate_hash
  checker_id
  checker_version
  checker_policy_hash
  result: ACCEPT | REJECT | UNKNOWN

ConfirmationReceipt
  problem_snapshot_id
  decision
  channel
  responding_principal
  assurance_basis

Outcome
  claim
  result
  checks
  interpretation_status
  provenance_status
  label_policy_id
  publication_decision
```

Temel değişmez:

$$
H_{\text{gösterilen}}
=
H_{\text{onaylanan}}
=
H_{\text{çözülen}}
=
H_{\text{sertifika}}
=
H_{\text{raporlanan}}.
$$

Eşitlik yalnızca ham IR’ı değil, anlamı etkileyen birim ve politika bağlamını da kapsamalı.

### Doğrudan görülen sözleşme boşlukları

| Alan | Sorun | Gerekli test |
| :-- | :-- | :-- |
| `frozen=True` + `list[...]` | Üst nesnenin alan atamasını kapatmak, iç listelerin değişmezliğini tek başına sağlamaz | Onaydan sonra `args`, `relations`, `quantities` değiştirilmeye çalışılsın |
| `Quantity.domain` | Rational/Decimal semantiği derleyicide korunmuyor | Alanlar arası karşı örnekler |
| Birim kapısı | Boyut uyumu ile ölçek/ofset normalizasyonu ayrı sözleşme olarak görünmüyor | `m/cm`, `kg/g`, `degC/K` karışık çözüm |
| `SourceRef.detail` | Serbest metin kaynak sadakatini kanıtlamaz | Yanlış hücre/yanlış satır ama geçerli hash |
| `Conditions` | Güven olguları boolean olarak taşınıyor | Çağırıcı sahte `paths_agree=True` veremesin |
| `Outcome.values` | Çözüm kümesi, koşullu sonuç, aralık kapsamı yok | Çok kök, boş küme, parametrik sonuç |
| JSON sınırı | Anahtar tekrarının reddi görülmüyor | Ham metinde iki `goal` / `value` |
| Kanonikleştirme | Sözdizimsel içerik kimliği ile matematiksel denklik ayrılmıyor | `"0.1"` / `"1/10"` farklı içerik, aynı değer |
| `eval_arb` hassasiyeti | Global bağlamın geçici değiştirilmesi eşzamanlılık riski | İki farklı hassasiyetli paralel iş |
| Mimari AST testi | Göreli/dinamik/transitif import kapsamı açık değil | Yasak bağımlılığı farklı yollarla ekleme |

Bu maddelerin bir kısmı doğrulanmış şema eksikliği, bir kısmı tasarım riskidir; uygulanmış ürün açığı olarak sunulmuyor.

### Parser

Python AST beyaz listesi kod yürütme riskini azaltabilir. Ancak tek başına:

- Derin ağaç.
- Aşırı büyük tamsayı.
- Dev üs.
- Uzun token.
- Bellek tüketimi.
- Unicode benzer karakter.
- İfade normalizasyonu.

risklerini çözmez.

Parser ve her solver alt süreci için kaynak limitleri gerekir. “`eval` yok” güvenli yürütmenin tamamı değildir.

### Replay

Üç işlem ayrılmalı:

1. Saklanan kanıtı yeniden kontrol etme.
2. Saklanan model çıktısını yeniden puanlama.
3. Uzak modeli yeniden çağırma.

Üçüncüsü aynı yürütmenin tekrarı değildir. Yeni sağlayıcı davranışı, model kimliği veya maliyet doğurabilir.

Tarihsel rapor da iki soruyu ayrı cevaplamalı:

- O günkü politika altında kabul edildi mi?
- Bugünkü politika altında yeniden kabul ediliyor mu?

______________________________________________________________________

## IX — Yol haritası ve kapsam analizi

### Üç uygulanabilir alternatif

| Alternatif | İçerik | Ertelenenler | Güvence sınırı |
| :-- | :-- | :-- | :-- |
| Güvenli en küçük çekirdek | Tipli IR, kesin rasyonel hesap, dar checker, kaynak bağlama, deterministik rapor, SDK | Doğal dil, heyet, CLI sürme, Lean, PDF/DOCX | Yalnızca desteklenen açık matematiksel iddialar |
| Sahibin ihtiyaçlarını karşılayan v1 | Çekirdek + roketin seçilmiş hesapları + finans B1/B2 + ince MCP + OpenRocket veri karşılaştırması | Genel kullanıcı onboarding’i, geniş alan paketleri, öğrenen hakem, tam heyet | Roket simülasyonu ve istatistikte açık çapraz doğrulama sınırı |
| Hedef mimari | Doğal dil, yeterlik, çoklu formülasyon, Lean, toplayıcılar, belge okuyucular, geniş paket ekosistemi | Kademeli yayımlama | Her kabiliyet kendi kabul ve tehdit modeliyle |

S-18 nedeniyle önerilen v1 ikinci alternatiftir. Bu öneri, uzun vadeli genel kullanıcı hedefini kaldırmaz.[^2_1]

### Ertelenemeyecekler

- İddia–sertifika–rapor bağlama.
- Sayı alanı ve Decimal semantiği.
- Birim ölçeği/ofseti.
- `UNKNOWN` ile `ACCEPT` ayrımı.
- Etiket kabul politikası.
- Güvenilir onay sınırının dürüst tanımı.
- Çözüm üyeliği/tamlık ayrımı.
- Kaynak limitleri.
- Uzak çağrı varsa veri izni ve bütçe.


### Ertelenebilecekler

Sahip onayıyla:

- `PROVEN` ürün etiketi.
- Genel doğal dil yolu.
- Üç üyeli yeterlik altyapısı.
- Lean entegrasyonu.
- PDF/DOCX okuyucular.
- Öğrenen hakem.
- Geniş alan paketi araçları.
- Toplayıcıların üst etikete katkısı.

K26 nedeniyle Lean’in ertelenmesi otomatik teknik karar değildir; açık sahip kararı gerekir.

### Önerilen bağımlılık sırası

```text
İddia ve etiket semantiği
        ↓
Sayı alanı + birim semantiği
        ↓
Snapshot ve sertifika bağlama
        ↓
Dar denetleyici + negatif kabul paketi
        ↓
SDK + deterministik rapor
        ↓
Finans mutabakatı / seçilmiş roket hesapları
        ↓
MCP ve güvenilir onay adaptörü
        ↓
Doğal dil ve sağlayıcı adaptörleri
        ↓
Değerlendirici kabulü
        ↓
Yeterlik ölçümü ve heyet
        ↓
Lean / geniş alanlar / öğrenme
```

Yeterlik şemasının erken tasarlanması döngüsel değildir. Gerçek ölçümü, henüz kabul edilmemiş değerlendiriciye bağlamak döngüsel güvence üretir. Önceki M-4 bu iki durumu yeterince ayırmıyor.

Takvim için doğrulanmış kapasite verisi yok. Bu nedenle ne “kesin yetişmez” ne “10–15 haftada sığar” sonucu veriyorum.

______________________________________________________________________

## X — Önceki Red Team denetiminin denetimi

Aşağıdaki değerlendirme ekli belgedeki bütün B, M ve m kimliklerini kapsar. Ancak “doğrulandı” yalnızca doğrudan görülen kısmı ifade eder; kesilen kaynaklara dayanan ayrıntılar açık kalır.[^2_1]

### B bulguları

| Bulgu | Yeniden değerlendirme |
| :-- | :-- |
| B-1 | Kısmen doğrulandı. Onay çatışması gerçek; ajan kaçış zincirinin son uygulaması görülmedi |
| B-2 | Kısmen doğrulandı. Tek karar sözleşmesi gerekli; ayrışma tek başına belirli adayın yanlışlığının kanıtı değil |
| B-3 | Doğrulandı, çözüm yetersiz. Solver/checker ayrımı gerekli; yalnızca `fractions`/`decimal` kullanmak sağlamlık kanıtı değil |
| B-4 | Destekleniyor. Aynı yetkili shell tehdidi gerçek; önerilen keychain+nonce tam çözüm değil |
| B-5 | Kısmen doğrulandı. Anthropic/Google riski var; OpenAI CI uyarısı genellenmiş |
| B-6 | Kısmen doğrulandı. Faz önceliği sorunu var; hafta tahminleri doğrulanmadı |
| B-7 | Öncelik çatışması S-18 ile artık açık değil. Erteleme ayrıntıları hâlâ onay bekliyor |
| B-8 | Doğrulandı: görülen Faz 1 şemaları eski. Kesilen görevler yeniden kontrol edilmedi |
| B-9 | Matematiksel olarak doğrulandı. Önerilen tamlık yollarının her biri ayrıca sağlamlık koşulu ister |
| B-10 | Kısmen çözülmüş. Ekli kayıt daha iyi; HEAD farklı ve durum çelişkileri sürüyor |

### M bulguları

| Bulgu | Yeniden değerlendirme |
| :-- | :-- |
| M-1 | Destekleniyor; yeni orchestration çekirdeğin dışında kalmalı |
| M-2 | Destekleniyor; “tek çağrı asla olmaz” fazla mutlak, kalıcı iş modeli daha güvenilir |
| M-3 | Destekleniyor; gizli sistem isteminin hash’ini istemek her sağlayıcıda uygulanabilir değil |
| M-4 | Kısmen doğrulandı; şema tanımı ile gerçek ölçüm ayrılmalı |
| M-5 | Yeni kanıt gerekli; şablon bölümünün tamamı görülmedi |
| M-6 | Destekleniyor; önerilen yoklama sorularının başarısı ölçülmüş değil |
| M-7 | Destekleniyor; bütün platform uygulamaları görülmedi |
| M-8 | Destekleniyor; izin/bütçe şeması açık |
| M-9 | Makul HCI riski; Rigor üzerinde ölçülmüş değil |
| M-10 | Destekleniyor; AST alternatifi kaynak tüketimini ayrıca sınırlamalı |
| M-11 | Destekleniyor; “her sayı kaynakta geçmeli” kuralı fazla katı |
| M-12 | Kısmen doğru. Sampling istemci aracılıdır; aynı aile olmasını protokol zorunlu kılmaz |
| M-13 | İstatistiksel kaygı doğru; sıfır toleransı heyete taşımak kendiliğinden güvenli değil |
| M-14 | Fazla güçlü. Aynı istemci aynı model/aile olmak zorunda değil; etiket katkısı gerçek kimliğe bağlı |
| M-15 | Öneri, zorunluluk değil. Kaynak alıntısı sıkıştırma olmadığını kanıtlamaz |
| M-16 | Destekleniyor; tohum planı benchmark güvenliğinin tamamını çözmez |
| M-17 | Destekleniyor; imza yanında freshness/rollback gerekli |
| M-18 | Kısmen doğrulandı; S-18 ile “sahip önce” artık eski hata değil, güncel öncelik |
| M-19 | Destekleniyor; aynı saldırgan doğrulayıcıyı da değiştirebiliyorsa `verify-report` yetmez |
| M-20 | Kısmen doğrulandı; görülen enum yeni durumları taşımıyor |
| M-21 | Destekleniyor; silinebilir ortam değişkeni saldırgan özyinelemeye karşı yetki sınırı değil |
| M-22 | Yeniden kaynak doğrulaması tamamlanmadı; Rigor’a sayısal etkin-üye hesabı taşınamaz |

### m bulguları

| Bulgu | Yeniden değerlendirme |
| :-- | :-- |
| m-1 | “Düzeltildi” durumu sürümler arasında eksiksiz karşılaştırılmadı |
| m-2 | Kısmen doğrulandı; Faz 2 okuyucuları yol haritasında görüldü |
| m-3 | Yeni kanıt gerekli; satır referanslarının tamamı yeniden doğrulanmadı |
| m-4 | Geri çekme ekli belgede var; teknik gerekçesi kesin kanıt değil |
| m-5 | 12 ifade sayımı yeniden yapılmadı |
| m-6 | Kısmen doğrulandı; README eski, fakat açık revizyon uyarısı var |
| m-7 | OpenRocket CSV kabiliyeti bu turda birincil kaynaktan doğrulanmadı |
| m-8 | F8’in bütün tüketicileri doğrulanmadı; kapsam çıkarımı olarak kalır |
| m-9 | Destekleniyor; sürümlü politika doğru yönelim |
| m-10 | Destekleniyor; tarihsel yürütme kanıtı gerekliliği korunmalı |
| m-11 | Belge yapısı değerlendirmesi makul; güvenlik engelleyicisi değil |


______________________________________________________________________

## XI — Toplu Red Team bulgu kayıtları

Bu bölümdeki bütün depo bulguları yukarıdaki HEAD’e bağlıdır. Kesin satır aralığı sağlanamayan yerlerde görev/bölüm verilmiştir; bu eksiklik saklanmamıştır.

### RT-001 — Onaylanmamış önerinin yürürlükte sayılması

- Önem: HIGH.
- Kanıt: VERIFIED.
- Konum: Depodaki `concepts_brief.md`, “Karar 5’in yeni metni”.
- Çatışma: Açık sahip onayı / “itiraz ederse geri gelir”.
- Başarısızlık: Uygulayıcı ücretsiz heyet politikasını sahibi onaylamış gibi kodlar.
- Düzeltme: `proposed/accepted/superseded/rejected` durumları; kabul kanıtı.
- Alternatif: Açık kararda güvenli varsayılan.
- Maliyet: Düşük; bütün belgelere etkili.
- Kalan risk: Belge yazarının yanlış otorite atfetmesi.
- Test: Onay kaydı olmayan politika üretim yapılandırmasına geçemesin.
- Sahip onayı: Politika içeriği için gerekli.


### RT-002 — Etiket sözleşmesi yeni güven modelini taşımıyor

- Önem: BLOCKER.
- Kanıt: VERIFIED.
- Konum: Faz 1 Görev 9; tasarım §4.1–§4.4.
- Hata: `CERTIFIED`, checker kabul olayı, yeterlik ve ayrıntılı ret ayrımı yok.
- Başarısızlık: Sertifikanın varlığı, gerçekten kabul edilmişliği yerine kullanılır.
- Düzeltme: Tek, sürümlü etiket kararı; tipli kontrol kayıtları.
- Alternatif: Güven etiketi yayımlamayan tanı modu.
- Maliyet: Orta; erken yapılırsa sınırlı.
- Etki: Session, rapor, MCP, replay, şablonlar.
- Test: Bütün koşul kombinasyonları; başarısız sertifikada olumlu etiket yok.
- Sahip onayı: Etiket anlamı için gerekli.


### RT-003 — Kanal temelli sahte doğrudan onay

- Önem: BLOCKER.
- Kanıt: VERIFIED.
- Konum: Tasarım §4.3; Faz 1 Görev 9 provenance testi.
- Başarısızlık: Ajan SDK’dan veya elicitation handler’dan “kullanıcı onayı” üretir.
- Koruma yetersizliği: Kanal adı insan kimliği değildir.[^2_3]
- Düzeltme: Güvenilen onay adaptörü; challenge’ı problem snapshot’ına bağlama.
- Alternatif: İnsan kökeni doğrulanamadığında üst süreç etiketi kapalı.
- Maliyet: Orta–yüksek; platforma bağlı.
- Kalan risk: Aynı kullanıcıda tam yetkili saldırgan.
- Test: Otomatik elicitation yanıtı ve SDK sahteciliği üst etiketi açamasın.
- Sahip onayı: Tehdit kapsamı ve platform sınırı için gerekli.


### RT-004 — Rational/Decimal alanlarının real’e genişletilmesi

- Önem: BLOCKER.
- Kanıt: VERIFIED.
- Konum: Faz 1 Görev 2, 3 ve 8.
- Karşı örnek: $x\in\mathbb Q,\ x^2=2$.
- Düzeltme: Alanı koruyan motor veya açık ret; Decimal yürütme profili.
- Alternatif: İlk çekirdeği yalnızca desteklenen kesin rasyonel işlemlerle sınırlama.
- Maliyet: Orta; finans için daha yüksek.
- Test: Alan değiştiren derlemeler reddedilsin; Decimal rounding farkları yakalansın.
- Sahip onayı: Kapsam daraltılırsa gerekli.


### RT-005 — Unsat core’un sertifika türü olarak sunulması

- Önem: BLOCKER; bağımsız sertifika etiketi açıyorsa.
- Kanıt: VERIFIED.
- Konum: Faz 1 Görev 10 `Certificate.kind`; yol haritası `certify/`.
- Hata: Açıklayıcı alt küme ile ispat nesnesi karışıyor.[^2_4]
- Düzeltme: `solver_verdict`, `unsat_core`, `checked_proof` ayrımı.
- Alternatif: Solver TCB’sini açıkça kabul eden daha sınırlı yol.
- Maliyet: Şema için düşük; gerçek proof checking için yüksek.
- Test: Sahte veya yalnızca isim listesi içeren core, sertifika kabulü üretemesin.
- Kalan risk: Checker/derleyici ortak hatası.
- Sahip onayı: Güven tanımı için gerekli.


### RT-006 — Onay sonrası iç içe IR mutasyonu

- Önem: BLOCKER riski.
- Kanıt: SUPPORTED.
- Konum: Faz 1 Görev 3, `frozen=True` ve liste alanları.
- Başarısızlık: Onaydan sonra ilişki veya ifade listesi değişir.
- Düzeltme: Derin değişmez snapshot; sınırda yeniden doğrulama; solve öncesi hash eşitliği.
- Alternatif: Kanonik baytlardan her aşamada yeniden yükleme.
- Maliyet: Düşük–orta.
- Kalan risk: Aynı süreçte ayrıcalıklı kod her şeyi değiştirebilir.
- Test: Onay sonrası bütün nested mutation girişimleri.
- Sahip onayı: Genellikle gerekmez; teknik gereklilik.


### RT-007 — Boyut kontrolü ile birim normalizasyonu arasında boşluk

- Önem: BLOCKER riski.
- Kanıt: INFERRED.
- Konum: Faz 1 Görev 5 ve 8.
- Başarısızlık: $x[\mathrm m]=y[\mathrm{cm}], y=100$ boyutsal olarak geçer; değer ölçeği kaybolursa $x=100$ hesaplanabilir.
- Düzeltme: Açık normalize edilmiş quantity temsili; ölçek/ofset dönüşüm sertifikası.
- Alternatif: Solver girişinde tek kanonik birim sistemi.
- Maliyet: Orta.
- Kalan risk: Yanlış tanım tablosu.
- Test: Eşdeğer karışık birim problemleri aynı fiziksel sonucu versin.
- Sahip onayı: Teknik gereklilik.

Bu, gerçekleşmiş ürün hatası değil; görülen sözleşmede kapanmamış bir entegrasyon riskidir.

### RT-008 — MILP optimumu için yetersiz sertifika ölçütü

- Önem: HIGH.
- Kanıt: VERIFIED.
- Konum: Yol haritası F8.
- Hata: LP/MILP’nin aynı “dual sertifikalı” kabul ifadesine bağlanması.
- Düzeltme: Ayrı LP, MILP ve konveks sertifika profilleri.
- Alternatif: v1’de MILP optimumuna formal etiket vermeme.
- Maliyet: Daraltma düşük; genel sertifika yüksek.
- Test: Pozitif integrality-gap örnekleri.
- Sahip onayı: Kapsam daralırsa gerekli.


### RT-009 — Yeterlikten sonuç başına güvene desteklenmeyen geçiş

- Önem: HIGH.
- Kanıt: SUPPORTED.
- Konum: Soru2-1’in görülen kısımları; ekli brief R-2…R-6.
- Hata: Örneklem kabulü ile vaka güveni karışabilir.
- Düzeltme: Yeterlik üyelik önkoşulu; tekil iddiada garanti değil.
- Alternatif: Üst süreç etiketi olmadan ölçüm raporu.
- Maliyet: Orta.
- Test: Profil dışı görev, bayat kayıt, yeni ayar ve adaptif tekrar.
- Sahip onayı: Eşikler için gerekli.[^2_1]


### RT-010 — Sağlayıcı erişiminin genel varsayılması

- Önem: HIGH.
- Kanıt: SUPPORTED.
- Konum: K14–K15, S-13.
- Düzeltme: Sağlayıcı/hesap/kimlik yöntemi bazında allowlist.
- Alternatif: Yerel çekirdek + ajan IR’ı; yetkisiz ağ çağrısı yok.
- Maliyet: Orta ve sürekli bakım.
- Test: Belirsiz kimlik yolu kapalı; API/abonelik sessiz değişmesin.
- Sahip onayı: Gerekli.[^2_9][^2_10][^2_14]


### RT-011 — Yanlış kapsamlı güvenceyi yalnızca `PROVEN` üzerinden ölçmek

- Önem: HIGH.
- Kanıt: VERIFIED.
- Konum: Tasarım A1; yol haritası F1/F9 çıkış ölçütleri.
- Hata: `PROVEN` kapalı olduğunda yanlış `CERTIFIED` veya sahte çapraz kontrol kaçabilir.
- Düzeltme: Yanlış iddia, yanlış kapsam, yanlış kontrol beyanı için ortak yayın güvenliği ölçütü.
- Alternatif: Her etiket için ayrı false-accept paketi.
- Maliyet: Düşük–orta.
- Test: Yapılmamış kontrol raporda görünmesin.
- Sahip onayı: Vaat metni için gerekli.


### RT-012 — Denetim ajanı yapılandırmasının yeniden üretilebilir olmaması

- Önem: MEDIUM.
- Kanıt: VERIFIED.
- Konum: `.claude/settings.json`.
- Hata: Etkin eklentiler görünür; bu dosyada sabit sürüm/commit görünmüyor.
- Düzeltme: Denetim manifest’inde gerçek eklenti sürümleri, istemler, model ve çıktı kimlikleri.
- Alternatif: Yedi ajan sayısını güvence kanıtı olarak kullanmama.
- Maliyet: Düşük.
- Kalan risk: Aynı modellerin ortak varsayımı.
- Test: Aynı denetim girdileri ve araç sürümleri yeniden kurulabilsin.
- Sahip onayı: Gerekmez.

______________________________________________________________________

## XII — Çakışmaların çözümü ve önerilerin adversarial denetimi

| Öneri | Sağladığı | Çözmediği / yeni riski |
| :-- | :-- | :-- |
| Küçük checker | TCB’yi daraltır | Checker hatası, parser hatası, yanlış birim tablosu |
| İmzalı kayıt | İçerik/köken kontrolü | Yanlış ölçüm, seçilmiş sonuç, ele geçirilmiş anahtar |
| OS penceresi | Ajan konuşmasından ayrışma | Aynı kullanıcıda UI otomasyonu ve sahte pencere |
| Nonce | Replay ve yanlış isteğe bağlama riskini azaltır | İnsanın gerçekten gördüğünü kanıtlamaz |
| Üç model | Çeşitlilik ve hata yakalama fırsatı | Ortak yanlış yorum |
| Kaynak alıntısı | Bazı aktarım hatalarını görünür kılar | Doğru alıntı + yanlış semantik |
| “Her sayı kaynakta” | Bazı uydurma girdileri yakalar | Türetilmiş sayıları ve standart sabitleri yanlış reddeder |
| `RIGOR_DEPTH` | Kazara özyinelemeyi azaltır | Silinebilen env değişkeni saldırgan sınırı değildir |
| Ayrı iş süreci | İstemci ömründen ayrışma | Yarış, çift harcama, stale worker |
| `verify-report` | Güvenilir doğrulayıcıyla değişikliği yakalar | Doğrulayıcı da değiştirilebiliyorsa koruma yok |
| `PROVEN` kapalı v1 | Bazı üst etiket risklerini kaldırır | Yanlış `CERTIFIED`, sahte çapraz kontrol |

Sonuç: Bunların çoğu risk azaltımıdır; temel sorunu tamamen ortadan kaldıran kanıt değildir.

Özellikle B-3’teki “yaklaşık bir haftalık checker” önerisini güvence planı olarak kabul etmiyorum. Önce desteklenen iddia dili ve checker sağlamlık argümanı yazılmalı; iş tahmini sonra yapılmalı.

______________________________________________________________________

## XIII — Önceliklendirilmiş düzeltme planı

### P0 — Koddan önce sözleşme kararı

1. İddia kapsamını ve etiket anlamlarını dondur.
2. S-5/S-9 ve S-12 uyuşmazlıklarını açık karara bağla.
3. `USER_DIRECT` güven tanımını düzelt.
4. `Conditions` yerine tipli kontrol olaylarını tanımla.
5. Rational/Decimal ve birim semantiğini dondur.
6. Snapshot–onay–sertifika–rapor bağını tanımla.
7. `UNKNOWN`, `REJECT`, `REFUSED`, `FAILED` ayrımını yap.

Bu maddeler Faz 1 Görev 3, 8, 9, 10 ve oturum/rapor görevlerinin güvenli uygulamasını engelliyor.

### P1 — Dar çekirdeğin güvence paketi

1. Desteklenen kesin iddia alt kümesi.
2. Dar checker.
3. Mutasyona dayanıklı snapshot.
4. Kaynak limitleri.
5. Sahte sertifika ve yanlış alan testleri.
6. Deterministik rapor.
7. Bağımsız yeniden kontrol.

### P2 — Sahip kullanımına teslimat

1. Finansal Decimal mutabakatı.
2. Seçilmiş roket kapalı form hesapları.
3. Veri okuyucular ve kaynak manifest’i.
4. OpenRocket karşılaştırma sözleşmesi.
5. SDK.
6. İnce MCP adaptörü.

Finans ve roket işleri, gerçek teknik bağımlılıkları ölçüsünde paralel ilerleyebilir.

### P3 — Uzak model ve doğal dil

1. Sağlayıcı uygunluk matrisi.
2. İzole adaptörler.
3. Veri izni ve bütçe rezervasyonu.
4. Formülasyon değerlendirme motoru.
5. Değerlendirici kabulü.
6. Model ve heyet ölçümü.

### P4 — Genişleme

Lean, genel belge okuyucular, alan paketi ekosistemi, öğrenen hakem ve geniş optimizasyon.

______________________________________________________________________

## XIV — Sahip onayına sunulacak kararlar

| Karar | Seçenekler | Öneri | Onay yoksa güvenli varsayılan | Engellediği aşama |
| :-- | :-- | :-- | :-- | :-- |
| O-1 — v1’de `PROVEN` | Var / yok | İlk v1’de kapalı | Kapalı | Heyet ve kayıt dağıtımı |
| O-2 — `CERTIFIED` kapsamı | Bütün problem / açık formal iddia | Yalnızca açık iddia | Bağımsız kabul yoksa verilmez | Etiket ve rapor |
| O-3 — “Bilmiyorum” | Ret / koşullu formal hesap | Eksik değer uydurmadan koşullu hesap | Yorum onayı yok diye açık yaz | Session ve onay |
| O-4 — S-5/S-9 | Fiyat kapısı / yeterlik kapısı | Fiyatı doğruluk ölçütü yapma | Çatışan üst etiket kapalı | `PROVEN` politikası |
| O-5 — CLI erişimi | Otomatik / sağlayıcı bazlı / API-only | Sağlayıcı bazlı, varsayılan kapalı | Ağ çağrısı yok | F3 adaptörleri |
| O-6 — Yerel saldırgan | Aynı kullanıcı shell kapsam içi / sınırlı | Güvence düzeylerini açık ayır | Tam shell’e karşı onay garantisi yok | Güvenlik vaadi |
| O-7 — Lean v1 | Korunur / ertelenir | Sahip-öncelikli v1 için ertele | K26 değiştirilmeden ertelenmiş sayılmaz | Kapsam |
| O-8 — PDF/DOCX | v1 / sonra | Sonra | Ajanın aktardığı işlemlerle sınırlı rapor | Belge yolu |
| O-9 — Toplayıcı üst katkısı | A/B/C | Ölçüm ve politika onayına kadar sayma | Üst etikete katkı yok | Heyet |
| O-10 — Platformlar | macOS/Linux/Windows | Gerçek onay adaptörüyle sınanmış platformlar | Desteklenmeyende ayrıcalıklı işlem yok | Dağıtım |
| O-11 — Yeterlik eşikleri | 300+100 / başka tasarım | Pilot sonrası dondur | Hiçbiri bilimsel garanti sayılmaz | Ölçüm |
| O-12 — v1 önceliği | Sahip / genel kullanıcı | S-18 gereği sahip | Sahip önce; hedef mimari korunur | Faz sırası |

Harness için ek karar: Opsiyonel istemci olarak değerlendirilsin; çekirdek bağımlılığı yapılmasın. Resmî ürün tanımı bu rolü destekliyor, matematiksel güvence rolünü değil.[^2_15]

______________________________________________________________________

## XV — Nihai Red Team kararı

Tam depo ve bütün geçmiş kararlar için karar: **INSUFFICIENT_EVIDENCE**.

Nedenleri:

- Beş uzun dosyanın içeriği kesildi.
- Tasarımın ve Faz 1 planının bütün kritik bölümleri kesintisiz okunamadı.
- Kesin satır aralığı şartı tamamlanamadı.
- Önceki bütün dış kaynaklar yeniden doğrulanmadı.
- CSV hesapları yeniden çalıştırılmadı.
- Planlanan testler ve solver deneyleri çalıştırılmadı.
- Bütün-dosya `main...development` diff denetimi tamamlanmadı.

Buna rağmen doğrudan görülen sözleşmeler şu kararı destekliyor:

> Mevcut Faz 1 planı, güven etiketleri üreten uygulamanın bağlayıcı geliştirme sözleşmesi olarak değişikliksiz kullanılmamalıdır.

Önce etiket semantiği, insan onayı iddiası, sayı alanları, sertifika türleri ve snapshot bağlama düzeltilmelidir. Özellikle resmî MCP SDK’nın otomatik elicitation yanıtına izin veren davranışı, “form geldi, öyleyse kullanıcı onayladı” savunmasının yeterli olmadığını doğrudan gösteriyor.[^2_3]

Rigor’un en güçlü ilerleme yolu daha fazla ajan veya daha fazla model eklemek değil; küçük bir iddia dilinde, hangi önermenin hangi denetleyici tarafından hangi varsayımlarla kabul edildiğini açık ve test edilebilir hale getirmektir. Çoklu model, insan incelemesi ve alan paketleri bu çekirdeğe ek savunmalar olabilir; onun yerine geçemez.

Bu çalışma sırasında GitHub dosyaları değiştirilmedi; commit, issue veya PR oluşturulmadı. Model sağlayıcılarına proje verisi gönderilmedi. Yerel doğrulama ortamında yalnızca ekli Markdown dosyasının metin ve karar kayıtları okundu; ürün testi, matematiksel deney veya bağımsız istatistik yeniden hesabı yapılmış gibi sunulmadı.

<span style="display:none">[^2_17][^2_18][^2_19][^2_20][^2_21][^2_22][^2_23][^2_24][^2_25][^2_26][^2_27][^2_28][^2_29][^2_30][^2_31][^2_32][^2_33][^2_34][^2_35][^2_36][^2_37][^2_38][^2_39][^2_40][^2_41][^2_42][^2_43][^2_44][^2_45][^2_46][^2_47][^2_48][^2_49][^2_50][^2_51][^2_52][^2_53][^2_54][^2_55][^2_56][^2_57][^2_58][^2_59][^2_60][^2_61][^2_62][^2_63][^2_64][^2_65][^2_66][^2_67][^2_68][^2_69][^2_70][^2_71][^2_72][^2_73][^2_74][^2_75][^2_76][^2_77][^2_78][^2_79][^2_80][^2_81][^2_82][^2_83][^2_84][^2_85][^2_86][^2_87][^2_88][^2_89][^2_90][^2_91][^2_92][^2_93]</span>

<div align="center">⁂</div>

[^2_1]: concepts_brief.md

[^2_2]: https://lean-lang.org/doc/reference/latest/ValidatingProofs/

[^2_3]: https://py.sdk.modelcontextprotocol.io/api/mcp/server/elicitation/

[^2_4]: https://microsoft.github.io/z3guide/docs/logic/propositional-logic/

[^2_5]: https://microsoft.github.io/z3guide/docs/strategies/summary/

[^2_6]: https://flintlib.org/doc/using.html

[^2_7]: https://flintlib.org/doc/algorithms/exact/zero-testing.html

[^2_8]: https://code.claude.com/docs/en/agent-sdk/hooks

[^2_9]: https://code.claude.com/docs/en/legal-and-compliance

[^2_10]: https://developers.openai.com/codex/noninteractive

[^2_11]: https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server

[^2_12]: https://geminicli.com/docs/resources/faq/

[^2_13]: https://geminicli.com/docs/get-started/authentication/

[^2_14]: https://geminicli.com/docs/resources/tos-privacy/

[^2_15]: https://www.deepseek.com/en/harness/

[^2_16]: https://github.com/deepseek-ai/deepseek-harness/

[^2_17]: concepts_brief.md

[^2_18]: https://code.claude.com/docs/en/settings-reference

[^2_19]: https://code.claude.com/docs/en/whats-new/rss.xml

[^2_20]: https://code.claude.com/docs/en/llm-gateway

[^2_21]: https://code.claude.com/docs/en/claude_code_docs_map

[^2_22]: https://code.claude.com/docs/ru/overview

[^2_23]: https://code.claude.com/docs/en/third-party-integrations

[^2_24]: https://code.claude.com/docs/en/claude-code-on-the-web

[^2_25]: https://code.claude.com/docs/en/agent-sdk/typescript

[^2_26]: https://code.claude.com/docs/en/data-usage

[^2_27]: https://code.claude.com/docs/en/zero-data-retention

[^2_28]: https://code.claude.com/docs/en/admin-setup

[^2_29]: https://code.claude.com/docs/en/best-practices

[^2_30]: https://code.claude.com/docs/en/auto-mode-config

[^2_31]: https://blog.modelcontextprotocol.io/posts/2025-11-21-mcp-apps/

[^2_32]: https://modelcontextprotocol.io/specification/draft/client/elicitation

[^2_33]: https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation

[^2_34]: https://ts.sdk.modelcontextprotocol.io/v2/servers/elicitation.html

[^2_35]: https://blog.modelcontextprotocol.io/posts/2026-07-28/

[^2_36]: https://csharp.sdk.modelcontextprotocol.io/v1/concepts/elicitation/elicitation.html

[^2_37]: https://ts.sdk.modelcontextprotocol.io/capabilities.html

[^2_38]: https://csharp.sdk.modelcontextprotocol.io/v1/api/ModelContextProtocol.Protocol.ClientCapabilities.html

[^2_39]: https://modelcontextprotocol.io/examples

[^2_40]: https://modelcontextprotocol.io/extensions/apps/overview

[^2_41]: https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector

[^2_42]: https://registry.modelcontextprotocol.io/v0/servers?search=perrylink

[^2_43]: https://registry.modelcontextprotocol.io/v0.1/servers?search=io.github.DMontgomery40/deepseek

[^2_44]: https://registry.modelcontextprotocol.io/

[^2_45]: https://www.deepseek.com/harness/en/

[^2_46]: https://github.com/deepseek-ai/deepseek-harness/tree/master

[^2_47]: https://github.com/deepseek-ai

[^2_48]: https://github.com/deepseek-harness

[^2_49]: https://github.com/deepseek-ai/deepseek-harness/blob/477b4f420553e8a52c2fbccc464d7561b239c443/README.md

[^2_50]: https://github.com/MHMITHUN/Deepseek-Harness

[^2_51]: https://github.com/panhouhui/DeepSeek_Harness

[^2_52]: https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md

[^2_53]: https://developers.openai.com/community/codex-for-oss

[^2_54]: https://developers.openai.com/training/codex-lab

[^2_55]: https://developers.openai.com/blog/codex-as-a-platform

[^2_56]: https://developers.openai.com/blog/skills-agents-sdk

[^2_57]: https://developers.openai.com/cookbook/examples/codex/secure_quality_gitlab

[^2_58]: https://developers.openai.com/cookbook/examples/codex/code_modernization

[^2_59]: https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.3-codex

[^2_60]: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide

[^2_61]: https://developers.openai.com/?site_locale=en

[^2_62]: https://geminicli.com/docs/

[^2_63]: https://geminicli.com/docs/cli/headless/

[^2_64]: https://geminicli.com/docs/reference/configuration/

[^2_65]: https://geminicli.com/terms/

[^2_66]: https://geminicli.com/plans/

[^2_67]: https://geminicli.com/docs/resources/faq.md

[^2_68]: https://geminicli.com/docs/changelogs/

[^2_69]: https://geminicli.com/docs/cli/enterprise/

[^2_70]: https://geminicli.com/

[^2_71]: https://geminicli.com/docs/cli/tutorials/automation/

[^2_72]: https://geminicli.com/docs/core/

[^2_73]: https://geminicli.com/docs/reference/tools/

[^2_74]: https://flintlib.org/doc/guide/correctness/guarantees.html

[^2_75]: https://flintlib.org/doc/guide/types/ball-arithmetic.html

[^2_76]: https://flintlib.org/doc/algorithms/ball-arithmetic/overview.html

[^2_77]: https://flintlib.org/doc/decimal/index.html

[^2_78]: https://flintlib.org/doc/tutorials/numerics/index.html

[^2_79]: https://flintlib.org/doc/decimal/decball_struct.html

[^2_80]: https://flintlib.org/doc/arb/index.html

[^2_81]: https://flintlib.org/doc/overview.html

[^2_82]: https://microsoft.github.io/z3guide/programming/Example Programs/Cores and Satisfying Subsets/

[^2_83]: https://microsoft.github.io/z3guide/programming/Parameters/

[^2_84]: https://microsoft.github.io/z3guide/programming/Z3 Python - Readonly/advanced/

[^2_85]: https://microsoft.github.io/z3guide/docs/theories/Datatypes/

[^2_86]: https://microsoft.github.io/z3guide/docs/logic/basiccommands

[^2_87]: https://microsoft.github.io/z3guide/programming/Example Programs/Formula Simplification/

[^2_88]: https://microsoft.github.io/z3guide/programming/Example Programs/MBQI/

[^2_89]: https://microsoft.github.io/z3guide/programming/Z3 Python/advanced/

[^2_90]: projects.thesis_and_grant_platform

[^2_91]: https://www.perplexity.ai/search/f9abba16-262b-4972-8aba-c45ed083b6ca

[^2_92]: https://www.perplexity.ai/search/92a841ea-82ef-484b-9028-4afc42918c0d

[^2_93]: https://www.perplexity.ai/search/0d9223ee-f0d0-4790-9b44-6a2bca04e00d


---

# Rigor — Deep Research Phase II

## Bağımsız yeniden inceleme ve mimari karar raporu

## I. Yönetici özeti

İncelenen tasarım ve Faz 1 uygulama sözleşmeleri için kararım: **ARCHITECTURE_CHANGES_REQUIRED**.

Önceki rapordan farklı olarak bu karar artık yalnızca kısmi belge okumalarına dayanmıyor. Bu turda Faz 1 planının tamamına commit patch’i üzerinden ulaştım; ana tasarımın daha önce kesilen bölümlerini ilk sürüm ve sonraki değişiklikler üzerinden inceledim. Ayrıca istatistik ekini yeniden hesapladım ve bazı matematiksel/yazılımsal karşı örnekleri izole ortamda çalıştırdım.

Bu ilerleme, bütün depo araştırmasının eksiksiz kapandığı anlamına gelmiyor: üç uzun Deep Research raporunun önceki turda kesilen bütün bölümleri bu turda tamamlanmadı; gerçek Rigor uygulaması, sağlayıcı adaptörleri ve MCP entegrasyonu çalıştırılmadı.

### Önceki değerlendirmede değişen başlıca sonuçlar

| Konu | Phase II sonucu |
| :-- | :-- |
| Birim normalizasyonu | Önceki RT-007 daraltıldı. Faz 1 Görev 11, verilenleri SI temel birimlerine dönüştürmeyi ve sonucu geri çevirmeyi açıkça tanımlıyor. “Normalizasyon tanımlanmamış” sonucu korunamaz. |
| Aralık sıfırı içeriyorsa eşitlik | Plan bunu zaten doğru ele alıyor: `undetermined`, `all_satisfied=False`. Önceki açık soru bu kapsamda kapandı. |
| Yerel kök araması | Yeni doğrudan risk: farklı başlangıçların aynı köke yakınsaması, teklik veya çözüm kümesi tamlığı kanıtı değildir. Planın fallback’i bunu ayıracak kadar açık değil. |
| Kullanıcı onayı | Önceki kanal güveni eleştirisi güçlendi. Ek olarak, formun gönderilmesi anlamındaki `accept` ile formdaki `onay=True` ayrılmalı. Resmî SDK örnekleri bu ayrımı açıkça yapıyor. [^3_1] |
| MCP sözleşmesi | Yeni protokol uyumsuzluğu bulundu: `ctx.elicit()` legacy back-channel yoludur; 2026-07-28 akışında resolver/MRTR kullanılmalıdır. [^3_1][^3_2] |
| İstatistik CSV’si | 34 veri satırının tamamı yeniden hesaplandı; sayısal hata bulunmadı. Bu, model yeterliğinin doğrulandığı anlamına gelmez. |
| İki aşamalı kabul | Önceden belirlenmiş olması yeterli değil. Önerilen 300+300 planı, %1 gerçek hata oranında kabul olasılığını %4,904’ten %5,633’e çıkarıyor. |
| Çoklu testler | “Bütün koşullar geçmeli” kabul kararı ile “bütün güven aralıkları eşzamanlı %95 kapsıyor” iddiası ayrılmalı. İlkinde uygun intersection–union test için otomatik Bonferroni zorunluluğu yok. [^3_3] |
| Yerel saldırgan | Önceki rapordaki “tehdit modeli yok” ifadesi fazla genişti. Tasarım, sınırsız shell/masaüstü erişimli ajanın yerel kanalları taklit edebileceğini zaten kabul ediyor. Eksik olan, bu sınırın uygulanabilir güvence seviyelerine bağlanması. |
| Sağlayıcı koşulları | Genel yasak sonucu verilemez. Özellikle Anthropic metnindeki değiştirilmemiş CLI istisnası ve OpenAI’nin yerel otomasyon desteği korunmalı; Rigor’un özel kullanım modeli ayrıca değerlendirilmeli. [^3_4][^3_5] |

### En önemli mimari sonuç

Rigor’un güvenli ilerlemesi için önce şu üç sorunun sözleşmesi kesinleşmeli:

1. Hangi matematiksel önerme doğrulandı?
2. Bu önerme hakkında hangi özellik doğrulandı: aday geçerliliği, tamlık, teklik, hata sınırı veya optimalite?
3. Bu matematiksel doğrulamanın kullanıcının amaçladığı problemle ilişkisi ne kadar incelendi?

Bu ayrım yapılmadan daha fazla model, daha fazla test veya daha küçük bir checker eklemek yanlış güven üretimini engellemez.

______________________________________________________________________

## II. Eksiklik denetimi

### 1. Sürüm ve kapsam kontrolü

| Alan | Phase II durumu |
| :-- | :-- |
| `development` HEAD | `f7f86d3bf1726f65577cb0764d45d740588f9aac` — değişmedi |
| `main` HEAD | `7e03b24d62597f8886f257e090ad6ba5fe3f78d5` — değişmedi |
| Issue kayıtları | Yeniden sorgulandı; 0 |
| Pull request kayıtları | Bütün durumlar yeniden sorgulandı; boş |
| Önceki dosya envanteri | Aynı commit nedeniyle 15 dosyalık envanter geçerli; bu tur yeni bir recursive-tree tamlık denetimi yapılmadı |
| Ekli brief | Depodaki eski brief’ten ayrı kaynak olarak korundu |
| Depo değişikliği | Yapılmadı |

### 2. Önceki erişim sorununun aşılması

Normal `get_file_contents` yanıtı Faz 1 planını yine Görev 10’da kesti. Ancak dosyanın eklendiği `ca689154…` commit’inin dosya bazında sayfalanmış tam patch’i, 779 satırlık planın tamamını döndürdü.

Ana tasarım için:

- İlk 810 satırlık sürüm;
- `52816e6…` alan bağımsızlığı değişiklikleri;
- `fea88dd…` alan uyarlaması ve Lean değişiklikleri;
- `c6bea6f…` MCP, comparator ve ortam düzeltmeleri;
- `ca68915…` son sıra düzeltmesi

doğrudan incelendi.

Bu, metinsel kapsam boşluğunu önemli ölçüde kapatır. Bununla birlikte tasarım dosyasını yerelde bütün patch’leri uygulayarak yeniden oluşturup Git blob hash’ini karşılaştırmadım. Dolayısıyla “bayt düzeyinde bağımsız yeniden kurulum” yapılmış değildir.

### 3. Zorunlu eksiklik matrisi

Önceki 12 önemli RT kaydının bütün alanlarını içeren eksiklik matrisi CSV olarak da sunuluyor. Aşağıdaki tablo, karar vermeyi etkileyen özettir.


| Önceki bulgu | İlk iddia ve kanıt | Tespit edilen eksiklik / risk | Yeni doğrulama | Yeni sonuç | Mimari etki ve kalan belirsizlik |
| :-- | :-- | :-- | :-- | :-- | :-- |
| RT-001 | HEAD brief’inde onaysız öneri geçerli sayılıyor | Kabul kanıtları bütün kararlar için çıkarılmamıştı | Değişmeyen HEAD ile ekli kayıt ayrımı korundu | CONFIRMED | Karar otoritesi sorunu sürüyor; yeni sahip onayı yok |
| RT-002 | Üç etiketli Faz 1 şeması yeni modeli taşımıyor | Session ve MCP sonu okunmamıştı | Planın tamamı okundu | STRENGTHENED | Sorun yalnız enum değil; onay, replay ve yayın sözleşmesini etkiliyor |
| RT-003 | Kanal insan kimliğini kanıtlamaz | Form eylemi ile boolean onay ayrılmamıştı | Görev 18 ve güncel SDK örnekleri karşılaştırıldı | STRENGTHENED | Güvenilir onay adaptörü gerekli; gerçek istemci testi yok |
| RT-004 | Rational/Decimal real’e genişletiliyor | İşlem bazlı semantik farklılıkları incelenmemişti | Decimal ve modulo karşı örnekleri çalıştırıldı | STRENGTHENED | Alan etiketi yanında operatör semantiği de sürümlenmeli |
| RT-005 | Unsat core bağımsız ispat değil | Proof object içindeki boş/trusted adımlar ele alınmamıştı | Alethe/cvc5 birincil belgeleri incelendi | STRENGTHENED | “Proof üretildi” yerine bütün adımların kabul kaydı gerekli |
| RT-006 | Frozen modelde nested mutation riski | Çalıştırılmış deney yoktu | Pydantic v2 izole mutasyon deneyi | STRENGTHENED | Risk doğrulandı; Rigor Session’ının gerçekten istismar edildiği gösterilmedi |
| RT-007 | Normalizasyon sözleşmesi görünmüyor | Görev 11 görülmemişti | Tam planda SI dönüşümü bulundu | CORRECTED | Eksiklik iddiası geri çekildi; motorlar arası uygulama tutarlılığı açık |
| RT-008 | MILP için dual sertifika ölçütü fazla geniş | Bütün dual tabanlı MILP sertifikaları yetersizmiş gibi okunabilirdi | Bound closure ayrımı yapıldı | CORRECTED | LP dual bound + uygun tamsayılı çözüm eşit hedefte buluşursa yeterli olabilir; genel MILP için aynı şey varsayılamaz |
| RT-009 | Yeterlik tekil sonuç garantisi değil | CSV yeniden hesaplanmamış; IUT ayrımı eksikti | 34 satır, iki aşamalı plan ve IUT yeniden incelendi | STRENGTHENED | Sayılar doğru; kabul politikasının anlamı düzeltilmeli |
| RT-010 | Sağlayıcı erişimi genel varsayılamaz | Tam metindeki izin istisnaları eksik ağırlıklandırılmıştı | Üç sağlayıcının ilgili sayfaları yeniden okundu | CORRECTED | Sağlayıcı bazlı uygunluk; genel otomasyon yasağı yok |
| RT-011 | Yalnız yanlış `PROVEN` ölçmek yetersiz | Tam altın test sonu görülmemişti | Görev 19 yeniden okundu | CONFIRMED | `PROVEN` yokluğu, diğer etiketlerin doğru olduğunu göstermiyor |
| RT-012 | Ajan eklenti sürümleri görünmüyor | Makinenin tamamında sabitleme olmadığı kanıtlanmamıştı | İddia proje dosyasıyla sınırlandı | CORRECTED | Yerel/global kurulum incelenmedi; bulgu MEDIUM’u aşmamalı |

### 4. Önceki raporun yöntemsel düzeltmeleri

Önceki raporda üç farklı durum bazı yerlerde yeterince ayrılmıyordu:

- Belgede koruma yok.
- Koruma var, yeterliliği gösterilmedi.
- Korumanın uygulaması başarısız.

Bu turda Rigor henüz uygulanmış olmadığı için üçüncü tür sonuç vermiyorum. Bulguların çoğu tasarım sözleşmesi kusuru veya uygulanırsa oluşabilecek başarısızlık yoludur.

______________________________________________________________________

## III. Yeni bilimsel ve teknik bulgular

### 1. İzole doğrulama deneyleri

Çalışma ortamı:


| Bileşen | Kullanılan sürüm |
| :-- | :-- |
| Python | 3.12.8 |
| SymPy | 1.14.0 |
| SciPy | 1.13.1 |
| Pydantic | 2.11.4 |
| mpmath | 1.3.0 |

SymPy sürümü plandaki 1.14 ile örtüşüyor. Pydantic ve mpmath sürümleri plandaki hedeflerden farklıdır. Sonuçlar Rigor entegrasyon testi değil, ilgili mekanizmaların izole karşı örnekleridir.


| Deney | Gözlem | Kanıtladığı sınır |
| :-- | :-- | :-- |
| `solve(sin(x), x, dict=True)` | Yalnız `0` ve `π` döndü | Dönen aday listesi bütün kökler değildir |
| `solveset(sin(x), x, Reals)` | Sonsuz aileleri taşıyan küme döndü | Sonuç temsili tamlık bilgisini korumalı |
| `sin(2π)` | Sembolik olarak 0 | `solve` listesinin dışında geçerli kök var |
| Üç yerel başlangıçtan `findroot(sin, …)` | Üçü de 0’a yakınsadı | Çoklu başlangıç uyuşması teklik kanıtı değil |
| Decimal, hassasiyet 2: `(1/3)*3` | `0.99` | İşlem sırasındaki rounding, final rounding ile aynı değil |
| Kesin rasyonel sadeleştirme sonrası dönüşüm | `1` | Aynı cebirsel ifade farklı yürütme semantiği taşıyabilir |
| `7 mod -3` | Python/SymPy: `-2`; Decimal: `1` | Tek `mod` adı farklı matematiksel işlemleri gizleyebilir |
| Frozen modelde listeye ekleme | Başarılı; serileştirilmiş içerik değişti | `frozen=True` derin değişmezlik sağlamaz |
| `solve(Eq(x,x), x, dict=True)` | `[]` | Sıfır aday, her zaman “çözüm yok” değildir |
| `solveset(0, x, Reals)` | `Reals` | Aynı durumda doğru çözüm kümesi bütün reellerdir |

SymPy’nin kendi belgesi de `solve` çıktısının bulabildiği çözümleri verdiğini, eksik çözümler konusunda her zaman işaret taşımadığını açıkça belirtiyor. `solveset` bu ayrımı `ConditionSet` gibi temsillerle korumayı amaçlıyor.[^3_6]

Deney sonuçları, istatistik yeniden denetimi ve ortam sürümleri ayrı CSV/JSON dosyalarında sunuluyor.

### 2. İstatistik ekinin yeniden hesabı

`rigor_yeterlik_istatistik_hesaplari.csv` içindeki:

- Sıfır hatalı üst sınırlar;
- Sıfırdan fazla hatalı Clopper–Pearson üst sınırlar;
- Gerekli örneklem sayıları;
- Sıfır hatayla geçme olasılıkları;
- Bonferroni hesapları;
- Başarı oranı alt sınırları

yeniden hesaplandı.

Sonuç:

- 34/34 veri satırı tolerans içinde uyuştu.
- Ana değerlerde en büyük mutlak fark: yaklaşık $2{,}22\times10^{-16}$.
- Ek alt sınır değerlerinde en büyük fark: yaklaşık $1{,}11\times10^{-16}$.

Sınırlama: Araçtan dönen CSV değerlerini yerel hesap girdisine aktardım; özgün CSV blob’unu bayt düzeyinde indirip hash doğrulamadım. Bu, sayısal içeriğin yeniden hesabıdır; dosya kökeni deneyi değildir.

### 3. Yeni birincil kanıtlar

| Kaynak | İncelenen sürüm/tarih | Gerçekten desteklediği sonuç | Desteklemediği çıkarım |
| :-- | :-- | :-- | :-- |
| MCP MRTR belirtimi | 2026-07-28 | `requestState` saldırgan kontrollü; yetkiyi etkiliyorsa bütünlük koruması zorunlu; tek kullanımlılık ayrıca sunucuda sağlanmalı | İmzalı token’ın replay’i tamamen önlediği [^3_2] |
| MCP Python SDK | 11 Kasım’da okunan canlı belge | `ctx.elicit` legacy; resolver/MRTR yeni akış; `accept` ile boolean karar ayrı | Her SDK sürümünün aynı API’yi sunduğu [^3_1][^3_7] |
| SMT-LIB Ints | 2.7; sayfada son içerik güncellemesi 16 Ocak 2026 | Euclidean `div/mod` semantiği | Python veya Decimal `%` ile genel eşdeğerlik [^3_8] |
| SMT-LIB Reals | 2.7; 21 Temmuz 2024 | Sıfıra bölme total fakat değeri kısıtlanmamış | Solver’ın sıradan matematikteki tanımsızlığı kendiliğinden reddettiği [^3_9] |
| Python Decimal | Canlı resmî belge | Remainder ve integer division semantiği integer/float’tan farklı | Decimal’i yalnız “kesin ondalık sayı” saymanın yeterli olduğu [^3_10] |
| cvc5 Alethe | Canlı ve 1.4.2 belgeleri | Proof formatı ve teori kapsamı sınırlı; örnekte `hole` adımları mevcut | Her proof object’in eksiksiz denetlendiği [^3_11][^3_12] |
| Berger–Hsu | 1996, Teorem 1 | Uygun all-required IUT’de ek multiplicity düzeltmesi gerekmeyebilir | Bütün bireysel aralıkların otomatik eşzamanlı %95 kapsadığı [^3_3] |


______________________________________________________________________

## IV. Karar ve belge çelişkilerinin yeniden değerlendirilmesi

### 1. Gerçekten kapanan veya daralan konular

#### Birim normalizasyonu

Görev 11 açıkça:

> Verilenler SI temel birimlerine dönüştürülür; çözüm bilinmeyenin birimine geri çevrilir.

diyor. Önceki RT-007’nin “böyle bir sözleşme görünmüyor” kısmını geri çekiyorum.

Açık kalan soru daha dardır:

- Z3 teklik kontrolü aynı normalize edilmiş problemi mi görüyor?
- Sertifika orijinal birim bağlamına doğru bağlanıyor mu?
- Affine birimlerde mutlak sıcaklık ile sıcaklık farkı ayrılıyor mu?

Bunlar uygulama kabul testleridir; artık “normalizasyon hiç tasarlanmamış” bulgusu değildir.

#### Aralıkta sıfır bulunması

Görev 10:

- Sembolik sıfır kanıtlanamıyorsa;
- Arb residual topu sıfırı içeriyorsa;

`undetermined` ve `all_satisfied=False` istiyor.

Bu koruma belge düzeyinde doğru. Uygulandığı test edilmedi, fakat eksikmiş gibi raporlanmamalı.

#### Yerel tam yetkili ajan

Tasarım §7.2’nin güncellenmiş metni, sınırsız shell ve masaüstü erişimi olan ajanın yerel onay kanallarını taklit edebileceğini zaten söylüyor.

Bu nedenle önceki “tehdit modeli yok” ifadesi şu hale düzeltilmeli:

> Tehdit sınırının bir bölümü belgelenmiş; fakat hangi etiketin hangi saldırgan altında korunabildiği ve hangi kontrolün bunu uyguladığı tanımlanmamış.

### 2. Kapanmayan çelişkiler

| Konu | Durum |
| :-- | :-- |
| `CERTIFIED` ile üç etiketli Faz 1 şeması | Açık |
| S-5 ücretsiz heyet yasağı ile S-9 eşit katkı | Açık sahip kararı |
| S-12 “bilmiyorum” ile zorunlu yorum onayı | Açık yayın politikası |
| Rapor önerilerinin sahip onayı sayılması | HEAD’de yönetişim problemi sürüyor |
| Onay sonrası kök kısıtı eklenmesi | Görev 14’te doğrudan doğrulandı |
| Şablonda “etiket korunur” ile güncel yeterlik | Entegrasyon kuralı eksik |
| K26 Lean v1 ile erteleme önerisi | Sahip onayı olmadan değiştirilemez |
| Tek `mod` operatörüyle farklı backend semantiği | Yeni sözleşme engelleyicisi |

S-5/S-9, S-12 ve erteleme önerilerinin onay durumları ekli brief’te de açıkça ayrılıyor. Araştırma önerilerini bağlayıcı karar yapmıyorum.[^3_13]

### 3. Yeni bulunan sıra uyuşmazlığı

Ana tasarım §10:

```text
4c alan uyarlama
4d optimizasyon
5 finans
```

sırasını veriyor.

Yol haritası ise:

```text
F6 alan uyarlama
F7 finans
F8 optimizasyon
```

diyor ve bunun tasarımla aynı sıra olduğunu belirtiyor.

Bu, gerçek fakat MEDIUM düzeyinde bir belge çelişkisidir. Finansın optimizasyondan önce yapılması kendi başına yanlış değildir. Sorun, iki farklı sıranın aynı bağlayıcı sıra gibi sunulmasıdır.

______________________________________________________________________

## V. Matematiksel doğruluk ve sertifika güvencesi

### 1. Aday, tek çözüm ve tam çözüm kümesi ayrılmalı

Faz 1 Görev 11 üç mekanizma içeriyor:

1. SymPy `solve`.
2. Z3 ile başka çözüm olmadığını sorgulama.
3. Z3 desteklemezse farklı başlangıçlardan mpmath `findroot`.

Üçüncü mekanizma, ikinciyle aynı iddiayı doğrulamaz.

$$
\sin x=0
$$

için birden çok başlangıçtan $x=0$ bulunabilir. Bu:

- 0’ın aday olduğunu destekler;
- $π,2π,\ldots$ köklerini dışlamaz;
- tekliği kanıtlamaz;
- tam çözüm kümesini vermez.

Üstelik SymPy 1.14.0 ile çalıştırılan deneyde `solve` yalnız 0 ve $π$ döndürürken `solveset` sonsuz kök ailelerini temsil etti. Bu davranış resmî belgelerde açıklanan sınırla uyumludur.[^3_6]

Gerekli sonuç kapsamları:


| Kapsam | Gerekli kanıt |
| :-- | :-- |
| `CANDIDATE_VALID` | Aday orijinal koşulları sağlıyor |
| `UNIQUE_IN_DOMAIN` | Belirtilen alanda başka çözüm yok |
| `COMPLETE_SET` | Dönen küme bütün çözümleri içeriyor |
| `LOCAL_NUMERICAL_MATCH` | Seçilmiş yerel aramalar uyuştu |
| `UNKNOWN_COMPLETENESS` | Adaylar var; tamlık belirlenmedi |

`LOCAL_NUMERICAL_MATCH`, `UNIQUE_IN_DOMAIN` yerine geçirilemez.

### 2. Boş aday listesi “çözüm yok” değildir

Görev 11’in “0 aday → `none`” kuralı genel uygulanırsa:

$$
x=x
$$

gibi bütün değerlerin çözüm olduğu durumda yanlış sınıflandırma yapılabilir. İzole SymPy deneyinde `solve(Eq(x,x),x,dict=True)` boş liste döndürdü; `solveset(0,x,Reals)` ise bütün reelleri verdi.

Bu örnek tam Session’da çalıştırılmadı. Başka bir kapı bunu durdurabilir. Ancak motor adaptörünün sözleşmesi yine de yanlış: “aday bulamadım” ile “çözüm olmadığını gösterdim” ayrı sonuçlardır.

### 3. Operatör semantiği backend seçimine bırakılamaz

Plan `mod` düğümünü SymPy ve Z3’e eşliyor; fakat tek bir matematiksel semantik tanımlamıyor.

Örnek:

$$
7\ \mathrm{mod}\ (-3).
$$

- Python/SymPy floor-mod sonucu: $-2$.
- SMT-LIB Euclidean mod sonucu: $1$.
- Decimal remainder sonucu: $1$.

İkinci örnek:

$$
(-7)\ \%\ 4.
$$

Python integer sonucu 1 iken Decimal sonucu $-3$’tür. Resmî Decimal belgesi bu farkı açıkça belgeliyor.[^3_10]

SMT-LIB ise sıfır olmayan bölen için:

$$
0\le r<|n|
$$

koşulunu kullanıyor.[^3_8]

Düzeltme seçenekleri:

- İlk sürümde yalnız pozitif tamsayı böleni desteklemek.
- `euclidean_mod`, `floor_mod`, `remainder` işlemlerini ayrı yapmak.
- IR’da sürümlü bir operasyon semantiği tanımlayıp bütün derleyicileri ona uydurmak.

İlk seçenek en basit güvenli daraltmadır. Genel `mod` desteği varmış gibi davranmamalıdır.

### 4. Tanımlılık, sadeleştirmeden önce çıkarılmalı

$$
\frac{x}{x}=1
$$

ifadesini sadeleştirmek, $x\ne0$ koşulunu ortadan kaldırmaz.

Görev 7 ilişki kaynaklı domain yükümlülüklerini tanımlıyor. Görev 12’de ise özdeşlik ifadeleri `goal.lhs` ve `goal.rhs` içinde bulunuyor. Bütün hedef ifadelerinin domain taramasına dahil olduğu açıkça söylenmiyor.

Gerekli yükümlülükler yalnız `relations` üzerinden değil bütün AST köklerinden çıkarılmalı:

- Hedef ifadeleri.
- Amaç fonksiyonu.
- Koşullar.
- Tabloların geçerlilik alanı.
- ODE/PDE başlangıç ve sınır koşulları.
- Negatif üslerin tabanı.
- Fonksiyonların tanım alanı.

SMT-LIB’de sıfıra bölmenin total fakat değeri kısıtlanmamış olması bu sınırı özellikle önemli yapar. Solver’dan exception beklemek güvenli değildir.[^3_9]

Bu, doğrulanmış bir Rigor exploit’i değil; HIGH/BLOCKER etkili bir sözleşme boşluğudur.

### 5. ODE/PDE geri koyması teklik kanıtlamaz

Tasarım §6.6, kapalı form çözümün denkleme ve başlangıç/sınır koşullarına geri konmasını `PROVEN` yolu olarak sunuyor.

Bu, şu iddiayı kanıtlayabilir:

> Sunulan fonksiyon denklemi ve koşulları sağlar.

Şunu kendiliğinden kanıtlamaz:

> Bu problemde mümkün olan tek hareket budur.

Karşı örnek:

$$
y'(t)=\sqrt{y(t)},\qquad y(0)=0,\qquad t\ge0.
$$

Hem $y(t)=0$, hem de uygun $c\ge0$ için:

$$
y_c(t)=
\begin{cases}
0,&t\le c,\\
(t-c)^2/4,&t>c
\end{cases}
$$

başlangıç koşulunu ve denklemi sağlar.

Dolayısıyla kapalı form sertifikası “geçerli bir çözüm” olarak etiketlenebilir; tek yörünge veya belirli sonraki değer iddiası için ek teklik koşulu gerekir. Bu analitik karşı örnektir; sayısal ODE deneyi yapılmadı.

### 6. Proof-producing solver da eksik proof üretebilir

cvc5 Alethe belgesi:

- Desteklenen teorileri sınırlı olarak listeliyor.
- Örnek proof içinde `:rule hole` ve `"untranslated rewrite"` adımları gösteriyor.[^3_11]

Bu, cvc5’in yanlış sonucu kabul ettiği anlamına gelmez. Çıkan proof’un bütün adımlarının seçilen checker tarafından denetlenmiş olduğunun ayrıca doğrulanması gerektiğini gösterir.

Asgari kabul sözleşmesi:

- Desteklenmeyen kural → ret.
- `hole`, atlanan adım veya trusted fallback → bağımsız tam proof kabulü yok.
- Proof varsayımları, özgün problemle eşleştirilir.
- Proof son hedefi, istenen iddiayla eşleştirilir.
- Checker timeout’u → `UNKNOWN`, kabul değil.
- “Checker süreç kodu 0” tek başına yeterli kabul olayı değildir.

Alethe’nin bağımsız checker tasarımı da otomatik olarak küçük, formal doğrulanmış çekirdek anlamına gelmiyor. İlgili birincil çalışma bu güven farkını açıkça açıklıyor.[^3_14]

### 7. Etiket politikası için önerilen kural

Önerim, tek bir sıralama yerine iddiaya bağlı karar vermektir:

1. Matematiksel kontrol reddedildiyse ilgili iddia olumlu yayımlanmaz.
2. Matematiksel kontrol kararsızsa `CERTIFIED` verilmez.
3. İki yöntem yalnız aday üzerinde uyuşmuşsa tamlık/teklik iddiası yapılmaz.
4. Heyet ayrışmışsa amaçlanan doğal dil probleminin cevabı olarak yayın durdurulur.
5. Ayrışan yorumlardan birinin açık formal hesabı ayrıca gösterilecekse yeni ve sınırlı bir iddia olarak sunulur; orijinal problem çözülmüş sayılmaz.
6. Sertifika sonrası snapshot değişirse yeni kabul olayı gerekir.

Bunlar yeni tasarım önerileridir. S-12 ile ilişkili yayın tercihinin sahibi tarafından onaylanması gerekir.

______________________________________________________________________

## VI. Güvenlik ve tehdit modeli

### 1. Onay olayının dört ayrı durumu var

Görev 18’in görülen sözleşmesi:

```text
AcceptedElicitation → USER_DIRECT/elicitation
Declined/Cancelled → OS diyaloğu
```

biçiminde.

Eksik ayrım:

```text
AcceptedElicitation(data.onay=False)
```

geçerli bir form gönderimidir; onay değildir.

SDK’nın resmî örneği bunu:

- `AcceptedElicitation(data=Confirm(ok=True))`;
- diğer `AcceptedElicitation` durumları;
- `DeclinedElicitation`;
- `CancelledElicitation`

olarak ayrı işler.[^3_1]

Gerekli karar tablosu:


| Olay | Güvenli sonuç |
| :-- | :-- |
| Form gönderildi, `onay=True` | Belirtilen snapshot için onay |
| Form gönderildi, `onay=False` | Ret |
| `decline` | Ret |
| `cancel` | İptal/karar yok |
| Yeteneğin bulunmaması | Alternatif kanal değerlendirilebilir |
| Protokol/API hatası | Teknik hata; onay üretilmez |

Ret veya iptal sonrasında başka pencere açılması otomatik olarak saldırı değildir; insan kararını değiştirebilir. Fakat mevcut talebin reddini “kanal çalışmadı” gibi ele almak, ret semantiğini ve denetim kaydını bozar. Yeniden sorulacaksa yeni, açık bir karar olmalıdır.

### 2. MCP sürümü yalnız paket sürümü değildir

Güncel belgeler:

- `ctx.elicit()` back-channel yolunu legacy bağlantılarla sınırlar.
- 2026-07-28 için `InputRequiredResult`/resolver akışını açıklar.
- Yeni protokolde her isteğin kendi bağlamını taşımasını ister.[^3_7][^3_15][^3_1]

Bu nedenle şu kayıtlar ayrı tutulmalı:

```text
sdk_package_version
negotiated_protocol_version
host_name_and_version
transport
supported_input_modes
```

“`mcp>=2.3,<3` kuruldu” demek, plandaki elicitation kodunun her host’ta çalışacağını göstermez.

### 3. İmzalı state tek kullanımlı değildir

MCP belirtimi açıkça şunu söylüyor:

- Principal, süre ve istek bağlama replay penceresini daraltır.
- Bunlar tek kullanımlılığı garanti etmez.
- En çok bir kez tüketim gerekiyorsa sunucu bunu ayrıca sağlamalıdır.[^3_2]

Rigor’a aktarımı:

- Aynı onay token’ı iki worker’da tüketilirse iki ücretli model çağrısı başlayabilir.
- Aynı işin retry’ı yeni harcama gibi yürütülebilir.
- Crash sonrası “çağrı gönderildi mi?” belirsizliği oluşabilir.

Gerekli koruma, yalnız imza değil:

- Kalıcı tüketim kaydı.
- Atomik durum geçişi.
- `expected_revision`.
- İş/etki bazlı idempotency anahtarı.
- Harcama öncesi rezervasyon.
- Belirsiz dış etki durumu.


### 4. Aktörlere göre uygulanabilir sınır

| Aktör | Korunabilecek güvence | Garanti edilemeyecek |
| :-- | :-- | :-- |
| Hatalı kullanıcı | Açık iddianın matematik kontrolü | Kullanıcının yanlış fiziksel veri vermediği |
| Hatalı ajan | Kaynak/IR/alan hatalarının bir kısmı | Bütün semantik hataların yakalanması |
| Güvenilmeyen araç argümanı | Schema, capability ve snapshot kontrolü | Argümandaki “kullanıcı dedi” beyanının doğruluğu |
| Proje dizinine yazabilen saldırgan | Ayrı korunan kayıt/anahtar varsa değişiklik tespiti | Aynı dizindeki hash’in kimlik doğrulaması |
| Aynı kullanıcıda tam shell/masaüstü ajanı | Sınır açıkça beyan edilebilir; ayrı izolasyon eklenebilir | Yerel dosya ve UI’nın koşulsuz güvenilirliği |
| Zararlı belge | Veri sınırlandırma, kaynak bağlama, bazı injection testleri | Üç modelin aynı manipülasyona kapılmaması |
| Sağlayıcı/toplayıcı | Beyan, rota, kullanım ve ayar kaydı | Uzak ağırlık kimliğinin yalnız metadatayla kanıtı |

### 5. Rapor doğrulaması doğru raporun görülmesini garanti etmez

Doğru imzalı bir rapor:

- Başka probleme ait olabilir.
- Eski sürüm olabilir.
- Yanlış sonuç dosyasının yanında gösterilebilir.
- Ajan tarafından yanıltıcı özetlenebilir.

Bu nedenle doğrulayıcı yalnız “imza geçerli” dememeli; problem kimliği, kaynak manifest’i, sonuç kapsamı, tarih ve geçerli politika durumunu göstermelidir.

Yerel saldırgan doğrulayıcıyı da değiştirebiliyorsa bu zincir korunmaz. Önceki `verify-report` önerisi bu sınır altında yalnız risk azaltımıdır.

______________________________________________________________________

## VII. Model yeterliği ve hakem heyeti

### 1. 300+100 neyi gösteriyor?

Ana binom sınır:

$$
p_U=1-0{,}05^{1/n}
$$

uygun bağımsız/özdeş örnekleme ve sabit yapılandırma varsayımlarında geçerlidir.

Yeniden hesaplanan örnekler:


| Sıfır hatalı örnek | Tek taraflı %95 üst sınır |
| --: | --: |
| 30 | %9,503 |
| 60 | Yaklaşık %4,87 |
| 100 | %2,951 |
| 300 | %0,994 |
| 3.000 | %0,100’e yakın |

Bunlar:

- Tek problem için doğruluk olasılığı değildir.
- Yeni görev profiline otomatik taşınmaz.
- Şablon türevlerini bağımsız aileler yapmaz.
- 100 stres testini 100 rastgele üretim vakası gibi saydırmaz.
- `PROVEN` etiketinin matematiksel gerekçesi değildir.


### 2. İki aşamalı kabulün kalibrasyonu

Önerilen plan:

- İlk $n$ testte sıfır hata → geç.
- Tam bir hata → ikinci $n$ testte sıfır hata varsa geç.
- Diğer durumlar → kal.

Bağımsız Bernoulli varsayımıyla:

$$
P(\mathrm{PASS}\mid p)
=(1-p)^n+np(1-p)^{2n-1}.
$$

Yerel hesap:


| Gerçek kritik hata oranı | Tek aşama, 300 | İki aşama, 300+300 |
| --: | --: | --: |
| %0,1 | %74,071 | %90,547 |
| %0,5 | %22,229 | %29,679 |
| %1 | %4,904 | %5,633 |
| %2 | %0,233 | %0,237 |

Sonuç: İki aşamalı plan kullanılabilir, ama tek aşamalı planın risk yorumunu aynen korumaz.

Yalnız $p=0{,}01$ sınırındaki kabul olasılığını %5’in altına indiren eşit-aşama örneğinde 311+311 yeterli çıktı. Bu bir politika önerisi veya Rigor için optimum örneklem değildir; yalnız kabul algoritmasının yeniden kalibre edilebildiğini gösterir.

Ayrıca ilk aşamadaki kritik hata silinmez. Planın istatistiksel kabulü, o hata türünün operasyonel olarak kabul edilebilir olduğu anlamına gelmez.

### 3. IUT ile eşzamanlı aralıklar ayrılmalı

Önceki rapor, çoklu ölçüt eleştirisinde yeterince kesin değildi.

Eğer kabul kuralı:

> Bütün önceden belirlenmiş ölçütler eşiklerini geçmeli.

ise ve her bileşen testi uygun şekilde kalibre edilmişse, global null “en az bir ölçüt yetersiz” olarak kurulur. Intersection–union ilkesi global yanlış kabulü ek Bonferroni olmadan sınırlayabilir. Bunun için bileşen testlerinin birbirinden bağımsız olması zorunlu değildir.[^3_3]

Ancak bu:

> Rapordaki bütün bireysel güven aralıkları birlikte %95 kapsar.

demek değildir.

Model seçimi, profil seçimi, “geçene kadar deneme”, değişen prompt ve tekrarlanan kabul kampanyaları da aynı sabit IUT sonucuyla otomatik korunmaz.

### 4. Bireysel yeterlikten heyet güvenine geçiş

Üç modelin hata oranı ayrı ayrı $p$ ise ortak hata oranı kendiliğinden $p^3$ değildir.

Tam ilişkili hatalarda üçü de aynı vakalarda yanılır; ortak hata oranı $p$ olabilir.

Kim ve arkadaşlarının 350’den fazla modeli kapsayan çalışması, farklı mimari ve sağlayıcılarda da ilişkili hatalar bulunduğunu destekliyor. Fakat çoktan seçmeli değerlendirme ve özgeçmiş tarama sonuçları, Rigor’un formalizasyon heyetine sayısal hata oranı vermez.[^3_16]

Yeni bulunan panel çalışması da NLI ve tercih değerlendirmesinde yüksek korelasyonun panel kazancını sınırladığını bildiriyor. Onun “etkin oy” sayıları da Rigor’a taşınmamalı.[^3_17]

Ölçülmesi gerekenler:

- Birlikte yanlış formalizasyon.
- Aynı yanlış varsayım.
- Aynı kısıtı atlama.
- Kaynakta olmayan değeri birlikte ekleme.
- Hatalı değerlendirici nedeniyle birlikte geçme.
- Profil dışı görevde ortak yanlış yeterlik iddiası.


### 5. Üç üye, iki aile, 30 gün

Bunların hiçbiri mevcut kanıtla bilimsel zorunluluk değil.

- Üç üye: süreç kapsamı tercihi.
- İki aile: çeşitlilik göstergesi.
- 30 gün: operasyonel yeniden ölçüm takvimi.
- Ücretli erişim: fiyat/erişim özelliği; ispat özelliği değil.
- Yeterlik kaydı: kapsamlı ölçüm kanıtına işaret eden kayıt; modelin genel doğruluk sertifikası değil.

S-5’in kaldırılması veya yeniden yazılması yine sahip onayı gerektirir. Araştırma bunu kendiliğinden yapamaz.[^3_13]

______________________________________________________________________

## VIII. Teknik sözleşmeler ve uygulama hazırlığı

### Sözleşme değişikliklerinin faz etkisi

| Şimdi yapılacak değişiklik | Yapılmazsa kırılacak alan |
| :-- | :-- |
| `result_scope`: aday/tam küme/tek çözüm | F1 solver, F2 ODE, F7 finans, F8 optimizasyon |
| Operatör semantiği ve Decimal trace | F1 compiler, F7 birebir mutabakat, replay |
| Bütün AST köklerinde tanımlılık | Identity, forall, optimizasyon ve Lean’e giriş |
| Değişmez snapshot | Session, onay, sertifika, rapor, şablon |
| Onay olayının ayrıntılı durumu | MCP, OS diyaloğu, S-12, bütçe izni |
| Sertifika kabul profili | `CERTIFIED`, `PROVEN`, bağımsız checker |
| İş revision/idempotency | Uzun işler, retry, bütçe, crash recovery |
| Tarihsel/güncel politika ayrımı | Şablon, yeterlik süresi, eski rapor ve replay |

### Önceki snapshot önerisinin düzeltilmesi

Tek başına:

$$
H_{\text{onay}}=H_{\text{çözüm}}
$$

yeterli değildir. Hash’e giren şeyin anlamı eksikse aynı hash altında farklı semantik yorumlar çalışabilir.

Snapshot en az şunları bağlamalı:

- IR schema.
- Sayı alanı ve operasyon semantiği.
- Birim tanımları.
- Model kütüphanesi referansları.
- Hedef kapsamı.
- Kaynak dosya manifest’i.
- İlgili politika kimliği.

Ayrıca Görev 14’te kök seçimi sonrasında IR’a yeni eşitlik eklenmesi, önceki genel “onaylanan=çözülen” önerisinin fazla katı uygulanabileceğini gösteriyor.

Daha doğru iki seçenek:

1. Yeni problem snapshot’ı oluşturup yeniden onaylamak.
2. Eski snapshot’a bağlı, seçenek kümesi ve seçilen kökü açıkça taşıyan bir daraltma kararı kaydetmek.

İkinci seçenek kullanılabilir; fakat “IR değişmedi” diye gösterilmemelidir.

### En küçük v1 ihtiyaçları karşılıyor mu?

Ekli brief’teki en küçük v1 önerisi bütün sahip ihtiyaçlarını otomatik karşılamıyor:

- R1–R7, roket önceliği R1–R11’in tamamı değil.
- “Finans B1” yalnız basit özdeşliklerden oluşmuyor.
- Decimal rounding trace olmadan birebir mutabakat eksik kalır.
- Optimizasyon ertelenirse ilgili portföy çıktılarının hangi kısmının sadece yeniden hesaplandığı açık olmalı.
- `.ork` ertelense bile karşılaştırma için motor, rüzgâr, kütle, koordinat ve olay tanımlarının eşleşmesi gerekir.

Bu nedenle önerilen v1, “sahibin bütün ihtiyaçları karşılandı” değil:

> Sahibin seçilmiş hesaplarını güvenli kapsamla karşılayan ilk kullanılabilir sürüm.

olarak sunulmalıdır. Hangi hesapların kabul kriteri olduğu sahip tarafından seçilmelidir.

______________________________________________________________________

## IX. Önceki önerilerin adversarial sınanması

| Önceki öneri | Korunan yarar | Çürütülen aşırı yorum | Kabul koşulu |
| :-- | :-- | :-- | :-- |
| Küçük bağımsız checker | TCB’yi daraltır | Küçük olması sağlam olduğu anlamına gelmez | İddia dili, sağlamlık argümanı, negatif proof paketi |
| Hash’e bağlı onay | Problem karışmasını azaltır | İnsan kimliğini ve anlamın doğruluğunu kanıtlamaz | Semantik bağlam dahil snapshot ve güvenilir receipt |
| Üç yeterlikli model | İnceleme çeşitliliği sağlar | Ortak hatayı $p^3$ yapmaz | Heyet düzeyinde ortak hata ölçümü |
| İmzalı yeterlik kaydı | Köken/bütünlük | Güncellik ve doğru kapsam sağlamaz | Süre, iptal, politika ve runtime eşleşmesi |
| OS penceresi | Konuşma kanalından ayrılır | Aynı kullanıcıdaki ajanı kesin dışlamaz | Açık tehdit sınırı, varsayılan onay yok, snapshot gösterimi |
| Yeni parser | Belirli dilde deterministik okuma | Kullanıcı niyetini ve kaynak tüketimini çözmez | Dilbilgisi, limitler, roundtrip ve differential test |
| `PROVEN` kapalı | Bir etiket yolunu kapatır | Yanlış `CERTIFIED`/sahte çaprazlamayı engellemez | Bütün olumlu yayınlar için false-accept testleri |
| Kalıcı worker | İstemci yaşamından ayrılır | Çift harcama/replay’i çözmez | Atomik iş durumu, idempotency ve bütçe rezervasyonu |
| `verify-report` | Değişiklik kontrolü | Doğru problemin doğru raporunun görüldüğünü garanti etmez | Problem kimliği ve güvenilir doğrulayıcı |
| Kaynak alıntısı | Bazı aktarım hatalarını yakalar | Alıntının doğru yorumlandığını kanıtlamaz | Kaynak–IR semantik inceleme ayrı |

### Sağlayıcı önerilerindeki düzeltme

Anthropic’in güncel tam metni hem geliştiricilerin kullanıcı adına abonelik yönlendirmesini kısıtlıyor hem de ürün içinde barındırılmış olsa bile son kullanıcının değiştirilmemiş Claude Code’a kendi aboneliğiyle girişini açıkça istisna tutuyor. Bu iki hükümden “her CLI sarmalayıcısı yasak” sonucu çıkarılamaz.[^3_4]

OpenAI, `codex exec` kullanımını betik ve pipeline için açıkça belgeliyor. Public/OSS uyarısı, ilgili sayfada ChatGPT-managed CI/CD kimlik dosyası akışının içinde yer alıyor; bütün yerel açık kaynak kullanımına genellenmemeli.[^3_5]

Google, OAuth kimliğinin üçüncü taraf yazılımla harvest/piggyback edilmesini yasaklıyor. Bu, bütün headless çağrıların aynı hukuki kategori olduğu anlamına gelmez.[^3_18]

Güvenli öneri değişmiyor ama gerekçesi daralıyor: token köprüleme yapılmamalı; her sağlayıcı için kullanım modeli ve kimlik yöntemi ayrı değerlendirilmeli. Belirsizlik yerel matematik çekirdeğini engellememeli.

______________________________________________________________________

## X. Yeni Red Team bulguları

Aşağıdaki sekiz kayıt, önceki raporda ayrı ve somut bulgu olarak yer almayan noktalardır. BLOCKER derecesi, ilgili güvence yolunun değişikliksiz uygulanmasını engeller; bütün projenin imkânsız olduğunu söylemez.

### P2-01 — Yerel kök uyuşmasının teklik/tamlık yerine geçmesi

- Önem: BLOCKER.
- Kanıt: VERIFIED.
- Konum: Faz 1 Görev 11, `crosscheck_numeric`; Görev 14 sonuç akışı.
- Başarısızlık: Eksik aday listesi + yerel arama uyuşması → tam/tek çözüm gibi rapor.
- Yeni kanıt: SymPy 1.14 ve mpmath izole deneyleri; SymPy birincil belge.[^3_6]
- Düzeltme: Aday geçerliliği, teklik ve tamlığı ayrı alanlar yap.
- Alternatif: Tamlık yoksa yalnız aday raporu veya ret.
- Maliyet: Şema için orta; genel tamlık için yüksek.
- Regresyon: `sin(x)=0`, özdeş sıfır denklem, çok köklü polinom.
- Kalan risk: Solver’ın eksik veya hatalı küme temsili.
- Sahip onayı: Yeni yayın kapsamı için gerekli.


### P2-02 — `mod` ve sayı işlemlerinde backend semantik farkı

- Önem: BLOCKER.
- Kanıt: VERIFIED.
- Konum: Görev 3 `OpName`; Görev 8 derleyiciler; Görev 13 modüler hesap.
- Başarısızlık: Aynı IR farklı matematiksel sonuçlara derlenir.
- Düzeltme: Operatör profili veya destek daraltması.
- Alternatif: İlk sürümde yalnız pozitif tamsayı bölen.
- Maliyet: Düşük–orta.
- Regresyon: Pozitif/negatif operandların bütün işaret kombinasyonları; Decimal remainder.
- Kalan risk: `pow`, `floor`, division gibi diğer operatörler.
- Sahip onayı: Kapsam daralırsa gerekli.[^3_8][^3_10]


### P2-03 — Hedef ifadelerinde tanımlılık yükümlülükleri eksik tanımlı

- Önem: BLOCKER.
- Kanıt: SUPPORTED.
- Konum: Görev 7, 12, 13; tasarım §6.3.
- Başarısızlık: Sadeleştirme alan koşulunu siler; yanlış kapsamlı özdeşlik kabul edilir.
- Düzeltme: Bütün AST köklerinden, sadeleştirmeden önce yükümlülük çıkar.
- Alternatif: İlk checker’ı total polinom/rasyonel alt kümeyle sınırla.
- Maliyet: Orta.
- Regresyon: `x/x`, `x**-1`, log/sqrt/tan sınırları.
- Kalan risk: Dal seçimi ve karmaşık sayı semantiği.
- Sahip onayı: Teknik düzeltme için değil; kapsam daralması için gerekli.

Bu, uygulamada exploit edildiği doğrulanmış bir açık değildir. Eksik sözleşmenin kritik sonucudur.

### P2-04 — Form gönderimi ile gerçek onay kararının karışması

- Önem: BLOCKER.
- Kanıt: SUPPORTED.
- Konum: Görev 18, `ConfirmForm.onay` ve `AcceptedElicitation` eşlemesi.
- Başarısızlık: `accept` taşıyan fakat `onay=False` olan form, onay gibi yorumlanabilir.
- Düzeltme: Eylem ve içerik değerini birlikte kontrol et; decline/cancel ayrımını koru.
- Alternatif: Onay adaptörünü tek tipli karar nesnesine indir.
- Maliyet: Düşük.
- Regresyon: `accept+True`, `accept+False`, decline, cancel, malformed, capability yokluğu.
- Kalan risk: Handler’ın otomatik yanıtı ve insan kökeni.
- Sahip onayı: Ret/devretme politikası için gerekli.[^3_1]


### P2-05 — MCP protokol çağı ve retry yürütme sözleşmesi eksik

- Önem: HIGH.
- Kanıt: VERIFIED.
- Konum: Tasarım §7.2; Görev 18.
- Başarısızlık: Yeni protokolde eski back-channel çağrısı; retry’da çift yürütme veya devam edememe.
- Düzeltme: Negotiated-version adaptörü, MRTR/resolver yolu, kalıcı iş kimliği.
- Alternatif: İlk sürümde açıkça sınanmış legacy uyumluluk profili.
- Maliyet: Orta.
- Regresyon: İki protokol profili, restart, çift retry, başka principal/argümanla state kullanımı.
- Kalan risk: Host uyumluluğu ve SDK sürüm değişimi.
- Sahip onayı: Desteklenen istemci profilleri için gerekli.[^3_2][^3_1]


### P2-06 — Kapalı form ODE/PDE sertifikasında teklik kapsamı

- Önem: HIGH.
- Kanıt: VERIFIED — matematiksel karşı örnek.
- Konum: Tasarım §6.6.
- Başarısızlık: Bir geçerli yörünge, problem tarafından zorunlu tek yörünge gibi sunulur.
- Düzeltme: `VALID_SOLUTION` ile `UNIQUE_SOLUTION` ayrımı.
- Alternatif: Teklik gösterilemiyorsa koşullu çözüm.
- Maliyet: Şema düşük; genel teklik doğrulaması yüksek.
- Regresyon: $y'=\sqrt y,\ y(0)=0$.
- Kalan risk: Çözümün varlık aralığı ve singularite.
- Sahip onayı: Çözüm sunum kapsamı için gerekli.


### P2-07 — Proof object içindeki boş/trusted adımlar

- Önem: HIGH.
- Kanıt: VERIFIED — birincil araç belgesi.
- Konum: Checker seçimi ve `Certificate` kabul profili.
- Başarısızlık: Proof üretildiği için eksiksiz bağımsız kontrol var sayılır.
- Düzeltme: Her kuralın destek ve kabul durumu; hole/unknown’da fail-closed.
- Alternatif: Dar, izinli proof profili.
- Maliyet: Orta–yüksek.
- Regresyon: Bilerek hole, bilinmeyen kural, değiştirilmiş varsayım ve yanlış sonuç eklenmiş proof.
- Kalan risk: Checker uygulama hatası.
- Sahip onayı: TCB ve kapsam seçimi için gerekli.[^3_11]


### P2-08 — Finans/optimizasyon sırası iki belgede farklı

- Önem: MEDIUM.
- Kanıt: VERIFIED.
- Konum: Tasarım §10; yol haritası §2.
- Başarısızlık: Uygulayıcı farklı bağımlılık ve teslimat sırası izler.
- Düzeltme: Tek bağımlılık grafiği ve türetilmiş faz tabloları.
- Alternatif: Bir belgeyi normatif, diğerini bilgilendirici ilan et.
- Maliyet: Düşük.
- Regresyon: Faz bağımlılıklarının otomatik tutarlılık kontrolü.
- Kalan risk: Yeni sahip kararlarının senkronize edilmemesi.
- Sahip onayı: Öncelik tercihi için gerekli.

Bu bulguların CSV kaydı da sunuluyor.

______________________________________________________________________

## XI. Önceliklendirilmiş düzeltmeler

### P0 — Güven etiketi üreten uygulama başlamadan

1. Sonuç kapsamını ayır: aday, tam küme, tek çözüm, enclosure, optimalite.
2. Sayı alanı ve operatör semantiğini dondur.
3. Domain yükümlülüklerini bütün hedeflere uygula.
4. `CheckReceipt` ile sertifika varlığını ve kabulünü ayır.
5. Onay eylemi/içeriği/kökeni ayrımını düzelt.
6. Snapshot ile daraltma kararlarını sürümlendir.
7. Etiket politikasını bu kayıtların türevi yap.

Bunlar Görev 3, 7–15 ve 18’in güvenilir sözleşmesini etkiliyor.

### P1 — Dar çekirdeğin kabul paketi

- Bozuk sertifika.
- Yanlış alan.
- Negatif modulo.
- Sadeleştirmede kaybolan domain.
- Eksik kök.
- Bütün değerlerin çözüm olduğu denklem.
- Onay sonrası nested mutation.
- `accept+False`.
- Hash’i yeniden hesaplanmış değiştirilmiş kayıt.
- Aynı kontrolün iki kez çalıştırılıp iki bağımsız yol gibi sunulması.


### P2 — Sahip öncelikli kullanılabilir sürüm

- Kesin rasyonel ve açık Decimal trace.
- Seçilmiş roket hesapları.
- Finans B1/B2’nin belirlenmiş alt kümesi.
- Veri manifest’i.
- Deterministik rapor.
- SDK.
- Sınanmış MCP profili.


### P3 — Uzak modeller ve uzun işler

- Sağlayıcı/kimlik yöntemi allowlist’i.
- Veri aktarım izni.
- Atomik bütçe rezervasyonu.
- Kalıcı iş revision’ı.
- MRTR/retry güvenliği.
- Değerlendirici kabulü.
- Sonra yeterlik ve heyet ölçümü.


### P4 — Genişleme

Lean, geniş belge okuyucular, öğrenen hakem ve genel alan paketi ekosistemi.

Erteleme, güvenlik kontrolünün kaldırılması anlamına gelmemeli. Örneğin doğal dil ertelenirse ajan IR’ı “insanın doğrulanmış yorumu” diye sunulmaz; uzak çağrı ertelenirse bütçe altyapısı eksik olduğu için gizlice abonelik çağrısı yapılmaz.

______________________________________________________________________

## XII. Sahip onayı gerektiren kararlar

| Karar | Önerilen seçenek | Onay yoksa güvenli geçici davranış | Engellediği |
| :-- | :-- | :-- | :-- |
| Sonuç kapsamı | Aday/tamlık/teklik ayrı | Gösterilemeyen kapsamı iddia etme | Solver ve rapor |
| S-12 “bilmiyorum” | Açık formal hesap, yorum onayı yok | Orijinal problem çözülmüş sayılmaz | Yayın politikası |
| S-5/S-9 | Fiyat yerine ölçülmüş yeterlik | Üst süreç etiketi kapalı | `PROVEN` |
| v1 `PROVEN` | İlk dar sürümde kapalı | Kapalı | Heyet altyapısı |
| Negatif mod/remainder | Ayrı operatör veya açık daraltma | Desteklenmeyeni reddet | IR/compiler |
| Rigor’un yerel saldırgan kapsamı | Güvence seviyeleri açık | Tam shell’e karşı insan onayı garantisi verme | Güvenlik vaadi |
| MCP istemci profili | Sınanmış protokol/host matrisi | Desteklenmeyen onay yolu kullanma | Dağıtım |
| İki aşamalı yeterlik | Yeniden kalibre edilmiş, tüm denemeleri saklayan politika | Eski plana otomatik geçiş yok | Qualification |
| Lean v1 | Sahip ihtiyaçlarına göre açık erteleme kararı | K26 yürürlükte kalır | Kapsam |
| İlk v1 hesap listesi | Roket ve finans için somut kabul envanteri | “Bütün ihtiyaçlar karşılandı” deme | Teslimat |

K ve S kararları bu raporla değiştirilmedi. Öneriler, kabul bekleyen maddelerdir.

______________________________________________________________________

## XIII. Araştırmalar arası ilerleme matrisi

### Önceki bulgular

| Sınıf | Kayıtlar | Anlamı |
| :-- | :-- | :-- |
| CONFIRMED | RT-001, RT-011 | Yeni inceleme önceki sonucu koruyor |
| STRENGTHENED | RT-002, RT-003, RT-004, RT-005, RT-006, RT-009 | Tam belge, birincil kaynak veya deney eklendi |
| CORRECTED | RT-007, RT-008, RT-010, RT-012 | Önceki kapsam/ifade daraltıldı |
| REJECTED | RT-007’nin “normalizasyon tanımlı değil” alt iddiası | Görev 11 bu hükmü içeriyor |
| NEW | P2-01…P2-08 | Önceki raporda ayrı somut bulgu olmayan kayıtlar |
| UNRESOLVED | Etiket semantiği, S-5/S-9, S-12, güvenilir onay, checker profili | Araştırma yön gösteriyor; karar/uygulama eksik |
| NOT VERIFIED | Gerçek adaptörler, host entegrasyonu, model yeterliği, proof zinciri | Bu turda çalıştırılmadı |

Bu sınıflandırma, “sorun düzeltildi” anlamına gelmez. Depo değiştirilmediği için mimari riskler giderilmiş değildir; yalnız daha doğru sınıflandırılmıştır.

### Gerçek kapanan kanıt boşlukları

- Faz 1 planının kesilen kısmı okundu.
- Ana tasarımın eksik bölümleri patch geçmişi üzerinden incelendi.
- Aralık sıfır kontrolünün zaten güvenli tanımlandığı görüldü.
- SI normalizasyonunun zaten planlandığı görüldü.
- CSV sayısal içerikleri yeniden hesaplandı.
- Frozen nested mutation çalıştırıldı.
- SymPy aday listesi/tamlık karşı örneği çalıştırıldı.
- Decimal trace farkı çalıştırıldı.
- Çoklu yerel kök araması/teklik karşı örneği çalıştırıldı.
- MCP’nin yeni protokol ve state güvenlik hükümleri birincil kaynaktan doğrulandı.


### Açık kalan kanıt boşlukları

- Üç uzun Deep Research raporunun bütün kesilen bölümleri.
- Güncel tasarımın yerelde bayt düzeyinde yeniden kurulup blob hash’iyle karşılaştırılması.
- Pydantic 2.14 ve mpmath 1.4 hedeflerinde aynı deneylerin tekrarı.
- Rigor’un gerçek Session, checker, compiler ve MCP entegrasyon testleri.
- Model/heyet ölçümü.
- Kullanıcı onayı arayüzü deneyleri.
- Sağlayıcıların Rigor’un belirli dağıtım modeline bağlayıcı uygunluk görüşü.

Bunlar kapatılmış gibi gösterilmedi.

______________________________________________________________________

## XIV. Nihai mimari durum

Nihai karar: **ARCHITECTURE_CHANGES_REQUIRED**.

Geçerlilik kapsamı: Sabit HEAD’deki ana tasarımın incelenen metinsel kapsamı, tamamı okunan Faz 1 planı, yol haritası, ilgili karar kayıtları ve bu raporda belirtilen birincil kaynak/izole deneyler.

Bu karar, bütün geçmiş araştırmaların eksiksiz denetlendiği veya uygulanmış ürünün güvenlik sertifikası verildiği anlamına gelmez.

### Hâlâ engelleyici olanlar

- Aday geçerliliği ile teklik/tamlığın karışması.
- Rational/Decimal/Real ve operatör semantiği.
- Hedef ifadelerinde tanımlılık sözleşmesi.
- Sertifika kabul olayının yeterli ayrıntıyla modellenmemesi.
- Onay eylemi, karar değeri ve insan kökeninin karışması.
- Onaylanan snapshot ile sonradan daraltılan problem arasındaki bağ.
- Bütün olumlu etiketler için yanlış kabul testlerinin bulunmaması.


### Önceki raporda yanlış veya fazla geniş değerlendirilenler

- Birim normalizasyonu yokluğu.
- Yerel tam yetkili ajan sınırının hiç belgelenmediği iddiası.
- Bütün çoklu ölçütler için otomatik multiplicity düzeltmesi çağrışımı.
- Genel resmî CLI otomasyon yasağına yaklaşan yorum.
- Dual sertifikanın MILP’de hiçbir koşulda yeterli olamayacağı izlenimi.
- `frozen=True` riskinin Rigor üzerinde kanıtlanmış exploit gibi okunabilecek önemi.


### Güvenli biçimde ertelenebilecekler

Sahip onayıyla:

- Üst süreç etiketi `PROVEN`.
- Genel doğal dil formülasyonu.
- Çok üyeli yeterlik altyapısı.
- PDF/DOCX.
- Öğrenen hakem.
- Geniş alan paketi araçları.
- Genel MILP sertifikasyonu.
- Lean entegrasyonu — K26 ayrıca değiştirilerek.

Ertelenemeyecek olan, yayımlanan sonucun neyi doğruladığını dürüstçe belirtmesidir.

### Artık daha güçlü desteklenen mimari yön

- LLM üretimi ile deterministik kontrolün ayrılması.
- Açık IR ve kapalı destek kapsamı.
- Küçük, iddiaya özgü checker profilleri.
- Çözüm üretimi ile çözüm kabulünün ayrılması.
- Semantik snapshot ve kabul kayıtları.
- Yeterliği sonuç garantisi değil, süreç önkoşulu saymak.
- Doğal dil yorumu ile matematiksel ispatı ayrı raporlamak.

Önceki araştırmaya göre en önemli ilerleme, daha fazla hata saymak değil; bazı şüpheleri geri çekip yanlış güven üretiminin daha somut yollarını belirlemek oldu. Özellikle yerel kök araması, backend modulo semantiği, form gönderimi/onay ayrımı ve retry tek-kullanımlılığı artık uygulanabilir negatif kabul testlerine dönüştürülebiliyor.

Rigor’un güvenilir ilk sürümü, “çok sayıda kontrol geçti” diyen bir sistemden önce, şu cümleyi teknik olarak doğru kurabilen bir sistem olmalıdır:

> Bu değişmez problem snapshot’ındaki bu iddia, bu kapsamda, bu denetleyici tarafından kabul edildi; bunun dışındaki yorum, kaynak ve gerçek dünya iddiaları doğrulanmış sayılmıyor.

Bu çalışma sırasında ürün kodu yazılmadı, depo değiştirilmedi ve GitHub üzerinde yazma işlemi yapılmadı. Yalnız salt okunur inceleme, bağımsız sayısal hesaplar ve izole karşı örnek deneyleri gerçekleştirildi.

<span style="display:none">[^3_100][^3_101][^3_102][^3_103][^3_104][^3_105][^3_106][^3_107][^3_108][^3_109][^3_110][^3_111][^3_19][^3_20][^3_21][^3_22][^3_23][^3_24][^3_25][^3_26][^3_27][^3_28][^3_29][^3_30][^3_31][^3_32][^3_33][^3_34][^3_35][^3_36][^3_37][^3_38][^3_39][^3_40][^3_41][^3_42][^3_43][^3_44][^3_45][^3_46][^3_47][^3_48][^3_49][^3_50][^3_51][^3_52][^3_53][^3_54][^3_55][^3_56][^3_57][^3_58][^3_59][^3_60][^3_61][^3_62][^3_63][^3_64][^3_65][^3_66][^3_67][^3_68][^3_69][^3_70][^3_71][^3_72][^3_73][^3_74][^3_75][^3_76][^3_77][^3_78][^3_79][^3_80][^3_81][^3_82][^3_83][^3_84][^3_85][^3_86][^3_87][^3_88][^3_89][^3_90][^3_91][^3_92][^3_93][^3_94][^3_95][^3_96][^3_97][^3_98][^3_99]</span>

<div align="center">⁂</div>

[^3_1]: https://py.sdk.modelcontextprotocol.io/handlers/elicitation/

[^3_2]: https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr

[^3_3]: https://projecteuclid.org/journals/statistical-science/volume-11/issue-4/Bioequivalence-trials-intersection-union-tests-and-equivalence-confidence-sets/10.1214/ss/1032280304.pdf

[^3_4]: https://code.claude.com/docs/en/legal-and-compliance

[^3_5]: https://developers.openai.com/codex/noninteractive

[^3_6]: https://docs.sympy.org/latest/modules/solvers/solveset.html

[^3_7]: https://py.sdk.modelcontextprotocol.io/handlers/multi-round-trip/

[^3_8]: https://smt-lib.org/theories-Ints.shtml

[^3_9]: https://smt-lib.org/theories-Reals.shtml

[^3_10]: https://docs.python.org/3/library/decimal.html

[^3_11]: https://cvc5.github.io/docs/latest/proofs/output_alethe.html

[^3_12]: https://cvc5.github.io/docs/cvc5-1.4.2/proofs/output_alethe.html

[^3_13]: concepts_brief.md

[^3_14]: https://verit.loria.fr/papers/pxtp2021.pdf

[^3_15]: https://modelcontextprotocol.io/specification/2026-07-28/basic

[^3_16]: https://arxiv.org/abs/2506.07962

[^3_17]: https://arxiv.org/html/2605.29800v1

[^3_18]: https://geminicli.com/docs/resources/faq/

[^3_19]: https://py.sdk.modelcontextprotocol.io/migration/

[^3_20]: https://py.sdk.modelcontextprotocol.io/api/mcp/client/auth/

[^3_21]: https://py.sdk.modelcontextprotocol.io/v1/

[^3_22]: https://py.sdk.modelcontextprotocol.io/

[^3_23]: https://py.sdk.modelcontextprotocol.io/servers/completions/

[^3_24]: https://py.sdk.modelcontextprotocol.io/handlers/subscriptions/

[^3_25]: https://py.sdk.modelcontextprotocol.io/handlers/lifespan/

[^3_26]: https://py.sdk.modelcontextprotocol.io/v2/api/mcp/server/mcpserver/context/

[^3_27]: https://py.sdk.modelcontextprotocol.io/v2/ko/client/callbacks/

[^3_28]: https://py.sdk.modelcontextprotocol.io/api/mcp/shared/subscriptions/

[^3_29]: https://py.sdk.modelcontextprotocol.io/v2/hi/troubleshooting/

[^3_30]: https://py.sdk.modelcontextprotocol.io/tr/get-started/

[^3_31]: https://github.com/ErenTahiroglu

[^3_32]: https://rigor.typedduck.fail/apiref/

[^3_33]: https://github.com/rigortype/rigor/blob/d01a937b/lib/rigor/cli/check_command.rb

[^3_34]: https://github.com/RafaelFerSilva/refinement-agent-skills/blob/main/skills/bootstrap-context/SKILL.md

[^3_35]: https://github.com/rigortype/rigor/blob/c26e0120/spec/rigor/language_server/end_to_end_spec.rb

[^3_36]: https://github.com/rigortype/rigor/blob/c26e0120/docs/CURRENT_WORK.md?plain=1

[^3_37]: https://rigor.typedduck.fail/handbook/

[^3_38]: https://rigor.typedduck.fail/manual/plugins/

[^3_39]: https://github.com/rigortype/rigor/blob/master/skills/rigor-project-init/SKILL.md

[^3_40]: https://github.com/rigortype/rigor/blob/c26e0120/spec/docs/spec_analyzer_guard_spec.rb

[^3_41]: https://docs.pydantic.dev/2.10/concepts/models

[^3_42]: https://docs.pydantic.dev/fastui/api/python_components/

[^3_43]: https://docs.pydantic.dev/fastui/

[^3_44]: https://verit.loria.fr/documentation/alethe-spec.pdf

[^3_45]: https://verit.loria.fr/papers/cade2019.bib

[^3_46]: https://verit.loria.fr/papers/scp2014.bib

[^3_47]: https://verit.loria.fr/download/tip/proofonomicon.pdf

[^3_48]: https://verit.loria.fr/papers/abz2012.bib

[^3_49]: https://verit.loria.fr/papers/cade2021.pdf

[^3_50]: https://verit.loria.fr/

[^3_51]: https://verit.loria.fr/alethe.pdf

[^3_52]: https://verit.loria.fr/papers/jar2020.pdf

[^3_53]: https://projecteuclid.org/journals/statistical-science/volume-11/issue-4/Bioequivalence-trials-intersection-union-tests-and-equivalence-confidence-sets/10.1214/ss/1032280304.full

[^3_54]: https://www.jstor.org/stable/pdf/2246024.pdf

[^3_55]: https://www.sciencedirect.com/science/article/pii/S0167715210003445

[^3_56]: https://stat.ethz.ch/CRAN//web/packages/SimTOST/vignettes/workflow.html

[^3_57]: https://aaroncaldwell.us/SimplyAgree/articles/agreement_analysis.html

[^3_58]: https://onlinelibrary.wiley.com/doi/full/10.1002/sim.6247

[^3_59]: https://www.stat.rice.edu/~rguerra/books/meta/MetaBook_Dar/MetaBook/Kim/meta-book-%20IUT%20chapter-001.3.doc

[^3_60]: https://doczz.net/doc/8629911/bioequivalence-trials--intersection–union-tests-and

[^3_61]: http://dml.mathdoc.fr/item/1032280304/

[^3_62]: https://docs.sympy.org/latest/modules/sets.html

[^3_63]: https://docs.sympy.org/latest/explanation/active-deprecations.html

[^3_64]: https://docs.sympy.org/dev/tutorials/intro-tutorial/solvers.html

[^3_65]: https://docs.sympy.org/latest/guides/solving/solve-equation-algebraically.html

[^3_66]: https://docs.sympy.org/latest/guides/solving/solving-guidance.html

[^3_67]: https://docs.sympy.org/latest/explanation/solve_output.html

[^3_68]: https://docs.sympy.org/latest/modules/solvers/solvers.html

[^3_69]: https://docs.sympy.org/latest/guides/solving/solve-system-of-equations-algebraically.html

[^3_70]: https://docs.sympy.org/latest/\_sources/explanation/solve_output.rst.txt

[^3_71]: https://smt-lib.org/logics-all.shtml

[^3_72]: https://smt-lib.org/version3.shtml

[^3_73]: https://smt-lib.org/index.shtml

[^3_74]: https://smt-lib.org/Logics/LIA.smt2

[^3_75]: https://smt-lib.org/theories-Reals_Ints.shtml

[^3_76]: https://smt-lib.org/theories-FixedSizeBitVectors.shtml

[^3_77]: https://smt-lib.org/papers/smt-lib-reference-v2.7-r2025-02-05.pdf

[^3_78]: https://smt-lib.org/papers/smt-lib-reference-v2.0-r10.12.21.pdf

[^3_79]: https://smt-lib.org/language.shtml

[^3_80]: https://cvc5.github.io/docs/cvc5-1.1.2/proofs/output_alethe.html

[^3_81]: https://cvc5.github.io/docs/latest/proofs/proofs.html

[^3_82]: https://cvc5.github.io/docs/cvc5-1.0.2/proofs/proofs.html

[^3_83]: https://cvc5.github.io/blog/2024/03/15/isabelle-reconstruction.html

[^3_84]: https://cvc5.github.io/docs/cvc5-1.0.9/proofs/output_alf.html

[^3_85]: https://cvc5.github.io/tutorials/beginners/theories.html

[^3_86]: https://cvc5.github.io/docs/cvc5-1.0.2/proofs/output_alethe.html

[^3_87]: https://cvc5.github.io/docs/cvc5-1.3.0/proofs/output_alethe.html

[^3_88]: https://www.arxiv.org/list/cs.CL/2025-06?skip=750\&show=25

[^3_89]: https://arxiv.org/html/2609.04373v1

[^3_90]: https://arxiv.org/html/2607.20464v2

[^3_91]: https://arxiv.org/audio/2506.07962

[^3_92]: https://arxiv.org/html/2610.13548v1

[^3_93]: https://arxiv.org/html/2610.01471v2

[^3_94]: https://arxiv.org/pdf/2611.09194.pdf

[^3_95]: https://ar5iv.labs.arxiv.org/html/2506.07962

[^3_96]: https://docs.python.org/3/tutorial/floatingpoint.html

[^3_97]: https://docs.python.org/3/library/math.html

[^3_98]: https://docs.python.org/3/reference/expressions.html

[^3_99]: https://docs.python.org/3/builtins/functions.html

[^3_100]: https://docs.python.org/3/builtins/stdtypes.html

[^3_101]: https://docs.python.org/3/library/time.html

[^3_102]: https://docs.python.org/ja/2.7/\_sources/library/decimal.rst.txt

[^3_103]: https://docs.pydantic.dev/latest/concepts/models/

[^3_104]: https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28

[^3_105]: https://py.sdk.modelcontextprotocol.io/api/mcp/server/request_state/

[^3_106]: https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices

[^3_107]: https://ts.sdk.modelcontextprotocol.io/v2/api/index/@modelcontextprotocol/client/

[^3_108]: https://modelcontextprotocol.io/specification/2026-07-28

[^3_109]: https://modelcontextprotocol.io/specification/2026-07-28/schema

[^3_110]: https://py.sdk.modelcontextprotocol.io/api/mcp/server/elicitation/

[^3_111]: https://blog.modelcontextprotocol.io/posts/2026-07-28/

