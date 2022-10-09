
class Shape:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def type(self):
        print("Triangle")
    def Position(self):
        print("Left")

Shape_1 = Shape(30,40)
print(Shape_1.b)
print(Shape_1.Position())


class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        return " Talks Heavily."

Person_1 = Person("Enigin Ozturk")
print(Person_1.name +Person_1.talk())

class Model:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}.I work as a Turkish actor.")

engin = Model("Enigin Ozturk")
engin.talk()
burak = Model("Burak Deniz")
burak.talk()

