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
- Erkekte DİŞİ adak çoksa: cinsel isteksizlik, eşine soğukluk, hemcinse meyil riskleri artar.
- Kadında ERKEK adak çoksa: aynı şekilde ters cinsiyet etkisi.
- Adak yerine getirilmemiş ise: 'açıkta kalmış adak' olarak vücuda yerleşir.
- Adak hayvanı çalındı / başkası yedi / usulsüz kesildi ise: kefareti tekrar verilmelidir.
- 5-6 adetten fazla adak (çoklu adak) ağır hastalık tetikleyebilir (örn. ensefalit, bipolar, otizm).
- Adak hayvanın ciğeri, kemiği, kafası yenirse o organa yönelik rahatsızlık tetiklenebilir.
- Hayvan adakları yendiği zaman egzamaya, reflüye sebep olur.
- Rüyada sıçrama olursa büyükbaş hayvan adağı işaretidir.
- Büyükbaş hayvan adakları gece uyutmaz.

HAYVAN ADAĞI TESPİTİ İÇİN SEANS ALINMASI GEREKİR.
Aşağıdaki belirtiler hayvan adağına işaret edebilir:

DAVRANIŞSAL BELİRTİLER:
- Uyku, tembellik, duygusallık, hayır diyememe
- İnatçılık, kadında erkeksi yapı, kıskançlık
- Yüksek yer sevgisi, yalnızlık, küsme
- Öfke patlaması, şehvet, şiddet eğilimi
- Şüphecilik, vesvese, göğüs büyümesi, şehvet
- Tembellik, çok konuşma, kekemelik
- Kıskançlık, pelteklik, S harfi zorluğu
- Sinirlilik, kincilik
- Çok uyutur, tembeldir
- Harama çağırıldığında hemen gider
- Aşırı duygusaldır ve ağlar
- Hayır diyemez, boyun eğer
- Kafa atar, inatçıdır, kincidir
- Geçmişi hatırlatır, gösterişi sever
- Affedemez, geçmişi unutmaz, helallik veremez
- Çabuk kalbi kırılır, hemen küser, boynunu büker
- Yalnız kalmayı sever
- Kafasını duvara vurarak sinirlenir
- Aniden öfke patlamasına neden olur
- Eliyle temas eder (kavga eder, vurar, kırar)
- Öfkelendiğinde evi yıkar, kendini durduramaz, sonra pişman olur ağlar
- "Ben erkek değil miyim? Benim sözüm neden tutulmuyor?" der
- Takıntı yapar, vesvese yapar, gözüyle gördüğüne inanmaz
- Gök bilimleri, astroloji merakı yapar
- İmanda şüpheye düşürmeye çalışır
- Eli kolu kalkmama, yavaş hareket etme
- Gece yemek yeme isteği yapar
- Susmayan konuşmaya sebep olur, çok konuşturur
- Bir konuyu bir cümleyle anlatacağına yüz cümleyle anlatır
- Aniden parlayıp çok konuşturur
- Eşini aşırı kıskanmaya sebep olur
- "S" harfini söylemede sıkıntı olur
- Dövüşürken ısırır
- Konuşmada pelteklik yapar
- İnsanı gıcık eder, dalga geçer
- Tükürür

FİZİKSEL BELİRTİLER:
- Kadında bazen erkek sesi çıkartır
- Kadının alnında sivilce çıkartır
- Erkekte şehvet yapar, kadında cinsel soğukluk yapar
- Kadınlarda erkeksi yapıya sebep olur
- Erkeklerde dik başlılık yapar
- Erkeklerde aşırı şehvete neden olur
- Kadında erkeksi yapı ve cinsel soğukluk yapar
- Göğüs irileşmesine sebep olur ("Büyük memeli inek keseceğim" sözü)
- Erkeklerde hormon bozukluğu ve yumuşak göğüs ("Kız gibi oğlum olsun" sözü)
- Kadında yüksek şehvet yapar, zinaya sevk eder
- Kadınların üst baldırlarında (basende) genişlemeye neden olur
- Kekemeliğe sebep olabilir

TEHLİKELİ BELİRTİLER:
- İntihara teşvik ederek yüksek yerden atlatır
- Yüksek yerleri sever, yüksek yerlere çıkma isteği
- Çocuklarda belirtisi: yüksek yerlere çıkma, koltuklarda zıplama

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

