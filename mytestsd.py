import telebot
from telebot import types
from database_sushi import roll_pic,roll,roll_names,roll_kkal,roll_cost
from database_pizza import pizza_pic,pizza,pizza_names,pizza_kkal,pizza_cost
from database_salat import salat_pic,salat,salat_names,salat_kkal,salat_cost
from database_girst import girst_pic,girst,girst_names,girst_kkal,girst_cost
from database_second import second_pic,second,second_names,second_kkal,second_cost
from database_drink import drink_pic,drink,drink_names,drink_kkal,drink_cost
from act import act_pic
from datetime import date
import pickle

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

today=date.today()
today=date(today.year, today.month, today.day).weekday()
cart=[]
cart_cost=[]
cart_kkal=[]
global h
h="/"
pizza_menu='1. Пепперони и томаты\n2. Сырная\n3. Супер Мит\n4. Морская с тунцом\n5. Вегетарианская\n6. Грибная пепперони\n7. Грибная\n8. Три сыра\n\nКакая пицца вас заинтересовала?'
sushi_menu='1. Ролл Хатамото\n2. Ролл с тигровой креветкой и лососем\n3. Ролл Сочная креветка\n4. Ролл Берри\n5. Ролл Калифорния в кунжуте\n6. Ролл Калифорния с креветкой\n\nКакие роллы вас заинтересовали?'
first_menu='1. Окрошка на кефире\n2. Рассольник Петербургский\n3. Суп "Харчо"\n4. Солянка домашняя\n5. Суп-лапша куриная домашняя\n\nКакое блюдо вас заинтересовало?'
second_menu='1. Лечо\n2. Кабачки в кляре\n3. Рулет омлет\n4. Поджарка из свинины\n5. Филе куриное запеченое в фольге\n\nКакое блюдо вас заинтересовало?'
salat_menu='1. Летний\n2. Овощной коктейль\n3. Винегрет\n4. Морковный\n5. Салат Столичный\n\nКакой салат вас заинтересовал?'
water_menu="1. Смузи персик клубника\n2. Кофе Фокс\n3. Сок J7\n4. Pepsi\n5.Вода бутилизованная питьевая газированная\n\nКакой напиток вас заинтересовал?"

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Вас приветствует чат-бот Dfg")
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
        msg = bot.send_message(m.chat.id, "Ищу акцию на сегодня...")        
        bot.send_photo(m.chat.id,photo=act_pic[today])
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
        bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)

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
        #print(cart)
        #print(cart_cost)
        #print(cart_kkal)
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Посмотреть заказ']])
        keyboard.add(*[types.KeyboardButton(advert5) for advert5 in ['Оформить заказ']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Что нужно сделать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, shoplist)
        
def advert3(m):
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
        bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)
    if m.text == 'Суши':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, find_roll)
    if m.text == 'Пицца':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, find_pizza)
    if m.text == 'Салат':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, find_salat)
    if m.text == 'Первое блюдо':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, find_girst)
    if m.text == 'Второе блюдо':
        msg = bot.send_message(m.chat.id, "Отлично")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Которые входят в состав']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Без этих ингредиентов']])
        m=bot.send_message(m.chat.id, 'Какие ингредиенты ищем?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, find_second)
   
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
        msg = bot.send_message(m.chat.id, water_menu)
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Смузи персик клубника', 'Кофе Фокс']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сок J7', 'Pepsi']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вода бутилизованная питьевая газированная']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Введите вручную либо нажмите на кнопку', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drink_menu)

def drink_menu(m):
    global h
    h=m.text
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Еда']])
        keyboard.add(*[types.KeyboardButton(advert1) for advert1 in ['Напитки']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        bot.send_message(m.chat.id, 'Еда или напитки?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, menu_menu)
    if m.text=='Смузи персик клубника':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=drink_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderD)
    if m.text=='Кофе Фокс':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=drink_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderD)
    if m.text=='Сок J7':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=drink_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderD)
    if m.text=='Pepsi':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=drink_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderD)
    if m.text=='Вода бутилизованная питьевая газированная':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=drink_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderD)

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
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Суп "Харчо"', 'Суп-лапша куриная домашняя']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Солянка домашняя']])
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


    


