import re

text = "Python, python, PyThOn"

match = re.findall(r"(?im)python", text)
print(match)