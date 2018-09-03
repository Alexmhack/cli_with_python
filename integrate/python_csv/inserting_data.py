import csv
from datetime import datetime

from append_function import get_length

FILE_PATH = '../data.csv'

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
			"date": datetime.now().strftime("%d %b at %H:%M"),
			"sent": sent
		})


users = [
	[
		"Hopper",
		"hopper@gmail.com",
		269,
		False
	],

	[
		"Drake",
		"drake@gmail.com",
		690,
		False
	],

	[
		"Adam",
		"adam@gmail.com",
		20,
		False
	],

	[
		"Justin",
		"justin@gmail.com",
		199,
		False
	]
]

for user in users:
	insert_user(user[0], user[1], user[2], user[3])
