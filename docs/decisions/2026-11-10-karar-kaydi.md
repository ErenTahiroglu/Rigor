# Rigor — hakem heyeti ve model erişimi

- **Yazar:** Eren Tahiroğlu
- **Tarih:** 2026-11-10
- **Durum:** Taslak. Altı sorunun hepsine sahip cevap verdi; soru 5 sahibin isteğiyle araştırılıp açık bırakıldı.
  2026-11-10'da yedi taze gözlü inceleme ajanı (EGM) depoyu ve bütün kararları taradı ("Tam tarama"). 2026-11-11'de
  sahibin eklediği iki dış tarama raporu denetlendi ("İkinci dış tarama"); bu bölüm ilk taramanın bazı maddelerini
  düzeltiyor ve çakışmada önceliklidir. Bütün kararların tek listesi "Kayıt" bölümünde. 2026-11-11'de sahip on üç
  öneriyi onayladı (S-20 … S-32); kararlar yeni mimari belgesine
  ([`../design/2026-11-11-rigor-mimari.md`](../design/2026-11-11-rigor-mimari.md)) ve faz planına
  ([`../plans/2026-11-11-rigor-faz-plani.md`](../plans/2026-11-11-rigor-faz-plani.md)) işlendi. Bu belge karar geçmişi
  olarak kalır.

## Genel bakış

Rigor, bir yapay zekâya yaptırılan matematiğin doğruluğunu denetleyen bir araç. Henüz kod yok; tasarım belgesi
(`docs/design/2026-11-07-rigor-design.md`), yol haritası ve Faz 1 planı var.

Bu belge, sahibin 2026-11-10'da verdiği altı kararın tasarımı nasıl değiştireceğini çalışır:

1. Hedef kullanıcı, aracı GitHub'da bulup kuran bir yabancıdır. Bu kişide Claude, ChatGPT, Gemini aboneliği olmayabilir.
2. İki adım vardır: önce matematik kütüphaneleriyle analiz, sonra ücretsiz ve ücretli API listesinden hakem heyeti.
3. Ücretli API'ler zorunlu değildir, ama kullanıcıda varsa istenir.
4. Toplu API toplayıcıları (OpenRouter türü) listeye girebilir.
5. Yalnızca ücretsiz modellerle doğrulanan sonuç `KANITLANDI` almaz; bir alt doğrulama seviyesi alır.
6. DeepSeek Harness işe yararsa kullanılır.

Bu altı kararın bugünkü durumu "Kayıt" bölümünde (S-1 … S-6). 2, 3 ve 5 sonraki sahip kararlarıyla değişti ya da
daraldı; 6 bu belgede hiç incelenmedi.

### Terimler

- **K1–K26, A1–A6, §:** tasarım belgesindeki karar, anti-hedef ve bölüm numaraları. Bu belgede en çok geçenler:
  K4 (eksik değerde sor, varsayma), K6 (formülü Rigor'un kendi LLM erişimi ya da çağıran ajan yazar), K14/K15 (LLM
  erişimi ve abonelikler), A1 (yanlış sonuç en üst etiketle dönmez), A2 (söylenmemiş varsayım yok), A3 (LLM çıktısı kod
  olarak çalıştırılmaz), A6 (ajan kullanıcının cevabını kendisi uyduramaz).
- **Plan G1–G11:** Faz 1 planının altın testleri (plan satır 766–776). Tasarımdaki G1–G7 hedefleriyle karışmasın diye
  "plan G3" diye yazılır.
- **Heyet:** bir problemi birbirini görmeden ayrı ayrı formüle eden üç model; tasarım §6.4'teki Red Team formülatörleri.
  Tasarım §6.9.1'deki "hakem paneli" ayrı bir şeydir.
- **Zorunlu üye / danışman üye:** en üst etiket için sayılan, geçerli yeterlik kaydı olan üye / kaydı olmayan, itirazı
  incelenen ama sayılmayan üye.
- **Yeterlik kaydı:** bir yapılandırmanın (model, erişim yolu, ayar, istem, görev profili, dil) belirli bir tarihte
  Rigor'un yeterlik setini geçtiğinin kaydı. **Heyet kabulü:** üç üyenin birlikte, yeni 100 görevde ölçülmesi.
  **Görev profili:** yeterliğin geçerli olduğu dar problem türü.
- **Erişim yolu / girdi yolu / onay kanalı:** sırasıyla modele nasıl ulaşıldığı (istemci, API, toplayıcı); girdinin
  türü (doğrudan ifade ya da metin); kullanıcının cevabının nereden geldiği (istemci formu, işletim sistemi penceresi,
  ajan). **Doğrudan yol** girdinin katı ayrıştırıcıdan bütünüyle geçmesidir; **yankı** o yolda çözülen ifadenin
  kanonik halinin sonuçla birlikte gösterilmesidir.
- **Bakımcı:** Rigor'u yayımlayan kişi; bugün sahip. **Sentinel testi:** modelin sessizce değişip değişmediğini
  yoklayan küçük test.

## Analiz

### Tam tarama (2026-11-10): çakışmalar, yanlışlar, eksikler, öneriler

Yöntem: EGM'nin yedi inceleme ajanı birbirini görmeden, sohbet geçmişi olmadan çalıştı. Okudukları: bu belge, tasarım
belgesi (986 satır), yol haritası, Faz 1 planı (780 satır), araştırma notları, Handoff ve README. Bulgular
birleştirildi, tekrarlar atıldı. Birincil kaynak denetimi ayrıca yapıldı (aşağıda B-5).

| İnceleme | Durum |
| --- | --- |
| Mimari eleştiri | tamamlandı |
| Teknik doğruluk | tamamlandı |
| Kapsam ve sadelik | tamamlandı |
| Anlaşılırlık (bağlamı bilmeyen okur) | tamamlandı |
| Uygulamaya hazırlık | tamamlandı |
| Belge yapısı | tamamlandı |
| Çelişki çözümü | tamamlandı |

Önem dereceleri: **B** = engelleyici (çözülmeden tasarım revize edilemez ya da kod yazılamaz), **M** = büyük,
**m** = küçük. "Öneri" yazan her şey tasarımcı önerisidir; sahip onaylamadı.

**2026-11-11 notu:** B-2, B-3, B-4, B-5, B-6, M-4, M-11, M-12, M-14, M-15, M-19, M-21, Ö-2-2 ve "en küçük v1" ikinci
dış taramada düzeltildi ya da daraltıldı. Düzeltilmiş halleri "İkinci dış tarama" bölümündeki tabloda; çakışmada o
tablo geçerlidir.

#### Engelleyiciler

**B-1. Onay kuralı kendi içinde çelişiyor; "bilmiyorum" ajana bir kaçış kapısı açıyor.** (5 inceleme)

- Soru 1 tasarımcı kararı 2: tanım onayı her olumlu etiket için zorunlu. Sahibin "bilmiyorum" kararı: onaysız çözüp
  `CERTIFIED` ya da `CROSS_VALIDATED` ver. Doğrudan yol önerisi: onay yok, yankı var. Tasarım §4.1 satır 197
  `CROSS_VALIDATED` için "formal tanım onaylandı" istiyor; plan satır 465'teki test onaysız sonucu reddediyor.
- Metinsel yolda tek bir modelin okuması, hiçbir insan bakmadan şartname olur. Bu, Rigor'un yakalamak için var olduğu
  formülasyon hatasıdır.
- Ajan "bilmiyorum"u kendisi seçebilir: onay durağını atlar ve hiçbir etiket kaybetmez, çünkü ajan aracılığıyla gelen
  "doğru" zaten `CROSS_VALIDATED` ile sınırlı.
- "Bilmiyorum" tek seçenek olarak iki farklı şeyi örtüyor: yorumun onayı ve eksik değer. İkincisi K4 gereği hiçbir
  zaman devredilemez (Handoff satır 41).
- **Öneri:** onay bir boole değil, bir durum olsun: `CONFIRMED`, `CORRECTED`, `DELEGATED` ("bilmiyorum"),
  `REJECTED`, `ECHO_ONLY` (doğrudan yol). Her durumun izin verdiği etiketler tek tabloda yazılsın. `DELEGATED` yalnızca
  doğrudan kanaldan kabul edilsin; ajandan gelirse onaysız sayılsın. `DELEGATED` eksik değer sorularını kapatmasın.
  `DELEGATED` altında `CERTIFIED` yalnızca "çıkarılan denklem"i kapsasın ve kutu bunu yazsın. Bu, §1.1 ve K4'ün açık
  bir sahip kararıyla değiştirilmesi demektir.

**B-2. Dört etiketin karar sırası tanımsız; heyetin ayrıştığı sonuç `CERTIFIED` alabilir.** (5 inceleme)

- "Tam heyet koşulları sağlanmamış olabilir" ifadesi iki durumu birden kapsıyor: heyet hiç çalışmadı ve heyet çalıştı
  ama ayrıştı. Ayrışma, formülasyon hatasının doğrudan kanıtıdır. İkincisini "sağlanmadı" okumak, yanlış olabilecek bir
  soruya `CERTIFIED` verir.
- "Etiketler merdiven değil" kuralı, A1'in "şüphede etiket düşürülür" kuralıyla, alan paketi tavanlarıyla ve Sentinax
  kapısıyla ("en az `CROSS_VALIDATED`") çelişiyor; bunların hiçbiri bir sıra olmadan değerlendirilemez.
- **Öneri:** `decide_label` için yukarıdan aşağıya tek bir tablo:
  1. Herhangi bir ret nedeni (heyet çalıştı ve ayrıştı, yollar uyuşmadı, sertifika reddedildi) → `REFUSED`.
  2. Bütün `PROVEN` koşulları → `PROVEN`.
  3. Bağımsız denetleyicinin kabul ettiği sertifika → `CERTIFIED`.
  4. Gerçekten ayrı iki yol uyuştu ve sınır testleri geçti → `CROSS_VALIDATED`.
  5. Hiçbiri → `REFUSED`.
  Tavanlar ve düşürmeler için kullanıcıya gösterilmeyen bir iç sıra tanımlansın. Sentinax kapısı bir küme olarak
  yazılsın (`{PROVEN, CERTIFIED, CROSS_VALIDATED}`).

**B-3. "Bağımsız denetleyici" tanımsız; bugünkü sertifikalar çözücüyle aynı güven tabanına dayanıyor.** (4 inceleme)

- İki inceleme ters sonuca vardı, bu da tanımın eksik olduğunu gösteriyor:
  - Teknik doğruluk: Soru 1 karar 3'ün harfiyle Faz 1'de böyle denetimler zaten var (Z3 teklik, Z3 özdeşlik, Z3+SymPy
    "her x için"); plan G2, G3, G7, G8, G9 `CERTIFIED` olurdu.
  - Mimari: çözücü de denetleyici de aynı `compile/` derleyicisinden geçiyor (plan satır 390); derleyicideki bir hata
    ikisinde ortak. Z3'ün `unsat` cevabı denetlenmiş bir ispat değil, çözücünün hükmüdür.
- Tasarım §3.4 matrisinde mantık ve eşitsizlik satırları `unsat` hükmüne dayanarak `PROVEN` diyor (satır 167, 175–177).
- Ara durum tanımsız: SymPy ile kesin geri koyma yapılmış ama denetleyici bağımsız değilse sonuç hiçbir etikete
  uymuyor (`CROSS_VALIDATED` "formal kanıt yok" der, bu da yanlış olur).
- Yanlış `CERTIFIED` hiçbir yerde ölçülmüyor; A1 ve çıkış ölçütleri yalnızca yanlış `PROVEN`'ı sayıyor.
- **Öneri:** `core/certify/kernel` adlı küçük bir denetleyici: yalnızca `fractions` ve `decimal` kullanır;
  `compile/`, SymPy, Z3 ve pint'i içe aktaramaz (Faz 1'deki mimari testle zorlanır); kendi kaynaklı birim tablosu
  vardır; yalnızca rasyonel ve `Decimal` aritmetiğini kapsar. Z3 `unsat` ve "her x için" hükümleri "çözücü hükmü"
  sayılsın: en çok `CROSS_VALIDATED` (denetlenebilir ispat nesnesi yoksa). Ara durum için açık kural: `CROSS_VALIDATED`,
  "Doğrulanan işlem" satırı ortak denetleyiciyi adıyla yazar. A1 ve bütün çıkış ölçütleri "yanlış `PROVEN` = 0 ve
  yanlış `CERTIFIED` = 0" olsun. Tahmini iş: testlerle yaklaşık bir hafta.

**B-4. Çağıran ajana karşı tehdit modeli yok; ajan izni, onayı ve yeterliği taklit edebilir.** (3 inceleme)

- Kabuk erişimi olan bir ajan şunları yapabilir:
  - `rigor` ayar komutunu kendisi çalıştırıp bütçeyi ya da süreyi yükseltmek ("yalnızca Rigor'un kendi komutuyla"
    kuralı bunu engellemez);
  - depodaki yeterlik dosyasını düzenlemek ya da yerel bir "geçti" kaydı yazmak;
  - oturum dosyasındaki `VIA_AGENT_UNVERIFIED` olayını `USER_DIRECT` yapıp anahtarsız SHA-256'yı yeniden hesaplamak
    (plan satır 630); rapor ve yeniden üretim doğrudan onay gösterir. Plandaki kurcalama testi sahte güven verir;
  - MCP sunucusunun ortam değişkenlerini proje dosyasıyla (`.mcp.json`) değiştirmek.
- Kontrolün tersine çevrilmesi riski büyütüyor: izin artık kullanıcının hesabından harcamaya ve veriyi sağlayıcılara
  göndermeye yetki veriyor.
- **Öneri:** yazılı bir tehdit modeli: dürüst ama özensiz ajan; yalnızca araç argümanlarıyla yalan söyleyen ajan;
  kabuk erişimli ajan. Her düzeyde hangi etiketin ayakta kaldığı yazılsın. Yetkiyi genişleten her işlem (bütçe, süre,
  katılığı kapatma, yerel yeterlik kaydını kabul) yeni bir rastgele değerle (nonce) bant dışı pencereden onaylansın ve
  kanalı kaydedilsin. Oturum ve izin kayıtları proje dizini dışında (işletim sistemi anahtar zinciri) tutulan bir
  sırla imzalansın; bunun çıtayı yükselttiği ama kanıt olmadığı yazılsın. Yerel yeterlik kaydı, Rigor'un kendi
  çalıştırıcısının doğrudan izinli bir oturumda ürettiği kayıt değilse `PROVEN`'ı açamasın. Ayarlar proje dizini
  dışında dursun; bütçe ve süre ortam değişkeninden okunmasın.

**B-5. Sağlayıcı koşulları, "Rigor kullanıcının kurulu istemcisini çağırır" kararıyla çelişebilir.** (birincil kaynak)

- Anthropic'in hukuki sayfası: üçüncü taraf geliştiricilerin kendi uygulamalarında Claude.ai girişi sunmasına ve
  "kullanıcıları adına Free, Pro, Max ya da Ultra plan kimlik bilgileriyle istek yönlendirmesine" izin verilmiyor. Ürün
  geliştirenler, Agent SDK kullananlar dahil, API anahtarı kullanmalı. Son kullanıcının değiştirilmemiş Claude Code'a
  kendi aboneliğiyle girmesi engellenmiyor. Rigor'un yaptığı ikisinin arasında; bu belirsizlik kullanıcının hesabını
  riske atar.
- Claude Code'un yalın başsız modu (`--bare`) abonelik girişini hiç okumuyor; API anahtarı istiyor.
- Codex belgesi, ChatGPT oturumuyla otomasyon için "herkese açık ya da açık kaynak depolarda kullanmayın" diyor.
- Tasarım §8.2 ve araştırma notları §11 aynı yasağı aracı katmanlar için zaten kaydetmişti.
- Sonuç: sahibin "önce kurulu istemci, API anahtarı en son" sırası bugünkü haliyle sağlayıcı koşullarına dayanmıyor.
- **Öneri:** sağlayıcı başına koşullar birincil metinden okunup onaylanana kadar varsayılan yol 3. yol olsun (çağıran
  ajanın yazdığı formül, "ajan yazdı" diye işaretli). Başsız istemci sürme her sağlayıcı için ayrı bir açma bayrağıyla
  gelsin; bir sağlayıcının yasağı tasarımı bütünüyle düşürmesin. Bu bir sahip kararıdır (Kayıt A-3).

**B-6. Kapsam süreye sığmıyor ve yol haritasının sırası sahibin erteleme kuralının tersi.** (kapsam incelemesi)

- Tahmin (tek geliştirici, kodlama ajanıyla tam zamanlı; yalnızca iş haftaları):

  | İş | Hafta |
  | --- | --- |
  | F1 çekirdek | 3–4 |
  | F2 roket | 3–5 |
  | F3 Red Team ve doğal dil | 4–6 |
  | F4 şablon ve hakem | 2–3 |
  | F5 Lean | 3–5 |
  | F6 alan araçları | 1–2 |
  | F7 finans | 3–5 |
  | F8 optimizasyon | 2–3 |
  | F9 sağlamlaştırma | 2 |
  | Bugün eklenenler (etiketler, denetleyici, ayrıştırıcı, `rigor solve`, izin ve bütçe, başsız adaptörler, yeterlik sistemi, heyet kabulü, belge okuyucu) | 10–17 |
  | **Toplam** | **33–52** |

  Eldeki süre 16 hafta. Yeterlik ölçümü ayrıca sıkıştırılamayan takvim süresi istiyor (ücretsiz kotada üye başına
  6–8 gün) ve F3'teki denklik denetleyicisinden sonra başlayabiliyor.
