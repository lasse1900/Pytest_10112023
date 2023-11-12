# from tempfile import TemporaryFile as tempfile

# with tempfile("r+t", delete=False) as file:
#     for i in range(1, 101):
#         file.write(str(i) + ' ')
#     # Reset the file position to the beginning before reading
#     file.seek(0)
#     # Read the first line
#     print(file.readline())
#     # Read the remaining lines and split them
#     lines = file.read().split(' ')
#     print(lines)

from tempfile import TemporaryFile

with TemporaryFile("r+t", delete=False) as file:
    for i in range(1, 101):
        file.write(str(i) + ' ')

    file.seek(0)
    # Read the first line
    print(file.readline().strip(), end=' ')

    # Read the remaining lines, split them, and filter out empty strings
    lines = file.read().split(' ')
    lines = list(filter(lambda x: x != '', lines))

    print(*lines)
