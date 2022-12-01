"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

import telebot

token = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
ndflbot = telebot.TeleBot(token)

'''Начало бота - команда start.'''
@ndflbot.message_handler(commands=["start"])
def start(message):
    ndflbot.send_message(message.chat.id, "Привет.")




'''Работа в режиме нон-стоп.'''
ndflbot.polling(none_stop=True)