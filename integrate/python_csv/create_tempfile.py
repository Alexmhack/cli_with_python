import os
import tempfile

temp = tempfile.NamedTemporaryFile(delete=False)
print(temp.name)

temp.write(b"Hello world\n")
temp.seek(0)
print(temp.read())
temp.close()
os.unlink(temp.name)
print(os.path.exists(temp.name))

with tempfile.NamedTemporaryFile(delete=False) as tp:
	print(tp.name)
	tp.write(b"Greetings python")
	tp.seek(0)
	print(tp.read())
	tp.close()
	os.unlink(tp.name)
	print(os.path.exists(tp.name))


with tempfile.NamedTemporaryFile() as temp:
	print(temp.name)
	temp.write(b"writing data in temporary file")
	temp.seek(0)
	print(temp.read())
	temp.close()
	print(os.path.exists(temp.name))
