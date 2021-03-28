"""
first_list = [
    # Название          Цена    Диагональ
    ['ASUS ROG',        150000, 28.2],
    ['Samsung 24PIB',   100000, 24],
    ['LG Pro Light',    180000, 32.5],
    ['ASUS StrMon',     160000, 29.4]
]
"""
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

new_list = []
for i in first_list:
    if i[1] <= 160000:
        new_list.append(i)

for i in new_list:
    print("\nНазвание: ", i[0],
          "\nЦена: ", i[1],
          "\nДиагональ: ", i[2])

