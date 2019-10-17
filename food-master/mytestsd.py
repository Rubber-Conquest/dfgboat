import telebot
from telebot import types

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

pizza_menu='1. Пепперони и томаты\n2. Сырная\n3. Супер Мит\n4. Морская с тунцом\n5. Вегетарианская\n6. Грибная пепперони\n7. Грибная\n8. Три сыра\n\nКакая пицца вас заинтересовала?'
sushi_menu='1. Ролл Хатамото\n2. Ролл с тигровой креветкой и лососем\n3. Ролл Сочная креветка\n4. Ролл Берри\n5. Ролл Калифорния в кунжуте\n6. Ролл Калифорния с креветкой\n\nКакие роллы вас заинтересовали?'


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
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu_menu)
        
    elif m.text == 'Акции':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert2) for advert2 in ['В разработке']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Акций к сожалению нет :(', reply_markup=keyboard)
    elif m.text == 'Поиск по ингредиентам': 
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Пицца', 'Суши']])
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert3) for advert3 in ['Салат']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что будем искать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, advert3)
    elif m.text == 'Расчёт калорий':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Выбрать категорию']])
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Выбрать блюдо']])
        keyboard.add(*[types.KeyboardButton(advert4) for advert4 in ['Рассчитать и вывести']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
    elif m.text == 'Корзина':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Оформить заказ']])
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Убрать некоторую еду из корзины']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
        
def advert3(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
        bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    if m.text == 'Пицца':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
   
def menu_menu(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
        bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    if m.text=='Еда':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Напитки':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Чай', 'Вода']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сок', 'Газировка']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drink_menu)

def eat_menu(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu_menu)
    if m.text=='Пицца':
        msg = bot.send_message(m.chat.id, pizza_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пепперони и томаты', 'Сырная']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Супер Мит', 'Морская с тунцом']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вегетарианская', 'Грибная пепперони']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Грибная', 'Три сыра']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.register_next_step_handler(msg, about_pizza)
    if m.text=='Суши':
        msg = bot.send_message(m.chat.id, sushi_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Хатамото', 'Ролл с тигровой креветкой и лососем']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Сочная креветка', 'Ролл Берри']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Калифорния в кунжуте', 'Ролл Калифорния с креветкой']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.register_next_step_handler(msg, about_sushi)


            
bot.polling(none_stop=True)
