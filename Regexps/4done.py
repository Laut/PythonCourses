# Задание 4: Очистите следующий твит, чтобы он содержал только одно сообщение
# пользователя. То есть, удалите все URL, хэштеги, упоминания, пунктуацию, RT и CC.
# Входные данные
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
# Требуемый вывод
# 'Good advice What I would do differently if I was learning to code today'

import re

print(re.sub(r'!\s|RT @\w+:|https.*',r'',tweet))