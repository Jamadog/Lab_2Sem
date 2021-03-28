n = int(input("Введите кол-во вершин: "))
graph = {}
for i in range(n):
    graph[i+1] = []


def add_graph(graph, pred, prm):
    graph.setdefault(pred, []).append(prm)
    return graph


if (n > 0) and (n <= 10):
    for i in range(n):
        string = input("Прдшественник и приемник: ")
        pred, prm = string.split()
        pred = int(pred)
        prm = int(prm)
        add_graph(graph, pred, prm)
    print("Список: ", graph)

    print("\nЗадание А: ")
    for j in graph:     # задание А
        if len(graph.get(j)) >= 2:
            print(j)

    print("\nЗадание Б:")
    for j in graph:     # задание Б
        if len(graph.get(j)) == 0:
            print(j)

    print("\nЗадание В: ")
    for j in graph:     # Задание В
        if len(graph.get(j)) >= 1:
            print("Для вершины: ", graph.get(j), "предшественник", j, "\n")

    print("\nЗадание Г: ")
    for j in graph:  # задание Г
        if len(graph.get(j)) == 1:
            print(j)
