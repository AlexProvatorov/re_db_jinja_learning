from jinja2 import Environment, FileSystemLoader

subs = ['Английский', 'Информатика', 'Физика']

file_loader = FileSystemLoader('jinja_learning/templates')
env = Environment(loader = file_loader)

tm = env.get_template('about_2.htm')
msg = tm.render(list_table = subs)

print(msg)