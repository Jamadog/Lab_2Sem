N = int(input("Кол-во последовательности? \n-> "))
lst_psl = []
i = 1
while i <= N:
    print(i, "элемент")
    a = int(input("-> "))
    lst_psl.append(a)
    i += 1

smm = 0
kol = 0
print("Элементы удовлетворяющие условию")
for i in range(len(lst_psl)):
    if (lst_psl[i] % 2 != 0) and ((i+1) % 2 == 0):
        smm += lst_psl[i]
        kol += 1
        print("->", lst_psl[i])
print("Ваша сумма -> ", smm)
print("Ваше кол-во -> ", kol)
