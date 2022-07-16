import re

text = "значения map и bitmap это разные вещи"
match = re.findall(r'\bmap\b', text)

print(match)