ALTIN TAKMA ADAĞI:
- Yerine getirilmezse bebeklerde sarılık olabilir

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
    "lanet": "Yaratılmışlara (renk, gökkuşağı, güneş vb.) Lanet Okuma",
    "yalanci_sahitlik": "Yalancı Şahitlik",
    "ciger_bedduasi": "Ciğere Okunan Beddua",
    "mezarci_ruhsat": "Mezarcı Kişi Ruhsatı",
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

    # === YENİ EKLENEN BİLGİLER ===

    {"name": "Göz Titremesi / Göz Hareketi", "category": "Oftalmolojik",
     "symptoms": ["göz titremesi", "gözlerin sürekli hareketi", "nistagmus"],
     "causes": ["adak_eylem"],
     "remedy": "Soydan veya kendisinin adayıp yerine getirmediği hatim ve Yasin okuma adaklarıdır."},

    {"name": "Migren / Baş Ağrısı (Köpek Zulmü + Gusül)", "category": "Nörolojik",
     "symptoms": ["baş ağrısı", "migren", "şiddetli baş ağrısı"],
     "causes": ["kopek_zulum", "sirk"],
     "remedy": "Köpeğe zulüm ve eksik gusül baş ağrısı ve migren yapar."},

    {"name": "Bebeklerde Sarılık", "category": "Pediatrik",
     "symptoms": ["yenidoğan sarılığı", "bebek sarılığı", "sarılık"],
     "causes": ["adak_eylem"],
     "remedy": "Atalarının 'altın takacağım' sözü verip yerine getirmemelerinden dolayı bebek sarılık olmaktadır."},

    {"name": "Ciğer Rahatsızlıkları (Detaylı)", "category": "İç Hastalık",
     "symptoms": ["ciğer rahatsızlığı", "akciğer problemi", "karaciğer sorunu"],
     "causes": ["beddua", "adak_eti", "zulum_insan"],
     "remedy": "Ciğere okunan beddua, adak hayvanının ciğerini yemek ve kişiyi soğukta dondurmak ciğer rahatsızlığı yapar."},

    {"name": "Vertigo / Baş Dönmesi", "category": "Nörolojik",
     "symptoms": ["vertigo", "baş dönmesi", "denge bozukluğu"],
     "causes": ["isyan", "zekat"],
     "remedy": "Yaratılan dünyaya isyan etmek ve zekât vermemekten vertigo olur."},

    {"name": "Kulak Çınlaması", "category": "KBB",
     "symptoms": ["kulak çınlaması", "tinnitus", "kulakta ses"],
     "causes": ["sirk", "iftira", "kul_hakki"],
     "remedy": "Gıybet, iftira, laf taşıma gibi duyarak şirke düşüldüğünde kulak çınlaması yapar. Kulağa yerleşen ruhsatlardır. Bitmeyen kulak çınlamasında sese lânet okuma vardır."},

    {"name": "Ani İflas / Ani Boşanma", "category": "Mali/Aile",
     "symptoms": ["ani iflas", "ani boşanma", "beklenmedik kayıp"],
     "causes": ["faiz"],
     "remedy": "Faiz günahından gelen şeytan çok sinsidir. Belirti göstermeden bekler ve kişiyi birden iflas ettirir veya birden boşanmasına sebep olur. 'Allah ve Resulüne savaş açmıştır' ayeti gereği ruhsatı büyüktür."},

    {"name": "Şirk Ruhsatı Belirtileri", "category": "Manevi",
     "symptoms": ["kafanın arkasında ağrı", "ense ağrısı", "manevi ağırlık"],
     "causes": ["sirk", "muska"],
     "remedy": "Şirk günahından gelen şeytan vücuttaki diğer şeytanların patronudur, çok ağır bir ruhsattır. Kafanın arka bölgesine yerleşir. Allah'a ait esma ve sıfatları bir insana veya maddeye yüklemek (hocam beni her yerde görür, muska beni korur gibi) şirke düşürür."},

    {"name": "İsyan Belirtileri", "category": "Manevi/Psikolojik",
     "symptoms": ["bıktım hissi", "dayanamama", "ölmek isteme"],
     "causes": ["isyan", "intihar"],
     "remedy": "İsyanın en ufak kelimesi 'Bıktım artık, dayanamıyorum!'dur. Ölmek istemek ve intihara teşebbüs etmek isyanın zirvesidir."},

    # === ANNE BABA İSYANI, KİBİR, KINAMA ===

    {"name": "Bel Ağrısı (Anne Baba İsyanı)", "category": "Ortopedik",
     "symptoms": ["bel ağrısı", "bel fıtığı", "sırt ağrısı"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne babaya isyan etmek bel ağrısı ruhsatlarından biridir. Anne babamıza kendimiz için dua hazırlayıp, sürekli bizim için dua etmesini istemeliyiz."},

    {"name": "Elle ve Dille Yapılan Zulüm", "category": "Manevi/Tehlike",
     "symptoms": ["zulüm işaretleri", "elle zulüm", "dille zulüm"],
     "causes": ["zulum_insan", "beddua", "iftira"],
     "remedy": "Elle ve dille yapılan zulümler çok tehlikelidir. Helalleşme gerekir."},

    {"name": "Kibir Günahı Belirtileri", "category": "Manevi/Tehlike",
     "symptoms": ["kibir", "büyüklenme", "kendini üstün görme", "ululuk taslama"],
     "causes": ["kinama", "isyan"],
     "remedy": "'Kalbinde zerre miktar kibir olan cennete giremez' (Hadis-i Şerif). Azamet ve Kibriya sahibi Cenab-ı Haktır. Ululuk ve yücelik Cenab-ı Hakka aittir. İnsan ulu ve yüce olamaz, olmaya çalışırsa kibirlenirse büyük bir gazaba uğrar. 'Aciziz, fakiriz ya Rabbi!' demeliyiz."},

    {"name": "Kınama Günahı Sonuçları", "category": "Manevi/Sosyal",
     "symptoms": ["hayatın kilitlenmesi", "işlerin durması", "çocuklarda problemler"],
     "causes": ["kinama"],
     "remedy": "Kınama günahı çok tehlikelidir. Namaz kılmayanları, içki içenleri, zina edenleri, boşanan insanları, evlenemeyenleri kınamak, kınayan insanların ve çocuklarının hayatını kilitleyen günahlardır. Kınadığımız şeylere düşeriz."},

    # === ŞİZOFRENİ, EPİLEPSİ, GAZ, MİRAS LÂNETİ, ZONA ===

    {"name": "Şizofreni (Detaylı Sebepler)", "category": "Psikiyatrik",
     "symptoms": ["şizofreni", "sanrı", "hayal görme", "hezeyan"],
     "causes": ["alim_evliya_zulum", "zekat", "adak_hayvan"],
     "remedy": "Şizofrenin sebepleri: Soydan büyük bir zulümcünün olması (âlim, evliya zulmü), anne ve babasının vermediği kendi zekât miktarının 100 binin üstünde olması, soydan büyükbaş hayvan adakları şizofreni hastalığına sebep olabilmektedir. Kişinin şizofren olması Şeytanın lisandan hiç inmemesi demektir. Şizofren hastası tamamen düzelebilir inşaAllah."},

    {"name": "Epilepsi / Sara (Çocuklarda Detaylı)", "category": "Nörolojik/Pediatrik",
     "symptoms": ["epilepsi krizi", "sara nöbeti", "çocukta nöbet"],
     "causes": ["isyan", "cocuk_aldirma", "intihar", "adak_eylem"],
     "remedy": "Çocuğun epilepsi krizi geçirme sebebi olarak anne ve baba soyundan ruhsatların olması ve annesinin benzer hataları yapmasıyla ruhsatlar aktifleşir. Bu ruhsatlar: doğuma isyan, çocuk düşsün diye kendi karnına vurma, birisine kızdığı için kendini bir yerden atma, doğum rahat geçerse diye adadığı adaktır. Bunların hepsi birleşiyor ve epilepsiye neden oluyor."},

    {"name": "Şişkinlik ve Gaz (Adak Sütü)", "category": "Sindirim",
     "symptoms": ["şişkinlik", "gaz", "bebeklerde gaz", "karın şişliği"],
     "causes": ["adak_hayvan"],
     "remedy": "Adak hayvanının sütünü içmek kişide şişkinlik ve gaz yapar. Bebeklerdeki gazın sebebi budur."},

    {"name": "Panik Atak ve Kalp Çarpıntısı (Miras Lâneti Detaylı)", "category": "Kardiyak/Psikiyatrik",
     "symptoms": ["panik atak", "kalp çarpıntısı", "ritim bozukluğu", "kalp kası çırpınması"],
     "causes": ["miras_laneti"],
     "remedy": "Miras lâneti panikatak yapar. Bundan dolayı kalpte ritim bozukluğu, çarpıntı yapar. Aslında kalpte herhangi bir rahatsızlık yoktur, kalp kası üzerinde Şeytan çırpınma yapar."},

    {"name": "Kamburluk / Skolyoz / Omurga Sorunları", "category": "Ortopedik",
     "symptoms": ["kamburluk", "skolyoz", "omurga eğriliği", "omurilik sıkıntısı"],
     "causes": ["yetim_zulum", "zulum_anne_baba"],
     "remedy": "Kamburluk, skolyoz, omurilikteki sıkıntıların sebepleri genellikle yetime ve anne babaya zulümdür."},

    {"name": "Anne Baba Zulmü Detaylı Sonuçları", "category": "Çoklu/Fiziksel",
     "symptoms": ["romatizma", "skolyoz", "titreme", "kas erimesi"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Anne baba soğukta dondurulursa romatizmaya, kafasına sırtına vurulursa skolyoz, tokat atılırsa titremeye, yılanlı kuyuya atılırsa kas erimesine (yürüyen cenaze gibi olur) sebep olur."},

    {"name": "Zona Hastalığı", "category": "Dermatolojik/Enfeksiyon",
     "symptoms": ["zona", "herpes zoster", "deri döküntüsü", "yanıklı döküntü"],
     "causes": ["zulum_insan"],
     "remedy": "Zona hastalığının sebebi: kaynar suyla yakma, güneşte bekleterek yakma, sıcak çorba/yemekle yakmak, yemeği beğenmeyen kocanın karısının üstüne sıcak yemeği dökmesidir."},

    {"name": "Düşman Durdurma Operasyonu", "category": "Manevi/Koruma",
     "symptoms": ["düşmandan korunma", "şerli insanlardan korunma"],
     "causes": [],
     "remedy": "Bir kişi kırk gün düşmanına dua etse o, onun dostu olur. Şerli bir insanın saldırmaması, zarar vermemesi için o kişinin ve soyu adına tövbe edildiğinde, sadaka verildiğinde, tövbe namazı kılındığında ve Ayet-el Kürsî okunduğunda o insan saldıramaz. Bu düşmanı durdurma operasyonudur."},

    # === FAKİR DOYURMA VE GİYDİRME ADAKLARI ===

    {"name": "Zayıflama (Fakir Doyurma Adağı)", "category": "Metabolik",
     "symptoms": ["zayıflama", "kilo kaybı", "aşırı zayıflamak"],
     "causes": ["adak_eylem", "mezarci_ruhsat"],
     "remedy": "Fakir doyurma adağı ve mezarcı kişide zayıflama yapar."},

    {"name": "Ciltte Kaşıntı ve Egzama (Fakir Giydirme)", "category": "Dermatolojik",
     "symptoms": ["kaşıntı", "egzama", "cilt tahrişi"],
     "causes": ["adak_eylem"],
     "remedy": "Fakir giydirme adağı vücutta kaşıntıyı ve egzamayı tetikleyen ruhsattır."},

    {"name": "Üşüme (Fakir Giydirme + Soğukta Zulüm)", "category": "Genel",
     "symptoms": ["üşüme", "ısınamama", "soğuk hissetme"],
     "causes": ["adak_eylem", "zulum_insan"],
     "remedy": "Fakir giydirme adağı ve soğukta dondurarak yapılan zulüm ve işkence üşümeye neden olur."},

    # === LANET VE BEDDUA KAYNAKLARI ===

    {"name": "Renk Körlüğü", "category": "Oftalmolojik",
     "symptoms": ["renk körlüğü", "renkleri ayırt edememe", "renk görme bozukluğu"],
     "causes": ["beddua", "lanet"],
     "remedy": "Renk körlüğünün sebebi renklere, gökkuşağına lânet okumaktır."},

    {"name": "Boğaz İltihaplanması", "category": "KBB",
     "symptoms": ["boğaz iltihaplanması", "boğaz ağrısı", "yutkunma güçlüğü"],
     "causes": ["beddua", "soy_laneti"],
     "remedy": "Boğaz iltihaplanmasının sebebi akrabaların birbiri hakkında çok fazla beddualaşması, lânetleşmesi, zehir, zıkkım sözleri olabilmektedir."},

    # === HAYVAN ZULMÜ SEBEBLİ HASTALIKLAR ===

    {"name": "Sedef Hastalığı (Eşek Zulmü Detaylı)", "category": "Dermatolojik",
     "symptoms": ["sedef", "deri kabuklanması", "psoriasis"],
     "causes": ["esek_zulum", "zulum_hayvan"],
     "remedy": "Eşek, ne güzel bir hayvandır. Senin yükünü taşır buna hamd etmek yerine ona zulmedersen sen ve soyun sedef hastası olursunuz."},

    # === YALANCI ŞAHİTLİK VE HAK HARAMLIĞI ===

    {"name": "Körlük (Yalancı Şahitlik)", "category": "Oftalmolojik",
     "symptoms": ["körlük", "görme kaybı", "gözlerin görmemesi"],
     "causes": ["yalanci_sahitlik", "zulum_insan"],
     "remedy": "Gözleri kör eden yalancı şahitlik, sen ne büyük bir günahsın."},

    {"name": "Fıtık ve Apandisit", "category": "Cerrahi",
     "symptoms": ["fıtık", "apandisit", "apandis patlaması", "kasık fıtığı"],
     "causes": ["hak_haram"],
     "remedy": "Fıtıkları yırtan, apandisi patlatan hak haramlığı sen ne büyük bir zulümsün."},

    # === CİĞER VE SOLUNUM BEDDUASI ===

    {"name": "Astım ve KOAH (Ciğer Bedduası)", "category": "Solunum",
     "symptoms": ["astım", "KOAH", "nefes darlığı", "solunum güçlüğü"],
     "causes": ["beddua", "ciger_bedduasi"],
     "remedy": "Bizim ve soyumuzdan ciğere okuduğumuz bedduanın kendimizde veya çocuklarımızda astım ve KOAH hastalığı yapabilir."},

    # === DEPREMDEN KURTULMA ADAĞI ===

    {"name": "Ani Sıçrama Hastalığı", "category": "Nörolojik",
     "symptoms": ["ani sıçrama", "irkiltme", "aniden sıçrama"],
     "causes": ["adak_eylem"],
     "remedy": "Adanıp yerine getirilmeyen depremden kurtulma üzerine adak ve sözler, ani sıçrama hastalığı yapabilir."},

    # === KINAMA SONUÇLARI ===

    {"name": "Evde Kalan Kız / Evlenememe (Kınama)", "category": "Sosyal",
     "symptoms": ["evlenememe", "evde kalma", "evlilik olmama"],
     "causes": ["kinama"],
     "remedy": "Evde kalan kızları kınamanın çocuklarının evlenememesine sebep olduğunu bil."},

    # === SAĞLIK ADAĞI ===

    {"name": "Sürekli Hastalık ve Güçsüzlük", "category": "Genel",
     "symptoms": ["sürekli hasta olma", "güç düşmesi", "kuvvetten düşme", "halsizlik"],
     "causes": ["adak_eylem"],
     "remedy": "Sürekli hasta olmanın, güç ve kuvvetten düşmenin sebebi senin sağlık üzerine adayıp yerine getirmediğin adak olduğunu bil."},

    # === SEDEF VE HAYVAN YAKMA ZULMÜ ===

    {"name": "Sedef (Köpek/Eşek Yakma Zulmü)", "category": "Dermatolojik",
     "symptoms": ["sedef hastalığı", "psoriasis", "deri kabuklanması"],
     "causes": ["kopek_zulum", "esek_zulum", "zulum_hayvan"],
     "remedy": "Sedef, köpek ve eşek yakma kesme öldürme diri diri gömme zulmü ile gelir."},

    # === AĞAÇ DİKME ADAĞI ===

    {"name": "Ciltte Kuruluk ve Susuzluk (Ağaç Adağı)", "category": "Dermatolojik",
     "symptoms": ["cilt kuruluğu", "susuzluk", "kuru cilt"],
     "causes": ["adak_eylem"],
     "remedy": "Ciltte kuruluk, susuzluk yapan adak ağaç dikme adağıdır."},

    # === ALTIN TAKMA ADAĞI ===

    {"name": "Sarılık / Göz Sarılığı (Altın Takma Sözü)", "category": "Pediatrik/Hepatik",
     "symptoms": ["sarılık", "göz sarılığı", "yenidoğan sarılığı"],
     "causes": ["adak_eylem"],
     "remedy": "'Bir çocuğun doğduğunu veya bir şey olduğunu görürsem altın takacağım' diyerek altın takma sözü vermekten sarılık olur."},

    # === ŞİRK - EL ALİM ESMASI ===

    {"name": "Şirk (El-Âlim Esması)", "category": "Manevi",
     "symptoms": ["şirk", "manevi ağırlık"],
     "causes": ["sirk"],
     "remedy": "Kişi 'Benim hocam her şeyi bilir.' der ise El-Âlim esmasından şirke düşer."},

    # === DİŞ ÇÜRÜMESI RUHSATLARI ===

    {"name": "Diş Çürümesi", "category": "Dental",
     "symptoms": ["diş çürümesi", "diş problemleri", "diş bozulması"],
     "causes": ["zulum_insan", "haram_kazanc", "kinama", "adak_eti", "zulum_anne_baba", "beddua"],
     "remedy": "Dişleri çürütme ruhsatları: İnsanların dişlerine vurarak ve dişlerini kırarak zulüm etme, haram olan şeyleri yemek, dişi çürüyenleri kınama, adak etini yemek, anne babayı ısırmak, diş ve kemiğe okunan lanet ve beddualar."},

    # === VAMPİR SENDROMU ===

    {"name": "Vampir Sendromu", "category": "Dermatolojik/Nadir",
     "symptoms": ["güneş hassasiyeti", "güneşten kaçma", "fotosensitivite"],
     "causes": ["beddua", "zulum_insan"],
     "remedy": "Güneşe lanet, güneşle insanlara eziyet edilerek yapılan işkenceler ve o zulme uğrayanların yaptıkları beddualar vampir sendromuna sebep olabilir."},

    # === KALSİYUM EKSİKLİĞİ ===

    {"name": "Kalsiyum Eksikliği", "category": "Metabolik/Kemik",
     "symptoms": ["kalsiyum eksikliği", "kemik zayıflığı", "osteoporoz"],
     "causes": ["beddua", "adak_eylem", "adak_hayvan", "zulum_hayvan"],
     "remedy": "Kalsiyum eksikliğinin sebepleri: Süt ve süt ürünlerine lanet, küfür. Süt ve süt ürünlerini dağıtma adakları. Zulm edilen, taciz edilen hayvanın ve adak hayvanının sütünü içme. Zulüm enerjisi. İliğe, kemiğe okunan lanet ve beddualar."},

    # === DEJAVU TUZAĞI ===

    {"name": "Dejavu Tuzağı", "category": "Psikolojik/Manevi",
     "symptoms": ["dejavu", "daha önce yaşamış hissi", "tekrar hissi"],
     "causes": ["zekat"],
     "remedy": "Dejavu tuzağını genelde zekâtçı şeytan kurar."},

    # === FAİZLİ KREDİ İLE YUVA KURMA ===

    {"name": "Yuva Yıkılması (Faizli Kredi)", "category": "Aile/Mali",
     "symptoms": ["yuva yıkılması", "evlilik bozulması", "boşanma", "maddi telef"],
     "causes": ["faiz"],
     "remedy": "Evlenmek isteyen bir kişi bankaya gitti ve kredi çekti. Bu kredi ile düğününü yaptı, evini kurdu. Böylelikle şeytanın yuva yıkma tuzağına düştü. Faiz o yuvayı yıkar maddi telef yapar."},

    # === MİDE ÜLSERİ VE KANSERİ ===

    {"name": "Mide Ülseri ve Mide Kanseri", "category": "Onkolojik/Sindirim",
     "symptoms": ["mide ülseri", "mide kanseri", "mide yanması"],
     "causes": ["zulum_insan", "adak_eti", "zekat"],
     "remedy": "Mide ülserinin ve kanserinin üç ana maddesi: Karından bıçaklama, yenmiş adakların çokluğu, zekâtsızlık."},

    # === ERKEN BOŞALMA ===

    {"name": "Erken Boşalma", "category": "Cinsel/Ürolojik",
     "symptoms": ["erken boşalma", "prematür ejakülasyon"],
     "causes": ["adak_eylem", "beddua"],
     "remedy": "Erken boşalma sebepleri: Adaklar sebep olabilir, adak tespiti yaptırılmalı. Kişinin organına aldığı beddualardan olur."},

    # === EVLATLARDAN AYRI YAŞAMA ===

    {"name": "Evlatlardan Ayrı Yaşama / Ayrılık Ruhsatı", "category": "Aile/Sosyal",
     "symptoms": ["çocuklardan ayrı kalma", "evlatları görememe", "aile ayrılığı"],
     "causes": ["zulum_anne_baba", "narsist_zulum"],
     "remedy": "Bir kişi evlatlarından ayrı yaşamak zorunda kalıyorsa soydan anneyi, babayı evlatlarından koparma zulmü, ayrılık ruhsatı vardır üzerinde."},

    # === VİTİLİGO ===

    {"name": "Vitiligo (Detaylı)", "category": "Dermatolojik",
     "symptoms": ["vitiligo", "deri renk kaybı", "beyaz lekeler"],
     "causes": ["zulum_insan", "aniz_yakma"],
     "remedy": "Vitiligo'nun günah sebepleri: Bir kişinin evini, tarlasını, hayvanlarını ve bir insanı yakma ile olabilmekte."},

    # === TRAFİK KAZASI ===

    {"name": "Trafik Kazası", "category": "Kaza/Manevi",
     "symptoms": ["trafik kazası", "araba kazası", "kaza yapma"],
     "causes": ["adak_eylem", "beddua"],
     "remedy": "Bir insan neden trafik kazası geçirir? Kaza bela gelmesin diye adanan adak veya araba üzerine adanıp kesilmeyen adaklar ve 'arabaların altında kalasın' bedduası, trafik kazası geçirmeye sebep olabilir."},

    # === TRAFİKTE BEKLEME ===

    {"name": "Trafikte Bekletilme / Kilitlenme", "category": "Sosyal/Manevi",
     "symptoms": ["trafikte bekleme", "yolda tıkanma", "işlerin gecikmesi"],
     "causes": ["zulum_insan", "hak_haram"],
     "remedy": "Kilitlenmiş bir trafik ve bekleme sıkıntısı neden gelir? Soydan yol kesme, insanları bekletme, eşkıyalık, insanların işlerini bozma ve beklemelerine sebep olma varsa trafikte beklemelerine sebep olur."},

    # === YERSİZ YURTSUZLUK ===

    {"name": "Bir Yerde Barınamama / Sürekli Taşınma", "category": "Sosyal/Manevi",
     "symptoms": ["bir yerde duramama", "sürekli taşınma", "barınamama", "yersiz yurtsuzluk"],
     "causes": ["zulum_insan", "beddua"],
     "remedy": "Bir aile bir yerde barınamıyorsa, sürekli taşınıyorsa bunun sebebi: Soydan insanları yerinden yurdundan etme olabilir. 'Yersiz yurtsuz kalasınız' bedduaları bu zulümle alınmış olabilir."},

    # === GÖĞÜS SARKMASI VE GÖĞÜS KANSERİ ===

    {"name": "Göğüs Sarkması", "category": "Jinekolojik/Fiziksel",
     "symptoms": ["göğüs sarkması", "meme sarkması", "göğüslerde sarkma"],
     "causes": ["zulum_insan", "insan_oldurme"],
     "remedy": "Bir kadında göğüs sarkması varsa bu göğüsleri keserek yapılan zulüm ve göğüs uçlarını kopararak, göğsü tamamen kökünden keserek yapılan zulüm ve öldürmeyle gelen bir ruhsattır."},

    {"name": "Göğüs Kanserinde Kitle Büyüklüğü", "category": "Onkolojik",
     "symptoms": ["göğüs kitlesi", "meme kitlesi", "göğüste kitle"],
     "causes": ["zekat", "zulum_insan"],
     "remedy": "Göğüs kanserindeki kitle büyüklüğü, kişideki zekât eksikliğinin miktarını gösterebilir (23 mm: 23 bin TL gibi). Bu kitleler ayrıca göğse şiş batırma ve hançerleme zulmüne de işaret olabilir."},

    # === EREKSİYON SORUNU ===

    {"name": "Ereksiyon Sorunu", "category": "Cinsel/Ürolojik",
     "symptoms": ["ereksiyon sorunu", "sertleşme problemi", "cinsel işlev bozukluğu"],
     "causes": ["beddua", "zina_ensest"],
     "remedy": "Ereksiyon sorununa sebep olan ana ruhsat taciz ile alınan beddualardır."},

    # === BEYİN DAMARI SIKIŞMASI ===

    {"name": "Beyin Damarı Sıkışması", "category": "Nörolojik/Kardiyovasküler",
     "symptoms": ["beyin damarı sıkışması", "serebral vazokonstriksiyon", "beyin kan akışı problemi"],
     "causes": ["zekat", "sirk", "zulum_anne_baba", "beddua"],
     "remedy": "Beyin damarı sıkışması zekât, şirk ve anne-baba bedduasıyla olmaktadır."},

    # === HAYAT KADINI OLMA İSTEĞİ ===

    {"name": "Hayat Kadını Olma İsteği", "category": "Psikolojik/Cinsel",
     "symptoms": ["fuhşa eğilim", "hayat kadını olma isteği", "fuhuş düşüncesi"],
     "causes": ["zina_ensest", "beddua", "kinama"],
     "remedy": "Hayat kadını olma isteğinin nedenleri: Soydan insanları fuhşa zorlama, hayat kadınlığı yaptırmaya zorlama, fuhşa zorlanan kadınlardan alınan beddua, kınama, soydan ensest."},

    # === YÜKSEK ŞEKER HASTALIĞI ===

    {"name": "Yüksek Şeker Hastalığı (Detaylı)", "category": "Endokrin",
     "symptoms": ["yüksek şeker", "diyabet", "kan şekeri yüksekliği"],
     "causes": ["adak_eylem", "adak_eti", "zekat"],
     "remedy": "En yüksek şeker hastalığında: Şeker, helva, tatlı dağıtma adakları, su açma, çeşme açma adakları var mı adak tespiti ve yenilen adak tespiti yapılır. Anne ve babasının vermediği zekâtlar, soy zekâtı, kendi zekâtı sebep olabilir."},

    # === TACİZE UĞRAMA SEBEPLERİ ===

    {"name": "Tacize Uğrama Ruhsatı", "category": "Sosyal/Manevi",
     "symptoms": ["tacize uğrama", "istismara maruz kalma"],
     "causes": ["yetim_zulum", "hamile_zulum", "zina_ensest", "beddua"],
     "remedy": "Bir kişinin tacize uğramasına sebep olabilecek etkenler: Soydan yetimlere, çocuklara ve hamile kadınlara taciz vardır. Bu tacizle alınan bir beddua vardır. Bu kişinin yapması gereken soy zinası, cinsel sapkınlık ve ensest günahlarına tövbe."},

    # === TARLA ZEKÂTI ETKİLERİ ===

    {"name": "Böbrek Taşı (Tarla Zekâtı)", "category": "Üriner",
     "symptoms": ["böbrek taşı", "idrar yolu taşı", "böbrekte kum"],
     "causes": ["zekat"],
     "remedy": "Tarla zekâtının vücuttaki etkileri: Tarla, taş ve toprak olduğu için genelde böbreklerde taş ve toprak sıkıntısına sebep olabilmektedir."},

    {"name": "Nasır ve Topuk Dikeni (Tarla Zekâtı)", "category": "Ortopedik",
     "symptoms": ["nasır", "topuk dikeni", "ayak nasırı"],
     "causes": ["zekat"],
     "remedy": "Tarla zekâtı ayaklarda nasır ve topuk dikenine sebep olabilmektedir."},

    # === PARA VE ALTIN ZEKÂTI ETKİLERİ ===

    {"name": "Kalp ve Damar Hastalıkları (Para/Altın Zekâtı)", "category": "Kardiyovasküler",
     "symptoms": ["damar hastalığı", "kalp hastalığı", "kalp krizi", "beyin kanaması"],
     "causes": ["zekat"],
     "remedy": "Para ve altın zekâtının vücuttaki etkileri: Damar ve kalp hastalıkları yapabilir, kalp krizi yapabilir, beyin kanaması yapabilmektedir."},

    # === EVLENEMEME (ENSEST VE AYRILIK) ===

    {"name": "Evlenememe (Ensest ve Ayrılık Ruhsatı)", "category": "Sosyal",
     "symptoms": ["evlenememe", "evlilik kapanması", "eş bulamama"],
     "causes": ["zina_ensest", "narsist_zulum"],
     "remedy": "Evlenemeyen insanlarda ensest ve ayrılık ruhsatı olup olmadığına bakılmalı, seans alıp tespit yaptırılmalı."},

    # === PROGERYA (DETAYLİ) ===

    {"name": "Progerya (Anne-Baba Gömme Zulmü)", "category": "Genetik",
     "symptoms": ["progerya", "erken yaşlanma", "çocukta yaşlılık"],
     "causes": ["zulum_anne_baba", "insan_oldurme"],
     "remedy": "Anne-babayı diri diri toprağa gömme zulmü progerya ruhsatıdır. Genç yaşta yaşlanıp ölen çocukların ruhsatıdır."},

    # === DİZ RUHSATLARI ===

    {"name": "Diz Ağrısı ve Sızlaması (Detaylı)", "category": "Ortopedik",
     "symptoms": ["diz ağrısı", "diz sızlaması", "diz problemi"],
     "causes": ["zulum_anne_baba", "beddua", "adak_eylem", "zulum_insan"],
     "remedy": "Dizlere yerleşen ruhsatlar: Yaşlı anne-babanın ayaklarına vurma, 'Elin ayağın tutmaz olsun dizin sızlasın' bedduası, kız kaçırma, savaştan kaçma, türbe ziyareti adakları. Bu üç ruhsat dizlere yerleşen ruhsatlardandır."},

    # === KENDİ YÜZÜNÜ TOKATLAMA ===

    {"name": "Kendi Yüzünü Tokatlama", "category": "Psikiyatrik/Davranışsal",
     "symptoms": ["kendi yüzünü tokatlama", "kendine vurma", "öz şiddet"],
     "causes": ["zulum_anne_baba", "beddua"],
     "remedy": "Bir kişi neden kendi yüzünü tokatlar? Soydan anne-babaya tokat atma ve 'Aynısı evlatlarınızdan çıksın, evlatlarınızdan çekin' bedduasını aldıysa o çocuklar kendini tokatlar."},

    # === SÜREKLİ AĞLAYAN ÇOCUK ===

    {"name": "Sürekli Ağlayan Çocuk", "category": "Pediatrik",
     "symptoms": ["sürekli ağlama", "çocuk ağlaması", "durdurulamayan ağlama"],
     "causes": ["hak_haram", "adak_eylem"],
     "remedy": "Sürekli ağlayan çocukta anne ve babanın yaptığı hak haramlığına ve adağı olup olmadığına bakılır."},

    # === ÇOCUK OLMAMASI (EN AĞIR RUHSAT) ===

    {"name": "Çocuk Olmaması (En Ağır Ruhsat)", "category": "Üreme",
     "symptoms": ["çocuk olmaması", "kısırlık", "çocuk yapamama"],
     "causes": ["zina_ensest", "cocuk_oldurme", "cocuk_aldirma", "adak_eylem", "beddua"],
     "remedy": "Çocuk olmamasına sebep olan en ağır ruhsatlar: Kendi geliniyle ya da kendi çocuklarıyla yaptıkları ensest ilişkinin sonucu aldığı beddua ve o çocuğu öldürmesi. Çocuk üzerine adanıp yerine getirilmeyen adakların üst üste yığılması. Soydan çok fazla çocuk öldürülmesi, kürtaj yapılması."},

    # === YUVAM HUZURSUZ EDEN EVLAT ===

    {"name": "Yuvayı Huzursuz Eden / Rezil Eden Evlat", "category": "Aile/Sosyal",
     "symptoms": ["huzursuz evlat", "rezil eden evlat", "problemli çocuk"],
     "causes": ["adak_eylem", "zulum_insan", "beddua"],
     "remedy": "Bir yuvayı huzursuz eden, rezil eden evlatta hangi ruhsat daha çok aktiftir? 'Yuvam ve çocuklarım olursa' diye adanan bir adak vardır. Soylarından insanlar toplum içinde rezil ederek çarmıha germe ve soyarak, döverek aldıkları beddualardan olabilmektedir."},

    # === HAFIZA DONMASI ===

    {"name": "Hafıza Donması / Nerede Olduğunu Unutma", "category": "Nörolojik/Psikiyatrik",
     "symptoms": ["hafıza donması", "nerede olduğunu unutma", "hafıza silinmesi", "ani unutkanlık"],
     "causes": ["zulum_insan", "cocuk_oldurme"],
     "remedy": "Hafızayı donduran, kişiyi nerede olduğunu bilmeyecek hale getiren ruhsat: Kişi nerede olduğunu bir anda unutuyorsa ve hafızası siliniyorsa o kişide soydan çocukları kaçırıp geçmişini unutturma ve soyuna karşı o çocukları asker, savaşçı yapıp savaştırma yani soyunun geçmişini unutturma (hafızasını silme) zulmü vardır."},

    # === BOYUN FITIĞI VE SAÇ DÖKÜLMESİ (YETİM ZULMÜ) ===

    {"name": "Boyun Fıtığı, Boyun Düzleşmesi, Saç Dökülmesi (Yetim Zulmü)", "category": "Ortopedik/Dermatolojik",
     "symptoms": ["boyun fıtığı", "boyun düzleşmesi", "saç dökülmesi"],
     "causes": ["yetim_zulum"],
     "remedy": "Boyun fıtığına, boyun düzleşmesine ve saç dökülmesine sebep olan zulüm çeşidi yetime zulümdür."},

    # === FAKİRLİK SEBEPLERİ ===

    {"name": "Fakirlik", "category": "Mali/Manevi",
     "symptoms": ["fakirlik", "maddi sıkıntı", "para darlığı", "yoksulluk"],
     "causes": ["zekat", "faiz", "adak_eylem", "miras_laneti", "kul_hakki"],
     "remedy": "Fakirliğin sebepleri: Zekâtçı (soy zekâtı, kendi zekâtı), faizci (kredi kartı, ev ve araba faizi), başarı üzerine adak (sadaka, para dağıtma), para üzerine lanet (miras laneti), borç aldığı kişinin borcunu ödemeyip onlardan alınan ah, soyun aldığı ahlar. Bu maddeler fakirliğe sebep olur."},

    # === SINAVDA BAŞARISIZLIK ===

    {"name": "Sınavda Başarısızlık (Dışarıda Başarılı)", "category": "Eğitim/Manevi",
     "symptoms": ["sınav başarısızlığı", "dışarıda başarılı sınavda başarısız", "sınav korkusu"],
     "causes": ["beddua", "adak_eylem"],
     "remedy": "Bir kişinin dışarıda başarılı olup sınavda başarısız olmasının sebebi: Sınava, sınav yapana okuduğu lanet ve beddualar; üniversiteye, okula ve sınav üzerine yaptığı adaklar olabilmektedir."},

    # === BEYİN TÜMÖRÜ (İKİ ANA RUHSAT) ===

    {"name": "Beyin Tümörü (İki Ana Ruhsat)", "category": "Onkolojik/Nörolojik",
     "symptoms": ["beyin tümörü", "kafa tümörü", "beyinde kitle"],
     "causes": ["zulum_insan", "zekat"],
     "remedy": "Beyin tümörünün iki ana ruhsatı: Beyne, kafanın olduğu yere demirle sopayla vurmak ve zekâtçıdır."},

    # === BOĞAZDA ŞİŞLİK, ÖDEM, KİTLE ===

    {"name": "Boğazda Şişlik, Ödem ve Kitle", "category": "KBB/Endokrin",
     "symptoms": ["boğaz şişliği", "boğaz ödemi", "boğazda kitle", "tiroid şişliği"],
     "causes": ["miras_laneti", "zekat", "beddua"],
     "remedy": "Boğazda şişlik, ödem ve kitle neden olur? Miras laneti ('boğazın şişsin' bedduası), zekâtsızlık boğazdaki şişliğe sebep olan ruhsatlardandır."},

    # === MİRAS LANETİ DETAYLI BELİRTİLERİ ===

    {"name": "Miras Laneti Belirtileri (Kapsamlı)", "category": "Çoklu/Manevi",
     "symptoms": ["kalp çarpıntısı", "panik atak", "guatr", "topuk dikeni", "ayaklarda nasır", "kabızlık", "parasal sıkıntı"],
     "causes": ["miras_laneti"],
     "remedy": "Kalp çarpıntısı, panik atak, guatr rahatsızlığı (zehir zıkkım olsun sözü), topuk dikeni, ayaklarda nasır, kabızlık yapan ruhsattır. Parasal sıkıntıya sebep olabilir. Bu özellikleri taşıyan ruhsat miras lanetidir."},

    # === ANKSİYETE ===

    {"name": "Anksiyete Hastalığı", "category": "Psikiyatrik",
     "symptoms": ["anksiyete", "kaygı bozukluğu", "endişe", "gerginlik"],
     "causes": ["miras_laneti", "beddua", "hak_haram"],
     "remedy": "Anksiyete hastalığının ruhsatı: Soydan veya akrabaların kendi aralarında yeme, içme ve mal miras üzerine okudukları ve aldıkları bedduaların ve yaptıkları hak haramlıkların sonucu olarak gelen miras laneti ruhsatı, anksiyete hastalığının sebebidir."},

    # === MENİSKÜS ===

    {"name": "Menisküs", "category": "Ortopedik",
     "symptoms": ["menisküs", "diz menisküsü", "menisküs yırtığı"],
     "causes": ["zulum_insan", "hainlik"],
     "remedy": "Savaştan kaçma ve hainlik var ise menisküse sebep olabilir."},

    # === KAMBURLAŞMA ===

    {"name": "Kamburlaşma", "category": "Ortopedik",
     "symptoms": ["kamburluk", "kamburlaşma", "sırt kamburu"],
     "causes": ["zulum_anne_baba", "adak_hayvan"],
     "remedy": "Kişinin kamburlaşmasına sebebiyet veren ruhsatlar: Anne-baba zulmü ve deve adağı kamburlaşmaya sebebiyet verir."},

    # === KUYRUK SOKUMU RAHATSIZLIĞI ===

    {"name": "Kuyruk Sokumu Rahatsızlığı", "category": "Ortopedik",
     "symptoms": ["kuyruk sokumu ağrısı", "koksiks ağrısı", "kuyruk sokumu rahatsızlığı"],
     "causes": ["beddua"],
     "remedy": "'O evde oturamayasınız' bedduası kuyruk sokumu rahatsızlığına neden olur."},

    # === BİTMEYEN ŞEHVET ===

    {"name": "Bitmeyen Şehvet", "category": "Cinsel/Psikolojik",
     "symptoms": ["bitmeyen şehvet", "aşırı cinsel istek", "kontrol edilemeyen şehvet"],
     "causes": ["zina_ensest", "zekat", "adak_hayvan"],
     "remedy": "Bitmeyen şehvetin sebepleri: En başı ensest, zekât, erkeklerde erkek adaklar ve kadında dişi adaklar bitmeyen şehvete sebep olur."},

    # === KULAK ÇINLAMASI (DETAYLI) ===

    {"name": "Kulak Çınlaması (Detaylı Sebepler)", "category": "KBB",
     "symptoms": ["kulak çınlaması", "tinnitus", "kulakta ses"],
     "causes": ["kinama", "iftira", "sirk", "zulum_insan"],
     "remedy": "Kulağı çınlatan ruhsatlar: Gıybet, kınama, iftira dinleme, laf taşıyan insanları onaylama ve 'Şifalandırıyorum, mucizelendiriyorum' diyerek gizli şirke düşürme, şirk kelimelerini duyduğu zaman onu onaylama yaptığında ve soydan kulağa yapılan zulüm kulak çınlamasına sebep olmaktadır."},

    # === ÇOCUKLARIN EL VE YÜZÜNDE LEKE ===

    {"name": "Çocuklarda El ve Yüzde Leke", "category": "Dermatolojik/Pediatrik",
     "symptoms": ["çocuklarda el lekesi", "çocuklarda yüz lekesi", "cilt lekesi"],
     "causes": ["zulum_anne_baba"],
     "remedy": "Çocukların ellerinde yüzlerinde lekeye sebep olan ruhsat: Anne ve babaya tokat atma, çocukların ellerinde ve yüzünde leke olmasına sebep olabilir."},

    # === KAS ZAYIFLAMASI VE ERİMESİ ===

    {"name": "Kas Zayıflaması ve Erimesi", "category": "Nörolojik/Kas",
     "symptoms": ["kas zayıflaması", "kas erimesi", "kas güçsüzlüğü", "miyopati"],
     "causes": ["zulum_anne_baba", "insan_oldurme", "hasta_cocuk_zulum", "beddua"],
     "remedy": "Kasların zayıflaması, erimesi hangi günahlar sebebiyledir? Kişilerin anne babalarına soydan yapılan zulüm, öldürme, hasta anne babalarına yapılan zulüm ve hasta engelli çocuklara yapılan zulümlerden gelen mezarcının kaslardaki rolü çok yüksektir. Ayrıca tacizle alınan beddua, 'kasların erisin' bedduası da kasları eritmektedir."},

    # === KANIN DURMAMASI ===

    {"name": "Kanın Durmaması", "category": "Hematolojik",
     "symptoms": ["kanın durmaması", "kanama durmaması", "sürekli kanama"],
     "causes": ["zulum_insan", "beddua"],
     "remedy": "Bir kişinin kanı durmuyorsa soyunda nasıl bir zulümle alınan beddua vardır? Soyunda eşkiyalık ve kan akıtma zulmü yapılarak aldıkları 'kanınız durmasın' bedduası buna sebeptir."},

    # === EŞEĞE ZULÜM BELİRTİLERİ (DETAYLI) ===

    {"name": "Eşeğe Zulüm ve Taciz Belirtileri", "category": "Davranışsal/Dermatolojik",
     "symptoms": ["yüksek sesle konuşma", "çirkin bağırma", "sedef"],
     "causes": ["esek_zulum"],
     "remedy": "'Kişi, yüksek sesle konuşur; çirkin bir bağırma tarzı olur. Sedef ruhsatı olabilir' - Bu özellikler eşeğe zulüm ve taciz ruhsatının olduğuna işarettir."},

    # === POLEN ALERJİSİ (DETAYLI) ===

    {"name": "Polen Alerjisi (Anız Yakma)", "category": "Alerji",
     "symptoms": ["polen alerjisi", "bahar alerjisi", "saman nezlesi"],
     "causes": ["aniz_yakma", "zulum_hayvan"],
     "remedy": "Anız, tarla yakarak hayvanları ve arıları yakma polen alerjisine sebep olur."},

    # === SEDEF (DERİ BEDDUASI) ===

    {"name": "Sedef (Deri Bedduası)", "category": "Dermatolojik",
     "symptoms": ["sedef", "psoriasis", "deri kabuklanması"],
     "causes": ["deri_bedduasi", "beddua"],
     "remedy": "'Deriniz kurusun' bedduası sedef hastalığına sebep olabilir."},

    # === TIRNAK MANTARI ===

    {"name": "Tırnak Mantarı", "category": "Dermatolojik",
     "symptoms": ["tırnak mantarı", "ayak tırnak mantarı", "onikomikoz"],
     "causes": ["zulum_insan", "zulum_hayvan"],
     "remedy": "Tırnak mantarına sebep olan zulümler: Tırnakları kopararak yapılan zulüm, ayak tırnaklarını kırarak yapılan zulüm, at ve eşeklerin tırnaklarına yapılan zulümler tırnak mantarına sebep olabilir."},

    # === DİL FELCİ ===

    {"name": "Dil Felci", "category": "Nörolojik/Konuşma",
     "symptoms": ["dil felci", "konuşamama", "dil tutulması"],
     "causes": ["beddua", "iftira", "isyan", "sirk"],
     "remedy": "Dil felcine sebep olan durumlar: Kişi küfür sözleri sürekli söylüyorsa, çok yalan söylüyorsa, lanet ve beddua okuyorsa, masuma iftira atıyorsa, inkâr sözleri söylüyorsa dil felcine sebep olabilir."},

    # === GÖBEK DÜŞMESİ ===

    {"name": "Göbek Düşmesi", "category": "Genel/Jinekolojik",
     "symptoms": ["göbek düşmesi", "göbek kayması", "karın rahatsızlığı"],
     "causes": ["cocuk_aldirma", "hamile_zulum"],
     "remedy": "Göbek düşmesi hangi ruhsattan kaynaklı olur? Genellikle çocuğun düşürülmesiyle alakalıdır. Tekme vurarak hamile kadının çocuğunu düşürmeyle alakalı bir ruhsattır. Hamile kadına taciz ve çocuğunu düşürme olabilir."},

    # === SEBEPSİZ KUSMA ===

    {"name": "Sebepsiz Kusma", "category": "Sindirim",
     "symptoms": ["sebepsiz kusma", "açıklanamayan kusma", "bulantı kusma"],
     "causes": ["hamile_zulum", "beddua"],
     "remedy": "Sebepsiz kusmanın sebebi: Hamile kadına yapılan hakaret ve zulümlerin işaretidir."},

    # === ŞEKER HASTALIĞI (KUYU/ÇEŞME ADAĞI) ===

    {"name": "Şeker Hastalığı (Kuyu/Çeşme Adağı)", "category": "Endokrin",
     "symptoms": ["şeker hastalığı", "diyabet", "kan şekeri yüksekliği"],
     "causes": ["adak_eylem"],
     "remedy": "Şeker hastalığına kuyu açma, çeşme açma adakları da sebep olabilir."},

    # === ELLERİNİ ISIRAN ÇOCUK ===

    {"name": "Ellerini Isıran Çocuk", "category": "Pediatrik/Davranışsal",
     "symptoms": ["elini ısırma", "kendini ısırma", "çocukta ısırma davranışı"],
     "causes": ["zulum_anne_baba", "hak_haram", "beddua"],
     "remedy": "Ellerini ısıran çocuklarda hangi ruhsata bakılır? Anne ve babanın elini ısırma ya da başkasının malını gasp edip mal sahibinin bedduasını alma, 'Kendi başını yiyesin, kendi elini yiyesin, kendi etini yiyesin' gibi ruhsatlara bakılır."},

    # === ACI YETİMİ ===

    {"name": "Acı Yetimi (Ağrı Hissetmeme)", "category": "Nörolojik/Nadir",
     "symptoms": ["acı hissetmeme", "ağrı duyusuzluğu", "ellerini yeme", "dilini yeme"],
     "causes": ["adak_eti", "beddua", "hak_haram"],
     "remedy": "Bu kişiler ellerini yiyorlar veya kendi dilini yiyorlar ve maalesef acı hissetmiyorlar. Bu hastalık, adanmış bir hayvanı çalıp da yiyen kişilerde, hırsızlık yapıp malı çalınan kişi 'Zehir zıkkım olsun, kendi başını yesin, kendi elini dilini yesin' diye ettiği beddualarla olabilmektedir Allah u âlem."},

    # === AKDENİZ ANEMİSİ ===

    {"name": "Akdeniz Anemisi (Talasemi)", "category": "Hematolojik",
     "symptoms": ["akdeniz anemisi", "talasemi", "kansızlık", "yorgunluk"],
     "causes": ["beddua", "miras_laneti", "isyan", "zekat", "adak_eylem"],
     "remedy": "Bu hastalık, beddua, kahır, intizar, isyan, lânet (zehir zıkkım olsun sözü) ile ve verilmeyen zekatla olur Allah u âlem. Özellikle bu hastalıkla canı yanan alacaklının yada mirasta hakkı olan kişinin can yanıklığıyla 'hakkım haram, zehir, zıkkım olsun ben yiyemedim siz de yiyemeyesiniz' gibi sözleri sarfetmesiyle birde yerine getirilmemiş adak ve zekat birleşimiyle olabilmektedir. Zekât tespiti yapılır, kendinin veya soyunun zekâtı verilir."},

    # === ALİS HARİKALAR DİYARI (DETAYLI) ===

    {"name": "Alis Harikalar Diyarı Sendromu (Detaylı)", "category": "Nörolojik/Psikiyatrik",
     "symptoms": ["algı bozukluğu", "boyut sapması", "dev gibi evleri fare kadar görme", "karıncayı apartman kadar görme"],
     "causes": ["kufur_kainata", "isyan", "kinama"],
     "remedy": "Bu hastalar dev gibi evleri bir fare kadar görüyorlar. Bazen bir karıncayı, bir kuşu da koskocaman, bir apartman gibi görüyorlar. Bu hastalarda kâinata küfür etme, tabiata, evlere, yaratılan dünyaya, içindekilere küfür ve alay etmekten kaynaklı bu kişilerde bu hastalık oluyor. O kâinata küfredip alay edersen, o kâinatın sahibine karşı alay etmeye, yaratılmışı beğenmemeye gider ve bu isyanına karşılık kâinat da seninle alay eder gibi olur. Fareyi aslan, karıncayı dev sanıp kaçarsın."},

    # === ALZHEİMER (DETAYLI) ===

    {"name": "Alzheimer (Detaylı)", "category": "Nörolojik",
     "symptoms": ["alzheimer", "unutkanlık", "hafıza kaybı", "demans"],
     "causes": ["zekat", "adak_eylem", "sirk", "zulum_anne_baba", "kinama"],
     "remedy": "Verilmeyen unutkan insanları kınama, zekât ve adak birleşir. Böylece şirk devreye girer ve bu hastalığa neden olur Allah u âlem. Bu hastalıkta kişinin soydan zekat enerjisi yüksek olduğu gibi kendi verilmeyen zekatı da yüksek çıkabilmektedir. Bu öncelikle kafayı şirkçi ile ele geçirmektedir Allahuâlem. Adaklar da zamanı geçip yerine getirilmediğinde zamanla bu hastalık tamamen beyni örtmektedir Allahuâlem. Anne babayı terketme, onları unutma ahını almada sebep olabilmektedir. Önce zekatlar tamamlanır, adaklar tespit edilir ve kişi üzerinden tek tek ruhsatlar kaldırılmaya çalışılır."},

    # === ASTIM VE KOAH (DETAYLI) ===

    {"name": "Astım ve KOAH (Detaylı)", "category": "Solunum",
     "symptoms": ["astım", "KOAH", "nefes alamama", "boğulma", "solunum krizi"],
     "causes": ["isyan", "zekat", "beddua"],
     "remedy": "Bu kişiler nefes alamaz, boğulurlar ve kriz geçirirler. Adeta hayattan tat alamazlar. Bu kişiler için hayatta kalmak bir nefes ile hayattan kopmakta bir nefes iledir. Onlar bu iki arada kalmış gibidirler. Peki neden böyle olur? Çünkü o kişiler veya soyları; hayata, yaşamaya lânet okur ve isyan ederler. Allahu âlem, bu günahlarından dolayı bu hastalığı yapan, göğsüne yerleşen görevli bir şeytandır. O günahı temsilen Allah'tan izin alarak ordadır ve buna sebepte kişinin kendisidir. Ona bu hastalığın gelmesi, kendi hayata yaptığı isyanının hayattan kopma krizi ile aslında tevbeye davet sinyalidir. Bu ruhsatlar zekât enerjisi ile sistemli çalışmaktadır Allahuâlem."},

    # === BAĞIRSAK KANSERİ, BASUR VE BAĞIRSAK ===

    {"name": "Bağırsak Kanseri, Basur ve Bağırsak Hastalıkları (Detaylı)", "category": "Sindirim/Onkolojik",
     "symptoms": ["bağırsak kanseri", "basur", "hemoroid", "bağırsak rahatsızlığı"],
     "causes": ["faiz", "beddua", "miras_laneti", "haram_kazanc", "hak_haram"],
     "remedy": "Bağırsak ile ilgili rahatsızlıklar; faiz günahından, beddua, lânet, miras lânetinden, haksız kazançtan ve hak haramlığından olur. Midenin sol tarafında faizden gelen azılı bir şeytan, midenin sağ tarafında hak haramlığından gelen azılı bir şeytan bulunmaktadır. Bağırsak hastalıkları ve daha bir çok hastalıkta rol oynamaktadırlar. Faiz öyle bir beladır ki tatlı tatlı yemenin hayat boyu nasıl acısının çıkacağını gösterir insana. Tabi bunu hayatını ve vücudunu alt üst ederek yaşatır. Allah-û Alem."},

    # === BEYİN TÜMÖRÜ (HAYRAT MALI) ===

    {"name": "Beyin Tümörü (Hayrat Malı)", "category": "Onkolojik/Nörolojik",
     "symptoms": ["beyin tümörü", "kafa tümörü", "beyinde kitle"],
     "causes": ["hayrat_mali", "zulum_insan", "zekat"],
     "remedy": "Hayrat malı yeme, kafaya zulüm ve zekat beyin tümörüne sebep olur."},

    # === BİPOLAR BOZUKLUK (DETAYLI) ===

    {"name": "Bipolar Bozukluk (Detaylı)", "category": "Psikiyatrik",
     "symptoms": ["bipolar", "manik depresif", "ruh hali dalgalanması"],
     "causes": ["zekat", "adak_eylem", "zulum_anne_baba", "zulum_hayvan", "beddua"],
     "remedy": "Bu hastalık; verilmeyen zekât ve kişinin anne babasının bizzat kendi vermedikleri zekat ile olabilmekte, yerine getirilmeyen adak, anne babaya zulüm, dövme ve işkence etme, beddualarını alma ve hayvan zulümleri ile de olabilmekte Allah u âlem."},

    # === BÖBREK (DETAYLI) ===

    {"name": "Böbrek Hastalıkları (Detaylı)", "category": "Üriner",
     "symptoms": ["böbrek hastalığı", "böbrek yetmezliği", "böbrek problemi"],
     "causes": ["zekat", "beddua"],
     "remedy": "Kendi veya soyunun vermediği zekâttan gelen zekâtçı, mide ve böbreklere yerleşir. Zekât kefâreti verildiği an ölür. Kişi biiznillah düzelir. Kana edilen beddualar, suya edilen beddualarada tevbe edilmeli Allahuâlem."},

    # === BURUN TIKANIKLIĞI ===

    {"name": "Burun Tıkanıklığı", "category": "KBB",
     "symptoms": ["burun tıkanıklığı", "burun eti büyümesi", "nefes alamama"],
     "causes": ["beddua", "zulum_hayvan", "adak_hayvan"],
     "remedy": "Soydan edilen veya kendinin ettiği; 'Nefesin kesilsin, nefesin tıkansın, ağzın burnun tıkansın' gibi beddualar sebep olmaktadır. Bu enerji, burun içi etlerine, ciğere yerleşip kişinin nefes almasını engellemektedir. Hayvanların ve insanların burnuna vurarak yapılan zulümde etki etmektedir. Ve ayrıca büyük baş hayvan adaklarıda bunda rol oynar."},

    # === ÇIBAN YARALARI ===

    {"name": "Çıban Yaraları", "category": "Dermatolojik",
     "symptoms": ["çıban", "apse", "deri yaraları", "tekrarlayan çıbanlar"],
     "causes": ["zulum_insan", "zulum_anne_baba"],
     "remedy": "Bu kişi veya soyunun yaptığı zulümle alâkalı, karşıdaki kişinin vücudunda nerelere vurduysa veya silah sıktıysa, oralarda bu çıkar. Ve 'Sen bu bölgelere vurarak zulüm ettin' sinyalidir Allahuâlem. Veya kişi kendi anne babasına vurduysa, gene bu yaralara maruz kalabilir."},

    # === DALAK ŞİŞMESİ ===

    {"name": "Dalak Şişmesi", "category": "İç Hastalık",
     "symptoms": ["dalak şişmesi", "dalak büyümesi", "splenomegali"],
     "causes": ["beddua", "zulum_insan"],
     "remedy": "Kendi veya soydan okunan 'Dalağın şişsin, dalağın patlasın gibi!' bedduaları ile kendi veya soyunun yaptığı zulüm ile ah almadan gelen şeytan bunu yapabilmekte Allahuâlem."},

    # === DERİ KANSERİ VE DERİ İLE İLGİLİ ===

    {"name": "Deri Kanseri ve Deri Hastalıkları", "category": "Dermatolojik/Onkolojik",
     "symptoms": ["deri kanseri", "deri hastalığı", "cilt problemi"],
     "causes": ["adak_eti", "zekat", "kinama", "adak_eylem", "hayrat_mali"],
     "remedy": "Deri ile ilgili rahatsızlıklar; adak eti yemekle, verilmeyen zekâtla, kınama zulmüyle, çocuk giydirme ve çocuk sevindirme adaklarıyla olur. Tabi kanser varsa unutmuyoruz zekat yüksek olabilmektedir. Ayrıca hayrat derisi gasp edip yemede yapar Allah u âlem."},

    # === DİL FELCİ ===

    {"name": "Dil Felci", "category": "Nörolojik/Konuşma",
     "symptoms": ["dil felci", "konuşamama", "dil tutulması"],
     "causes": ["beddua", "iftira", "isyan"],
     "remedy": "Kişi küfür sözleri söyledi ise, çok yalan söylüyor ise, lânet, beddua okuyorsa, masuma iftira atıyorsa, inkar sözleri söylüyorsa, bu enerjiler dile yerleşir ve dil felcine sebep olur Allahuâlem. Veya soydan 'dilin tutulsun' gibi beddua edildiyse, dil felci olabilmektedir."},

    # === DİYABET - ŞEKER (DETAYLI) ===

    {"name": "Diyabet - Şeker Hastalığı (Detaylı)", "category": "Endokrin",
     "symptoms": ["şeker hastalığı", "diyabet", "yüksek kan şekeri"],
     "causes": ["zekat", "kinama", "soy_laneti", "beddua", "adak_eylem", "adak_eti"],
     "remedy": "Şeker hastalığı; verilmeyen zekâttan, kınamadan, lânet, beddua ve soy lânetinden (yani lânet, beddua okuyup bundan tevbe etmeden ölen yakınlarımızın tutan bedduası), 'Şeker bana haram olsun' sözü, şeker-çikolata-helva-tatlı dağıtma adakları ve bolca yenilmiş hayvan adaklarından olabilmektedir Allahuâlem."},

    # === DOWN SENDROMU (DETAYLI) ===

    {"name": "Down Sendromu (Detaylı)", "category": "Genetik",
     "symptoms": ["down sendromu", "genetik bozukluk", "gelişim geriliği"],
     "causes": ["zekat", "isyan", "adak_hayvan", "adak_eti", "haramzade", "iftira"],
     "remedy": "Bu hastalık, eksik zekâttan, Allah'a isyan ve iftiralardan, çok fazla küçükbaş veya büyük baş adaktan, adak eti yemekten, haramzadeden, 'Çocuğum olsun da nasıl olursa olsun' sözünden olur Allah-u âlem. Bu hastalardaki enerji çok yüksek olduğundan mıdır bilinmez kolay kolay seansa gelememekteler Allahuâlem. Rabbim seans almayı nasip eylesin."},

    # === EGZAMA (DETAYLI) ===

    {"name": "Egzama (Detaylı)", "category": "Dermatolojik",
     "symptoms": ["egzama", "cilt tahrişi", "kaşıntı"],
     "causes": ["adak_eti", "zekat", "zulum_insan"],
     "remedy": "Yenmiş adak ve zekât ve zulüm ile olabilmektedir."},

    # === EMMEYEN ÇOCUK ===

    {"name": "Emmeyen Çocuk", "category": "Pediatrik",
     "symptoms": ["çocuk emmeme", "emzirme sorunu", "bebek emmeme"],
     "causes": ["hak_haram", "beddua"],
     "remedy": "Annenin hak haram etmesi ve kendi veya başkasının çocuğuna beddua yapmakla çocuk emmeyi reddedebilir Allahu âlem. Ayrıca anne yediğine içtiğine dikkat etsin, haram katmasın çocuk helali arar. Anne baba olarak soy zürriyet ağacı tevbesi yapılır."},

    # === ENSAFALİT LATHARGİCA ===

    {"name": "Ensafalit Lathargica", "category": "Nörolojik/Nadir",
     "symptoms": ["sürekli uyuma", "aylarca uyuma", "uykusuzluk", "kontrolsüz yürüme"],
     "causes": ["adak_hayvan"],
     "remedy": "Bu hastalığı olan kişiler; sürekli sağa sola yürüyorlar. Aylarca uyuyorlar, bazen de sürekli uykusunda rahatsız oluyorlar, uyuyamıyorlar. Erkekte çok fazla dişi adaklar varsa (5 veya 6 tane), kadında da çok fazla erkek adaklar varsa (5 veya 6 tane), yerine getirilmeyen adaklarla gelen şeytanlar aldıkları bu ruhsatla kişilerdeki bu hastalığı yapabilmektedir Allah-u âlem. Adak tespitleri yapılıp yerine getirilir. Ancak bu kişilerde misal 6 tane koyun adağı varsa tek tek kesilip bitene kadar tespit etmeye devam edilir."},

    # === EPİLEPSİ (DETAYLI) ===

    {"name": "Epilepsi (Detaylı)", "category": "Nörolojik",
     "symptoms": ["epilepsi", "sara", "nöbet", "kasılma"],
     "causes": ["zekat", "insan_oldurme", "kinama", "beddua", "zulum_insan", "adak_eylem"],
     "remedy": "Kişinin eksik zekâtı varsa, soydan insan öldürme varsa, kınama varsa, lânet ve beddualar okudu veya aldıysa, ah aldıysa, zulüm ettiyse, özellikle Kur'an talebelerine alimlere zulmettiyse (kendi veya soyu olabilmekte), çocuğum düşmesse diye adak adandıysa yerine getirilmediyse olabilmektedir."},

    # === ERGENLİK SİVİLCELERİ ===

    {"name": "Ergenlik Sivilceleri", "category": "Dermatolojik",
     "symptoms": ["sivilce", "akne", "ergenlik sivilceleri"],
     "causes": ["adak_hayvan", "zekat", "kinama"],
     "remedy": "Erkekte koyun adağı, kadında ise koç adağı varsa, üzerinde zekât enerjisi varsa, sivilceli insanlarla alay edip kınama yapıldıysa, bu olabilmektedir Allah-u âlem."},

    # === EŞCİNSELLİĞE SEBEP OLAN GÜNAHLAR ===

    {"name": "Eşcinselliğe Sebep Olan Günahlar", "category": "Cinsel",
     "symptoms": ["eşcinsellik", "hemcinse ilgi", "cinsel yönelim bozukluğu"],
     "causes": ["zina_ensest", "adak_hayvan", "zekat", "beddua"],
     "remedy": "Soydan yapılan tecavüzler, adaklar (erkekte çok fazla dişi adak olursa dişi adaklar kadından hoşlandırmaz erkeğe yönlendirir. Kadında da tam tersi, erkek adaklar çoksa hemcinsine yönlendirir), verilmeyen zekât bizzat anne babasının veya kendinin zekatıysa olabilir önce zekatı halletmeli, lânet ve beddualar bu duruma neden olur Allah u âlem."},

    # === EVLENEMEYEN KİŞİLER (DETAYLI) ===

    {"name": "Evlenemeyen Kişiler (Detaylı)", "category": "Sosyal",
     "symptoms": ["evlenememe", "eş bulamama", "evlilik kapanması"],
     "causes": ["zina_ensest", "narsist_zulum", "adak_eylem", "iftira", "kinama", "isyan"],
     "remedy": "Zina, ensest, narsist lânet, adak. Bu dört şey varsa, bunlar kişiyi evlendirmemek için çabalar ya da karşıdaki erkekte aynı günahlardan şeytanlar varsa o erkeğe yönlendirir. İftira, kınama ve isyanlar da evlenmeye engel olabilecek unsurlardır Allah-u âlem."},

    # === FELÇ İNMESİ (DETAYLI) ===

    {"name": "Felç İnmesi (Detaylı)", "category": "Nörolojik",
     "symptoms": ["felç", "inme", "vücut tutmaması"],
     "causes": ["zulum_insan", "beddua", "adak_eylem", "sirk", "isyan", "zekat", "zulum_hayvan"],
     "remedy": "Başkalarına yapılan zulümden, beddua lânetlerden, adaktan, şirk ve isyandan ve verilmeyen çok fazla zekatdan ve ayrıca hayvana zulüm işkence ve hayvanı yakmaktan da olabilmekte Allah-u âlem."},

    # === GÖZ ALTI MORLUĞU ===

    {"name": "Göz Altı Morluğu", "category": "Oftalmolojik",
     "symptoms": ["göz altı morluğu", "morluk", "göz çevresi kararmış"],
     "causes": ["beddua", "zulum_insan", "zekat", "kul_hakki", "insan_oldurme"],
     "remedy": "Lânet okuyanların soylarının gözleri mor olur. Göze zulüm ve zekat da buna neden olur Allah u âlem. Soydan cinayetler, alınmış ahlar, kul hakları ve zulümler de sebep olmaktadır Allahuâlem. Detaylı tespit ile kişiye kefâretleri verdirilir."},

    # === GÖZ KANLANMASI ===

    {"name": "Göz Kanlanması", "category": "Oftalmolojik",
     "symptoms": ["göz kanlanması", "kırmızı göz", "gözde kan"],
     "causes": ["beddua", "adak_eylem"],
     "remedy": "Göze okunan beddualar, yerine getirilmeyen hatim adakları, yasin adakları ve normal hayvan adağı buna sebep olabilmektedir. Hatim adağı sözünden gelen şeytan, hatim gözle okunduğu için göze yerleşir. Bu enerjiler gözdeki sıkıntılara sebebiyet verebilir. Özellikle kişinin anne babasına beddua tevbesini yaptırmanızı tavsiye ediyorum."},

    # === İÇ ORGANLARIN YANMASI, KENDİLİĞİNDEN YANMA ===

    {"name": "İç Organların Yanması / Kendiliğinden Yanma", "category": "Nadir/Dahili",
     "symptoms": ["iç organların yanması", "bağırların yanması", "içten yanma hissi"],
     "causes": ["beddua", "isyan"],
     "remedy": "'İçin yansın, bağrın yansın' gibi beddualar, isyanla birleşince bu rahatsızlık olur Allah-u âlem."},

    # === KABIZLIK (DETAYLI) ===

    {"name": "Kabızlık (Detaylı)", "category": "Sindirim",
     "symptoms": ["kabızlık", "bağırsak tıkanıklığı", "dışkılama güçlüğü"],
     "causes": ["zekat", "faiz", "hak_haram", "beddua"],
     "remedy": "Zekât, faiz, mal veya miras üzerine hak haram etme, o malı haram etme buna sebep olabilmekte Allah-u âlem. Birde 'Bağırsağın dolansın, tıkansın, bağırsağın şişsin' gibi beddualar kabızlığa sebep olabilmektedir."},

    # === KALBİ DELİK DOĞAN ÇOCUKLAR ===

    {"name": "Kalbi Delik Doğan Çocuklar", "category": "Kardiyak/Pediatrik",
     "symptoms": ["kalp deliği", "doğuştan kalp hastalığı", "konjenital kalp defekti"],
     "causes": ["zulum_anne_baba", "beddua", "kinama", "zekat", "adak_eylem", "zulum_insan"],
     "remedy": "Çocuğun anne babası, onlarında anne babaları ve üst soya doğru bakıldığında kalp kırma varsa, 'Delinesin, kalbinden vurulasın, delik deşik olasın' gibi beddualar, Müslümanlara 'kâfirler, gâvurlar' demek, anne babanın çocuğa bedduaları 'Kalbin dursun, yaşamasın, ölsün' gibi ve çocuğu istememek, kendi soyundan birinin birini silâh ile kalbinden vurması, kalbi hasta başka çocukları kınama, zekat, adak bu hastalığın sebeplerindendir."},

    # === KALP RİTMİ BOZUKLUĞU ===

    {"name": "Kalp Ritmi Bozukluğu (Anne Baba İsyanı)", "category": "Kardiyak",
     "symptoms": ["kalp ritmi bozukluğu", "aritmi", "kalp atış düzensizliği"],
     "causes": ["zulum_anne_baba", "isyan", "kinama"],
     "remedy": "Kalp ritmi bozukluğu, anne-baba hukukunu çiğneyen veya isyan eden kişilerde olabilmekte. İsyan; kadere rızasızlık, şükürsüzlük, başına gelenlere itirazdır. Müslümanların Müslümanlığını eleştirmek de bunu yapar Allahuâlem. Bu o kişiye 'Senin kalbindeki iman neden bu haline mani olmuyor' sinyali olabilmekte."},

    # === KAN KANSERİ (DETAYLI) ===

    {"name": "Kan Kanseri (Detaylı)", "category": "Onkolojik/Hematolojik",
     "symptoms": ["kan kanseri", "lösemi", "lenfoma"],
     "causes": ["adak_eylem", "adak_eti", "zekat", "beddua", "zulum_insan"],
     "remedy": "Bu hastalık; adanıp yerine getirilmeyen adaktan olur. Adadığı hayvanın etinden yiyen insanlarda da olabilmektedir. Kişi kan akıtma sözünü yerine getirmemiştir ve şeytan kanı ele geçirmeye izin almıştır. Şeytan hem kanı hem de tüm hücreleri ele geçirir. Zekatın çok eksik verilmesi sebebiyle zekâtçı vücutta çok kuvvetli vaziyete gelmiştir. Bu şeytanlar beddua ve lânetlerle 'kanın kurusun, kanser olasın' vs. gibi sözlerden, günahlardan ruhsat almaktalar. Hastalık fabrikasının tek enerji merkezidir 'zekâtçı'dır. Yani zekâtı verilmeyen maldan yiyenlerin vücuduna yerleşen şeytan, zulümle kan akıtanın kanına nüfuz etmesine sebep olur, çok tehlikelidir. Zekat enerjisi bu hastalıkta çok yüksektir Allahuâlem."},

    # === KARACİĞER BÜYÜMESİ (DETAYLI) ===

    {"name": "Karaciğer Büyümesi (Detaylı)", "category": "İç Hastalık",
     "symptoms": ["karaciğer büyümesi", "hepatomegali", "ciğer şişmesi"],
     "causes": ["zekat", "beddua", "adak_eti"],
     "remedy": "Karaciğer büyümesini, verilmeyen zekât, beddualar ve lânetlerle gelen görevliler yapabilmektedir Allahuâlem. 'Ciğerin şişsin, ciğerin çıksın, ciğerin patlasın' gibi beddualar... Adak hayvanının ciğerini yemekte ciğerde rahatsızlık olabilmekte Allahuâlem. Adak tesbit edilmeli, kefâreti yerine getirilmeli."},

    # === KARACİĞER KANSERİ (DETAYLI) ===

    {"name": "Karaciğer Kanseri (Detaylı)", "category": "Onkolojik",
     "symptoms": ["karaciğer kanseri", "ciğer kanseri", "hepatoselüler karsinom"],
     "causes": ["zekat", "beddua", "adak_eti"],
     "remedy": "Bu kanser türü; verilmeyen zekâttan ve 'Ciğerin kurusun, ciğerin yansın, ciğerin batsın' gibi beddualardan olur Allahuâlem. Adak hayvanının ciğerini yemekte ciğerde rahatsızlık olabilmekte Allahuâlem. Adak tesbit edilmeli, kefâreti yerine getirilmeli."},

    # === KAZA BELÂ GEÇİREN ÇOCUKLAR ===

    {"name": "Kaza Belâ Geçiren Çocuklar", "category": "Pediatrik/Kaza",
     "symptoms": ["çocuk kazası", "çocukta bela", "sürekli kaza geçiren çocuk"],
     "causes": ["beddua", "adak_eti", "adak_eylem", "zekat"],
     "remedy": "Bu durum; beddualardan (elin ayağın kırılsın gibi), adak eti yemekten, yerine getirilmeyen adaktan ve verilmeyen zekâttan olur Allah u âlem."},

    # === KEKEMELİK (DETAYLI) ===

    {"name": "Kekemelik (Detaylı)", "category": "Konuşma",
     "symptoms": ["kekemelik", "konuşma takılması", "peltek konuşma"],
     "causes": ["zulum_insan", "beddua", "adak_hayvan"],
     "remedy": "Kekemelik; zulüm ile alınan ah ve beddualardan olabilmektedir Allah-u âlem. Misal 'Çenen batsın, çenen sussun, konuşamayasın' beddualarından olur. Nadiren de tavuk adakları yapar."},

    # === KELEBEK (DETAYLI) ===

    {"name": "Kelebek Hastalığı (Detaylı)", "category": "Dermatolojik",
     "symptoms": ["kelebek hastalığı", "lupus", "deride kırmızı yanıklar"],
     "causes": ["zulum_anne_baba", "zulum_insan", "beddua", "adak_eylem"],
     "remedy": "Kelebek hastalığı; deride kıpkırmızı yanıklar olur. Anne babaya zulüm edip dövme, onlardan ah, lânet ve beddua alma ile, soydan zulüm ile, insanları dövme, ah alma gibi günahlar ile bu hastalık kişinin kendisinde veya evlatlarında çıkabilmektedir Allah-u âlem. Ayrıca un, ekmek, bulgur dağıtma adakları bu hastalığa sebep olabilmektedir, yerine getirilmelidir İnşaallah."},

    # === KELLİK VE SAÇ DÖKÜLMESİ (DETAYLI) ===

    {"name": "Kellik ve Saç Dökülmesi (Detaylı)", "category": "Dermatolojik",
     "symptoms": ["kellik", "saç dökülmesi", "alopesi"],
     "causes": ["adak_eylem", "kinama", "beddua", "zulum_insan", "yetim_zulum", "zulum_anne_baba"],
     "remedy": "Kellik ve saç dökülmesi ile ilgili; yerine getirilmeyen adak, kel olan birine zulüm, kel biriyle dalga geçme, kınama, beddua ve lânetler 'kel kalasın, saçın dökülsün' deme ve saç baş yolarak zulmetme gibi günahların buna sebep olduğu söylenebilir Allah-u âlem. Saç yolma, yetimi dövme, anne babanın kafasına vurma da sebep olabilmektedir."},

    # === KEMİK ERİMESİ ===

    {"name": "Kemik Erimesi", "category": "Ortopedik",
     "symptoms": ["kemik erimesi", "osteoporoz", "kemik zayıflığı"],
     "causes": ["adak_eti", "zulum_insan", "beddua"],
     "remedy": "Kemik erimesi, kendi adadığı adağı yeme veya kemiklerini kaynatıp suyunu içme, soydan zulümler yapılarak ah alma, 'İliğin kemiğin kurusun' gibi beddualar buna sebep olabilmektedir Allahuâlem."},

    # === KOLERA (DETAYLI) ===

    {"name": "Kolera (Detaylı)", "category": "Enfeksiyon",
     "symptoms": ["kolera", "şiddetli ishal", "kusma"],
     "causes": ["zina_ensest", "soy_laneti", "haramzade", "faiz"],
     "remedy": "Kolera hastalığına; büyük zina yani evli iken yapılan zina, soy lâneti, haramzade ve faiz günahı sebep olabilmektedir. Allahuâlem."},

    # === KÖRLÜK VE GÖZ (DETAYLI) ===

    {"name": "Körlük ve Göz Hastalıkları (Detaylı)", "category": "Oftalmolojik",
     "symptoms": ["körlük", "görme kaybı", "göz hastalığı"],
     "causes": ["adak_eylem", "kinama", "zulum_insan", "beddua", "zekat", "zina_ensest"],
     "remedy": "Her türlü göz hastalıkları ve körlük; en başta Kur'an okuma ve hatim adaklarından, kör insanı kınama, gözü kör etme zulmü, 'Gözün batsın, gözün kör olsun, gözüne kara gele' gibi beddualardan ve lânetlerden, verilmeyen zekâttan ve göz zinasından olur Allah u âlem."},

    # === KRAMPLAR GİRMESİ ===

    {"name": "Kramplar Girmesi", "category": "Kas/Nörolojik",
     "symptoms": ["kramp", "kas krampı", "bacak krampı", "el krampı"],
     "causes": ["zulum_insan", "adak_eylem", "zekat", "beddua"],
     "remedy": "Kramplar girmesi; insan ve hayvanları el ve ayaklarından asarak zulüm. Adak enerjisi, verilmeyen veya eksik verilen zekât günahından, ayrıca zulüm edildi ise, o zulümle vurulan yerlerde kramplar olur. Enerji kişinin kendi vücudunda vurduğu o yerlere yerleşir. Ete, kemiğe, damara lânet ve beddua okumalar da sebep olur Allahuâlem."},

    # === KUDUZ ===

    {"name": "Kuduz", "category": "Enfeksiyon",
     "symptoms": ["kuduz", "kuduz hastalığı", "hayvan ısırığı sonrası"],
     "causes": ["zulum_hayvan"],
     "remedy": "Kuduz olma; soyda hayvana zulüm aşırı derecede varsa, vücutta bu ruhsat hazırdır. Hayvan ısırdığı anda kişiye kuduz hastalığı hemen bulaşır."},

    # === KULAK ÇINLAMASI - TİNNİTUS ===

    {"name": "Kulak Çınlaması - Tinnitus (Detaylı)", "category": "KBB",
     "symptoms": ["kulak çınlaması", "tinnitus", "kulakta uğultu"],
     "causes": ["beddua", "iftira", "zulum_insan"],
     "remedy": "Kulak çınlaması: 'kulağın çınlasın' bedduası. Gıybet, dedikodu dinleyip gidip iftira attıysa, başkalarının kulaklarına vurma veya kulakla ilgili başka türlü zulümlerde olur Allah-u âlem."},

    # === MOEBIUS SENDROMU ===

    {"name": "Moebius Sendromu", "category": "Nörolojik/Nadir",
     "symptoms": ["yüz felci", "gözleri kapatamama", "yüzü oynatamama"],
     "causes": ["beddua", "zulum_anne_baba", "yetim_zulum", "miras_laneti"],
     "remedy": "Mebius sendromunda; kişi yüzünü oynatamaz, sağa sola bakamaz, gözlerini kapatamaz. Bu, yüze okunan beddualarla, anne-babanın yüzüne vurma, yetimin yüzüne vurma, mirası üzerine kavga edip adam dövenlerde veya vuranlarda olabilmekte Allahuâlem."},

    # === MEME KANSERİ (DETAYLI) ===

    {"name": "Meme Kanseri (Detaylı)", "category": "Onkolojik",
     "symptoms": ["meme kanseri", "göğüs kanseri", "memede kitle"],
     "causes": ["hayrat_mali", "isyan", "soy_laneti", "zekat", "zulum_insan"],
     "remedy": "Bu hastalığa hayrat malı yeme, hayata isyan, soy lâneti, zekat enerjisi, göğüs bıçaklama neden olur Allahuâlem. 1. Allah (CC)'ın El-Hayy, El-Kayyum isimlerinden tevbe edilir. 2. Zekat kefâreti yapılır ve beddua kefâreti yapılır."},

    # === MİDE KANSERİ (DETAYLI) ===

    {"name": "Mide Kanseri (Detaylı)", "category": "Onkolojik",
     "symptoms": ["mide kanseri", "gastrik kanser", "midede kitle"],
     "causes": ["zekat", "zulum_insan", "beddua"],
     "remedy": "Soy zekatı, mide bıçaklama zulmü ve beddua mide kanserine sebep olur."},

    # === MİGREN (DETAYLI) ===

    {"name": "Migren (Detaylı)", "category": "Nörolojik",
     "symptoms": ["migren", "şiddetli baş ağrısı", "zonklayıcı ağrı"],
     "causes": ["sirk", "zulum_anne_baba", "zulum_hayvan"],
     "remedy": "Şirk, anne babaya sesle zulüm ve hayvan zulümleri sebep olabilmektedir."},

    # === NARSİST HASTALIĞI (DETAYLI) ===

    {"name": "Narsist Hastalığı (Detaylı)", "category": "Psikiyatrik",
     "symptoms": ["narsisizm", "manipülasyon", "empati yokluğu", "aşık edip terk etme"],
     "causes": ["kinama", "narsist_zulum", "kul_hakki", "insan_oldurme"],
     "remedy": "Bu hastalık olan kişiler, sevgili olduğu karşıdaki kişiyi kopyalar, ona müthiş bir kadın veya erkek rolü oynar, sonra o kişiyi kendine bağlar ve bir müddet sonra ondan uzaklaşır. Kişi çok kısa sürede alıştığı bu kimseden ayrılınca üzüntü yaşamaya başlar. Tabi o, narsist hastasındaki şeytan için seçilmiş bir kurbandır. Kendine bağlayıp ortadan kaybolur ve kısa bir süre geçtikten sonra tekrar hiçbir şey olmamış gibi sevdiği kimsenin yanına gelir. Onunla çok profesyonel bir oyuncu gibi oynar. İlk tanışmalarındaki müthiş insan modeli zamanla yok olmaya başlar ve şeytan gerçek yüzünü ortaya çıkartır. Karşıdakini bir tümör gibi yıpratarak öldürmeye başlar. Tutarsız hareketleri, tavırları ve gerçek kişiliği ortaya çıkar. Nefis ve hevasına çok düşkün biri ortaya çıkar. İlk zamanlardaki tevazulu, güler yüzlü ve sevgi dolu insan adeta kaybolur. Bu kişilerin üzerinde bulunan musallat, karşıdakini intihar seviyesine getirip hedefine ulaşmak derdindedir. Soydan gelen insanları kafirlikle çokça itham etme ve bir birine aşık iki kişiyi gaddarca ayırarak yada onlardan birini öldürüp diğerinin aşk acısıyla yanmasına ve beddua etmesine sebep olarak yapılan bir zulümden gelen bir enerji olabilmektedir Allahuâlem. İnsanları mahkum ederek yuvasından ayırma, yol kesip kadınları kaçırarak eşlerinden ayırma, çocukları kaçırarak yada öldürerek anne babadan ayırma zulümleri o habis ruhu getirmektedir Allahuâlem ve soylarından bu zulümler olan kişilerde narsist olabilmektedir."},

    # === OBEZİTE (DETAYLI) ===

    {"name": "Obezite (Detaylı)", "category": "Metabolik",
     "symptoms": ["obezite", "aşırı kilo", "şişmanlık"],
     "causes": ["harami_esme", "zekat", "hak_haram", "kinama", "beddua"],
     "remedy": "Obezite, harami eşmeden, verilmeyen zekatlardan, hak haramlığından, kınama ve beddualardan olabilmekte Allahuâlem."},

    # === OTİZM VE OTİSTİK ÇOCUKLAR (DETAYLI) ===

    {"name": "Otizm ve Otistik Çocuklar (Detaylı)", "category": "Nörogelişimsel",
     "symptoms": ["otizm", "otistik spektrum", "iletişim güçlüğü"],
     "causes": ["beddua", "zulum_insan", "faiz", "cocuk_aldirma", "zulum_hayvan", "kinama"],
     "remedy": "Beddua, lânet ve zulümler varsa, faiz yediler veya yedirdilerse, çocuk aldırma yapıldıysa bu rahatsızlık olabilir Allahuâlem. Hayvan zulümleri, hasta engelli ve zulüm de bu hastalıkta aktif rol oynar."},

    # === ÖDEM VE ŞİŞLİKLER (DETAYLI) ===

    {"name": "Ödem ve Şişlikler (Detaylı)", "category": "Genel",
     "symptoms": ["ödem", "şişlik", "su tutma"],
     "causes": ["beddua"],
     "remedy": "Ödem ve şişlik; suya lanet, 'şişesin' bedduası ile olmaktadır Allah-u âlem."},

    # === ÖFKE KRİZİ (DETAYLI) ===

    {"name": "Öfke Krizi (Detaylı)", "category": "Psikiyatrik",
     "symptoms": ["öfke krizi", "kontrolsüz öfke", "hiddet patlaması"],
     "causes": ["adak_hayvan", "zulum_anne_baba", "zekat", "haramzade"],
     "remedy": "Öfke krizi; büyükbaş adaktan, anne babaya kin ve öfkeden, bir çok küçükbaş adaktan, verilmeyen zekâttan ve haramzadeden gelir Allahuâlem."},

    # === ÖZÜRLÜ DOĞAN ÇOCUKLAR ===

    {"name": "Özürlü Doğan Çocuklar", "category": "Genetik/Pediatrik",
     "symptoms": ["doğuştan özür", "engelli doğum", "konjenital anomali"],
     "causes": ["beddua", "kinama", "zulum_insan", "soy_laneti", "adak_eylem", "zekat"],
     "remedy": "Anne-baba çocuğu istemezse, lânet ederse, kendinin ve soyunun özürlü insanları kınaması ile, özürlüye zulüm edilirse, soy lâneti ile, adaklar ve verilmeyen zekatlar dolayısıyla bu durum oluşur Allahuâlem."},

    # === PANİK ATAK (DETAYLI) ===

    {"name": "Panik Atak (Detaylı)", "category": "Psikiyatrik",
     "symptoms": ["panik atak", "anksiyete", "ölüm korkusu", "korku krizi"],
     "causes": ["adak_eylem", "yemin_bozma", "miras_laneti"],
     "remedy": "Buna sebep; korku üzerine verilen söz ve adaklardır. Misal; üniversite sınavı korkusuyla 'Allah'ım, eğer kazanırsam şunu yapacağım' der. Örneğin; fakir doyuracağım. Sınavı geçer ve doyurmazsa, şeytan sözünü yerine getirmemekten göğsüne yerleşir ve panik atak başlar. Veya 'Evladım sağlıklı doğsun, ölmesin, kurban keseceğim' der. O çocuk doğarsa ve ölmezse üç günü vardır. Bu üç gün içinde anne adağını yerine getirmezse çocuğa ve anneye görevli gelir. Ölüm korkusu yaşaması, anneye 'Sen ölüm üzerine bir şey adamıştın, yerine getir' sinyalidir. Bir örnek daha verecek olursak; kişi esrar içer. Birden korku basınca 'Allah'ım beni kurtar, ölmeyeyim, bir daha içmeyeceğim, namazlarımı kılacağım' der. Ama tekrar içer ya da namazını kılmaz. Şeytan ölüm korkusu vermek üzere ruhsat alır ve bedene yerleşir. Adak, yemin ve sözden uzak durmak gerekir. Adandıysa mutlaka yerine getirilmelidir. Yani; 'Ölmez de yaşarsa' diye adanan adaktan, korku üzerine söz verilir ve tutulmazsa (korkum geçsin şunu yapacağım gibi) ve miras lânetinden de bu hastalık olabilmektedir Allahuâlem."},

    # === PARKİNSON ===

    {"name": "Parkinson", "category": "Nörolojik",
     "symptoms": ["parkinson", "titreme", "hareket güçlüğü"],
     "causes": ["beddua", "zulum_anne_baba", "sirk"],
     "remedy": "Bu rahatsızlığa; 'Elin ayağın batsın' gibi beddualar ve anne baba bedduası ve şirk neden olmaktadır Allahuâlem. Anne babaya el kaldırma da hastalığın sebebi olabilmektedir."},

    # === PATLAYAN KAFA SENDROMU ===

    {"name": "Patlayan Kafa Sendromu", "category": "Nörolojik/Nadir",
     "symptoms": ["patlayan kafa sendromu", "kafada patlama hissi", "gürültü hissi"],
     "causes": ["adak_hayvan"],
     "remedy": "Patlayan kafa sendromu olan hastalarda; büyükbaş adak iki veya üç tane ise, bu hastalık olabilmektedir."},

    # === PROGERIA - ERKEN YAŞLANMA (DETAYLI) ===

    {"name": "Progeria - Erken Yaşlanma (Detaylı)", "category": "Genetik/Nadir",
     "symptoms": ["progeria", "erken yaşlanma", "çocukta yaşlılık belirtileri"],
     "causes": ["zulum_anne_baba", "kinama", "iftira", "insan_oldurme"],
     "remedy": "Erken yaşlanma hastalığı olan kişiler; çocuk yaşta yaşlanıyorlar, gücünü kaybediyor, derileri büzüşüyor ve on yaş civarlarında ölüyorlar. Allah-u âlem bu kişilerin soyu veya kendisi, yaşlı bir kimseyi çok fazla döverek zulmettilerse, o kişiyi aşağılayıp hor görüp kınadılarsa, kibirle zulüm ettiler ise, ölmüş birine çok ağır iftira atıldıysa, anne veya babasını canlı canlı toprağa mezara attılarsa, bu hastalık bu kişilerin evlâtlarında ortaya çıkabilmektedir. Ceza amelin cinsinden gelir. O kişilere yaptıklarının karşılığı olarak bu hastalık gelir ve bu bir ikazdır. Allah u alem."},

    # === PROSTAT (DETAYLI) ===

    {"name": "Prostat Kanseri (Detaylı)", "category": "Onkolojik/Ürolojik",
     "symptoms": ["prostat kanseri", "prostat büyümesi", "idrar güçlüğü"],
     "causes": ["zekat", "kinama", "adak_eylem"],
     "remedy": "Prostat kanseri; soy zekatı, kınama, su dağıtma ve çeşme yaptırma adaklarından olabilmektedir."},

    # === RAHİM EGZAMASI VE İLTİHABI ===

    {"name": "Rahim Egzaması ve İltihabı", "category": "Jinekolojik",
     "symptoms": ["rahim egzaması", "rahim iltihabı", "endometrit"],
     "causes": ["cocuk_aldirma", "isyan", "adak_eylem", "kinama"],
     "remedy": "Rahim egzaması ve rahim iltihabı. Gurre yani çocuğu bilerek düşürme, çocuğun doğumuna isyan, çocuğun olmasına ya da olmamasına isyan, çocuğun olması üzerine adak ve kınama."},

    # === RAHİM KANSERİ (DETAYLI) ===

    {"name": "Rahim Kanseri (Detaylı)", "category": "Onkolojik/Jinekolojik",
     "symptoms": ["rahim kanseri", "uterus kanseri", "endometrium kanseri"],
     "causes": ["zekat", "cocuk_aldirma"],
     "remedy": "Soy zekatı, çocuk kürtajı zulmü rahim kanserine sebep olur."},

    # === ROMATİZMA, BACAK BALDIR AĞRISI ===

    {"name": "Romatizma, Bacak Baldır Ağrısı", "category": "Romatolojik/Ortopedik",
     "symptoms": ["romatizma", "bacak ağrısı", "baldır ağrısı", "diz ağrısı"],
     "causes": ["isyan", "beddua", "zulum_insan", "adak_eylem", "zekat"],
     "remedy": "Yağmura intizar, 'Bir bitmedin' gibi beddualar, 'Dizin batsın' gibi, hayata, var olmaya isyan, dizle birine vurma veya birinin bacağına vurarak zulüm, su adağı, bacakla yapılan zulüm, 'dizlerin sızlasın' bedduası, deve adakları ve zekat enerjisi buna sebep olabilmekte."},

    # === SAÇKIRAN ===

    {"name": "Saçkıran", "category": "Dermatolojik",
     "symptoms": ["saçkıran", "alopecia areata", "bölgesel kellik"],
     "causes": ["beddua", "kinama", "zulum_anne_baba", "zulum_insan"],
     "remedy": "Saçkıran hastalığı; beddua, lânet okumaktan, kahırlanmaktan, kınamaktan, anne babaya ya da herhangi bir kimseye soyu veya kendisinin saç yolarak zulmetmesinden olabilmektedir. O kişiye 'Sen veya soyun bu şekilde saç yolarak birilerini dövdünüz veya ah, beddua aldınız' işaretidir Allahuâlem."},

    # === SARA (DETAYLI) ===

    {"name": "Sara Hastalığı (Detaylı)", "category": "Nörolojik",
     "symptoms": ["sara", "epilepsi", "nöbet", "kasılma"],
     "causes": ["zekat", "insan_oldurme", "zulum_hayvan"],
     "remedy": "Sara hastalığı, başta eksik zekât, hayvan ve insan zehirleyerek öldürme buna sebep olabilmekte."},

    # === SANDOF ===

    {"name": "Sandof Hastalığı", "category": "Genetik/Nadir",
     "symptoms": ["kemik eğrilmesi", "kas erimesi", "erken ölüm"],
     "causes": ["adak_eylem", "zekat", "zulum_anne_baba", "beddua"],
     "remedy": "Bu hastalıkta, çocukların kemikleri eğrilir, kasları eriyerek 4-5 yaşlarında vefat ederler. Çocuk üzerine 'Çocuğum olsun, kurban keseceğim' adakları çok fazla olur. Soyunda veya kendinde çok yüklü zekât borcu vardır. Anne baba zulmü ile alınan 'çocuklarınız ölsün' bedduası da olabilmekte bu hastalıkta."},

    # === SEDEF (DETAYLI) ===

    {"name": "Sedef Hastalığı (Adak Eti ve Eşek Zulmü)", "category": "Dermatolojik",
     "symptoms": ["sedef", "psoriasis", "deri kabuklanması"],
     "causes": ["adak_eti", "beddua", "esek_zulum"],
     "remedy": "Adak eti yeme, beddua ve eşek zulmünden olabilmekte."},

    # === SES KAYBI ===

    {"name": "Ses Kaybı", "category": "KBB/Nörolojik",
     "symptoms": ["ses kaybı", "afoni", "konuşamama"],
     "causes": ["isyan", "beddua"],
     "remedy": "Ses kaybı; aşırı isyan, sese beddua lanet okuma ve 'sesin kısılsın' bedduasından olabilmekte."},

    # === SİNÜZİT (DETAYLI) ===

    {"name": "Sinüzit (Detaylı)", "category": "KBB",
     "symptoms": ["sinüzit", "burun tıkanıklığı", "yüz ağrısı"],
     "causes": ["zulum_hayvan", "kedi_zulum"],
     "remedy": "Hayvanları suda boğma ve kedi zulmü sinüzite sebep olur."},

    # === TANSİYON ===

    {"name": "Tansiyon", "category": "Kardiyovasküler",
     "symptoms": ["yüksek tansiyon", "hipertansiyon", "düşük tansiyon"],
     "causes": ["zekat", "adak_eylem", "zulum_anne_baba", "sirk"],
     "remedy": "Verilmeyen zekât, adak, anne babaya isyan ve şirk bu hastalığa neden olur Allahuâlem."},

    # === UYUZ HASTALIĞI ===

    {"name": "Uyuz Hastalığı", "category": "Dermatolojik/Enfeksiyon",
     "symptoms": ["uyuz", "şiddetli kaşıntı", "deri döküntüsü"],
     "causes": ["adak_eylem", "kinama"],
     "remedy": "Uyuz hastalığı; fakir giydirme adağı, gariban yıkama adağı, adak eti yemek ile uyuz insanları kınama ile olabilmektedir Allahuâlem."},

    # === VAMPİR SENDROMU (DETAYLI) ===

    {"name": "Vampir Sendromu (Detaylı)", "category": "Dermatolojik/Nadir",
     "symptoms": ["vampir sendromu", "güneş alerjisi", "güneşten yanma", "fotosensitivite"],
     "causes": ["beddua", "isyan"],
     "remedy": "Vampir sendromu; güneşe çıkınca yanan, derileri kızaran ve yaralar oluşan anlamına gelir. Yani bu kişiler güneşe çıktığında derisinde, etinde, kemik içinde yaralar oluşuyor. Bu hastalık vampir filmlerindeki ismi almıştır. Bu hastalık; güneşe küfür edenlerde, güneşe lânet, beddua okuyanlarda olabilmektedir. Bu kişiler güneşten hayır görmez, vücudu yanar. Unutmayın, neye lânet okursanız ondan mahrum olur, sıkıntı yaşarsınız Allahuâlem."},

    # === UYUR GEZERLİK ===

    {"name": "Uyur Gezerlik", "category": "Uyku/Nörolojik",
     "symptoms": ["uyur gezerlik", "somnambülizm", "gece yürüme"],
     "causes": ["adak_eylem", "mezarci_ruhsat"],
     "remedy": "Ölmüş birine ziyaret adağı, mezarcı ruhsatı uyur gezerliğe sebep olur."},

    # === VARİS ===

    {"name": "Varis", "category": "Kardiyovasküler",
     "symptoms": ["varis", "bacak varisi", "toplardamar genişlemesi"],
     "causes": ["beddua", "zekat"],
     "remedy": "Damara okunan beddualar ve altın zekatı varise sebep olur."},

    # === VEBA ===

    {"name": "Veba", "category": "Enfeksiyon",
     "symptoms": ["veba", "bubonik veba", "ateşli hastalık"],
     "causes": ["beddua", "zulum_insan"],
     "remedy": "Veba hastalığı; okunan beddualar ile soydan insanlara hastalık bulaştırma zulmü ile gelebilmekte."},

    # === YÜRÜYEN CESET HASTALIĞI ===

    {"name": "Yürüyen Ceset Hastalığı (Cotard Sendromu)", "category": "Psikiyatrik/Nadir",
     "symptoms": ["yürüyen ceset sendromu", "cotard sendromu", "kendini ölü sanma"],
     "causes": ["iftira", "beddua", "hak_haram"],
     "remedy": "Yürüyen ceset hastalığında; bu kişiler kendilerinin öldüğünü zannedip yiyip içmez, gün geçtikçe erir. Hastalık, bir kişiye ağır iftira atıldığında, o kişi de ah edip, beddua edip, hak haram edip öldüyse olabilmektedir Allahuâlem."},

    # === YÜZ FELCİ (DETAYLI) ===

    {"name": "Yüz Felci (Detaylı)", "category": "Nörolojik",
     "symptoms": ["yüz felci", "bell palsi", "yüz kaslarının tutmaması"],
     "causes": ["zulum_anne_baba", "kinama", "beddua"],
     "remedy": "Bu hastalık; anne babanın yüzünü yamsılama, onlarla alay etme, beddualarını alma ile olabilir Allahuâlem. Yüzü felçli bir kişiyi kınamak da bu rahatsızlığın sebebi olabilmektedir."},

    # === ZATÜRRE ===

    {"name": "Zatürre", "category": "Solunum",
     "symptoms": ["zatürre", "pnömoni", "akciğer iltihabı"],
     "causes": ["beddua", "zulum_insan"],
     "remedy": "Zatürre hastalığı; ciğere okunan beddualar ve zulümler zatürre yapabilir."},

    # === ZONA (DETAYLI) ===

    {"name": "Zona (Detaylı)", "category": "Dermatolojik/Enfeksiyon",
     "symptoms": ["zona", "herpes zoster", "ağrılı döküntü"],
     "causes": ["zulum_insan", "zulum_hayvan"],
     "remedy": "İnsan ve hayvanlara zehirli okla zulüm zona yapabilir."},
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
