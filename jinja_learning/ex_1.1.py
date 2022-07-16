from jinja2 import Template

name = "Федор"

tm = Template("Привет {{ name }}")
msg = tm.render(name=name)

msg2 = f"Привет {name}"
print(msg, msg2, sep = "\n")