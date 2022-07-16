from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('jinja_learning/templates')
env = Environment(loader = file_loader)

tm = env.get_template('about.htm')
msg = tm.render()

print(msg)