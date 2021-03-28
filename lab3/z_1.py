import pickle
import random

filename = 'z_1.dat'

with open(filename, 'wb') as fl:
    n = [random.randint(-100, 100) for i in range(15)]
    first = n[0]
    last = None
    for i, v in enumerate(reversed(n)):
        if v < 0:
            last = len(n) - 1 - i
            break
    print("Первый элемент: ", first)
    print("Последний элемент: ", n[last])
    first = n.index(n[0])
    last = n.index(n[last])
    n[first], n[last] = n[last], n[first]
    pickle.dump(n, fl)

with open(filename, 'rb') as fl:
    n = pickle.load(fl)
    print("Список из файлы:\n", n)


