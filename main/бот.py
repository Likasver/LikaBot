import telebot
from telebot import types

# Константы
BOT_TOKEN = "7636250407:AAFVqHGrt4F9-gkSrTYTrzugAMz8njx_SWI"
KNOWLEDGE_BASE = {
    "minimalism": {
        "гостиная": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=c0cc9aac344ad2bac58495f411e56d30-5232511-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=58604683860e676c438d8bcc448618d200ed6d795d358aff-12534005-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=576d1fedebf6a6eb73141c9963165aac696c0d8f-10299502-images-thumbs&n=13"],
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=40be64df1c477c93a692f2bfd9a7fd39-3501814-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=dfc1bbb329dc68491a8ddc3757e8be2f1558ce36-5606166-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=4b43668b150d1a792cd23cccc75049a1220d2a21-4900921-images-thumbs&n=13"],
            }
        },
        "кухня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=8f10ba24b7aa85b8ef2223f805ce9c3a5cbb8e11-10850090-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=139dcf7758b8d68de7a4c0b7a2af56d07867ccf4-8282002-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=52ccdb497cb6701fd0bf1ce41d2f59fd521631801d709878-12322312-images-thumbs&n=13"],
            }
        },
        "детская": {
            "цвет": {
                 "белый": ["https://avatars.mds.yandex.net/i?id=aa9b9631892b975ef3658d209dbe7d648178dd29-8497900-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=9a7aeaf8d80e689dce38e9b6060ce332-5875719-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=fc1d6b3b4222f642c6d4f4a199eb91fa623ca106-10256664-images-thumbs&n=13"],
            }
        },
        "прихожая": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=800830123cb8c31cd8345075b913a92d1568baa5-10285533-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=67e466ce22f2af369797e33adfd50cefd2b7415f-7051980-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=30b3e5a0201c6b920635cce2a4ffb57d666200bd-10599899-images-thumbs&n=13"],
            }
        }
    },
"loft": {
    "гостиная": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=9831bea2055206cc08101795306f3101170711f0-7001681-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=e9483b7d0a6a83875ec493f6379b85acc2a6b1ea-10354750-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=7840246eda875417f8d0accc52c9476d974a8491-10849338-images-thumbs&n=13"],
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=c03fb413757ddc5612846a1d0d24a7b816799e21edd67585-11376718-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=5f96837ea117caff962f45570eadf75b760b4507-13509485-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=cdc84be21d1e7a6774c28155f130e6b0851b677b-10767243-images-thumbs&n=13"],
            }
        },
        "кухня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=b9412bea812c583a1a6d6585db45bb0d306226f6-7065709-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=19f4906a9d15885e3b97f204ede03e6d22065f0f-12500826-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=6542bb102e98e7f7de4a4a55725b753a1e27d5b3-13469218-images-thumbs&n=13"],
            }
        },
        "детская": {
            "цвет": {
                 "белый": ["https://avatars.mds.yandex.net/i?id=d1be969f28378d95daea12bd73577a6430781280-5271179-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=82de79a93e1655ad49365c5e16336d76e1fdeda6-5364055-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=d163d04147506fa004b1e99944bbf6f951d2d5ee-12540459-images-thumbs&n=13"],
            }
        },
        "прихожая": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=0a862016d139f5c9a73f79dcf1161f412b4eb076-9847625-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=9bf9449def76a62b5753b6551006c33e4fb283be-5221636-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=e55851226c2b70a9c8b12e79ab973427d3ddff19-9860570-images-thumbs&n=13"],
            }
        }
    },
