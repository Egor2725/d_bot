import telebot
from telebot import types

from time import sleep


from config import token
from keybord import base, courses, citys, start_key
from pars_course import show_money
from pars_weather import city_name, wheather_now, hourly_weather
from pars_films import get_films


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет)\nЧем могу помочь?)', reply_markup=base())


@bot.message_handler(content_types=['text'])
def sent_text(message):
    chat_id = message.chat.id
    if message.text == 'Привет':
        bot.send_message(chat_id, 'Привет)')
    elif message.text == '$Курсы валют':
        text = "↓Выберите валюту"
        bot.send_message(chat_id, text, reply_markup=courses())
    elif message.text == '☀Погода':
        bot.send_message(chat_id, f"Погода в {city_name.capitalize()} сейчас:\n{wheather_now('Минск')}", reply_markup=citys())
    elif message.text == '✌Афиша tut.by':
        films = get_films()
        for i in films.keys():
            bot.send_message(chat_id, f"{i}\n{films[i]}", reply_markup=base())
    else:
        bot.send_message(message.chat.id, 'Пока не понимаю.\nМеня ещё не доделали :c')


@bot.callback_query_handler(func=lambda message:True)
def ans(message):
    chat_id = message.message.chat.id
    money = show_money()
    if "courses_currency" in message.data:
        mes = message.data.split('_').pop()
        bot.send_message(chat_id, f"{mes} сейчас равен {money[mes]} BYN")
    if message.data == "return":
        bot.send_message(chat_id, '''\n\n☑Вы в главном меню\n\n''', reply_markup=base())
    if message.data == "change_city_name":
        mes = bot.send_message(chat_id, "Какой город интересует?")
        bot.register_next_step_handler(mes, weather)


@bot.message_handler(content_types=['locals'])
def get_locals(message):
    mes = message.locals
    chat_id = message.chat.id
    return mes


def weather(message):
    try:
        city_name = message.text
        chat_id = message.chat.id
        bot.send_message(chat_id, f"Погода в {city_name.capitalize()} сейчас:\n{wheather_now(city_name)}", reply_markup=citys())
    except:
        mes = bot.send_message(chat_id, "ooops:c\nЧто-то не так, попробуй ещё")
        bot.register_next_step_handler(mes, weather)




bot.polling(none_stop=True)

