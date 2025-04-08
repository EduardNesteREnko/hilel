import string

text = input("Hashtag: ")

  
allowed = ""
for char in text:
    found = False
    for symbol in string.punctuation + " ":
        if char == symbol:
            found = True
    if found == False:
        allowed += char


hashtag = "#" + allowed.title()


hashtag = hashtag[:140]

print(hashtag)
