# import turtle
#
# star = turtle.Turtle()
#
# for i in range(5):
#     star.forward(50)
#     star.right(144)
#
# turtle.done()

import turtle

spiral = turtle.Turtle()

for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()

# import turtle
# spiral = turtle.Turtle()
#
# for i in range(20):
#     spiral.forward(i * i)
#     spiral.right(144)
#
#
# turtle.done()