# 11. Write a Python class named Circle constructed by a radius and two methods
# which will compute the area and the perimeter of a circle.


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius**2*3.14

    def get_perimeter(self):
        return self.radius*2*3.14


circle = Circle(6)
print(circle.get_area(), circle.get_perimeter())
