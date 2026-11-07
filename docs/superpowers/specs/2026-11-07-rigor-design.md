# Rigor — Tasarım Belgesi

| | |
|---|---|
| Tarih | 2026-11-07 |
| Durum | TASLAK — sahibin onayını bekliyor |
| Sahip | Eren Tahiroğlu |
| Kaynaklar | [`../../../Handoff`](../../../Handoff) (önceki oturum, Bölüm 1 bağlayıcı), [`../../research/2026-11-07-arastirma-notlari.md`](../../research/2026-11-07-arastirma-notlari.md) |

> **Okuma kuralı:** "**Sahip kararı**" ile işaretli maddeler sahibin açıkça söylediği şeylerdir ve değiştirilemez.
> "**Tasarımcı kararı**" ile işaretli maddeler bu belgeyi yazanın verdiği, sahibin henüz ayrıca onaylamadığı kararlardır;
> sahip okurken bunları kontrol etmelidir. İşaretsiz maddeler bu ikisinden türeyen teknik ayrıntılardır.

---

## 1. Niyet: neden var?

Bir LLM'e matematik yaptırdığında iki tür hata olur:

- **Tip-1 — Hesap hatası:** `17 × 23`'ü yanlış çarpmak, bir türevi yanlış almak.
- **Tip-2 — Formülasyon hatası:** Doğal dildeki problemi yanlış denkleme dökmek ("en fazla" yerine `>=` yazmak,
  birimi karıştırmak, eksik bir parametreyi sessizce uydurmak). Çözücü bu durumda **yanlış sorunun kusursuz
  cevabını** verir. En tehlikeli hata budur.

Çıkış noktası (Handoff §2.1): `Qwenputer` projesi bir RISC-V işlemciyi LLM ağırlıklarına gömüp aritmetiği kusursuz
yaptı, ama GSM8K'de temel modelle berabere kaldı. Çünkü darboğaz Tip-1 değil Tip-2'dir.

Rigor, sahibin AI'a yaptırdığı matematiksel çıktılardan **emin olabilmesi** için bir araçtır. Somut kullanımlar
(**Sahip kararı**):

1. **Roket takımı hesapları** — yakında başlayacak; itki, kütle bütçesi, Tsiolkovsky, irtifa/yörünge, sürükleme vb.
2. **Kişisel kripto alım-satım botu** (özel repo; herkese açık belgelerde anonim, K23) — botun temeli hazır,
   matematiğinin doğru olduğundan emin olunmak isteniyor.
3. **Sentinax** — sahibin yatırım karar destek web sitesi; canlıya almadan matematiksel doğruluk (K21).

Önce sahibin kendisi için; roket takımındaki arkadaşları da çıktıları (özellikle kanıt raporunu) görebilir.

### 1.1. Dürüst garanti tanımı

Tip-2 hataları için literatürde **matematiksel garanti veren hiçbir yöntem yoktur** (bkz. araştırma notları §1).
Bu yüzden Rigor'un vaadi şudur:

> **Rigor'un döndürdüğü her sonuç ya sahibin onayladığı formal tanıma göre doğrulanmıştır (ve doğrulamanın
> gücü etiketle açıkça belirtilir), ya da Rigor cevap vermeyi reddeder ve nedenini söyler.
> Etiketsiz bir sayı asla dönmez.**

"Sıfır halüsinasyon" hedefi bu şekilde işlemsel hale gelir: hesap hataları deterministik motorlarla sıfırlanır;
formülasyon hataları bağımsız çapraz formülasyon + insan onayı ile yakalanır; yakalanamayan belirsizlik
reddetmeye dönüşür.

---

## 2. Bağlayıcı kararlar (Handoff Bölüm 1 + bu oturum)

