
# 📚 Tafsir Annotation Tag Guide | دليل وسوم تفسير الطبري

This documentation defines the structure and usage of tags used to annotate the **Tafsir al-Tabari** text. Tags are organized by major Islamic disciplines and support detailed classification and analysis.

---

## 🧷 Master Tag Categories | الفئات الرئيسية للوسوم

| Category        | Arabic Name      | Tag Prefix Example | Description |
|----------------|------------------|---------------------|-------------|
| Fiqh           | الفقه            | `fiqhterm`          | Covers legal matters, contracts, punishments, family law, jihad, inheritance, etc. |
| Kalam          | الكلام            | `kalamterm`         | Theological topics including divine attributes, free will, prophecy, and sects. |
| Lugha          | اللغة             | `lughaterm`         | Linguistic matters including grammar, semantics, idioms, and dialects. |
| Asbab al-Nuzul | أسباب النزول     | `a` series          | Context of revelation: time, event, place, or situation. |
| Naskh          | النسخ            | `NN`, `MM`, etc.    | Abrogation – identifies abrogating and abrogated verses. |
| Qira’at        | القراءات          | `q*` series         | Variant readings from different reciters and regions. |
| Science        | العلوم            | `science*`          | Natural sciences and related content in the Qur'an. |
| Sirah          | السيرة            | `sirah*`            | Biographical and historical context of the Prophet Muhammad ﷺ. |
| Sufism         | التصوف           | `sufi*`             | Topics in spiritual purification and inner practices. |
| Adyan/Tareekh  | الأديان/التاريخ  | `adyan*`            | Other religions and historical events/figures. |
| Israeliyat     | إسرائيليات        | N/A                 | Reports traced back to Jewish/Christian sources or narrators. |

---

## ⚖️ Fiqh Tags | وسوم الفقه

Subcategories fall under `fiqhterm`. Examples:

| Tag       | Arabic              | Description (English)                       |
|-----------|---------------------|---------------------------------------------|
| `adabqazi` | أدب القاضي          | Etiquette of judges and legal processes     |
| `aqiqa`    | العقيقة             | Birth sacrifice in Islam                    |
| `hadzina`  | حد الزنا            | Punishment for adultery                     |
| `hudud`    | الحدود              | Fixed legal punishments in Islamic law      |
| `nikah`    | النكاح              | Marriage laws                               |
| `talaq`    | الطلاق              | Divorce laws                                |
| `zakah`    | الزكاة              | Alms and obligatory charity                 |

➡ Full list includes over 85+ detailed tags under Fiqh.

---

## 🗣 Kalam Tags | وسوم علم الكلام

Used for theology. General tag: `kalamterm`.

| Tag        | Arabic               | Description                                |
|------------|----------------------|--------------------------------------------|
| `Imankufr` | الإيمان والكفر        | Belief and disbelief                       |
| `qazaqadr` | القضاء والقدر         | Predestination and divine decree           |
| `Firaq`    | الفرق                | Islamic sects and theological groups       |
| `Sifatilahi` | صفات الله تعالى     | Attributes of God                          |

---

## 🗣 Lugha Tags | وسوم اللغة

Language and grammar references, grouped under `lughaterm`.

| Tag         | Arabic               | Description                                |
|-------------|----------------------|--------------------------------------------|
| `Sarfnahaw` | النحو والصرف          | Morphology and syntax                      |
| `Amthal`    | أمثال العرب           | Arabic proverbs                            |
| `Lahajat`   | لهجات العرب           | Arabic dialects                            |
| `Tabeer`    | التعبير العربي         | Arabic expressions                         |

---

## 🕰 Asbab al-Nuzul | أسباب النزول

These tags capture the historical and contextual reasons for the revelation of specific verses.

Examples include:

- `a2yah` — 2nd year after Hijrah | السنة الثانية بعد الهجرة  
- `afbadr` — From Battle of Badr | من غزوة بدر  
- `av22:22` — At verse 22:22 | عند آية ٢٢:٢٢

---

## 🔁 Naskh Tags | وسوم النسخ

### Abrogating Verses (ناسخة)
- `NN`, `NN11`, `NNQ` — Various forms depending on the source

### Abrogated Verses (منسوخة)
- `MM`, `MM11`, `MMQ` — Verses that are abrogated

---

## 📖 Qira’at Tags | وسوم القراءات

| Tag         | Arabic             | Description |
|-------------|--------------------|-------------|
| `Qmakkah`   | قراء مكة           | Reciters of Makkah |
| `Qiraq`     | قراء العراق         | Reciters of Iraq |
| `Qghairjaiz`| القراءة غير الجائزة| Invalid recitations |

---

## 🔬 Science Tags | وسوم العلوم

| Tag       | Arabic    | Description |
|-----------|-----------|-------------|
| `Insan`   | الإنسان   | Human being |
| `Shams`   | الشمس     | The sun     |
| `Tib`     | الطب       | Medicine    |

---

## 📜 Sirah Tags | وسوم السيرة

| Tag       | Arabic       | Description |
|-----------|--------------|-------------|
| `Sbadr`   | بدر          | Battle of Badr |
| `Sfathmakkah` | فتح مكة  | Conquest of Makkah |
| `Swilada` | الولادة     | Birth of the Prophet ﷺ |

---

## 🌿 Sufism Tags | وسوم التصوف

| Tag      | Arabic    | Description |
|----------|-----------|-------------|
| `Awliya` | الأولياء  | Saints |
| `Riqaq`  | الرقائق   | Heart-softening topics |
| `Hub`    | الحب       | Divine love |

---

## 🏛 Adyan / Tareekh | الأديان / التاريخ

| Tag         | Arabic          | Description |
|-------------|------------------|-------------|
| `Yahudiya`  | اليهودية         | Judaism |
| `Nasraniya` | النصرانية        | Christianity |
| `Majusiya`  | المجوسية         | Zoroastrianism |
| `Khilafaumar` | خلافة عمر       | Caliphate of Umar ibn al-Khattab |

---

## 📘 Israeliyat Narrators | رواة الإسرائيليات

These are narrators whose input stems from Judeo-Christian traditions. Example:

- كعب الأحبار  
- وهب بن منبه  
- عبد الله بن سلام  
- عكرمة  

Full list includes over 150 named narrators.

---

## ✅ Rājeḥ Tags (Preferred Opinion Tags) | وسوم الراجح

These tags are used to **highlight the preferred or strongest opinion** (الرأي الراجح) within various disciplines in the annotation of the Tafsir.

| Tag         | Arabic Equivalent             | Meaning |
|-------------|-------------------------------|---------|
| `Frajeh`    | الفقهي الراجح                | Preferred opinion in **Fiqh** |
| `Krajeh`    | الكلامي الراجح               | Preferred opinion in **Kalam** |
| `Crajeh`    | العلمي الراجح                | Preferred opinion in **Science** |
| `Arajeh`    | أسباب النزول الراجح         | Preferred **Asbab al-Nuzul** view |
| `Srajeh`    | الصوفي الراجح               | Preferred opinion in **Sufism** |
| `Adrajeh`   | الديني الراجح               | Preferred opinion in **Other religions/history** |
| `Srrajeh`   | السيري الراجح               | Preferred opinion in **Sirah (biography)** |
| `Nrajeh`    | النسخي الراجح               | Preferred opinion regarding **Naskh (abrogation)** |

---

