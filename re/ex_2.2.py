import re

text = "Google, Gooogle, Goooooogle"

match = re.findall(r"Go{2,}gle", text)
print(match)

match = re.findall(r"Go{,4}gle", text)
print(match)

phone = "89123456789"
match = re.findall(r"8\d{10}", phone)
print(match)