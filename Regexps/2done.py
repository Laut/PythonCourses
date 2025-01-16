# Задание 2: Извлеките все слова, начинающиеся с ‘b’ или ‘B’ из данного текста.
# Входные данные
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
# Требуемый вывод
# ['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter', 'butter',
# 'better']

import re

print(re.findall('[Bb]\w+',text))