from telnetlib import TELNET_PORT
from jinja2 import Template

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

tm = Template(link)
msg = tm.render()

print(msg)