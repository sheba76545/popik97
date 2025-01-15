from turtle import *
tracer(0)
m = 25
pendown()
for i in range(4):
    fd(10 * m)
    rt(90)
penup()
fd(5 * m)
rt(90)
fd(2 * m)
pendown()
for i in range(4):
    fd(7 * m)
    rt(90)
penup()
fd(5 * m)
rt(90)
fd(2 * m)
pendown()
for i in range(4):
    fd(3 * m)
    rt(90)
    fd(10 * m)
    rt(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * m, y * m)
        dot(2,'red')

done()

