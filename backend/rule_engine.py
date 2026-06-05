"""
Kural Tabanlı Analiz Motoru (AI'sız, ücretsiz)

Kullanıcının form yanıtlarını knowledge_base.py'deki örüntülerle ve templates.py'deki
şablonlarla eşleştirerek Markdown çıktı üretir. Çıktı, AI'nın ürettiği formatla AYNI:

  ## Aile Büyükleri & Soy Yükü
  - madde 1
  - madde 2

  ## Mali Durum
  - ...

  Lütfen seans alınız.
"""

from typing import Dict, List
from collections import Counter

from knowledge_base import (
    DISEASE_PATTERNS,
    FORM_QUESTION_HINTS,
    CAUSE_CATEGORIES,
)
from templates import (
    TEMPLATES_MALI,
    TEMPLATES_SORULAR,
    KAPANIS,
)


# ============================================================
# Yardımcılar
# ============================================================
def _f(doc: Dict, key: str) -> str:
    v = (doc.get(key) or "")
    return v.strip() if isinstance(v, str) else ""


def _is_evet(value: str) -> bool:
    """'Evet', 'Evet — ...' vs gibi başlangıçları algılar."""
    return value.strip().lower().startswith("evet")


def _is_hayir(value: str) -> bool:
    return value.strip().lower().startswith("hayır")


def _elder_status(value: str) -> str:
    """'Sağ, 65 yaşında' → 'sag', 'Vefat, 2010' → 'vefat', boş → ''"""
    v = value.strip().lower()
    if v.startswith("sağ"):
        return "sag"
    if v.startswith("vefat"):
        return "vefat"
    return ""


# ============================================================
# Bölüm 1 — Aile Büyükleri & Soy Yükü
# ============================================================
ELDER_KEYS = [
    ("anne_durum", "anne"),
    ("baba_durum", "baba"),
    ("anneanne_durum", "anneanne"),
    ("anne_babasi_durum", "annenin babası"),
    ("babaanne_durum", "babaanne"),
    ("baba_babasi_durum", "babanın babası"),
]


def build_aile(doc: Dict) -> List[str]:
    bullets: List[str] = []

    statuses = {label: _elder_status(_f(doc, key)) for key, label in ELDER_KEYS}
    vefat = [label for label, s in statuses.items() if s == "vefat"]
    sag = [label for label, s in statuses.items() if s == "sag"]

    if vefat:
        if len(vefat) == 1:
            bullets.append(
                f"Bildirilen vefat: **{vefat[0].capitalize()}**. Vefat eden yakın için dua ve helalleşme; "
                f"varsa onun adına yarım kalmış adak/zekat gibi yükümlülüklerin tamamlanması önerilebilir."
            )
        else:
            isim_listesi = ", ".join([x.capitalize() for x in vefat])
            bullets.append(
                f"Bildirilen vefatlar: **{isim_listesi}**. Vefat edenler için dua ve helalleşme; "
                f"onlardan kalmış olası adak veya hak yükümlülüklerinin gözden geçirilmesi faydalı olabilir."
            )

    if sag:
        if len(sag) == 1:
            bullets.append(
                f"Hayatta olduğu bildirilen: **{sag[0].capitalize()}**. Onunla helalleşme ve dua, soy hattındaki "
                f"manevi dengeyi olumlu yönde etkileyebilir."
            )
        else:
            isim_listesi = ", ".join([x.capitalize() for x in sag])
            bullets.append(
                f"Hayatta olduğu bildirilenler: **{isim_listesi}**. Yaşayan büyüklerle gönül kazanma ve helalleşme süreci, "
                f"soy hattındaki olası yükleri hafifletmede önemli olabilir."
            )

    # Annenin babası + Babanın babası ikisi de vefat → ek bilgi
    if (statuses.get("annenin babası") == "vefat" and statuses.get("babanın babası") == "vefat"):
        bullets.append(
            "Her iki dede tarafının da vefat etmiş olması durumunda; geçmiş kuşaktan gelmiş olabilecek "
            "adak, beddua, hak helalleşmesi gibi yüklerin tespitinde manevi rehberlik faydalı olabilir."
        )

    return bullets


