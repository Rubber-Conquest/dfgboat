import telebot
from telebot import types
from database import roll,roll_names,roll_pic

bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")

@bot.message_handler(commands=["start"])
def start(m):
    msg = bot.send_message(m.chat.id, "Hello")
    
@bot.message_handler(content_types=['text'])    
def search(m):
    for number1 in range(len(roll)):
        o=roll[number1]
        for number2 in range(len(o)):
            h=o[number2]
            if h==m.text:
                msg = bot.send_message(m.chat.id,roll_names[number1])
                msg = bot.send_photo(m.chat.id,photo=roll_pic[number1])
                
    
bot.polling()