- Sahibin üç kullanımından ikisi (kripto botu, Sentinax) yalnızca F7'de. F7, sahibin hiçbir kullanımının ihtiyaç
  duymadığı Lean (F5) ve akışkanlar paketinden (F6) sonra geliyor. Takvim kayarsa yapılmayan şey sahibin en çok
  ihtiyaç duyduğu iş olur.
- K16 takvim yapılmasını yasaklıyor; bu yüzden kaymayı erken gösterecek bir işaret yok.
- **Öneri:** "her şey yetişir" beklentisi bu kapsamla tutmuyor. Aşağıdaki erteleme sırası şimdi benimsensin. K16'ya
  rağmen iki kontrol noktası konsun: 5. haftanın sonu (F1 ve `CERTIFIED`), 10. haftanın sonu (roket ve finans
  çekirdeği). Kaçırılan her noktada listedeki sıradaki iş bekletilsin.

**B-7. Hedef kullanıcı ile erteleme kuralı ters yönlere çekiyor.** (kapsam ve çelişki incelemeleri)

- Sahibin kullanımları denklemleri kendisi kurucu API ile yazıyor; ilk çalıştırma akışına, üç seçenekli ekrana, başsız
  istemci sürmeye, izin ve bütçeye, katı ayrıştırıcıya, belge okuyucuya, dağıtılan yeterlik kayıtlarına, toplayıcıya,
  birinci sınıf İngilizceye, Lean'e, akışkanlar paketine, optimizasyona ve öğrenen hakem paneline ihtiyaç duymuyor.
- Sahibin kuralı ("kendi kullanımımda en az ihtiyacım olan bekler") harfiyen uygulanırsa bugünkü revizyonun neredeyse
  tamamı ilk ertelenenler arasına girer. Revizyon yabancı için yapıldı; kural sahibi koruyor. İkisi birden önce gelemez.
- Sahibin kullanımlarının hiçbiri `KANITLANDI` gerektirmiyor (soru 6). Yeterlik sistemi, heyet ve heyet kabulünün tek
  çıktısı `PROVEN` hakkı. v1 `PROVEN` hiç vermezse "en üst etiketle yanlış sonuç dönmez" vaadi kendiliğinden tutar.
- **Bu bir sahip sorusudur** (Kayıt A-1).

**B-8. Faz 1 sözleşmeleri eski üç etiketli modeli donduracak.** (4 inceleme)

- Yol haritası `Conditions`, `Outcome` ve `Provenance`'ı "fazlar arası sözleşme" sayıyor; F1 bunları tanımlıyor.
  Plan bugünkü haliyle yazılırsa sonraki her faz sözleşmeyi genişletmek yerine kırmak zorunda kalır. Değişmesi
  gerekenler:
  - `Label` (plan satır 442): `CERTIFIED` yok.
  - `Conditions` (satır 444): `certificate: "formal" | "none"`; denetleyici kimliği, ortak bağımlılık, onay durumu,
    tanımı kimin yazdığı, problem sürümü, yeterlik kaydı alanı yok. Satır 460'taki test yeterlik olmadan `PROVEN`
    döndürüyor.
  - `Session.confirm` (satır 627) iki değerli; `ConfirmForm` (satır 746) boole; işletim sistemi penceresi iki düğmeli
    (satır 729); `zenity --question` yalnızca evet/hayır.
  - `Outcome.values` (satır 446) değişken başına tek metin; çözüm kümesi taşıyamaz.
  - `Certificate.kind` (satır 481) `unsat_core` içeriyor.
  - Sayı alanları (satır 390, 394) ve tekrarlı anahtar (sınır denetimi yok).
  - Problem sürümü: onaydan sonra IR değişiyor (satır 630). Bu alan `v0.1.0`'dan sonra eklenirse kanonik JSON ve IR
    özeti değişir, kayıtlı bütün oturumlar ve yeniden üretimler kırılır.
  - Rapor bölümleri (satır 701): dört alanlı kutu, tanımın yazarı, harcama satırı yok. A4 testi rapordaki her sayının
    kayıtta olmasını istiyor; harcama sayıları kayda yazılmazsa test kırılır.
- **Öneri:** kod yazılmadan önce yalnızca F1'in dokunduğu yerler revize edilsin (görev 2, 3, 8, 9, 10, 14, 15, 17,
  18, 19); tasarımın geri kalanı sonra işlensin. Problem sürümü IR'a değil oturum olaylarına eklensin; her onay olayı
  gösterilen IR'ın özetini taşısın; `onaylanan = çözülen = raporlanan` değişmezi test edilsin.

**B-9. "Çöz, çözüm kümesini döndür" bir tamlık kanıtı ister.** (3 inceleme)

- 2 ve 3'ü yerine koymak kök olduklarını kanıtlar, başka kök olmadığını kanıtlamaz. SymPy aşkın ya da parametrik
  denklemlerde eksik küme döndürebilir; eksik kümeyi "küme" diye vermek A1 sınıfı bir hatadır.
- Karmaşık köklerin atılması söylenmemiş bir alan varsayımıdır (A2): `x²+1=0` için "çözüm yok" yanlış olabilir.
- "Tek değer gerektiğinde sor" kararını metinsel yolda formülatör verir; bu da bir Tip-2 kararıdır.
- **Öneri:** alanı açıkça belirten bir çözüm kümesi hedefi (ℝ, ℂ, ℤ ya da bir aralık). Sertifika iki parçalı olsun:
  üyelik (kesin geri koyma) ve tamlık (ör. `denklemler ∧ x≠2 ∧ x≠3` için Z3 `unsat`, polinomlarda derece ve çarpanlara
  ayırma, ya da Arb ile kök yalıtımı). Tamlık gösterilemezse "bulunan kökler" ifadesiyle `CROSS_VALIDATED` ya da ret.
  Yankı alanı yazsın. Plan G3, görev 11 ve 14 buna göre değişir.

**B-10. Kararların tek bir listesi yok; durumlar birbirini tutmuyor.** (3 inceleme; bu turda düzeltildi)

- Sahip kararları sekiz ayrı yere dağılmıştı. Karar 2, 3 ve 6 sessizce değişmiş ya da daralmıştı. Karar 5'in durumu
  üç yerde üç farklı biçimde yazıyordu. Yazarın gösterdiği raporlar tasarımın okuma kuralında olmayan üçüncü bir kategori
  ("Karar, rapordan") olarak geçiyordu. LLM yollarının sırası yanlışlıkla sahibe atfedilmişti ve araştırma maddeleri yol
  numaralarını karıştırıyordu. Bunlar bu turda düzeltildi; yeni "Kayıt" bölümü tek liste.

#### Büyük bulgular

##### Mimari

- **M-1. Kontrolün tersine çevrilmesinin paket mimarisinde yeri yok.** İzin, bütçe, istemci bulma, formülatörleri
  çalıştırma ve yeterlik denetimi Session'a konursa çekirdek LLM ve MCP modüllerine bağımlı olur (K24 kuralı kırılır).
  *Öneri:* çekirdeğin dışında bir yürütme katmanı (`rigor.runner`, `rigor.consent`, `rigor.qualification`); çekirdek
  saf durum makinesi kalır ve tipli olgular alır. Yeterlik şeması (yalnızca veri modeli) çekirdekte, doğrulaması
  dışarıda. Mimari test bu modülleri çekirdeğe yasaklasın.
- **M-2. Tek kaba araç saatler süren, kota bekleyen bir işi tek MCP çağrısında tutamaz.** MCP istemcileri araç
  çağrılarını zaman aşımına uğratıyor; stdio sunucusu istemciyle birlikte ölüyor. Bu da beklemeyi kısaltma ve sessizce
  model değiştirme baskısı yaratır. *Öneri:* iş modeli: `rigor_solve` hemen bir iş kimliği döndürür;
  `rigor_status` ve `rigor_result` ilerlemeyi sorar; iş kendi ömrü ve kilit dosyası olan ayrı bir süreçte çalışır;
  izin ve onay o süreçten işletim sistemi kanalıyla istenir. 3. yol için ayrı bir `rigor_submit_formula` aracı.
  `rigor solve` için çıkış kodları ve JSON çıktı sözleşmesi.
- **M-3. Yeterlik anahtarı başsız istemcilere uymuyor.** Resmî istemciler haftada birkaç kez güncelleniyor ve gizli
  sistem istemlerini, varsayılan model takma adlarını değiştiriyor. Sürüm anahtardaysa `PROVEN` neredeyse hiç açılmaz;
  değilse ölçülen ile çağrılan sessizce ayrışır. Rigor'un kendi istemi de anahtardaysa her Rigor sürümü dağıtılan
  bütün kayıtları düşürür. *Öneri:* anahtar alanları tek yerde: istemci adı ve ikili dosya özeti, etkin sistem
  isteminin özeti, yanıtta dönen model kimliği (istemcinin beyanı olduğu yazılarak), düşünme ayarı, plan katmanı.
  Her alan için düşürme kuralı yazılsın. Rigor sabitlenmiş bir ikili yolu kendiliğinden güncelleme kapalı çağırsın.
- **M-4. Yeterlik ölçümünün fazı döngüsel.** Değerlendiricinin önce sınanması gerekiyor, ama değerlendirici (denklik
  denetleyicisi) F3'te. Ölçüm ayrıca formülatör adaptörleri, doğal dil ayrıştırma ve K4 soru protokolü istiyor;
  hepsi F3. "Kayıt şeması F1" için planda görev yok ve anahtar açık soru 5'e bağlı. *Öneri:* F3 ikiye bölünsün:
  F3a (tek formülasyonlu doğal dil yolu: adaptörler, izin, çıkarma, üç seçenekli onay) ve F3b (denklik denetleyicisi
  → değerlendirici kabulü → ölçüm → heyet).
- **M-5. Şablonlar kayıt süresini atlatıyor.** Tasarım §6.9 onaylı şablonda Red Team'i tekrarlamıyor ve etiketi
  koruyor; üyelerinin kaydı düşmüş bir şablon `PROVEN` vermeye devam eder. *Öneri:* şablon kullanımında kayıt
  geçerliliği yeniden denetlensin; öz-denetime bir adım olarak eklensin.

##### Onay ve kullanıcı

- **M-6. Onay ekranı denklem okuyamayana denklem gösteriyor.** Sade anlatım da IR'dan üretiliyor; onu onaylamak bir
  çeviriyi onaylamaktır. Matematik bilmeyen okur "en fazla" ile "küçüktür" farkını düz yazıda da kaçırır. *Öneri:*
  soruyu tersine çevir: formül değil sonuç göster. Adayların ayrıştığı ve mutasyonların sonucu değiştirdiği yerlerden
  deterministik "yoklama" soruları üret ("Bir müşteri tam 3 tane alabilir mi?", "Roket 1 kg ağırlaşırsa tepe irtifası
  artmalı mı azalmalı mı?"). Cevabı girdi metninden zaten belli olan bir yoklama ekle; yanlış cevap o oturumun onayını
  "karar vermedi"ye düşürsün. Ölçülmesi gereken: farklı matematik düzeyindeki kullanıcılarda, kasıtlı hatalı
  formülasyonların denklem, düz yazı ve yoklama ekranlarında yakalanma oranı.
- **M-7. Üç seçenekli ekranın veri biçimi ve kanal davranışı yok.** Saf "reddet" kayboluyor (`USER_REJECTED_SPEC`
  ulaşılamaz olur). "Yanlış"ın düzeltme içeriği (serbest metin mi, ifade mi, IR mi), kimin yeniden formüle edeceği ve
  kaç tur süreceği tanımsız. Toplu ekranda her kalemin kararı kendi IR özetine bağlanmıyor; tek tık N kalemi onaylıyor.
  Windows'ta ve ekransız Linux'ta işletim sistemi penceresi yok; VS Code eklentisi elicitation'ı reddedebiliyor. Bu
  ortamlarda her onay "ajan iletti"ye düşer. *Öneri:* `ConfirmDecision` ve `NEEDS_RECONFIRMATION` durumu; kalem başına
  `ir_sha256` ve sürüm; kanal matrisi (elicitation, pencere, ajan, hiçbiri × izin, onay, eksik değer, harcama); Windows
  ya desteklensin ya da README ve `rigor doctor`'da açıkça dışarıda bırakılsın; toplu ekran hiçbir zaman "hepsini kabul
  et" varsayılanıyla açılmasın.
- **M-8. İzin ve bütçenin durum makinesi ve birimi yok.** Tanımsız olanlar:
  - 15 dakikalık sayaç kullanıcı bir soruyu düşünürken (`NEEDS_INPUT`) işliyor mu?
  - İzin nerede saklanıyor ve kurcalamaya karşı nasıl korunuyor?
  - Kapsam anahtarı ne: çalışma dizini mi, git kökü mü?
  - İstemci güncellenince izin düşüyor mu, izin nasıl geri alınıyor?
  - "Devralma izni" ile "istemci kullanma izni" arasındaki fark ne?
  - "Bir çağrı" ne: yeniden denemeler, kota beklemeleri, anlatım denemeleri (en çok üç) sayılıyor mu?

  İzin ne zaman bitiyor sorusunda belge kendisiyle çelişiyor: "görev bitince" ve "iş bittikten 15 dakika sonra".
  Metinsel bir problem kabaca 8–15 çağrı (üç formülasyon, geri çeviri, anlatım denemeleri, ayrışma sonrası tekrarlar);
  200 işlemlik bir belge binlerce çağrı. *Öneri:* birim "bir LLM'e giden bir alt süreç ya da HTTP isteği, yeniden
  denemeler ve başarısızlıklar dahil". Aşama başına çağrı formülü yazılsın. Bütçe okunabildiği yerde token cinsinden de
  tutulsun. `NEEDS_CONSENT` durumu ve kaldığı yerden devam. Bütçenin tek çağrı bile aşılmadığını sınayan test.
  Ekranda yazacak tek cümle: "izin, son işin bitişinden sonraki 15 dakika içinde başlayan işleri bütçe bitene kadar
  kapsar".
- **M-9. İzin istemleri kullanıcıya "evet"e basmayı öğretiyor.** *Öneri:* süreye göre değil değişikliğe göre sor (yeni
  istemci, yeni dizin, veriyi alan yeni sağlayıcı, aşılan bütçe eşiği). Rigor'un ayar komutuyla ajan dışında bir kez
  kurulan, ajanın yükseltemeyeceği sert sınırlı bir politika. Risk arttığında düğme yerine yazılan ya da seçilen bir
  değer iste. Ölçülmesi gereken: 2 saniyenin altında kabul edilen istem oranı.

##### Girdi

- **M-10. Katı ayrıştırıcının dilbilgisi yok.** Yasak A3 değil, §6.2 satır 421–422 ve plan satır 17; ikisi değişmeli.
  Tanımsız: `^` ve `**`, Unicode `²` ve `−`, örtük çarpım (`5x`, `1/2x`), `-x^2` önceliği, ondalık virgül, birim, denklem
  sistemleri, hangi değişkenin çözüleceği. Ajanın aktardığı ifadeyi "kullanıcının yazdığı" diye göstermek yanlıştır.
  *Öneri:* yayımlanmış bir dilbilgisi; her belirsizlik soru ya da ret; ifade doğrudan kanaldan ya da kullanıcının
  verdiği dosyadan gelmediyse "ajan aktardı" diye işaretlensin. Kısa yol: Python'un standart `ast.parse(..., mode="eval")`
  çağrısı kod çalıştırmadan ayrıştırır; beyaz listeli bir ağaç yürüyücüsüyle IR'a çevrilir; `^` ve örtük çarpım
  reddedilir. Hypothesis ile "ayrıştır → yaz → ayrıştır" özdeşliği sınansın.
- **M-11. Belgedeki gizli talimat bütün heyeti aynı yöne çekebilir.** "Sınırı ≥ al" ya da "0,3 m/ft kullan" gibi bir
  cümle üç üyeye aynı anda ulaşır; ilişkili uyuşma oybirliği gibi görünür ve `PROVEN` üretebilir. PDF ve DOCX
  ayrıştırıcıları da yeni bir saldırı yüzeyi. *Öneri:* belge metni güvenilmeyen veri olarak sabit bir zarfla verilsin;
  emir ya da üst düzey metin deterministik olarak işaretlenip onay ekranında gösterilsin; IR'daki her sayı kaynakta
  geçmeli; dosya okuma için izin listesi (kapsam dizini altında gerçek yol, metin biçimleri, boyut sınırı), yasak
  listesi (`.env*`, anahtar dosyaları), dosya özeti ve bayt aralıkları; ajan metin değil, özetlenmiş dosyadaki
  konumları göndersin ki yeniden anlatım yakalanabilsin.
- **M-12. Sampling bağımsız bir formülasyon yolu değil.** Sampling çağıran istemcinin modelini kullanır (ajanla aynı
  aile) ve istemci isteği ve yanıtı değiştirebilir. *Öneri:* "ajan aracılı" sayılsın; hiçbir zaman zorunlu üye olmasın.

##### Yeterlik ve heyet

- **M-13. Sıfır tolerans heyet düzeyine taşınmalı.** Her üyeye ayrı sıfır tolerans, en üst etiketi ayların çoğunda
  kapalı tutuyor. *Öneri:* üyeler sıfır olmayan bir üst sınırla nitelendirilsin; sıfır tolerans heyet düzeyindeki
  "birlikte yanlış oybirliği" oranına ve sonuç başına denetimlere uygulansın. Bir kritik hata yalnızca ilgili tabakada
  (ör. eksik değer davranışı) kaydı düşürsün ve kalıcı bir test olsun. **Sabit sınır:** sıfır hatayla bir oranın p'nin
  altında olduğunu göstermek yaklaşık 3/p örnek ister. 100 görevlik heyet kabulü birlikte hata oranını ancak yaklaşık
  %3'ün altına bağlar; %0,1 için yaklaşık 3.000 görev gerekir. Hiçbir tasarım bunu kaldırmaz.
- **M-14. Tek istemcili yabancıda başsız sürüş etiket kazandırmaz.** Çağıran ajan ile aynı istemcinin başsız çağrısı
  aynı ailedir; maliyeti (üç adaptör, sürüm başına yalıtım testleri, döngü riski, belirsiz fatura, B-5) karşılığında
  etiket değişmez. *Öneri:* aynı aileden yalıtılmış örnekler yalnızca "aile içi uyuşma" diye raporlansın, aile
  çeşitliliği diye değil.
- **M-15. Toplayıcıda yol çeşitliliği gerekir.** *Öneri:* sayılan en az bir üye toplayıcı dışı bir yoldan gelsin.
  Her üye kullandığı kaynak aralıklarını ve sayıları çıktısında aynen alıntılasın; alıntı ile özgün metin arasındaki
  fark, aracının istemi sıkıştırdığını aracının beyanından bağımsız gösterir. Kapsam incelemesi v1 için soru 5'i A
  seçeneğiyle kapatmayı öneriyor.
- **M-16. Test setinin sızması için zaman ayrımı.** *Öneri:* üretici ve puanlayıcı açık; her ölçümün tohumu, ölçüm
  kaydedildikten sonra belirlenen bir değerden türetilir; ölçümden sonra tohum ve kanıt paketi yayımlanır, herkes
  yeniden üretip puanlar. Gerçek 40 problem bir dönem gizli kalır, sonraki dönem yayımlanır.
- **M-17. Kayıt dağıtımında güncellik ve geri alma koruması yok.** İmzalı ama eski bir kayıt listesi, iptal edilmiş
  bir yapılandırmayı yeniden geçerli gösterebilir. *Öneri:* imzalı, sürüm numarası yalnızca artan, son tarihli bir
  anlık görüntü; pakette sabitlenmiş kök anahtar; düşük sürüm reddi; bilinmeyen şema sürümü kapalı başarısızlık.
  Taze anlık görüntü yoksa `PROVEN` kapalı ve kutu nedenini yazar.

##### Tasarımın geri kalanı

- **M-18. Tasarım hâlâ sahibi tek kullanıcı sayıyor.** §1 ("önce sahibin kendisi için"), K6, K14, K15, §4.1'deki
  `strict_independence = false` gerekçesi ("sahibin 3 aboneliği"), §4.3'teki `strict_input_provenance = false` (ajanın
  doldurduğu bir değer heyet varken `PROVEN` altında kalabilir), §11 ("`PROVEN` ulaşılabilir", "açık soru kalmadı").
  *Öneri:* varsayılanlar `strict_input_provenance = true` ve `PROVEN` için `strict_independence = true` olsun; yeni
  sahip kararları K27 ve sonrası olarak eklensin ve eski K satırlarında "yerine: K…" yazsın. K2'nin "Red Team
  denetiminden geçmiş kadar kesin" standardının yalnızca `PROVEN` için geçerli olduğu sahipçe açıkça kabul edilsin.
