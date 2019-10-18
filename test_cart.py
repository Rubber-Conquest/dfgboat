import telebot
from telebot import types
from database_roll import roll,roll_names,roll_pic
from database_pizza import pizza_pic
global cart
cart=[]
global h
h="0"

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hello")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Ролл Хатамато', 'Ролл с тигровой креветкой и лососем']])
    bot.send_message(m.chat.id, 'Выберите нужный пункт меню', reply_markup=keyboard)
    bot.register_next_step_handler(msg, about_sushi)
    
def about_sushi(m):
 global h
 h=m.text
 if m.text=='Ролл Хатамато':
    
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
     keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
     msg = bot.send_photo(m.chat.id,photo=roll_pic[0])
     msg=bot.send_message(m.chat.id,h)
     m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
     bot.register_next_step_handler(msg, make_order)
     
 if m.text=='Ролл с тигровой креветкой и лососем':
    
     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
     keyboard.add(*[types.KeyboardButton(advert33) for advert33 in ['Да', 'Нет']])
     msg = bot.send_photo(m.chat.id,photo=roll_pic[0])
     msg=bot.send_message(m.chat.id,h)
     m=bot.send_message(m.chat.id, 'Добавить блюдо в корзину?', reply_markup=keyboard)
     bot.register_next_step_handler(msg, make_order)
        
 		
def make_order(m):
    if m.text=='Да':
        for number1 in range(len(roll_names)):
            o=roll_names[number1]
            if h==o:
                global cart
                cart.append(h)
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(advert34) for advert34 in ['Корзина','Назад']])
    msg=bot.send_message(m.chat.id,"Добавлено",reply_markup=keyboard)
    bot.register_next_step_handler(msg,cart_list) 
                
             
def cart_list(m):
    global cart
    if m.text=='Корзина':
        for number1 in range(len(cart)):
            msg=bot.send_message(m.chat.id,cart[number1])
    if m.text=='Назад':
        #здесь кнопку до выбора сделайте
        
    
        
            
        
               
bot.polling()
