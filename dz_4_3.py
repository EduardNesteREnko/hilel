import random

lst1 = [1, 2, 3, 4, 5, 6, 7, 9]
lst2 = [1, 1, 2, 1]
lst3 = [6, 3, 7]

new1 = [lst1[0], lst1[2], lst1[-2]]
new2 = [lst2[0], lst2[2], lst2[-2]]
new3 = [lst3[0], lst3[2], lst3[-2]]

random.shuffle(new1)
random.shuffle(new2)
random.shuffle(new3)

print(new1)
print(new2)
print(new3)
