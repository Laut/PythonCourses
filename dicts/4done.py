# Задание 4
# Дан список интерфейсов коммутатора и их настроек. Сформировать словарь
# ключ-значение, где ключ это интерфейс, значение - это параметры этого интерфейса. Дан
# список VLAN настроенном на коммутаторе. Определить какие интерфейсы будут
# заблокированы, например, порт настроен в VLAN 15, а VLAN 15 не настроен на
# коммутаторе
# Пример
# Дано
# List_vlan=[10,20,30,40]
# list_interface=["fa0/1","fa0/2","fa0/3","fa0/4"]
# list_interface_config=[
# {"speed":100, "duplex":"full","mode":" switchport mode access ", "vlan":11},
# {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":20},
# {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":30},
# {"speed":100, "duplex":"full","mode":" switchport mode access ", "vlan":42}
# ]
# Результат:
# Порты Fa0/1 и Fa0/4 заблокированы

List_vlan=[10,20,30,40]
list_interface=["fa0/1","fa0/2","fa0/3","fa0/4"]
list_interface_config=[
        {"speed":100, "duplex":"full","mode":" switchport mode access ", "vlan":11},
        {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":20},
        {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":30},
        {"speed":100, "duplex":"full","mode":" switchport mode access ", "vlan":42}
]

config={}
index=0

for i in range(len(list_interface)):
    config[list_interface[i]]=list_interface_config[i]

for i in config:
    for j in config[i]:
        if j == "vlan" and config[i][j] != List_vlan[index]:
            print("Порт", i, "заблокирован")
    index=index+1