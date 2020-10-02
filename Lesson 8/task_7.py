class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} + {self.y}j"

    def __add__(self, other):
        return f"{self.x + other.x} + {self.y + other.y}j"

    def __mul__(self, other):
        return f"{self.x * other.x - self.y * other.y} + {self.x * other.y + other.x * self.y}j"


num1 = ComplexNum(3, 5)
num2 = ComplexNum(4, 6)
print(num1 + num2)
print(num1 * num2)