- **M-19. Diskteki rapor korunmuyor.** "Güvenilen çıktı rapor dosyasıdır", ama ajan dosyayı Rigor yazdıktan sonra
  düzenleyebilir. *Öneri:* iş sonu bildirimi etiketi, ana değeri ve kısa bir rapor özetini de taşısın;
  `rigor verify-report <dosya>` komutu.
- **M-20. Yeni ret kodları tanımsız.** İzin verilmedi, bütçe bitti, metin için LLM yolu yok, desteklenmeyen dosya
  biçimi, kapsam dışı dosya, düzeltme turu sınırı, yalıtım ya da iç içe çağrı hatası, toplayıcı sözleşme ihlali,
  birden çok problemden seçim yapılmadı. Tasarımın ret listesi (satır 198) plandaki listeyle (satır 443) de uyuşmuyor.
- **M-22. Farklı geliştiricilerin modelleri de belirgin biçimde birlikte yanılıyor; üç üyeli heyet kabaca 1,7
  bağımsız üye kadar bilgi taşıyor.** Morante ve García-Rubio (2026) MMLU üzerinde ölçtü: tek modelin farklı sıcaklık
  örnekleri ve personaları arasında hata korelasyonu 0,85; farklı geliştiricilerin beş modeli arasında 0,38. Makalenin
  modelinde (birbirinin yerine geçebilir ikili oylar, eşit doğruluk, eşit korelasyon) N üyenin "etkin bağımsız üye
  sayısı" N / (1 + (N−1)ρ) olur ve 1/ρ'yu aşamaz. ρ = 0,38 ile üç üye ≈ 1,7 bağımsız üyeye denk gelir; üye eklemek
  bunu 2,6'nın üstüne çıkaramaz. Makale ayrıca çoğunluğun tek bir üyeden daha kötü olabileceğini ve "dil modelleri
  arasında uzlaşmanın kendi başına doğruluk kanıtı olmadığını" söylüyor.
  *Aktarım sınırı:* ölçüm çoktan seçmeli sorularda ve çoğunluk oyu üzerine; Rigor oy saymıyor, oybirliği ve biçimsel
  denklik istiyor. Rakamlar Rigor'a doğrudan taşınmaz. Taşınan sonuç: aile çeşitliliği gerekli ama bağımsızlık değil;
  aynı modelden yalıtılmış birden çok örnek (M-14) neredeyse hiç bağımsızlık katmaz (ρ ≈ 0,85).
  *Öneri:* R-2'deki heyet kabulü üyeler arası hata korelasyonunu ölçsün ve raporlasın; makalenin önerdiği altı
  maddelik raporlama listesi kanıt raporu §6.8'e uyarlanmak üzere incelensin.
- **M-21. İç içe çağrı ve istemci bulma tanımsız.** *Öneri:* yalıtım bayraklarından bağımsız bir özyineleme koruması
  (ör. `RIGOR_DEPTH` ortam değişkeni varken `rigor_solve` reddeder) ve negatif testi; istemci bulma yöntemi ve istemci
  başına yetenek tablosu; yalıtımı doğrulanamayan istemci yeterlik eşleşmesine giremesin.

#### Küçük bulgular (bu turda düzeltilenler işaretli)

- m-1. LLM yolu numaraları araştırma maddelerinde karışmıştı. *Düzeltildi.*
- m-2. Groq sınırı yalnızca bir modelin örneğiydi; veri okuyucuları F1'de değil F2'de; serbest metin yasağı A3'te
  değil §6.2'de. *Düzeltildi.*
- m-3. "Sıraya alınan açıklar" tablosundaki kanıtlar eksik ya da yanlış satır gösteriyordu. *Düzeltildi.*
- m-4. Soru 2'deki "kayıtlar önce ücretsiz yollar için" önerisinin öncülünü soru 3'teki bulgu çürüttü.
  *Geçersiz işaretlendi.*
- m-5. "Sıra ifadesi" sayısı 11 değil 12. *Düzeltildi.*
- m-6. README hâlâ eski vaadi, üç etiketi, "3 bağımsız model"i, yalnızca sahibin aboneliklerini, dokuz MCP aracını ve
  altı adımlı yapım sırasını gösteriyor. İzin isteme, kullanıcının kotasından harcama ve problem metninin sağlayıcıya
  gitmesi hiç yazmıyor. Yabancı için README ve kullanım dosyası yalnızca Türkçe. *Açık; tasarım revizyonuyla birlikte.*
- m-7. OpenRocket karşılaştırması (K17) `.ork` okuyucusu gerektirmiyor; OpenRocket simülasyon CSV'si veriyor.
- m-8. F8 optimizasyonun tek tüketicisi Sentinax'ın iki çıktısı; onlar zaten dürüstçe `CROSS_VALIDATED` alıyor.
- m-9. Eşikler (300 + 100, %80/%90, 30 gün, 15 dakika, bütçe) şema değişmeden değişebilmeli: sürümlü bir politika
  dosyası; kayıtlar ölçüldükleri politikanın özetini taşısın.
- m-10. Yeniden üretim, kaydın çalışma anında geçerli olup olmadığını kuramaz: kayıt, çağrı başına dönen model kimliği,
  izin kimliği ve bütçe sayaçları oturum kaydına yazılmalı.
- m-11. Belgenin yapısı: araştırma tabloları analizin içinde; her soru farklı bir şablonla yazılmış; aynı kısıt
  (A6, "anahtar formla istenemez", "form her istemcide çalışmıyor") üç yerde farklı sözlerle tekrarlanıyor. Tam bir
  yeniden düzenleme `egm-draft` adımına bırakıldı.

#### Sahibin kullanımına göre erteleme sırası (tasarımcı önerisi; S-17'nin uygulaması)

Hangisinin önce bekleyeceği, sahibin üç kullanımının (roket R1–R11, kripto botu, Sentinax) ona ihtiyaç duyup
duymadığına göre sıralandı. İlk sıradaki ilk bekler.

1. Lean 4 arka ucu (F5, K26). Birimli problemlerde Lean yolu hiç seçilmiyor (§6.11); sahibin bütün problemleri birimli.
2. F6 alan araçları, akışkanlar paketi, PDE ve geniş alan altın seti. Alandan bağımsızlık mimari test olarak kalır.
3. `KANITLANDI`'nın tamamı: yeterlik sistemi, kayıt dağıtımı, üç üyeli heyet, heyet kabulü, toplayıcı adaptörleri.
4. F4 hakem paneli ve öğrenme defteri. Şablonlar ve deterministik öz-denetim kalır (B2 toplu mutabakat bunlara dayanır).
5. Başsız istemci sürme; izin, bütçe, 15 dakika ve bildirim (B-5 yüzünden de beklemeli).
6. PDF/DOCX okuyucu.
7. F8 optimizasyon.
8. F3 Red Team'in kendisi (üç formülatör, geri çeviri, mutasyon), LLM sadeleştirme, okunabilirlik puanı, birinci sınıf
   İngilizce.
9. `.ork` okuyucu (CSV karşılaştırması kalır).
10. Toplu onay ekranı.
11. Katı ayrıştırıcı (doğrudan yol da bekletilirse; bekletilmezse `ast` beyaz listesiyle).

Sahip 2026-11-11'de "çatışırsa ben önceyim" dedi (S-18); yukarıdaki sıra bu sürümdür. Sıranın kendisi tasarımcının
türetmesidir ve sahip onayı bekler.

Bu sıraya göre en küçük v1 (tasarımcı önerisi):

- Etiketler `CERTIFIED`, `CROSS_VALIDATED`, `REFUSED`. `PROVEN` hiç verilmez; en üst etiketle yanlış sonuç dönmez.
- Girdi: kurucu API (sahip), tek kaba `rigor_solve` aracı ve `rigor solve` komutu (ajan yazdı diye işaretli IR).
  Onay F1'deki elicitation ve işletim sistemi penceresiyle, B-1'deki durumlarla.
- Sertifika: B-3'teki dar denetleyici; dışındaki her şey en çok `CROSS_VALIDATED`.
- Roket: R1–R7, `.eng`/xlsx/CSV okuyucular, iki integratörlü ODE, CSV'den OpenRocket karşılaştırması.
- Finans: B1 özdeşlik denetimi, B2 `Decimal` mutabakatı, bütünlük ve regresyon öz-denetimli şablonlar.
- Tahmini iş: 10–15 hafta; 16 haftaya payla sığar.

### İkinci dış tarama (2026-11-11): iki rapor, Faz II ve ekleri

Sahip 2026-11-11'de iki dış tarama raporu ve ekleri ekledi (hepsi `docs/research/external-reports/` altında):

- **R-TR:** `2026-11-11-tam-tarama-tr.md` (özgün adı "Rigor - Tam Depo Adversarial Red Team Denetimi ve Mimari
  Güvence Raporu").
- **R-FII:** `2026-11-11-tam-tarama-ve-faz-ii.md` (özgün adı "RIGOR — FULL REPOSITORY ADVERSARIAL RED TEAM &amp;"). İçinde iki rapor var: birinci tur
  ("Bağımsız Red Team mimari denetimi") ve "Deep Research Phase II".
- **Ekler** (`data/2026-11-11-faz-ii/` altında): `faz_ii_yeni_bulgular.csv`, `onceki_rapor_eksiklik_matrisi.csv`, `izole_karsi_ornekler.csv`,
  `istatistik_yeniden_denetim.csv`, `iki_asamali_kabul.csv`, `kabul_kalibrasyonu.csv`, `deney_ortami.json`.

Bu bölüm iki raporun tasarımcı tarafından yapılan denetimidir; EGM'nin taze gözlü incelemesi değildir.

#### Raporların kendi güvenilirliği

| Rapor | Değerlendirme |
| --- | --- |
| R-TR | Büyük ölçüde bu belgeyi yeniden anlatıyor ve kaynak olarak çoğunlukla bu belgeyi gösteriyor; bağımsız kanıt az. Üç uydurma ya da yanlış ayrıntı var: (1) "development HEAD (8f2a1b9c)" yok; o tarihteki HEAD `f7f86d3`. (2) Faz 1 planının yolu `2026-11-08-phase-1-mvp.md` diye verilmiş; gerçek yol `2026-11-07-faz-1-cekirdek.md`. (3) "rational ve decimal motorlara IEEE 754 kayan noktalı sayı olarak gidiyor" yanlış: SymPy'de `real=True` sembolik bir varsayım, Z3'te `Real` kesin rasyonel aritmetik. Sorun yuvarlama değil, alan üyeliği (`x ∈ ℚ` korunmuyor). Bu rapordan yalnızca bağımsız kaynakla desteklenen tek bulgu (QF_NRA, aşağıda Y-16) alındı. |
| R-FII | Titiz. İncelediği sürümü doğru veriyor (HEAD `f7f86d3`), kendi kapsam sınırını açıkça yazıyor ("tam depo için INSUFFICIENT_EVIDENCE"), Faz II'de Faz 1 planının tamamını okumuş, istatistik ekini yeniden hesaplamış ve karşı örnekleri yalıtılmış ortamda çalıştırmış. Deney ortamı Pydantic 2.11.4, SciPy 1.13.1 (Rigor'un hedefi 2.14 ve 1.18; `deney_ortami.json`). Önceki taramanın birçok maddesini haklı olarak daraltıyor. |