# ============================================================
# Bölüm 2 — Mali Durum
# ============================================================
def build_mali(doc: Dict) -> List[str]:
    bullets: List[str] = []
    zekat = _f(doc, "zekat_veriyor").lower()
    faiz = _f(doc, "faizli_kredi").lower()

    for tpl in TEMPLATES_MALI:
        m = tpl["match"]
        val = _f(doc, m["field"]).lower()
        if "equals_lower" in m and val == m["equals_lower"]:
            bullets.append(tpl["text"])
        elif "starts_with_lower" in m and val.startswith(m["starts_with_lower"]):
            bullets.append(tpl["text"])

    return bullets


# ============================================================
# Bölüm 3 — Aile Hastalıkları
# ============================================================
def _match_diseases(text: str) -> List[Dict]:
    """Verilen serbest metinde geçen anahtar kelimeleri DISEASE_PATTERNS ile eşleştirir."""
    if not text:
        return []
    t = text.lower()
    matched = []
    seen_names = set()  # Aynı hastalığı tekrar eklemeyi önle
    
    for d in DISEASE_PATTERNS:
        name_l = d["name"].lower()
        hit = False
        
        # 1. Tam isim eşleşmesi (en güçlü)
        if name_l in t:
            hit = True
        
        # 2. İsmin önemli kelimelerini ara (parantez ve özel karakterler hariç)
        if not hit:
            # Parantez içini temizle ve kelimelere ayır
            clean_name = name_l.split("(")[0].strip()
            name_words = [w.strip() for w in clean_name.replace("/", " ").split() if len(w) > 2]
            # Her önemli kelimeyi ara
            for word in name_words:
                if word in t:
                    hit = True
                    break
        
        # 3. Semptom eşleşmesi (en kapsamlı)
        if not hit:
            for sym in d.get("symptoms", []):
                sym_lower = sym.lower()
                # Semptom metinde var mı?
                if sym_lower in t:
                    hit = True
                    break
                # Semptomun kelimelerini de ara (2+ karakter)
                sym_words = [w for w in sym_lower.split() if len(w) > 2]
                for sw in sym_words:
                    if sw in t:
                        hit = True
                        break
                if hit:
                    break
        
        # Eşleşme varsa ve daha önce eklenmemişse ekle
        if hit and name_l not in seen_names:
            matched.append(d)
            seen_names.add(name_l)
    
    return matched


def _causes_to_labels(causes: List[str], short: bool = False) -> str:
    """['zekat', 'beddua'] → 'Zekat, Beddua' veya kısa format için 'zekat ve beddua'"""
    labels = [CAUSE_CATEGORIES.get(c, c) for c in causes]
    if len(labels) > 3:
        labels = labels[:3]
    
    if short:
        # Parantez içlerini KORU, sadece çok uzun olanları kısalt
        clean_labels = []
        for l in labels:
            # / ile ayrılmış ise sadece ilkini al (örn: "Beddua / Lânet" → "Beddua")
            if ' / ' in l:
                l = l.split(' / ')[0].strip()
            # "ve taciz" gibi ekleri kaldır (ana kavramı koru)
            if ' ve taciz' in l.lower():
                l = l.lower().replace(' ve taciz', '').strip()
            clean_labels.append(l.lower())
        
        # Tekrar eden kelimeleri temizle
        seen = set()
        unique_labels = []
        for label in clean_labels:
            # Ana kelimeyi al (parantez öncesi)
            base = label.split('(')[0].strip() if '(' in label else label
            if base not in seen:
                seen.add(base)
                unique_labels.append(label)
        clean_labels = unique_labels[:3]
        
        if len(clean_labels) == 1:
            return clean_labels[0]
        elif len(clean_labels) == 2:
            return f"{clean_labels[0]} ve {clean_labels[1]}"
        else:
            return f"{clean_labels[0]}, {clean_labels[1]} ve {clean_labels[2]}"
    
    return ", ".join(labels)


def build_aile_hastalik(doc: Dict) -> List[str]:
    bullets: List[str] = []
    for key, who in [("anne_hastalik", "Annede"), ("baba_hastalik", "Babada"), ("cocuk_hastalik", "Çocuklarda")]:
        txt = _f(doc, key)
        if not txt:
            continue
        diseases = _match_diseases(txt)
        if diseases:
            for d in diseases[:2]:  # Bir alan için en fazla 2 hastalık göster
                bullets.append(
                    f"{who} bildirilen **{d['name']}** durumu; bilgi tabanında "
                    f"_{_causes_to_labels(d['causes'])}_ kategorileriyle ilişkilendirilebilir. "
                    f"Öneri: {d['remedy']}"
                )
        else:
            # Eşleşme yok ama dolu — genel ifade
            bullets.append(
                f"{who} bildirilen rahatsızlıklar (\"{txt[:60]}{'…' if len(txt) > 60 else ''}\") "
                f"manevi yön açısından değerlendirilebilir; uygun kategorinin tespiti için seans önerilir."
            )
    return bullets


