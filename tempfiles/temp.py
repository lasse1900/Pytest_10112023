from tempfile import TemporaryFile

# Use binary mode ('w+b') instead of text mode ('r+t')
tp = TemporaryFile('w+b')
tp.write(b'Hello world!')

tp.seek(0)
data = tp.read()
tp.close()

print(data.decode('utf-8'))
