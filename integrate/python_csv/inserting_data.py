import csv
from datetime import datetime

from append_function import get_length

FILE_PATH = 'data.csv'

def insert_user(name, email, amount, sent):
	with open(FILE_PATH, 'a', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		fieldnames = ['id', 'name', 'email', 'amount', 'date', 'sent']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		next_id = get_length(FILE_PATH)

		if next_id == 0:
			writer.writeheader()
			next_id = 1

		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email,
			"amount": amount,
			"date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"sent": sent
		})


insert_user("hopper", "hopper@gmail.com", 299, True)
