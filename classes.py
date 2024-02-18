from math import sqrt

class Triangle:
    def __init__(self, s1, s2, s3):
        self.a = s1
        self.b = s2
        self.c = s3
        
        if self.getArea() == 0:
            print('warning: not a valid triangle')

    def printSides(self):
        print(f'side 1: {self.a}')
        print(f'side 2: {self.b}')
        print(f'side 3: {self.c}')
    
    def getPerimeter(self):
        return self.a + self.b + self.c
    
    def getArea(self):
        s = (self.a + self.b + self.c) / 2
        area = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return round(area, 2)
    
    def getHeightGivenBase(self, base):
        area = self.getArea()
        height = (2 * area) / base
        return round(height, 2)
    

t = Triangle(6, 2, 5)
t.printSides()

# t1 = Triangle(5, 10, 15)

# print(f"perimeter: {t.getPerimeter()}")
print(f'area: {t.getArea()}')
print(f'height given base is s1: {t.getHeightGivenBase(t.a)}')


