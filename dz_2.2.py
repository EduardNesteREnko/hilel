number = int(input('Type number:'))
d1 = number // 10000
d2 = (number // 1000) % 10
d3 = (number // 100) % 10
d4 = (number // 10) % 10
d5 = number % 10

print(d5)
print(d4)
print(d3)
print(d2)
print(d1)
