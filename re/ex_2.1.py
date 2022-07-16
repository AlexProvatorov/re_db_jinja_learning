import re

text = "Google, Gooogle, Goooooogle"

match = re.findall(r"o{2,5}", text) # Мажорный квантификатор
print(match)

match = re.findall(r"o{2,5}?", text) # Минорный квантификатор
print(match)