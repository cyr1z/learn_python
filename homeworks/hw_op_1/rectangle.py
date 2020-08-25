# 10. Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_rectangle = Rectangle(10, 12)
print(my_rectangle.area())
