lst1 = [12, 3, 4, 10]# => [10, 12, 3, 4]
#lst1 = [1]# => [1]
#lst1 = [] #=> []
#lst1 = [12, 3, 4, 10, 8]# => [8, 12, 3, 4, 10

if len(lst1) >=1:
    lst1[0],lst1[-1] = lst1[-1],lst1[0]
    print(lst1)
else:
    print(lst1)