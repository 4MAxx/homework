class Device():
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd

    def turn_on(self):
        print('Включаюсь...')

    def turn_off(self):
        print('Выключаюсь, до встречи!')

    def features(self, f):
        f1 = 'включаться, выключаться'
        print(f + f1)


class AnyDevice(Device):
    def __init__(self, type, cpu='-unknown-', ram='-unknown-', hdd='-unknown-'):
        self.type = type
        super().__init__(cpu, ram, hdd)

    def show_type(self):
        print(f'Я {self.type}')

    def turn_on(self):
        Device.turn_on(self)
        self.show_type()
        print(f'Мой процессор {self.cpu} Mhz, ОЗУ {self.ram} Гб, жесткий диск {self.hdd} Гб')

    def features(self, f='Я умею: '):
        f1 = 'показывать тип и характеристики, '
        super().features(f + f1)


class Notebook(AnyDevice):
    def __init__(self, cpu='-unknown-', ram='-unknown-', hdd='-unknown-'):
        super().__init__('Notebook', cpu, ram, hdd)

    def show_battery(self):
        import random
        print(f'Заряд батареи: {random.randint(0, 100)}%')

    def features(self, f='Я умею: '):
        f1 = 'показывать заряд батареи, '
        super().features(f + f1)


class Smartphone(AnyDevice):
    def __init__(self, cpu='-unknown-', ram='-unknown-', hdd='-unknown-'):
        super().__init__('Smartphone', cpu, ram, hdd)

    def call(self):
        n = input("введите номер для связи:")
        print(f'Набираю номер {n} ...')

    def features(self, f='Я умею: '):
        f1 = 'звонить, '
        super().features(f + f1)


# n = Notebook(cpu=2100,ram=4,hdd=512)
# n.turn_on()
# n.features()
# n.show_battery()
# print()
# s = Smartphone(ram=6)
# s.turn_on()
# s.features()
# s.turn_off()
# print()
# pc = AnyDevice(cpu=3100, type='PC')
# pc.show_type()
# pc.turn_on()
# pc.features()

class Car():
    def __init__(self, mark, model, gv, speed=0):
        self.mark = mark
        self.model = model
        self.gv = gv
        self.speed = speed

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.speed *= -1

    def show_speed(self):
        print(self.speed)


# car1 = Car('wv', 'passat b5', 1990)
# car1.speed_up()
# car1.speed_up()
# car1.speed_down()
# car1.stop()
# car1.show_speed()

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        print(f'Привет, меня зовут {self.name}')

    def say_age(self):
        print(f'Мне {self.age} лет')


class Doctor(Human):
    def __init__(self, name, age, spec='', stage=0, zp=0, place='', t='', qual='', post=''):
        super().__init__(name, age)
        self.spec = spec
        self.stage = stage
        self.zp = zp
        self.place = place
        self.teach = t
        self.qual = qual
        self.post = post

    def do(self):
        print('следую протоколу оказания мед. помощи')

    def work(self):
        print(f'я работаю в {self.place}, у меня стаж {self.stage}')


# max = Doctor('Max', 25, place='УЗ 6-я поликлиника')
# max.stage = 2
# max.say_name()
# max.work()
# max.do()
# max.say_age()
