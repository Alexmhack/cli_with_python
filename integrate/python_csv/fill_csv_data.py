import csv

with open('data.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Title', 'Description', 'Summary'])
	writer.writerow(['New row', 'Awesome description for row', 'Awesome summary'])