# ============================================================
# Bölüm 4 — Yaşanılan Ruhsal & Fiziksel Rahatsızlıklar
# ============================================================
def build_rahatsizlik(doc: Dict) -> List[str]:
    bullets: List[str] = []
    txt = _f(doc, "rahatsizliklar")
    if not txt:
        return bullets

    diseases = _match_diseases(txt)
    if not diseases:
        bullets.append(
            f"Bildirdiğiniz rahatsızlıklar (\"{txt[:80]}{'…' if len(txt) > 80 else ''}\") "
            "bilgi tabanındaki örüntülerle birebir eşleşmemektedir; daha detaylı manevi değerlendirme için seans önerilir."
        )
        return bullets

    # En spesifik hastalıkları öncelikli göster (remedy uzunluğu > 50 = daha detaylı)
    detailed_diseases = [d for d in diseases if len(d.get('remedy', '')) > 80]
    simple_diseases = [d for d in diseases if len(d.get('remedy', '')) <= 80]
    
    # Önce detaylı, sonra basit - toplam 15 hastalık göster
    ordered_diseases = detailed_diseases[:10] + simple_diseases[:5]
    
    for d in ordered_diseases[:15]:
        remedy = d.get('remedy', '')
        causes_text = _causes_to_labels(d['causes'], short=True)
        
        # Remedy'den anlamlı bir açıklama çıkar
        # İlk cümleyi al, nokta veya 150 karaktere kadar
        if '.' in remedy:
            parts = remedy.split('.')
            first_sentence = parts[0].strip()
            # Eğer ilk cümle çok kısaysa ikinci cümleyi de ekle
            if len(first_sentence) < 40 and len(parts) > 1 and parts[1].strip():
                first_sentence = f"{first_sentence}. {parts[1].strip()}"
        else:
            first_sentence = remedy[:150]
        
        if len(first_sentence) > 150:
            first_sentence = first_sentence[:147] + '...'
        
        # Sondaki gereksiz nokta ve boşlukları temizle
        first_sentence = first_sentence.rstrip('. ')
        
        # Daha zengin ve profesyonel cümle yapısı
        bullets.append(
            f"**{d['name']}**: Bu rahatsızlık, soyda {causes_text} ile ilişkilendirilebilir. {first_sentence}."
        )
    return bullets


# ============================================================
# Bölüm 5 — Manevi İşaretler (17 sorudan "Evet" olanlar)
# ============================================================
QUESTION_DISPLAY = {
    "adak_yemin": "Adak / Yemin",
    "muska_okunmus_su": "Muska / Okunmuş Su",
    "miras_sorunu": "Miras Sorunu",
    "beddua_hak_haram": "Beddua / Hak Haram",
    "intihar": "İntihar Girişimi",
    "anne_baba_ofke": "Anne-Babaya Öfke",
    "es_soguklugu": "Eş Soğukluğu",
    "sehvet": "Şehvet",
    "duygusallik": "Duygusallık",
    "kin": "Kin",
    "kusme_alinganlik": "Küsme / Alınganlık",
    "ofke": "Öfke",
    "nefret": "Nefret",
    "supheci": "Şüphecilik",
    "uyku_sorunu": "Uyku Sorunu",
    "aniden_parlama": "Aniden Parlama",
    "alaycilik": "Alaycılık",
}


def build_manevi(doc: Dict) -> List[str]:
    bullets: List[str] = []
    for q_key, label in QUESTION_DISPLAY.items():
        val = _f(doc, q_key)
        if not _is_evet(val):
            continue
        text = TEMPLATES_SORULAR.get(q_key, "")
        # Kullanıcı açıklama yazdıysa parantez içinde ekle
        note = ""
        v_lower = val.lower()
        if "—" in v_lower or "-" in val:
            parts = val.split("—") if "—" in val else val.split("-", 1)
            if len(parts) > 1:
                user_note = parts[-1].strip()
                if user_note and user_note.lower() != "evet":
                    note = f' (Kişisel not: "{user_note[:80]}{"…" if len(user_note) > 80 else ""}")'
        if text:
            bullets.append(f"**{label}**: {text}{note}")
    return bullets