def about_pizza(m):
    global h
    h=m.text
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
    global h
    h=m.text
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
    global h
    h=m.text
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




def about_first(m):
    global h
    h=m.text
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Окрошка на кефире':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=girst_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderF)
    if m.text=='Рассольник Петербургский':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=girst_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderF)
    if m.text=='Суп "Харчо"':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=girst_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderF)
    if m.text=='Суп - лапша куриная домашняя':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=girst_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderF)
    if m.text=='Солянка домашняя':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=girst_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderF)



def about_second(m):
    global h
    h=m.text
    if m.text=='Назад':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пицца', 'Суши', 'Салат']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Первое блюдо', 'Второе блюдо']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, eat_menu)
    if m.text=='Лечо':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=second_pic[0])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSec)
    if m.text=='Кабачки в кляре':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=second_pic[1])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSec)
    if m.text=='Рулет омлет':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=second_pic[2])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSec)
    if m.text=='Поджарка из свинины':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=second_pic[3])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSec)
    if m.text=='Филе куриное запеченое в фольге':
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
        msg = bot.send_photo(m.chat.id,photo=second_pic[4])
        m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, make_orderSec)








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
    if m.text == "Да":
        global h
        for number1 in range(len(roll_names)):
                if h==roll_names[number1]:
                    cart.append(h)
                    cart_cost.append(roll_cost[number1])
                    cart_kkal.append(roll_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Хатамото', 'Ролл с тигровой креветкой и лососем']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Сочная креветка', 'Ролл Берри']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Ролл Калифорния в кунжуте', 'Ролл Калифорния с креветкой']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
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
    if m.text == "Да":
        global h
        for number1 in range(len(pizza_names)):
                if h==pizza_names[number1]:
                    cart.append(h)
                    cart_cost.append(pizza_cost[number1])
                    cart_kkal.append(pizza_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Пепперони и томаты', 'Сырная']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Супер Мит', 'Морская с тунцом']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вегетарианская', 'Грибная пепперони']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Грибная', 'Три сыра']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
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
    if m.text == "Да":
        global h
        for number1 in range(len(salat_names)):
                if h==salat_names[number1]:
                    cart.append(h)
                    cart_cost.append(salat_cost[number1])
                    cart_kkal.append(salat_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Летний', 'Овощной коктейль']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Винегрет', 'Морковный']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Салат Столичный']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_salat)
def make_orderF(m):
    if m.text=='Нет':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Окрошка на кефире', 'Рассольник Петербургский']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Суп "Харчо"', 'Суп-лапша куриная домашняя']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Солянка домашняя']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_first)
    if m.text == "Да":
        global h
        for number1 in range(len(girst_names)):
                if h==girst_names[number1]:
                    cart.append(h)
                    cart_cost.append(girst_cost[number1])
                    cart_kkal.append(girst_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Окрошка на кефире', 'Рассольник Петербургский']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Суп "Харчо"', 'Суп-лапша куриная домашняя']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Солянка домашняя']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_first)
def make_orderSec(m):
    if m.text=='Нет':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Лечо', 'Кабачки в кляре']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Рулет омлет', 'Поджарка из свинины']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Филе куриное запеченое в фольге']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_first)
    if m.text == "Да":
        global h
        for number1 in range(len(second_names)):
                if h==second_names[number1]:
                    cart.append(h)
                    cart_cost.append(second_cost[number1])
                    cart_kkal.append(second_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Лечо', 'Кабачки в кляре']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Рулет омлет', 'Поджарка из свинины']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Филе куриное запеченое в фольге']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, about_second)
def make_orderD(m):
    if m.text=='Нет':
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Смузи персик клубника', 'Кофе Фокс']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сок J7', 'Pepsi']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вода бутилизованная питьевая газированная']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drink_menu)
    if m.text == "Да":
        global h
        for number1 in range(len(drink_names)):
                if h==drink_names[number1]:
                    cart.append(h)
                    cart_cost.append(drink_cost[number1])
                    cart_kkal.append(drink_kkal[number1])
        msg = bot.send_message(m.chat.id, "Добавляю...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Смузи персик клубника', 'Кофе Фокс']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Сок J7', 'Pepsi']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вода бутилизованная питьевая газированная']])
        keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['Назад']])
        m=bot.send_message(m.chat.id, 'Что желаете заказать еще?', reply_markup=keyboard)
        bot.register_next_step_handler(msg, drink_menu) 


