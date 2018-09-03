# cli_with_python
command line intergration with python

In this tutorial we will be continuing where we left off in previous [tutorial series](https://github.com/Alexmhack/python_intermediate)

If you haven't started from there be sure to complete that [tutorial](https://github.com/Alexmhack/python_intermediate) first 

So far we have made our command line app work with simple commands like

**USAGE**
```
.../python_intermediate> python integrate --help
.../python_intermediate> python integrate -h
.../python_intermediate> python integrate view -id 1
.../python_intermediate> python integrate view --user_id 10
.../python_intermediate> python integrate message
```

In this tutorial we will be advancing our command line app.

# Installation
Just clone the repository and you can all the above commands, add more data in data.csv 
file and create your own commands by adding or editing code in ```__main__.py``` file.

# Advancing Project
Create a new folder inside **integrate** folder and name it **utils** , copy paste the
```__init__.py``` file in the utils fodler which makes utils a python module.

Now copy the ```templates.py``` file from **python_intermediate/python_emailing** and paste 
it inside the **utils** folder.

**Project Tree**
```
C:.
└───integrate
    ├───python_csv
    ├───templates
    ├───utils
    │   └───__pycache__
    └───__pycache__
```

**integrate folder**
```
C:.
├───python_csv
├───templates
├───utils
│   └───__pycache__
└───__pycache__
```

Now we will move some of the code from ```templates.py``` into ```__main__.py```

**templates.py**
```
import os

def get_template_path(path):
	file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
	if not os.path.isfile(file_path):
		raise Exception(f"{file_path} is not a valid template path...")
	return file_path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()


def render_context(template_string, context):
	return template_string.format(**context)

```

```
__main__.py

from utils.templates import get_template, render_context
...

if args.type == "view":
	if args.user_id:
		print(find_user(user_id=args.user_id))
	if args.email:
		print(find_user(user_email=args.email))
else:
	print("sending message")
	template = get_template(r'templates\email_message.txt')
	template_html = get_template(r'templates\email_message.html')

	context = {
		'name': 'Pranav',
		'date': '15th Aug, 18',
		'total': 599
	}

	print(render_context(template, context))
	print(render_context(template_html, context))
	print("sending message...")
```

This will only give us one more functionality of priting the message that exists inside 
the templates ```templates\email_message.txt``` and ```templates\email_message.html```

Oh yes, where does these two templates come from, we have on more copy paste work left.
Copy the whole **templates** folder from **python_intermediate** and paste it in **
integrate**

We have made some changes in templates.py file.

```
def get_template_path(path):
	file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
	...
```

The file path argument that function takes looks into the integrate folder, you can print
the ```file_path``` to check. We achieve this using two ```os.path.dirname```, first one
takes us back one folder and second tells to take from this current folder and then we join
the paths.

```
.../cli_with_python> python integrate message

# RESULT
sending message
Hi Pranav!
Thank you for your purchase on 15th Aug, 18.
We hope you are excited about using it.
Just as a reminder the purchase total was $599.
Have a greate one!

Team Alexmhack
<!DOCTYPE html>
<html>
<head>
        <title>Alexmhack Email Message</title>
</head>
<body>
        <h1>Hi Pranav!</h1>
        <p>
                Thank you for your purchase on 15th Aug, 18.
                We hope you are excited about using it.
                Just as a reminder the purchase total was $599.
                Have a greate one!
        </p>
        <p>Team Django</p>
</body>
</html>
sending message...
```

As expected the contents of the file inside the templates gets printed.

Now we will be reducing some workload from ```__main__.py``` file and moving the code
to the data_class.py and creating a class there with our functions as methods of the 
class.

Check the ```data_class.py``` [file](https://github.com/Alexmhack/cli_with_python/blob/master/integrate/data_class.py) to understand what I mean.
