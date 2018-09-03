import csv

def delete_row(file_path, row_id=None, email=None):
	with open(file_path, 'r', newline='') as csvfile:
		reader = csv.DictReader(csvfile)

		with open('new.csv', 'a', newline='') as writefile:
			count = 0
			fieldnames = ['id', 'name', 'email', 'amount', 'sent']
			writer = csv.DictWriter(writefile, fieldnames=fieldnames)
			for row in reader:
				count += 1
				print(row)
				if row['id'] == row_id:
					del row['id']
					del row['name']
					del row['email']
					del row['amount']
					del row['sent']
					writer.writerow(row)
					break


delete_row('new.csv', 1)
