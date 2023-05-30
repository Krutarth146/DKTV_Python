# List Methods

list1 = [10,20,30.90,78,67]

print(list1)  # [10, 20, 30.9, 78, 67]

list1.append(1000)   # For Insert element in the last Index
list1.append("Manoj")

print(list1)  # [10, 20, 30.9, 78, 67, 1000, 'Manoj']


# list1.extend(900)  # Generates Error
list1.extend('4021')
print(list1)  # [10, 20, 30.9, 78, 67, 1000, 'Manoj', '4', '0', '2', '1']


list3 = [10,20,30,40,50]

list1.extend(list3)
print(list1)


list4 = [(10,20,30), (40,50,60)]
list1.extend(list4)
print(list1)   # [10, 20, 30.9, 78, 67, 1000, 'Manoj', '4', '0', '2', '1', 10, 20, 30, 40, 50, (10, 20, 30), (40, 50, 60)]


list1.append(list3)
print(list1)  # [10, 20, 30.9, 78, 67, 1000, 'Manoj', '4', '0', '2', '1', 10, 20, 30, 40, 50, (10, 20, 30), (40, 50, 60), [10, 20, 30, 40, 50]]


list1.insert(3,500)
print(list1)


del list1[4:]
print(list1)   # [10, 20, 30.9, 500]
  
list1.insert(-1,900)
list1.insert(-2,7700)
print(list1)   # [10, 20, 30.9, 7700, 900, 500]

list1[-2] = 6565

print(list1)  # [10, 20, 30.9, 7700, 6565, 500]

# Element Romoval


list1.pop()
list1.pop()
print(list1)  # [10, 20, 30.9, 7700]

x = list1.pop(2)  # [10, 20, 7700]   # index

print(x)   # 30.9
print(list1)  # [10, 20, 7700]

list1.remove(7700)   # Element
print(list1)   # [10, 20]

list2 = list1.copy()   # Shallow Copy   # xerox 
print(id(list2))  # 2269233011200
print(id(list1))  # 2269228554176
list3 = list1   # Deep copy  # reference copy  # DIgilocker
print(id(list3))
print(id(list1))
 # 2085244295104
 # 2085244295104

print(list2)  # [10, 20]
print(list3)  # [10, 20]
x = 90

list1.append(3000)
print(list2)  # [10, 20]
print(list3)  # [10, 20, 3000]

list3.insert(1,20)

print(list1)  # [10, 20, 20, 3000]

# list1.clear()
# print(list1)  # []
# [10, 20, 20, 3000]
print(list1.count(20))  # 2
print(list1.index(20))  # 1

list1.reverse()
print(list1)  # [3000, 20, 20, 10]

list1.sort()
print(list1)  # [10, 20, 20, 3000]

list1.sort(reverse=True)
print(list1)   # [3000, 20, 20, 10]


# List : Ordered (Indexed), Allow's Duplicates, Mutable (Changeble)

list1 = [20,30,10,20,30,40,10,50,70,10]

# set -> A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

set1 = {10}
dict1 = {}
 
print(type(dict1))  # <class 'dict'>
print(type(set1))   # <class 'set'>

list1 = [20,30,10,20,30,40,10,50,70,10]


# 1.
# list1 = list(set(list1))
# print(list1)  # [70, 40, 10, 50, 20, 30]

# 2:

temp = []
for i in list1:  # 20
    if i not in temp:
        temp.append(i)

print(temp)  # [20, 30, 10, 40, 50, 70]


# -------------------------------

list1 = [34, 78, 90, 53 , 32]

# Combinations
# ans = [[34,34], [34,78], [34,90], [34,56], [34,32], [78,34],[78,78], [78,90], [78,56].....]

ans = []
for _ in list1:
    for t in list1:
        ans.append([_,t])

print(ans)  # [[34, 34], [34, 78], [34, 90], [34, 56], [34, 32], [78, 34], [78, 78], [78, 90], [78, 56], [78, 32], [90, 34], [90, 78], [90, 90], [90, 56], [90, 32], [56, 34], [56, 78], [56, 90], [56, 56], [56, 32], [32, 34], [32, 78], [32, 90], [32, 56], [32, 32]]


# List Comprehension
print()
print()
res = [[_,t] for _ in list1 for t in list1 if t % 2 != 0]
print(res)  # [[34, 53], [78, 53], [90, 53], [53, 53], [32, 53]]