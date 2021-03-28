import module_one as mo

list_one = mo.create_list()
new_list = mo.edit_list(list_one)

for i in new_list:
    print("\nНазвание: ", i[0],
          "\nЦена: ", i[1],
          "\nДиагональ: ", i[2])
