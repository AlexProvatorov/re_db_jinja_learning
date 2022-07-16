import re

text = "Бублик 5, монета 55."
match = re.findall(r"[0123456789]", text)
print(match)

#Или можно указать диапазон от и до посредством "-"
match = re.findall(r"[0-9]", text)
print(match)
#Результат аналогичен

#Ище две цифры подряд
match = re.findall(r"[0-9][0-9]", text)
print(match)

#Инвертировать поиск, т.е. ищем не цифры
match = re.findall(r"[^0-9]", text)
print(match)

#Поиск тире(запись в начале)
text = "Еда, беду, из-за, победа"
match = re.findall(r"[-0-9]", text)
print(match)

