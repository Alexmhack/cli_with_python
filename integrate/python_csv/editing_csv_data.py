import csv
import shutil

from tempfile import NamedTemporaryFile

FILE_NAME = 'data.csv'
temp_file = NamedTemporaryFile(delete=True)

with open(FILE_NAME, 'rb') as csvfile, temp_file:
	reader = csv.DictReader(csvfile)
	fieldnames = [b'id', b'name', b'email', b'amount', b'sent']
	writer = csv.writer(csvfile)
	# writer.writeheader()
	print(temp_file.name)

	name = b"NAME"
	temp_file.write(name)

	temp_file.seek(0)
	print(temp_file.read())

	shutil.move(temp_file.name, FILE_NAME)
