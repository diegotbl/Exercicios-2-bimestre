import sys

class Car(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        print(self.name + " is " + self.color)

class CarDecorator(Car):
    def __init__(self, car):
        self._car = car

    # def __getattr__():
    #     return getattr(self._car, name)

    def __str__(self):
         color = self._car.color
         self._car.__str__()
         if color == "red":
             print("\tI don't like red cars")
         elif color == "blue":
             print("\tI like blue cars")
         print()

def main():
    Car1 = CarDecorator(Car("Ferrari", "red"))
    Car2 = CarDecorator(Car("Porsche", "gray"))
    Car3 = CarDecorator(Car("BMW", "blue"))

    Car1.__str__()
    Car2.__str__()
    Car3.__str__()

if __name__ == '__main__':
    main()
