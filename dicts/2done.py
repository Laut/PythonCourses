# Задание 2
# Дан список интерфейсов коммутатора и их настроек. Сформировать словарь
# ключ-значение, где ключ это интерфейс, значение - это параметры этого интерфейса.
# Определить какие интерфейсы работают в режиме транк и какие vlan передаются через
# данные транки.
# Пример
# Дано
# list_interface=["fa0/1","fa0/2","fa0/3","fa0/4"]
# list_interface_config=[{"speed":100, "duplex":"full","mode":"switchport mode trunk", "switchport allowed vlan":[10,20,30]},
# {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":20},
# {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":30},
# {"speed":100, "duplex":"full","mode":"switchport mode trunk", "switchport allowed vlan":[11,21,31]}
# ]
# Результат:
# Fa0/1 [10,20,30]
# Fa0/4 [11,21,31]

list_interface=["fa0/1","fa0/2","fa0/3","fa0/4"]
list_interface_config=[{"speed":100, "duplex":"full","mode":"switchport mode trunk", "switchport allowed vlan":[10,20,30]},
                       {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":20},
                       {"speed":100, "duplex":"full","mode":"switchport mode access","vlan":30},
                       {"speed":100, "duplex":"full","mode":"switchport mode trunk", "switchport allowed vlan":[11,21,31]}
]
config={}

for i in range(len(list_interface)):
    config[list_interface[i]]=list_interface_config[i]

for i in config:
    if config[i]["mode"]=="switchport mode trunk":
            print(i,config[i]["switchport allowed vlan"])