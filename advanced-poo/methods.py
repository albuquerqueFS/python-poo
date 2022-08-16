class Circle():
    pi = 3.14

    def __init__(self, radius=1) -> None:
        self.radius = radius

    def area(self) -> float:
        return self.radius * self.radius * self.pi

    def perimeter(self) -> float:
        return 2 * self.radius * self.pi

    def multiply_radius(self, number) -> float:
        self.radius = self.radius * number
        print(f'Radius has been doubled to {self.radius}')

c = Circle(radius=4)
print(c.area())
print(c.perimeter())
print(c.multiply_radius(2))