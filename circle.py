import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)
