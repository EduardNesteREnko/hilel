#lst1 = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
#lst1 = [0] #-> [0]
#lst1 = [1, 0, 13, 0, 0, 0, 5]# -> [1, 13, 5, 0, 0, 0, 0]
#lst1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]# -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

output = []
zeros = 0
for x in lst1:
    if x == 0:
        zeros += 1
    else:
        output.append(x)

while zeros > 0:
    output.append(0)
    zeros -= 1

print(output)
