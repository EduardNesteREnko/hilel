import string
import keyword

name = input("Variable name: ")

is_valid = True

if len(name) == 0:
    is_valid = False
elif name[0] in string.digits:
    is_valid = False

for ch in name:
    if ch in string.ascii_uppercase:
        is_valid = False

for ch in name:
    if ch in string.punctuation and ch != "_":
        is_valid = False
    if ch == " ":
        is_valid = False

for kw in keyword.kwlist:
    if kw == name:
        is_valid = False

underscore_count = 0
for ch in name:
    if ch == "_":
        underscore_count += 1
if underscore_count > 1:
    is_valid = False

print(is_valid)
