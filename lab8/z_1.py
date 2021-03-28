
filename = open('st.txt', 'r', encoding='utf8')
data = filename.read().split('\n')
filename.close()

lst = []
for i in data:
    lst.append(i.split())


def request(lst_):
    family = input("Введите фамилию: ")
    k = 0
    for line in lst_:
        line[2] = [int(item) for item in line[2]]
        rating = sum(line[2]) / len(line[2])
        line.append(rating)
        second_name, first_name, grades, rating = line
        if second_name.lower() == family.lower():
            print("Такая фамилия есть!")
            print("Фамилия: ", second_name)
            print("Инициалы: ", first_name)
            print("Оценки: ", grades)
            print("Средний балл: ", rating)
            k = 1
    if k == 0:
        print("Такого студента нет!")
    return lst_


def sort_ball(list_):
    new_lst = sorted(list_, key=lambda x: x[3], reverse=True)
    return new_lst


def request_data(lst_):
    for line in lst_:
        second_name, first_name, grades, rating = line
        if rating >= 4.5:           # а
            print("а: \n", line)
        if rating >= 4:             # б
            print("б: \n", line)
        if grades.count(2) >= 1:    # в
            print("в: \n", line)
        if grades.count(2) == 0 and (grades.count(3) == 0):     # г
            print("г: \n", line)
        if rating < 4:              # д
            print("д: \n", line)
        if grades.count(2) == 0 and (rating < 4):   # е
            print("е: \n", line)
        if grades.count(2) > 1:     # ж
            print("ж: \n", line)
        if grades.count(5) >= 2:    # з
            print("з: \n", line)
        if grades.count(2) <= 1:    # и
            print("и: \n", line)
        if grades.count(2) > 2:     # к
            print("к: \n", line)
        if grades.count(4) == 1 and (grades.count(5) == 4):     # л
            print("л: \n", line)
