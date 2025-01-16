# Задание 1 Написать программу – которая по заданным границам отрезка, который
# указывает пользователь, находит сумму всех четных чисел, произведение всех нечетных# чисел.


a=int(input("Введите 1 границу: "))
b=int(input("Введите 2 границу: "))

limit1=max(a,b)
limit2=min(a,b)

summ=0
multiply=1

while limit1 >= limit2:
    if limit1 % 2 == 0:
        summ=summ+limit1
        limit1=limit1-1
    else:
        print(multiply)
        multiply=limit1*2

        limit1=limit1-1

print("Сумма четных чисел ",summ)
print("Произведение нечетных чисел", multiply)