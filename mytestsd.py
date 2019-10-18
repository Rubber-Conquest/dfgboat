import telebot
from telebot import types
from database_sushi import roll_pic
from database_pizza import pizza_pic
from database_salat import salat_pic

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

pizza_menu='1. Пепперони и томаты\n2. Сырная\n3. Супер Мит\n4. Морская с тунцом\n5. Вегетарианская\n6. Грибная пепперони\n7. Грибная\n8. Три сыра\n\nКакая пицца вас заинтересовала?'
sushi_menu='1. Ролл Хатамото\n2. Ролл с тигровой креветкой и лососем\n3. Ролл Сочная креветка\n4. Ролл Берри\n5. Ролл Калифорния в кунжуте\n6. Ролл Калифорния с креветкой\n\nКакие роллы вас заинтересовали?'
first_menu='1. Окрошка на кефире\n2. Рассольник Петербургский\n3. Суп "Харчо"\n4. Солянка домашняя\n5. Суп-лапша куриная домашняя\n\nКакое блюдо вас заинтересовало?'
second_menu='1. Лечо\n2. Кабачки в кляре\n3. Рулет омлет\n4. Поджарка из свинины\n5. Филе куриное запеченое в фольге\n\nКакое блюдо вас заинтересовало?'
salat_menu='1. Летний\n2. Овощной коктейль\n3. Винегрет\n4. Морковный\n5. Салат Столичный\n\nКакой салат вас заинтересовал?'

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
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Чай', 'Кофе']])
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
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_pizza)
    if m.text=='Суши':
        msg = bot.send_message(m.chat.id, sushi_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Хатамото', 'Ролл с тигровой креветкой и лососем']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Сочная креветка', 'Ролл Берри']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Калифорния в кунжуте', 'Ролл Калифорния с креветкой']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_sushi)
    if m.text=='Салат':
        msg = bot.send_message(m.chat.id, salat_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Летний', 'Овощной коктейль']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Винегрет', 'Морковный']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Салат Столичный']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_salat)
        
    if m.text=='Первое блюдо':
        msg = bot.send_message(m.chat.id, first_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Окрошка на кефире', 'Рассольник Петербургский']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Суп "Харчо"', 'Солянка домашняя']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Суп-лапша куриная домашняя']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_first)
    if m.text=='Второе блюдо':
        msg = bot.send_message(m.chat.id, second_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Лечо', 'Кабачки в кляре']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Рулет омлет', 'Поджарка из свинины']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Филе куриное запеченое в фольге']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_second)


def drink_menu(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu_menu)
    


def about_pizza(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Пепперони и томаты':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Сырная':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Супер Мит':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Морская с тунцом':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Вегетарианская':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Грибная пепперони':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[5])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Грибная':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[6])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
    if m.text=='Три сыра':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=pizza_pic[7])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderP)
       
def about_sushi(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Ролл Хатамото':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)
    if m.text=='Ролл с тигровой креветкой и лососем':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)
    if m.text=='Ролл Сочная креветка':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)
    if m.text=='Ролл Берри':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)
    if m.text=='Ролл Калифорния в кунжуте':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)
    if m.text=='Ролл Калифорния с креветкой':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=roll_pic[5])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderS)



def about_salat(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Летний':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=salat_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSal)
    if m.text=='Овощной коктейль':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=salat_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSal)
    if m.text=='Винегрет':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=salat_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSal)
    if m.text=='Морковный':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=salat_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSal)
    if m.text=='Салат Столичный':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=salat_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSal)




def make_orderS(m):
    if m.text=='Нет':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Хатамото', 'Ролл с тигровой креветкой и лососем']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Сочная креветка', 'Ролл Берри']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Калифорния в кунжуте', 'Ролл Калифорния с креветкой']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
def make_orderP(m):
    if m.text=="Нет": 
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пепперони и томаты', 'Сырная']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Супер Мит', 'Морская с тунцом']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вегетарианская', 'Грибная пепперони']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Грибная', 'Три сыра']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_pizza)
def make_orderSal(m):
    if m.text=='Нет':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Летний', 'Овощной коктейль']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Винегрет', 'Морковный']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Салат Столичный']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_salat)           
bot.polling(none_stop=True)
