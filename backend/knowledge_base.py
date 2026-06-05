"""
Tıbb-ul Furkan Bilgi Tabanı (Knowledge Base)
"1. KİTAP TIBB'ÜL FURKAN DÜZENLENMİŞ NÜSHA - 9 kasım 2024" baz alınarak hazırlanmıştır.

Bu modül; analiz motoruna ve Yapay Zeka katmanına sabit bilgi (context) sağlar.
LLM çağrılarında 'system_message' içine eklenir; her analizde PDF'in tamamı gönderilmek yerine
kompakt, kategorize edilmiş özet kullanılır (maliyet/hız için).
"""

# ============================================================
# 1. ADAK HAYVANLARININ ÖZELLİKLERİ (PDF Bölüm: ADAK HAYVANLARININ ÖZELLİKLERİ)
# ============================================================
ADAK_HAYVANLARI = """
ADAK HAYVANLARININ ÖZELLİKLERİ:
- Adak hayvanı adanır ve usulüne uygun kesilmezse, bedenden ayrılmayan ve hastalık üreten
  bir 'ruhsat'a (görevli enerji) dönüşür.
- Erkekte DİŞİ adak (koyun, inek, tavuk) çoksa: cinsel isteksizlik, eşine soğukluk, hemcinse meyil
  riskleri artar.
- Kadında ERKEK adak (koç, boğa, horoz) çoksa: aynı şekilde ters cinsiyet etkisi.
- Adak yerine getirilmemiş ise: 'açıkta kalmış adak' olarak vücuda yerleşir.
- Adak hayvanı çalındı / başkası yedi / usulsüz kesildi ise: kefareti tekrar verilmelidir.
- 5-6 adetten fazla adak (çoklu adak) ağır hastalık tetikleyebilir (örn. ensefalit, bipolar, otizm).
- Adak hayvanın ciğeri, kemiği, kafası yenirse o organa yönelik rahatsızlık tetiklenebilir.
- Hayvan adakları yendiği zaman egzamaya, reflüye sebep olur.
- Rüyada sıçrama olursa büyükbaş hayvan adağı işaretidir.
- Büyükbaş hayvan adakları gece uyutmaz.

KOYUN / DİŞİ KUZU ADAĞI BELİRTİLERİ:
- Çok uyutur, tembellik yapar
- Harama çağırıldığında hemen gider
- Aşırı duygusaldır ve ağlar
- Hayır diyemez, boyun eğer
- İntihara teşvik ederek yüksek yerden atlatır
- Koyun sayısı arttıkça duygusallık ve uyku etkisi artar

KOÇ / ERKEK KUZU ADAĞI BELİRTİLERİ:
- Kadında bazen erkek sesi çıkartır
- Kadının alnında sivilce çıkartır
- Erkekte şehvet yapar, kadında cinsel soğukluk yapar
- Kafa atar, inatçıdır, kincidir
- Geçmişi hatırlatır, gösterişi sever
- Kadınlarda erkeksi yapıya sebep olur
- Erkeklerde dik başlılık yapar
- Affedemez, geçmişi unutmaz, helallik veremez
- İntihara teşvik ederek yüksek yerden atlatır

KEÇİ ADAĞI BELİRTİLERİ:
- Küser, aşırı inatçıdır
- Yüksek yerleri sever, yeşilliği sever
- Çocuklarda belirtisi: yüksek yerlere çıkma, koltuklarda zıplama
- İnsan içine çıkmak istememeye, sıkılmaya sebep olur
- Yemeklere tuz atmayı sever
- Çabuk kalbi kırılır, hemen küser, boynunu büker
- Yalnız kalmayı sever
- Yüksek yerden intihara teşvik ettirir

BOĞA / TOSUN ADAĞI BELİRTİLERİ:
- Kafasını duvara vurarak sinirlenir
- Erkeklerde aşırı şehvete neden olur
- Kadında erkeksi yapı ve cinsel soğukluk yapar
- Aniden öfke patlamasına neden olur
- Eliyle temas eder (kavga eder, vurar, kırar)
- Öfkelendiğinde evi yıkar, kendini durduramaz, sonra pişman olur ağlar
- "Ben erkek değil miyim? Benim sözüm neden tutulmuyor?" der

İNEK ADAĞI BELİRTİLERİ:
- Aşırı şüphecidir
- "Büyük memeli inek keseceğim" sözü göğüs irileşmesine sebep olur
- "Kız gibi oğlum olsun inek keseceğim" sözü erkeklerde hormon bozukluğu ve yumuşak göğüse sebep olur
- Kadında yüksek şehvet yapar, zinaya sevk eder
- Kadınların üst baldırlarında (basende) genişlemeye neden olur
- Takıntı yapar, vesvese yapar, gözüyle gördüğüne inanmaz
- Gök bilimleri, astroloji merakı yapar
- İmanda şüpheye düşürmeye çalışır

EŞEK ADAĞI BELİRTİLERİ:
- Eli kolu kalkmama, yavaş hareket etme, tembellik yapar
- Gece yemek yeme isteği yapar
- Sürekli şüpheye yönlendirmek ister
- Susmayan konuşmaya sebep olur, çok konuşturur
- Bir konuyu bir cümleyle anlatacağına yüz cümleyle anlatır
- Kekemeliğe sebep olabilir
- Aniden parlayıp çok konuşturur

HOROZ ADAĞI BELİRTİLERİ:
- Eşini aşırı kıskanmaya sebep olur
- "S" harfini söylemede sıkıntı olur
- Dövüşürken ısırır
- Konuşmada pelteklik yapar
- (Peltek insanları kınamak da peltekliğe sebep olabilir)
- İnsanı gıcık eder, dalga geçer

KÖPEK ADAĞI BELİRTİLERİ:
- Çok sinirli olabilir
- Kincidir, inatçıdır
- Tükürür

KELLE PAÇA ADAĞI BELİRTİLERİ:
- İnsanın yüzünde, boynunda, kafasında kızarıklıklara ve kaşıntıya sebep olur
- Hayvanın neresi yendiyse o bölge kaşınır (işaret)
- Kelebek hastalığına sebep olur, kişinin yüzü boynu kıpkırmızı olur

DİĞER ADAKLAR VE BELİRTİLERİ:

TÜRBE ZİYARETİ ADAĞI:
- Türbe ziyareti adanmış ve bunu adayan ölmüş işaretidir

YORGAN/BATTANİYE DAĞITMA ADAĞI:
- Gece vücudun yorganı atmasına sebep olur
- Ayak istemsiz yorganı teper
- "Dağıtacağım" denmiş ama fakire ulaşmamış

FAKİR GİYDİRME ADAĞI:
- Kişi üşüyorsa fakir giydirme adağı olabilir
- O fakir giydirilmedikçe kişi üşümeye devam eder
- Cilt rahatsızlıklarında ruhsatı vardır, kaşıntı yapabilir

UN/BUĞDAY DAĞITMA ADAĞI VE BUĞDAY TARLASI YAKMA:
- Glüten alerjisine sebep olur
- Çölyak hastalığına sebep olur

FAKİR DOYURMA ADAĞI:
- Yeme isteği çok olur
- Kilo yapar, adaklar çok fazlaysa zayıflamaya sebep olur
- Çocuklarda yemek yememeye neden olur

ÇOCUK SEVİNDİRME ADAĞI:
- Kişiyi çocuksu bir hale çevirir
- Çocuk gibi hareketler yapar

KUR'AN-I KERİM OKUMA ADAĞI:
- Kur'an okumada zorlanmaya sebep olur
- Yakını görememeye neden olur (miyop)
- "Her gece Yasin okuyacağım" adağı tavukkarası göz hastalığına sebep olur (kişi gece göremez)

AĞAÇ DİKME ADAĞI:
- Ciltte kuruluk, susuzluk yapabilir

UYKU HARAM OLSUN SÖZÜ:
- "Uyku bana/sana haram olsun" sözü uyutmaz
"""

