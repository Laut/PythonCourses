# Задание 1: Извлеките никнейм пользователя, имя домена и суффикс из данных email
# адресов
# Входные данные
emails = """zuck26@facebook.com page33@google.com jeff42@amazon.com"""
# Требуемый вывод
# [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re

emails=emails.split()
result=[]

for i in emails:
    i=re.split('\s+|@|\.', i)
    result.append(tuple(i))

print(result)
