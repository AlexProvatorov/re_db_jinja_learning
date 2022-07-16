import re

text = "Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img.*?>", text)
print(match)

match = re.findall(r"<img\s+[^>]*src\s*=\s*[^>]*>", text)
print(match)