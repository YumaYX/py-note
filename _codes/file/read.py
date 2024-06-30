path = "read.txt"
with open(path) as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
