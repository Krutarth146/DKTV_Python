list1 = [102, 89.78, 67, 90]
print(list1)   # [102, 89.78, 67, 90]

print(list1[-2])

list2 = [[10,20,40], 
         [90,89,78], 
         [45,32,31]]
print(list2[1][1])
print(list2[2][2])

print(list2)

for h in list2:
    # print(h)
    for j in h:  # [10, 20, 40]
        print(j)