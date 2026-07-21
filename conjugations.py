"""
Spanish Verb Conjugation Data
Common verbs with full conjugation tables
"""

# Regular verb endings
REGULAR_AR = {
    "presente": ["o", "as", "a", "amos", "áis", "an"],
    "pretérito": ["é", "aste", "ó", "amos", "asteis", "aron"],
    "imperfecto": ["aba", "abas", "aba", "ábamos", "abais", "aban"],
    "futuro": ["aré", "arás", "ará", "aremos", "aréis", "arán"],
    "condicional": ["aría", "arías", "aría", "aríamos", "aríais", "arían"],
    "subjuntivo_presente": ["e", "es", "e", "emos", "éis", "en"],
}

REGULAR_ER = {
    "presente": ["o", "es", "e", "emos", "éis", "en"],
    "pretérito": ["í", "iste", "ió", "imos", "isteis", "ieron"],
    "imperfecto": ["ía", "ías", "ía", "íamos", "íais", "ían"],
    "futuro": ["eré", "erás", "erá", "eremos", "eréis", "erán"],
    "condicional": ["ería", "erías", "ería", "eríamos", "eríais", "erían"],
    "subjuntivo_presente": ["a", "as", "a", "amos", "áis", "an"],
}

REGULAR_IR = {
    "presente": ["o", "es", "e", "imos", "ís", "en"],
    "pretérito": ["í", "iste", "ió", "imos", "isteis", "ieron"],
    "imperfecto": ["ía", "ías", "ía", "íamos", "íais", "ían"],
    "futuro": ["iré", "irás", "irá", "iremos", "iréis", "irán"],
    "condicional": ["iría", "irías", "iría", "iríamos", "iríais", "irían"],
    "subjuntivo_presente": ["a", "as", "a", "amos", "áis", "an"],
}

PRONOUNS = ["yo", "tú", "él/ella/Ud.", "nosotros", "vosotros", "ellos/Uds."]

