def create_list():
    first_list = []
    message = 'да'
    while message.lower() == 'да':
        print("Введите название: ")
        name = input()
        print("Введите цену: ")
        price = input()
        print("Введите его диагональ: ")
        diag = input()
        for i in first_list:
            i.append(name, price, diag)
        message = input("Хотите продолжить?\n->Да\t\n->Нет\n")
    return first_list


def edit_list(list_):
    new_list = []
    for i in list_:
        if i[1] <= 160000:
            new_list.append(i)
    return new_list
