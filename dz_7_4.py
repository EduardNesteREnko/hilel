def common_elements():
    multiples_of_3 = {i for i in range(100) if i % 3 == 0}
    multiples_of_5 = {i for i in range(100) if i % 5 == 0}
    return multiples_of_3 & multiples_of_5

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')