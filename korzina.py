def shoplist(m):
    global num
    answer=''
    num=0
    if m.text=='Посмотреть заказ':
        #ну, здесь должен быть вывод заказа. Но поскольку корзины пока нет, будет пустое сообщение
         #количество еды в заказе
        if num=0:
            answer='Ваша корзина пуста'
        else:
            answer='В вашей корзине сейчас:/n/n'#ну и дальше выводится всё, что в корзине: наименование товара и его количество. В конце идёт общая сумма заказа
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