def find_roll(m):
    if m.text == "Которые входят в состав":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_cucumber)
    elif m.text == "Без этих ингредиентов":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_not_cucumber)         

def find_cucumber(m):
    pr=m.text
    for number1 in range(len(roll)):
       o=roll[number1]
       for number2 in range(len(o)):
            h=o[number2]
            if h==pr.lower():
                msg = bot.send_message(m.chat.id,roll_names[number1])
                msg = bot.send_photo(m.chat.id,photo=roll_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)
                
def find_not_cucumber(m):
    s=[0,0,0,0,0,0]

    pr=m.text
    for number1 in range(len(roll)):
            o=roll[number1]
            for number2 in range(len(o)):
                h=o[number2]  
                if h==pr.lower():
                    s[number1]=1
            
            if s[number1]==0:
               msg = bot.send_message(m.chat.id,roll_names[number1])
               msg = bot.send_photo(m.chat.id,photo=roll_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)



def find_pizza(m):
    if m.text == "Которые входят в состав":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_tomato)
    elif m.text == "Без этих ингредиентов":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_not_tomato)         

def find_tomato(m):
    pr=m.text
    for number1 in range(len(pizza)):
       o=pizza[number1]
       for number2 in range(len(o)):
            h=o[number2]
            if h==pr.lower():
                msg = bot.send_message(m.chat.id,pizza_names[number1])
                msg = bot.send_photo(m.chat.id,photo=pizza_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)
                
def find_not_tomato(m):
    s=[0,0,0,0,0,0,0,0]

    pr=m.text
    for number1 in range(len(pizza)):
            o=pizza[number1]
            for number2 in range(len(o)):
                h=o[number2]  
                if h==pr.lower():
                    s[number1]=1
            
            if s[number1]==0:
               msg = bot.send_message(m.chat.id,pizza_names[number1])
               msg = bot.send_photo(m.chat.id,photo=pizza_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)

def find_salat(m):
    if m.text == "Которые входят в состав":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_carrot)
    elif m.text == "Без этих ингредиентов":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_not_carrot)         

def find_carrot(m):
    pr=m.text
    for number1 in range(len(salat)):
       o=salat[number1]
       for number2 in range(len(o)):
            h=o[number2]
            if h==pr.lower():
                msg = bot.send_message(m.chat.id,salat_names[number1])
                msg = bot.send_photo(m.chat.id,photo=salat_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)
def find_not_carrot(m):
    s=[0,0,0,0,0]

    pr=m.text
    for number1 in range(len(salat)):
            o=salat[number1]
            for number2 in range(len(o)):
                h=o[number2]  
                if h==pr.lower():
                    s[number1]=1
            
            if s[number1]==0:
               msg = bot.send_message(m.chat.id,salat_names[number1])
               msg = bot.send_photo(m.chat.id,photo=salat_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)

def find_girst(m):
    if m.text == "Которые входят в состав":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_potato)
    elif m.text == "Без этих ингредиентов":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_not_potato)         

def find_potato(m):
    pr=m.text
    for number1 in range(len(girst)):
       o=girst[number1]
       for number2 in range(len(o)):
            h=o[number2]
            if h==pr.lower():
                msg = bot.send_message(m.chat.id,girst_names[number1])
                msg = bot.send_photo(m.chat.id,photo=girst_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)
def find_not_potato(m):
    s=[0,0,0,0,0]

    pr=m.text
    for number1 in range(len(girst)):
            o=girst[number1]
            for number2 in range(len(o)):
                h=o[number2]  
                if h==pr.lower():
                    s[number1]=1
            
            if s[number1]==0:
               msg = bot.send_message(m.chat.id,girst_names[number1])
               msg = bot.send_photo(m.chat.id,photo=girst_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)

