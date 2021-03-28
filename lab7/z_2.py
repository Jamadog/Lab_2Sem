def func(n):
    lst = []
    for i in range(n):
        lst.append(input("Введите " + str(i+1) + " элемент: "))
    return lst


n1 = int(input("Введите кол-во первого стека: "))
lst_1 = func(n1)

n2 = int(input("Введите кол-во второго стека: "))
lst_2 = func(n2)

print("Ваши списки: \n", lst_1, "\n", lst_2)

new_lst = lst_1 + lst_2
new_lst.sort()
new_lst = set(new_lst)
print("Отсортированный список: ", new_lst)
