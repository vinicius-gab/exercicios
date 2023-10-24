import turtle
turtle = turtle.Turtle()
turtle.color('cyan')
turtle.shape("turtle")
turtle.goto(50,0)
for _ in [1, 2, 3]:
    turtle.forward(90)
    turtle.right(120)
turtle.shape("arrow")
turtle.color('purple')
turtle.home()
for _ in [1, 2, 3, 4]:
  turtle.forward(200)
  turtle.right(90)