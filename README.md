# Rigor

**AI'a yaptırdığın matematikten emin olmak için bir doğrulama motoru.**
Python kütüphanesi + MCP sunucusu (Claude Code ve diğer kodlama ajanları için).

> **Durum:** Tasarım aşaması. Henüz kod yok; mimari ve kararlar [tasarım belgesinde](docs/superpowers/specs/2026-11-07-rigor-design.md).
>
> **Revizyon sürüyor (2026-11-10):** Etiketler, hakem heyeti ve model erişimi yeniden ele alınıyor. Alınan kararlar ve
> açık noktalar [`concepts_brief.md`](concepts_brief.md) dosyasında; tasarım belgesine henüz işlenmedi. Aşağıdaki
> etiket tablosu ve model erişimi anlatımı önceki sözleşmeyi yansıtır.

---

## Neden?

Bir LLM'e matematik yaptırdığında iki tür hata olur:

| | Hata | Örnek | Rigor'un cevabı |
|---|---|---|---|
| **Tip-1** | Hesap hatası | `17 × 23`'ü yanlış çarpmak | Hesabı LLM yapmaz; deterministik ve kesin motorlar yapar (SymPy, Z3, Arb…) |
| **Tip-2** | Formülasyon hatası | "En fazla" yerine `>=` yazmak, birimi karıştırmak, eksik bir değeri uydurmak | Bağımsız modellerin çapraz formülasyonu, matematiksel denklik kontrolü, insan onayı |

Tip-2 daha tehlikelidir: çözücü **yanlış sorunun kusursuz cevabını** verir. Bu hatayı matematiksel olarak
sıfırlayan bir yöntem yok. Rigor bu yüzden "her zaman doğru" demez, **ne kadar emin olduğunu** söyler.

## Vaat

> Rigor'un döndürdüğü her sonuç ya **senin onayladığın tanıma göre doğrulanmıştır** ve doğrulamanın gücü
> etiketle yazar, ya da Rigor cevap vermeyi **reddeder** ve nedenini söyler. Etiketsiz bir sayı asla dönmez.

| Etiket | Anlamı |
|---|---|
| **KANITLANDI** | Tanımı sen onayladın, en az 2 farklı model ailesi aynı formülasyonda oybirliği yaptı, sonucu makinece kontrol edilebilir bir kanıt destekliyor (kesin aritmetik, SMT ispatı ya da Lean 4 çekirdeği). |
| **ÇAPRAZ DOĞRULANDI** | Güçlü destek var ama formal kanıt yok (ör. diferansiyel denklem simülasyonu). |
| **REDDEDİLDİ** | Eksik bilgi, çelişki, birim hatası ya da modeller anlaşamadı. Ne gerektiği söylenir. |

Eksik bir parametre varsa Rigor **tahmin etmez, sorar**. Her sonucun yanında sade Türkçeyle bir açıklama ve
yeniden üretilebilir bir **kanıt raporu** gelir.

## Nasıl çalışır?

```text
 Problem (doğal dil)
   │
   ├─ 1. Ayrıştırma      büyüklükler, birimler, bilinmeyenler — her biri metindeki yeriyle
   ├─ 2. Tipli IR        eval yok; her düğümde birim ve kaynak
   ├─ 3. Statik kapılar  birim kontrolü · eksik/fazla tanım analizi · çelişki çekirdeği   → eksikse SORU
   ├─ 4. Red Team        3 bağımsız model · denklik kontrolü · geri çeviri · mutasyon testi → ayrışırsa SORU
   ├─ 5. Onay            "Problemi şöyle anladım" — sade dille, senin onayınla
   ├─ 6. Çözüm           problem türüne göre motor seçimi, en az 2 bağımsız yol
   ├─ 7. Kanıt           kesin aritmetikle geri koyma · unsat çekirdeği · hata sınırları
   └─ 8. Rapor           sonuç + etiket + sade anlatım + kanıt raporu
```

- **Modeller bağımsız olmalı:** Claude, ChatGPT ve Gemini aboneliklerini yalnızca resmi CLI'larla (`claude`,
  `codex`, `gemini`) ve Groq gibi ücretsiz API'leri kullanır. Önbellek, otomatik model değiştirme ya da istem
  sıkıştırma yapan ara katmanlar bağımsızlığı bozduğu için güvenilmez sayılır.
- **Tekrarlanan hesaplar:** Onaylı bir formülasyon şablon olarak kaydedilir ve yeni değerlerle yeniden kullanılır.
  Sık kullanılan şablonları araç LLM'siz kendisi denetler. Şüpheli bir alarmda farklı model ailelerinden hakemlere
  sorar, son kararı yine sen verirsin.

## Ne için?

Rigor'un çekirdeği hiçbir alanı bilmez; **istediğin alana uyarlanır ve o alan için optimize edilir.** Uyarlama bir
**alan paketiyle** yapılır: alanın modelleri, veri okuyucuları, birimleri, terim sözlüğü, beklenen davranışları ve
kendi test seti. `rigor domain new / verify / bench` ile paket kurulur, doğrulanır ve ölçülür. Optimizasyon soru
sayısını ve kapsamı iyileştirir; güvenlik kurallarını (oybirliği, kanıt şartları) hiçbir paket gevşetemez.

