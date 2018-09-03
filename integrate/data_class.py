import os
from pathlib import Path
import csv

FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.csv')

class UserManager:
	def get_user_data(self, user_id=None, user_email=None):
		with open(FILE_PATH) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				row_id = int(row.get("id"))
				unknown_id = None
				unknown_email = None
				found_email = None
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
				if user_email == row.get("email"):
					return row

			if unknown_email and found_id is not None:
				return f"USER EMAIL: {unknown_email} NOT FOUND BUT USER ID: {found_id}"
			if unknown_id is not None:
				if found_email is not None:
					return f"USER ID: {unknown_id} NOT FOUND BUT FOUND EMAIL: {found_email}"
				return f"USER ID: {unknown_id} NOT FOUND AND EMAIL NOT PROVIDED"
		return None
