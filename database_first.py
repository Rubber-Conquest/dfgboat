#картофель отв
#огурец свежий
#редис
#яйцо отварное
#колбаса вареная  
#кефир
#минеральная вода
#майонез

#бульон говяжий
#картофель свежий
#огурцы соленые
#лук репчатый свежий
#морковь столовая свежая
#крупа перловая
#масло растительное
#пряности

#говядина
#рис
#соус ткемали
#томатная паста
#сахар
#масло растительное
#соль 
#пряности

#бульон куриный
#мясо кур 
#макаронные изделия 
#томаты очищенные
#чеснок
 
#свинина
#вода
#молоко сухое
#грудинка копченая


 
first_okr_kef=["картофель отв","огурец свежий","редис","яйцо отварное","колбаса вар","кефир","минеральная вода","майонез"]
first_ras_peter=["бульон говяжий","картофель свежий","огурцы соленые","лук репчатый свежий","морковь столовая свежая","крупа перловая","масло растительное","пряности"]
first_harcho=["бульон говяжий","лук репчатый свежий","говядина","рис","соус ткемали","томатная паста","сахар","масло растительное","соль","пряности"]
first_lapsha=["бульон куриный","мясо кур","макаронные изделия","томаты очищенные","морковь столовая свежая","лук репчатый свежий","масло растительно","чеснок","соль","пряности"]
first_sol_dom=["бульон говяжий","картофель свежий","колбаса вареная","лук репчатый свежий","грудинка копченая","огурцы соленые","свинина","томатная паста","масло растительное"]

first=[]
first.append(first_okr_kef)
first.append(first_ras_peter)
first.append(first_harcho)
first.append(first_lapsha)
first.append(first_sol_dom)

first_name=["Окрошка на кефире","Рассольник Петербургский","Суп 'Харчо'","Суп - лапша куриная домашняя","Солянка домашняя"]

first1=open('first\first1.png','rb')
first2=open('first\first2.png','rb')
first3=open('first\first3.png','rb')
first4=open('first\first4.png','rb')
first5=open('first\first5.png','rb')

first_pic=[]
first_pic.append(first1)
first_pic.append(first2)
first_pic.append(first3)
first_pic.append(first4)
first_pic.append(first5)




first_okr_kef_cost=[135]
first_ras_peter_cost=[104]
first_harcho_cost=[125]
first_lapsha_cost=[119]
first_sol_dom_cost=[141]

first_cost=[]
first_cost.append(first_okr_kef_cost)
first_cost.append(first_ras_peter_cost)
first_cost.append(first_harcho_cost)
first_cost.append(first_lapsha_cost)
first_cost.append(first_sol_dom_cost)



first_okr_kef_kkal=[141]
first_ras_peter_kkal=[121.2]
first_harcho_kkal=[345]
first_lapsha_kkal=[255]
first_sol_dom_kkal=[105]

first_kkal=[]
first_kkal.append(first_okr_kef_kkal)
first_kkal.append(first_ras_peter_kkal)
first_kkal.append(first_harcho_kkal)
first_kkal.append(first_lapsha_kkal)
first_kkal.append(first_sol_dom_kkal)
