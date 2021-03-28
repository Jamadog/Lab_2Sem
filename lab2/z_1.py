import random


def task_one():     # Удалить из массива все четные элементы
    list_first = [random.randint(-100, 100) for i in range(50)]
    print("Начальный список: \n", list_first)
    list_second = list(filter(lambda i: int(i) % 2, list_first))
    print("Корректированный список: \n", list_second)


def task_two():
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
    matrix = [[random.randint(1, 10) for j in range(m)] for i in range(n)]
    print("Ваша матрица:")
    for i in range(n):
        print(matrix[i])

    j = 0
    while j < n:
        i = 0
        while i < (m/2):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[m - 1 - i][j]
            matrix[m - 1 - i][j] = tmp
            i += 1
        j += 2

    print("Исправленная матрица:")
    for x in range(n):
        print(matrix[x])


def task_three():
    list_first = str(input("Введите строку: \n"))
    word = []
    list_first = list_first.replace(',', '').replace('.', '')
    for i in list_first.lower().split():
        word.append(i)
    print(word)

    i = 0
    while i < len(word):
        wrd = word[i][::-1]
        if wrd.startswith('а') or \
                wrd.startswith('у') or \
                wrd.startswith('о') or wrd.startswith('ы') or \
                wrd.startswith('и') or wrd.startswith('э') or \
                wrd.startswith('я') or wrd.startswith('ю') or \
                wrd.startswith('ё') or wrd.startswith('е'):
            del word[i]
            continue
        i += 1
    print(' '.join(word))

