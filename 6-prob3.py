from turtle import *
m = 35
tracer(0)
for i in range(9):
    fd(5*m)
    rt(50)
    fd(10*m)
    rt(130)
penup()
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*m,y*m)
        dot(2,'red')








done()