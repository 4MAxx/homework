class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, new_e):
        if  '@' in new_e and new_e.count('@') == 1 and  new_e.find('@') < new_e.find('.'):
            self.__email = new_e
        else: print('Ошибочная почта')


# k = UserMail('belosnezhka227', 'prince@wait.you')
# # print(k.get_email())
# k.set_email([1, 2, 3])
# k.set_email('prince@wait@.you')
# k.set_email('fafa@mail.ru')
# print(k.get_email())

class Robot:

    def __init__(self, name, year, psyh, fiz):
        self.name = name
        self.year = year
        self.__psyh = psyh
        self.__fiz = fiz
        self.__condition = psyh + fiz

    def get_condition(self):
        if self.__condition <= -1: return 'Я чувствую себя несчастным!'
        elif -1 < self.__condition <= 0: return 'Я чувствую себя плохо!'
        elif 0 < self.__condition <= 0.5: return 'Могло быть хуже!'
        elif 0.5 < self.__condition <= 1: return 'Кажется все в порядке!'
        else: return 'Супер!'

# robot1 = Robot('Marvin', 1979, 0.2, 0.4)
# robot2 = Robot('Caliban', 1993, -0.4, 0.3)
# print(robot1.get_condition())
# print(robot2.get_condition())

class Money:
    def __init__(self, dol, cnt):
        self.dollars = dol
        self.cents = cnt
        self.total_cents = dol * 100 + cnt

    def get_dollars(self):
        return self.dollars

    def set_dollars(self, s):
        if type(s) is int and s >= 0:
            self.total_cents = s * 100 + self.cents
        else: print('Error dollars')

    def get_cents(self):
        return self.cents

    def set_cents(self, c):
        if type(c) is int and 100 > c >= 0:
            self.total_cents = self.dollars * 100 + c
            self.cents = c
        else: print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.get_dollars()} долларов {self.get_cents()} центов'

# cash = Money(34, 77)
# print(cash.get_dollars())
# cash.set_dollars('hello')
# cash.set_dollars(-45)
# cash.set_dollars(78.8)
# print(cash.get_cents())
# cash.set_cents('hello')
# cash.set_cents(455)
# cash.set_cents(9)
# print(cash)

class Player:
    def __init__(self, nik):
        self.nik = nik
        self.role = 0
        self.color = ''

    def set_color(self):
        print('Выберите цвет: ', end='')
        if len(colors) != 0:
            for i in colors:
                print(i, end=' ')
            print()
            import random
            self.color = colors.pop(random.randint(0, len(colors)-1))
            print(f'Введите цвет: {self.color}')
            return f'Выбран цвет {self.color}\n'
        else: return 'Цвет не может быть назначен! Очередь уже заполнена :('


colors = ['red', 'green', 'blue']

player1 = Player('Alice558')
player2 = Player('Mike557')
player3 = Player('LonelyMan556')
player4 = Player('LonelyMan557')

print(player1.set_color())
print(player2.set_color())
print(player3.set_color())
print(player4.set_color())