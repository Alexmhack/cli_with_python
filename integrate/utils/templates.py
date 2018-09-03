import os

def get_template_path(path):
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception(f"{file_path} is not a valid template path...")
	return file_path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()


def render_context(template_string, context):
	return template_string.format(**context)


template = get_template(r'templates\email_message.txt')
template_html = get_template(r'templates\email_message.html')

context = {
	'name': 'Pranav',
	'date': '15th Aug, 18',
	'total': 599
}

print(render_context(template, context))
print(render_context(template_html, context))

render_html = render_context(template_html, context)
