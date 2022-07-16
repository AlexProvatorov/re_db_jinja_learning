import re

text = "<font color=#CC0000 bg=#ffffff>"

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-f]{6})", text, re.I)
print("Метод re.search:", match)

match = re.finditer(r"(?P<key>\w+)=(?P<value>#[\da-f]{6})", text, re.I)
for iter in match:
    print("Метод re.finditer через цикл:", iter)

match = re.findall(r"(?P<key>\w+)=(?P<value>#[/da-f]{6})", text, re.I)
print("Метод re.findall:", match)