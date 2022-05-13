class Matter:
    number = 0
    law = 'not defined'

    @staticmethod
    def out():
        print(f'я вселенная номер «{Matter.number}», я имею закон «{Matter.law}»')

    def set_number(self, num):
        Matter.number = num

    def set_law(self, law):
        Matter.law = law

# komet = Matter()
# Matter.out()
# komet.set_number(5)
# komet.set_law('bernulli')
# komet.out()
# Matter.out()

class Human(Matter):
    # атрибуты класса
    count = 0
    sex = 'unknown'
    lang = 'unknown'
    planet = 'Earth'

    # 3 атрибута экземпляра, 1 закрытый атрибут экземпляра
    def __init__(self, name, age, sex=sex, edu='unknown'):
        self.__name = name
        self.age = age
        self.sex = sex
        self.edu = edu
        Human.count += 1

    # сетер и гетер для закрытого атрибута экземпляра
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # один метод класса, который позволяет создать экземпляр класса через
    # другое значение одного из атрибутов
    @classmethod
    def create(cls, name, year):
        from datetime import date
        return cls(name, (date.today().year - year))

    # 3 метода экзепляра класса, в которых используются атрибуты экземпляров класса и атрибуты  класса
    def show_data(self):
        print('---------')
        print(f'My name is {self.get_name()}, sex is {self.sex}')
        print(f'I`am {self.age} years old, my education is {self.edu}')
        print(f'My language is: {self.lang}')
        print(f'I`am from planet {Human.planet}')

    # 2 статических метода, в которых используются атрибуты
    @staticmethod
    def change_human_sex(s):
        Human.sex = s

    @staticmethod
    def show_lang():
        print(Human.lang)


vasya = Human.create('Vasya', 1982)
print(vasya.get_name(), vasya.age)
petr = Human('Petya', 22, 'male')
print(petr.get_name(), petr.age)
vasya.lang = 'english'
petr.show_data()
vasya.show_data()
vasya.change_human_sex('it')
print(Human.sex, petr.sex, vasya.sex)
print(vasya.lang)
vasya.show_lang()
