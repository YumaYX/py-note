import re

s = 'abc'

if re.search('^ab', s):
    print("^ab")

if re.search('xyz', s):
    print("xyz")