Çekirdeğin desteklediği matematik: cebir, eşitsizlikler, kalkülüs, diferansiyel denklemler, doğrusal cebir, olasılık
ve istatistik, sayılar kuramı, kombinatorik, mantık, optimizasyon, geometri ve **Lean 4** ile soyut ispatlar.
Desteklemediği bir yapıda tahmin yürütmez, bunu açıkça söyler. Termodinamik, akışkanlar mekaniği, eklemeli imalat
gibi alanlar alan paketiyle eklenir; v1 `rocket`, `finance` ve örnek olarak `fluids` paketiyle gelir.

Sahibinin kendi kullanımları:

- **Roket:** TEKNOFEST Roket Yarışması (A2 Orta İrtifa) hesapları: kütle bütçesi, statik marjin, motor itkisi,
  rampadan çıkış hızı, tepe irtifası, paraşüt iniş hızları, eksen dönüşümleri, haberleşme paketi. Sonuçlar
  **OpenRocket** ile karşılaştırılabilir.
- **Finans:** Bir kripto alım-satım botunun ve [Sentinax](https://github.com/ErenTahiroglu/Sentinax) yatırım karar
  destek platformunun matematiği. Formüller literatürdeki tanımlarla karşılaştırılır, üretilen sayılar bağımsız
  olarak yeniden hesaplanır. Kod denetlenmez; yalnızca matematik kontrol edilir.

### Örnek: şartnamede bulunan bir hata

Tasarım aşamasında Rigor'un yöntemiyle (SymPy ile sembolik denklik + karşı örnek) TEKNOFEST 2026 şartnamesi
**Ek-1'deki kuaterniyon çarpım formülünün yanlış** olduğu gösterildi. Ek-1, vektör kısmını
`s_a·v_a + s_b·v_b + v_a × v_b` olarak veriyor; doğrusu `s_a·v_b + s_b·v_a + v_a × v_b`.
Karşı örnek: `a = (1, 0, 0, 0)`, `b = (0, 1, 0, 0)` için Ek-1 `(0, 0, 0)` verir, doğru sonuç `(1, 0, 0)`'dır.
Kanıt betiği: [`docs/research/evidence/ek1_kuaterniyon_dcm_kontrol.py`](docs/research/evidence/ek1_kuaterniyon_dcm_kontrol.py).

## Kullanım (planlanan)

```python
import rigor

s = rigor.Session(config=rigor.Config.load())
step = s.submit("Roketin kuru kütlesi 12 kg, ... rampadan çıkış hızı kaç m/s olur?")
while step.state in {"NEEDS_INPUT", "NEEDS_CONFIRMATION"}:
    step = s.answer(step, ...)        # eksik bilgiyi ve onayı sen verirsin
print(step.result.label, step.result.value)
step.result.report.write("rapor.md")
```

MCP üzerinden: `rigor_solve`, `rigor_answer`, `rigor_confirm`, `rigor_report`, `rigor_template`,
`rigor_selfcheck`, `rigor_compare_openrocket`, `rigor_audit_formula`, `rigor_reconcile`.

## Yapım sırası

1. Çekirdek: tipli IR, birim ve tanım kapıları, kesin motorlar, kanıt, rapor, ince MCP
2. Roket fiziği: model kütüphanesi, `.eng`/xlsx/CSV/`.ork` okuyucular, uçuş simülasyonu, OpenRocket karşılaştırması
3. Red Team ve doğal dil: bağımsız formülasyon, denklik, sade anlatım, tam MCP
4. Şablonlar, öz-denetim ve hakem süreci; Lean 4 ispat arka ucu; alan uyarlama araçları
5. Finans: formül denetimi ve bağımsız yeniden hesap
6. Sağlamlaştırma: altın test seti, gerçek dosyalarla kabul testi

## Dallar

| Dal | Ne için |
|---|---|
| `main` | Kararlı son sürüm. Yalnızca `development`'tan gelen pull request'lerle güncellenir; her birleştirme bir sürüm etiketi (`vX.Y.Z`) alır. |
| `development` | Geliştirme. Yeni işler buraya gelir. |

## Belgeler

| Belge | İçerik |
|---|---|
| [Tasarım belgesi](docs/superpowers/specs/2026-11-07-rigor-design.md) | Mimari, bağlayıcı kararlar, hedefler ve anti-hedefler |
| [Yol haritası](docs/superpowers/plans/2026-11-07-rigor-yol-haritasi.md) | Paket mimarisi, fazlar (F1–F9), çıkış ölçütleri |
| [Faz 1 planı](docs/superpowers/plans/2026-11-07-faz-1-cekirdek.md) | Çekirdeğin adım adım TDD uygulama planı |
| [Araştırma notları](docs/research/2026-11-07-arastirma-notlari.md) | Kaynaklı bulgular, araç durumu, sürümler, Red Team incelemeleri |
| [Karar özeti (taslak)](concepts_brief.md) | Etiket, yeterlik ve heyet revizyonu: alınan kararlar, Red Team bulguları, açık noktalar |
| [Ham araştırma raporları](docs/research/Deep%20Research/) | Dış araçla üretilmiş raporlar ve hesap eki. Doğrulanmış sonuç değildir; denetimi karar özetindedir |
| [Handoff](Handoff) | Projenin başlangıç devri |

## Lisans

[PolyForm Noncommercial 1.0.0](LICENSE). Kişisel kullanım, araştırma, eğitim, öğrenci takımları ve kâr amacı
gütmeyen kuruluşlar serbestçe kullanabilir, değiştirebilir ve dağıtabilir. **Ticari kullanım bu lisansla izinli
değildir**; ticari lisans için sahibiyle iletişime geçin.

Required Notice: Copyright (c) 2026 Eren Tahiroğlu (https://github.com/ErenTahiroglu)
