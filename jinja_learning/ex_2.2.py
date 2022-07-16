from jinja2 import Template

persons = [
    {"name": "Bob", "old": 20, "weight": 78},
    {"name": "Alex", "old": 22, "weight": 73},
    {"name": "Jack", "old": 32, "weight": 88}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)