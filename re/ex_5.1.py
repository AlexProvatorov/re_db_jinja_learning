import re

text = "<font color=#CC0000>"
match = re.search(r"#[\da-fA-F]{6}\b", text)
print(match.group(0))

match = re.search(r"(\w+)=(#[\da-fA-F]{6})\b", text)
print("\nИндекс 0: ", match.group(0))
print("Индекс 1: ", match.group(1))
print("Индекс 2: ", match.group(2))
print("Индекс 0,1,2: ", match.group(0,1,2))
print("Метод группы: ", match.groups())

print("\nМетод ластиндекс: ", match.lastindex)
print("Метод старт: ", match.start(2))
print("Метод енд: ", match.end(2))
print("Метод span: ", match.span(1))
print("Метод pos: ", match.pos)
print("Метод endpos: ", match.endpos)

print("\nМетод re: ", match.re)
print("Метод string: ", match.string)

match = re.search(r"(?P<key>\w+)=(?P<value>#[\da-fA-F]{6})\b", text)
print("\nМетод groupdict: ", match.groupdict())

print("\nМетод expand: ", match.expand(r"\g<key>:\g<value>"))