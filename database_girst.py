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


 
girst_okr_kef=["картофель отв","огурец свежий","редис","яйцо отварное","колбаса вар","кефир","минеральная вода","майонез"]
girst_ras_peter=["бульон говяжий","картофель свежий","огурцы соленые","лук репчатый свежий","морковь столовая свежая","крупа перловая","масло растительное","пряности"]
girst_harcho=["бульон говяжий","лук репчатый свежий","говядина","рис","соус ткемали","томатная паста","сахар","масло растительное","соль","пряности"]
girst_lapsha=["бульон куриный","мясо кур","макаронные изделия","томаты очищенные","морковь столовая свежая","лук репчатый свежий","масло растительно","чеснок","соль","пряности"]
girst_sol_dom=["бульон говяжий","картофель свежий","колбаса вареная","лук репчатый свежий","грудинка копченая","огурцы соленые","свинина","томатная паста","масло растительное"]

girst=[]
girst.append(girst_okr_kef)
girst.append(girst_ras_peter)
girst.append(girst_harcho)
girst.append(girst_lapsha)
girst.append(girst_sol_dom)

girst_names=["Окрошка на кефире","Рассольник Петербургский","Суп 'Харчо'","Суп - лапша куриная домашняя","Солянка домашняя"]


girst1=open('girst\girst1.png','rb')
girst2=open('girst\girst2.png','rb')
girst3=open('girst\girst3.png','rb')
girst4=open('girst\girst4.png','rb')
girst5=open('girst\girst5.png','rb')

girst_pic=[]

girst_pic.append(girst1)
girst_pic.append(girst2)
girst_pic.append(girst3)
girst_pic.append(girst4)
girst_pic.append(girst5)


girst_okr_kef_cost=[135]
girst_ras_peter_cost=[104]
girst_harcho_cost=[125]
girst_lapsha_cost=[119]
girst_sol_dom_cost=[141]

girst_cost=[]
girst_cost.append(girst_okr_kef_cost)
girst_cost.append(girst_ras_peter_cost)
girst_cost.append(girst_harcho_cost)
girst_cost.append(girst_lapsha_cost)
girst_cost.append(girst_sol_dom_cost)



girst_okr_kef_kkal=[141]
girst_ras_peter_kkal=[121.2]
girst_harcho_kkal=[345]
girst_lapsha_kkal=[255]
girst_sol_dom_kkal=[105]

girst_kkal=[]
girst_kkal.append(girst_okr_kef_kkal)
girst_kkal.append(girst_ras_peter_kkal)
girst_kkal.append(girst_harcho_kkal)
girst_kkal.append(girst_lapsha_kkal)
girst_kkal.append(girst_sol_dom_kkal)
