import os
import csv

from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.templates import get_template, render_context

FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')

host = "smtp.gmail.com"
port = 587
username = "your-email-address"
password = "your-password"

from_email = username
to_list = []

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

	def message_user(self, user_id=None, user_email=None):
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

	def message_all(self):
		with open(FILE_PATH) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				row_id = int(row.get("id"))
				print(self.message_user(user_id=row_id))

	def get_user_data(self, user_id=None, user_email=None):
		with open(FILE_PATH) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				row_id = int(row.get("id"))
				unknown_id = None
				unknown_email = None
				found_email = None
				found_id = None
				if user_id is not None:
					if user_email is not None:
						if int(user_id) == row_id:
							if user_email == row.get("email"):
								return row
							else:
								unknown_email = user_email
								found_id = user_id
						else:
							unknown_id = int(user_id)
							if user_email == row.get("email"):
								found_email = user_email
					else:
						if int(user_id) == row_id:
							return row
						else:
							unknown_id = int(user_id)
				else:
					if user_email == row.get("email"):
						return row
					else:
						unknown_email = user_email

			if unknown_email is not None:
				if found_id is not None:
					return f"USER EMAIL: {unknown_email} NOT FOUND BUT USER ID: {found_id}"
				return f"USER EMAIL: {unknown_email} NOT FOUND AND ID NOT PROVIDED"
			if unknown_id is not None:
				if found_email is not None:
					return f"USER ID: {unknown_id} NOT FOUND BUT FOUND EMAIL: {found_email}"
				return f"USER ID: {unknown_id} NOT FOUND AND EMAIL NOT PROVIDED"
		return None
