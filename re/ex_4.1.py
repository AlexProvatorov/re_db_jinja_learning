import re

text = "Подоходный налог, доход"
match = re.findall(r"\bдоход\b|\bприбыль\b|\bобретение\b", text)
print(match)

text = "Подоходный налог, доход"
match = re.findall(r"\b(?:доход|прибыль|обретение)\b", text)
print(match)
