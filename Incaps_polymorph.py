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

robot1 = Robot('Marvin', 1979, 0.2, 0.4)
robot2 = Robot('Caliban', 1993, -0.4, 0.3)
print(robot1.get_condition())
print(robot2.get_condition())