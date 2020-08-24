class Round:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius**2*3.14

    def get_perimeter(self):
        return self.radius*2*3.14


circle = Round(6)
print(circle.get_area(), circle.get_perimeter())
