# https://docs.python.org/ja/3/tutorial/datastructures.html

list = []

for f in range(10):
    list.append(f)

print("append:")
print(list)

print("pop:")
list.pop()
print(list)

print("index:")
print(list[2])

print("clear:")
list.clear()
print(list)
