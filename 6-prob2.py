from turtle import*
m=10
tracer(0)
for i in range (10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
penup()
fd(m)
rt(90)
fd(m)
lt(90)
pendown()
for i in range (10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
penup()
for x in range(-40,40):
    for y in range(-40,40):
        setpos(x*m,y*m)
        dot(5,'red')





done()