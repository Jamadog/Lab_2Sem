N = int(input("Каков размер последовательности \n-> "))
print("Теперь введите последовательность")
i = 1
lst_psl = []
while i <= N:
    a = int(input("-> "))
    lst_psl.append(a)
    i += 1

nct_ch = 1
for i in range(len(lst_psl)):
    if lst_psl[i] % 2 != 0:
        nct_ch *= lst_psl[i]

otr = min(lst_psl)
for i in range(len(lst_psl)):
    x = lst_psl[i]
    if (x > otr) and (x < 0):
        otr = x

rzn = nct_ch - otr
print("Разность", rzn)
