import re

text = "+7(123)456-78-90"
text2 = " +7(123)456-78-90"

match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text)
print("\nМетод re.match:", match)
match = re.match(r"\+7\(\d{3}\)\d{3}-\d{2}-\d{2}", text2)
print("Метод re.match но пробел в начале строки:", match)

text = """<point lon="40.8482" lat="52.6274" />
<point lon="40.8559" lat="52.6361" />; <point lon="40.8614" lat="52.651" />
<point lon="40.8676" lat="52.6585" />, <point lon="40.8672" lat="52.6626" />
"""

ar = re.split(r"[\n;,]+", text)
print("\nМетод re.split:", ar)

text = """Москва
Казань
Тверь
Самара
Уфа"""

list = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text)
print("\nМетод re.sub:\n" + list)

count = 0
def replFind(m):
    global count
    count += 1
    return f"<option value='{count}'>{m.group(1)}</option>\n"

list = re.sub(r"\s*(\w+)\s*", replFind, text)
print(list)

rx = re.compile(r"\s*(\w+)\s*")
list, total = rx.subn(r"<option>\1</option>\n", text)
list2 = rx.sub(replFind, text)
print(list, total, list2, sep='\n')