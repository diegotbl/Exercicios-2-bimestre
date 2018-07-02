class Area(object):
    def size(self, x, y):
        print("The area of the rectangle is " + str(x*y) + "")

class Perimeter(object):
    def size(self, x, y):
        print("The perimeter of the rectangle is " + str(2*(x+y)))

class Rect(object):
    def __init__(self, x, y, area_or_perimeter):
        self._x = x
        self._y = y
        self._area_or_perimeter = area_or_perimeter

    def size(self):
        self._area_or_perimeter.size(self._x, self._y)

def main():
    Rect1 = Rect(5, 3, Area())
    Rect2 = Rect(2, 8, Perimeter())

    print("1:")
    Rect1.size()
    print("\n2:")
    Rect2.size()

if __name__ == '__main__':
    main()
