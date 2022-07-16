import re

text = "еда, беда, победа"
match = re.findall(r"еда", text)
print(match)