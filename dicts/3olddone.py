# Задание 3
# Переделать скрипт из задания 1a таким образом, чтобы, при запросе
# параметра, отображался список возможных параметров. Список параметров надо
# получить из словаря, а не прописывать вручную.
# Вывести информацию о соответствующем параметре, указанного устройства.
# Пример выполнения скрипта:
# $ python task_5_1b.py
# Введите имя устройства: r1
# Введите имя параметра (location, vendor, model, ios, ip): ip
# 10.255.0.1
# $ python task_5_1b.py
# Введите имя устройства: sw1
# Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ip
# 10.255.0.101
# Замечание – использование циклов и условного оператора запрещено

london_co = {
    "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1",
        },
    "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2",
        },
    "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True,
        },
}

user_iface=input("Введите имя устройства: ")
user_set=input(f"Введите имя параметра {tuple(london_co[user_iface].keys())}: ")
print(london_co[user_iface][user_set])