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
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
    elif m.text == 'Акции':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert2) for advert2 in ['В разработке']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Акций к сожалению нет :(', reply_markup=keyboard)
    elif m.text == 'Поиск по ингредиентам': #####делаю поиск по ингредиентам
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Пицца', 'Суши']])
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Салат']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что будем искать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, advert3)
    elif m.text == 'Расчёт калорий':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Выбрать категорию']])
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Выбрать блюдо']])
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Рассчитать и вывести']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
    elif m.text == 'Корзина':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Оформить заказ']])
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Убрать некоторую еду из корзины']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
#####################################################################################################
#делаю поиск по ингредиентам
def advert3(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Отлично")
        bot.register_next_step_handler(msg, start)
    elif m.text == 'Пицца':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, advert33)

def advert33(m):
    if m.text == 'Которые входят в состав':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Соус томатный','Соус цезарь']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Соус грибной','Соус сырный']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Креметте','Шампиньоны']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сыр Моцарелла','Сыр Пармезан']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пепперони','Ветчина','Бекон','Салями']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Цыплёнок','Орегано','Лук']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Томаты','Базилик','Маслины']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Тунец','Перец',]])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id,'Выберете ингредиент')
        bot.register_next_step_handler(msg, find_food)
            
    if m.text == 'Без этих ингредиентов':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Соус томатный','Соус цезарь']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Соус грибной','Соус сырный']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Креметте','Шампиньоны']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сыр Моцарелла','Сыр Пармезан']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пепперони','Ветчина','Бекон','Салями']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Цыплёнок','Орегано','Лук']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Томаты','Базилик','Маслины']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Тунец','Перец',]])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id,'Выберете ингредиент')
        bot.register_next_step_handler(msg, find_food)

def find_food(m):
    bot.send_message(m.chat.id,'Произвожу анализ...')
            
#####################################################################################################
bot.polling()
