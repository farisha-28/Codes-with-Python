import turtle

painter = turtle.Turtle()

painter.pencolor("blue")

for i in range(40):
    painter.forward(50)
    painter.left(125) # Let's go counterclockwise this time

painter.pencolor("red")
for i in range(40):
    painter.forward(100)
    painter.left(125)

turtle.done()