class Circle:
    def __init__(self, radius):
        self._radius = radius  # underscore denotes a private variable

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print("Initial radius:", circle.radius)
print("Area of the circle:", circle.area())

circle.radius = 7
print("New radius:", circle.radius)
print("Updated Area of the circle:", circle.area())
