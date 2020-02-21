from telebot import types

from pars_course import show_money


def start_key():
    k_b = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("↕Вернуться")
    k_b.add(btn)
    return k_b


def base():
    k_b = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton("$Курсы валют")
    btn2 = types.KeyboardButton("☀Погода")
    btn3 = types.KeyboardButton("✌Афиша tut.by")
    btn4 = types.KeyboardButton("☆Заведения\nрядом")
    k_b.add(btn1, btn2, btn3, btn4)
    return k_b


def courses():
    money = show_money()
    keybord = types.InlineKeyboardMarkup()
    for i in money.keys():
        keybord.add(types.InlineKeyboardButton(text=i, callback_data=f"courses_currency_{i}"))
    keybord.add(types.InlineKeyboardButton(text="◀Вернуться в главное меню", callback_data="return"))
    return keybord


def citys():
    from bot import bot
    keybord = types.InlineKeyboardMarkup()
    key_change = types.InlineKeyboardButton(text="✏️Изменить город", callback_data="change_city_name")
    ret = types.InlineKeyboardButton(text="◀Вернуться в главное меню", callback_data="return")
    keybord.add(key_change, ret)
    return keybord


# def films():
#     films_list = get_films()
#     keybord = types.InlineKeyboardMarkup()
#     for i in films_list:
#         keybord.add(types.InlineKeyboardButton(text=f"", callback_data=f"courses_currency_{i}"))
#     keybord.add(types.InlineKeyboardButton(text="◀Вернуться в главное меню", callback_data="return"))





