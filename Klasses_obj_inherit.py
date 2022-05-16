class Rectangle:
    def __init__(self, length=10, width=5):
        self.length = length
        self.width = width

    def calculate_area(self):
        return f'Площадь: {self.length * self.width}'

    def draw(self):
        for i in range(1, self.width + 1):
            for n in range(1, self.length + 1):
                print('*', end='')
            print(end='\n')

# r1 = Rectangle()
# r2 = Rectangle(5, 3)
# print(r1.calculate_area())
# print(r2.calculate_area())
# r1.draw()
# r2.draw()

class Square(Rectangle):
    def __init__(self, length=3):
        super().__init__(length, length)

s1 = Square()
s1.draw()
print(s1.calculate_area())
s2 = Square(6)
s2.draw()
print(s2.calculate_area())