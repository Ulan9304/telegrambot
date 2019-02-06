# Бот курса валют

"""
?
Описание бота
"""

import telebot
import constants
import request
import urllib.request
from datetime import datetime

import json

bot = telebot.TeleBot(constants.TOKEN)


#Инфо о боте
print (bot.get_me())

def log(message,answer):
    print("\n ------")
    print(datetime.now())
    print("Сообщения от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                  message.from_user.last_name,
                                                                  str(message.from_user.id),
                                                                  message.text))
    print (answer)

# Парсес курса валют Fixer


def get_html(url):
    response = urllib.request.urlopen(url)
    return  response.read()

def main():
    currencies = get_html("http://data.fixer.io/api/latest?access_key=25daf431465a09f36aceea4609376f4a")
    # currencies = get_html("http://data.fixer.io/api/convert?access_key=25daf431465a09f36aceea4609376f4a&from=USD&to=KGS&amount=1")
    resp_dict = json.loads(currencies)
    rates = resp_dict['rates']
    usd = []
    for key, value in rates.items():
        if key == 'USD':
            usd.append(key)
            usd.append(value)
    print (rates['USD'])
    print("test",usd)


# Сообщения Бота при вводе данных

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row('/USD to SOM')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_start(message):
    hide_mark_up = telebot.types.ReplyKeyboardMarkupHide()
    bot.send_message(message.from_user.id, ",,", reply_markup=hide_mark_up)


@bot.message_handler(content_types=['help'])
def handle_text(message):
    if message.text == "help":
        bot.send_message(message.chat.id,"у меня только одна функция")
    else:
        pass

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Converter"
    if message.text == "USD SOM":
        log(message, answer)
        bot.send_message(message.chat.id,"68")
    elif message.text == str():
        log(message, answer)
    else:
        bot.send_message(message.chat.id, answer)
        log(message, answer)

bot.polling(none_stop=True,interval=0)