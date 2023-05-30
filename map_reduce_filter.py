num = 34

def cube1(dhruv):
    return dhruv**3

print(cube1(num))   # 39304

cube = lambda x : x**3
print(cube(25))  # 15625

l1 = [4,5,3,2,90]
res = []
for i in l1:
    res.append(i**3)

print(res)


# Powerful functions ----> Map, reduce, filter

# MAP ---------------------
l1 = [4,5,3,2,90]
x = tuple(map(lambda x : x**3, l1))
# print(x)   # <map object at 0x000001D02E036590>
print(x)  # (64, 125, 27, 8, 729000)


l2 = ['23', '90', '312', '12', '784']

print(list(map(lambda f : int(f) , l2)))   # [23, 90, 312, 12, 784]

l3 = [100, 3000,9000, 100000, 900000]

Incre_sal = list(map(lambda x : x+1000, l3))
print(Incre_sal)   # [1100, 4000, 10000, 101000, 901000]
print(type(Incre_sal))   # <class 'list'>


l3 = [(10,90), (54, 89), (32, 78), (32,21)]
print(sorted(l3))

for i in range(len(l3)-1):   # i = (10,90)
    for j in range(i+1,len(l3)):
        if l3[i][-1] > l3[j][-1]:
            temp = l3[i]
            l3[i] = l3[j]
            l3[j] = temp
print(l3)

# HW ---------

l3 = [[10,89,78,32], [46,89,21,65], [44,98,67,21], [11,20,30,5]]

# [78,65,67,20]

for j in l3:  # j = [10,89,78,32]
    j.sort()    
    print(j[-2])

print(list(map( lambda x : sorted(x)[-2],l3)))   # [78, 65, 67, 20]

# Filter ------------------------------

l4 = [10, 90, 88, 77 , 56, 45, 70]

divi_5 = list(map(lambda x : x % 5 == 0 and x % 7 == 0 ,l4))

print(divi_5)  # [False, False, False, False, False, False, True]

divi_5 = list(filter(lambda x : x % 5 == 0 and x % 7 == 0 ,l4))
print(divi_5)  # [70]


# Map, filter, lambda ---> 10 Programs

# Next Topics: reduce, accumulate, Generators, Iterators, Recursion, Regex