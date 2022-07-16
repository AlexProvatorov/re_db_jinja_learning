import re

#Юзаем несколько диапазонов для нахождения всех русских букв и цифр
text = "Еду, беда, 55 победа"
match = re.findall(r"[а-яА-Я0-9]", text)
print(match)

#Ищем слово в скобках
text = "Еду, (еда), 55 победа"
match = re.findall(r"[(]еда[)]", text)
print(match)

#Ищем все символы
match = re.findall(r".", text)
print(match)