import telebot
answer1="><"
k="keymenu"
bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")
global p

    
keymenu1 = telebot.types.ReplyKeyboardMarkup(False,True)
keymenu2 = telebot.types.ReplyKeyboardMarkup(False,True)
keymenu3 = telebot.types.ReplyKeyboardMarkup(False,True)
keymenu1.row('Меню','Акции')
keymenu1.row('Поиск по ингридиентам','Расчет каллорий')
keymenu1.row('Корзина','Заказать')
keymenu1.row('НИ ШАГУ НАЗАД')
keymenu2.row('Еда')
keymenu2.row('Не еда')
keymenu2.row('НИ ШАГУ НАЗАД')

#keymenu = telebot.types.InlineKeyboardMarkup()
#key1=telebot.types.InlineKeyboardButton(text='Меню',callback_data="")
#key2=telebot.types.InlineKeyboardButton(text='Акции',callback_data="")
#key3=telebot.types.InlineKeyboardButton(text='Поиск по ингридиентам',callback_data="")
#key4=telebot.types.InlineKeyboardButton(text='Расчет каллорий',callback_data="")
#key5=telebot.types.InlineKeyboardButton(text='Корзна',callback_data="")
#key6=telebot.types.InlineKeyboardButton(text='Заказать',callback_data="")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#	bot.reply_to(message, message.text)

#@bot.message_handler(content_types=['text'])
#def send_message(message):
#        bot.send_message(message.chat.id,answer1,reply_markup=keyboard1)
      
@bot.message_handler(content_types=['text'])
def send_menu(message):
    p=1
    if message.text=="Notice me":
        o=k+str(p)
        p=p+1
        bot.send_message(message.chat.id,answer1,reply_markup=o)
    elif message.text=="Меню":
        o=k+str(p)
        p=p+1
        bot.send_message(message.chat.id,answer1,reply_markup=o)
    elif message.text=="НИ ШАГУ НАЗАД":
        o=k+str(p)
        p=p-1
        bot.send_message(message.chat.id,answer1,reply_markup=o)
    
        

bot.polling()

