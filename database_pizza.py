#соус томатный
#сыр моцарелла
#пепперони
#томаты
#орегано
#базилик
#ветчина
#цыпленок
#бекон
#салями
#соус цезарь
#тунец
#шампиньоны
#перец зеленый болгарский
#хрустящий лучок
#маслины
#соус грибной
#креметте
#сыр пармезан
#соус сырный

pizza_pep=["соус томатный","сыр моцарелла","пепперони","томаты"]
pizza_cheese=["соус томатный","сыр моцарелла","орегано","базилик"]
pizza_super_meat=["соус томатный","ветчина","цыпленок","бекон","салями","пепперони","сыр моцарелла","томаты","орегано"]
pizza_sea=["соус цезарь","тунец","сыр моцарелла","томаты"]
pizza_veg=["шампиньоны","перец зеленый болгарский","хрустящий лучок","томаты","маслины","соус томатный","сыр моцарелла"]
pizza_mush_pep=["соус грибной","пепперони","шампиньоны","сыр моцарелла"]
pizza_mush_sim=["соус грибной","шампиньоны","сыр моцарелла"]
pizza_t_cheese=["соус томатный","креметте","сыр пармезан","соус сырный"]

pizza=[]
pizza.append(pizza_pep)
pizza.append(pizza_cheese)
pizza.append(pizza_super_meat)
pizza.append(pizza_sea)
pizza.append(pizza_veg)
pizza.append(pizza_mush_pep)
pizza.append(pizza_mush_sim)
pizza.append(pizza_t_cheese)

pizza_names=["Пепперони и томаты","Сырная","Супер Мит","Морская с тунцом","Вегетарианская","Грибная пепперони","Грибная","Три сыра"]

pizza1 = open('pizza\pizza1.png','rb')
pizza2 = open('pizza\pizza2.png','rb')
pizza3 = open('pizza\pizza3.png','rb')
pizza4 = open('pizza\pizza4.png','rb')
pizza5 = open('pizza\pizza5.png','rb')
pizza6 = open('pizza\pizza6.png','rb')
pizza7 = open('pizza\pizza7.png','rb')
pizza8 = open('pizza\pizza8.png','rb')

pizza_pic=[]
pizza_pic.append(pizza1)
pizza_pic.append(pizza2)
pizza_pic.append(pizza3)
pizza_pic.append(pizza4)
pizza_pic.append(pizza5)
pizza_pic.append(pizza6)
pizza_pic.append(pizza7)
pizza_pic.append(pizza8)




pizza_pep_cost=[245]
pizza_cheese_cost=[245]
pizza_super_meat_cost=[445]
pizza_sea_cost=[785]
pizza_veg_cost=[385]
pizza_mush_pep_cost=[245]
pizza_mush_sim_cost=[245]
pizza_t_cheese_cost=[385]

pizza_cost=[]
pizza_cost.append(pizza_pep_cost)
pizza_cost.append(pizza_cheese_cost)
pizza_cost.append(pizza_super_meat_cost)
pizza_cost.append(pizza_sea_cost)
pizza_cost.append(pizza_veg_cost)
pizza_cost.append(pizza_mush_pep_cost)
pizza_cost.append(pizza_mush_sim_cost)
pizza_cost.append(pizza_t_cheese_cost)



pizza_pep_kkal=[251.1]
pizza_cheese_kkal=[259.3]
pizza_super_meat_kkal=[219.8]
pizza_sea_kkal=[163.8]
pizza_veg_kkal=[181.5]
pizza_mush_pep_kkal=[271.1]
pizza_mush_sim_kkal=[249.1]
pizza_t_cheese_kkal=[237.6]

pizza_kkal=[]
pizza_kkal.append(pizza_pep_kkal)
pizza_kkal.append(pizza_cheese_kkal)
pizza_kkal.append(pizza_super_meat_kkal)
pizza_kkal.append(pizza_sea_kkal)
pizza_kkal.append(pizza_veg_kkal)
pizza_kkal.append(pizza_mush_pep_kkal)
pizza_kkal.append(pizza_mush_sim_kkal)
pizza_kkal.append(pizza_t_cheese_kkal)
