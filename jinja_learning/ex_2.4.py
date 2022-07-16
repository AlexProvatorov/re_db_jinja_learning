from cgitb import html
from jinja2 import Template

persons = [
    {"name": "Bob", "old": 20, "weight": 78},
    {"name": "Alex", "old": 22, "weight": 73},
    {"name": "Jack", "old": 32, "weight": 88}
]

html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro %}

{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ui>
{% endcall -%}
'''

tm = Template(html)
msg = tm.render(users=persons)

print(msg)