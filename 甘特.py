import pygame as py
import pandas as  pd

df=pd.read_excel('./DF_BT.xlsx')
def fx(x):
    tm=None    
    if 'day' in x:
        lt=x.split('day')
        tm=float(lt[0])*8*6      
    else:
        lt=x.split('mins')
        tm=float(lt[0])/10
    return tm
        
df['get_time']=df['time'].map(fx)

print(df)
long=len(df)

#初始化
py.init()

#窗口长宽设置
l=1250
w=600
wd=py.display.set_mode([l,w])
py.display.set_caption('签约到发货流程')
bkgrd=(220,255,255)
wd.fill(bkgrd)
font = py.font.SysFont('Simsun', 10)

font1 = py.font.SysFont('Simsun', 40)
title=font1.render('签约到发货流程',True, (0, 0, 0))
wd.blit(title,py.Rect(500,10,10,40))



ww=80
sum_long=5


for i in range(0,long):

        tx=df.loc[i,'task']   
        cd=df.loc[i,'get_time']
        zfc=df.loc[i,'time']
        text = font.render((str(tx)+'('+str(zfc)+' '+df.loc[i,'resource']+')'),True, (0, 0, 0))
        zb=py.Rect(sum_long,ww,cd,20)
        py.draw.rect(wd,(244, 100, 100),(zb))
        ww=ww+25
        sum_long=sum_long+cd
        wd.blit(text,py.Rect(sum_long,ww-22,cd,20))
 
py.display.flip()
py.image.save(wd, "甘特图.png")
py.quit()
