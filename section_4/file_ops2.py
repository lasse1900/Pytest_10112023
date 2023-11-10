

with open("myfile.txt", "r") as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

print('-'* 20)

with open("myfile.txt", "r") as f:
    print(f.readline())
    lines = f.read().split('\n')
    print(lines)


print('-'* 20)

with open("myfile.txt", "r") as f:
    for line in f:
        print(line.strip())