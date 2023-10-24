import turtle
turtle = turtle.Turtle()
def jump(a):
    turtle.up()
    turtle.forward(a)
    turtle.down()
def qg(pixel):
    for _ in range(4):
        turtle.shape('square')
        turtle.color('silver')
        turtle.forward(pixel)
        turtle.right(90)
jump(30)
for _ in range(4):
    turtle.shape('circle')
    turtle.color('red')
    turtle.forward(50)
    turtle.right(90)
jump(-30)
for _ in range(4):
    turtle.shape('arrow')
    turtle.color('green')
    turtle.right(90)
    turtle.forward(50)
turtle.penup()
turtle.goto(0,-100)#fica debaixo do azul
turtle.pendown()
turtle.right(90)
for _ in range(4):
   turtle.shape('triangle')
   turtle.color('blue')
   turtle.forward(50)
   turtle.right(90)
turtle.penup()
turtle.goto(40,-100)#x=40 e y=-100
turtle.pendown()
turtle.right(90)
for _ in range(4):
   turtle.shape('turtle')
   turtle.color('yellow')
   turtle.left(90)
   turtle.forward(50)
turtle.penup()
turtle.goto(100,-155)
turtle.pendown()
qg(200)