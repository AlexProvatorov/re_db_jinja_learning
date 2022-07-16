from jinja2 import Template

name_1 = "Итити Онидзука"
name_2 = "Александр Проваторов"
age = 22
single = "Холост"
married = "Женат"


tm = Template("Меня зовут {{ n }}, мне {{ a }} года. {{ ms }}.")
msg_1 = tm.render(a=age, n=name_1, ms=single)
msg_2 = tm.render(a=age, n=name_2, ms=married)

print(msg_1, msg_2, sep = "\n")