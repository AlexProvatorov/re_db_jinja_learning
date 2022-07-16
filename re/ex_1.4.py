import re

text = "Еда, беду, победа"
match = re.findall(r"[Ее]д[ау]", text)
print(match)