from jinja2 import Template

per = { 'name': 'Федор', 'age': 33 }

tm = Template("Мне {{ p.age }} лет и зовут {{ p['name'] }}.")
msg = tm.render(p = per)

print(msg)