# Irregular verbs (fully conjugated)
IRREGULAR_VERBS = {
    "ser": {
        "meaning": "to be (permanent)",
        "meaning_zh": "是（永久性质）",
        "presente": ["soy", "eres", "es", "somos", "sois", "son"],
        "pretérito": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "imperfecto": ["era", "eras", "era", "éramos", "erais", "eran"],
        "futuro": ["seré", "serás", "será", "seremos", "seréis", "serán"],
        "condicional": ["sería", "serías", "sería", "seríamos", "seríais", "serían"],
        "subjuntivo_presente": ["sea", "seas", "sea", "seamos", "seáis", "sean"],
    },
    "estar": {
        "meaning": "to be (temporary/location)",
        "meaning_zh": "在/处于（暂时状态）",
        "presente": ["estoy", "estás", "está", "estamos", "estáis", "están"],
        "pretérito": ["estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron"],
        "imperfecto": ["estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"],
        "futuro": ["estaré", "estarás", "estará", "estaremos", "estaréis", "estarán"],
        "condicional": ["estaría", "estarías", "estaría", "estaríamos", "estaríais", "estarían"],
        "subjuntivo_presente": ["esté", "estés", "esté", "estemos", "estéis", "estén"],
    },
    "tener": {
        "meaning": "to have",
        "meaning_zh": "有/拥有",
        "presente": ["tengo", "tienes", "tiene", "tenemos", "tenéis", "tienen"],
        "pretérito": ["tuve", "tuviste", "tuvo", "tuvimos", "tuvisteis", "tuvieron"],
        "imperfecto": ["tenía", "tenías", "tenía", "teníamos", "teníais", "tenían"],
        "futuro": ["tendré", "tendrás", "tendrá", "tendremos", "tendréis", "tendrán"],
        "condicional": ["tendría", "tendrías", "tendría", "tendríamos", "tendríais", "tendrían"],
        "subjuntivo_presente": ["tenga", "tengas", "tenga", "tengamos", "tengáis", "tengan"],
    },
    "ir": {
        "meaning": "to go",
        "meaning_zh": "去",
        "presente": ["voy", "vas", "va", "vamos", "vais", "van"],
        "pretérito": ["fui", "fuiste", "fue", "fuimos", "fuisteis", "fueron"],
        "imperfecto": ["iba", "ibas", "iba", "íbamos", "ibais", "iban"],
        "futuro": ["iré", "irás", "irá", "iremos", "iréis", "irán"],
        "condicional": ["iría", "irías", "iría", "iríamos", "iríais", "irían"],
        "subjuntivo_presente": ["vaya", "vayas", "vaya", "vayamos", "vayáis", "vayan"],
    },
    "hacer": {
        "meaning": "to do/make",
        "meaning_zh": "做/制作",
        "presente": ["hago", "haces", "hace", "hacemos", "hacéis", "hacen"],
        "pretérito": ["hice", "hiciste", "hizo", "hicimos", "hicisteis", "hicieron"],
        "imperfecto": ["hacía", "hacías", "hacía", "hacíamos", "hacíais", "hacían"],
        "futuro": ["haré", "harás", "hará", "haremos", "haréis", "harán"],
        "condicional": ["haría", "harías", "haría", "haríamos", "haríais", "harían"],
        "subjuntivo_presente": ["haga", "hagas", "haga", "hagamos", "hagáis", "hagan"],
    },
    "decir": {
        "meaning": "to say/tell",
        "meaning_zh": "说/告诉",
        "presente": ["digo", "dices", "dice", "decimos", "decís", "dicen"],
        "pretérito": ["dije", "dijiste", "dijo", "dijimos", "dijisteis", "dijeron"],
        "imperfecto": ["decía", "decías", "decía", "decíamos", "decíais", "decían"],
        "futuro": ["diré", "dirás", "dirá", "diremos", "diréis", "dirán"],
        "condicional": ["diría", "dirías", "diría", "diríamos", "diríais", "dirían"],
        "subjuntivo_presente": ["diga", "digas", "diga", "digamos", "digáis", "digan"],
    },
    "poder": {
        "meaning": "to be able to/can",
        "meaning_zh": "能/可以",
        "presente": ["puedo", "puedes", "puede", "podemos", "podéis", "pueden"],
        "pretérito": ["pude", "pudiste", "pudo", "pudimos", "pudisteis", "pudieron"],
        "imperfecto": ["podía", "podías", "podía", "podíamos", "podíais", "podían"],
        "futuro": ["podré", "podrás", "podrá", "podremos", "podréis", "podrán"],
        "condicional": ["podría", "podrías", "podría", "podríamos", "podríais", "podrían"],
        "subjuntivo_presente": ["pueda", "puedas", "pueda", "podamos", "podáis", "puedan"],
    },
    "querer": {
        "meaning": "to want/love",
        "meaning_zh": "想要/爱",
        "presente": ["quiero", "quieres", "quiere", "queremos", "queréis", "quieren"],
        "pretérito": ["quise", "quisiste", "quiso", "quisimos", "quisisteis", "quisieron"],
        "imperfecto": ["quería", "querías", "quería", "queríamos", "queríais", "querían"],
        "futuro": ["querré", "querrás", "querrá", "querremos", "querréis", "querrán"],
        "condicional": ["querría", "querrías", "querría", "querríamos", "querríais", "querrían"],
        "subjuntivo_presente": ["quiera", "quieras", "quiera", "queramos", "queráis", "quieran"],
    },
    "saber": {
        "meaning": "to know (facts)",
        "meaning_zh": "知道（事实）",
        "presente": ["sé", "sabes", "sabe", "sabemos", "sabéis", "saben"],
        "pretérito": ["supe", "supiste", "supo", "supimos", "supisteis", "supieron"],
        "imperfecto": ["sabía", "sabías", "sabía", "sabíamos", "sabíais", "sabían"],
        "futuro": ["sabré", "sabrás", "sabrá", "sabremos", "sabréis", "sabrán"],
        "condicional": ["sabría", "sabrías", "sabría", "sabríamos", "sabríais", "sabrían"],
        "subjuntivo_presente": ["sepa", "sepas", "sepa", "sepamos", "sepáis", "sepan"],
    },
    "venir": {
        "meaning": "to come",
        "meaning_zh": "来",
        "presente": ["vengo", "vienes", "viene", "venimos", "venís", "vienen"],
        "pretérito": ["vine", "viniste", "vino", "vinimos", "vinisteis", "vinieron"],
        "imperfecto": ["venía", "venías", "venía", "veníamos", "veníais", "venían"],
        "futuro": ["vendré", "vendrás", "vendrá", "vendremos", "vendréis", "vendrán"],
        "condicional": ["vendría", "vendrías", "vendría", "vendríamos", "vendríais", "vendrían"],
        "subjuntivo_presente": ["venga", "vengas", "venga", "vengamos", "vengáis", "vengan"],
    },
    "dar": {
        "meaning": "to give",
        "meaning_zh": "给",
        "presente": ["doy", "das", "da", "damos", "dais", "dan"],
        "pretérito": ["di", "diste", "dio", "dimos", "disteis", "dieron"],
        "imperfecto": ["daba", "dabas", "daba", "dábamos", "dabais", "daban"],
        "futuro": ["daré", "darás", "dará", "daremos", "daréis", "darán"],
        "condicional": ["daría", "darías", "daría", "daríamos", "daríais", "darían"],
        "subjuntivo_presente": ["dé", "des", "dé", "demos", "deis", "den"],
    },
    "ver": {
        "meaning": "to see",
        "meaning_zh": "看",
        "presente": ["veo", "ves", "ve", "vemos", "veis", "ven"],
        "pretérito": ["vi", "viste", "vio", "vimos", "visteis", "vieron"],
        "imperfecto": ["veía", "veías", "veía", "veíamos", "veíais", "veían"],
        "futuro": ["veré", "verás", "verá", "veremos", "veréis", "verán"],
        "condicional": ["vería", "verías", "vería", "veríamos", "veríais", "verían"],
        "subjuntivo_presente": ["vea", "veas", "vea", "veamos", "veáis", "vean"],
    },
    "poner": {
        "meaning": "to put/place",
        "meaning_zh": "放/放置",
        "presente": ["pongo", "pones", "pone", "ponemos", "ponéis", "ponen"],
        "pretérito": ["puse", "pusiste", "puso", "pusimos", "pusisteis", "pusieron"],
        "imperfecto": ["ponía", "ponías", "ponía", "poníamos", "poníais", "ponían"],
        "futuro": ["pondré", "pondrás", "pondrá", "pondremos", "pondréis", "pondrán"],
        "condicional": ["pondría", "pondrías", "pondría", "pondríamos", "pondríais", "pondrían"],
        "subjuntivo_presente": ["ponga", "pongas", "ponga", "pongamos", "pongáis", "pongan"],
    },
    "salir": {
        "meaning": "to go out/leave",
        "meaning_zh": "出去/离开",
        "presente": ["salgo", "sales", "sale", "salimos", "salís", "salen"],
        "pretérito": ["salí", "saliste", "salió", "salimos", "salisteis", "salieron"],
        "imperfecto": ["salía", "salías", "salía", "salíamos", "salíais", "salían"],
        "futuro": ["saldré", "saldrás", "saldrá", "saldremos", "saldréis", "saldrán"],
        "condicional": ["saldría", "saldrías", "saldría", "saldríamos", "saldríais", "saldrían"],
        "subjuntivo_presente": ["salga", "salgas", "salga", "salgamos", "salgáis", "salgan"],
    },
    "haber": {
        "meaning": "to have (auxiliary)",
        "meaning_zh": "有（助动词）",
        "presente": ["he", "has", "ha", "hemos", "habéis", "han"],
        "pretérito": ["hube", "hubiste", "hubo", "hubimos", "hubisteis", "hubieron"],
        "imperfecto": ["había", "habías", "había", "habíamos", "habíais", "habían"],
        "futuro": ["habré", "habrás", "habrá", "habremos", "habréis", "habrán"],
        "condicional": ["habría", "habrías", "habría", "habríamos", "habríais", "habrían"],
        "subjuntivo_presente": ["haya", "hayas", "haya", "hayamos", "hayáis", "hayan"],
    },
}

