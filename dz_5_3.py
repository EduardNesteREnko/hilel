import string

input = input("Введите текст для хэштега: ")

allowed = ""
for char in input:
    found = False
    for symbol in string.punctuation + " ":
        if char == symbol:
            found = True
    if found == False:
        allowed += char

hashtag = "#" + input.strip().replace(' ','_').title()


hashtag = hashtag[:140]

print(hashtag)
