import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, sec):
        nx = self.x - sec.x
        ny = self.y - sec.y
        return math.sqrt(nx**2 + ny**2)

p = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))
q = Point(int(input("Enter value at x-axis: ")), int(input("Enter value at y-axis: ")))


print(p.distance(q))