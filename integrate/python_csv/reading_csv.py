import csv

with open('data.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		print(row)


with open('data.csv', 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row)