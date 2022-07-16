import re

text = "стеклянный, стекляный"

match = re.findall(r"стеклянн?ый", text)
print(match)

text = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 2001"
match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)

d = text.split(";")
print(d)