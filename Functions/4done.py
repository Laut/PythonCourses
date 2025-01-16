# Задача 4 Написать программу, которая последовательно вызывает три функции.
# Функция 1 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело
# на 3, функция 2 – подсчитывает для заданного отрезка чисел все числа, которые делятся
# нацело на 4, Функция 3– подсчитывает для заданного отрезка чисел все числа, которые
# делятся нацело на 5

start=int(input("Введите начало отрезка: "))
end=int(input("Введите конец отрезка: "))

def func1(num1,num2):
    list_3=[]
    for i in range(num1,num2):
        if i % 3 == 0:
            list_3.append(i)
    return print("Числа которые делятся на 3:", list_3)

def func2(num1,num2):
    list_4=[]
    for i in range(num1,num2):
        if i % 4 == 0:
            list_4.append(i)
    return print("Числа которые делятся на 4:", list_4)

def func3(num1,num2):
    list_5=[]
    for i in range(num1,num2):
        if i % 5 == 0:
            list_5.append(i)
    return print("Числа которые делятся на 5:", list_5)

func1(start,end)
func2(start,end)
func3(start,end)