class Uchenik:
    sum1 = 0
    def __init__(self, name, zel = 0, mag = 0, trav = 0, trans = 0):
        self.name = name
        self.zel = zel
        self.mag = mag
        self.trav = trav
        self.trans = trans

    def sum(self):
        self.sum1 = self.zel+self.mag+self.trav+self.trans
        return self.sum1


# potter = Uchenik(input('Введите имя ученика: '))
# potter.zel = int(input('Балл за "Зельеварение":'))
# potter.mag = int(input('Балл за "Историю магии":'))
# potter.trav = int(input('Балл за "Травологию":'))
# potter.trans = int(input('Балл за Трансфигурацию:'))
# print(f'Ученик:{potter.name}, сумма баллов за экзамен {potter.sum()}')

class GreatTalent():
    sex = 'male'
    education = 'unknown'
    def __init__(self, name, age, lang):
        from datetime import date
        self.name = name
        self.age = age
        self.year_of_birth = date.today().year - age
        self.fav_prog_lang = lang

    def show_data(self):
        print(f'name: {self.name}')
        print(f'sex: {self.sex}')
        print(f'age: {self.age}')
        print(f'year of birth: {self.year_of_birth}')
        print(f'favorite prog language: {self.fav_prog_lang}')
        print(f'education: {self.education}')


Max = GreatTalent('Max', 40, 'python')
Max.show_data()