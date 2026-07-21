"""
Daily Spanish Readings - 每日西语小阅读
Simple texts with translations and grammar explanations
"""

READINGS = [
    {
        "title": "En el mercado",
        "level": "A1",
        "text": "María va al mercado todos los sábados. Ella compra frutas frescas y verduras. Le gusta mucho hablar con los vendedores. Hoy compra manzanas, naranjas y un kilo de tomates.",
        "translation": "玛丽亚每个周六都去市场。她买新鲜水果和蔬菜。她很喜欢和商贩们聊天。今天她买了苹果、橘子和一公斤西红柿。",
        "grammar": [
            {"point": "va al = va + a + el", "explanation": "ir（去）的第三人称单数现在时 + a + el 缩合为 al"},
            {"point": "todos los sábados", "explanation": "表示频率：'每个周六'。los + 星期复数 = 每周X"},
            {"point": "Le gusta hablar", "explanation": "gustar 结构：间接宾语代词 + gusta + 动词原形 = 喜欢做某事"},
        ]
    },
    {
        "title": "Mi familia",
        "level": "A1",
        "text": "Tengo una familia pequeña. Somos cuatro personas: mi padre, mi madre, mi hermana y yo. Mi padre se llama Carlos y trabaja en un hospital. Mi madre es profesora de inglés.",
        "translation": "我有一个小家庭。我们一共四口人：我爸爸、妈妈、姐姐和我。我爸爸叫卡洛斯，在医院工作。我妈妈是英语老师。",
        "grammar": [
            {"point": "Tengo", "explanation": "tener（有）的第一人称单数：yo tengo"},
            {"point": "Somos", "explanation": "ser（是）的第一人称复数：nosotros somos"},
            {"point": "se llama", "explanation": "llamarse（叫做）的反身动词结构，él se llama = 他叫..."},
        ]
    },
    {
        "title": "Un día normal",
        "level": "A1",
        "text": "Me despierto a las siete de la mañana. Primero me ducho y después desayuno café con tostadas. Salgo de casa a las ocho y tomo el autobús para ir al trabajo.",
        "translation": "我早上七点醒来。先洗澡，然后吃早餐，喝咖啡配吐司。八点出门，坐公交车去上班。",
        "grammar": [
            {"point": "Me despierto", "explanation": "despertarse（醒来）是反身动词，me = 我自己"},
            {"point": "a las siete", "explanation": "表示时间：a la(s) + 数字 = 在...点"},
            {"point": "para ir", "explanation": "para + 动词原形 = 为了做某事（表目的）"},
        ]
    },
    {
        "title": "El restaurante",
        "level": "A1",
        "text": "Ayer fui a un restaurante con mis amigos. Pedí una paella de mariscos y un vaso de vino tinto. La comida estaba deliciosa. Pagamos la cuenta y dejamos una propina.",
        "translation": "昨天我和朋友们去了一家餐厅。我点了海鲜烩饭和一杯红酒。菜很好吃。我们付了账单并留了小费。",
        "grammar": [
            {"point": "fui", "explanation": "ir（去）的过去时第一人称：yo fui = 我去了"},
            {"point": "Pedí", "explanation": "pedir（点菜/请求）的过去时第一人称"},
            {"point": "estaba deliciosa", "explanation": "estar + 形容词 描述暂时状态。这里用未完成过去时表示当时的状态"},
        ]
    },
    {
        "title": "El clima",
        "level": "A1",
        "text": "Hoy hace mucho calor. El sol brilla en el cielo azul y no hay nubes. En verano siempre hace calor aquí. Me gusta ir a la playa cuando hace buen tiempo.",
        "translation": "今天很热。太阳在蓝色的天空中照耀，没有云。夏天这里总是很热。天气好的时候我喜欢去海滩。",
        "grammar": [
            {"point": "Hace calor", "explanation": "hacer 用于描述天气：hace calor（热）, hace frío（冷）, hace viento（刮风）"},
            {"point": "no hay nubes", "explanation": "hay = there is/are（有），否定形式 no hay = 没有"},
            {"point": "cuando hace buen tiempo", "explanation": "cuando + 动词 = 当...时候"},
        ]
    },
    {
        "title": "De compras",
        "level": "A2",
        "text": "Necesito comprar ropa nueva para el invierno. Voy a la tienda y me pruebo un abrigo negro. Me queda un poco grande, así que pido una talla más pequeña. Al final compro el abrigo y una bufanda roja.",
        "translation": "我需要买冬天的新衣服。我去商店试了一件黑色外套。有点大了，所以我要了小一号的。最后我买了外套和一条红围巾。",
        "grammar": [
            {"point": "me pruebo", "explanation": "probarse（试穿）反身动词，me pruebo = 我试穿"},
            {"point": "Me queda grande", "explanation": "quedar 表示衣服合不合身：me queda bien（合身）, grande（大）, pequeño（小）"},
            {"point": "así que", "explanation": "连接词，表示'所以/因此'"},
        ]
    },
    {
        "title": "Las vacaciones",
        "level": "A2",
        "text": "El verano pasado viajé a Barcelona con mi novio. Visitamos la Sagrada Familia y paseamos por las Ramblas. Comimos tapas en un bar pequeño cerca del puerto. Fue un viaje maravilloso.",
        "translation": "去年夏天我和男朋友去了巴塞罗那。我们参观了圣家堂，在兰布拉大道散步。在港口附近的小酒吧吃了西班牙小吃。这是一次美妙的旅行。",
        "grammar": [
            {"point": "viajé", "explanation": "viajar 过去时第一人称。规则-ar动词过去时：é, aste, ó, amos, asteis, aron"},
            {"point": "Visitamos, paseamos, comimos", "explanation": "过去时第一人称复数，讲述已完成的连续动作"},
            {"point": "Fue", "explanation": "ser 的过去时第三人称：fue = it was"},
        ]
    },
    {
        "title": "En el médico",
        "level": "A2",
        "text": "No me siento bien hoy. Me duele la cabeza y tengo fiebre. Voy al médico y me dice que tengo gripe. Me receta medicinas y me aconseja descansar tres días en casa.",
        "translation": "我今天不舒服。头疼还发烧。去看医生，他说我得了流感。给我开了药，建议我在家休息三天。",
        "grammar": [
            {"point": "Me duele la cabeza", "explanation": "doler（疼）和 gustar 一样用间接宾语结构：me duele = 我...疼"},
            {"point": "me dice que", "explanation": "decir que = 说/告诉某人...。que 引导宾语从句"},
            {"point": "me aconseja descansar", "explanation": "aconsejar + 动词原形 = 建议做某事"},
        ]
    },
    {
        "title": "El fin de semana",
        "level": "A2",
        "text": "Este fin de semana voy a hacer muchas cosas. El sábado por la mañana voy a limpiar la casa. Por la tarde quedaré con mis amigos para tomar café. El domingo quiero dormir hasta tarde y leer un libro.",
        "translation": "这个周末我要做很多事。周六上午打扫房间。下午约朋友喝咖啡。周日想睡懒觉然后看书。",
        "grammar": [
            {"point": "voy a + infinitivo", "explanation": "ir a + 动词原形 = 近将来时，表示计划/打算做某事"},
            {"point": "por la mañana/tarde", "explanation": "por la mañana（上午）, por la tarde（下午）, por la noche（晚上）"},
            {"point": "quedaré con", "explanation": "quedar con alguien = 和某人约见面。这里用将来时"},
        ]
    },
    {
        "title": "Recuerdos de la infancia",
        "level": "A2",
        "text": "Cuando era niño, vivía en un pueblo pequeño. Todos los días jugaba con mis amigos en la plaza. Mi abuela nos hacía galletas y nos contaba cuentos antes de dormir. Eran tiempos muy felices.",
        "translation": "小时候我住在一个小镇上。每天和朋友们在广场上玩。奶奶给我们做饼干，睡前给我们讲故事。那是非常幸福的时光。",
        "grammar": [
            {"point": "Cuando era niño", "explanation": "未完成过去时（imperfecto）描述过去的持续状态或习惯"},
            {"point": "vivía, jugaba, hacía", "explanation": "imperfecto 表示过去的习惯性动作（以前经常...）"},
            {"point": "antes de dormir", "explanation": "antes de + 动词原形 = 在做某事之前"},
        ]
    },
    {
        "title": "La tecnología",
        "level": "A2",
        "text": "Uso mi teléfono móvil todos los días. Lo necesito para trabajar, para comunicarme con mi familia y para ver las noticias. Sin embargo, creo que pasamos demasiado tiempo mirando pantallas.",
        "translation": "我每天都用手机。工作需要它，和家人联系需要它，看新闻也需要它。但是我觉得我们花太多时间盯着屏幕了。",
        "grammar": [
            {"point": "Lo necesito", "explanation": "lo = 直接宾语代词（它），代替前面提到的 teléfono"},
            {"point": "para + infinitivo", "explanation": "para 后接动词原形表示目的：para trabajar = 为了工作"},
            {"point": "Sin embargo", "explanation": "转折连词 = 但是/然而"},
        ]
    },
    {
        "title": "Aprender idiomas",
        "level": "A2",
        "text": "Estoy aprendiendo español desde hace seis meses. Al principio era muy difícil, pero ahora puedo entender conversaciones sencillas. Practico todos los días escuchando podcasts y leyendo artículos cortos.",
        "translation": "我学西班牙语已经六个月了。开始很难，但现在能听懂简单的对话了。每天通过听播客和读短文来练习。",
        "grammar": [
            {"point": "Estoy aprendiendo", "explanation": "estar + gerundio（-ando/-iendo）= 现在进行时"},
            {"point": "desde hace seis meses", "explanation": "desde hace + 时间 = 从...前开始到现在（持续了多久）"},
            {"point": "escuchando, leyendo", "explanation": "副动词（gerundio）表示方式：通过听.../通过读..."},
        ]
    },
    {
        "title": "La cocina española",
        "level": "B1",
        "text": "La tortilla española es uno de los platos más famosos de España. Se prepara con huevos, patatas y, a veces, cebolla. Aunque parece fácil, hacer una buena tortilla requiere práctica. El secreto está en el punto de cocción del huevo.",
        "translation": "西班牙土豆饼是西班牙最有名的菜之一。用鸡蛋、土豆，有时加洋葱来做。虽然看起来简单，但做好一个土豆饼需要练习。秘诀在于鸡蛋的火候。",
        "grammar": [
            {"point": "uno de los platos más famosos", "explanation": "uno de los + 最高级 = ...中最...的之一"},
            {"point": "Se prepara", "explanation": "se + 第三人称动词 = 被动/无人称结构（被准备/人们准备）"},
            {"point": "Aunque parece fácil", "explanation": "aunque = 虽然/尽管，引导让步从句"},
        ]
    },
    {
        "title": "Un sueño",
        "level": "B1",
        "text": "Anoche tuve un sueño muy extraño. Estaba caminando por una ciudad que no conocía. De repente, empezó a llover y todas las personas desaparecieron. Me sentí solo pero no tenía miedo. Cuando desperté, me di cuenta de que era solo un sueño.",
        "translation": "昨晚做了一个很奇怪的梦。我在一个陌生的城市走着。突然下起了雨，所有人都消失了。我感到孤单但不害怕。醒来时才意识到那只是一个梦。",
        "grammar": [
            {"point": "Estaba caminando", "explanation": "imperfecto de estar + gerundio = 过去进行时（当时正在走）"},
            {"point": "empezó a llover", "explanation": "empezar a + infinitivo = 开始做某事。empezó 是过去时"},
            {"point": "me di cuenta de que", "explanation": "darse cuenta de que = 意识到...（反身动词 + 从句）"},
        ]
    },
]


def get_reading_for_today():
    """Get today's reading based on day of year"""
    from datetime import datetime
    day_of_year = datetime.now().timetuple().tm_yday
    index = day_of_year % len(READINGS)
    reading = READINGS[index]
    reading["day_index"] = index
    reading["total"] = len(READINGS)
    return reading


def get_reading_by_index(index):
    """Get a specific reading by index"""
    if 0 <= index < len(READINGS):
        reading = READINGS[index]
        reading["day_index"] = index
        reading["total"] = len(READINGS)
        return reading
    return None
