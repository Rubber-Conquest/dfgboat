from datetime import date


act_pic=[]

act1=open('day\one.jpg','rb')
act2=open('day\wo.jpg','rb')
act3=open('day\hree.jpg','rb')
act4=open('day\our.jpg','rb')
act5=open('day\ive.jpg','rb')
act6=open('day\six.jpg','rb')
act7=open('day\seven.jpg','rb')

act_pic.append(act1)
act_pic.append(act2)
act_pic.append(act3)
act_pic.append(act4)
act_pic.append(act5)
act_pic.append(act6)
act_pic.append(act7)

def today_act(today):
    return act_pic[today]
        
