# Задача 4 Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел в диапазоне 1-10. Программа находит повторяющиеся
# элементы и удаляет их из списка. Например, дан список (1,1,1,2,3,4,2,3,4) результат
# (1,2,3,4)

import random

size=10
list=[]

while size > 0:
    list.append(random.randint(1,10))
    size=size-1

print("Исходный список:", list)

while size < len(list):
    num = list[size]
    if num in list[size+1:]:
        list.pop(size)
    else:
        size=size+1

print("Конечный список:", list)