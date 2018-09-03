import csv

with open('data.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(['Append row', 'append description', 'append summary'])
	

with open('data.csv', 'a') as csvfile:
	fieldnames = ['Title', 'Description', 'Summary']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	# writes the fieldnames (heading) for columns
	writer.writeheader()
	writer.writerow({'Title': 'Row3', 'Description': 'Row3', 'Summary': 'Row3'})
