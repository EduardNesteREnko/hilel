def first_word(text):
    # Замінюємо коми й крапки на пробіли
    for ch in ('.', ','):
        text = text.replace(ch, ' ')
    words = text.split()
    for word in words:
        if any(c.isalpha() for c in word): # перевірка, що слово містить літери
            return word
    return ''

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')