def find_second(m):
    if m.text == "Которые входят в состав":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_meat)
    elif m.text == "Без этих ингредиентов":
        msg = bot.send_message(m.chat.id,"Введите ингредиент")
        bot.register_next_step_handler(msg, find_not_meat)         

def find_meat(m):
    pr=m.text
    for number1 in range(len(second)):
       o=second[number1]
       for number2 in range(len(o)):
            h=o[number2]
            if h==pr.lower():
                msg = bot.send_message(m.chat.id,second_names[number1])
                msg = bot.send_photo(m.chat.id,photo=second_pic[number1])
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)
def find_not_meat(m):
    s=[0,0,0,0,0]

    pr=m.text
    for number1 in range(len(second)):
            o=second[number1]
            for number2 in range(len(o)):
                h=o[number2]  
                if h==pr.lower():
                    s[number1]=1
            
            if s[number1]==0:
               msg = bot.send_message(m.chat.id,second_names[number1])
               msg = bot.send_photo(m.chat.id,photo=second_pic[number1])    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert0) for advert0 in ['В стартовое меню']])
    m=bot.send_message(m.chat.id, 'Вот что удалось найти', reply_markup=keyboard)
    bot.register_next_step_handler(msg, start)




def shoplist(m):
    msg = bot.send_message(m.chat.id, 'Корзина:')
    global num
    answer='В вашей корзине сейчас:/n/n'
    sum=0
    num=0
    if m.text=='Посмотреть заказ':
        #ну, здесь должен быть вывод заказа. Но поскольку корзины пока нет, будет пустое сообщение
         #количество еды в заказе
        m=bot.send_message(m.chat.id,"Название:")
        m=bot.send_message(m.chat.id,cart)
        m=bot.send_message(m.chat.id,"Стоимость:")
        m=bot.send_message(m.chat.id,cart_cost)
        m=bot.send_message(m.chat.id,"Калории:")
        m=bot.send_message(m.chat.id,cart_kkal)

        #if num==0:
            #answer='Ваша корзина пуста'
        #else:
        #ну и дальше выводится всё, что в корзине: наименование товара и его количество. В конце идёт общая сумма заказа
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Назад']])
        bot.register_next_step_handler(msg, name)
    if m.text=='Оформить заказ':
        if num!=0:
            msg = bot.send_message(m.chat.id, 'Выберете способ доставки')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Курьером']])
            keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Самовывоз']])
            bot.register_next_step_handler(msg, delivery)
        else:
            msg = bot.send_message(m.chat.id, 'Вы не можете оформить доставку, потому что ваша корзина пуста. Пожалуйста, добавьте сперва товары')
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Назад']])
            bot.register_next_step_handler(msg, name)
    if m.text == "Назад":
        msg = bot.send_message(m.chat.id, "Выполняю переход назад...")
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(name) for name in ['Меню', 'Акции']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Поиск по ингредиентам', 'Расчёт калорий']])
        keyboard.add(*[types.KeyboardButton(name) for name in ['Корзина']])
        bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
        bot.register_next_step_handler(msg, name)

def delivery(m):
    if m.text=='Курьером':
        msg = bot.send_message(m.chat.id, 'Ожидайте доставку в ближайшее время!')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вернуться в главное меню']])
        bot.register_next_step_handler(msg, start)
    if m.text=='Самовывоз':
        msg = bot.send_message(m.chat.id, 'Выберете место получения')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Место 1']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Место 2']])
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Место 3']])
        bot.register_next_step_handler(msg, delivery_end)
        
def delivery_end(m):
    if m.text=='Место 1':
        msg = bot.send_message(m.chat.id, 'Ваш заказ будет ожидать вас в месте вручения 1!')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вернуться в главное меню']])
        bot.register_next_step_handler(msg, start)
    if m.text=='Место 2':
        msg = bot.send_message(m.chat.id, 'Ваш заказ будет ожидать вас в месте вручения2!')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вернуться в главное меню']])
        bot.register_next_step_handler(msg, start)
    if m.text=='Место 3':
        msg = bot.send_message(m.chat.id, 'Ваш заказ будет ожидать вас в месте вручения 3!')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Вернуться в главное меню']])
        bot.register_next_step_handler(msg, start)
             
bot.polling(none_stop=True)
           
              
        
        

    


