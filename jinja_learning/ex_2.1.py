from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 3500},
    {'model': 'BMW', 'price': 4000},
    {'model': 'Mazda', 'price': 3000},
    {'model': 'Toyota', 'price': 3000}
]

tpl = "Cуммарная цена автомобилей {{ cs | sum(attribute='price') }}"

tm = Template(tpl)
msg = tm.render(cs = cars)

print(msg)

digits = [1,2,3,4,5]

tpl = "Cумма всех чисел: {{ ds | sum }}"
tpl_1 = "Наибольшее число в списке: {{ ds | max }}"

tm = Template(tpl)
tm_1 = Template(tpl_1)
msg = tm.render(ds=digits)
msg_1 = tm_1.render(ds=digits)

print(msg)
print(msg_1)