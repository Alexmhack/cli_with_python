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

# Sending emails
Now that we have our template ready but it still lacks few things like rendering context
from the actual ```data.csv``` file as well as the date column is missing in our file
so for that I have written code using pieces of code from files in **python_csv** folder 
in ```inserting_data.py``` which simply inserts the data.

Inside ```data_class.py``` file we have made some changes with **message_user** function
in the **UserManager** class.

```
class UserManager:

	def message_user(self, user_id=None, user_email=None):
		user = self.get_user_data(user_id=user_id, user_email=user_email)
		if isinstance(user, dict):
			template = get_template(r'templates\email_message.txt')
			template_html = get_template(r'templates\email_message.html')

			context = user
			print(render_context(template, context))
			print(render_context(template_html, context))
		return None
```

Instead of passing the dict with **key value** pairs representing data, we just pass in the
user variable which is actually the returned value received from calling get_user_data 
method with the user_id and user_email. 

Since our function get_user_data returns dict objects as well as strings for error we 
don't wanna be inserting that in our context so we used a simple logic of checking if
the user is a dict object then executing further code

```
	if isinstance(user, dict):
		...
```

That's it now we can run commands 

**cmd**
```
.../cli_with_python> python integrate message -id 1

sending message
Hi Hopper!
Thank you for your purchase on 2018-09-03 18:56:01.
We hope you are excited about using it.
Just as a reminder the purchase total was $269.
Have a greate one!

Team Django
<!DOCTYPE html>
<html>
<head>
        <title>Django Email Message</title>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
</head>
<body>
        <h1 class="text-center">Hi Hopper!</h1>
        <p>
                Thank you for your purchase on 2018-09-03 18:56:01.
                We hope you are excited about using it.
                Just as a reminder the purchase total was $269.
                Have a greate one!
        </p>
        <p>Team Django</p>
</body>
</html>
```

As you can see we have all the information of our user with **id 1** rendered in the 
template and the email is ready to be sent to the user at the email address.

**NOTE:** The user data we have used is fake with fake email addresses so you can use
your data and actually see the email being sent using actual email addresses.

For sending email we will be using the same code we used in the ```html_format_email.py```
file. So copy paste the imports and email credentials from that file into 
```data_class.py```

Create a new method named ```render_message(self, user_data)``` in which we are going to
do all the rendering stuff and in the message_user method we will send email

**data_class.py**
```
class UserManager:

	def render_message(self, user_data):
		template = get_template(r'templates\email_message.txt')
		template_html = get_template(r'templates\email_message.html')

		if isinstance(user_data, dict):
			context = user_data
			plain = render_context(template, context)
			html = render_context(template_html, context)
			return (plain, html)
		return (None, None)
```

So basically we moved all our rendering code into this method.

Now for sending email we have 

**data_class.py**
```
...
	def message_user(self, user_id=None, user_email=None, all_users=False):
		user = self.get_user_data(user_id=user_id, user_email=user_email)
		if isinstance(user, dict):
			plain_, html_ = self.render_message(user)
			email = user.get("email", username)
			to_list.append(email)

			try:
				email_conn = SMTP(host, port)
				email_conn.ehlo()
				email_conn.starttls()

				message = MIMEMultipart("alternative")
				message['Subject'] = "Hello there"
				message['From'] = 'Python Developer'
				message['To'] = email

				part_1 = MIMEText(plain_, 'plain')
				part_2 = MIMEText(html_, 'html')

				message.attach(part_1)
				message.attach(part_2)

				email_conn.login(username, password)
				email_conn.sendmail(from_email, to_list, message.as_string())
				return f"EMAIL SENT TO {email}"
			except SMTPException as e:
				print(e)
			finally:
				email_conn.quit()

		return None
```

So we get the user details by caling ```get_user_data(user_id, user_email)``` on the
user_id we received from ```__main__.py``` file where we call this class method passing
in the user_id from the arguments provided in command prompt

Then we do all the same stuff for sending email then at last we return the string 
containing email else we ```return None```

Very simple and nicely called methods for completing the task.

# Sending emails to all users
In 	```__main__.py``` file we create another argument named ```--all_users``` which
does not take any argument and we do that using ```action="store_true"``` attribute

__main__.py
```
parser.add_argument(
	"-all",
	"--all_users",
	action="store_true",
	help="sends message to all the users"
)
```

Now we check if ```args``` contains ```-all``` or ```--all_users``` argument by

```
elif args.type == "message":
	if args.all_users:
		print("SENDING EMAILS...")
		print(UserManager().message_all())
	else:
		print("SENDING EMAILS...")
		print(UserManager().message_user(user_id=args.user_id, user_email=args.email))
```

If yes then we call ```message_all()``` class method which simply opens the csvfile and 
iterates over all the rows and sends emails by calling the 
```message_user(user_id=row_id)```

**data_class.py**
```
...
	def message_all(self):
		with open(FILE_PATH) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				row_id = int(row.get("id"))
				print(self.message_user(user_id=row_id))
```

We all print the returned message from function call

One more thing that is missing from our email sending command line app is that we don't 
have a tally which tells that which users are already been mailed, we have a field defined 
for this purpose remember the **sent** field which is currently set to False.

What we will be doing now is editing that field to True if email has been sent and checking
the next time before sending emails that we don't send email to users with **True** set as 
**sent** field.
