# Задача 2 Создать функцию calc(a, b, operation). Описание входных параметров:
# 1 Первое число
# 2 Второе число
# 3 Действие над ними:
# 1) + Сложить
# 2) - Вычесть
# 3) * Умножить
# 4) / Разделить
# 5) В остальных случаях функция должна возвращать "Операция не поддерживается"

first_num=int(input("Введите первое число: "))
second_num=int(input("Введите второе число: "))
operation=input("Введите символ математической операци: ")

def calc(a, b, operation):
    result=0
    if operation == "+":
        result=a+b
    elif operation == "-":
        result=a-b
    elif operation == "*":
        result=a*b
    elif operation == "/":
        result=a/b
    else:
        result="Операция не поддерживается"
    return result

print(calc(first_num,second_num,operation))