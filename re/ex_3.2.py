import re

#Сохраним ключи и значения
text = "lat = 5, lon=7, a = 5"
match = re.findall(r"(lat|lon)\s*=\s*(\d+)", text)
print(match)

#Найдем значение атрибута src в тэге img
text = "Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(r"<img\s+[^>]*src=[\"'](.+?)[\"']", text)
print(match)

#Юзаем ссылку на сохранение
match = re.findall(r"<img\s+[^>]*src=([\"'])(.+?)\1", text)
print(match)

#Юзаем ссылку на сохранение через имя
match = re.findall(r"<img\s+[^>]*src=(?P<q>[\"'])(.+?)(?P=q)", text)
print(match)