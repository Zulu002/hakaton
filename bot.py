"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

import telebot
from telebot import types
import dataBase
import pendulum

token = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
ndflbot = telebot.TeleBot(token)

'''Начало бота - команда start.'''

@ndflbot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in range(1, 6):
        markup.add(types.KeyboardButton(str(i)))
    ndflbot.send_message(message.chat.id, "Привет это бот, который да..", reply_markup=markup)



'''Заполнение данных.'''
@ndflbot.message_handler(content_types=["text"])
def hendler_files(message):
    list_1 = ["1", "2", "3", "4", "5"]
    list_answer = []
    a = message.from_user.id
    b = message.text
    times = pendulum.now()
    if message.text in list_1:
        ndflbot.send_message(message.chat.id, "Ваша оценка была занесена в базу данных.")
        dataBase.Database().registerUser(a, str(times), b)
        list_answer.append(message.text)
    else:
        ndflbot.send_message(message.chat.id, message.text)


'''Работа в режиме нон-стоп.'''
ndflbot.polling(none_stop=True)
