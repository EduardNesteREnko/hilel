from string import ascii_letters

input_str = input('star:')

start = input_str[0]
end = input_str[2]

result = ""
code = ord(start)
end_code = ord(end)

if code <= end_code:
    while code <= end_code:
        result += chr(code)
        code += 1
else:
    while code <= ord('z'):
        result += chr(code)
        code += 1
    code = ord('A')
    while code <= end_code:
        result += chr(code)
        code += 1

print(result)
