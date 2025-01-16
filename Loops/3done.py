# Задание 3 Для заданного интервала вывести все простые числа

a=int(input("Введите 1 границу: "))
b=int(input("Введите 2 границу: "))

limit1=min(a,b)
limit2=max(a,b)

list=[]

for i in range(limit1,limit2):
    if i % 2 == 0:
        list.append(i)
        
print(list)