#chika="цыпленок"
#papr="паприка"
#salat_a="салат айсберг"
#masago="масаго"
#kunjut="кунжут"
#sheff_s="шеф-соус"
#fish_l="лосось"
#shrimp_tig="кверетка тигровая"
#shrimp_sim="креветка обыч"
#cheese_s="сливочный сыр"
#avocado="авокадо"
#crab_c="краб-крем"
#cucumber="огурец"
#banan="банан"
#cherry="вишня"
#testo_h="тесто харумаки"
#sirop_cr="сироп клубничный"
#sirop_ch="сироп шоколадный"

roll_h=["цыпленок","паприка","салат айсберг","масаго","кунжут","шеф-соус"]
roll_tig=["лосось","кверетка тигровая","сливочный сыр","авокадо","масаго"]
roll_tas=["кверетка тигровая","краб-крем","огурец","сливочный сыр","масаго","шеф-соус"]
roll_ber=["банан","вишня","сливочный сыр","тесто харумаки","сироп клубничный","сироп шоколадный"]
roll_cal_cun=["краб-крем","огурец","шеф-соус","авокадо","кунжут"]
roll_cal_shr=["креветка обыч","огурец","шеф-соус","краб-крем","масаго"]

roll=[]
roll.append(roll_h)
roll.append(roll_tig)
roll.append(roll_tas)
roll.append(roll_ber)
roll.append(roll_cal_cun)
roll.append(roll_cal_shr)

roll_names=['Ролл Хатамато','Ролл с тигровой креветкой и лососем','Ролл Сочная креветка','Ролл Берри','Ролл Калифорния в кунжуте','Ролл Калифорния с креветкой']

sushi1 = open('sushi\sushi1.png','rb')
sushi2 = open('sushi\sushi2.png','rb')
sushi3 = open('sushi\sushi3.png','rb')
sushi4 = open('sushi\sushi4.png','rb')
sushi5 = open('sushi\sushi5.png','rb')
sushi6 = open('sushi\sushi6.png','rb')

roll_pic=[]
roll_pic.append(sushi1)
roll_pic.append(sushi2)
roll_pic.append(sushi3)
roll_pic.append(sushi4)
roll_pic.append(sushi5)
roll_pic.append(sushi6)



roll_h_cost=[199]
roll_tig_cost=[345]
roll_tas_cost=[255]
roll_ber_cost=[199]
roll_cal_cun_cost=[199]
roll_cal_shr_cost=[259]


roll_cost=[]
roll_cost.append(roll_h_cost)
roll_cost.append(roll_tig_cost)
roll_cost.append(roll_tas_cost)
roll_cost.append(roll_ber_cost)
roll_cost.append(roll_cal_cun_cost)
roll_cost.append(roll_cal_shr_cost)




roll_h_kkal=[0]
roll_tig_kkal=[0]
roll_tas_kkal=[0]
roll_ber_kkal=[0]
roll_cal_cun_kkal=[0]
roll_cal_shr_kkal=[0]


roll_kkal=[]
roll_kkal.append(roll_h_kkal)
roll_kkal.append(roll_tig_kkal)
roll_kkal.append(roll_tas_kkal)
roll_kkal.append(roll_ber_kkal)
roll_kkal.append(roll_cal_cun_kkal)
roll_kkal.append(roll_cal_shr_kkal)


