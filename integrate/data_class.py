import os
import csv

from utils.templates import get_template, render_context

FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')

class UserManager:

	def message_user(self):
		template = get_template(r'templates\email_message.txt')
		template_html = get_template(r'templates\email_message.html')

		context = {
			'name': 'Pranav',
			'date': '15th Aug, 18',
			'total': 599
		}

		print(render_context(template, context))
		print(render_context(template_html, context))
		return None

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
