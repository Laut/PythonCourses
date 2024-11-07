# Задача 3 Найти ошибку в программе и исправить
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.append(list2)
# print(list1)
# Результат программы должен быть таким [1, 2, 3, 4, 5, 6]
# Категория задач – средней сложности:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
for i in range(len(list2)):
    list1.append(list2[i])
print(list1)