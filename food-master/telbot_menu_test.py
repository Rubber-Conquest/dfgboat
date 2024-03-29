import telebot
from telebot import types

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hello")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
    bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
    bot.register_next_step_handler(msg, name)

def name(m):
    if m.text == 'Меню':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    elif m.text == 'Акции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['В разработке']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        bot.send_message(m.chat.id, 'Акций к сожалению нет :(', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    elif m.text == 'Поиск по ингредиентам':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Выбрать блюдо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Вывести список подходящих блюд']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    elif m.text == 'Расчёт калорий':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Выбрать категорию']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Выбрать блюдо']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Рассчитать и вывести']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    elif m.text == 'Корзина':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Оформить заказ']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Убрать некоторую еду из корзины']])
        keyboard.add(*[types.KeyboardButton(advert) for advert in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)

bot.polling()