import re

text = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Уроки по Python</title>
</head>
<body>
<p align=center>Hello World!</p>
<script type="text/javascript">
let o = document.getElementById('id_div');
console.log(obj);
</script>
</body>
</html>"""

#Опережающая проверка на совпадение
match = re.findall(r"^<script.*?>([\w\W]+)(?=</script>)", text, re.MULTILINE)
print(match)

#Позитивная ретроспективная проверка
match = re.findall(r"^<script.*?>([\w\W]+)(?<=</script>)", text, re.MULTILINE)
print(match)

#Выберем все пары атрибут=значение
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*[\"']([^\"']+)(?<![ \t])", text, re.MULTILINE)
print(match)

#Выберем все пары ключ="значение" или ключ=значение
match = re.findall(r"([-\w]+)[ \t]*=[ \t]*(?P<q>[\"'])?(?(q)([^\"']+(?<![ \t]))|([^ \t>]+))", text, re.MULTILINE)
print(match)