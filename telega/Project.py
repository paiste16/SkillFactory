import telebot
from config import keys, TOKEN
from utils import ConvertionException, MonetaryConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def welcome_baby(message: telebot.types.Message):
    text = "Чтобы пересчитать свое баблишко в другую валюту прикажи мне так:\n<что за баблишко у тебя сейчас><в какое баблишко перевести> <скока баблишка пересчитать>\n Чтобы увидеть какие валюты можем пересчитать, прикажи мне так: /values"
    bot.reply_to(message, f"Привет, мой повелитель {message.chat.username}!!!\n{text}")

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Какие валюты можем пересчитать:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConvertionException('Слишком много Вы по-написали, между прочим!!!')
        if len(values) < 3:
            raise ConvertionException('Слишком мало Вы по-написали, между прочим!!!')

        quote, base, amount = values
        total_base = MonetaryConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Чет Вы не то сделали, хозяин!!!\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Чет ниче у меня не получилось, плак, плак\n{e}')
    else:
        text = f'{amount} {quote} это {total_base} {base}'
        bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['voice'])
def you_sexy(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Ты секси, крошка!!!')

@bot.message_handler(content_types=['photo'])
def nice_meme(message: telebot.types.Message):
    bot.reply_to(message, f"Азаза, лал! Ну ты {message.chat.username} прекалист ваабщще!!!")




bot.polling()