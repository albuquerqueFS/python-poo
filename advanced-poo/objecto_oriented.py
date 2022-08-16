class Student():
    
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa


stu1 = Student('Henrique', gpa=4.0)
stu2 = Student('Albuquerque', gpa=3.5)

print(stu1)

class Agent():
    origin = "USA"

    def __init__(self, name, height, weight) -> None:
        self.name = name
        self.height = height
        self.weight = weight

x = Agent('Jose', 6, 170)
print(x)