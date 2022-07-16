import re

text = "lat = 5, lon=7"
match = re.findall(r"\w+\s*=\s*\w+", text)
print(match)

#Однако данный шаблон будет работать и стакими данными, как 'pi=3, a = 5'
text2 = "pi=3, a = 5"
match = re.findall(r"\w+\s*=\s*\w+", text2)
print(match)

#Если мы хотим чтобы учитывались только ключи lat и lot, их нужно явно указать
text3 = "lat = 5, lon=7, a = 5"
match = re.findall(r"lat\s*=\s*\d+|lon\s*=\s*\d+", text3)
print(match)

#Оптимизация записи, юзаем несохраняющую группировку
match = re.findall(r"(?:lat|lon)\s*=\s*\d+", text3)
print(match)

#Cохраняющая группировка
match = re.findall(r"(lat|lon)\s*=\s*\d+", text3)
print(match)

#Смотрим оба уровня при сохраняющей группировке
match = re.findall(r"((lat|lon)\s*=\s*\d+)", text3)
print(match)