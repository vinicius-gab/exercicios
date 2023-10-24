import turtle
import random
turtle.pensize(6)
turtle = turtle.Turtle()
colors = ['cyan', 'black', 'yellow']

for _ in [1, 2, 3]:
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(120)