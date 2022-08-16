class Circle():
    pi = 3.14

    def __init__(self, radius=1) -> None:
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

c = Circle(radius=4)
print(c.area())