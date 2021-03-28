import pickle
import random

filename = 'z_2.dat'

with open(filename, 'wb') as fl:
    lst = [
        # Фамилия и Иниц.   Дата рождения Должность         Стаж    Оклад
        ['Огурцов Д.И.',    '12.05.1999', 'Директор',       22,     250000],
        ['Должников И.В.',  '29.06.1997', 'Заместитель',    12,     115000],
        ['Иванов Г.Д.',     '14.02.1998', 'Работник',       9,      59000],
    ]
    pickle.dump(lst, fl)

with open(filename, 'rb') as fl:
    lst_ = pickle.load(fl)
    print("Начальный список: ")
    for i in lst_:
        print("||Фамилия, иницалы ", str(i[0]), "\n",
              "||Год рождения ", str(i[1]), "\n",
              "||Должность ", str(i[2]), "\n",
              "||Стаж ", str(i[3]), "\n",
              "||Оклад ", str(i[4]))

with open(filename, 'wb') as fl:
    for i in lst_:
        i.append(random.randint(100000, 300000))
    for i in lst_:
        if i[3] > 10:
            i[4] = i[4] + ((i[5] * 10) / 100)
        elif i[3] > 20:
            i[4] = i[4] + ((i[5] * 15) / 100)
    pickle.dump(lst_, fl)

with open(filename, 'rb') as fl:
    lst_ = pickle.load(fl)
    print("\nКонечный список: ")
    for i in lst_:
        print("||Фамилия, иницалы ", str(i[0]), "\n",
              "||Год рождения ", str(i[1]), "\n",
              "||Должность ", str(i[2]), "\n",
              "||Стаж ", str(i[3]), "\n",
              "||Оклад ", str(i[4]), "\n",
              "||Зарплата ", str(i[5]))
