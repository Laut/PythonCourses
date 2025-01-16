# Задача 3 Дан упорядоченый список vlan настроенных на коммутаторе. Список
# формируется на основе датчика случайных чисел. Реализовать функции работы с этим
# списком:
# - функция удаления VLAN из списка
# - функция поиска VLAN из списка
# - функция вставки VLAN из списка
# - функция сравнения двух списков. Списки равны если равны длины списков и равны
# по «элементно»
# - функция удаления списка VLAN
# - функция добавления списка VLAN

import random

vlan_list=[]
size=int(input("Введите количество Vlan: "))

while size > 0:
    vlan_list.append(random.randint(1,50))
    vlan_list.sort()
    size-=1

print(vlan_list)

def delete(vlan):
    vlan_list.remove(vlan)
    result=vlan_list
    return print(result)

def find(vlan):
    for i in range(len(vlan_list)):
        if vlan_list[i] == vlan:
            result=f"Vlan найден с индексом {i}"
            break
    return print(result)

def add(vlan):
    vlan_list.append(vlan)
    result=vlan_list
    return print(result)

def compare(list1,list2):
    if list1==list2:
        return print("Списки равны")
    else:
        return print("Списки не равны")

def del_list(list):
    del list
    return print("Список удален")

def add_list(list):
    list=[]
    return print("Список создан", list)

vlan_del=int(input("Введите Vlan для удаления: "))
delete(vlan_del)

vlan_find=int(input("Введите Vlan для поиска: "))
find(vlan_find)

vlan_input=int(input("Введите Vlan для добавления: "))
add(vlan_input)

new_list=[]
size=int(input("Введите количество Vlan второго списка: "))

while size > 0:
    new_list.append(random.randint(1,50))
    new_list.sort()
    size-=1

compare(vlan_list,new_list)

del_list(new_list)

add_list(new_list)