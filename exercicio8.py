import turtle
import random

turtle = turtle.Turtle()

colors = ['purple', 'blue', 'yellow', 'green', 'pink', 'red', 'indigo']
for _ in range (10):
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(100)
    turtle.backward(100)
    turtle.right(45)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(55)