import turtle
my_turtle = turtle.Turtle()
def square(length,angle):

    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

for item in range(6):
    square(100,90)
my_turtle.done()