import turtle
tao = turtle.Pen()
tao.shape('circle')
def Flower():
    for i in range(20):
        tao.circle(60)
        tao.right(18)
        tao.fd(10)
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

Go(-100,-50)
Flower()
