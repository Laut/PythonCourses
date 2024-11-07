# Написать программу: дан список из 10 чисел, которые задаются с помощью
# датчика случайных чисел. Программа находит повторяющиеся элементы и считает
# количество повторений. Например дан список (1,1,1,2,3,4,2,3,4) результат число 1
# повторяется 3 раза, число 2 – 2 раза, число 3 - 2 раза, число 4 – 2 раза

import random

size=10
list=[]
checked=[]

while size > 0:
    list.append(random.randint(1,10))
    size=size-1

print("Исходный список:", list)

for i in range(len(list)):
    num = list[i]
    if num not in checked:
        count = 0
        for j in range(len(list)):
            if list[j] == num:
                count=count+1

        if count >= 2:
            print(f"Число", num, "повторяется", count, "раза")
        checked.append(num)