# ============================================================
# 2. GÜNAH / RUHSAT KATEGORİLERİ
# ============================================================
CAUSE_CATEGORIES = {
    "zekat": "Verilmeyen veya Eksik Zekat",
    "adak_hayvan": "Yerine Getirilmeyen Hayvan Adağı (kurban)",
    "adak_eylem": "Yerine Getirilmeyen Eylemsel Adak (oruç, namaz, Kur'an, hatim, ziyaret, hac)",
    "yemin_bozma": "Yemin Etme ve Bozma",
    "beddua": "Beddua / Lânet",
    "soy_laneti": "Soy Lâneti",
    "zulum_insan": "İnsana Zulüm (dövme, ah alma)",
    "zulum_hayvan": "Hayvana Zulüm / İşkence / Yakma",
    "zulum_anne_baba": "Anne-Babaya Zulüm / Öfke",
    "isyan": "Allah'a / Kadere İsyan, Şükürsüzlük",
    "sirk": "Şirk",
    "kinama": "Kınama / Alay",
    "faiz": "Faiz Yeme veya Yedirme, Faizli Kredi",
    "hak_haram": "Hak Haramlığı",
    "haram_kazanc": "Haksız Kazanç",
    "hayrat_mali": "Hayrat / Vakıf Malı Yeme",
    "zina_ensest": "Zina / Ensest / Tecavüz",
    "iftira": "İftira",
    "yetim_hakki": "Yetim Hakkı Yeme",
    "miras_laneti": "Miras Üzerine Kavga / Lânet",
    "adak_eti": "Adak Eti Yeme",
    "kufur_kainata": "Kâinata Küfür / Yaratılmışları Beğenmeme",
    "narsist_zulum": "Âşıkları Ayırma, Yuva Yıkma",
    "kul_hakki": "Genel Kul Hakkı",
    "cocuk_aldirma": "Çocuk Aldırma (kürtaj)",
    "harami_esme": "Harami Eşme",
    "haramzade": "Haramzade",
    "muska": "Muska Takma / Okunmuş Su İçme (büyücüye gitme)",
    "intihar": "İntihar Girişimi / Kendine Zulüm",
    # === YENİ EKLENMİŞ KATEGORİLER ===
    "kopek_zulum": "Köpeğe Zulüm ve Taciz",
    "esek_zulum": "Eşeğe Zulüm ve Taciz",
    "kedi_zulum": "Kediye Zulüm (suda boğma vb.)",
    "aniz_yakma": "Anız/Tarla Yakarak Hayvanları Yakma",
    "gelin_zulum": "Gelin ve Eş Zulmü",
    "yetim_zulum": "Yetime Zulüm ve Taciz",
    "cocuk_oldurme": "Çocuk Öldürme ve Çocuk Zulmü",
    "hasta_cocuk_zulum": "Hasta Çocuğa Zulüm",
    "hasta_mahkum_zulum": "Hasta Mahkûma Zulüm",
    "hamile_zulum": "Hamile Kadına Zulüm",
    "alim_evliya_zulum": "Âlim ve Evliya Zulmü/Öldürme",
    "insan_oldurme": "İnsan Öldürme veya İşkence Ederek Öldürme",
    "kan_bedduasi": "Kana Okunan Beddua",
    "damar_bedduasi": "Damara Okunan Beddua",
    "el_ayak_bedduasi": "Elin Ayağın Tutmaz Olsun Bedduası",
    "goz_bedduasi": "Gözünüz Kör Olsun Bedduası",
    "deri_bedduasi": "Deriniz Kurusun Bedduası",
    "dil_bedduasi": "Ağzın Dilin Tutulsun Bedduası",
    "toplum_bedduasi": "Toplum İçine Çıkamayasın Bedduası",
    "komik_beddua": "Çoluk Çocuğunuza Gülsünler Bedduası",
    "evlat_bedduasi": "Allah Evlat Vermesin Bedduası",
}