| # | Karar | Kaynak |
|---|---|---|
| K1 | **Genel amaçlı hibrit sistem.** Mühendislik/fizik (termodinamik, akışkanlar, kütle/enerji denklikleri, diferansiyel ve doğrusal olmayan denklemler) + finansal/algoritmik modelleme, mantıksal kurallar, optimizasyon. Tek alana odaklanmaz; problem türüne göre motor seçen bir yönlendirici vardır. | Handoff K1 |
| K2 | **Süre sınırsız, kesinlik mutlak.** "Ne kadar sürerse sürsün ama sonucu Red Team denetiminden geçmiş kadar kesin olsun." Gecikme hedefi yoktur. | Handoff K2 |
| K3 | **Çift arayüz:** projelere gömülebilen bir **Python kütüphanesi/SDK** + kodlama ajanlarının (Claude Code, Gemini CLI vb.) çağırabildiği yerel bir **MCP sunucusu**. | Handoff K3 |
| K4 | **Eksik parametrede kullanıcıyı sıkıştır (fail-closed).** Sistem asla kendi varsayımını yapmaz, parametrik/sembolik geçiştirme yapmaz; durur, eksiği tespit eder, kullanıcıdan ister. | Handoff K4 |
| K5 | **Kanıt raporu** üretilir. | Bu oturum |
| K6 | **İki formülasyon kaynağına da uygun olmalı:** Rigor'un kendi LLM API erişimi (çoklu sağlayıcı) **ve** formülasyonu çağıran ajanın sağlaması. | Bu oturum |
| K7 | **Sade anlatım:** Sistem denklemleri yalnızca okunur dile çevirip onaylatmakla kalmaz; problemi, varsayımları ve çözümü **olabildiğince basit bir dille** anlatır. | Bu oturum |
| K8 | **Roket kapsamı:** TEKNOFEST 2026 Roket Yarışması şartnamesi ve eklerindeki **tüm matematiksel işlemleri** sorunsuz yapabilmeli (kapalı formlu hesaplar ve simülasyon dahil; envanter §5.3). | Bu oturum |
| K9 | **Kullanım:** Hem Python'dan hem Claude Code (MCP) üzerinden kullanılabilmeli; ikisi de birinci sınıf. | Bu oturum |
| K10 | **Fiziksel alt modeller:** Rigor sürümlü, adlandırılmış bir model kütüphanesiyle gelir ve **otomatik** kullanır (seçenek A); ama oturumun **en başında** kullanıcıya "Kendi denklemlerini/verilerini vermek ister misin?" (seçenek B) diye sorulur ve cevaba göre ilerlenir. | Bu oturum |
| K11 | **Python: seçenek (b).** 3.15 birincil hedef ve geliştirme sürümü; lazy davranış `__lazy_modules__` ile; aynı kod 3.12–3.14'te lazy olmadan çalışır (§8.1). | Bu oturum |
| K12 | **Takım kategorisi: A2 Orta İrtifa** (M1850 motor, asgari 8.000 ft, rampadan çıkış ≥ 25 m/s). Envanter önceliği buna göre (§5.3). | Bu oturum |
| K13 | **Uçuş bilgisayarının C/C++ kodunun denetimi kapsam dışı.** | Bu oturum |
| K14 | **LLM erişimi:** ücretsiz API'ler (ör. Groq) + sahibin AI abonelikleri: **Claude, ChatGPT, Gemini**. API anahtarlı ücretli kullanım varsayılmaz. | Bu oturum |
| K15 | **Yönlendirici kararı (§8.2) onaylandı:** abonelikler yalnızca resmi CLI'lar (`claude`, `codex`, `gemini`) üzerinden kullanılır; OmniRoute vb. ağ geçitleri yalnızca ücretsiz/API sağlayıcıları için, geçiş sözleşmesiyle ve opsiyonel olarak. | Bu oturum |
| K16 | **Hedef: Şubat 2027 sonu**, o tarihte araç sahibin istediği tüm özellikleri karşılıyor olmalı. Ayrıntılı takvim yapılmaz; yalnızca sıra (§10). | Bu oturum |
| K17 | **OpenRocket karşılaştırması zorunlu özellik:** takımın OpenRocket'ta yaptığı hesaplarla Rigor'un değerleri karşılaştırılabilmeli (§6.10). | Bu oturum |
| K18 | **Onaylı şablon + öz-denetim:** onaylı formülasyon şablon olarak yeniden kullanılır (§6.9); aynı şablon belli bir sürede defalarca kullanılırsa **araç, LLM kullanmadan** şablonun hâlâ doğru olduğunu kendisi kontrol eder. | Bu oturum |
| K19 | **Öz-denetim alarmında hakem LLM + öğrenme:** öz-denetim büyük bir hata bulursa ve geçmişe bakınca aynı hata önceden de varsa, araç LLM'e "gerçek hata mı, yoksa kontrolün kendisi mi yanlış alarm veriyor?" diye sorar; algoritma mümkün olduğunca bu kararlardan öğrenir (§6.9.1). | Bu oturum |
| K20 | **Kripto botu: kod denetimi değil, yalnızca matematiksel hesapların kontrolü** (§5.2). | Bu oturum |
| K21 | **Mod B kapsamı: B1 (formül denetimi) + B2 (bağımsız yeniden hesap) ikisi birden**, iki finans yazılımı için: kripto botu ve [Sentinax](https://github.com/ErenTahiroglu/Sentinax) (yatırım karar destek web sitesi). Sentinax için amaç: **canlıya almadan önce** matematiksel doğruluk kontrolü. | Bu oturum |
| K22 | **Lisans: PolyForm Noncommercial 1.0.0**; repo: `github.com/ErenTahiroglu/Rigor`. | Bu oturum |
| K23 | **İki dal:** `development` = geliştirme, `main` = kararlı son sürüm (§8.4). **Kripto botuyla ilgili kısımlar herkese açık belgelerde anonim**; kimliği belirleyen ayrıntılar git'e girmeyen `docs/private/` altında. | Bu oturum |

---

## 3. Hedefler, hedef olmayanlar, anti-hedefler

### 3.1. Hedefler
- G1. Tip-1 hatalarını deterministik/kesin motorlarla tamamen ortadan kaldırmak.
- G2. Tip-2 hatalarını bağımsız çoklu formülasyon, SMT/CAS denklik kontrolü, geri-çeviri ve insan onayıyla yakalamak.
- G3. Eksik, çelişkili veya boyutsal olarak tutarsız problemleri **çözücüye gitmeden** tespit etmek ve kullanıcıya sormak.
- G4. Her sonuca, neyin neden doğru olduğunu gösteren, yeniden üretilebilir bir kanıt raporu eklemek.
- G5. Problemi, varsayımları ve sonucu bir lise öğrencisinin anlayacağı sadelikte anlatmak.
- G6. Kripto botunun kullandığı formülleri ve ürettiği sayıları bağımsız olarak doğrulamak; kodu denetlemeden (Mod B, §5.2, K20).

### 3.2. Hedef olmayanlar (v1)
- Hız/düşük gecikme (K2).
- **Fiziksel modelin gerçekliği.** Rigor matematiği garanti eder; "sürükleme katsayısı 0.45 doğru mu?" sorusunu
  cevaplamaz. Girdi değerleri ve fiziksel model seçimi kullanıcının sorumluluğundadır ve raporda bu açıkça yazar.
- Trading stratejisinin kârlılığı veya piyasa öngörüsü. Mod B yalnızca "formül doğru mu, sayı doğru hesaplanmış mı?"
  sorularını cevaplar.
- Kod denetimi (K13, K20): Rigor ne uçuş bilgisayarı kodunu ne botun kodunu okur, çalıştırır veya test eder.
- Soyut teorem ispatı (Lean 4) v1'de yok; IR, ileride Lean arka ucu eklenebilecek şekilde tasarlanır.
- Grafik arayüz. Kanıt raporu Markdown/HTML olarak üretilir, o kadar.
- Barındırılan (hosted) çok kullanıcılı servis. Yerel çalışır.

### 3.3. Anti-hedefler (teknik olarak çalışsa bile başarısızlık sayılır)
- A1. **Yanlış bir sonucun "KANITLANDI" etiketiyle dönmesi.** En kötü başarısızlık budur; sistemin tüm eşikleri
  bunu önlemek için muhafazakâr seçilir. Şüphede kalınırsa etiket düşürülür veya reddedilir.
- A2. Kullanıcıya söylenmemiş herhangi bir varsayım (birim, işaret, başlangıç değeri, yuvarlama modu…).
- A3. LLM çıktısının `eval()`/`exec()`/`sympy.parse_expr` gibi kod çalıştıran yollarla işlenmesi.
- A4. Sade anlatımda kanıt raporunda olmayan bir sayı, birim veya karşılaştırma ifadesinin bulunması
  (anlatımın kendisinin halüsinasyonu).
- A5. Jargon dolu, uzman olmayanın anlayamayacağı açıklama.
- A6. Ajanın, kullanıcıya sorulması gereken eksik bir parametreyi kendi kafasından doldurup bunun
  kullanıcı cevabıymış gibi kaydedilmesi.

---

## 4. Temel kavramlar

### 4.1. Doğrulama etiketleri (sonuç seviyeleri)

| Etiket | Anlamı | Şartlar (hepsi) |
|---|---|---|
| **KANITLANDI** (`PROVEN`) | Sonuç, onaylı tanıma göre formal olarak doğru. | (a) Formal tanım kullanıcı tarafından onaylandı; (b) formülasyon konsensüsü **oybirliği** ile ve **≥2 farklı model ailesinden** geldi; (c) çözüm için makinece kontrol edilebilir bir sertifika var (kesin aritmetikle geri ikame, `unsat` ispatı, rasyonel aritmetikle doğrulanmış LP dual sertifikası, Arb top aritmetiğiyle hata sınırı vb.). |
| **ÇAPRAZ DOĞRULANDI** (`CROSS_VALIDATED`) | Sonuç güçlü biçimde destekleniyor ama formal sertifika yok ya da formülasyon bağımsızlığı zayıf. | (a) Formal tanım onaylandı; (b) oybirliği konsensüsü var; (c) en az iki bağımsız yöntem aynı sonucu verdi ve sınır testleri geçti. Örnekler: ODE ile yörünge, tek model ailesinden gelen formülasyon, Mod B2'de bootstrap tabanlı istatistikler. |
| **REDDEDİLDİ** (`REFUSED`) | Sonuç verilmedi. | Neden kodu (ör. `UNDERDETERMINED`, `INCONSISTENT`, `DIMENSION_MISMATCH`, `NO_CONSENSUS`, `SOLVER_UNKNOWN`, `CERTIFICATE_FAILED`, `USER_REJECTED_SPEC`, `TEMPLATE_SELF_CHECK_FAILED`) + sade dille açıklama + kullanıcıdan ne gerektiği. |

Etiketin altındaki her şart raporda ayrı ayrı "geçti/geçmedi" olarak listelenir; böylece kullanıcı güvenin neye
dayandığını görür.

**Tasarımcı kararı — tek model ailesi politikası:** Elde yalnızca bir model ailesi varsa (ör. API anahtarı yok,
sadece çağıran ajan var) Rigor **çalışır**, ama sonuç en fazla `CROSS_VALIDATED` olabilir ve raporda
"Formülasyon bağımsızlığı zayıf: tek model ailesi" uyarısı çıkar. Yapılandırmada `strict_independence = true`
seçilirse bu durumda `REFUSED (INSUFFICIENT_INDEPENDENCE)` döner. Varsayılan: `strict_independence = false`
(sahibin 3 aboneliği + Groq ile tek aile durumu olağan kullanımda zaten oluşmaz).

### 4.2. Oturum durumları

Çok adımlı bir etkileşim olduğu için her çözüm bir **oturum**dur:

```
YENİ → AYRIŞTIRILDI → (GİRDİ_GEREKLİ ⟲) → FORMÜLE_EDİLDİ → (ONAY_GEREKLİ ⟲) → ÇÖZÜLDÜ → SONUÇ{PROVEN|CROSS_VALIDATED|REFUSED}
```

- `GİRDİ_GEREKLİ` (`NEEDS_INPUT`): eksik parametre, belirsiz birim, iki yoruma ayrılan ifade. Soru ve cevap
  formatı yapılandırılmıştır (beklenen birim, değer aralığı).
- `ONAY_GEREKLİ` (`NEEDS_CONFIRMATION`): "Problemi şöyle anladım" anlatımı (§6.7) kullanıcıya gösterilir;
  kullanıcı onaylar, düzeltir ya da reddeder.
- Oturumlar diske kalıcı yazılır (yeniden başlatmada kaldığı yerden devam). Oturum kaydı, raporun girdisidir.
- Onaylı şablon kullanımı (§6.9) `AYRIŞTIRILDI → … → ONAY_GEREKLİ` adımlarını atlar ve doğrudan statik kapılara
  girer; öz-denetim gerekiyorsa önce `ÖZ_DENETİM` (`SELF_CHECK`), alarmda `HAKEM` (`ADJUDICATION`, §6.9.1) durumuna geçer.

### 4.3. Girdi kaynağı kaydı (A6'ya karşı)

Kullanıcıdan gelen her değer kaynağıyla birlikte kaydedilir:
- `USER_DIRECT` — kullanıcı doğrudan girdi (SDK'da doğrudan çağrı, MCP'de elicitation formu).
- `VIA_AGENT_UNVERIFIED` — çağıran ajan ilettiği için kullanıcıdan geldiği doğrulanamadı.
- `USER_FILE` — kullanıcının gösterdiği bir veri dosyasından okundu (**Tasarımcı kararı**). Kayıt: dosya yolu,
  SHA-256, konum (sayfa + hücre, satır/sütun). Dosya yolu `USER_DIRECT` ile verildiyse değer `USER_DIRECT` kadar
  güvenilir sayılır ve `PROVEN`'ı destekleyebilir; yol ajan aracılığıyla geldiyse `VIA_AGENT_UNVERIFIED` kuralı
  uygulanır. Rapor her değerin dosyadaki yerini gösterir.

`VIA_AGENT_UNVERIFIED` girdiler raporda açıkça işaretlenir. **Tasarımcı kararı:** bu tür girdiyle `PROVEN` etiketi
verilebilir ama rapor başlığında uyarı çıkar; `strict_input_provenance = true` ise en fazla `CROSS_VALIDATED`.
**Tanım onayı (`NEEDS_CONFIRMATION`) daha katıdır (Tasarımcı kararı, Red Team düzeltmesi):** `PROVEN`'ın (a) şartı
"tanımı kullanıcı onayladı"dır; onay ajan aracılığıyla geldiyse bu şart doğrulanamaz. Bu yüzden ajan aracılığıyla
gelen onay `VIA_AGENT_UNVERIFIED` kaydedilir ve sonuç **her zaman en fazla `CROSS_VALIDATED`** olur (ajan onayı
kendisi verip `PROVEN` üretemez, A6). `PROVEN` için onay `USER_DIRECT` olmalıdır (SDK'da doğrudan, MCP'de elicitation).

### 4.4. Tek formülasyonlu (insan yazımı) IR

**Tasarımcı kararı:** Red Team uygulanmamış tek bir IR (ör. 1. aşamada kullanıcının ya da ajanın elle yazdığı)
en fazla `CROSS_VALIDATED` alabilir; raporda "Red Team uygulanmadı: tek formülasyon" uyarısı çıkar. Bu durumda
`CROSS_VALIDATED`'in (b) konsensüs şartı "uygulanmadı" olarak işaretlenir; diğer şartlar (onay, iki bağımsız
çözüm yolu, sınır testleri) aynen aranır. İnsanların IR'ı ham JSON ağacı yazmadan kurabilmesi için SDK'da bir
Python kurucu API'si bulunur (ör. `q = rigor.given("m_dry", 12, "kg")`, `rigor.eq(...)`); bu API kod çalıştırmaz,
yalnızca IR nesnesi üretir.

### 4.5. Model kütüphanesi ve kullanıcı denklemleri (K10) hangi etiketi alabilir

**Tasarımcı kararı:**
- **Kütüphane modelleri (seçenek A) güvenilir, ayrıca doğrulanmış varlıklardır**; §4.4 sınırına tabi değildir.
  Bir model kütüphaneye ancak şu doğrulamayla girer: (1) kaynak standardın/kitabın yayımlanmış tablolarına veya
  çözülmüş örneklerine karşı test (ör. ISA 1976 tablo değerleri, Barrowman için yayımlanmış örnek hesaplar),
  (2) denklemlerin kaynaktan **iki ayrı kez** IR'a yazılıp Rigor'un kendi denklik kontrolünden geçirilmesi,
  (3) birim ve geçerlilik aralığı testleri. Bu doğrulamanın kaydı modelle birlikte sürümlenir ve raporda atıf alır.
- Model kullanan bir problemde Red Team modelin denklemlerini yeniden türetmez; formülatörlerin **hangi modeli,
  hangi parametrelerle ve hangi büyüklüğe bağlayarak** kullandığı üzerinde oybirliği aranır. Böylece R3, R7, R8,
  R13 (lüle) için `PROVEN (modele göre)` ulaşılabilir kalır.
