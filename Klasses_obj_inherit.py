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

# s1 = Square()
# s1.draw()
# print(s1.calculate_area())
# s2 = Square(6)
# s2.draw()
# print(s2.calculate_area())

class Elevator:
    def __init__(self, kol=5, flor=3):
        self.kol = kol
        self.flor = flor

    def up(self):
        if self.flor < self.kol:
            self.flor += 1
            print(f'Лифт поднимается на {self.flor} этаж')
        elif self.flor == self.kol:
            print('Лифт не может подняться выше')

    def down(self):
        if self.flor > 1:
            self.flor -= 1
            print(f'Лифт опускается на {self.flor} этаж')
        elif self.flor == 1:
            print('Лифт не может опуститься ниже')

# elevator1 = Elevator(7, 5)
# elevator2 = Elevator()
# elevator1.up()
# elevator1.up()
# elevator1.up()
# elevator2.down()
# elevator2.down()
# elevator2.down()
# elevator2.down()

class NewElevator(Elevator):
    def __init__(self, kol, flor):
        super().__init__(kol, flor)

    def move(self, stage):
        if 1 <= stage <= self.kol:
            print(f'Лифт отправляется с {self.flor} на {stage} этаж')
            self.flor = stage
        else: print('Неправильный номер этажа')

elevator = NewElevator(10, 1)
elevator.move(10)
elevator.down()
elevator.up()
elevator.move(2)