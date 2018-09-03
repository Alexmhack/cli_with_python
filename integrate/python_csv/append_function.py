import csv

# number of rows
def get_length(file_path):
	with open(file_path) as csvfile:
		reader = csv.reader(csvfile)
		reader_list = list(reader)
	return len(reader_list)

def append_data(file_path, name, email):
	fieldnames = ['id', 'name', 'email']
	next_id = get_length(file_path)
	with open('data.csv', 'a', newline='') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		if next_id == 0:
			writer.writeheader()
			next_id = 1
		writer.writerow({
			"id": next_id,
			"name": name,
			"email": email
		})


append_data("data.csv", "Alex", "Alex@code.com")
