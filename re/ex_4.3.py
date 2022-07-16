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

match = re.findall(r"""([-\w]+)             #выделяем атрибут
                   [ \t]*=[ \t]*            #далее, должно идти равно и кавычки
                   (?P<q>[\"'])?            #проверяем наличие кавычки
                   (?(q)([^\"']+(?<![ \t]))|([^ \t>]+))     #выделяем значение атрибута
                   """, 
                   text, re.MULTILINE|re.VERBOSE)

print(match)