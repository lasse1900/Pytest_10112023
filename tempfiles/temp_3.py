from tempfile import TemporaryFile as tempfile

# tp = tempfile('r+t', delete=False)
tp = tempfile('r+t')
tp.write("Hello Test!")

tp.seek(0)
data = tp.read()

tp.close()
print(data)
assert data == "Hello Test!"

print('-'*20)