# ============================================================
# Bölüm 6 — Genel Değerlendirme (en güçlü kategoriler)
# ============================================================
def build_genel(doc: Dict) -> List[str]:
    """Tüm sinyal kaynaklarını toplayıp en sık geçen kategorileri öne çıkarır."""
    counter = Counter()

    # Sorular → kategoriler
    for q_key, hints in FORM_QUESTION_HINTS.items():
        if _is_evet(_f(doc, q_key)):
            for c in hints:
                counter[c] += 2  # Sorular daha güçlü sinyal

    # Hastalıklar → kategoriler
    all_text = " ".join([_f(doc, k) for k in ["rahatsizliklar", "anne_hastalik", "baba_hastalik", "cocuk_hastalik"]])
    diseases = _match_diseases(all_text)
    for d in diseases:
        for c in d["causes"]:
            counter[c] += 1

    # Mali sinyaller
    if _f(doc, "zekat_veriyor").lower() == "hayır":
        counter["zekat"] += 3
    if _f(doc, "faizli_kredi").lower().startswith("evet"):
        counter["faiz"] += 3

    bullets: List[str] = []
    if not counter:
        bullets.append("Form yanıtlarınız üzerinden bilgi tabanında belirgin örüntü tespit edilmemiştir; "
                       "daha kapsamlı bir değerlendirme için seans önerilir.")
        return bullets

    top = counter.most_common(3)
    labels = [CAUSE_CATEGORIES.get(c, c) for c, _ in top]
    bullets.append(
        f"Tüm yanıtlarınız birlikte değerlendirildiğinde, en güçlü öne çıkan kategoriler: "
        f"**{labels[0]}**{', **' + labels[1] + '**' if len(labels) > 1 else ''}"
        f"{' ve **' + labels[2] + '**' if len(labels) > 2 else ''}."
    )
    bullets.append(
        "Bu kategoriler doğrultusunda; tövbe, helalleşme, varsa adak/zekat eksiklerinin tamamlanması "
        "ve manevi rehberlik öncelikli adımlar olarak değerlendirilebilir."
    )
    bullets.append(
        "Bu çıktı; bildirilen verilere göre _olası_ işaretleri özetler. Kesin tespit ve uygulamaya yönelik "
        "yönlendirme için seans alınması önerilir."
    )
    return bullets


# ============================================================
# ANA ÜRETİCİ
# ============================================================
def generate_analysis(doc: Dict) -> Dict:
    """Form dökümünü alır, Markdown analiz metni ve sinyal özeti döner."""
    sections = []

    aile = build_aile(doc)
    if aile:
        sections.append(("Aile Büyükleri & Soy Yükü", aile))

    mali = build_mali(doc)
    if mali:
        sections.append(("Mali Durum", mali))

    aile_hast = build_aile_hastalik(doc)
    if aile_hast:
        sections.append(("Aile Hastalıkları", aile_hast))

    rahatsizlik = build_rahatsizlik(doc)
    if rahatsizlik:
        sections.append(("Ruhsal & Fiziksel Rahatsızlıklar", rahatsizlik))

    manevi = build_manevi(doc)
    if manevi:
        sections.append(("Manevi İşaretler", manevi))

    genel = build_genel(doc)
    if genel:
        sections.append(("Genel Değerlendirme", genel))

    # Markdown oluştur
    lines = []
    for title, bullets in sections:
        lines.append(f"## {title}")
        lines.append("")
        for b in bullets:
            lines.append(f"- {b}")
        lines.append("")
    lines.append(KAPANIS)
    markdown = "\n".join(lines)

    # Sinyal özeti (Counter çıktısı - debug/info için)
    signals: Dict[str, List[str]] = {}
    for q_key, hints in FORM_QUESTION_HINTS.items():
        if _is_evet(_f(doc, q_key)):
            for c in hints:
                signals.setdefault(c, []).append(QUESTION_DISPLAY.get(q_key, q_key))

    return {"ai_analysis": markdown, "signals": signals}
