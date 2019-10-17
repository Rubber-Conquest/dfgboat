import telebot
answer="-_-"
bot = telebot.TeleBot("944485905:AAHrw7jtHjnAVxqU7GsPS_xrhPPO6fUdiqU")
keymenu1 = telebot.types.ReplyKeyboardMarkup(False,True)
keymenu1.row('mushroom','cheese')
keymenu1.row('meat')
keymenu1.row('tomato','green')

@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text=="Поиск":
       bot.send_message(message.chat.id,answer,reply_markup=keymenu1)

bot.polling()
