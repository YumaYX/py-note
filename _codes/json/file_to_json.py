import json

with open('output.json', 'r') as f:
    my_list = json.load(f)

print(my_list)
print(type(my_list))
