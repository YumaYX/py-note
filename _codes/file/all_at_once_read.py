file_data = open("read.txt", "r")
text = file_data.read()
print(text, end="")
file_data.close()
