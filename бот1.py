"""Дальше бога нет.
   ссылка на бота -> http://t.me/ndflDok_bot"""

import telebot

token = "5614187069:AAFxZNIR2tNpFLFWQ2IirgubkPBQNQzLMos"
ndflbot = telebot.TeleBot(token)

'''Начало бота - команда start.'''


@ndflbot.message_handler(commands=["start"])
def start(message):
    ndflbot.send_message(message.chat.id, "Привет.")


'''Заполнение данных.'''


@ndflbot.message_handler(content_types=["document"])
def hendler_files(message):
    document_id= message.document.file_id
    file_info = ndflbot.get_file(document_id)
    print(document_id)
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')
    ndflbot.send_message(message.chat.id, document_id)

@ndflbot.message_handler(content_types=["photo"])
def handler_photo(message):
    photo_id= message.photo[3].file_id
    file_info=ndflbot.get_file(photo_id)
    print(photo_id)
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')

'''Работа в режиме нон-стоп.'''
ndflbot.polling(none_stop=True)
