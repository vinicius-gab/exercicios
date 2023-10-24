import turtle
turtle = turtle.Turtle()
turtle.shape("turtle")
turtle.color('blue')
turtle.pensize(4)

for color in ['pink', 'purple', 'blue', 'green']:
    turtle.color(color)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)