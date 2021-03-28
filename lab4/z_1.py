def shot(a_, b_):
    return a_/b_


def arithmetics(x, y):
    summa = x + y
    rzn = x - y
    print("Сумма дробей: ", summa)
    print("Разность дробей: ", rzn)


a = int(input("Введите числитель первой дроби: "))
b = int(input("Введите значенатель первой дроби: "))

n = int(input("Введите числитель второй дроби: "))
m = int(input("Введите знаменатель первой дроби: "))

arithmetics(shot(a, b), shot(n, m))
