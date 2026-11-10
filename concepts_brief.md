# Rigor — hakem heyeti ve model erişimi

- **Yazar:** Eren Tahiroğlu
- **Tarih:** 2026-11-10
- **Durum:** Taslak. Soru 1 ve soru 2 kapandı (sahibin gösterdiği raporlara göre; onay bekleyen maddeler aşağıda
  listeli). Soru 3 sürüyor; sorular 4–6 açık. Taze gözle inceleme (alt ajanlar) henüz yapılmadı. Kararlar tasarım
  belgesine henüz işlenmedi; sorular kapanınca tek revizyonda işlenecek.

## Genel bakış

Rigor, bir yapay zekâya yaptırılan matematiğin doğruluğunu denetleyen bir araç. Henüz kod yok; tasarım belgesi
(`docs/superpowers/specs/2026-11-07-rigor-design.md`), yol haritası ve Faz 1 planı var.

Bu belge, sahibin 2026-11-10'da verdiği altı kararın tasarımı nasıl değiştireceğini çalışır:

1. Hedef kullanıcı, aracı GitHub'da bulup kuran bir yabancıdır. Bu kişide Claude, ChatGPT, Gemini aboneliği olmayabilir.
2. İki adım vardır: önce matematik kütüphaneleriyle analiz, sonra ücretsiz ve ücretli API listesinden hakem heyeti.
3. Ücretli API'ler zorunlu değildir, ama kullanıcıda varsa istenir.
4. Toplu API toplayıcıları (OpenRouter türü) listeye girebilir.
5. Yalnızca ücretsiz modellerle doğrulanan sonuç `KANITLANDI` almaz; bir alt doğrulama seviyesi alır.
   (Soru 2'de yeterlik temelli metinle değiştirildi; aşağıya bakın.)
6. DeepSeek Harness işe yararsa kullanılır.

## Analiz

### Soru 1 (kapandı): Sertifikası olan ama tam heyetten geçmemiş sonuç ne alır?

Kaynak: sahip `docs/research/Deep Research/Soru1-2` dosyasını cevap olarak gösterdi.

| Etiket | Anlamı |
| --- | --- |
| `PROVEN` / KANITLANDI | Matematiksel kanıt kabul edildi **ve** Rigor'un tam güvence koşulları sağlandı (heyet, doğrudan onay, köken). Faz 1'de verilmez. |
| `CERTIFIED` / MATEMATİKSEL SERTİFİKA DOĞRULANDI | Gösterilen matematiksel iddianın sertifikası denetleyicide kabul edildi; tam heyet koşulları sağlanmamış olabilir. |
| `CROSS_VALIDATED` / ÇAPRAZ DOĞRULANDI | Gerçekten ayrı hesap yöntemleri karşılaştırıldı ve uyuştu; formal kanıt yok. |
| `REFUSED` / REDDEDİLDİ | Cevap verilmedi; nedeni yazılır. |

- Etiketler bir doğruluk merdiveni olarak sunulmaz.
- Özet kutusunda dört alan zorunludur: sonuç ve etiket; doğrulanan işlem; problem incelemesi; sınır.
- Gerçekleşmemiş bir heyet ya da onay kutuya yazılamaz.
- İddia–kanıt grafiği, `RECOMPUTED` durumu ve ikinci durum makinesi v1'e alınmaz.

Örnek kutu (heyet hiç çalışmadıysa):

> Sonuç: 8000 ft = 12192/5 m = 2438,4 m
> Durum: MATEMATİKSEL SERTİFİKA DOĞRULANDI
> Doğrulanan işlem: Uluslararası foot tanımıyla (1 ft = tam 0,3048 m) verilen değerin metreye çevrilmesi. Denetleyici
> bu eşitliği kabul etti; 2438,4 m yuvarlanmış değildir.
> Problem incelemesi: Tam hakemlik koşulları tamamlanmadı.
> Sınır: Bu kanıt, 8000 ft değerinin kaynaktan doğru alındığını, asıl sorunun doğru yorumlandığını veya gerçek bir
> yüksekliğin doğru ölçüldüğünü göstermez.

#### Soru 1'de tasarımcı kararları (sahip onaylamadı)

1. Türkçe ad dosyada iki biçimde geçiyordu; sonraki metin alındı: **MATEMATİKSEL SERTİFİKA DOĞRULANDI**, kod adı
   `CERTIFIED`.
2. Kullanıcının tanım onayı her olumlu etiket için zorunlu kalır (tasarım §1.1). `CERTIFIED`'da eksik olabilen şey
   heyet düzeyi ya da onayın doğrudan kanaldan gelmesidir.
3. `CERTIFIED` ile `CROSS_VALIDATED` sınırı "denetim kesin mi" ölçütüdür. Çözücüden ayrı bir denetleyici kesin iddiayı
   karara bağlıyorsa `CERTIFIED`; yalnızca tolerans içinde uyuşma varsa `CROSS_VALIDATED`.
4. Birim dönüşümünde denetleyici katsayıyı ayrı, kaynağı yazılı bir tanım tablosundan alır; alamıyorsa kutu ortak
   bağımlılığı yazar ve "bağımsız" demez.
5. Faz 1'de `CERTIFIED` üretecek bağımsız denetleyici yok; örnekteki kutu `v0.1.0`'da çıkamaz. Dar bir rasyonel
   denetleyicinin fazı soru 6'ya bırakıldı.
6. Tasarımda "en fazla / en az `CROSS_VALIDATED`" diyen 11 kural açık koşula çevrilecek.
7. Ajan aracılığıyla gelen onayda tasarımın bugünkü davranışı (düşük etiket + uyarı) korunur; rapor bunu "bekle ya da
   reddet"e sertleştirmeyi öneriyordu.
8. `CERTIFIED` çok farklı durumları tek ad altında toplar; farkı yalnızca "Problem incelemesi" satırı taşır.
9. Sertifikasız sonuçlarda heyetin niteliği etikette görünmez; yine yalnızca "Problem incelemesi" satırındadır.

#### Sıraya alınan açıklar (depoda doğrulandı)

| Açık | Kanıt | Nerede ele alınacak |
| --- | --- | --- |
| `rational` ve `decimal` alanları motorlara `real` olarak gidiyor | Plan satır 390 | Tasarım revizyonu; yeterlik ölçümünden önce |
| JSON'da tekrarlı anahtar ayrıştırıcıda reddedilmiyor | Plan satır 163 | Tasarım revizyonu |
| `unsat_core` sertifika türü sayılıyor | Plan satır 481 | Tasarım revizyonu |
| Onay, hesap ve rapor aynı problem sürümüne bağlanmıyor | Planda problem revizyonu alanı yok | Tasarım revizyonu |
| API anahtarı MCP form elicitation ile istenemez | MCP belirtimi | Soru 4 |
| Yanıt önbelleği ile istem önbelleği ayrı; yeni üretim kimliği yeni üretim kanıtı değil | OpenRouter belgeleri | Soru 5 |
| "İki ham yanıt bayt bayt aynıysa reddet" kuralı kısa cevaplarda fazla katı olabilir | Tasarım §8.2 | Soru 5 |

### Soru 2 (kapandı): Heyet üyelerinin yeterliği nasıl bilinir, kaç üye yeterlikli olmalı?

#### Sahip kararları (2026-11-10)

- Ücretsiz modellere güvensizliğin iki gerekçesi var: kota ve çözme kapasitesi.
- Rigor'un kendi yeterlik seti modelleri sınar; geçen model, sınandığı düşünme düzeyiyle birlikte kaydedilir.
- Güçlü model ücretsiz katmanda verilirse katkısı aynı sayılır. Çekince: bekleme uzayabilir.
- Depoda bir kayıt dosyası olur; Rigor modelin orada olup olmadığına bakar.
- Önce sahibin elindeki modellerle ilerlenir.
- Cevap olarak `docs/research/Deep Research/Soru2-1` dosyası ve `rigor_yeterlik_istatistik_hesaplari.csv` gösterildi.

#### Karar (gösterilen rapordan)

- **Üç zorunlu üyenin üçü de** ilgili görev kapsamı, erişim yolu ve çağrı ayarı için geçerli yeterlik kaydına sahip
  olmalı. En az iki farklı model ailesi bulunmalı. Heyet ayrıca birlikte ölçülmeli (100 yeni görev).
- **Ölçülen nesne model değil, yapılandırmadır:** model kimliği + erişim yolu + sağlayıcı + çağrı ayarları +
  formülasyon istemi + görev profili + dil. Ortak bir `low … max` ölçeği varsayılmaz; sağlayıcının kendi değeri
  kaydedilir. Kayıt başka yola, ayara ya da profile taşınmaz.
- **Başlangıç paketi:** 300 ölçüm örneği + 100 davranış/stres örneği (60 eşli/metamorfik, 40 kaynak dışı ya da gerçek
  problem). Önce 50 soruluk pilot. Ölçüm ve stres sonuçları ayrı raporlanır.
- **Geçme ölçütü:** doğrulanmış kritik hata sıfır; tam tanımlı problemlerde doğru formül oranının alt sınırı en az %80
  (210'da en az 178); eksik problemlerde doğru soru sorma oranının alt sınırı en az %90 (60'ta en az 59); destek dışı
  görevde sessiz destek iddiası yok.
- **Değerlendirici önce kendisi sınanır.** Model ölçümünden önce referans formüller, üretici ve denklik denetleyicisi
  için kabul paketi geçmiş olmalı.
- **Kayıt:** kanıt paketi ve ondan türetilen karar ayrı tutulur. İki katman: bakımcının dağıttığı kayıtlar ve
  kullanıcının yerel ölçümü; rapor hangisinden geldiğini yazar. İmza tek başına yetmez; kapsam, süre, iptal ve çalışma
  anı eşleşmesi de denetlenir.
- **Süre:** 30 gün, idari yeniden ölçüm takvimi olarak. Bilinen model, yol ya da ayar değişikliğinde kayıt hemen
  düşer.
- **Kayıtsız üye** danışman olarak çalışabilir; zorunlu üye sayılmaz. İtirazı yine incelenir. Ayrışma oy çokluğuyla
  kapatılmaz.
- **Başlangıç kapsamı:** yalnızca gerçekten kullanılacak üç yapılandırma ve tek dar görev profili.
- **Faz:** kayıt şeması F1; ölçüm altyapısı F3 öncesi; gerçek yeterlik ve heyet kapısı F3.

#### Karar 5'in yeni metni

Sahibin iki cevabı ("güçlü ücretsiz modelin katkısı aynı", "yeterlik ölçülecek") ve gösterdiği raporun önerisi:

> `KANITLANDI` için gerekli bütün üyelerin görev kapsamına uygun, geçerli yeterlik kaydı bulunmalıdır. Erişimin ücretli
> veya ücretsiz olması tek başına yeterliği artırmaz veya azaltmaz. Kota ve erişilebilirlik ayrıca raporlanır.

Sonucu: tamamen ücretsiz ama yeterlikli bir heyet `KANITLANDI`'ya ulaşabilir. Rapor bu değişikliğin sahipçe açıkça
onaylanmasını istiyor. Burada geçerli sayıldı; sahip itiraz ederse eski metin geri gelir.

#### Red Team: bu cevapta kalan sorunlar

1. **Sıfır tolerans, iyi modelleri de sık sık düşürür.** Gerçek kritik hata oranı %0,1 olan bir yapılandırma 300
   soruluk sıfır hata şartını %74 olasılıkla geçer. Üç üyenin aynı ay hepsinin geçme olasılığı %41, tek üyenin art
   arda 12 ay geçme olasılığı %2,7. `KANITLANDI`, ölçülebilenden on kat iyi modellerle bile ayların çoğunda
   kullanılamaz.
   *Tasarımcı önerisi:* önceden ilan edilmiş iki aşamalı plan. Sıfır hata: geçer. Tam bir hata: yeni 300 soru, sıfır
   hata şart. Bu planda %0,1'lik model %91, %1'lik model %5,6 olasılıkla geçer. "Geçene kadar yeniden dene" yasağı
   bozulmaz, çünkü kural sonuç görülmeden önce sabittir.
2. **"%1" başlığı en kritik davranış için geçerli değil.** Sıfır hatanın %1 üst sınırı 300 sorunun bütünü içindir.
   Eksik parametreyi sessizce doldurma (K4, A2, A6) yalnızca 60 eksik problemde ölçülür; oradaki üst sınır %4,9.
   Destek dışı 30 görevde %9,5. *Tasarımcı önerisi:* sınırlar tabaka başına raporlanır; eksik problem payı artırılır.
3. **Hedef kullanıcı için maliyet yüksek.** Bakımcının kayıtları kendi erişim yolu içindir ve başka yola taşınmaz;
   yabancı o yola sahip değildir (karar 1). Kendi ölçmesi gerekir: üye başına 400 çağrı. Araştırma notları §13'teki
   ücretsiz katman sınırıyla (model başına günde 200.000 token, ikincil kaynak) ve çağrı başına 3.000 token
   varsayımıyla bu, her 30 günde o modelin yaklaşık 6 günlük kotasıdır.
   *Tasarımcı önerisi:* dağıtılan kayıtlar önce yabancının kullanacağı ücretsiz yollar için üretilir; sahibin ücretli
   modelleri sahibin kendi kullanımı içindir.
4. **30 gün, sürüm takvimine bağlanır.** 30 günden eski bir Rigor sürümüyle gelen bütün kayıtların süresi dolmuştur.
   Kayıtların sürümden bağımsız güncellenmesi gerekir; bu da ağ bağımlılığı ve bakımcıya aylık ölçüm yükü getirir.
   *Tasarımcı önerisi:* sürümü sabitlenebilen modellerde (tarihli kimlik, açık ağırlık) süre uzatılır; açık nokta.
5. **`KANITLANDI` başlangıçta tek profilde açılır.** Kayıt profile bağlı olduğu için, ilk ölçülen dar profil dışındaki
   her problem türünde (roket model bağlama dahil) en üst etiket kapalı kalır. Hangi profilin önce ölçüleceği
   K8/K16'yı etkiler; açık nokta.
6. **Ölçüm Rigor'un kendi denklik denetleyicisine dayanır.** O denetleyici F3'te geliyor ve bilinen açıklar
   (`rational → real`) önce kapatılmalı; yoksa bütün modeller yanlış değerlendiriciyi tutarlı biçimde geçebilir.
7. **Üç kaydın iki kayıttan güvenli olduğu ölçülmedi.** Rapor da bunu söylüyor: gerekçe süreç tamlığıdır. Üçüncü üye
   doğru sonuçları gereksiz reddedebilir; aynı görevlerde iki ve üç üyeli kabul karşılaştırılmalı.

#### Raporun düzelttiği tasarımcı iddiaları (kabul edildi)

- "Depoda sızacak cevap anahtarı olmaz" fazla güçlüydü: açık şablon ve referans formül cevap üretme kuralını açığa
  çıkarır.
- "Açık ve gizli paydaki fark ezberin göstergesidir" tek başına yetmez: gizli pay daha zor ya da farklı alanlı olabilir.
- "Satırı komut yazar" tek başına güven sağlamaz: köken, yeniden puanlanabilir paket ve yetki sınırı da gerekir.
- GSM-Symbolic'teki "%65'ten fazla düşüş" belirli modeller içindir; genellenemez.
- Gizli set de sonuçlarına bakılarak tekrar kullanıldıkça geliştirme verisine dönüşür; kabul setleri yenilenmeli ve
  bütün denemeler kaydedilmeli.
- Metamorfik tutarlılık doğruluk değildir: `f(x) = 0,3x` doğrusallık testlerini geçer ama foot dönüşümü için yanlıştır.
  Mutlak referans örnekleri de gerekir.

#### Hesap denetimi

`rigor_yeterlik_istatistik_hesaplari.csv` dosyasındaki 34 satırın tamamı yalnızca standart kütüphaneyle yeniden
hesaplandı (Clopper–Pearson, ikiye bölme). Uyuşmayan satır yok; en büyük fark 2·10⁻¹⁶. Yukarıdaki ek rakamlar (%41,
%2,7, %91, %5,6, %4,9, %9,5) aynı betikle üretildi.

#### Kaynak denetimi

| Kaynak | Sonuç |
| --- | --- |
| ConStat (arXiv 2405.16281) | Var; yeniden ifade, aynı dağılım ve başka benchmark ayrımı özetle doğrulandı. |
| Dwork vd. (arXiv 1506.02629) | Var; "holdout'un uyarlamalı yeniden kullanımı aşırı uyuma yol açar" doğrulandı. |
| Snell vd. (arXiv 2408.03314) | Var; etkinin problem zorluğuna bağlı olduğu doğrulandı. "Daha fazla hesaplama zarar verebilir" özetten doğrulanamadı. |
| Howard vd. (arXiv 1810.08240) | Var; "her zaman geçerli" doğrulandı. Sabit örneklemle karşılaştırma özetten doğrulanamadı. |
| EquivaMap (arXiv 2502.14760) | Var; ölçüt karar değişkenleri arasında eşleme varlığı. |
| CheckList (ACL 2020) | Var; üç test türü makalenin kendisinden doğrulandı. |
| WILDS (ICML 2021) | Var; dağılım dışı başarının düştüğü doğrulandı. |
| TUF belirtimi | Var; geri alma, dondurma ve karıştırma saldırıları doğrulandı. |
| GitHub artifact attestations | Var; "güvenli olduğunun garantisi değildir" doğrulandı. |
| NIST el kitabı 6.2.3.2 | Var; AQL, LTPD, üretici ve tüketici riski doğrulandı. |
| NASA NTRS 19870018000 | Kayıt var: "Detection of faults and software reliability analysis" (J. C. Knight, 1987). PDF okunmadı. |
| Berger–Hsu 1996 (Statistical Science) | **Erişilemedi** (sayfa boş döndü). |
| Chen vd. 2018 (ACM Computing Surveys) | **Erişilemedi** (403). |
| Knight–Leveson 1986 (IEEE TSE) | **Erişilemedi** (içerik dönmedi). |
| Springer `10.1007/s44564-026-00040-z` | **Erişilemedi** (oturum istiyor). |

Önceki turlarda doğrulananlar: Kim vd. 2506.07962; Buçinca vd. 2102.09692; Lin–Hooi 2509.14034; Batra vd. 2610.35930;
GSM-Symbolic 2410.05229; LiveBench 2406.19314; MCP elicitation; OpenRouter yanıt önbelleği.

### Soru 3 (sürüyor): Hiç anahtarı ve aboneliği olmayan biri ilk çalıştırmada ne görmeli?

#### Sahip kararı (2026-11-10)

Yabancı Rigor'u kendi reposuna ya da ajanına verir; düz bir belge ya da problem verip "çöz" der. Rigor çözer ve
çıktısını verir.

Tasarımcı okuması: ilk çalıştırmanın birincil yolu bir kodlama ajanı üzerindendir (MCP). Girdi düz metin ya da
belgedir. Bu kullanıcının tek LLM'i, Rigor'u çağıran ajandır. Hiç LLM'i olmayan Python kullanıcısı ikincil durumdur.

#### Red Team

- **"Ver, çözsün" tek adım bekler; Rigor'un iki zorunlu durağı var.** Eksik değerde soru sorar (K4) ve çözmeden önce
  tanımı onaylatır (tasarım §1.1). İlk deneyim "soru, onay, sonra sonuç" olur.
- **Bu yolda formülü çağıran ajan yazar** (K6). Tek aile, yeterlik kaydı yok; en üst etiket kapalıdır. Sertifika
  varsa `CERTIFIED`, yoksa `CROSS_VALIDATED` ya da ret. İlk çıktının bunu ve nasıl yükseltileceğini söylemesi gerekir.
- **"Çöz" talimatı ajanı eksik değeri kendisi doldurmaya iter** (A6). Ajan hem formülü yazan hem kullanıcının cevabını
  ileten taraftır. Savunma istemcinin formu ya da bant dışı onaydır; ikisi de yoksa girdi "ajan iletti, doğrulanmadı"
  diye işaretlenir.
- **Rigor belge okumaz.** Yalnızca veri okuyucuları var (`.eng`, xlsx, CSV, `.ork`). Belgeyi ajan okur ve metni
  aktarır; kaynak aralıkları ajanın aktardığı metne göredir. Ajanın yanlış aktarması Rigor'un göremeyeceği bir hata
  kaynağıdır. Bir belgede birden çok problem varsa hangisinin çözüleceğini kimin seçeceği tanımsızdır.
- **"Repoya vermek" kod denetimi beklentisi doğurabilir.** Kod denetimi kapsam dışıdır (K13, K20). Yabancı
  "repomdaki hesapları kontrol et" derse Rigor yalnızca formülleri ve sayıları denetler.
- **İstemciler aynı değil.** Doğrudan onay formu her istemcide çalışmıyor (tasarım §7.2). Aynı ilk çalıştırma
  istemciye göre farklı etiketle bitebilir.
- Faz 1'de bağımsız denetleyici olmadığı için bu kullanıcının ilk sonucu `CERTIFIED` olamaz (soru 1, madde 5).

#### Açık nokta

Onay durağında yabancının ne yapmasının beklendiği sahibe soruldu.

### Yerel ortam

Sahibin makinesindeki istemci, model ve hesap ayrıntıları `docs/private/` altına taşındı. Tasarım için genel sonuçlar:

- Düşünme düzeyi sözlüğü istemciden istemciye değişiyor; birinde düzey bayrağı hiç yok.
- Kurulu erişim, tasarım K14/K15'in varsaydığı "üç abonelik, üç resmî istemci" tablosuyla birebir örtüşmüyor.

## Hedefler ve hedef olmayanlar

- **Kapsamdaki hedefler:** K14, K15, §4.1, §6.4, §8.2 ve §9'un kararlara göre revizyonu; `CERTIFIED` etiketi ve kutu
  biçimi; yeterlik kaydı ve ölçüm sözleşmesi; hiç erişimi olmayan kullanıcının ilk çalıştırması; anahtarların ne zaman
  isteneceği; toplayıcıların en üst etikete katkı koşulu; heyetin fazı.
- **Kapsam dışı:** kod yazmak, bağımlılık kurmak; Türkçe kutunun kullanıcılarla sınanması; DeepSeek Harness'e özel
  bir entegrasyon; iddia–kanıt grafiği; tam TUF dağıtımı; otomatik risk sınıflayıcı; genel "confidence sequence"
  altyapısı.

## Tartılan alternatifler

- **Mevcut `CROSS_VALIDATED` içinde ek şart satırı.** Sahibin benimsediği raporda elendi: etiket yapılmamış bir
  çapraz doğrulamayı söyler.
- **`PROVEN`'ı yalnızca matematik iddiasına indirmek.** İlk iki raporun önerisi; üçüncü rapor karar 5 nedeniyle geri
  çekti.
- **Tam iddia–kanıt grafiği, `RECOMPUTED`, ayrı yayın durumu.** Üçüncü rapor v1 için ağır bulup düz kayda indirdi.
- **Ölçüt olarak fiyat ("çağrı ücretli plandan yapılmalı").** Sahibin "katkıyı aynı sayarım" cevabıyla elendi: aynı
  model iki planda aynı cevabı verir; zayıf ama ücretli model en üst etiketi açardı.
- **Tarihli "üst düzey modeller" listesi.** Sahibin "yeterlik ölçülsün" kararıyla elendi: eskir ve Rigor'un ölçmediği
  bir şeye dayanır.
- **Bir ya da iki yeterlikli üye.** Sahibin benimsediği raporda elendi: zorunlu üyelerden biri ölçülmemiş kalır. İki
  kayıtlı heyet ayrı, düşük maliyetli bir yol olarak çalışabilir; en üst etiketi vermez.
- **Göreve göre değişen üye sayısı.** Raporda ertelendi: risk sınıflayıcı güven tabanını büyütür.

## Kararlar ve sonraki adımlar

- Sahip kararları yukarıda; bağlayıcı.
- **Sahibin açık onayını bekleyenler:**
  - Soru 1'deki dokuz tasarımcı kararı.
  - Karar 5'in yeterlik temelli yeni metni.
  - Paket büyüklüğü (300 + 100), geçici %80/%90 hedefleri, sıfır kritik hata, 30 gün, bakımcı ve yerel kayıt için
    varsayılan güven politikası (raporun kendi listesi).
  - Soru 2'deki dört tasarımcı önerisi: iki aşamalı kabul planı; tabaka başına sınır ve daha büyük eksik problem payı;
    dağıtılan kayıtların önce ücretsiz yollar için üretilmesi; sabitlenebilen modellerde daha uzun süre.
- **Açık noktalar:** ilk ölçülecek görev profili; kayıtların sürümden bağımsız güncellenme yolu.
- **Soru 3:** sürüyor. Sahip ilk çalıştırma yolunu söyledi (ajana düz belge ya da problem verip "çöz" demek). Onay
  durağındaki davranış açık. **Sorular 4–6:** sırada.

## Kaynaklar

- [ConStat (arXiv 2405.16281)](https://arxiv.org/abs/2405.16281)
- [Generalization in Adaptive Data Analysis and Holdout Reuse (arXiv 1506.02629)](https://arxiv.org/abs/1506.02629)
- [Scaling LLM Test-Time Compute (arXiv 2408.03314)](https://arxiv.org/abs/2408.03314)
- [Time-uniform confidence sequences (arXiv 1810.08240)](https://arxiv.org/abs/1810.08240)
- [EquivaMap (arXiv 2502.14760)](https://arxiv.org/abs/2502.14760)
- [CheckList (ACL 2020)](https://aclanthology.org/2020.acl-main.442/)
- [WILDS (ICML 2021)](https://proceedings.mlr.press/v139/koh21a.html)
- [The Update Framework belirtimi](https://theupdateframework.github.io/specification/latest/)
- [GitHub: artifact attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations)
- [NIST el kitabı 6.2.3.2](https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc232.htm)
- [NASA NTRS 19870018000](https://ntrs.nasa.gov/citations/19870018000)
- [GSM-Symbolic (arXiv 2410.05229)](https://arxiv.org/abs/2410.05229)
- [LiveBench (arXiv 2406.19314)](https://arxiv.org/abs/2406.19314v2)
- [Who Convinced Whom? (arXiv 2610.35930)](https://arxiv.org/abs/2610.35930)
- [MCP elicitation belirtimi, 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)
- [OpenRouter: response caching](https://openrouter.ai/docs/guides/features/response-caching.md)
- [Correlated Errors in Large Language Models (arXiv 2506.07962)](https://arxiv.org/abs/2506.07962v1)
- [To Trust or to Think (arXiv 2102.09692)](https://arxiv.org/abs/2102.09692v1)
- [Enhancing Multi-Agent Debate System Performance via Confidence Expression (arXiv 2509.14034)](https://arxiv.org/abs/2509.14034)