TENSE_NAMES = {
    "presente": "现在时 Presente",
    "pretérito": "简单过去时 Pretérito",
    "imperfecto": "未完成过去时 Imperfecto",
    "futuro": "将来时 Futuro",
    "condicional": "条件时 Condicional",
    "subjuntivo_presente": "虚拟式现在时 Subjuntivo",
}


def conjugate_regular(verb):
    """Conjugate a regular verb based on its ending"""
    if verb.endswith("ar"):
        stem = verb[:-2]
        endings = REGULAR_AR
    elif verb.endswith("er"):
        stem = verb[:-2]
        endings = REGULAR_ER
    elif verb.endswith("ir"):
        stem = verb[:-2]
        endings = REGULAR_IR
    else:
        return None

    result = {
        "meaning": "",
        "meaning_zh": "",
    }
    for tense, ends in endings.items():
        if tense in ("presente", "pretérito", "imperfecto", "subjuntivo_presente"):
            result[tense] = [stem + e for e in ends]
        else:
            # futuro and condicional use full infinitive as stem
            result[tense] = [verb + e.lstrip(verb[-2:]) if tense == "futuro" else verb + e.lstrip(verb[-2:]) for e in ends]

    # For futuro and condicional, the stem is the full infinitive
    futuro_ends = ["é", "ás", "á", "emos", "éis", "án"]
    condicional_ends = ["ía", "ías", "ía", "íamos", "íais", "ían"]
    result["futuro"] = [verb + e for e in futuro_ends]
    result["condicional"] = [verb + e for e in condicional_ends]

    return result


def get_conjugation(verb):
    """Get conjugation for a verb (irregular or regular)"""
    verb = verb.lower().strip()

    # Check irregular verbs first
    if verb in IRREGULAR_VERBS:
        return IRREGULAR_VERBS[verb]

    # Try regular conjugation
    regular = conjugate_regular(verb)
    if regular:
        return regular

    return None
