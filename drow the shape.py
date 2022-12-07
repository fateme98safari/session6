import turtle
import time

n=3
line=3
go=80
p= turtle.Pen()
p.left(30)
for i in range(0,3):
 p.left(120)
 p.forward(80)
 i+=1
 
while line<=52:
    
    p.right((((n-2)*180)/n)/2)
    p.up()
    p.forward(20)
    p.down()
    n+=1
    p.left((180-(((n-2)*180)/n)) + ((((n-2)*180)/n)/2))
    p.forward(go+10)
    for j in range(1,n):
        p.left(180-(((n-2)*180)/n))
        p.forward(go+10)
    go+=10
line+=1

time.sleep(15)