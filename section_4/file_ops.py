
try:
    f = open("myfile.txt", "r")
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

finally:
    f.close()
