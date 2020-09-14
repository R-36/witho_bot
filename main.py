import telebot
from utils import find_vowel, find_consonant
from config import vowel, consonant

bot = telebot.TeleBot('1299434028:AAFRfZA-UqOuhVpyHmeLHTyu_GayjKv8KN4')


bot_keyboard = telebot.types.ReplyKeyboardMarkup(True)
bot_keyboard.row('Гласные', 'Согласные')
bot_keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
bot_keyboard2.row('Последние сообщение', 'Последние 10 сообщений')
state = {'find_object_type': 'Гласные', 'find_object_methods': ''}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот, который умеет считать гласные и согласные буквы в твоем сообщении,'
                                      ' какие буквы необходимо посчитать?', reply_markup=bot_keyboard)


@bot.message_handler(content_types=['text'])
def start_message(message, arr=None):
    if arr is None:
        arr = state
    if message.text.lower() == 'гласные':
        arr['find_object_type'] = 'Гласные'
        bot.send_message(message.chat.id, f'Выбранный тип: {arr["find_object_type"]}')
        bot.send_message(message.chat.id, 'Выберите период:', reply_markup=bot_keyboard2)
    elif message.text.lower() == 'согласные':
        arr['find_object_type'] = 'Согласные'
        bot.send_message(message.chat.id, f'Выбранный тип: {arr["find_object_type"]}')
        bot.send_message(message.chat.id, 'Выберите период:', reply_markup=bot_keyboard2)
    elif message.text.lower() == 'последние сообщение':
        arr['find_object_methods'] = 'последние сообщение'
        bot.send_message(message.chat.id, f'Выбранный период: {arr["find_object_methods"]}')
        bot.send_message(message.chat.id, 'Введите сообщение')
    elif message.text.lower() == 'последние 10 сообщений':
        arr['find_object_methods'] = ''
        bot.send_message(message.chat.id, 'Данная функция пока не доступна')
        bot.send_message(message.chat.id, 'Выберите период:', reply_markup=bot_keyboard2)
    elif arr['find_object_type'] == '' or arr['find_object_methods'] == '':
        bot.send_message(message.chat.id, 'Введена неправильная команда, попробуй еще раз')
        bot.send_message(message.chat.id, 'Какие буквы необходимо посчитать', reply_markup=bot_keyboard)
    elif arr['find_object_type'] == 'Гласные' and arr['find_object_methods'] == 'последние сообщение':
        counter = find_vowel(vowel, message.text.lower())
        bot.send_message(message.chat.id, f'Количество гласных букв: {counter}')
        arr['find_object_type'] = ''
        arr['find_object_methods'] = ''
        bot.send_message(message.chat.id, 'Какие буквы необходимо посчитать', reply_markup=bot_keyboard)
    elif arr['find_object_type'] == 'Согласные' and arr['find_object_methods'] == 'последние сообщение':
        counter = find_consonant(consonant, message.text.lower())
        bot.send_message(message.chat.id, f'Количество согласных букв: {counter}')
        arr['find_object_type'] = ''
        arr['find_object_methods'] = ''
        bot.send_message(message.chat.id, 'Какие буквы необходимо посчитать', reply_markup=bot_keyboard)


bot.polling()
