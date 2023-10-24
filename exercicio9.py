import turtle
import random
turtle = turtle.Turtle()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'indigo']
for c in range(360):
    color = random.choice(colors)
    turtle.forward(3)
    turtle.color(color)
    turtle.right(1)