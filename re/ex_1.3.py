import re

text = "(еда), победа, беда"

match = re.findall(r"\(еда\)", text)
print(match)