# ============================================================
# 3. HASTALIK ↔ MANEVI SEBEP İLİŞKİLERİ
# (PDF: GÜNAHLARIN SEBEP OLDUĞU BELA VE RAHATSIZLIKLAR bölümü)
# ============================================================
DISEASE_PATTERNS = [
    {"name": "Alis Harikalar Diyarı Sendromu", "category": "Nörolojik/Psikiyatrik",
     "symptoms": ["algı bozukluğu", "boyut sapması"],
     "causes": ["kufur_kainata", "isyan"],
     "remedy": "Yaratılmışlara saygı, kibirden arınma, tövbe."},

    {"name": "Alzheimer / Unutkanlık", "category": "Nörolojik",
     "symptoms": ["unutkanlık", "hafıza kaybı", "bilinç bulanıklığı"],
     "causes": ["zekat", "adak_eylem", "sirk", "zulum_anne_baba", "kinama"],
     "remedy": "Zekat tamamlanır, adaklar tespit edilir; anne-baba helalleşmesi."},

    {"name": "Astım / KOAH / Solunum", "category": "Solunum",
     "symptoms": ["nefes alamama", "boğulma hissi", "kriz"],
     "causes": ["isyan", "zekat"],
     "remedy": "Hayata isyandan tövbe, zekat eksiği tamamlama."},

    {"name": "Bağırsak Hastalıkları (Kanser, Basur, Kabızlık)", "category": "Sindirim",
     "symptoms": ["bağırsak rahatsızlığı", "hemoroid", "kabızlık"],
     "causes": ["faiz", "miras_laneti", "haram_kazanc", "hak_haram", "beddua"],
     "remedy": "Faiz tövbesi, hak helalleşmesi, miras helalleşmesi."},

    {"name": "Beyin Tümörü", "category": "Onkolojik",
     "symptoms": ["şiddetli baş ağrısı", "tümör"],
     "causes": ["hayrat_mali", "zulum_insan", "zekat"],
     "remedy": "Hayrat malı iadesi, zekat tövbesi."},

    {"name": "Bipolar Bozukluk", "category": "Psikiyatrik",
     "symptoms": ["manik dönemler", "depresif dönemler", "ruh hali dalgalanması"],
     "causes": ["zekat", "adak_eylem", "zulum_anne_baba", "zulum_hayvan"],
     "remedy": "Anne-baba ile helalleşme, zekat ve adakları tamamlama."},

    {"name": "Böbrek Hastalıkları", "category": "Üriner",
     "symptoms": ["böbrek yetmezliği"],
     "causes": ["zekat", "beddua"],
     "remedy": "Zekat kefareti, suya/kana beddua tövbesi."},

    {"name": "Cinsel İsteksizlik / Eşten Soğuma", "category": "Cinsel",
     "symptoms": ["isteksizlik", "soğukluk"],
     "causes": ["adak_hayvan", "zina_ensest", "iftira", "kinama"],
     "remedy": "Adak tespiti ve kefareti, helalleşme."},

    {"name": "Diyabet (Şeker)", "category": "Endokrin",
     "symptoms": ["yüksek şeker", "tatlı bağımlılığı"],
     "causes": ["zekat", "kinama", "soy_laneti", "beddua", "adak_eylem", "adak_eti"],
     "remedy": "Zekat tamamlama, soy lâneti tövbesi, tatlı dağıtma adaklarını yerine getirme."},

    {"name": "Down Sendromu / Genetik Bozukluk", "category": "Genetik",
     "symptoms": ["genetik bozukluk", "gelişimsel gecikme"],
     "causes": ["zekat", "isyan", "adak_hayvan", "adak_eti", "haramzade"],
     "remedy": "Zekat tamamlama, isyan tövbesi, adak tespiti."},

    {"name": "Otizm", "category": "Nörogelişimsel",
     "symptoms": ["iletişim sorunu", "sosyal güçlük"],
     "causes": ["beddua", "zulum_insan", "faiz", "cocuk_aldirma", "zulum_hayvan", "kinama"],
     "remedy": "Beddua, faiz ve zulüm tövbeleri."},

    {"name": "Felç / İnme", "category": "Nörolojik",
     "symptoms": ["vücut tutmaz", "inme"],
     "causes": ["zulum_insan", "beddua", "sirk", "isyan", "zekat", "zulum_hayvan"],
     "remedy": "Tüm zulümlerden helalleşme, zekat."},

    {"name": "Kan Kanseri (Lösemi)", "category": "Onkolojik",
     "symptoms": ["lösemi", "kan kanseri"],
     "causes": ["adak_eylem", "adak_eti", "zekat", "beddua", "zulum_insan"],
     "remedy": "Adak yerine getirme, zekat kefareti."},

    {"name": "Karaciğer Hastalıkları (Büyüme, Kanser)", "category": "İç Hastalık",
     "symptoms": ["ciğer şişmesi", "ciğer kanseri"],
     "causes": ["zekat", "beddua", "adak_eti"],
     "remedy": "Zekat, beddua, adak ciğeri tövbesi."},

    {"name": "Meme Kanseri", "category": "Onkolojik",
     "symptoms": ["meme kanseri"],
     "causes": ["hayrat_mali", "isyan", "soy_laneti", "zekat", "zulum_insan"],
     "remedy": "El-Hayy, El-Kayyum isimlerinden tövbe; zekat ve beddua kefareti."},

    {"name": "Mide Kanseri", "category": "Onkolojik",
     "symptoms": ["mide kanseri"],
     "causes": ["zekat", "zulum_insan", "beddua"],
     "remedy": "Zekat ve beddua kefareti."},

    {"name": "Migren", "category": "Nörolojik",
     "symptoms": ["şiddetli baş ağrısı"],
     "causes": ["sirk", "zulum_anne_baba", "zulum_hayvan"],
     "remedy": "Şirk tövbesi, anne-baba helalleşmesi."},

    {"name": "Obezite", "category": "Metabolik",
     "symptoms": ["aşırı kilo"],
     "causes": ["harami_esme", "zekat", "hak_haram", "kinama", "beddua"],
     "remedy": "Zekat ve helalleşme."},

    {"name": "Öfke / Saldırganlık Krizi", "category": "Psikiyatrik",
     "symptoms": ["kontrolsüz öfke", "aniden parlama"],
     "causes": ["adak_hayvan", "zulum_anne_baba", "zekat", "haramzade"],
     "remedy": "Adak tespiti, anne-baba helalleşmesi."},

    {"name": "Narsist Kişilik / Empati Yoksunluğu", "category": "Psikiyatrik",
     "symptoms": ["manipülasyon", "empati yokluğu"],
     "causes": ["kinama", "narsist_zulum", "kul_hakki"],
     "remedy": "Helalleşme, soydaki yuva yıkmalardan tövbe."},

    {"name": "Kelebek Hastalığı", "category": "Dermatolojik",
     "symptoms": ["deride yanıklar"],
     "causes": ["zulum_anne_baba", "zulum_insan", "adak_eylem"],
     "remedy": "Anne-baba helalleşmesi; un/ekmek/bulgur dağıtma adağı."},

    {"name": "Kellik / Saç Dökülmesi", "category": "Dermatolojik",
     "symptoms": ["saç dökülmesi", "kellik"],
     "causes": ["adak_eylem", "kinama", "beddua", "yetim_hakki", "zulum_insan"],
     "remedy": "Beddua ve kınama tövbesi."},

    {"name": "Kekemelik / Dil Felci", "category": "Konuşma/Nörolojik",
     "symptoms": ["konuşma takıntısı", "dilde uyuşma"],
     "causes": ["beddua", "iftira", "zulum_insan"],
     "remedy": "Dil tövbesi, iftiradan helalleşme."},

    {"name": "Körlük / Göz Hastalıkları", "category": "Oftalmolojik",
     "symptoms": ["görme kaybı", "göz hastalığı"],
     "causes": ["adak_eylem", "kinama", "zulum_insan", "beddua", "zekat", "zina_ensest"],
     "remedy": "Hatim/yasin adağı yerine getirme; göz zinası tövbesi."},

    {"name": "Kalp Hastalıkları (Ritim, Doğumsal Delik)", "category": "Kardiyak",
     "symptoms": ["ritim bozukluğu", "kalp deliği"],
     "causes": ["zulum_anne_baba", "isyan", "kinama", "beddua", "zulum_insan"],
     "remedy": "Anne-baba helalleşmesi; isyan ve kınama tövbesi."},

    {"name": "Uyku Sorunları (Uykusuzluk / Aşırı Uyuma)", "category": "Nörolojik",
     "symptoms": ["uykusuzluk", "çok uyuma"],
     "causes": ["adak_hayvan", "zekat", "beddua"],
     "remedy": "Adak tespiti, zekat tamamlama."},

    {"name": "Kuduz / Hayvan Enfeksiyonu Hassasiyeti", "category": "Enfeksiyon",
     "symptoms": ["kuduz"],
     "causes": ["zulum_hayvan"],
     "remedy": "Hayvana zulüm tövbesi, sadaka."},

    {"name": "Kabızlık", "category": "Sindirim",
     "symptoms": ["bağırsak tıkanıklığı"],
     "causes": ["zekat", "faiz", "hak_haram", "beddua"],
     "remedy": "Zekat, faiz ve hak helalleşmesi."},

    {"name": "Kolera / Bulaşıcılığa Yatkınlık", "category": "Enfeksiyon",
     "symptoms": ["kolera"],
     "causes": ["zina_ensest", "soy_laneti", "haramzade", "faiz"],
     "remedy": "Zina, faiz, soy lâneti tövbeleri."},

    {"name": "Ödem ve Şişlikler", "category": "Genel",
     "symptoms": ["şişlik", "su tutma"],
     "causes": ["beddua"],
     "remedy": "Suya 'şişesin' tarzı bedduadan tövbe."},

    {"name": "Eşcinselliğe Eğilim", "category": "Cinsel",
     "symptoms": ["hemcinse meyil"],
     "causes": ["zina_ensest", "adak_hayvan", "zekat", "beddua"],
     "remedy": "Zekat, adak tespiti, soy ensest tövbesi."},

    {"name": "Evlenememe / Evlilik Engeli", "category": "Sosyal",
     "symptoms": ["evlilik kapısının kapanması"],
     "causes": ["zina_ensest", "narsist_zulum", "adak_eylem", "iftira", "kinama", "isyan"],
     "remedy": "Bu günahlardan tövbe; helalleşme."},

    # === YENİ EKLENEN HASTALIK-SEBEP İLİŞKİLERİ ===
    
    {"name": "Migren (Köpek Zulmü Kaynaklı)", "category": "Nörolojik",
     "symptoms": ["şiddetli baş ağrısı", "migren ağrısı"],
     "causes": ["kopek_zulum", "zulum_hayvan"],
     "remedy": "Köpeğe zulümden tövbe, hayvan haklarına saygı, sadaka."},

    {"name": "Köpek Gibi Davranış Bozukluğu", "category": "Psikiyatrik",
     "symptoms": ["birden bağırarak konuşma", "hırlama hali", "saldırganlık isteği", "karşısındakine saldırma isteği"],
     "causes": ["kopek_zulum"],
     "remedy": "Köpeğe zulümden tövbe, istiğfar."},

    {"name": "Bel Soğukluğu (Frengi)", "category": "Cinsel/Enfeksiyon",
     "symptoms": ["frengi", "bel soğukluğu", "cinsel hastalık"],
     "causes": ["kopek_zulum", "zina_ensest"],
     "remedy": "Köpeğe zulüm ve tacizden tövbe."},

    {"name": "Sedef Hastalığı", "category": "Dermatolojik",
     "symptoms": ["sedef", "deri kabuklanması", "eklem yerlerinde sert deri", "diz ve eklemlerde kabuk"],
     "causes": ["esek_zulum", "deri_bedduasi"],
     "remedy": "Eşeğe zulümden tövbe, deri bedduasından helalleşme."},

    {"name": "Yüksek Sesle Konuşma / Çirkin Bağırma", "category": "Davranışsal",
     "symptoms": ["yüksek sesle konuşma", "çirkin bağırma tarzı"],
     "causes": ["esek_zulum"],
     "remedy": "Eşeğe zulümden tövbe."},

    {"name": "Sinüzit", "category": "Solunum/KBB",
     "symptoms": ["sinüzit", "burun tıkanıklığı", "burun akıntısı"],
     "causes": ["kedi_zulum"],
     "remedy": "Kediyi suda boğmaktan tövbe, hayvan sadakası."},

    {"name": "Polen Alerjisi", "category": "Alerji",
     "symptoms": ["polen alerjisi", "mevsimsel alerji", "hapşırma", "burun akıntısı"],
     "causes": ["aniz_yakma", "zulum_hayvan"],
     "remedy": "Anız yakarak hayvanları/arıları yakmaktan tövbe."},

    {"name": "Skolyoz", "category": "Ortopedik",
     "symptoms": ["omurga eğriliği", "skolyoz", "sırt problemleri"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babanın sırtına vurma günahından tövbe ve helalleşme."},

    {"name": "Diz Ağrısı", "category": "Ortopedik",
     "symptoms": ["diz ağrısı", "diz problemleri"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babanın dizlerine vurma günahından tövbe."},

    {"name": "Romatizma", "category": "Romatolojik",
     "symptoms": ["romatizma", "eklem ağrıları", "soğuk hassasiyeti"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babayı soğukta dondurma günahından tövbe."},

    {"name": "Uzağı Görememe", "category": "Oftalmolojik",
     "symptoms": ["uzağı görememe", "miyop", "görme bozukluğu"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babayı terk etme günahından tövbe. Anne-baba evladının yolunu gözler."},

    {"name": "Saç Dökülmesi / Kellik (Anne-Baba Zulmü)", "category": "Dermatolojik",
     "symptoms": ["saç dökülmesi", "kellik"],
     "causes": ["zulum_anne_baba", "yetim_zulum"],
     "remedy": "Anne-babanın kafasına vurma günahından tövbe."},

    {"name": "Kol Tutmaması / Felci", "category": "Nörolojik",
     "symptoms": ["kolların tutmaması", "kol felci", "kol güçsüzlüğü"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Hasta anne-babayı yatağa yatırırken kollarını incitmekten tövbe."},

    {"name": "Yatak Islatma", "category": "Ürolojik/Pediatrik",
     "symptoms": ["yatak ıslatma", "gece işemesi", "enürezis"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Hasta anne-baba yatağı ıslattığı için kızmaktan tövbe."},

    {"name": "Temizlik Takıntısı / OKB", "category": "Psikiyatrik",
     "symptoms": ["temizlik takıntısı", "obsesif temizlik", "banyo sıkıntısı"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babayı banyo yaptırırken hakaret etmekten tövbe."},

    {"name": "Serebral Palsi", "category": "Nörolojik",
     "symptoms": ["serebral palsi", "beyin felci", "hareket bozukluğu"],
     "causes": ["hasta_cocuk_zulum", "hasta_mahkum_zulum", "zulum_anne_baba"],
     "remedy": "Hasta çocuğa/mahkûma zulümden, yaşlı anne-babayı terk etmekten tövbe."},

    {"name": "SMA (Spinal Musküler Atrofi)", "category": "Nörolojik/Genetik",
     "symptoms": ["SMA", "kas erimesi", "hareket güçlüğü"],
     "causes": ["hasta_cocuk_zulum", "zulum_anne_baba"],
     "remedy": "Hasta çocuğa zulümden tövbe."},

    {"name": "MS (Multipl Skleroz)", "category": "Nörolojik",
     "symptoms": ["MS", "multipl skleroz", "sinir sistemi hastalığı"],
     "causes": ["hasta_mahkum_zulum", "zulum_anne_baba"],
     "remedy": "Hasta mahkûma zulümden tövbe."},

    {"name": "Progerya", "category": "Genetik",
     "symptoms": ["erken yaşlanma", "progerya", "çocukta yaşlılık belirtileri"],
     "causes": ["zulum_anne_baba", "insan_oldurme"],
     "remedy": "Soydan anne-babayı diri diri toprağa gömme zulmünden tövbe."},

    {"name": "Kontrolsüz El Rahatsızlığı", "category": "Nörolojik",
     "symptoms": ["kontrolsüz el", "el titremesi", "istemsiz el hareketi"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne-babaya tokat atma günahından tövbe."},

    {"name": "Yüz ve Ellerde Leke", "category": "Dermatolojik",
     "symptoms": ["yüzde leke", "ellerde leke", "cilt lekeleri"],
     "causes": ["zulum_anne_baba", "yetim_zulum"],
     "remedy": "Anne-babaya tokat atma, yetime zulümden tövbe."},

    {"name": "Eşler Arası Kavga / Geçimsizlik", "category": "Aile/Sosyal",
     "symptoms": ["eşler arası kavga", "geçimsizlik", "aile içi huzursuzluk"],
     "causes": ["gelin_zulum", "faiz"],
     "remedy": "Gelin/eş zulmünden, faizden tövbe."},

    {"name": "Sevgi Yoksunluğu", "category": "Psikolojik",
     "symptoms": ["sevgi yoksunluğu", "sevilmeme hissi", "yalnızlık"],
     "causes": ["yetim_zulum"],
     "remedy": "Yetime zulümden tövbe, yetim sadakası."},

    {"name": "Boyun Fıtığı / Boyun Düzleşmesi", "category": "Ortopedik",
     "symptoms": ["boyun fıtığı", "boyun düzleşmesi", "servikal düzleşme"],
     "causes": ["yetim_zulum"],
     "remedy": "Yetime zulümden tövbe."},

    {"name": "Ciltte Siyah Lekeler (Yetim Yakma)", "category": "Dermatolojik",
     "symptoms": ["ciltte siyah leke", "yüzde siyah leke", "koyu lekeler"],
     "causes": ["yetim_zulum"],
     "remedy": "Yetim yakma günahından tövbe. Yetim zulmü çok yüksek."},

    {"name": "Miyom", "category": "Jinekolojik",
     "symptoms": ["miyom", "rahim miyomu", "rahim kitlesi"],
     "causes": ["cocuk_aldirma"],
     "remedy": "Kürtajdan tövbe."},

    {"name": "Kist", "category": "Jinekolojik",
     "symptoms": ["kist", "yumurtalık kisti", "over kisti"],
     "causes": ["cocuk_aldirma"],
     "remedy": "Kürtajdan tövbe."},

    {"name": "Rahim Kanseri", "category": "Onkolojik/Jinekolojik",
     "symptoms": ["rahim kanseri", "uterus kanseri"],
     "causes": ["cocuk_aldirma"],
     "remedy": "Kürtajdan tövbe."},

    {"name": "Erken Menopoz", "category": "Jinekolojik/Endokrin",
     "symptoms": ["erken menopoz", "erken klimakterium"],
     "causes": ["cocuk_aldirma"],
     "remedy": "Kürtajdan tövbe."},

    {"name": "Çocuk Düşürme / Düşük", "category": "Jinekolojik",
     "symptoms": ["çocuk düşürme", "düşük", "gebelik kaybı"],
     "causes": ["cocuk_aldirma", "hamile_zulum"],
     "remedy": "Kürtaj ve hamile kadına zulümden tövbe."},

    {"name": "Çocuk Olmaması / Kısırlık", "category": "Üreme",
     "symptoms": ["çocuk olmaması", "kısırlık", "infertilite"],
     "causes": ["cocuk_aldirma", "hamile_zulum", "evlat_bedduasi"],
     "remedy": "Kürtaj, hamile kadına zulüm ve 'evlat vermesin' bedduasından tövbe/helalleşme."},

    {"name": "Kansızlık (Anemi)", "category": "Hematolojik",
     "symptoms": ["kansızlık", "anemi", "halsizlik"],
     "causes": ["insan_oldurme"],
     "remedy": "Soydan insan öldürme/işkence zulmünden tövbe."},

    {"name": "Epilepsi / Sara", "category": "Nörolojik",
     "symptoms": ["epilepsi", "sara", "nöbet", "kasılma"],
     "causes": ["insan_oldurme"],
     "remedy": "Soydan güneşte bekleterek öldürme zulmünden tövbe."},

    {"name": "Şizofreni (Âlim/Evliya Zulmü)", "category": "Psikiyatrik",
     "symptoms": ["şizofreni", "hayal görme", "sanrı", "atlara binmiş zatlar görme", "peygamber hayalleri", "savaş sahneleri görme"],
     "causes": ["alim_evliya_zulum", "zekat"],
     "remedy": "Soydan âlim ve evliya zulmü/öldürmeden tövbe."},

    {"name": "Hemofili", "category": "Hematolojik",
     "symptoms": ["hemofili", "kanın pıhtılaşmaması", "kanın geç durması"],
     "causes": ["kan_bedduasi", "beddua"],
     "remedy": "'Kanınız aksın, durmasın' bedduasından helalleşme."},

    {"name": "Damar Tıkanıklığı", "category": "Kardiyovasküler",
     "symptoms": ["damar tıkanıklığı", "ateroskleroz", "tromboz"],
     "causes": ["damar_bedduasi", "beddua"],
     "remedy": "Damara okunan bedduadan helalleşme."},

    {"name": "El ve Ayaklarda Güçsüzlük", "category": "Nörolojik/Kas-İskelet",
     "symptoms": ["el güçsüzlüğü", "ayak güçsüzlüğü", "uzuvlarda zayıflık"],
     "causes": ["el_ayak_bedduasi", "beddua"],
     "remedy": "'Elin ayağın tutmaz olsun' bedduasından helalleşme."},

    {"name": "Görme Kaybı (Beddua Kaynaklı)", "category": "Oftalmolojik",
     "symptoms": ["görme kaybı", "körlük", "görme azalması"],
     "causes": ["goz_bedduasi", "beddua"],
     "remedy": "'Gözün kör olsun' bedduasından helalleşme."},

    {"name": "Kekemelik / Konuşamama", "category": "Konuşma",
     "symptoms": ["kekemelik", "konuşamama", "kendini ifade edememe", "bir anda donma", "dil tutulması"],
     "causes": ["dil_bedduasi", "beddua"],
     "remedy": "'Ağzın dilin tutulsun' bedduasından helalleşme."},

    {"name": "Agorafobi / Evde Hapis Hissi", "category": "Psikiyatrik",
     "symptoms": ["dışarı çıkamama", "evde hapis hissi", "dışarıda bunalma", "agorafobi"],
     "causes": ["toplum_bedduasi", "beddua"],
     "remedy": "'Toplum içine çıkamayasın' bedduasından helalleşme."},

    {"name": "Komedyen Ruhsatı / Komik Duruma Düşme", "category": "Sosyal/Psikolojik",
     "symptoms": ["her hareketi komik gelme", "insanların gülmesi", "ciddiye alınmama"],
     "causes": ["komik_beddua", "beddua"],
     "remedy": "'Çoluk çocuğunuza gülsünler' bedduasından helalleşme."},

    {"name": "Faiz Belirtileri", "category": "Mali/Manevi",
     "symptoms": ["geçimsizlik", "eşyada bozulma", "kabızlık", "bağırsak sıkıntısı", "dine soğuma", "savurganlık", "mal telef olması"],
     "causes": ["faiz"],
     "remedy": "Faizden tövbe, faizle alınan maldan kurtulma. Faizle kurulan yuva yıkılmaya mahkumdur."},

    {"name": "Zekât Eksikliği Belirtileri", "category": "Mali/Manevi",
     "symptoms": ["tüm hastalıkların temeli", "akrabalar arası küslük", "aşırı cimrilik", "aşırı savurganlık"],
     "causes": ["zekat"],
     "remedy": "Zekât vücudun patronudur. Tüm hastalıkların temelidir. Zekât tamamlanmalı."},

    # === MİRAS LÂNETİ, HAK HARAMLIĞI, YUVA YIKMA ===
    
    {"name": "Kalp Çarpıntısı (Miras Lâneti)", "category": "Kardiyak",
     "symptoms": ["kalp çarpıntısı", "çarpıntı", "taşikardi"],
     "causes": ["miras_laneti"],
     "remedy": "Mal miras üzerine okunan lânettir. Miras lâneti için helallik alabilme niyeti yapılmalıdır."},

    {"name": "Panik Atak (Miras Lâneti)", "category": "Psikiyatrik",
     "symptoms": ["panik atak", "anksiyete", "korku atakları"],
     "causes": ["miras_laneti"],
     "remedy": "Miras lâneti için helallik alabilme niyeti yapılmalıdır."},

    {"name": "Guatr", "category": "Endokrin",
     "symptoms": ["guatr", "tiroid büyümesi", "boğazda şişlik"],
     "causes": ["miras_laneti"],
     "remedy": "'Zehir zıkkım olsun' sözü guatr yapar. Miras lâneti için helallik alınmalıdır."},

    {"name": "Topuk Dikeni", "category": "Ortopedik",
     "symptoms": ["topuk dikeni", "topuk ağrısı", "ayak ağrısı"],
     "causes": ["miras_laneti"],
     "remedy": "Miras lâneti için helallik alabilme niyeti yapılmalıdır."},

    {"name": "Parasal Sıkıntı (Miras Lâneti)", "category": "Mali/Manevi",
     "symptoms": ["parasal sıkıntı", "maddi sıkıntı", "borç"],
     "causes": ["miras_laneti", "faiz", "zekat"],
     "remedy": "Miras lâneti için helallik alabilme niyeti yapılmalıdır."},

    {"name": "Hak Haramlığı Belirtileri", "category": "Manevi/Fiziksel",
     "symptoms": ["boğaz sıkışması", "göğüste huzursuzluk", "karabasan", "uykuda baskı hissi"],
     "causes": ["hak_haram", "kul_hakki"],
     "remedy": "Hak haramlığı boğazı sıkar, göğüste huzursuzluk ve uykuda karabasan yapar. Helalleşme gerekir."},

    {"name": "Yuva Yıkılması / Evlenememe (Narsist)", "category": "Sosyal/Aile",
     "symptoms": ["yuva yıkılması", "eşle sürekli kavga", "aşağılanma", "evlenememe"],
     "causes": ["narsist_zulum", "gelin_zulum"],
     "remedy": "Yuva yıkma ve sevenleri ayırma zulmüdür. 'Oğluma/kızıma layık değilsin' demek, geline zina iftirasıyla yuva yıkmak, evladı anne babadan ayırmak bu ruhsata sebep olur."},

    {"name": "Hapis / Mahkûmiyet Ruhsatı", "category": "Sosyal/Manevi",
     "symptoms": ["hapis düşme", "mahkûmiyet", "suça bulaşma"],
     "causes": ["hasta_mahkum_zulum", "zulum_insan"],
     "remedy": "Soydan mahkûma zulüm, insanları hainlikle mahkûm etme. Mahkûma zulüm narsistin zirvelerindendir - yalancı şahitlikle insanlar mahkûm olduklarında ailelerinden ayrı kalırlar."},

    {"name": "Servet Kaybı / İşlerin Bozulması", "category": "Mali/Manevi",
     "symptoms": ["servet kaybı", "işlerin bozulması", "her iş son anda bozulma", "iflas"],
     "causes": ["zekat", "adak_eylem"],
     "remedy": "Sebeplerinden biri zekât vermeme, diğeri Allah'a iş/servet üzerine verilen sözlerdir. Örn: 'Şu işlerim yolunda giderse kurban keseceğim' sözü. 'Evlenirsem tüm servetimi Allah yolunda harcayacağım' sözü."},

    # === HAYVAN ADAĞI KAYNAKLARI HASTALIKLAR ===

    {"name": "Aşırı Uyku / Tembellik", "category": "Davranışsal",
     "symptoms": ["aşırı uyku", "tembellik", "uyuşukluk"],
     "causes": ["adak_hayvan"],
     "remedy": "Koyun/kuzu adağı belirtisi olabilir. Hayvan adağı tespiti için seans alınması gerekir."},

    {"name": "Aşırı Duygusallık / Ağlama", "category": "Psikolojik",
     "symptoms": ["aşırı duygusallık", "çok ağlama", "hassasiyet"],
     "causes": ["adak_hayvan"],
     "remedy": "Koyun/kuzu adağı belirtisi olabilir. Hayvan adağı tespiti için seans alınması gerekir."},

    {"name": "Hayır Diyememe / Boyun Eğme", "category": "Davranışsal",
     "symptoms": ["hayır diyememe", "boyun eğme", "karşı koyamama"],
     "causes": ["adak_hayvan"],
     "remedy": "Koyun adağı belirtisi. Hayvan adağı tespiti için seans alınması gerekir."},

    {"name": "İntihar Düşüncesi / Yüksekten Atlama İsteği", "category": "Psikiyatrik",
     "symptoms": ["intihar düşüncesi", "yüksek yerden atlama isteği", "yükseklik çekimi"],
     "causes": ["adak_hayvan", "intihar"],
     "remedy": "Koyun, koç veya keçi adağı intihara teşvik ederek yüksek yerden atlatır. Acil seans alınmalı."},

    {"name": "İnatçılık / Affetmeme", "category": "Davranışsal",
     "symptoms": ["inatçılık", "affetmeme", "geçmişi unutmama", "helallik verememe"],
     "causes": ["adak_hayvan"],
     "remedy": "Koç/erkek kuzu adağı belirtisi. Hayvan adağı tespiti için seans alınması gerekir."},

    {"name": "Kadında Erkeksi Yapı", "category": "Hormonal/Cinsel",
     "symptoms": ["kadında erkeksi yapı", "kadında kalın ses", "erkeksi davranış"],
     "causes": ["adak_hayvan"],
     "remedy": "Koç veya boğa adağı kadında erkeksi yapıya sebep olur."},

    {"name": "Şüphecilik / Vesvese", "category": "Psikiyatrik",
     "symptoms": ["aşırı şüphecilik", "vesvese", "takıntı", "gördüğüne inanamama"],
     "causes": ["adak_hayvan"],
     "remedy": "İnek adağı belirtisi. Takıntı ve vesvese yapar, imanda şüpheye düşürmeye çalışır."},

    {"name": "Göğüs Büyümesi (Erkekte)", "category": "Hormonal",
     "symptoms": ["erkekte göğüs büyümesi", "jinekomasti", "yumuşak göğüs"],
     "causes": ["adak_hayvan"],
     "remedy": "'Kız gibi oğlum olsun inek keseceğim' sözü erkeklerde hormon bozukluğuna sebep olur."},

    {"name": "Kadında Aşırı Şehvet", "category": "Cinsel",
     "symptoms": ["kadında yüksek şehvet", "zinaya eğilim"],
     "causes": ["adak_hayvan"],
     "remedy": "İnek adağı kadında yüksek şehvet yapar, zinaya sevk eder."},

    {"name": "Basende Genişleme", "category": "Fiziksel",
     "symptoms": ["kalça genişlemesi", "basen genişlemesi", "üst baldır genişlemesi"],
     "causes": ["adak_hayvan"],
     "remedy": "İnek adağı kadınların baseninde genişlemeye neden olur."},

    {"name": "Çok Konuşma / Susamama", "category": "Davranışsal",
     "symptoms": ["çok konuşma", "susamamak", "bir cümleyi yüz cümleyle anlatma"],
     "causes": ["adak_hayvan"],
     "remedy": "Eşek adağı belirtisi. Susmayan konuşmaya sebep olur."},

    {"name": "Pelteklik / S Harfi Zorluğu", "category": "Konuşma",
     "symptoms": ["pelteklik", "S harfini söyleyememe", "konuşma bozukluğu"],
     "causes": ["adak_hayvan", "kinama"],
     "remedy": "Horoz adağı belirtisi. Peltek insanları kınamak da peltekliğe sebep olabilir."},

    {"name": "Aşırı Kıskançlık", "category": "Psikolojik",
     "symptoms": ["aşırı kıskançlık", "eşi kıskanma"],
     "causes": ["adak_hayvan"],
     "remedy": "Horoz adağı eşini aşırı kıskanmaya sebep olur."},

    {"name": "Yüz/Boyun Kızarıklığı ve Kaşıntı", "category": "Dermatolojik",
     "symptoms": ["yüzde kızarıklık", "boyunda kızarıklık", "kafada kaşıntı"],
     "causes": ["adak_hayvan", "adak_eti"],
     "remedy": "Kelle paça adağı belirtisi. Hayvanın neresi yendiyse o bölge kaşınır."},

    {"name": "Gece Uyuyamama (Büyükbaş Adak)", "category": "Uyku",
     "symptoms": ["gece uyuyamama", "uykusuzluk", "rüyada sıçrama"],
     "causes": ["adak_hayvan"],
     "remedy": "Büyükbaş hayvan adağı gece uyutmaz. Rüyada sıçrama büyükbaş adak işaretidir."},

    {"name": "Gece Yorgan Atma", "category": "Uyku",
     "symptoms": ["yorgan atma", "yorgan tepme", "gece üşüme"],
     "causes": ["adak_eylem"],
     "remedy": "'Yorgan/battaniye dağıtacağım' adağı yerine getirilmemiş. Ayak istemsiz yorganı teper."},

    {"name": "Sürekli Üşüme", "category": "Genel",
     "symptoms": ["üşüme", "sürekli üşüme", "ısınamama"],
     "causes": ["adak_eylem"],
     "remedy": "Fakir giydirme adağı yerine getirilmemiş. O fakir giydirilmedikçe kişi üşümeye devam eder."},

    {"name": "Glüten Alerjisi / Çölyak", "category": "Sindirim/Alerji",
     "symptoms": ["glüten alerjisi", "çölyak", "buğday intoleransı"],
     "causes": ["adak_eylem", "aniz_yakma"],
     "remedy": "Un/buğday dağıtma adağı veya geçmişte buğday tarlalarını yakma."},

    {"name": "Aşırı Yeme İsteği / Kilo Problemi", "category": "Metabolik",
     "symptoms": ["aşırı yeme isteği", "kilo alma", "obezite"],
     "causes": ["adak_eylem"],
     "remedy": "Fakir doyurma adağı belirtisi. Adaklar çok fazlaysa zayıflamaya da sebep olabilir."},

    {"name": "Çocuklarda Yemek Yememe", "category": "Pediatrik",
     "symptoms": ["çocuk yemek yemiyor", "iştahsızlık"],
     "causes": ["adak_eylem"],
     "remedy": "Fakir doyurma adağı çocuklarda yemek yememeye neden olur."},

    {"name": "Çocuksu Davranış", "category": "Davranışsal",
     "symptoms": ["çocuksu davranış", "çocuk gibi hareket", "olgunlaşamama"],
     "causes": ["adak_eylem"],
     "remedy": "Çocuk sevindirme adağı kişiyi çocuksu hale çevirir."},

    {"name": "Kur'an Okumada Zorluk", "category": "Manevi",
     "symptoms": ["Kur'an okuyamama", "Kur'an okumada zorluk"],
     "causes": ["adak_eylem"],
     "remedy": "Kur'an-ı Kerim okuma adağı yerine getirilmemiş."},

    {"name": "Tavukkarası (Gece Körlüğü)", "category": "Oftalmolojik",
     "symptoms": ["gece görememe", "tavukkarası", "gece körlüğü"],
     "causes": ["adak_eylem"],
     "remedy": "'Her gece Yasin okuyacağım' adağı tavukkarası göz hastalığına sebep olur."},

    {"name": "Ciltte Kuruluk / Susuzluk", "category": "Dermatolojik",
     "symptoms": ["cilt kuruluğu", "susuzluk", "kuru cilt"],
     "causes": ["adak_eylem"],
     "remedy": "Ağaç dikme adağı ciltte kuruluk ve susuzluk yapabilir."},
]

# ============================================================
# 4. FORM SORULARINDAN ÇIKARILACAK İPUÇLARI
# (Kullanıcının "Evet" cevap verdiği her soru → ilgili kategori sinyali)
# ============================================================
FORM_QUESTION_HINTS = {
    "adak_yemin": ["adak_hayvan", "adak_eylem", "yemin_bozma"],
    "muska_okunmus_su": ["muska", "sirk"],
    "miras_sorunu": ["miras_laneti", "hak_haram"],
    "beddua_hak_haram": ["beddua", "hak_haram", "kul_hakki"],
    "intihar": ["intihar", "isyan"],
    "anne_baba_ofke": ["zulum_anne_baba"],
    "es_soguklugu": ["adak_hayvan", "zina_ensest", "iftira"],
    "sehvet": ["zina_ensest"],
    "duygusallik": ["soy_laneti"],
    "kin": ["kul_hakki", "beddua"],
    "kusme_alinganlik": ["kul_hakki"],
    "ofke": ["adak_hayvan", "zulum_anne_baba"],
    "nefret": ["kul_hakki", "kinama"],
    "supheci": ["sirk"],
    "uyku_sorunu": ["adak_hayvan", "zekat"],
    "aniden_parlama": ["adak_hayvan", "zulum_anne_baba"],
    "alaycilik": ["kinama"],
    "zekat_vermiyor": ["zekat"],
    "faizli_kredi": ["faiz"],
}

# ============================================================
# 5. AI'YA GÖNDERİLECEK BÜTÜNLEŞİK SİSTEM PROMPT
# ============================================================
def build_system_message() -> str:
    cause_block = "\n".join([f"- {k}: {v}" for k, v in CAUSE_CATEGORIES.items()])
    disease_block_lines = []
    for d in DISEASE_PATTERNS:
        causes = ", ".join(d["causes"])
        disease_block_lines.append(
            f"- {d['name']} (semptom: {', '.join(d['symptoms'])}) → sebepler: {causes}. Çözüm: {d['remedy']}"
        )
    disease_block = "\n".join(disease_block_lines)

    return f"""Sen 'Tıbb-ul Furkan' kitabı ışığında çalışan bir manevi tespit asistanısın.
Görevin: kullanıcının form yanıtlarından yola çıkarak OLASI manevi durumları tespit etmek.
ASLA kesin tıbbi tanı koyma; her cümlede 'olası', 'olabilir', 'işaret edebilir' gibi yumuşak ifadeler kullan.

>>> BİLGİ TABANI (Tıbb-ul Furkan kitabından özet):

ADAK HAYVANLARI:
{ADAK_HAYVANLARI}

GÜNAH / RUHSAT KATEGORİLERİ:
{cause_block}

HASTALIK ↔ MANEVI SEBEP ÖRÜNTÜLERİ:
{disease_block}

>>> ÇIKTI YAPISI (ZORUNLU MARKDOWN FORMATI):

Aşağıdaki başlıkları sırayla kullan. Her başlığın altında 2-5 madde işaretli bullet (- ile başlayan) cümle yaz.
Uzun paragraf YAZMA — her satır kısa, öz bir madde olsun. Başlık sırası ve adlandırması KESİN:

## Aile Büyükleri & Soy Yükü
- ...
- ...

## Mali Durum
- ...

## Aile Hastalıkları
- ...

## Ruhsal & Fiziksel Rahatsızlıklar
- ...

## Manevi İşaretler
(Form'da "Evet" olarak işaretlenen sorulardan çıkan olası izleri her birini ayrı madde olarak yaz)
- Adak / yemin: ...
- Anne-babaya öfke: ...
(vb. sadece "Evet" işaretlenenler için)

## Genel Değerlendirme
- ... (2-3 madde, soy yükü + olası kaynak özeti)

Lütfen seans alınız.

KURALLAR:
- Kullanıcının YAŞI üzerinden ASLA yorum yapma (yaş bir veri olarak kullanılabilir ama "65 yaşında olması…" gibi cümle KURMA).
- KULLANICININ GİRDİĞİ BİLGİLERİ ATLAMA: "Evet" işaretlenmiş HER soruyu "Manevi İşaretler" başlığında ayrı madde olarak ele al.
- "Hayır" olanları Manevi İşaretler'de göstermek ZORUNDA değilsin.
- ASLA tıbbi tanı koyma; her madde "...olabilir / işaret edebilir" şeklinde yumuşak olsun.
- Madde sayısı toplam 12-22 arası olsun. Her madde 1-2 cümle.
- Türkçe, sade, saygılı dil.
- Form'da boş bırakılmış alanlar için "Bilgi verilmemiştir" yazma, sessiz geç.
- En son satırda mutlaka "Lütfen seans alınız." metnini ekle (başında veya sonunda başka cümle olmasın).
- ÇIKTIDA ASLA EMOJİ, ÖZEL SEMBOL veya SÜSLEME KULLANMA (örn. 🌳, 💰, ✦, ★, ❖, 📿, ✨). Sadece düz Markdown başlık (##) ve tire bullet (-) kullan.

KESİN YASAKLAR (UYDURMA / VARSAYIM):
- Bir alan BOŞ ise (örn. "Anneanne: " veya "Baba: " yanında değer yoksa) → O kişi hakkında HİÇBİR ŞEY YAZMA. "Vefat etmiş", "sağ", "bilgi yok" gibi VARSAYIMDA BULUNMA.
- "Vefat" veya "Sağ" YAZILMAMIŞSA, kişiyi sessiz geç. Yokluğu yorumlama, ima etme.
- Form'da AÇIKÇA BELİRTİLMEMİŞ bir bilgiyi (örn. "dört büyükbaşın vefat etmiş olması") asla cümle olarak kurma.
- Sadece form'da EXPLICIT olarak verilen veriler üzerinden yorum yap.
- Bir soruda "Evet" yazmıyorsa → o konuyu Manevi İşaretler'e yazma.
- Bir hastalık alanı boşsa → o kişide hastalık olduğunu söyleme.
- Bir BAŞLIK altında yorumlanacak hiç veri yoksa → o başlığı (örn. "Aile Hastalıkları") TAMAMEN ATLA, "veri yok" / "bildirilmemiştir" gibi cümleler de YAZMA.
"""