"boho": {
    "гостиная": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=8aa4a05a82af92f04f7579c1f064cc66-5447357-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=f886f1ba94a3b945133200593c643b99-4885303-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=da96ee2608eb6d60f43031c3cc32c877feb7b613-8310741-images-thumbs&n=13"],
            }
        },
        "спальня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=6910781f04619e4244eb477cd2d006b155013728-10555242-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=95c24d10f664bdd78f1e6db13e7bad610a9a3826-8225729-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=8a3cf95cffb91525dba88ea6dbbe6d0ed77267b7-12639726-images-thumbs&n=13"],
            }
        },
        "кухня": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=8ccaedfaa9ddffd2de0efecacd7b8f31d724d25c-4552311-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=af0cc61df42f3aea6fb54e43d7bddaf7d6e3ed93-6948220-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=2a00000179ff22c0f875defa8afe4a3d334a-4575918-images-thumbs&n=13"],
            }
        },
        "детская": {
            "цвет": {
                 "белый": ["https://avatars.mds.yandex.net/i?id=76f6c2ce731bf82c1f66de7aa0f2811848700774-8497203-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=2fca30b1b98a2e7914fb3183b124ba09-5549228-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=5caf41726e7668cabab78d5c4dfcbfb24a41ed69-5235028-images-thumbs&n=13"],
            }
        },
        "прихожая": {
            "цвет": {
                "белый": ["https://avatars.mds.yandex.net/i?id=8ed397f4a4271c1d7a0054a787db077206f562d0-12575309-images-thumbs&n=13"],
                "серый": ["https://avatars.mds.yandex.net/i?id=a2bb592d96abeb5500fa4944fc9a37863616ed94-9832347-images-thumbs&n=13"],
                "коричневый": ["https://avatars.mds.yandex.net/i?id=883de5ba9b4a2eaf4760b4a82de5fd91415ef235-12490070-images-thumbs&n=13"],
            }
        }
    }
}
# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)

# Хранение данных пользователя
user_data = {}

# Команды
COMMANDS = {
    "start": "Начать работу с ботом",
    "help": "Получить справку по командам",
    "style": "Выбрать стиль интерьера (например, /style minimalism, loft, boho)",
}

# Сообщения
MESSAGES = {
    "welcome": """
Привет! Я ваш помощник в дизайне интерьера. Вот что я могу:
/style - Выбрать стиль интерьера (например, /style minimalism, loft, boho)
""",
    "unknown_command": "Извините, я не понимаю эту команду. Используйте /help для списка команд.",
    "style_not_found": "Извините, я не знаю такой стиль. Попробуйте ещё раз.",
    "room_not_found": "Пожалуйста, выберите одно из предложенных помещений (гостиная, спальня, кухня, детская, прихожая).",
    "color_not_found": "Извините, я не знаю такой цвет. Попробуйте ещё раз.",
    "photo_error": "Не удалось загрузить фото.",
}

# Обработчик команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, MESSAGES["welcome"])

# Обработчик команды /style
@bot.message_handler(commands=['style'])
def ask_style(message):
    try:
        style_name = message.text.split(" ", 1)[1].lower()
        if style_name in KNOWLEDGE_BASE:
            user_data[message.chat.id] = {"style": style_name, "step": "ask_room"}
            bot.reply_to(message, "Выберите тип помещения (гостиная, спальня, кухня, детская, прихожая):")
        else:
            bot.reply_to(message, MESSAGES["style_not_found"])
    except IndexError:
        bot.reply_to(message, "Пожалуйста, укажите стиль после команды /style (например, /style minimalism, loft, boho)")

# Обработчик для выбора помещения
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_room")
def ask_room(message):
    room = message.text.lower()
    if room in KNOWLEDGE_BASE[user_data[message.chat.id]["style"]]:
        user_data[message.chat.id]["room"] = room
        user_data[message.chat.id]["step"] = "ask_color"
        bot.reply_to(message, "Какой цвет вы предпочитаете? (например, белый, серый, коричневый)")
    else:
        bot.reply_to(message, MESSAGES["room_not_found"])

# Обработчик для выбора цвета
@bot.message_handler(func=lambda message: user_data.get(message.chat.id, {}).get("step") == "ask_color")
def ask_color(message):
    color = message.text.lower()
    style = user_data[message.chat.id]["style"]
    room = user_data[message.chat.id]["room"]

    if color in KNOWLEDGE_BASE[style][room]["цвет"]:
        user_data[message.chat.id]["color"] = color
        user_data[message.chat.id]["step"] = None

        photos = KNOWLEDGE_BASE[style][room]["цвет"][color]
        for photo_url in photos:
            try:
                bot.send_photo(message.chat.id, photo_url, caption=f"Пример стиля {style} для {room} в цвете {color}")
            except Exception as e:
                print(f"Ошибка отправки фото: {e}")
                bot.reply_to(message, MESSAGES["photo_error"])
    else:
        bot.reply_to(message, MESSAGES["color_not_found"])

    user_data.pop(message.chat.id, None)

# Обработчик для неизвестных команд
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, MESSAGES["unknown_command"])

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен!")
    try:
        bot.infinity_polling()
    except Exception as e:
        print(f"Бот упал с ошибкой: {e}")