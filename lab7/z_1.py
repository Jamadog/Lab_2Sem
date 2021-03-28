import random


def chunk_list(seq, size):
    return (seq[i::size] for i in range(size))


def func(lst_, ):
    done = []
    not_done = []
    for i in range(len(lst_)):
        if lst_[i] == lst_[::-1]:
            break
        elif (lst_[i] ** 3) > -10 and ((lst_[i] ** 3) < 20):
            done.append(lst_[i])
            continue
        else:
            not_done.append(lst_[i])
            continue
    return done, not_done


x = [random.randint(-10, 10) for i in range(51)]
lst = list(chunk_list(x, 2))

one = lst[0]
two = lst[1]
print("Первая половина: \n", one, len(one))
print("Вторая половина: \n", two, len(two))
one_, one__ = func(one)
two_, two__ = func(two)

print("Эти элементы (1 половины) удовлетворяют условию: \n", one_, "\n")
print("Эти элементы (1 половины) не удовлетворяют условию: \n", one__, "\n")


print("Эти элементы (2 половины) удовлетворяют условию: \n", two_, "\n")
print("Эти элементы (2 половины) не удовлетворяют условию: \n", two__, "\n")