İstatistik eki: `istatistik_yeniden_denetim.csv` 34 satırın hepsini yeniden hesaplamış, hepsi geçti. Bu, aynı dosyanın
üçüncü bağımsız yeniden hesabıdır (ilki 2026-11-10'da bu belgede). Sayıların doğru olması model yeterliğinin
ölçüldüğü anlamına gelmez.

#### İlk taramada düzeltilen maddeler (R-FII'ye göre; tasarımcı kabul etti)

| Madde | Düzeltme |
| --- | --- |
| B-2 | Heyetin ayrışması, belirli bir adayın yanlış olduğunun kanıtı değildir; geçerli iki okuma ya da hizalama hatası olabilir. Ama yayını durdurmak için yeterlidir. Yeni kural (R-FII Faz II §V.7): heyet ayrışmışsa amaçlanan problemin cevabı olarak yayın durur; ayrışan yorumlardan biri ayrıca gösterilecekse yeni ve sınırlı bir iddia olarak sunulur, orijinal problem çözülmüş sayılmaz. |
| B-3 | "Z3 hükmü en çok `CROSS_VALIDATED`" önerisi yanlıştı: ikinci yöntem çalışmadıysa yapılmamış bir çapraz doğrulamayı iddia eder. Doğrusu: dört etiketten hiçbiri uymuyorsa olumlu etiket verilmez, açık bir `solver_verdict` tanı kaydı yazılır. Ayrıca yalnızca `fractions` ve `decimal` kullanmak denetleyicinin sağlamlık kanıtı değildir; denetleyicinin kendi negatif kabul paketi gerekir. |
| B-4 | "Tehdit modeli yok" fazla genişti: tasarım §7.2, sınırsız kabuk erişimli ajanın yerel kanalları taklit edebileceğini zaten kabul ediyor. Eksik olan, bu sınırın hangi etiketin hangi saldırgana karşı korunduğuna bağlanması. Anahtar zinciri ve rastgele değer de tam çözüm değil: aynı kullanıcı hesabındaki ajan anahtar zincirine ya da imzalama servisine erişebilir. |
| B-5 | Daraltıldı. Anthropic metni değiştirilmemiş Claude Code'a son kullanıcının kendi girişi için istisna içeriyor; OpenAI'nin "açık kaynak depolarda kullanmayın" uyarısı belirli bir ChatGPT oturumlu CI akışına özgü ve bütün yerel otomasyona genellenemez; OpenAI ayrıca ChatGPT girişli uygulama entegrasyonunu belgeliyor; Google üçüncü tarafların OAuth'u sırtlanmasını yasaklıyor. Sonuç: genel yasak da genel izin de söylenemez. Öneri değişmedi: sağlayıcı başına açma bayrağı, varsayılan kapalı. |
| B-6 | 33–52 ve 10–15 hafta doğrulanmış tahmin değil. Sahip 2026-11-11'de "takvime gerek yok" dedi (S-19); kontrol noktası önerisi düştü. |
| "`PROVEN` kapalıysa vaat kendiliğinden tutar" | Yanlış. Yanlış `CERTIFIED` da kritik başarısızlıktır (B-3'teki "yanlış `CERTIFIED` = 0" ölçütü bu yüzden ayrıca gerekli). |
| M-4 | Yeterlik şemasını erken tasarlamak döngüsel değildir. Döngüsel olan, gerçek ölçümü henüz kabul edilmemiş bir değerlendiriciye bağlamaktır. |
| M-11 | "IR'daki her sayı kaynakta geçmeli" fazla katı: türetilmiş sabitler (π, birim katsayıları, ara değerler) kaynakta geçmez. Kural "her verilen değer" olmalı. |
| M-12 | Sampling'in çağıranla aynı aile olması protokolün zorunluluğu değil; ama istemci aracılı olduğu için bağımsız yol sayılmaması doğru. |
| M-14 | Fazla güçlü: aynı istemci farklı bir modeli çağırabilir. Katkı, yanıtta dönen gerçek model kimliğine bağlanmalı, istemci adına değil. |
| M-15 | Kaynak alıntısı, aracının istemi sıkıştırmadığını kanıtlamaz; yalnızca bazı sıkıştırmaları yakalar. |
| M-19, M-21 | `verify-report` ve `RIGOR_DEPTH` ortam değişkeni, aynı saldırgan doğrulayıcıyı ya da ortamı değiştirebiliyorsa yetki sınırı değildir; yalnızca risk azaltır. |
| M-22 | Rakamlar makalenin PDF'inden doğrulandı (2026-11-10); R-FII'nin dediği gibi Rigor'un güvence hesabında kullanılmamalı. Bu belge zaten öyle demişti. |
| Ö-2-2 | İki aşamalı plan iyi modeli daha sık geçirir ama kötüyü de: gerçek hata oranı %1 olan modelin geçme olasılığı %4,90'dan %5,63'e çıkıyor. İki aşamayı 311 + 311 soruya büyütmek bunu %5,00'e geri çekiyor (`kabul_kalibrasyonu.csv`). Önceden ilan edilmiş olmak tek başına yetmez; bütün durma yolları ve her hata oranında geçme olasılığı yazılmalı. |
| En küçük v1 | Sahibin ihtiyaçlarını otomatik karşılamıyor: roket önceliği R1–R11, öneri R1–R7; finans B1 yalnızca basit özdeşlik değil; `Decimal` yuvarlama izi olmadan birebir mutabakat eksik kalır. Hangi hesapların v1 kabul ölçütü olduğu sahibin seçimi (A-13). |

#### Yeni bulgular

R-FII Faz II'nin "P2" kayıtları ve iki raporun öbür yeni maddeleri. Karşı örneklerin çoğu `izole_karsi_ornekler.csv`
dosyasında çalıştırılmış haliyle var.

##### Engelleyici

- **Y-1. Aday geçerliliği, teklik ve tamlık karışıyor** (P2-01). Planın yedek yolu (`crosscheck_numeric`: farklı
  başlangıçlardan aynı köke yakınsama) teklik kanıtı değil: `sin x = 0` için üç başlangıç da 0'a yakınsadı, π de
  köktür. SymPy `solve` yalnızca `{0, π}` döndürüyor; 2π eksik. *Öneri:* sertifika `WITNESS_VALIDITY`,
  `COMPLETENESS`, `UNIQUENESS` ayrımını taşısın; desteklenmeyen özellikte etiket verilmesin.
- **Y-2. `mod` ve sayı işlemlerinin anlamı arka uca göre değişiyor** (P2-02). `7 mod −3`: Python −2, `Decimal` 1
  (ikisi 2026-11-11'de yerelde yeniden çalıştırıldı), SymPy −2 (rapora göre); SMT-LIB Öklid kalanı kullanır (1). *Öneri:* sürümlü bir işlem
  anlamı profili (ör. `mod_floor`, `mod_euclid`, `mod_trunc` ayrı işlemler); negatif bölen testleri; anlamı korunamayan
  derleme reddedilsin.
- **Y-3. Hedef ifadelerinin tanımlılık yükümlülükleri açık değil** (P2-03). `x/x` sadeleşince `x ≠ 0` koşulu kayboldu.
  *Öneri:* tanımlılık yükümlülükleri sadeleştirmeden önce bütün ağaçtan çıkarılsın; negatif üs sıfır olmayan taban
  ister.
- **Y-4. Elicitation insan onayının kanıtı değil.** Resmî MCP Python SDK belgesi, istemci bir ajansa isteği
  kullanıcıya sormadan kendisinin yanıtlayabileceğini söylüyor; Claude SDK'nın elicitation kancaları da yanıtı
  programla işleyip değiştirebiliyor. Faz 1 testlerindeki `Provenance(USER_DIRECT, "sdk")` da kimlik değil: SDK'yı ajan
  da çağırabilir. Bu, tasarımın "elicitation varsa `USER_DIRECT`" varsayımını ve bu belgedeki B-1, M-7 önerilerinin
  öncülünü zayıflatıyor. *Öneri:* onay kaydı `transport_channel`, `responding_principal`, `human_presence_evidence`
  ayrımını taşısın; kanıtlanamayan her platformda rapor bunu açıkça yazsın; `USER_DIRECT` yalnızca güvenilen bir onay
  bağdaştırıcısı üretebilsin.
- **Y-5. Formun gönderilmesi ile onay kararı karışıyor** (P2-04). Plan görev 18'de `AcceptedElicitation` doğrudan
  `USER_DIRECT` onay sayılıyor; `AcceptedElicitation(onay=False)` ayrılmıyor. Reddetme ya da iptal işletim sistemi
  penceresine düşüyor; bu, kullanıcının "hayır"ını başka kanaldan yeniden sormak demek. *Öneri:* "kabul edildi ve
  `onay=True`" açık kural; reddetme ve iptal son durum.

##### Büyük

- **Y-6. MCP protokol çağı ve yeniden deneme sözleşmesi eksik** (P2-05). Güncel MCP belgelerine göre `ctx.elicit()`
  eski bağlantılar için geri kanal yoludur; 2026-07-28 protokolünde `InputRequiredResult` ve çözücü akışı kullanılır.
  İmzalı durum tek kullanımlık değildir: aynı onay iki işçide tüketilirse iki ücretli çağrı başlayabilir. *Öneri:*
  kayıtta SDK sürümü, anlaşılan protokol sürümü, istemci adı ve sürümü; kalıcı tüketim kaydı, atomik durum geçişi,
  `expected_revision`, iş bazlı yineleme anahtarı, harcamadan önce rezervasyon, "dış etki belirsiz" durumu.
- **Y-7. Kapalı form ODE/PDE çözümünü yerine koymak tekliği kanıtlamaz** (P2-06). *Öneri:* "geçerli yörünge" ile
  "tek çözüm" ayrı iddialar.
- **Y-8. İspat nesnesi üreten çözücü de eksik ispat üretebilir** (P2-07). cvc5'in Alethe çıktısında boş ("hole") ve
  güvenilen adımlar olabiliyor. *Öneri:* boş, bilinmeyen ya da desteklenmeyen adımda kapalı başarısızlık.
- **Y-9. Dört ayrı izin var.** Tanımı kabul etmek, iş akışını devretmek, veriyi bir sağlayıcıya göndermek ve kaynak
  harcamak ayrı izinlerdir. Birincisi diğer üçünü, devralma izni de eksik değer uydurmayı kapsamaz.
- **Y-10. `Decimal` yürütme politikası kesin ifade değildir.** Hassasiyet, yuvarlama modu, işlem sırası ve yuvarlama
  noktaları sonucun parçasıdır: 2 basamak hassasiyette `(1/3) × 3` ara yuvarlamayla 0,99 (yerelde yeniden
  çalıştırıldı), kesin hesaptan sonra tek yuvarlamayla 1 verir. *Öneri:* "kesin matematiksel ifade" ile "belirtilen `Decimal` politikasının çıktısı" iki ayrı
  iddia; dar rasyonel denetleyici bu ayrım olmadan finans mutabakatını sertifikalayamaz.
- **Y-11. F8 çıkış ölçütü fazla geniş.** "LP/MILP altın testleri `PROVEN` (dual sertifikalı)" MILP için yetmez: `max x,
  2x ≤ 3, x ∈ ℤ≥0` için LP gevşetmesi 1,5, tamsayı optimumu 1. *Öneri:* LP, MILP ve konveks KKT ayrı kabul profilleri;
  MILP için tamsayı uygunluğu ve küresel sınırı kapatan ek kanıt.
- **Y-12. Boş aday listesi "çözüm yok" değildir.** `0 = 0` için SymPy `solve` boş liste döndürdü, `solveset` bütün
  reelleri. *Öneri:* boş liste ret ya da "çözüm yok" diye yorumlanmasın.
- **Y-13. `frozen=True` iç içe listeleri dondurmuyor.** Pydantic 2.11.4'te onaydan sonra `args` listesine eleman
  eklenebildi (2.14'te sınanmadı). *Öneri:* demet tipleri ya da onay anında derin kopya ve özet; onaydan sonra
  değiştirme testi.
- **Y-14. Ayrıştırıcıda kaynak sınırı yok.** `ast.parse` beyaz listesi kod çalıştırmayı önler ama derin ağacı, dev
  üssü, çok büyük tamsayıyı, uzun belirteci ve Unicode benzer karakterleri önlemez. *Öneri:* ayrıştırıcıya ve her
  çözücü alt sürecine boyut, derinlik, süre ve bellek sınırı.
- **Y-15. Yeniden üretim üç ayrı işlemdir:** saklanan kanıtı yeniden denetlemek, saklanan model çıktısını yeniden
  puanlamak, uzak modeli yeniden çağırmak. Üçüncüsü aynı yürütmenin tekrarı değildir. Eski bir rapor iki soruyu ayrı
  cevaplamalı: o günkü politikayla kabul edildi mi, bugünkü politikayla ediliyor mu?
- **Y-16. Doğrusal olmayan eşitsizliklerde Farkas sertifikası yok** (R-TR HIGH-05). Farkas önermesi yalnızca doğrusal
  reel aritmetik için sertifika verir; tasarımın "polinom eşitsizlikleri Z3 ile `PROVEN`" satırı (§3.4) için bağımsız
  denetleyici yok. B-3'ün düzeltilmiş haline bağlanır.
- **Y-17. Tasarım §10 ile yol haritasının sırası farklı** (P2-08). Tasarım: alan uyarlama, optimizasyon, finans. Yol
  haritası: F6 alan, F7 finans, F8 optimizasyon; ve "tasarımla aynı sıra" diyor. *Öneri:* tek bağımlılık grafiği.

##### Küçük

- **Y-18.** `eval_arb`'nin genel hassasiyet bağlamını geçici değiştirmesi eşzamanlı işlerde risk.
- **Y-19.** Mimari içe aktarma testinin göreli, dinamik ve geçişli içe aktarmaları kapsayıp kapsamadığı açık değil.
- **Y-20.** Kanonik JSON sözdizimsel kimliktir: `"0.1"` ile `"1/10"` aynı değer, farklı özet. İçerik kimliği ile
  matematiksel denklik ayrı tutulmalı.
- **Y-21.** Lean'i (K26) ertelemek teknik bir karar değil; açık sahip kararı gerekir (A-12).

#### Kapanan ya da daralan konular (R-FII Faz II'ye göre)

- **Birim normalizasyonu:** Faz 1 görev 11 verilenleri SI temel birimlerine çeviriyor ve sonucu geri çeviriyor.
  "Normalizasyon tanımsız" iddiası geri çekildi. Kalan sınama soruları: Z3 teklik denetimi aynı normalleştirilmiş
  problemi mi görüyor; mutlak sıcaklık ile sıcaklık farkı ayrılıyor mu.
- **Aralığın sıfırı içermesi:** Faz 1 görev 10 bu durumda `undetermined` ve `all_satisfied=False` veriyor; tasarım
  doğru.
- **Onaydan sonra kök kısıtı eklenmesi:** görev 14'te doğrudan doğrulandı; açık (B-8).

#### İki raporun sahibe sorduğu kararlar

Çoğu bu belgedeki açık noktalarla örtüşüyor. Raporların önerdiği ve sahip onaylamazsa güvenli varsayılan:

| Karar | Raporların önerisi | Onay yoksa güvenli varsayılan | Kayıt |
| --- | --- | --- | --- |
| v1'de `PROVEN` | İlk v1'de kapalı (iki rapor da) | Kapalı | A-5 |
| `CERTIFIED` kapsamı | Yalnızca açık formal iddia, bütün problem değil | Bağımsız kabul yoksa verilmez | Ö-1-3 |
| "Bilmiyorum" | Eksik değer uydurmadan koşullu formal hesap; yorum onayı yok diye açık yazılır. R-TR: etiket tavanı `CROSS_VALIDATED` | Orijinal problem çözülmüş sayılmaz | A-2 |
| S-5 / S-9 | Fiyat doğruluk ölçütü olmasın | Çatışan üst etiket kapalı | Ö-2-1 |
| Başsız istemci | Sağlayıcı bazlı, varsayılan kapalı | Ağ çağrısı yok | A-3 |
| Yerel saldırgan kapsamı | Güvence düzeyleri açıkça ayrılsın | Tam kabuk erişimine karşı onay garantisi verilmez | A-14 |
| Lean v1 (K26) | Sahip önce v1 için ertele | K26 yürürlükte kalır | A-12 |
| PDF/DOCX | Sonra | Ajanın aktardığı işlemlerle sınırlı rapor | A-11 |
| Toplayıcının üst katkısı | Ölçüm ve politika onayına kadar sayma | Katkı yok | A-4 |
| Platformlar | Gerçek onay bağdaştırıcısıyla sınanmış platformlar; R-TR: v1 macOS ve Linux | Desteklenmeyende ayrıcalıklı işlem yok | A-8 |
| Yeterlik eşikleri | Pilottan sonra dondur | Hiçbiri bilimsel garanti sayılmaz | R-4 |
| İlk v1 hesap listesi | Roket ve finans için somut kabul envanteri | "Bütün ihtiyaçlar karşılandı" denmez | A-13 |
| Negatif `mod` | Ayrı işlemler ya da açık daraltma | Desteklenmeyen reddedilir | Y-2 |

### Soru 1 (kapandı): Sertifikası olan ama tam heyetten geçmemiş sonuç ne alır?

Kaynak: sahip `docs/research/external-reports/2026-11-10-soru1-etiketler-2.md` (kısa adı `Soru1-2`) dosyasını cevap olarak gösterdi.

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
   heyet düzeyi ya da onayın doğrudan kanaldan gelmesidir. **Çelişki (tam tarama B-1):** sahibin sonraki "bilmiyorum"
   kararı ve doğrudan yol önerisi onaysız olumlu etiket veriyor; bu madde onlarla birlikte yeniden yazılacak.
3. `CERTIFIED` ile `CROSS_VALIDATED` sınırı "denetim kesin mi" ölçütüdür. Çözücüden ayrı bir denetleyici kesin iddiayı
   karara bağlıyorsa `CERTIFIED`; yalnızca tolerans içinde uyuşma varsa `CROSS_VALIDATED`.
4. Birim dönüşümünde denetleyici katsayıyı ayrı, kaynağı yazılı bir tanım tablosundan alır; alamıyorsa kutu ortak
   bağımlılığı yazar ve "bağımsız" demez.
5. Faz 1'de `CERTIFIED` üretecek bağımsız denetleyici yok; örnekteki kutu `v0.1.0`'da çıkamaz. Dar bir rasyonel
   denetleyicinin fazı soru 6'ya bırakıldı.
6. Tasarımda etiket sırasına dayanan ifadeler açık koşula çevrilecek. Sayı 11 değil, 12: tasarım satır 145, 174,
   204, 236, 239, 245, 264, 305, 312, 353, 557, 797 ("en fazla / en az"), ayrıca 443 ("ile sınırlı kalır"). 239 ile
   797 aynı kuralı iki kez söyler; 305 bir alt sınırdır (Sentinax kapısı). Yol haritası satır 63, 75 ve plan satır 7
   da aynı dili kullanıyor.
7. Ajan aracılığıyla gelen onayda tasarımın bugünkü davranışı (düşük etiket + uyarı) korunur; rapor bunu "bekle ya da
   reddet"e sertleştirmeyi öneriyordu.
8. `CERTIFIED` çok farklı durumları tek ad altında toplar; farkı yalnızca "Problem incelemesi" satırı taşır.
9. Sertifikasız sonuçlarda heyetin niteliği etikette görünmez; yine yalnızca "Problem incelemesi" satırındadır.

#### Sıraya alınan açıklar (depoda doğrulandı)

| Açık | Kanıt | Nerede ele alınacak |
| --- | --- | --- |
| `rational` ve `decimal` alanları motorlara `real` olarak gidiyor | Plan satır 390 (SymPy) ve 394 (Z3). `decimal` alanında hassasiyet ve yuvarlama alanı da yok (plan satır 166; tasarım §6.2 bunu istiyor) | Tasarım revizyonu; yeterlik ölçümünden önce |
| JSON'da tekrarlı anahtar reddedilmiyor | Planda bunu sınayan test yok; Pydantic son değeri alır. MCP yolunda SDK tekrarlı anahtarları Rigor'a ulaşmadan birleştirir, yani denetim ham metin sınırında yapılmalı | Tasarım revizyonu |
| `unsat_core` sertifika türü sayılıyor | Plan satır 481; tasarım §3.4 satır 177 ve §6.6 satır 554; yol haritası satır 23 | Tasarım revizyonu |
| Onaylanan, çözülen ve raporlanan IR'ın aynı olduğu denetlenmiyor | Her olay IR özetini zaten kaydediyor (plan satır 630); eksik olan eşitlik kuralı. Çok kök yolunda seçilen kök onaydan sonra IR'a ekleniyor | Tasarım revizyonu |
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
- Cevap olarak `docs/research/external-reports/2026-11-10-soru2-yeterlik.md` (kısa adı `Soru2-1`) dosyası ve `docs/research/external-reports/data/2026-11-10-soru2-yeterlik-istatistik.csv` (özgün adı
  `rigor_yeterlik_istatistik_hesaplari.csv`) gösterildi.

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

Sonucu: tamamen ücretsiz ama yeterlikli bir heyet `KANITLANDI`'ya ulaşabilir.

Durum: sahibin sonraki kararı (güçlü ücretsiz model aynı sayılır) karar 5'in eski metniyle çelişiyor. Yeni metin
tasarımcı önerisidir ve sahip onayı bekliyor (Kayıt: S-5, Ö-2-1).

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
   örnek sınırla (bir model için günde 200.000 token; Groq sayfası bu tablonun Developer planına ait olduğunu
   söylüyor, ücretsiz plan rakamı doğrulanamadı) ve çağrı başına 3.000 token varsayımıyla bu, her 30 günde o modelin
   yaklaşık 6 günlük kotasıdır.
   *Tasarımcı önerisi (geçersiz; soru 3'teki bulgu öncülünü çürüttü, bkz. M-6):* dağıtılan kayıtlar önce yabancının
   kullanacağı ücretsiz yollar için üretilir.
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

`data/2026-11-10-soru2-yeterlik-istatistik.csv` dosyasındaki 34 satırın tamamı yalnızca standart kütüphaneyle yeniden
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
| Berger–Hsu 1996 (Statistical Science 11(4)) | PDF'ten doğrulandı (2026-11-11). Teorem 1: her bileşen testi α düzeyindeyse kesişim–birleşim testi de α düzeyindedir; "çoklu karşılaştırma düzeltmesine gerek yoktur". |
| Chen vd. 2018 (ACM Computing Surveys 51(1)) | PDF'ten doğrulandı (2026-11-11): metamorfik ilişkiler hedef fonksiyonun "gerekli özellikleri"dir; "her gerekli özellik metamorfik ilişki değildir". İlk eklenen PDF başka bir makaleydi (Liu vd., "A Systematic Survey on Large Language Models for Algorithm Design"). |
| Knight–Leveson 1986 (IEEE TSE SE-12(1)) | PDF'ten doğrulandı. Aynı şartnameden bağımsız yazılmış 27 sürüm, bir milyon test; bağımsızlık modeli %99 güven düzeyinde reddedildi; bir test girdisinde 27 sürümün 8'i birlikte hata verdi. |
| Morante ve García-Rubio 2026, Discover Informatics 1:35 (`10.1007/s44564-026-00040-z`) | PDF'ten doğrulandı. Başlık: "Correlation limits the reliability of ensemble decision making with large language models". Ayrıntı tam tarama M-22'de. |

Önceki turlarda doğrulananlar: Kim vd. 2506.07962; Buçinca vd. 2102.09692; Lin–Hooi 2509.14034; Batra vd. 2610.35930;
GSM-Symbolic 2410.05229; LiveBench 2406.19314; MCP elicitation; OpenRouter yanıt önbelleği.

### Soru 3 (kapandı): Hiç anahtarı ve aboneliği olmayan biri ilk çalıştırmada ne görmeli?

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
- **Rigor belge okumaz.** Veri okuyucuları (`.eng`, xlsx, CSV, `.ork`) da F2'de geliyor; F1'de Rigor hiç dosya
  okumaz. Belgeyi ajan okur ve metni
  aktarır; kaynak aralıkları ajanın aktardığı metne göredir. Ajanın yanlış aktarması Rigor'un göremeyeceği bir hata
  kaynağıdır. Bir belgede birden çok problem varsa hangisinin çözüleceğini kimin seçeceği tanımsızdır.
- **"Repoya vermek" kod denetimi beklentisi doğurabilir.** Kod denetimi kapsam dışıdır (K13, K20). Yabancı
  "repomdaki hesapları kontrol et" derse Rigor yalnızca formülleri ve sayıları denetler.
- **İstemciler aynı değil.** Doğrudan onay formu her istemcide çalışmıyor (tasarım §7.2). Aynı ilk çalıştırma
  istemciye göre farklı etiketle bitebilir.
- Faz 1'de bağımsız denetleyici olmadığı için bu kullanıcının ilk sonucu `CERTIFIED` olamaz (soru 1, madde 5).

#### Sahip kararı: ilk çalıştırma akışı (2026-11-10, ikinci cevap)

1. Yabancı ajanına "bu repoyu kullanarak şu problemi, denklemi ya da belgedeki tüm matematiksel işlemleri çöz" der.
2. Ajan Rigor'u açar; bundan sonra akışı Rigor yönetir.
3. Girdi doğrudan bir matematik işlemiyse Rigor çözer ve çıktıyı verir.
4. Girdi metinsel anlatımsa Rigor elindeki bütün gücü kullanır, denklemleri çıkarır ve kullanıcıya üç seçenekle sunar:
   - **Doğru.**
   - **Yanlış** (kullanıcı doğrusunu verir).
   - **Bilmiyorum, sana bırakıyorum.**

#### Red Team: bu akış

- **Rigor görevi "devralamaz".** Rigor bir kütüphane ve MCP sunucusudur; kontrol ajanda kalır. Rigor akışı ancak araç
  açıklamaları, sunucu talimatları ve ajana yönelik bir kullanım dosyasıyla yönlendirebilir. Ajan uymayabilir; bu
  kanıtlanamaz, yalnızca kayda geçer.
- **"Bütün gücü" erişime bağlıdır.** Anahtarsız yabancıda Rigor'un kendi LLM'i yoktur; denklemleri çıkaran, Rigor'u
  çağıran ajanın modelidir. Heyet ancak kullanıcı erişim bağlarsa devreye girer.
- **"Doğrudan matematik" kimin kararı?** Bunu ajan sınıflarsa, metinsel bir problemi "doğrudan" sayıp onay durağını
  atlayabilir. Ayrıca bugünkü tasarımda Rigor serbest metin ifade ayrıştırmaz (§6.2 ve plan satır 17; A3 yalnızca kod
  çalıştıran yolları yasaklar); `x^2 - 5x + 6 = 0` yazısını IR'a
  çeviren de bir LLM'dir ve işaret, üs ya da örtük çarpım hatası yapabilir.
- **"Çözecek ve çıktıyı verecek" bugünkü planla çelişiyor.** Faz 1 altın testi G3, `x² − 5x + 6 = 0` için iki kökü
  görünce durup hangisinin istendiğini soruyor. Sahibin akışında beklenen çıktı çözüm kümesidir: `{2, 3}`.
- **Üçüncü seçenek bugünkü vaadi değiştirir.** Tasarım §1.1 "her sonuç sahibin onayladığı tanıma göre doğrulanmıştır
  ya da reddedilir" diyor; K4 Rigor'un kendi varsayımını yapmasını yasaklıyor. "Sana bırakıyorum" cevabında tanımı
  onaylayan bir insan yoktur.
- **Üçüncü seçeneğin lehine güçlü bir gerekçe var.** Hedef kullanıcı matematiği yargılayamadığı için aracı kullanıyor
  olabilir. Yalnızca "Doğru / Yanlış" sunulursa bilmeyen kullanıcı "Doğru"ya basar; sahte onay, dürüst "bilmiyorum"dan
  daha kötüdür, çünkü raporda "kullanıcı onayladı" yazar.
- **"Belgedeki tüm işlemler" denetlenemez.** Belgeyi ajan okur. Rigor ajanın bir işlemi atlayıp atlamadığını bilemez;
  çıktı "belgedeki tüm işlemler" değil, "ajanın aktardığı N işlem" demelidir. N işlem için N ayrı onay sorusu da
  kullanıcıyı düşünmeden onaylamaya iter.
- **Seçenekler ajan üzerinden gelirse ajan kendisi seçebilir** (A6). Üç seçenek istemcinin formunda ya da bant dışı
  pencerede gösterilmeli; gösterilemiyorsa cevap "ajan iletti" diye kaydedilir.

#### Tasarımcı önerileri (sahip onaylamadı)

- **"Doğrudan" mekanik tanımlanır:** girdi, LLM kullanmayan katı bir ifade ayrıştırıcısından bütünüyle geçiyorsa
  doğrudandır (kod çalıştırmayan, sabit dilbilgili bir ayrıştırıcı; A3'ü çiğnemez). Geçmiyorsa metinsel yola girer.
  Bu yeni bir bileşendir.
- **Doğrudan yolda onay durağı yoktur, yankı vardır:** çıktı, çözülen ifadenin kanonik halini ve kullanılan tanımları
  (ör. hangi foot) gösterir. Tanım kullanıcının kendi yazdığı ifadedir.
- **"Çöz" hedefi çözüm kümesini döndürür;** Rigor yalnızca tek değer gerektiğinde sorar. G3 buna göre değişir.
- **Üç seçenek kayda üç ayrı durum olarak geçer:** onaylandı; düzeltildi (yeni problem sürümü, yeniden sunulur);
  kullanıcı karar vermedi. Üçüncüsünde `KANITLANDI` verilmez ve kutu "tanımı kullanıcı onaylamadı" yazar.
- **Kullanıcıya denklemle birlikte sade anlatım gösterilir** (K7), böylece simgeyi değil anlamı yargılar.
- **Toplu işlerde tek onay ekranı** bütün çıkarılan işlemleri listeler; sonuç tablosunda her işlemin kendi etiketi olur.
- **Ajana yönelik kullanım dosyası** depoya eklenir: kurulum, hangi aracın çağrılacağı, metnin değiştirilmeden
  aktarılması, eksik değerin doldurulmaması.

#### Sahip kararı: "bilmiyorum" cevabı (2026-11-10, üçüncü cevap)

Kullanıcı "bilmiyorum, sana bırakıyorum" derse ve formülü tek bir model yazmışsa Rigor yine çözer ve sonuca bir not
düşer: "Sizin verdiğiniz matematiksel işlemin sonucu bu."

Red Team:

- **Not, metinsel yolda yanlış olur.** O yolda kullanıcı bir matematiksel işlem vermedi; metin verdi ve işlemi bir model
  yazdı. "Sizin verdiğiniz işlem" cümlesi formülün sahibini kullanıcı gibi gösterir.
- *Tasarımcı önerisi:* not iki yolda farklı yazılır ve çözülen denklemi her zaman gösterir.
  - Doğrudan yol: "Verdiğiniz şu ifadenin sonucu budur: …"
  - Metinsel yol: "Verdiğiniz metinden şu denklem çıkarıldı ve çözüldü: … Bu denklemi siz onaylamadınız; tek bir
    model yazdı."
- Etiket değişmez: `KANITLANDI` verilmez; sertifika varsa `CERTIFIED`, yoksa `CROSS_VALIDATED` ya da ret.
- Bu karar tasarım §1.1'deki vaadi değiştirir. Yeni hali: "Her sonuç, yanında yazan tanıma göre doğrulanmıştır;
  tanımı kimin yazdığı ve kimin onayladığı sonuçla birlikte gösterilir."

#### Rigor akışı tam olarak devralabilir mi? (sahibin sorusu)

MCP'nin içinde kalarak tam devralma olmaz; MCP'de kontrol istemcidedir. Devralma, kontrolün ters çevrilmesiyle olur:
Rigor sürücü olur, LLM onun çağırdığı bir alt süreç olur. Üç iş ayrı ayrı devralınabilir:

| İş | Bugün kimde | Rigor nasıl devralır | Sınır |
| --- | --- | --- | --- |
| Girdiyi almak | Ajan metni okur ve aktarır | Tek giriş noktası: ham metin ya da dosya yolu. Dosya yolu verilirse Rigor dosyayı kendisi okur | PDF/DOCX için okuyucu gerekir (yeni bileşen). Ajan metni yapıştırırsa değiştirmediği bilinemez |
| Kullanıcıya sormak | Ajan iletir | İstemcinin formu (elicitation) ya da işletim sistemi penceresi; ajanı atlar | Form her istemcide çalışmıyor (tasarım §7.2) |
| Formülü yazdırmak | Çağıran ajanın modeli | Rigor LLM'i kendi istemiyle, yalıtılmış olarak çağırır (aşağıdaki sıra) | Rigor'un ulaşabildiği bir LLM yolu olmalı |

Formül için LLM yolları (sahip yalnızca "önce izinle kurulu istemci, API anahtarı en son" dedi; 2. ve 3. sıranın
yeri tasarımcı önerisidir):

1. Makinede kurulu resmî ajan istemcilerinin başsız modu (tasarımdaki `CLIFormalizer`), kullanıcının izniyle.
   **Sağlayıcı koşulları bu yolu riskli kılıyor; bkz. tam tarama B-5.**
2. İstemcinin "sampling" desteği: sunucu, istemcinin modeline kendi istemiyle üretim yaptırır. Aynı izne tabidir.
   **Tam tarama M-12:** sampling çağıran ajanın modelini kullanır ve istemcinin elinden geçer; bağımsız yol sayılmaz.
3. İzin verilmezse çağıran ajanın yazdığı formül; "ajan yazdı" diye işaretlenir.
4. Son seçenek: kullanıcının bağladığı API erişimi (ücretsiz ya da ücretli).

Araştırma (zayıf, üçüncü taraf kaynaklar; tasarıma yazılmadan önce birincil kaynakla doğrulanmalı):

- Sampling'i yalnızca VS Code (Copilot) belgeliyor görünüyor; Claude Code'un resmî MCP sayfası sampling'den hiç söz
  etmiyor (birincil kaynakla doğrulandı). Yani 2. yol bugün çoğu istemcide yok.
- Başsız `claude -p` kullanımının abonelik kotasından ayrı bir krediye taşınacağı duyurulmuş (Haziran 2026); resmî
  başsız mod sayfası ayrı krediden söz etmiyor. Yani 1. yolun maliyeti hâlâ belirsiz.

Devralınamayanlar:

- Ajanın Rigor'u çağırıp çağırmayacağı ve sonucu kullanıcıya değiştirmeden aktarıp aktarmayacağı. Güvenilen çıktı
  Rigor'un yazdığı rapor dosyasıdır; ajanın yeniden anlatımı değildir.
- Ayrı bir Rigor ajanı yazmak (kendi döngüsü, kendi arayüzü) tam kontrol verir, ama bir API anahtarı gerektirir ve
  anahtarsız yabancıya uymaz. Önerilmiyor.

*Tasarımcı önerisi:* MCP kalır, ama yüzeyi tek kaba araca iner (`rigor_solve`: ham girdi ya da dosya yolu). Aynı işi
yapan bir komut eklenir (`rigor solve <dosya>`), ajan onu kabuktan da çalıştırabilir. Ajanın rolü kuryeliktir.

#### Sahip kararı: ajan istemcisini kullanma ve görevi devralma izni (2026-11-10, dördüncü cevap)

- Rigor, yabancının makinesinde kurulu ajan istemcisini formül yazdırmak için kendisi çağırabilir. Çağırmadan önce
  bunu yaptığını belirtir ve izin ister.
- API anahtarı istemek ya da `.env` okumak **son seçenektir**. Önce kullanıcının ajanlarını kullanmak için izin istenir.
- Ayrıca "matematiksel işlem bitene kadar bütün görevi devralmama izin var mı?" diye sorulur. İzin verilirse Rigor
  her şeyi üstlenir ve yapar.

#### Red Team: bu karar

- **Tek istemci tek ailedir.** Yalnızca bir ajan istemcisi olan kullanıcıda heyet kurulamaz; en üst etiket kapalı
  kalır. Anahtar istemek son seçenek olduğu için yabancıların çoğu tek formülasyonla kalır.
- **Birden çok istemci kuruluysa anahtarsız heyet mümkündür.** İzin ekranı bulunan bütün istemcileri saymalı.
- **Bu karar soru 2'deki bir sorunu hafifletir.** Yabancının yolu da bakımcının yolu da aynı resmî istemcidir; bu
  yüzden bakımcının dağıttığı yeterlik kayıtları yabancıda da geçerli olabilir (model kimliği, düşünme düzeyi ve
  istemci sürümü eşleşiyorsa).
- **İzni ajan kendisi verebilir** (A6). İzin sorusu istemcinin formunda ya da işletim sistemi penceresinde
  gösterilmeli. Doğrudan kanal yoksa izin verilmemiş sayılır ve 3. yola (ajanın yazdığı formül) düşülür.
- **"Her şeyi üstlenir" K4 ile çakışabilir.** K4, Rigor'un eksik değeri kendisinin doldurmasını yasaklıyor; sahip de
  metinsel yolda üç seçenekli onay ekranını kararlaştırdı.
- **Maliyet belirsiz.** Başsız kullanımın ayrı bir krediden düşüp düşmediği doğrulanmadı. İzin metni çağrıların
  kullanıcının hesabından harcayacağını ve tahmini çağrı sayısını söylemeli.
- **İç içe çağrı.** Kullanıcının ajanı Rigor'u çağırır, Rigor aynı istemciyi başsız çağırır. Başsız çağrı Rigor'u
  yeniden yüklerse döngü oluşur; tasarım §6.4'teki yalıtım (araçsız, MCP'siz, boş dizin) burada zorunludur.
- **`.env` okumak fazla geniş bir izindir.** Bir `.env` dosyasında Rigor'la ilgisi olmayan sırlar da bulunur.
- **Sağlayıcı koşulları.** Resmî istemciyi başka bir aracın başsız çağırmasına her sağlayıcının izin verdiği
  doğrulanmadı; tasarıma yazılmadan önce birincil metinler okunmalı.

#### Tasarımcı okuması ve önerileri (sahip onaylamadı)

- **Devralma, akışın kontrolüdür; kullanıcının yargısı değildir.** Devralma izni verilse de Rigor eksik değerde durup
  sorar (K4) ve metinsel yolda üç seçenekli onay ekranını gösterir.
- **İzin metni dört şeyi söyler:** hangi istemcilerin çağrılacağı; tahmini çağrı sayısı ve bunun kullanıcının
  hesabından harcayacağı; problem metninin o istemcinin sağlayıcısına gideceği; iznin bu görev bitince sona ereceği.
- **Görevin sonu** sonuç kutusunun ve raporun yazılmasıdır.
- **Rigor proje `.env` dosyalarını hiç okumaz.** Anahtar yalnızca Rigor'un kendi ayar komutuyla ya da adı belli ortam
  değişkenleriyle verilir (ayrıntı soru 4'te).

### Soru 4 (kapandı): İzinler ve anahtarlar ne zaman ve nasıl istenecek?

Soru 3'ten gelen sahip kararları: önce ajan istemcisini kullanma izni istenir; API anahtarı son seçenektir.

Red Team notları:

- **Kalıcı izin kolaylık sağlar ama görünmez harcamaya yol açar.** Bir kez verilip hatırlanan devralma izni, sonraki
  her ajan çağrısının kullanıcı görmeden hesabından harcamasına izin verir.
- **Her görevde sormak güvenlidir ama toplu kullanımı yorar.** Sahibin kendi kullanımı (aynı şablonla çok sayıda
  hesap) her seferinde pencere açılmasını kaldırmaz.
- **Anahtar MCP formuyla istenemez** (MCP belirtimi; önceki turda doğrulandı). Anahtar ajanın konuşmasına da girmemeli.

#### Sahip kararı: izin süresi ve harcama satırı (2026-11-10)

- **İzin kayan bir süreyle geçerlidir.** Bir iş bittikten sonra 15 dakika içinde yeni iş başlatılmazsa Rigor izni
  yeniden sorar. 15 dakika kesin değil; tasarımcıdan daha iyi bir süre önerisi istendi.
- **Her iş bitince kısa bir çıktı verilir:** işin bittiği ve, okunabiliyorsa, kaç token harcandığı. Bu satır raporda
  da yer alır.

#### Red Team: izin süresi

- **Yalnızca boşta kalma süresi üst sınır koymaz.** Döngüye girmiş bir ajan 15 dakikadan sık iş başlatırsa izin hiç
  bitmez. Kullanıcının görmeden harcama yaptığı durum tam budur.
- **İş sonu satırı harcamayı engellemez, bildirir.** Satır ajanın çıktısında kalırsa kullanıcı görmeyebilir.
- **İznin kapsamı tanımsız.** Bir projede verilen izin, 15 dakika içinde başka bir projede ya da başka bir ajanda da
  geçerli mi? Tek problem için verilen izin 200 işlemlik bir belgeyi de kapsar mı?
- **Token sayısı her istemciden okunamayabilir.** Okunan sayı da istemcinin kendi beyanıdır.

#### Tasarımcı önerisi: süre (sahip istedi)

**15 dakikayı koru, yanına toplam çağrı bütçesi ekle.** İzin hangisi önce gelirse onunla biter.

- *Neden daha kısa değil:* sonucu okuyup bir değeri değiştirip yeniden çalıştırmak dakikalar sürer. 5 dakikalık
  süre bu olağan düşünme aralığında izni düşürür; sık sorulan izin okunmadan onaylanır.
- *Neden daha uzun değil:* burada işi başlatan insan değil ajandır. Kullanıcı masadan kalktıktan sonra iznin açık
  kaldığı süre, ajanın habersiz harcayabildiği süredir.
- *Emsal:* `sudo` parola sormadan önce yaygın dağıtımlarda 15 dakika bekler (ikincil kaynaklar; bazıları 5 dakika
  diyor). NIST SP 800-63B-4 oturumlar için iki sınırı birlikte ister: hareketsizlik süresi ve toplam süre. Burada
  toplam sınırın karşılığı bütçedir, çünkü zarar süre değil harcamadır.
- *Bütçe:* izin ekranında söylenen çağrı sayısıdır ve izin süresince birikimli sayılır; her işte sıfırlanmaz.
  Bütçe dolunca Rigor durur ve yeniden sorar.

#### Tasarımcı önerileri: diğerleri (sahip onaylamadı)

- **İzin proje dizinine ve onaylanan istemcilere bağlıdır.** Başka dizinde ya da başka istemci için yeniden sorulur.
- **İş sonu satırı üç şey söyler:** bu işte kaç çağrı ve (okunabildiyse) kaç token; bu izinle toplam; kalan bütçe.
  Token okunamadıysa "token sayısı okunamadı" yazar; tahmin yazmaz. Para tutarı hesaplanmaz.
- **İş sonu satırı ajanı atlayan kanaldan da gösterilir** (işletim sistemi bildirimi), böylece ajan raporu özetlese
  de kullanıcı harcamayı görür.
- **Süre ve bütçe ayarlanabilir, ama yalnızca Rigor'un kendi ayar komutuyla;** ajan ya da alan paketi yükseltemez.
- **Anahtar ne zaman istenir (sahibin "son seçenek" kararının uygulaması):** kurulumda sorulmaz. Yalnızca üç yerde
  seçenek olarak görünür: `rigor doctor` çıktısında; sonuç kutusunun "bu sonuç nasıl yükseltilir" satırında;
  kullanıcı kendisi isterse. Anahtar Rigor'un kendi komutuyla girilir; MCP formuyla ya da ajan konuşmasıyla istenmez.

### Soru 5 (açık bırakıldı): Toplayıcı üzerinden gelen yanıt en üst etikete katkı verebilir mi?

Önceki kararlardan çıkanlar:

- Yeterlik kaydı erişim yoluna bağlıdır (soru 2). Toplayıcı ayrı bir yoldur; o yoldan ölçülmüş kaydı olmayan
  yapılandırma en üst etikete katkı vermez.
- Soru 1'de gösterilen rapor bir adaptör sözleşmesi öneriyor: model ve sağlayıcı sabit, yedekleme kapalı, istem
  dönüşümü kapalı, yanıt önbelleği kapalı, dönen model ve rota kayıtlı; belirsiz adaptör katkı vermez.
- Anahtar son seçenek olduğu için (soru 3) toplayıcı da son seçeneğin içindedir.

Red Team notları:

- **Tek anahtarla çok aile.** Anahtar vermeye razı olan yabancı için tam heyete en ucuz yol toplayıcıdır.
- **Üç üye de aynı aracıdan geçer.** Yönlendirme, istem dönüşümü ve önbellek üçü için ortaktır; aracının bir
  davranışı üç üyeyi birden etkiler.
- **Model kimliği aracının beyanıdır.** Dönen model adı ağırlıkların kanıtı değildir.
- **Ölçüm aracıyı kısmen kapsar.** Kayıt aynı yoldan ölçüldüğü için aracının o günkü etkisi ölçüme dahildir. Aracı
  davranışını sonradan değiştirirse kayıt bunu görmez.

#### Sahip kararı: araştır ve açık bırak (2026-11-10)

Sahip bu soruda fikri olmadığını söyledi: araştırma yapılacak, soru dosyada açık kalacak.

#### Araştırma: OpenRouter'ın birincil belgeleri (2026-11-10'da okundu)

| Konu | Belgede yazan | Rigor için anlamı |
| --- | --- | --- |
| Varsayılan yönlendirme | Sağlayıcılar fiyat, hız, gecikme ve güvenilirliğe göre ağırlıklandırılır; her istek ağırlıklı rastgele bir sağlayıcıya gider | Aynı model adı istekten isteğe farklı sağlayıcıda çalışır |
| `allow_fallbacks` | Varsayılan `true`. `order` ile birlikte `false` yapılırsa istek tek sağlayıcıya sabitlenir, o başarısızsa hata döner | Sabitleme mümkün, ama varsayılan değil |
| `require_parameters` | Varsayılan `false`: parametreyi desteklemeyen sağlayıcı isteği alır ve parametreyi yok sayar | Düşünme düzeyi gibi bir ayar sessizce düşebilir |
| `quantizations` | Sıkıştırma düzeyine göre filtre (`int4` … `fp32`, `unknown`); varsayılan filtre yok | Aynı model farklı sıkıştırmayla sunulabilir |
| Bağlam sıkıştırma | 8.192 token ve altı bağlamlı uç noktalarda varsayılan açık; istemin ortasından mesaj siler ya da kırpar; istek başına kapatılabilir | Problem metni kayıpla kısalabilir |
| Model yedeği | `models` dizisi verilirse hata durumunda sıradaki modele geçer; kullanılan model yanıtın `model` alanındadır. Dizi verilmediğinde model değişip değişmediği belgede yazmıyor | Dizi kullanılmamalı; dönen model her yanıtta denetlenmeli |
| Üretim kaydı | `model`, `provider_name`, `upstream_id`, her denemeyi listeleyen `provider_responses`; token ve katman bilgisi "sağlayıcının bildirdiği" diye etiketli | Denetim kaydı var; doğrulandığı yazmıyor |
| Yanıt önbelleği (önceki tur) | Başlık ya da ön ayarla açılır; isabet yanıt başlığında bildirilir; her isabette yeni üretim kimliği verilir | Kapalı tutulmalı; kimlik yeni üretim kanıtı değil |
| Veri politikası | Eğitim yapan sağlayıcılara yönlendirme hesap ayarıdır; ücretli ve ücretsiz modeller için ayrı. `data_collection: deny` ve `zdr` istek ayarları var. OpenRouter'ın kendi saklama politikası bu sayfada yazmıyor | Kullanıcıya söylenmeli (K4, A2) |

İkincil kaynaklardan: ücretsiz modellerde sınır hesap genelinde günde 50 istek, 10 dolarlık kredi alınmışsa 1.000. Bu
doğruysa 400 çağrılık bir yeterlik ölçümü ücretsiz hesapta 8 gün sürer (soru 2'deki maliyet bulgusunu ağırlaştırır).

#### Araştırma: aynı model adı aynı model mi?

- **Gao, Liang, Guestrin (arXiv 2410.20247):** dokuz ticari sağlayıcıda dört Llama modelinin 31 uç noktasını
  Meta'nın yayımladığı referans ağırlıklarla karşılaştırdı; 31'in 11'i sapıyor (2024 yazı). Olası nedenler:
  sıkıştırma, budama, filigran, yanlış uygulanmış çözümleme ayarı.
- **Cai vd. (arXiv 2504.04715):** çıktıya bakarak model ikamesini yakalamanın sınırlı olduğunu gösteriyor. Sağlayıcı
  isteklerin bir kısmını ikame modele yönlendirebilir ya da denetim sorgusunu tanıyıp gerçek modelle cevaplayabilir.
  Güvenilir yol olarak donanım tabanlı güvenli yürütme ortamını öneriyor.

Sonuç: "aynı model adı, aynı model" varsayımı ölçümle çürütülmüş durumda, ve küçük bir sentinel testi bunu güvenle
yakalayamaz.

#### Bu bulgulardan çıkanlar (tasarımcı)

- Toplayıcı tek aracı değil, iki katmandır: toplayıcı ve arkasındaki sağlayıcı. Yeterlik anahtarı "toplayıcı +
  sabitlenmiş sağlayıcı + sıkıştırma düzeyi" olmalı. Sabitlenmemiş bir toplayıcı çağrısı her seferinde farklı bir
  yapılandırmadır ve hiçbir kayıtla eşleşemez.
- OpenRouter için en üst etikete aday bir çağrının taşıması gerekenler: tek sağlayıcılı `order` ve
  `allow_fallbacks: false`; `require_parameters: true`; sabit `quantizations`; bağlam sıkıştırma kapalı; yanıt
  önbelleği kapalı; `models` dizisi yok. Yanıtta `model`, üretim kaydında `provider_name` beklenenle aynı olmalı ve
  `provider_responses` tek deneme göstermeli.
- Bütün bu denetimler aracının beyanına dayanır.
- Başka toplayıcılar (LiteLLM, Vercel AI Gateway, Cloudflare AI Gateway, Portkey) incelenmedi. OmniRoute araştırma
  notları §11'de incelenmişti.

#### Açık soru: üç üye de tek toplayıcıdan gelirse sonuç ne alır?

Karar verilmedi. Seçenekler:

- **A.** Toplayıcı yolu en üst etikete hiç katkı vermez. Toplayıcı çalışır; sonuç sertifikaya göre `CERTIFIED` ya da
  `CROSS_VALIDATED` alır.
- **B.** Aynı toplayıcıdan en çok bir üye sayılır; diğer ikisi başka yoldan gelmelidir.
- **C.** Üçü de sayılır; koşul: her üye farklı bir arka sağlayıcıya sabitlenmiş, her birinin o yola özgü yeterlik kaydı
  var, her yanıtta yukarıdaki denetimler geçmiş ve heyet kabulü aynı yoldan ölçülmüş.

Kararı belirleyecek ölçüm: aynı yapılandırmanın doğrudan sağlayıcıdan ve toplayıcı üzerinden yeterlik sonuçlarının
karşılaştırılması. Bu ölçüm yapılmadan C'nin güvenli olduğu söylenemez.

Tasarımcı eğilimi (karar değil): ölçüm yapılana kadar A. Gerekçe A1: şüphede etiket düşürülür.

### Soru 6 (cevaplandı): Hepsi yetişmezse ne bekler?

Bugünkü yol haritası: F1 çekirdek, F2 roket fiziği, F3 Red Team ve doğal dil, sonra F4–F9. Hedef Şubat 2027 sonu
(K16). Bugün 2026-11-10; hedefe yaklaşık 16 hafta var ve kod sıfır.

Bugünkü kararların yol haritasına eklediği işler:

- Dört etiketli sözleşme ve tasarımdaki 12 sıra ifadesinin yeniden yazımı.
- Dar bir bağımsız rasyonel denetleyici (`CERTIFIED` için).
- LLM kullanmayan katı ifade ayrıştırıcısı (doğrudan yol için).
- `rigor solve` komutu ve tek kaba MCP aracı; ajana yönelik kullanım dosyası.
- İzin ekranı, birikimli bütçe, iş sonu harcama satırı ve bildirim.
- Başsız ajan istemcisi adaptörleri (bugünkü planda F3'te).
- Yeterlik sistemi: kayıt şeması, şablon üretici, değerlendirici kabul paketi, 300 + 100 soruluk ölçüm, kayıt dağıtımı.
- Heyet kabulü (100 yeni görev).
- Belge okuyucu (PDF/DOCX), önerildiyse.

Red Team:

- **"Heyet" artık tek parça değil.** İki ayrı iş var. (a) Tek formülasyonlu doğal dil yolu: izin, başsız istemci,
  denklem çıkarma, üç seçenekli onay. (b) Üç yeterlikli üyeli heyet, yeterlik ölçümü ve heyet kabulü.
- **(a) hedef kullanıcının bütün ilk deneyimidir** ve `KANITLANDI` gerektirmez. Bugünkü planda F3'te; yani F1 ve F2
  bittiğinde yabancı yalnızca doğrudan yolu kullanabilir, o da katı ayrıştırıcı yazılırsa.
- **(b) en pahalı parçadır** ve yalnızca en üst etiketi açar.
- **F2 (roket) sahibin kendi kullanımıdır** ve doğal dile ihtiyaç duymaz; denklemler kurucu API ile verilir.
- **Takvim.** Dokuz faz ve yukarıdaki ekler 16 haftaya sığmayabilir. Neyin bekleyeceği sahibin kararıdır.

#### Sahip kararı: erteleme kuralı (2026-11-10)

Hedefe yetişmezse sahibin kendi kullanımında en az ihtiyaç duyduğu iş bekler. Sahip her şeyin yetişeceğini düşünüyor.

Sahibin kendi kullanımları (tasarım §1): roket hesapları (R1–R11, A2), kripto botunun matematiği, Sentinax'ın canlıya
alma kontrolü. Bu kullanımların hiçbiri `KANITLANDI` gerektirmiyor: R5 ve R6 zaten en fazla `CROSS_VALIDATED`;
Sentinax kapısı "en az `CROSS_VALIDATED`" istiyor (§5.2). Buna göre tasarımcının türettiği erteleme sırası
tam tarama bölümünde.

### Soru 3'teki "istemciyi çağırma" kararının birincil kaynak denetimi (2026-11-10)

Resmî belgeler okundu (ayrıntı ve bağlantılar Kaynaklar bölümünde):

| Konu | Belgede yazan | Etkisi |
| --- | --- | --- |
| Anthropic hukuki sayfası | "Anthropic does not permit third-party developers to offer Claude.ai login into their own applications" ve "route requests through Free, Pro, Max, or Ultra plan credentials on behalf of their users". Ürün geliştirenler, Agent SDK kullananlar dahil, API anahtarı kullanmalı. Son kullanıcının değiştirilmemiş Claude Code'a kendi aboneliğiyle girmesi engellenmiyor | Rigor'un kullanıcının abonelikle giriş yapmış `claude` istemcisini başsız çağırması, "kullanıcılar adına abonelik kimliğiyle istek yönlendirme" sayılabilir. Karar bu haliyle sağlayıcı koşullarıyla çelişme riski taşıyor |
| Claude Code başsız mod | `-p` belgelenmiş; JSON çıktısında `total_cost_usd` var ve "istemci tarafı tahmin" diye etiketli. Yalın modda (`--bare`) abonelik girişi okunmuyor, API anahtarı gerekiyor | Harcama satırı için sayı okunabilir, ama faturanın kendisi değil |
| Claude Code MCP istemcisi | Elicitation (form ve URL) ilan ediliyor; başsız modda yanıtlanmayan elicitation iptal ediliyor. Sampling belgede geçmiyor | Sampling yolu (2. yol) Claude Code'da yok sayılmalı |
| Codex `exec` | Betik ve CI için belgelenmiş; `turn.completed` olayında `usage` (girdi, önbellek, çıktı, akıl yürütme token'ları). ChatGPT oturumuyla CI kullanımı için "herkese açık ya da açık kaynak depolarda kullanmayın" uyarısı var | Token sayısı okunabilir. Uyarı, açık kaynak bir aracın ChatGPT oturumunu otomasyonla kullanmasına dair belirsizlik ekliyor |
| Gemini CLI başsız mod | `-p` ve `--output-format json` belgelenmiş; `stats` alanı token kullanımı veriyor. Veri kullanımı sayfası 404 döndü | Eğitim politikası doğrulanamadı |
| Groq | Sınırlar kuruluş düzeyinde; tabloda `gpt-oss-120b` için 30 istek/dk, 1.000 istek/gün, 8.000 token/dk, 200.000 token/gün. Sayfa tablonun "Developer" planı için olduğunu söylüyor; ücretsiz plan rakamı okunamadı | Araştırma notları §13'teki rakamlar ücretsiz plan için doğrulanamadı |

Bu bulgu, soru 3'teki "izinle kurulu istemciyi çağır" kararını yeniden açıyor (tam tarama bölümünde B-1).

### Yerel ortam

Sahibin makinesindeki istemci, model ve hesap ayrıntıları `docs/private/` altına taşındı. Tasarım için genel sonuçlar:

- Düşünme düzeyi sözlüğü istemciden istemciye değişiyor; birinde düzey bayrağı hiç yok.
- Kurulu erişim, tasarım K14/K15'in varsaydığı "üç abonelik, üç resmî istemci" tablosuyla birebir örtüşmüyor.

## Hedefler ve hedef olmayanlar

- **Kapsamdaki hedefler:** tasarım belgesinin "Kayıt" bölümündeki eşleme tablosunda listelenen bütün yerlerinin
  revizyonu; yol haritası, Faz 1 planı ve README'nin buna uydurulması; `CERTIFIED` etiketi ve kutu biçimi; yeterlik
  kaydı ve ölçüm sözleşmesi; ilk çalıştırma akışı; izin, bütçe ve anahtar kuralları; toplayıcı koşulu; erteleme sırası.
- **Kapsam dışı (tasarımcı önerisi; sahip onaylamadı):** kod yazmak, bağımlılık kurmak; Türkçe kutunun
  kullanıcılarla sınanması; iddia–kanıt grafiği; tam TUF dağıtımı; otomatik risk sınıflayıcı; genel "confidence
  sequence" altyapısı. DeepSeek Harness'e özel entegrasyon da burada sayılıyordu; bu sahibin karar 6'sını daraltır,
  bu yüzden açık nokta A-9'a taşındı.
- **Ertelenenler:** tam taramadaki erteleme sırası (tasarımcı önerisi; S-17'nin uygulaması).

## Tartılan alternatifler

"Eleyen" sütunu kimin elediğini söyler. Raporlar: `Soru1-1` (birinci ve ikinci aşama raporu), `Soru1-2` (üçüncü ve
dördüncü aşama), `Soru2-1`. Dosya adları (`docs/research/external-reports/`): `Soru1-1` =
`2026-11-10-soru1-etiketler-1.md`, `Soru1-2` = `2026-11-10-soru1-etiketler-2.md`, `Soru2-1` =
`2026-11-10-soru2-yeterlik.md`. Sahip bu raporları cevap olarak gösterdi; kalem kalem onayı yok (Kayıt: rapor önerileri).

| Alternatif | Soru | Eleyen | Gerekçe | Gerekçe hâlâ geçerli mi |
| --- | --- | --- | --- | --- |
| Mevcut `CROSS_VALIDATED` içinde ek şart satırı | 1 | Rapor `Soru1-2` | Etiket yapılmamış bir çapraz doğrulamayı söyler | Evet |
| `PROVEN`'ı yalnızca matematik iddiasının etiketi yapmak | 1 | Rapor `Soru1-2`, `Soru1-1`'in önerisini geri çekti | Karar 5 ile çelişir; fark edilmemiş formülasyon hatası en üst etiketle yayımlanır | Kısmen: karar 5'in yeni metni (Ö-2-1) onaylanırsa ilk gerekçe düşer, ikincisi kalır |
| Tam iddia–kanıt grafiği, `RECOMPUTED`, ayrı yayın durumu | 1 | Rapor `Soru1-2` | v1 için ağır | Evet |
| Ölçüt olarak fiyat | 2 | Sahip (S-9) | Aynı model iki planda aynı cevabı verir; zayıf ama ücretli model en üst etiketi açar | Evet |
| Tarihli "üst düzey modeller" listesi | 2 | Sahip (S-8) | Eskir; Rigor'un ölçmediği bir şeye dayanır | Evet |
| Bir ya da iki yeterlikli üye | 2 | Rapor `Soru2-1` | Zorunlu üyelerden biri ölçülmemiş kalır | Belirsiz: üç kaydın ikiden güvenli olduğu ölçülmedi (soru 2, madde 7) |
| Göreve göre değişen üye sayısı | 2 | Rapor `Soru2-1` ertelendi | Risk sınıflayıcı güven tabanını büyütür | Evet; ertelenmiş, elenmemiş |
| Tek aşamalı sıfır tolerans | 2 | Tasarımcı (Ö-2-2) | İyi modelleri sık düşürür | Evet; ayrıca M-13 |
| Yalnızca "Doğru / Yanlış" iki seçenek | 3 | Sahip (S-11) | Bilmeyen kullanıcı "Doğru"ya basar | Evet; ama "bilmiyorum" B-1'i doğurdu |
| Yalnızca MCP içinde kalmak | 3 | Sahip (S-13) | Tam devralma olmaz | B-5 yüzünden yeniden açık |
| Ayrı bir Rigor ajanı yazmak | 3 | Tasarımcı | API anahtarı ister; anahtarsız yabancıya uymaz | Evet |
| Ajan aracılı onayı "bekle ya da reddet"e sertleştirmek | 1 | Tasarımcı (Ö-1-7) | Elicitation'sız istemcileri bant dışı onaya mecbur eder | Belirsiz: B-1'deki `DELEGATED` önerisi ters yönde |
| Hatırlanan kalıcı izin | 4 | Tasarımcı | Görünmez harcama | Kısmen: M-9 sert sınırlı bir politikayı öneriyor |
| 5 dakika ya da daha uzun izin süresi | 4 | Tasarımcı (Ö-4-1) | Kısa süre okunmadan onaylatır; uzun süre habersiz harcatır | Evet |
| Toplayıcı seçenekleri A, B, C | 5 | Karar yok | Ölçüm gerekiyor | Açık (A-4) |

## Kayıt: kararlar ve sonraki adımlar

Bu bölüm bütün kararların tek listesidir. Durum sözlüğü:

- **Sahip kararı:** sahibin söylediği; bağlayıcı. Daha yeni tarihli bir sahip kararı eskisinin yerini alır; eski
  satırda "yerine" yazar. Tasarım belgesine işlenirken bu kural tasarımın okuma kuralına eklenecek (bugünkü kural sahip
  kararlarını "değiştirilemez" sayıyor ve bir yenisinin eskisini nasıl değiştireceğini söylemiyor).
- **Rapor önerisi:** sahibin cevap olarak gösterdiği dış raporun önerisi; kalem kalem sahip onayı bekler. Tasarımın
  okuma kuralında böyle bir kategori yok; işlenirken her kalem ya sahip kararı ya tasarımcı kararı olacak.
- **Tasarımcı önerisi:** bu belgeyi yazanın önerisi; sahip onayı bekler.
- **Açık nokta:** henüz karar yok.

### Sahip kararları

| No | Karar | Tarih | Durum |
| --- | --- | --- | --- |
| S-1 | Hedef kullanıcı GitHub'dan kuran bir yabancı; aboneliği olmayabilir | 2026-11-10 | Geçerli. Çelişki: S-17 (A-1) |
| S-2 | Önce matematik kütüphaneleriyle analiz, sonra ücretsiz ve ücretli API listesinden hakem heyeti | 2026-11-10 | Kısmen S-11 ile değişti: metinsel yolda formülü önce LLM yazar |
| S-3 | Ücretli API zorunlu değil; kullanıcıda varsa istenir | 2026-11-10 | S-14 ile daraldı: anahtar son seçenek, kurulumda sorulmaz (Ö-4-6) |
| S-4 | Toplayıcılar listeye girebilir | 2026-11-10 | Geçerli; en üst etikete katkısı açık (A-4) |
| S-5 | Yalnızca ücretsiz modellerle doğrulanan sonuç `KANITLANDI` almaz | 2026-11-10 | S-9 ile çelişiyor; yeni metin Ö-2-1 onay bekliyor. Onaya kadar eski metin geçerli |
| S-6 | DeepSeek Harness işe yararsa kullanılır | 2026-11-10 | Bu belgede incelenmedi. Gösterilen rapor (`Soru1-2` §11): çekirdek bağımlılığı değil, sonra opsiyonel istemci (A-9) |
| S-7 | Ücretsiz modellere güvensizliğin gerekçesi kota ve çözme kapasitesi | 2026-11-10 | Bilgi; kota kanıtı etkilemez, yalnızca süreyi (soru 2) |
| S-8 | Rigor'un yeterlik seti modelleri sınar; kayıt model ve düşünme düzeyiyle tutulur | 2026-11-10 | Geçerli |
| S-9 | Güçlü model ücretsiz katmanda verilirse katkısı aynı sayılır; bekleme uzayabilir | 2026-11-10 | Geçerli |
| S-10 | Depoda bir yeterlik kayıt dosyası olur; önce sahibin elindeki modellerle ilerlenir | 2026-11-10 | Geçerli; güvenliği B-4 |
| S-11 | İlk çalıştırma: ajana "çöz" denir, Rigor akışı yönetir; doğrudan işlem çözülür; metinde denklemler çıkarılıp Doğru / Yanlış / Bilmiyorum seçenekleriyle sunulur | 2026-11-10 | Geçerli; uygulanışı B-1, M-2, M-7 |
| S-12 | "Bilmiyorum" denirse Rigor yine çözer ve "sizin verdiğiniz matematiksel işlemin sonucu bu" notunu düşer | 2026-11-10 | Geçerli; çelişki B-1 (A-2); not metni Ö-3-4 |
| S-13 | Rigor kurulu ajan istemcisini izinle çağırabilir; ayrıca "işlem bitene kadar devralma" izni istenir | 2026-11-10 | Sağlayıcı koşullarıyla çelişme riski: B-5 (A-3) |
| S-14 | API anahtarı istemek ya da `.env` okumak son seçenek | 2026-11-10 | Geçerli; `.env` için Ö-3-10 |
| S-15 | İzin, iş bittikten sonra 15 dakika yeni iş başlamazsa yeniden sorulur (15 dakika geçici); her iş sonunda harcama satırı | 2026-11-10 | Geçerli; süreye tasarımcı cevabı Ö-4-1 |
| S-16 | Soru 5 araştırılsın ve açık bırakılsın | 2026-11-10 | Yapıldı (A-4) |
| S-17 | Hedefe yetişmezse sahibin kendi kullanımında en az ihtiyaç duyduğu iş bekler; sahip her şeyin yetişeceğini düşünüyor | 2026-11-10 | Geçerli. Tarama: yetişmiyor (B-6) |
| S-18 | v1'de yabancı kullanıcının ihtiyacı ile sahibin kendi kullanımı çatışırsa sahibin kullanımı önce gelir | 2026-11-11 | Geçerli. A-1'i kapattı; erteleme sırasının "sahip önce" sürümü uygulanır. S-1 hedef kullanıcı olarak kalır |
| S-19 | "Takvime gerek yok" | 2026-11-11 | Geçerli. Tasarımcı okuması: takvim ve kontrol noktası yapılmaz (B-6'nın kontrol noktası önerisi düştü; K16'nın "ayrıntılı takvim yapılmaz" kuralı korunur). A-5'e cevap sayılmadı |
| S-20 | v1'de `PROVEN` kapalı | 2026-11-11 | Geçerli. A-5'i kapattı |
| S-21 | v1 kabul hesapları: roket R1–R11; bot ve Sentinax için B1 ve B2 | 2026-11-11 | Geçerli. A-13'ü kapattı; finans envanteri F4'te formül formül yazılır |
| S-22 | Lean (K26) v1'den ertelenir | 2026-11-11 | Geçerli. A-12'yi kapattı; F12 |
| S-23 | v1'de doğrudan matematik (katı ayrıştırıcı) ve kurucu API; doğal dil yolu v1'den sonraki ilk faz | 2026-11-11 | Geçerli. A-11'i kapattı (PDF/DOCX v1'de yok; F9) |
| S-24 | "Bilmiyorum": çöz; etiket yalnızca çıkarılan denklemi kapsar; kutu "tanımı kullanıcı onaylamadı" yazar; eksik değerde asla geçerli değil | 2026-11-11 | Geçerli. A-2'yi kapattı |
| S-25 | Başsız istemci v1'de kapalı; sonra sağlayıcı başına açma bayrağı | 2026-11-11 | Geçerli. A-3'ü kapattı; F6 |
| S-26 | Aynı hesaptaki tam kabuk erişimli ajana karşı garanti verilmez; README ve raporda açık yazılır | 2026-11-11 | Geçerli. A-14'ü kapattı |
| S-27 | Platform: macOS ve Linux; Windows sonra | 2026-11-11 | Geçerli. A-8'i kapattı; Windows F14 |
| S-28 | Kayıttaki bütün öneriler toplu kabul (Ö-2-1 dahil) | 2026-11-11 | Geçerli. İkinci dış taramada düzeltilen maddelerin düzeltilmiş hali kabul edildi; bir sahip kararıyla çelişen öneride sahip kararı geçerli. S-5'in yerine Ö-2-1 |
| S-29 | Geliştirme araçları varsayılan olarak yerel ve ağsız; model çağıran özellikler açık izinle | 2026-11-11 | Geçerli |
| S-30 | Depoda yalnızca belgelenmiş, isteğe bağlı araç listesi; proje ayarıyla otomatik eklenti, kanca ya da MCP yok | 2026-11-11 | Geçerli. `.claude/settings.json`'daki eklentilerin çıkarılması ayrıca onay bekliyor (mimari T-10) |
| S-31 | Red Team incelemeleri yalnızca kritik faz geçişlerinde; inceleme ajanları daha ucuz modelle; birleştirmeyi ana ajan yapar | 2026-11-11 | Geçerli. Kapılar K-1 … K-4 (faz planı §2) |
| S-32 | Mimari `docs/design/`, faz planı `docs/plans/` altına; eski tasarıma "yerini aldı" notu; commit için ayrıca onay | 2026-11-11 | Yapıldı: `docs/design/2026-11-11-rigor-mimari.md`, `docs/plans/2026-11-11-rigor-faz-plani.md` |

### Rapor önerileri (kalem kalem onay bekliyor)

| No | Öneri | Kaynak |
| --- | --- | --- |
| R-1 | Dört etiket: `PROVEN`, `CERTIFIED`, `CROSS_VALIDATED`, `REFUSED`; `PROVEN` tam süreç etiketi; Faz 1'de `PROVEN` yok; dört alanlı özet kutusu | `docs/research/external-reports/2026-11-10-soru1-etiketler-2.md` (kısa adı `Soru1-2`) |
| R-2 | Üç zorunlu üyenin üçü yeterlikli, en az iki aile, 100 görevlik heyet kabulü | `Soru2-1` |
| R-3 | Ölçülen nesne yapılandırmadır; kayıt başka yola, ayara ya da profile taşınmaz | `Soru2-1` |
| R-4 | 300 ölçüm + 100 stres örneği, 50 soruluk pilot; sıfır kritik hata; %80 ve %90 alt sınırları | `Soru2-1` |
| R-5 | Değerlendirici model ölçümünden önce sınanır | `Soru2-1` |
| R-6 | Kayıt 30 gün geçerli; bilinen değişiklikte hemen düşer; bakımcı ve yerel katman; imza tek başına yetmez | `Soru2-1` |
| R-7 | Kayıtsız üye danışmandır; ayrışma oy çokluğuyla kapatılmaz | `Soru2-1` |
| R-8 | Faz yerleşimi: kayıt şeması F1, ölçüm F3 öncesi, heyet kapısı F3 (M-4 bunun döngüsel olduğunu gösterdi) | `Soru2-1` |

### Tasarımcı önerileri (onay bekliyor)

| No | Öneri | Yer |
| --- | --- | --- |
| Ö-1-1 … Ö-1-9 | Soru 1'deki dokuz madde (Türkçe ad, onay kuralı, denetleyici sınırı, birim tablosu, Faz 1'de `CERTIFIED` yok, sıra ifadeleri, ajan onayı, iki not) | Soru 1 |
| Ö-2-1 | Karar 5'in yeni metni: `KANITLANDI` için bütün üyelerin geçerli yeterlik kaydı; erişimin ücretli ya da ücretsiz olması tek başına yeterliği değiştirmez | Soru 2 |
| Ö-2-2 | İki aşamalı kabul planı | Soru 2, madde 1 |
| Ö-2-3 | Sınırların tabaka başına raporlanması; eksik problem payının büyütülmesi | Soru 2, madde 2 |
| Ö-2-4 | Sabitlenebilen modellerde daha uzun kayıt süresi | Soru 2, madde 4 |
| Ö-2-5 | Kayıt dosyasını komut yazar; satırda tam model kimliği; iki katman; dosyada yoksa tik yok; adı "yeterlik kayıtları" | Soru 2 |
| Ö-2-6 | Ezbere karşı: problem değil şablon; eşli tuzaklar; gizli pay; tarihli tik | Soru 2 |
| Ö-3-1 | "Doğrudan" mekanik tanım: katı ayrıştırıcıdan bütünüyle geçen girdi | Soru 3 |
| Ö-3-2 | Doğrudan yolda onay yerine yankı | Soru 3 |
| Ö-3-3 | "Çöz" çözüm kümesi döndürür (B-9'daki tamlık şartıyla) | Soru 3 |
| Ö-3-4 | İki ayrı not metni (doğrudan yol, metinsel yol) | Soru 3 |
| Ö-3-5 | Üç seçenek üç ayrı kayıt durumu; sade anlatım denklemle birlikte | Soru 3 |
| Ö-3-6 | Toplu işlerde tek onay ekranı | Soru 3 |
| Ö-3-7 | Ajana yönelik kullanım dosyası | Soru 3 |
| Ö-3-8 | Tek kaba `rigor_solve` aracı ve `rigor solve` komutu (M-2'deki iş modeliyle) | Soru 3 |
| Ö-3-9 | Devralma akışın kontrolüdür; K4 ve onay ekranı kalır | Soru 3 |
| Ö-3-10 | İzin metninin dört maddesi; Rigor proje `.env` dosyalarını hiç okumaz | Soru 3 |
| Ö-3-11 | LLM yollarında 2. ve 3. sıranın yeri (sampling, ajanın yazdığı formül) | Soru 3 |
| Ö-3-12 | İzin ekranı kurulu bütün istemcileri saysın | Soru 3 |
| Ö-3-13 | Yeni §1.1 metni: "Her sonuç yanında yazan tanıma göre doğrulanmıştır; tanımı kimin yazdığı ve kimin onayladığı sonuçla birlikte gösterilir" | Soru 3 |
| Ö-4-1 | 15 dakikayı koru, yanına birikimli çağrı bütçesi | Soru 4 |
| Ö-4-2 | İzin proje dizinine ve istemcilere bağlı | Soru 4 |
| Ö-4-3 | İş sonu satırının üç bilgisi; token okunamazsa "okunamadı" | Soru 4 |
| Ö-4-4 | İş sonu satırı işletim sistemi bildirimiyle de gösterilir | Soru 4 |
| Ö-4-5 | Süre ve bütçe yalnızca Rigor'un ayar komutuyla değişir (B-4 bunun yetmediğini gösterdi) | Soru 4 |
| Ö-4-6 | Anahtar kurulumda sorulmaz; yalnızca `rigor doctor`, kutunun "nasıl yükseltilir" satırı ve kullanıcı isteyince | Soru 4 |
| Ö-5-1 | Toplayıcı yeterlik anahtarı: toplayıcı + sabitlenmiş sağlayıcı + sıkıştırma düzeyi; OpenRouter çağrı sözleşmesi | Soru 5 |
| Ö-T | Tam taramadaki bütün "Öneri"ler: B-1 … B-9, M-1 … M-21, m-6 … m-10, erteleme sırası, en küçük v1 | Tam tarama |

### Açık noktalar

| No | Soru | Kimin kararı | Neyi engelliyor |
| --- | --- | --- | --- |
| A-1 | v1'de çatışırlarsa yabancı mı, sahibin kendi kullanımı mı önce gelir? (B-7) | Sahip | **Kapandı (S-18): sahip önce** |
| A-2 | "Bilmiyorum" hangi etiketlere izin verir; ajan üzerinden gelirse ne olur; eksik değer sorusunda ne olur? (B-1) | Sahip | **Kapandı (S-24, 2026-11-11)** |
| A-3 | Sağlayıcı koşulları doğrulanana kadar varsayılan formül yolu ne olsun? (B-5) | Sahip | **Kapandı (S-25, 2026-11-11)** |
| A-4 | Toplayıcıdan gelen üye en üst etikete katkı verir mi (A, B, C)? | Sahip (araştırıldı) | F3b; v1'de `PROVEN` yoksa hiçbir şeyi |
| A-5 | v1'de `PROVEN` olacak mı? (B-7, en küçük v1) | Sahip | **Kapandı (S-20, 2026-11-11)** |
| A-6 | İlk ölçülecek görev profili | Sahip | F3b |
| A-7 | Kayıtların sürümden bağımsız güncellenme yolu (M-17) | Tasarımcı | Kayıt dağıtımı |
| A-8 | Desteklenen platformlar; Windows (M-7) | Sahip | **Kapandı (S-27, 2026-11-11)** |
| A-9 | DeepSeek Harness'in yeri (S-6) | Sahip | Hiçbir şeyi (opsiyonel istemci) |
| A-10 | "Yanlış" seçeneğinde düzeltmenin biçimi ve tur sınırı (M-7) | Tasarımcı | Faz 1 görev 14 |
| A-11 | Belge okuyucu (PDF/DOCX) v1'de var mı? (M-11) | Sahip | **Kapandı (S-23, 2026-11-11)** |
| A-12 | Lean (K26) v1'den ertelensin mi? (Y-21) | Sahip | **Kapandı (S-22, 2026-11-11)** |
| A-13 | v1'in kabul ölçütü olan somut roket ve finans hesapları hangileri? | Sahip | **Kapandı (S-21, 2026-11-11)** |
| A-14 | Rigor, aynı kullanıcı hesabındaki tam kabuk erişimli ajana karşı ne vaat ediyor? (B-4, Y-4) | Sahip | **Kapandı (S-26, 2026-11-11)** |

### Doğrulanacaklar (birincil kaynakla, tasarıma yazılmadan önce)

| No | İddia | Önerilen kaynak |
| --- | --- | --- |
| D-1 | Anthropic koşullarının, açık kaynak bir aracın kullanıcının kendi `claude` istemcisini başsız çağırmasına izin verip vermediği (B-5) | Anthropic Consumer Terms ve Claude Code hukuki sayfası; gerekirse Anthropic'e sorulmalı |
| D-2 | OpenAI ve Google için aynı soru | Codex ve Gemini CLI kullanım koşulları; Gemini veri kullanımı sayfası (404 döndü) |
| D-3 | Başsız kullanımın faturalandırması (ayrı kredi var mı?) | Anthropic fiyatlandırma ve yardım sayfaları |
| D-4 | Groq ücretsiz plan sınırları | Groq konsolundaki "Free Plan Limits" sekmesi |
| D-5 | OpenRouter ücretsiz modellerde günde 50 istek | OpenRouter rate limits sayfası |
| D-6 | VS Code eklentisi ve diğer istemcilerde elicitation ve sampling desteği | İstemcilerin resmî belgeleri ve `initialize` yanıtı |
| D-7 | MCP elicitation şemasının yalnızca düz alanlara izin verdiği (toplu onay ekranı için) | MCP belirtimi 2026-07-28 |
| D-8 | Erişilemeyen dört kaynak | **Kapandı:** dördü de 2026-11-11'de PDF'ten doğrulandı |
| D-9 | Y-4: MCP Python SDK'nın ajan istemcide elicitation'ı otomatik yanıtlamaya izin verdiği; Y-6: `ctx.elicit()`'in eski bağlantılara özgü olduğu ve 2026-07-28 akışı | R-FII'nin alıntıladığı resmî SDK ve belirtim sayfaları; tasarıma yazılmadan önce tasarımcı tarafından okunmalı |
| D-10 | Y-13: `frozen=True` davranışı Pydantic 2.14'te | Hedef sürümde küçük bir deney |

### Tasarım belgesine eşleme

| Tasarım yeri | Değişiklik | Kayıt |
| --- | --- | --- |
| Başlık (satır 6), okuma kuralı (satır 10–12) | "Onaylandı" durumu; sahip kararlarının birbirinin yerini alma kuralı | Bu bölümün başı |
| §1 (satır 28–36), §1.1 (satır 43–45) | Hedef kullanıcı; yeni vaat metni | S-1, Ö-3-13, A-2 |
| §2: K2, K4, K6, K14, K15, K16; yeni K27 ve sonrası | Yeni sahip kararları; eski satırlarda "yerine" | S-1 … S-17, M-18 |
| §3.3: A1, A3, A6 | Yanlış `CERTIFIED` = 0; ayrıştırıcı istisnası; A6 izin ve onay kanalını da kapsar | B-3, M-10, B-4 |
| §3.4 (satır 138, 145, 163–182) | Matris etiket sütunu; `unsat` hükümleri; paket olgunluk tavanı | B-2, B-3 |
| §4.1 (satır 194–207) | Dört etiket; karar tablosu; tek aile politikası; ret listesi | R-1, B-2 |
| §4.2 (satır 214–223) | Onay durumları; `NEEDS_CONSENT`; `NEEDS_RECONFIRMATION` | B-1, M-7, M-8 |
| §4.3 (satır 225–240) | Formülün yazarı ekseni; `strict_input_provenance` varsayılanı | B-1, M-18 |
| §4.4, §4.5 | Tavan kuralları açık koşul olur | B-2 |
| §5.2 (satır 305, 312), §5.3 tablo | Sentinax kapısı küme olarak; etiket sütunu | B-2 |
| §6.1, §6.2 (satır 421–431, 443) | Dosya okuma kuralları; ayrıştırıcı; `decimal` hassasiyet ve yuvarlama; rasyonel alan | M-10, M-11 |
| §6.3 | Katı denetimler ve "bilinmiyor"un geçti sayılmaması | B-8 |
| §6.4 (satır 471–517) | Adaptörler, izin, yalıtım, iç içe çağrı, yeterlik kapısı, sampling | B-5, M-3, M-12, M-21 |
| §6.6 (satır 550–560) | Bağımsız denetleyici; `unsat_core` sertifika değil; çözüm kümesinde tamlık | B-3, B-9 |
| §6.7, §6.8 (satır 562–602) | Onay ekranı ve yoklama soruları; dört alanlı kutu; yazar, harcama, "nasıl yükseltilir" | R-1, M-6, M-19 |
| §6.9, §6.9.1 | Şablonda kayıt geçerliliği; hakem paneli üyelerinin yeterliği | M-5 |
| §7.1, §7.2 (satır 757–807) | Tek kaba araç ve iş modeli; `rigor solve`; kanal matrisi; anahtar elicitation ile istenmez | Ö-3-8, M-2, M-7 |
| §8.2 (satır 840–873) | Yanıt ve istem önbelleği ayrımı; bayt bayt aynı yanıt kuralı; toplayıcı sözleşmesi | Ö-5-1, A-4 |
| §8.3 (satır 886–887) | Anahtar kaynakları; `.env` okunmaz | S-14, Ö-3-10 |
| §9 (satır 912–930) | Yanlış `CERTIFIED` ölçütü; yeterlik seti; negatif testler | B-3, Ö-2-6 |
| §10, §11, §12 | Faz sırası; açık sorular; `rigor solve` komut adı artık uygulayıcıya bırakılmıyor | B-6, A-1 … A-11 |

Diğer belgeler:

- **Yol haritası:** §1 paket ağacı (yürütme katmanı, ayrıştırıcı, yeterlik, izin); satır 50 ve 54 (sözleşmeler); faz
  tablosu satır 63, 65, 71, 75; F3'ün F3a ve F3b'ye bölünmesi; F7'nin öne alınması.
- **Faz 1 planı:** satır 7, 17, 21, 32; görev 2, 3, 8, 9, 10, 11, 14, 15, 16, 17, 18, 19; plan G1, G3, G11; yeni
  görevler: tehdit modeli testleri, dar denetleyici, revizyon bağı, platform matrisi.
- **README:** vaat, etiket tablosu, "3 bağımsız model", model erişimi, kullanım, MCP araçları, yapım sırası; izin ve
  harcama bölümü; yabancı için kurulum ve kullanım dosyası.

### Sıradaki adımlar

1. Sahip açık noktaları cevaplar. **2026-11-11:** A-1, A-2, A-3, A-5, A-8, A-11, A-12, A-13, A-14 kapandı; açık
   kalanlar mimari belgenin §9'unda.
2. Sahip rapor önerilerini ve tasarımcı önerilerini kalem kalem onaylar ya da reddeder. **2026-11-11:** toplu kabul
   (S-28).
3. Bu belge resmî tasarım taslağına dönüştürülür; taslak yeniden taze gözle incelenir. **2026-11-11:** mimari belge
   ve faz planı yazıldı; inceleme sonucu mimari belgenin §11'inde.
4. Tek revizyonda tasarım belgesi, yol haritası, Faz 1 planı ve README güncellenir.

Birleştirme koşulu: 1. ve 2. adım bitmiş olmalı. Açık kalan her nokta tasarıma "açık" diye ve fail-closed varsayılanla
yazılır (ör. A-4 için A seçeneği).

## Kaynaklar

- [Claude Code: legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- [Claude Code: headless mode](https://code.claude.com/docs/en/headless)
- [Claude Code: MCP](https://code.claude.com/docs/en/mcp)
- [Codex: non-interactive mode](https://developers.openai.com/codex/noninteractive)
- [Gemini CLI: headless mode](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/headless.md)
- [Groq: rate limits](https://console.groq.com/docs/rate-limits)
- [OpenRouter: provider selection](https://openrouter.ai/docs/guides/routing/provider-selection.md)
- [OpenRouter: message transforms](https://openrouter.ai/docs/guides/features/message-transforms.md)
- [OpenRouter: generation metadata](https://openrouter.ai/docs/api/api-reference/generations/get-request-&-usage-metadata-for-a-generation)
- [OpenRouter: model fallbacks](https://openrouter.ai/docs/guides/routing/model-fallbacks.md)
- [OpenRouter: privacy and logging](https://openrouter.ai/docs/guides/privacy/logging.md)
- [Model Equality Testing (arXiv 2410.20247)](https://arxiv.org/abs/2410.20247v2)
- [Auditing Model Substitution in LLM APIs (arXiv 2504.04715)](https://arxiv.org/abs/2504.04715v2)
- [NIST SP 800-63B-4: Authenticator Assurance Levels](https://pages.nist.gov/800-63-4/sp800-63b/aal)
- Chen, Kuo, Liu, Poon, Towey, Tse, Zhou (2018). Metamorphic Testing: A Review of Challenges and Opportunities. ACM
  Computing Surveys 51(1). [doi:10.1145/3143561](https://doi.org/10.1145/3143561)
- Morante, García-Rubio (2026). Correlation limits the reliability of ensemble decision making with large language
  models. Discover Informatics 1:35. [doi:10.1007/s44564-026-00040-z](https://doi.org/10.1007/s44564-026-00040-z)
- Knight, Leveson (1986). An experimental evaluation of the assumption of independence in multiversion programming.
  IEEE Transactions on Software Engineering SE-12(1), 96–109.
- Berger, Hsu (1996). Bioequivalence trials, intersection–union tests and equivalence confidence sets. Statistical
  Science 11(4), 283–319. [doi:10.1214/ss/1032280304](https://doi.org/10.1214/ss/1032280304)
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
