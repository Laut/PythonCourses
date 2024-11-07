# Задача 1 Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно
# присутствует, замените его на 200 Обновите список только при первом вхождении числа
# 20
import random

size=int(input("Введите размер списка: "))
list=[]

while size > 0:
    list.append(random.randint(10,30))
    size=size-1

for i in range(len(list)):
    if list[i] == 20:
        list[i] = 200 
        break

print(list)