import csv
class Zad_1:
    name1 = 'zad1_in.csv'
    name2 = 'zad1_out.txt'

    @staticmethod
    def write(row):
        with open(Zad_1.name1, 'a') as file:
            wr = csv.writer(file, lineterminator='\r')
            wr.writerow(row)

    def out(self):
        print('Производится запись отчета...')
        groups = ['', '1-12', '13-18', '19-25', '26-40', '40+']
        data = [0, 0, 0, 0, 0, 0]
        with open(Zad_1.name1, 'r') as f_read:
            fr = csv.reader(f_read, delimiter = ",")
            for row in fr:
                if 1 <= int(row[2]) <= 12: data[1] += 1
                elif 13 <= int(row[2]) <= 18: data[2] += 1
                elif 19 <= int(row[2]) <= 25: data[3] += 1
                elif 26 <= int(row[2]) <= 40: data[4] += 1
                elif 40 < int(row[2]): data[5] += 1
        with open(Zad_1.name2, 'w', encoding='utf-8') as f_write:
            f_write.write('Возрастные группы:\n')
            for i in range(1, len(data)):
                f_write.write(f'{groups[i]}: {data[i]}'+'\n')
        import time
        time.sleep(1)


def zapolnenie():
    print('Введите данные через пробел: Имя Фамилия Возраст')
    Zad_1.write(input().split(' '))

def otchet():
    z = Zad_1()
    z.out()

def vivod_o():
    print("\n" * 100)
    with open(Zad_1.name2, 'r', encoding='utf-8') as f_read:
        for i in f_read:
            print(i, end='')
    input('Нажмите любую клавишу для продолжения...')

def vivod_d():
    print("\n" * 100)
    with open(Zad_1.name1, 'r', encoding='utf-8') as f_read:
        for i in f_read:
            print(i, end='')
    input('Нажмите любую клавишу для продолжения...')

n = 1
menu = ['', 'Заполнить данные', 'Создать отчет', 'Печать отчета на экран', 'Вывод данных на экран', 'Выход']
menu_func = {1:zapolnenie, 2:otchet, 3:vivod_o, 4:vivod_d}
while n != 5:
    print("\n" * 100)
    for i in range(1,len(menu)):
        print(f'{i} - {menu[i]}')
    n = int(input('Введите вариант:'))
    if n == 5: break
    elif n < 1 or n > 5: continue
    print("\n" * 100)
    menu_func.get(n)()