- **Kullanıcının kendi denklemleri (seçenek B):** Denklemler metin/LaTeX/sözlü tarif olarak verilirse normal
  boru hattından geçer (K formülatör bağımsız olarak IR'a çevirir, denklik, onay) → `PROVEN` mümkün. Doğrudan
  Python kurucu API'siyle IR olarak verilirse §4.4 geçerlidir (en fazla `CROSS_VALIDATED`).
- Kullanıcının verdiği **veri** (tablo, `.eng`, xlsx) `USER_FILE` kaydıyla girer (§4.3); verinin fiziksel
  doğruluğu kapsam dışıdır, okunmasının doğruluğu (hash + konum) kapsam içidir.

---

## 5. Çalışma modları

### 5.1. Mod A — Problem çöz (öncelikli: roket)

Girdi: doğal dilde problem (+ isteğe bağlı: ajanın hazırladığı IR, bilinen değerler tablosu).
Çıktı: etiketli sonuç + sade anlatım + kanıt raporu.

**Alt tür — iddia/formül denetimi:** Girdi bir problem değil, bir belgede yazan formül veya iddia olabilir
("Ek-1'deki Hamilton çarpımı doğru mu?"). Aynı boru hattı kullanılır; iddia IR'a çevrilir, referans tanımla
(ör. SymPy'nin kuaterniyon cebiri) denklik kontrolünden geçer, yanlışsa karşı örnek verilir. Bu yeteneğin değeri
2026-11-07 incelemesinde somut olarak görüldü: şartname Ek-1'deki kuaterniyon çarpım formülünün yanlış olduğu
bu yöntemle kanıtlandı (araştırma notları §9.2).

### 5.2. Mod B — Finans yazılımlarının matematiğini denetle (K20, K21; kod denetimi değil)

Hedefler: kripto botu ve Sentinax. Rigor bu yazılımların kodunu okumaz, çalıştırmaz, test etmez. İki şey yapar
(K21: ikisi birden):

- **B1 — Formül denetimi:** Botun kullandığı formül, belgesinde veya protokolünde yazdığı haliyle Rigor'a verilir
  (metin, LaTeX veya kullanıcı tarifi). Mod A'nın iddia/formül denetimi alt türüyle (§5.1) literatürdeki referans
  tanımla denklik kontrolünden geçer; yanlışsa karşı örnek verilir. Örnekler (botun istatistik protokolü
  metninden, 2026-11-07 incelemesi): günlük Sharpe = ortalama / örneklem std (ddof=1), yıllıklandırma
  `× √365.25`, Deflated Sharpe Ratio ve beklenen maksimum Sharpe `√V·((1−γ)Φ⁻¹(1−1/N) + γΦ⁻¹(1−1/(N·e)))`
  (Bailey & López de Prado), Hansen SPA istatistiği `max(max_k √T·mean(d_k)/ω_k, 0)`; ücret = oran × nominal
  (alış → baz varlıkta, satış → kote varlıkta), bakiye özdeşliği (açılış + akışlar + dolumların etkisi = kapanış).
- **B2 — Sonuç denetimi (mutabakat):** Botun ürettiği somut sayılar (ücret, bakiye, kuantize miktar, Sharpe/DSR
  değeri…) ve bu sayıların girdileri botun çıktı dosyalarından okunur (`USER_FILE`, §4.3). Rigor aynı hesabı onaylı
  şablonla (§6.9) **bağımsız olarak** yeniden yapar ve karşılaştırır: `Decimal` para hesaplarında birebir (aynı
  hassasiyet + yuvarlama modu), kapalı formlu istatistiklerde Arb hata sınırı içinde. Uyuşmazlık → somut satır ve
  iki değer raporda.

**Sentinax için (K21):** Sentinax'ın formülleri (DCF/iç değer ve güvenlik marjı, Buffett puanlaması, TEFAS fon
getirisi yıllıklandırma `(1+R)^(12/H) − 1`, maksimum düşüş, Calmar, HRP, risk paritesi, CVaR, Black-Litterman
benzeri Bayes sonsalı, ücret/vergi, enflasyon düzeltmesi, kıymetli maden birim dönüşümleri, SEC çeyrek türetme)
B1 ile; canlıya almadan önce örnek portföyler ve şirketler için ürettiği sayılar B2 ile denetlenir. **Canlıya alma
kapısı (Tasarımcı kararı):** Rigor, B1'de en az `CROSS_VALIDATED` almamış ya da B2'de uyuşmazlığı olan her formülü
"canlıya hazır değil" listesinde gösteren bir özet rapor üretir. Kaynağı olmayan girdi (ör. sabit kodlanmış bir
puan) B2'de `USER_FILE` ya da kaynak kaydı alamadığı için ayrıca işaretlenir (§4.3, §6.1).

**Sınırlar (Tasarımcı kararı):**
- Rastgele tohumlu hesaplar (ör. durağan bootstrap ile SPA p-değeri) botun rastgele sayı akışı yeniden üretilmeden
  birebir doğrulanamaz. Rigor bunları kendi bağımsız bootstrap'ıyla, Monte Carlo hata payı içinde karşılaştırır;
  sonuç en fazla `CROSS_VALIDATED`.
- B2'de girdi dosyalarının botun gerçekte kullandığı veriler olduğu Rigor'un kanıtlayabileceği bir şey değildir;
  raporda dosya hash'leriyle "bu dosyalara göre" diye yazar.
- Formüllerin hangi formdan geldiği (belge mi, kullanıcının aktardığı mı) raporda kaynak olarak görünür.

Botun para hesaplarında `Decimal` kullanılıyor ve sistem fail-closed tasarlanmış; bu yüzden IR'ın `Decimal`
semantiğini (hassasiyet + yuvarlama modu) birebir modelleyebilmesi zorunludur (§6.2).

### 5.3. Roket matematiği envanteri (K8)

Kaynak: `Roket Takımı/Yarışma Şartnameleri` (TEKNOFEST 2026 şartnamesi + EK-1…EK-14 + motor verileri), 2026-11-07'de
incelendi. Tablo, her işin hangi yoldan çözüleceğini ve **ulaşılabilecek en yüksek etiketi** gösterir. "Model" sütunu
§5.4'teki kütüphaneden gelen alt modeldir; model seçimi ve parametreleri her zaman onay anlatımında gösterilir.

| # | İş (şartname yeri) | Matematik | Yol | En yüksek etiket |
|---|---|---|---|---|
| R1 | Birim dönüşümleri: asgari irtifalar **ft**, hızlar **m/s**, kütle g/kg (Tablo 3.3, 4.3) | Kesin rasyonel dönüşüm | pint + Rational | PROVEN |
| R2 | Kütle bütçesi, toplam kütle, ağırlık merkezi (Kütle Bütçesi xlsx; 4.5.16 CG iki ray butonu arasında) | Ağırlıklı toplam, eşitsizlik | Rational + Z3 kontrolü | PROVEN |
| R3 | Statik marjin `SM = (X_CP − X_CG)/D`, 0,3 Mach'ta 1,5–2,5 (Tanımlar; 4.4.5, 4.10.6) | Kapalı form; X_CP için Barrowman modeli | SymPy + Arb; model: Barrowman | PROVEN (modele göre) |
| R4 | Motor itki eğrisi: toplam impuls, ortalama itki, yakıt kütlesi düzeltmesiyle zaman ölçekleme (motor xlsx, `.eng`) | Tablo + trapez integral (kesin), oran | Rational | PROVEN |
| R5 | Rampadan çıkış hızı ≥ eşik (A2: 25 m/s; Tablo 4.3) | 1B ODE (itki tablosu, ağırlık, ray sürtünmesi, sürükleme) | solve_ivp ×2 + yakınsama | CROSS_VALIDATED |
| R6 | Tepe noktası (apogee), beyan edilen hedefe ±%15 (3.2.19), asgari irtifa (Tablo 3.3) | v1: 3-SD nokta kütle ODE (atış düzleminde 2B + yan rüzgâr), 85° rampa (4.1.35), rüzgâr profili, Cd(Mach), değişken kütle | solve_ivp ×2 + yakınsama; OpenRocket karşılaştırması (§6.10; raporlanır, etiketi belirlemez), opsiyonel RocketPy | CROSS_VALIDATED |
| R7 | Paraşüt iniş hızları 5–9 ve 9–20 m/s (4.2.5–4.2.8) | `v = √(2mg / (ρ·Cd·A))`, ρ irtifaya göre | SymPy + Arb; model: ISA | PROVEN (modele göre) |
| R8 | Ayırma sistemi: basınç, kuvvet, emniyet pimi (shear pin) sayısı (4.2.18) | İdeal gaz, `P·A ≥ n·F_pin` + emniyet katsayısı | SymPy + Z3 | PROVEN (modele göre) |
| R9 | Eksen dönüşümleri: DCM (ZYX), Euler açıları, kuaterniyon (EK-1) | Sembolik özdeşlikler, ortogonallik | SymPy | PROVEN |
| R10 | UKB test paketi: checksum, big-endian kodlama, IEEE-754 float alanları (EK-7) | Modüler aritmetik, bit düzeyi | Z3 bit-vektör + Python | PROVEN |
| R11 | PMF oranı ve ilave puan bantları (4.11.3, 4.12.3) | Oran + aralık sınıflandırması | Rational | PROVEN |
| R12 | Aktif kontrol (B1): ±2° toplam açısal hata bütçesi (tolerans yığılması), 4 Hz bant genişliği, 100°/s, menteşe momenti (5.2.15–5.2.22) | Aralık aritmetiği, transfer fonksiyonu, frekans cevabı | Arb aralık; python-control + bağımsız kontrol | PROVEN (bütçe) / CROSS_VALIDATED (dinamik) |
| R13 | Hibrit/sıvı motor (B2/B3, A6/A7): 100 N itki, yanma odası basıncı, lüle (izantropik akış), Aksaray irtifa koşulları (5.3, 5.4) | Kapalı form izantropik bağıntılar; yanma için kimyasal denge | SymPy + Arb; denge için Cantera (bağımsız ikinci yol gerekir) | PROVEN (lüle) / CROSS_VALIDATED (yanma) |
| R14 | Simülasyon yazılımı (B4): Mach 0,3–2,0 aerodinamik katsayılar, atalet, CG değişimi, tolerans etkisi, istatistiksel analiz, düşme bölgesi (5.5) | Monte Carlo, istatistik, 6-SD ODE | Formül ve sonuç denetimi (Mod B yöntemi; kod denetlenmez) + istatistik raporu | CROSS_VALIDATED |

**Uçuş modeli kapsamı (Tasarımcı kararı):** Rigor kendi integratörünü kullanır (IR'daki ODE → `solve_ivp`); v1 uçuş
modeli 3 serbestlik dereceli nokta kütledir (dönme dinamiği yok; rampa fazı 1B, ray sürtünme katsayısı kullanıcıdan,
K4). Roket yönelimi hız vektörüne hizalı varsayılır ve bu varsayım onay anlatımında açıkça yazılır. 6-SD uçuş
R14 ile birlikte sonraya kalır. OpenRocket/RocketPy farklı fiziksel modeller kullandığı için onlarla fark bir
**hata değil, bilgi**dir; `ENGINE_DISAGREEMENT` üretmez (§6.5). Karşılaştırmanın kuralları §6.10'da.

"PROVEN (modele göre)": matematik kanıtlıdır; seçilen fiziksel modelin (Barrowman, ISA, ideal gaz) gerçeği ne kadar
iyi temsil ettiği kapsam dışıdır (§3.2) ve raporda yazılır.

**İstatistiksel sonuçlar (R14, tolerans analizleri):** Monte Carlo sonucu bir sayı değil, bir dağılımdır. Rigor
bu sonuçları her zaman tohum, örnek sayısı ve güven aralığıyla raporlar ve en fazla `CROSS_VALIDATED` verir.
Tahmin edicilerin (ortalama, yüzdelik, güven aralığı) formülleri ayrıca `PROVEN` düzeyinde kontrol edilir.

**Öncelik (K12, A2 kategorisi):** R1–R11 birinci öncelik. A2 için somut eşikler: asgari 8.000 ft, beyan edilen
hedefe ±%15, rampadan çıkış ≥ 25 m/s, 0,3 Mach'ta SM 1,5–2,5, birincil paraşüt 9–20 m/s, ikincil 5–9 m/s, görev
yükü ≥ 4 kg ve kendi paraşütüyle 9–20 m/s, motor M1850. Hedef irtifa beyanı ±%15 toleransla yapıldığı için R6'nın
girdi toleranslarıyla (§6.2 aralıklı girdiler) çözülmesi A2 için özellikle değerlidir. R12–R14 A2'de doğrudan
istenmez; envanterde kalır, sonraya bırakılır (Tasarımcı kararı).

**Kapsam dışı (K13):** EK-7 uçuş bilgisayarının C/C++ kodu denetlenmez. R10 (checksum, paket kodlaması) bir
matematik işi olarak kapsamda kalır; Rigor doğru değerleri üretir, kodun bunları üretip üretmediğine bakmaz.

### 5.4. Model kütüphanesi (K10)

- **v1 modelleri (öneri):** ISA 1976 standart atmosferi (sahaya göre irtifa ofsetiyle), RASP `.eng` motor dosyası
  okuyucu ve itki tablosu, Barrowman basınç merkezi, paraşüt limit hızı, ideal gaz ayırma yükü, Tsiolkovsky,
  izantropik lüle bağıntıları, sürükleme `Cd(Mach)` tablosu (kullanıcı/OpenRocket verisinden), rüzgâr modeli
  (sabit + üstel/kuvvet yasası irtifa profili; değerler kullanıcıdan), ray sürtünmesi (Coulomb, katsayı kullanıcıdan).
- **Veri okuyucular (Tasarımcı kararı, v1):** RASP `.eng`, xlsx (yalnızca değerler, `openpyxl` salt-okunur; formül
  hücresinde önbellekteki değer okunur ve raporda "formül sonucu, Rigor tarafından yeniden hesaplanmadı" diye
  işaretlenir), CSV (OpenRocket simülasyon dışa aktarımı dahil), OpenRocket `.ork` (K17; yalnızca okuma, §6.10). RASAero v1 dışı.
- Her model: ad, sürüm, kaynak (kitap/standart), geçerlilik aralığı (ör. Barrowman küçük hücum açısı ve
  ses altı için), denklemleri IR olarak, birim testleri.
- **Akış (K10):** Oturum başında Rigor sorar: "Kendi denklemlerini veya verilerini vermek ister misin?" Hayır derse,
  kütüphane modelleri otomatik seçilir; seçilen her model ve parametresi (ör. "Aksaray atış alanının deniz
  seviyesinden yüksekliği") onay anlatımında listelenir. Model parametresi eksikse (ör. saha yüksekliği) K4 gereği
  sorulur, varsayılmaz. Evet derse, kullanıcının denklemleri/verisi IR'a girer ve aynı kapılardan geçer.
- Model kütüphanesi kullanıldığında raporda `fiziksel model: {ad} v{sürüm}, kaynak: …` satırı bulunur.
- `.eng` dosyaları yalnızca CR (`\r`) satır sonu kullanabilir (yarışma dosyası `Teknofest26_M1850_Rev1.eng` böyle);
  okuyucu CR, LF ve CRLF'yi desteklemelidir. RASP biçiminde (0, 0) noktası örtüktür.

---

## 6. Mimari

```
                    ┌──────────────────────── rigor (Python çekirdek / SDK) ────────────────────────┐
 Doğal dil ────────►│ 6.1 Ayrıştırma      : büyüklükler, birimler, bilinmeyenler, kaynak cümle      │
 (veya ajanın IR'ı) │ 6.2 Tipli IR        : Pydantic AST, eval yok, her düğümde birim + kaynak     │
                    │ 6.3 Statik kapılar  : birim (pint) · serbestlik derecesi (DM) · tutarlılık   │──► GİRDİ_GEREKLİ
                    │ 6.4 Red Team        : K bağımsız formülasyon · denklik · roundtrip           │──► GİRDİ_GEREKLİ (karşı örnek)
                    │ 6.7 Sade anlatım ①  : "Problemi şöyle anladım"                              │──► ONAY_GEREKLİ
                    │ 6.5 Çözüm           : yönlendirici → ≥2 bağımsız motor                       │
                    │ 6.6 Sertifika       : kesin/aralık geri ikame · unsat · LP dual · hata sınırı │
                    │ 6.7 Sade anlatım ②  : "Sonuç şu, çünkü…" + anlatım koruması                   │
                    │ 6.8 Kanıt raporu    : etiket, şartlar, varsayımlar, sürümler, hash            │
                    └───────────────────────────────────────────────────────────────────────────────┘
                                 ▲                                    ▲
                    Formülatör adaptörleri (6.4)          MCP sunucusu (§7) = ince kabuk
                    Claude · GPT · Gemini · Ajan IR'ı     araçlar + elicitation + oturum durumu
```

### 6.1. Ayrıştırma

LLM (yapılandırılmış çıktı ile) doğal dil metinden şunları çıkarır, her birini **metindeki kaynak aralığıyla**
(`source_span`) eşler: verilen büyüklükler (değer + birim), istenen büyüklükler, ilişkiler/kısıtlar, açık
varsayımlar ("sürtünmesiz", "deniz seviyesi"), örtük olabilecek varsayımlar (bunlar kullanıcıya soru olur, K4).
Kaynak aralığı olmayan hiçbir öğe IR'a giremez. Kaynak; metin aralığı, `USER_FILE` konumu (§4.3) veya kütüphane
modeli referansı (§4.5) olabilir.

### 6.2. Tipli ara temsil (IR)

- Pydantic v2 modelleri; JSON olarak serileştirilir. LLM IR'ı doğrudan JSON olarak üretir; serbest metin ifade
  ayrıştırılmaz (A3). İfadeler ağaç olarak gelir (`{"op": "mul", "args": [...]}`).
- **Düğüm türleri (en az):** `Quantity` (ad, birim, alan, rol), `Constant`, `Equation`, `Inequality`,
  `Objective` (min/max), `Piecewise`, `Derivative`/`ODE` (başlangıç koşuluyla), `Integral`, `Sum`/`Product`
  (indeks kümeleri üzerinde), `LogicalRule` (And/Or/Not/Implies), `Function` (adlandırılmış hesap, ör. Sharpe, DSR).
- **Rol (`role`):** `given` (verilen parametre), `unknown` (bulunacak), `decision` (optimizasyon karar değişkeni),
  `intermediate`. Serbestlik derecesi analizi bu ayrıma dayanır: optimizasyonda karar değişkenlerinin serbest
  olması normaldir; ama **her `given` bir değere sahip olmalıdır**.
- **Sayı alanları:** `Integer`, `Rational` (kesin), `Decimal(prec, rounding)` (Mod B ve para hesapları için,
  yuvarlama modu açık), `Real` (Arb top/aralık aritmetiğiyle değerlendirilir), `IEEEFloat` (yalnızca float
  kullanan bir kodu modellerken, açıkça). Rasyonel girdiler (`0.1`) varsayılan olarak kesin rasyonel okunur.
- **Ek düğüm türleri (Tasarımcı kararı, roket ve mühendislik ihtiyacı için):** `Table` (tablo verisi + açık
  interpolasyon yöntemi; veri dosyasının yolu ve SHA-256 hash'i ile), `Vector` (2B/3B büyüklükler, bileşen
  bazında birim), `NamedModel` (sürümlü, adlandırılmış alt model referansı; bkz. §4.5, §5.4). Z3/SymPy tablo fonksiyonlarını
  doğrudan kullanamaz; tablo içeren ifadeler sayısal yola yönlendirilir ve etiketleri buna göre sınırlanır.
- **Aralıklı girdiler (Tasarımcı kararı):** Bir `given` nokta değer yerine aralık (`12 ± 0.2 kg`, `[0.40, 0.50]`)
  taşıyabilir. Kapalı formlu/sayısal yollarda aralık Arb ile sonuca taşınır ve sonuç **garanti edilen aralık**
  olarak raporlanır. ODE yolunda aralık yayılımı garanti edilemez; burada uç ve örnek noktalar ayrı ayrı çözülür ve
  sonuç "örneklenmiş aralık" olarak `CROSS_VALIDATED` ile sınırlı kalır. IR şeması aralıkları baştan destekler;
  uygulama sırası uygulayıcıya bırakılmıştır.
- **Her düğüm** `id`, `unit`, `source_span`, `origin` (hangi formülatörden geldi) taşır.
- **Derleyiciler:** IR → SymPy, IR → Z3, IR → HiGHS/CVXPY, IR → python-flint (Arb), IR → pint (birim kontrolü),
  IR → Python değerlendirici (Mod B2 bağımsız yeniden hesap). Her derleyici kendi test takımıyla gelir.

### 6.3. Statik kapılar (çözücüden önce)

1. **Birim kapısı (pint):** Her ifadenin boyutu hesaplanır. `metre + saniye`, üs içinde birimli büyüklük,
   denklemin iki tarafında farklı boyut → `REFUSED (DIMENSION_MISMATCH)` veya, belirsizlik varsa, soru.
   Birim belirtilmemiş sayısal girdi → soru (K4). Birim dönüşümleri yalnızca pint ile yapılır.
2. **Serbestlik derecesi (DoF) ve yapısal analiz:** Denklem–bilinmeyen iki parçalı çizgesi (networkx) kurulur,
   maksimum eşleme bulunur, **Dulmage–Mendelsohn ayrıştırması** ile sistem eksik tanımlı (under-), tam tanımlı
   (well-) ve aşırı tanımlı (over-determined) bloklara ayrılır.
   - Eksik tanımlı blok → hangi büyüklüklerden biri verilirse sistemin kapanacağı hesaplanır ve kullanıcıya
     **somut aday listesiyle** sorulur ("Şu üçünden birini vermen gerekiyor: …"). K4.
   - Aşırı tanımlı blok → tutarlılık kontrolü (Z3 `assert_and_track` + `unsat_core`); çelişki varsa çelişen
     kurallar kaynak cümleleriyle gösterilir.
   - Yapısal olarak tam ama sayısal olarak tekil durumlar için çözüm noktasında sembolik Jakobiyen rank kontrolü (SymPy).
3. **Alan kontrolleri:** `sqrt`/`log` argümanları, sıfıra bölme olasılığı, işaret kısıtları. Belirsizse soru.

### 6.4. Red Team formülasyon katmanı (Tip-2'ye karşı)

**Formülatör adaptörleri (K6, K14):**
- `CLIFormalizer` — sahibin aboneliklerini **resmi istemciler üzerinden** kullanır: `claude -p --json-schema …`
  (Claude Code), `codex exec --output-schema …` (Codex CLI), `gemini -p … -o json` (Gemini CLI). Üçü de sahibin
  makinesinde kurulu (2026-11-07: Claude Code 2.1.302, codex-cli 0.167.0, Gemini CLI 0.64.0) ve headless +
  yapılandırılmış çıktıyı destekliyor. Abonelik bu şekilde, sağlayıcının kendi istemcisi içinde kullanılır (§8.2).
- `OpenAICompatibleFormalizer` — OpenAI uyumlu herhangi bir uç nokta: Groq gibi ücretsiz API'ler, ileride ücretli
  API'ler veya §8.2 sözleşmesine uyan bir yönlendirici.
- `AgentSuppliedIR` — çağıran ajanın gönderdiği IR bir aday sayılır.
- `MCPSamplingFormalizer` — istemci destekliyorsa (Claude Code'un MCP sampling desteği 2026-11 itibarıyla
  doğrulanamadı; opsiyonel, sistem ona bağımlı değil).

Her adaptör `model_family` (modeli eğiten kuruluş: Anthropic, OpenAI, Google, Meta, Alibaba, Moonshot…) ve
**yanıtı gerçekten üreten modelin kimliğini** (yanıttan okunur, istenen değil) kaydeder. Dikkat: Groq'taki
`gpt-oss` OpenAI ailesidir; Codex ile aynı aileden sayılır.

**CLI izolasyonu (Tasarımcı kararı):** CLI'lar kendi sistem promptlarını, bellek dosyalarını (`CLAUDE.md`,
`AGENTS.md`, `GEMINI.md`, kullanıcının global talimatları), MCP sunucularını ve araçlarını ekleyebilir. Bağımsızlık
ve tekrarlanabilirlik için her çağrı: boş geçici bir çalışma dizininde, araçsız (`--tools ""` / salt-okunur mod),
MCP'siz (`--strict-mcp-config`), oturum kalıcılığı kapalı (`--no-session-persistence`, `--ephemeral`), otomatik model
yedeği (fallback) kapalı ve açık model adıyla çalışır. Kullanıcının global bellek/talimat dosyalarının bu modda
gerçekten yüklenmediği uygulamada her CLI için test edilir; edilemiyorsa o CLI'ın adayı raporda "izolasyon
doğrulanamadı" olarak işaretlenir.

**Hız sınırları:** Ücretsiz katmanların istek/token sınırları vardır. K2 (süre sınırsız) gereği Rigor sınırlara
takıldığında bekler; kuyruk diske yazılır, yeniden başlatmada devam eder. Hız sınırı nedeniyle başka bir modele
**sessizce geçilmez**.

Adımlar:
1. **Bağımsız formülasyon:** Aynı problemden K aday IR üretilir (**Tasarımcı kararı:** varsayılan K=3; mümkün
   olduğunda farklı model ailelerinden). Formülatörler birbirlerinin çıktısını görmez.
2. **Hizalama:** Adayların değişken adları farklı olabilir; değişkenler kaynak aralığı + birim + rol üzerinden
   eşlenir. Eşleme belirsizse (SOVER'daki tek hata kaynağı buydu) soru olur, tahmin yapılmaz.
3. **Denklik kontrolü:** Her aday çifti için:
   - Mantıksal/doğrusal kısıtlar: Z3'te `Not(F1 ⇔ F2)` → `unsat` ise eşdeğer; `sat` ise **karşı örnek**.
   - Cebirsel/kalkülüs ifadeleri: SymPy ile `simplify(e1 - e2) == 0` + rastgele rasyonel noktalarda kesin
     değerlendirme; sembolik kanıt yoksa sayısal eşitlik yalnızca destekleyici kanıt sayılır.
   - Doğrusal olmayan reel kısıtlar: δ-tamamlı kontrol (dReal) opsiyonel arka uç.
4. **Karar kuralı (K2 gereği):** **Oybirliği.** Tek bir aday bile ayrışırsa sistem durur. Ayrışmayı sağlayan karşı
   örnek sade dile çevrilip kullanıcıya soru olarak gelir: "Metindeki 'en fazla 3 kademe' ifadesi iki şekilde
   okunabiliyor: (a) … (b) … Hangisi?" Kullanıcının cevabı IR'a işlenir, katman yeniden koşar.
5. **Roundtrip:** Konsensüs IR'ı, orijinal problemi **görmeyen** bir formülatöre doğal dile geri çevirtilir; bu
   metin tekrar formüle edilir; sonuç konsensüs IR'ı ile denklik kontrolünden geçer. Uyuşmazlık → hangi aşamanın
   bozulduğu teşhis edilir, soru üretilir.
6. **Mutasyon/sınır testi:** IR'daki karşılaştırma yönleri, işaretler ve sabitler sistematik olarak değiştirilir;
   her mutasyonun sonucu değiştirdiği doğrulanır (değiştirmiyorsa o kısıt sonuç üzerinde etkisizdir ve raporda
   "etkisiz kısıt" olarak işaretlenir). Değişkenler 0, sınır ve negatif değerlerde zorlanır.
7. **İnsan onayı:** Sade anlatım ① (§6.7) kullanıcıya gösterilir. Onay olmadan çözüme geçilmez.

### 6.5. Çözüm: yönlendirici ve motorlar

Yönlendirici, IR'ın yapısına bakarak (doğal dile değil) motoru seçer:

| Problem yapısı | Birincil motor | Bağımsız ikinci yol |
|---|---|---|
| Mantık, tamsayı/boolean kısıtlar, kural tutarlılığı | Z3 (`Solver`, sonra gerekiyorsa `Optimize`) | CVC5 veya kaba kuvvet (küçük alanlarda) |
| Cebir, analitik çözüm, türev/integral | SymPy | python-flint/Arb ile sayısal kontrol |
| LP/MILP | HiGHS (`highspy`) | Z3 (küçük) veya CVXPY; dual sertifika rasyonel aritmetikle kontrol |
| Konveks optimizasyon | CVXPY | KKT koşullarının bağımsız kontrolü |
| Sayısal kök, integral | python-flint/Arb (kesin hata sınırlı) | mpmath yüksek hassasiyet |
| ODE (ör. roket irtifası) | SciPy `solve_ivp` (DOP853) | farklı integratör (Radau) + adım yarılama yakınsama testi; tam uçuş simülasyonunda opsiyonel RocketPy karşılaştırması |
| `Decimal` hesapları (Mod B) | IR değerlendirici (`decimal` modülü, açık bağlam) | Rational ile kesin hesap + yuvarlama kuralının ayrıca uygulanması |

Bilinen Z3 tuzakları (Handoff §2.3): `Optimize` `assert_and_track`'i desteklemez → önce `Solver` ile tutarlılık,
sonra `Optimize`. Doğrusal olmayan tamsayı aritmetiği `unknown` dönebilir → zaman aşımı zorunlu; `unknown` asla
sonuç sayılmaz (`REFUSED (SOLVER_UNKNOWN)` veya başka motora yönlendirme). K2 gereği zaman aşımları cömerttir ve
yapılandırılabilir, ama sonsuz değildir.

İki yol aynı sonucu vermezse: `REFUSED (ENGINE_DISAGREEMENT)` + iki sonuç raporda. "Aynı sonuç": kesin yollarda
birebir eşitlik; sayısal yollarda iki yolun kesin/tahmini hata sınırlarının örtüşmesi; ODE'de yakınsama testinden
türetilen tolerans içinde kalma. Bu kural **aynı IR modelini** çözen iki yol içindir; farklı fiziksel model
kullanan dış araçlarla (RocketPy, OpenRocket) karşılaştırma yalnızca raporlanır (§5.3).

### 6.6. Sertifika

- Bulunan çözüm **orijinal** (konsensüs) IR kısıtlarına kesin aritmetikle (Rational) ya da Arb top aritmetiğiyle
  geri konur; her kısıt için "sağlandı / sağlanmadı / belirsiz (aralık sıfırı içeriyor)" kaydedilir.
- `unsat` iddiaları için unsat core; LP optimalliği için dual çözümün rasyonel aritmetikle kontrolü ve sıfır
  optimalite boşluğu; sayısal sonuçlar için kesin hata sınırı.
- ODE sonuçlarında formal sertifika yoktur (Python'da hazır, kanıt üreten ODE çözücüsü bulunamadı); bu yüzden
  ODE içeren sonuçlar en fazla `CROSS_VALIDATED` olur ve raporda tolerans, adım sayıları ve yakınsama tablosu yer alır.

### 6.7. Sade anlatım (K7)

Sade anlatım iki yerde kullanılır:
- **① Onay anlatımı:** "Problemi şöyle anladım": ne biliniyor, ne aranıyor, hangi kural/denklem neden var,
  hangi varsayımlar yapıldı (hepsi kullanıcı onaylı), birimler.
- **② Sonuç anlatımı:** "Sonuç şu, çünkü…": adım adım, her adım bir IR düğümüne ve sertifikadaki bir değere bağlı.

**Üretim yöntemi (anlatımın kendisinin halüsinasyonuna karşı, A4):**
1. **İskelet deterministiktir:** Onaylı IR'dan ve çözüm izinden, her adımı bir IR düğümüne bağlı bir yapı üretilir
   (adım id'si, kullanılan değerler, sonuç değeri, birim).
2. **Sadeleştirme LLM'e yaptırılır:** LLM iskeleti basit Türkçeye çevirir; kural: kısa cümleler, her teknik
   terim ilk geçtiğinde günlük dille açıklanır, mümkünse somut benzetme, sayılar birimiyle birlikte.
3. **Anlatım koruması:** Üretilen metindeki her sayı, birim ve karşılaştırma ifadesi ("en az", "en fazla",
   "artar", "azalır") çıkarılır ve iskeletle/sertifikayla eşleştirilir. Eşleşmeyen tek bir öğe → metin reddedilir,
   yeniden üretilir; üç denemede geçmezse deterministik iskelet metni (daha az akıcı ama doğru) kullanılır.
4. **Anlam roundtrip'i (onay anlatımı için):** Onay anlatımı, problemi görmeyen bir formülatöre tekrar formüle
   ettirilir ve konsensüs IR ile denklik kontrolü yapılır. Anlatım IR'ı doğru taşımıyorsa kullanıcıya gösterilmez.
5. **Okunabilirlik ölçümü:** Türkçe için Ateşman okunabilirlik puanı hesaplanır; **Tasarımcı kararı:** hedef ≥ 70
   ("kolay"). Altında kalırsa sadeleştirme tekrarlanır. İngilizce destek eklenirse Flesch Reading Ease kullanılır.
   Formül ölçümü tek başına yeterli değildir; jargon listesi kontrolü de yapılır (§6.7 adım 2'deki kural).

**Tasarımcı kararı:** Varsayılan anlatım dili Türkçe; `language` yapılandırmasıyla İngilizce eklenebilir.

### 6.8. Kanıt raporu (K5)

Markdown (ve isteğe bağlı HTML) olarak üretilir; arkadaşlara gönderilebilir. Bölümler:

1. **Özet kutusu:** sonuç + etiket + tek cümlelik sade açıklama.
2. **Sade anlatım ②.**
3. **Problemin onaylı tanımı:** sade anlatım ① + formal IR'ın okunur hali (denklemler).
4. **Varsayımlar ve girdiler:** her biri kaynağıyla (`USER_DIRECT` / `VIA_AGENT_UNVERIFIED` / metinden).
5. **Doğrulama şartları tablosu:** etiketin her şartı, geçti/geçmedi, kanıtı.
6. **Red Team kaydı:** kaç formülatör, hangi model aileleri, ayrışmalar ve nasıl çözüldükleri, roundtrip sonucu,
   mutasyon testi özeti.
7. **Çözüm ve sertifika:** motorlar, sonuçlar, geri ikame tablosu, hata sınırları.
8. **Kapsam uyarıları:** fiziksel model doğruluğu garanti edilmez vb.
9. **Yeniden üretim:** Rigor sürümü, motor sürümleri, model adları/sürümleri, IR'ın ve oturum kaydının SHA-256
   hash'i, rastgele tohumlar. `rigor replay <oturum>` ile LLM çağrısı yapmadan (kaydedilmiş IR'dan) çözüm ve
   sertifika yeniden üretilebilir.

### 6.9. Onaylı şablonlar ve öz-denetim (K18)

**Şablon:** Onaylanmış bir formülasyon (konsensüs IR + K aday IR + onay kaydı + kullanılan model sürümleri) adıyla
kaydedilir. Sonraki kullanımda yalnızca `given` değerleri değişiyorsa Red Team ve onay tekrarlanmaz; birim/DoF/alan
kapıları, iki bağımsız çözüm yolu ve sertifika **her seferinde** yeniden koşar. Etiket korunur; raporda
"onaylı şablon: {ad}, onay tarihi, son öz-denetim" yazar. Şablon yalnızca adıyla ve yeni `given` değerleriyle
çağrılır (`rigor_template(ad, değerler)`); yeni bir doğal dil metni gönderilirse tam süreç koşar (Rigor eşleşen bir
şablon görürse bunu yalnızca önerir). Formülasyonun yapısı veya kullanılan model sürümü değişirse şablon geçersiz
olur ve tam süreç tekrar koşar. Mod B2'de (§5.2) aynı şablon toplu mutabakat için ve pytest içinden çağrılabilir.

**Öz-denetim (LLM yok, tamamen deterministik):** Şu adımların hepsi geçmelidir:
1. **Bütünlük:** Şablon IR'ının SHA-256'sı onay kaydındakiyle aynı mı (dosya bozulması, elle değişiklik).
2. **Konsensüs yeniden kanıtı:** Kayıtlı K aday IR ile şablon IR arasındaki denklik Z3/SymPy ile yeniden kanıtlanır.
3. **Statik kapılar:** Birim, DoF ve alan kontrolleri, son kullanımlarda görülen değer aralıklarının tamamıyla.
4. **Regresyon:** Onay sırasındaki örnek hesap ve son kullanımların girdileri iki bağımsız yolla yeniden çözülür;
   sonuçlar ve sertifikalar kayıtlı olanlarla karşılaştırılır (motor/kütüphane sürümü değişmişse fark burada çıkar).
5. **Model kütüphanesi regresyonu:** Şablonun kullandığı modellerin referans tablo testleri (§4.5) yeniden koşar.
6. **Geçerlilik aralığı:** Son kullanımlardaki girdiler modellerin geçerlilik aralığında mı (ör. Barrowman Mach sınırı).
   Dışına taşan kullanım varsa denetim başarısız olur.
7. **Beklenen davranışlar:** Şablon onaylanırken her şablona deterministik olarak sınanabilecek özellikler
   eklenir ve kullanıcı bunları da onaylar: sınır durumları (ör. itki 0 → irtifa 0), monotonluk (ör. kuru kütle
   artarsa tepe irtifası azalır), boyutsal ölçekleme, bilinen özel değerler. Kütüphane modelleri kendi özellik
   listeleriyle gelir; diğerlerini Rigor onay sırasında önerir, kullanıcı ekler veya çıkarır. Öz-denetimde bu
   özellikler Hypothesis ile rastgele ve uç girdilerde sınanır.

**Ne zaman koşar (Tasarımcı kararı, yapılandırılabilir):** (a) aynı şablon son öz-denetimden bu yana 7 gün içinde 5
kez kullanıldığında, bir sonraki kullanımdan önce; (b) Rigor, motor veya model kütüphanesi sürümü değiştiğinde, ilk
kullanımdan önce; (c) elle: `rigor selfcheck [şablon]` / MCP `rigor_selfcheck`.

**Başarısızlıkta (fail-closed):** Şablon askıya alınır, kullanım `REFUSED (TEMPLATE_SELF_CHECK_FAILED)` döner, hangi
adımın neden kaldığı sade dille anlatılır. Son başarılı öz-denetimden sonra o şablonla üretilmiş tüm sonuçlar
listelenir ve raporları "şüpheli — yeniden doğrulanmalı" olarak işaretlenir.

**Sınır:** Öz-denetim LLM kullanmadığı için formülün **problem metnine uygunluğunu** (Tip-2) tek başına yeniden
kanıtlayamaz. Bu boşluk §6.9.1'deki hakem süreciyle kapatılır.

#### 6.9.1. Alarm hakemliği ve öğrenme (K19)

**Alarm sınıfları (Tasarımcı kararı):**
- **Kesin alarm** — bütünlük (hash), konsensüs denkliği, sertifika, motorlar arası uyuşmazlık. Bunlar yoruma açık
  değildir; LLM'e sorulmaz. Rigor hangi sürümün/dosyanın değiştiğini deterministik olarak teşhis eder ve şablon
  ancak tam süreçten (Red Team + onay) geçerek açılır.
- **Yorumlu alarm** — beklenen davranış ihlali, regresyonda kayıtlı örnekle uyuşmazlık, geçerlilik aralığı ihlali,
  açıklanamayan büyük OpenRocket farkı (§6.10). Bunlar ya gerçek bir formül hatasıdır ya da kontrolün kendisi yanlış
  kurulmuştur (ör. beklenen davranış her bölgede geçerli değil).

**Geçmiş taraması:** Yorumlu bir alarmda Rigor önce aynı kontrolü şablonun onay anındaki örneğine ve kayıtlı tüm
geçmiş kullanımlarına deterministik olarak uygular:
- Hata **yeni** ise (yalnızca son kullanımlarda var): büyük olasılıkla girdiler yeni bir bölgeye taşınmıştır.
  Rigor bölgeyi ve ilk görüldüğü kullanımı gösterir; LLM çağrılmaz.
- Hata **geçmişte de varsa** (onaydan beri hep oradaysa): ya formül baştan yanlıştı (Red Team'den kaçmış bir Tip-2)
  ya da kontrol yanlıştı. **Bu durumda hakem paneli çağrılır.**

**Hakem paneli (LLM):**
1. ≥2 farklı model ailesinden, birbirini görmeyen, §6.4 izolasyon kurallarıyla çalışan hakemler.
2. **Kör adım:** Hakemlere önce yalnızca problem metni verilir ve ihlal edilen davranış soru olarak sorulur
   ("Kuru kütle artarsa tepe irtifası nasıl değişmeli? Hangi koşullarda?"). Formül ve alarm gösterilmez. Böylece
   hakem, "kilidi açacak" cevaba yönlendirilmez.
3. **Açık adım:** Sonra formülün okunur hali, ihlal edilen kontrol ve deterministik karşı örnek (girdi + çıktı)
   gösterilir. Yapılandırılmış cevap: `FORMÜL_HATALI | KONTROL_HATALI | İKİSİ_DE | BELİRSİZ` + gerekçe + IR olarak
   düzeltme önerisi (düzeltilmiş formül veya daraltılmış/düzeltilmiş kontrol).
4. **Önerilerin deterministik sınanması:** Düzeltilmiş formül tüm kontrollerden ve kayıtlı örneklerden geçmeli.
   Düzeltilmiş kontrol tüm geçmişte tutmalı **ve** mutasyon testlerinde (§6.4 adım 6) hâlâ aynı bozulmaları
   yakalamalı. Bu, "kontrolü gevşeterek alarmı susturan" bir düzeltmeyi reddeder.
5. **Karar her zaman kullanıcınındır:** Panelin oybirliği ve sınama sonucu sade dille kullanıcıya sunulur; şablonu
   açmak veya alarmı "yanlış alarm" saymak yalnızca `USER_DIRECT` bir kararla olur. Panel ayrışırsa ya da `BELİRSİZ`
   derse iki görüş de gösterilir, şablon kilitli kalır. **LLM tek başına hiçbir alarmı kapatamaz** (A1).
6. Sonuç `FORMÜL_HATALI` ise: şablon emekliye ayrılır, düzeltilmiş formül tam süreçten geçer, eski sonuçlar
   "yanlış olabilir" listesine alınır ve yeni formülle yeniden hesaplanabilir.

**Öğrenme (Tasarımcı kararı: kurallı, açık, geri alınabilir; eğitilmiş model değil):** Garanti verebilmek için
öğrenilen her şey okunabilir bir kural olarak saklanır; istatistiksel bir model eğitilmez.
- **Karar defteri:** Her hakem süreci (alarm imzası, panel cevapları, kullanıcı kararı, düzeltme) kalıcı kaydedilir.
- **Gerçek hatadan öğrenme (kontrol ekler):** Karşı örnek kalıcı bir test olur; ihlal edilen davranış aynı modeli
  kullanan diğer şablonlara da önerilir; Red Team'den kaçan hata türü mutasyon kütüphanesine eklenir. Böylece aynı
  hata bir daha Red Team aşamasında yakalanır.
- **Yanlış alarmdan öğrenme (kontrolü daraltır):** Kontrolün düzeltilmiş hali sürümlü bir **istisna** olarak
  kaydedilir: kapsam (şablon/model), gerekçe, onaylayan, tarih. İstisna her öz-denetimde yeniden sınanır (hâlâ
  gerekçesine uyuyor mu, mutasyon yakalama gücü düşmedi mi); raporda yürürlükteki istisnalar listelenir; kullanıcı
  istediği an geri alabilir.
- **Asla:** bir kontrolü sessizce silmek, istisnayı kapsamı dışına genellemek, ajan aracılığıyla gelen
  (`VIA_AGENT_UNVERIFIED`) bir kararla `PROVEN` sonuçları etkileyen istisna oluşturmak.
- Aynı kontrol farklı şablonlarda tekrar tekrar yanlış alarm veriyorsa Rigor bunu kütüphane düzeyinde bir düzeltme
  önerisi olarak sunar; uygulanması model kütüphanesi doğrulamasını (§4.5) yeniden gerektirir.

### 6.10. OpenRocket karşılaştırması (K17)

- **Girdi:** OpenRocket `.ork` dosyası (zip içinde XML; tasarım, fırlatma koşulları ve kayıtlı simülasyon özetleri)
  ve/veya simülasyon CSV dışa aktarımı (zamana göre irtifa, hız, ivme, Mach, CG/CP konumu, stabilite marjı, Cd).
  Dosyalar güvenilmez veri sayılır: XML `defusedxml` ile, boyut ve zip-bomb sınırlarıyla okunur. Her değer `USER_FILE`
  kaydı alır (§4.3).
- **Önce girdi eşleşmesi:** Karşılaştırma ancak iki taraf **aynı girdilerle** hesaplıyorsa anlamlıdır. Rigor
  `.ork`'taki fırlatma koşullarını (saha yüksekliği, rampa uzunluğu ve açısı, rüzgâr, sıcaklık/basınç, motor ve
  gecikme, kütle) kendi girdileriyle karşılaştırır; farklı olan her girdi tabloda gösterilir ve o karşılaştırma
  "girdiler farklı" diye işaretlenir.
- **Karşılaştırılan büyüklükler (en az):** tepe irtifası, tepeye varış süresi, maks. hız ve Mach, maks. ivme, rampadan
  çıkış hızı, 0,3 Mach'taki stabilite marjı, CG ve CP konumu, kuru/ıslak kütle, paraşüt iniş hızları.
- **Rapor:** Her büyüklük için Rigor değeri (etiketiyle), OpenRocket değeri, fark ve yüzde fark, ve bilinen model
  farkları (ör. OpenRocket genişletilmiş Barrowman, kendi sürükleme modeli ve 6-SD yörünge kullanır; Rigor v1 3-SD).
  **Tasarımcı kararı:** fark %5'i aşarsa uyarı çıkar; eşik yapılandırılabilir. Fark sonucu reddetmez ama
  açıklanmamış büyük farklar sade dille "şunları kontrol et" listesiyle sunulur. Aynı açıklanamayan fark kayıtlı
  geçmiş karşılaştırmalarda da sürüyorsa §6.9.1 hakem süreci isteğe bağlı olarak çalıştırılabilir ("model farkı mı,
  hata mı?").
- Kapalı formlu, aynı modelin kullanıldığı büyüklüklerde (ör. kütle toplamı, CG) fark bir model farkı olamaz; burada
  fark varsa bu bir **girdi veya hesap hatası işareti** olarak ayrıca vurgulanır.

---

## 7. Arayüzler (K3)

### 7.1. Python SDK

Çekirdek kütüphanedir; MCP sunucusu bunun üstünde ince bir kabuktur. Taslak kullanım:

```python
import rigor

s = rigor.Session(config=rigor.Config.load())          # formülatörler, politikalar
step = s.submit("Roketin kuru kütlesi 12 kg, ... maksimum irtifa ne olur?")
while step.state in {"NEEDS_INPUT", "NEEDS_CONFIRMATION"}:
    step = s.answer(step, ...)                          # kullanıcı cevabı / onay
result = step.result                                    # label, value, explanation, report
result.report.write("rapor.md")
```

Ayrıca: `s.submit_ir(ir_json)` (formülasyonu kendisi getiren çağıranlar için), `rigor.audit_formula(formül, referans?)`
(Mod B1 / iddia denetimi), `rigor.reconcile(şablon, veri_dosyası)` (Mod B2),
`rigor.replay(session_id)`, `rigor.templates` (şablon kaydı/kullanımı), `rigor.selfcheck(template)`,
`rigor.compare_openrocket(result, ork_or_csv)`.

### 7.2. MCP sunucusu

- **SDK:** resmi `mcp` Python SDK 2.x (2026-11 itibarıyla PyPI'da 2.3.0). Taşıma: stdio (yerel).
- **Araçlar (taslak):** `rigor_solve(problem, ir?)`, `rigor_answer(session_id, answers)`,
  `rigor_confirm(session_id, decision, corrections?)`, `rigor_audit_formula(formula, reference?)`,
  `rigor_reconcile(template, data_path)`, `rigor_adjudication(template)` (hakem sonucunu görme/karar),
  `rigor_report(session_id)`, `rigor_status(session_id)`, `rigor_template(name, givens)`, `rigor_selfcheck(name?)`,
  `rigor_compare_openrocket(session_id, path)`.
- **Kullanıcıyı sıkıştırma (K4) yolu:**
  1. İstemci MCP **elicitation** destekliyorsa (Claude Code 2.1.76'dan itibaren destekliyor — ikincil kaynaklardan;
     kurulumda doğrulanmalı) Rigor soruyu doğrudan kullanıcıya form olarak sorar → girdi `USER_DIRECT`.
  2. Desteklemiyorsa araç `NEEDS_INPUT` durumunu yapılandırılmış soru listesiyle döndürür; ajan kullanıcıya sorup
     `rigor_answer` ile iletir → girdi `VIA_AGENT_UNVERIFIED` (§4.3). Araç açıklamalarında ajana "bu soruları
     kendin cevaplama, kullanıcıya sor" talimatı açıkça yer alır.
- Onay (`NEEDS_CONFIRMATION`) için de aynı iki yol geçerlidir.
- **Tasarımcı kararı:** Sahibin kullandığı Claude Code sürümünde elicitation'ın gerçekten çalıştığı, MCP aşamasını
  beklemeden erken bir deneyle (küçük bir deneme sunucusu) doğrulanır; sonuç, MCP üzerinden `PROVEN`'a
  ulaşılabilirliği belirler.
- Oturumlar sunucu yeniden başlasa da diskten devam eder.

---

## 8. Kısıtlar ve teknoloji

### 8.1. Python sürümü (K11) — Red Team bulgusu

Sahip, lazy import için Python 3.15 öneriyor. İnceleme (2026-11-07):

- **Özellik gerçek ve uygun:** PEP 810 (Final) `lazy import x` / `lazy from x import y` sözdizimini 3.15'e getirdi;
  3.15.0 2026-10-09'da yayımlandı (ikincil kaynaklar). SymPy, SciPy, CVXPY gibi ağır kütüphaneler yalnızca gerektiğinde
  yüklenir; MCP sunucusunun ve CLI'nin açılışı hızlanır. Gerekçe geçerli.
- **Engel 1 — bağımlılık wheel'leri:** 2026-11-07 itibarıyla PyPI'da macOS arm64 için **cp315 wheel'i olmayanlar**:
  `python-flint` 0.9.0 (Arb, yani kesin hata sınırlarının temeli), `highspy` 1.15.1 (LP/MILP), `cvxpy` 1.9.3, `osqp`,
  `cantera` 3.2.0. Bunlar ya kaynaktan derlenmeli (C/C++ derleyici ve FLINT kütüphanesi gerekir) ya da wheel'ler
  çıkana kadar beklenmeli. `numpy`, `scipy`, `pydantic-core`, `scs`, `crosshair-tool` hazır; saf Python paketler sorunsuz.
  `jacobian` 0.23 `<3.14` istediği için 3.15'te kullanılamaz.
- **Risk 2 — hataların gecikmesi (A1 açısından önemli):** Lazy import'ta `ImportError` import satırında değil ilk
  kullanımda çıkar. Bir çözücü arka ucu eksikse bu, boru hattının ortasında ortaya çıkar. **Önlem (Tasarımcı
  kararı):** oturum başlamadan önce yapılandırılmış tüm arka uçları gerçekten yükleyip sürümlerini kaydeden bir ön kontrol
  (`rigor doctor`) çalışır; eksik varsa fail-closed.
- **Kısıt 3:** `lazy` yalnızca modül düzeyinde ve `try` bloğu dışında kullanılabilir; opsiyonel bağımlılıklar
  (`dreal`, `cantera`) `importlib.util.find_spec` ile tespit edilmeli.
- **Kısıt 4:** `lazy` anahtar kelimesi 3.14 ve öncesinde `SyntaxError` verir. Kütüphane bu durumda yalnızca 3.15+'ta
  çalışır; takım arkadaşlarının da 3.15 kurması gerekir. PEP 810'daki `__lazy_modules__` listesi aynı lazy davranışı
  3.15'te sağlar ve eski sürümlerde sessizce yok sayılır (orada import'lar normal yüklenir).
**Karar (K11): seçenek (b).** `requires-python = ">=3.12"`, geliştirme ve birincil hedef 3.15, CI 3.12/3.14/3.15.
Kaynak kodda `lazy` anahtar kelimesi kullanılmaz; ağır modüller `__lazy_modules__` listesine yazılır. `rigor doctor`
her ortamda zorunlu ön kontroldür.

### 8.2. LLM yönlendiricileri (OmniRoute vb.) — Red Team bulgusu ve sözleşme

`cheaper-inference/OmniRoute` (v3.8.54, MIT, ~27.700 dosya; 2026-11-07'de incelendi) 380 sağlayıcıyı tek OpenAI
uyumlu uç noktada toplayan bir ağ geçidi. Varsayılan davranışlarından birkaçı Rigor'un garantilerini **doğrudan bozar**:

| OmniRoute özelliği | Rigor'a etkisi |
|---|---|
| **Semantik yanıt önbelleği** (`temperature=0` yanıtlarını önbellekler) | K "bağımsız" formülasyon tek bir önbellek yanıtından gelebilir → **sahte oybirliği → sahte `PROVEN`** (A1). En ağır risk. |
| **Otomatik yedekleme (auto-fallback, combo)** | İstenen model yerine başka model cevap verebilir → model ailesi sayımı yanlış olur, bağımsızlık iddiası çöker. |
| **İstem sıkıştırma** (RTK → Caveman, LLMLingua…; istek içeriğini şeffafça değiştirir) | Problem metni kayıplı sıkıştırılırsa "en az/en fazla", birim, sayı kaybolabilir → altyapı Tip-2 hata **üretir**. |
| **Bellek / guardrail / bağlam enjeksiyonu** | Formülatörler birbirinin ya da önceki oturumların bağlamını görebilir → bağımsızlık bozulur. |
| **Abonelik OAuth köprüleri** (`claude` = Claude Code OAuth, `agy` = Antigravity, `codex`, ChatGPT Web köprüsü, "TLS stealth") | Anthropic, Şubat 2026'dan beri Free/Pro/Max OAuth token'larının Claude Code ve Claude.ai dışında kullanımını açıkça yasaklıyor (ikincil kaynaklar; hesap kapatma riski). OmniRoute'un kendi kataloğu Antigravity için de ToS yasağı not ediyor. |
| **Kendi belgelerinde çelişki** | README "`tos: avoid` sağlayıcılar otomatik yönlendirmeden hariç" diyor; `FREE_TIERS.md` "ToS bayrağı yalnızca bilgi amaçlı, yönlendirmeyi engellemez" diyor. |
| **Saldırı yüzeyi** | MITM/TPROXY (yerel CA kurulumu), Electron, uzak mod, 110 MCP aracı; çok büyük bağımlılık ağacı. |

**Karar (K15, sahip onayladı):**
1. Abonelikler **yalnızca resmi CLI'lar üzerinden** kullanılır (`CLIFormalizer`); OmniRoute veya benzeri bir araçla
   abonelik OAuth'u köprülenmez.
2. OmniRoute (veya LiteLLM gibi başka bir ağ geçidi) yalnızca **ücretsiz/API anahtarlı** sağlayıcılara erişim için,
   aşağıdaki **geçiş sözleşmesine** uyduğu sürece opsiyonel bir `OpenAICompatibleFormalizer` uç noktası olabilir.
   Varsayılan değildir; varsayılan, Groq vb. sağlayıcılara doğrudan bağlantıdır.

**Geçiş sözleşmesi (her ağ geçidi için; Rigor her yanıtta kontrol eder, ihlalde yanıt atılır = fail-closed):**
- Sıkıştırma kapalı: her istekte `x-omniroute-compression: off`; yanıttaki `X-OmniRoute-Compression` başlığı `off`
  değilse yanıt reddedilir.
- Yedekleme yok: istek açık `sağlayıcı/model` ile yapılır (`auto`/combo yasak); yanıttaki `X-OmniRoute-Decision`
  başlığı ve yanıt gövdesindeki model kimliği istenenle eşleşmezse yanıt reddedilir.
- Önbellek yok: semantik önbellek kapatılır. Ek savunma olarak her formülatör çağrısı benzersiz bir istek kimliği
  taşır ve aynı oturumdaki iki adayın ham yanıtı bayt bayt aynıysa ikisi de reddedilir.
- Bellek/guardrail/bağlam enjeksiyonu kapalı; MITM/TPROXY kurulmaz; ağ geçidi yalnızca `127.0.0.1`'e bağlanır.
- Ağ geçidinin sürümü ve yapılandırması kanıt raporuna yazılır.

Bu kurallar genel bir ilkenin uygulamasıdır: **Rigor ile model arasındaki her katman (ağ geçidi, proxy, önbellek)
güvenilmez kabul edilir**; bağımsızlık ve model kimliği her yanıtta Rigor tarafından doğrulanır.

### 8.3. Diğer kısıtlar

- **Python sürümü:** §8.1 (K11). Paket yöneticisi: `uv`. Test: `pytest` + Hypothesis.
- **Çekirdek bağımlılıklar (2026-11 PyPI sürümleri):** pydantic 2.14, sympy 1.14, z3-solver 5.3, pint 0.26,
  python-flint 0.9, mpmath 1.4, networkx 3.7, highspy 1.15, cvxpy 1.9, scipy, mcp 2.3, openpyxl, defusedxml,
  hypothesis 6.170 (öz-denetim ve beklenen davranış testleri).
- **Opsiyonel:** rocketpy 1.13 (roket karşılaştırması),
  dreal 4.21 (sistem kütüphaneleri ister; opsiyonel), jacobian 0.23 (değerlendirilecek, aşağıya bakın).
- **LLM SDK'ları:** anthropic, openai, google-genai — hepsi opsiyonel extra; API anahtarları ortam değişkeninden
  veya yapılandırma dosyasından, asla rapora yazılmaz.
- **Güvenlik:** LLM çıktısı hiçbir zaman kod olarak çalıştırılmaz (A3). Rigor kullanıcının kodunu da çalıştırmaz
  (K13, K20); okuduğu dosyalar (`.eng`, xlsx, CSV, `.ork`, bot çıktıları) yalnızca veri olarak ayrıştırılır.
- **Hazır parçalar hakkında:** `usolver` arşivlenmiş; `sympy-mcp` `parse_expr` (içeride `eval`) kullandığı için
  A3'ü ihlal eder; `jacobian` aktif ve iyi bir işlem sözlüğü ama birim, DoF ve formülasyon katmanı yok. Rigor bu
  katmanları kendisi yazar; motorlara doğrudan bağlanır. `jacobian`'ın arka uç olarak kullanılması uygulayıcının
  değerlendirmesine bırakılmıştır.

### 8.4. Depo, dallar ve sürüm akışı (K23)

- **`development`:** tüm geliştirme buraya gelir. Büyük işler istenirse `development`'tan açılan kısa ömürlü dallarda
  (`feature/…`, `fix/…`) yapılır ve `development`'a birleştirilir.
- **`main`:** yalnızca kararlı son sürüm. `main`'e doğrudan commit atılmaz; değişiklik `development` → `main` pull
  request'iyle gelir. **Tasarımcı kararı:** her `main` birleştirmesi bir sürümdür ve SemVer etiketi alır (`v0.1.0`,
  …); ilk etiket, 1. aşama (çekirdek) kullanılabilir olduğunda. Tasarım aşamasında `main` yalnızca onaylı
  belgeleri taşır.
- **Birleştirme şartı (kod geldiğinde):** `development` → `main` PR'ında testler (3.12/3.14/3.15) ve altın test seti
  yeşil olmalı; altın sette yanlış `PROVEN` = 0 (§9).
- **GitHub ayarı (Tasarımcı kararı):** varsayılan dal `main` (ziyaretçi kararlı sürümü görür); `main` korumalı:
  PR zorunlu, force-push ve silme kapalı. Tek geliştirici olduğu için PR onayı zorunlu değildir.
- **Gizlilik:** `docs/private/`, `private/` ve `.rigor/` git'e girmez. Herkese açık belgeler özel repoların kimliğini
  (ad, link, dosya yolu, sürüm) içermez.

---

## 9. Rigor'un kendi doğrulanması

"Sıfır halüsinasyon" iddiası test edilmeden anlamsızdır.

- **Altın test seti:** Elle doğrulanmış problemler + beklenen etiket. İçinde mutlaka: "en az/en fazla" tuzakları,
  birim tuzakları (N/lbf, m/ft, %/oran), eksik parametreli problemler (beklenen: `NEEDS_INPUT`), çelişkili
  problemler (beklenen: `REFUSED (INCONSISTENT)`), iki yoruma açık ifadeler (beklenen: soru), roket örnekleri,
  `Decimal` yuvarlama örnekleri.
- **Ana metrik:** Altın sette **yanlış `PROVEN` sayısı = 0** (A1). İkincil: gereksiz soru oranı, çözülebilen problem oranı.
- **Mutasyon testi:** Doğru IR'lar bilerek bozulur (karşılaştırma yönü, birim, işaret); Red Team katmanının
  bunları yakalaması beklenir.
- **Derleyici testleri:** Her IR → motor derleyicisi için, rastgele IR'larda motorlar arası tutarlılık (diferansiyel test).
- **Test verileri (Tasarımcı kararı):** Şartname PDF'leri, yarışma motor dosyaları ve takımın verileri repoya
  konmaz; testler sentetik ama aynı biçimdeki dosyalarla (ör. CR satır sonlu `.eng`) yazılır. Gerçek dosyalarla
  yerel, repoya girmeyen bir kabul testi koşulabilir.
- Herkese açık setlerden faydalanılabilir (ör. GSM-Hard, NL4Opt türü optimizasyon setleri) ama asıl ölçüt sahibin
  kendi alanlarından (roket, bot) gelen örneklerdir.

---

## 10. Sıra (Tasarımcı kararı; hedef K16)

Ayrıntılı takvim yok (K16). Her aşamanın sonunda araç o ana kadarki özelliklerle gerçekten kullanılabilir olur;
roket hesapları son aşamayı beklemeden başlayabilir.

1. **Çekirdek:** IR + Python kurucu API, birim/DoF/alan kapıları, SymPy/Z3/Arb derleyicileri, sertifika, rapor,
   `rigor doctor`, ince MCP + elicitation deneyi. Kullanılabilir: R1–R4, R7–R11 elle kurulan IR ile (`CROSS_VALIDATED`, §4.4).
2. **Roket fiziği:** §5.4 model kütüphanesi + doğrulamaları (§4.5), `.eng`/xlsx/CSV/`.ork` okuyucular, ODE +
   yakınsama, OpenRocket karşılaştırması (§6.10). Kullanılabilir: R5, R6.
3. **Red Team + doğal dil:** ayrıştırma, CLI/Groq formülatör adaptörleri, hizalama, denklik, roundtrip, mutasyon,
   sade anlatım + koruma, tam MCP. Kullanılabilir: doğal dilden problem, `PROVEN`.
4. **Şablon + öz-denetim + hakem:** §6.9, §6.9.1.
5. **Mod B (finans):** B1 formül denetimi, B2 mutabakat (§5.2); kripto botu ve Sentinax (canlıya alma özeti).
6. **Sağlamlaştırma:** altın test setinin tamamı, gerçek dosyalarla yerel kabul testi.

R12–R14 A2'de istenmediği için Şubat 2027 hedefine dahil değildir.

Ayrıntılı uygulama planı bu belge onaylandıktan sonra ayrı bir plan belgesinde yazılır.

---

## 11. Sahibe açık sorular

Cevaplananlar: roket kapsamı → K8; kullanım şekli → K9; fiziksel modeller → K10; Python → K11; kategori → K12;
UKB kodu → K13; LLM erişimi ve abonelikler → K14; yönlendirici → K15.

Model aileleri: Anthropic (Claude Code), OpenAI (Codex; Groq `gpt-oss` de bu aile), Google (Gemini CLI) ve Groq
üzerinden Meta, Alibaba, Moonshot. Yani en az 3 aileden bağımsız formülasyon olağan kullanımda mümkündür ve `PROVEN`
ulaşılabilir bir etikettir (§4.1).

Hedef → K16; OpenRocket → K17; şablon + öz-denetim → K18; hakem + öğrenme → K19; kripto botu → K20;
Mod B kapsamı + Sentinax → K21; lisans → K22; dallar ve anonimlik → K23.

Açık soru kalmadı. (Botla ilgili ertelenen bir nokta `docs/private/` altında; bot hazır olunca ele alınır.)

## 12. Uygulayıcıya bırakılanlar

Modül/dosya yapısı, sınıf adları, IR JSON şemasının alan adları, prompt metinleri, zaman aşımı varsayılan
değerleri, rapor görsel düzeni, CLI komut adları, test setinin ilk içeriği, `jacobian`'ın kullanılıp kullanılmayacağı.
