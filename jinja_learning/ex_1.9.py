from jinja2 import escape

link = '''В HTML-документе ссылки определяются так:
<a href="#">Ссылка</a>'''

msg = escape(link)
print(msg)