# 3. Extract Unique Values in a Given Dictionary
# -> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

ans1 = []
for i,j in D1.items():
    ans1.extend(j)

print(sorted(list(set(ans1))))


# Set ------> Don't Allow Duplicates, Unordered, Unchangeble
# Set items are unchangeable, but you can remove items and add new items.

set1 = {}
print(type(set1))   # dict

set2 = {20}
print(type(set2))  #  <class 'set'>

set3 = set()
print(type(set3)) #  <class 'set'>


set1 = {10,10,10,10,20,30,90.08, True, 78+9j, "Krrish", (10,20,30,40)}
print(set1)  # {True, (78+9j), 10, (10, 20, 30, 40), 20, 90.08, 'Krrish', 30}

print(len(set1))   # 8
print(id(set1))   # 2129811836480
print(set1.__sizeof__())   # 712


set1.add(5000)
print(set1)  # {'Krrish', True, 5000, (78+9j), 10, (10, 20, 30, 40), 20, 90.08, 30}

# set1.update([77,44,2,3,1])
set1.update((77,44,2,3,1))
print(set1)   # {True, 2, 3, 5000, (78+9j), 10, 44, 77, (10, 20, 30, 40), 20, 'Krrish', 90.08, 30}

# set1.clear()
# print(set1(5000))   # Gives Error
# print(dict1['5000'])

# del set1

set2 = set1.copy()   # Shallow Copy

set3 = set1  # Deep Copy


set1.add(1000)
set3.add(400)
print(set1)  # {True, 2, 3, 5000, (78+9j), 10, 1000, 44, 77, 400, (10, 20, 30, 40), 20, 90.08, 'Krrish', 30}
print(set2)  # {True, 2, 3, 5000, (78+9j), 10, 44, 77, (10, 20, 30, 40), 20, 90.08, 30, 'Krrish'}
print(set3)  # {True, 2, 3, 5000, (78+9j), 10, 1000, 44, 77, 400, (10, 20, 30, 40), 20, 90.08, 'Krrish', 30}ish'}


set1 = {10,20,30,40,50}
set2 = {40,50,60}

# print(set1.difference(set2))    # {10, 20, 30}
# print(id(set1))
# set1.difference_update(set2)
# print(id(set1))
# print(set1)


print(set1.intersection(set2))   # {40, 50}

# set1.intersection_update(set2)   # {40, 50}
print(set1)

set1.union(set2)
print(set1.union(set2))   # {50, 20, 40, 10, 60, 30}

print(set1.symmetric_difference(set2))     # {10, 20, 60, 30}
print(set1.difference(set2))  # {10, 20, 30}

set1.discard(20)
print(set1)


set1 = {10,20,300}
set2 = {90,80,79}
print(set1.isdisjoint(set2))  # True


set1 = {10,20,300}
set2 = {10,20,300,900}
print(set1.issubset(set2))    # True

set1 = {10,20,300}
set2 = {10,20,300,900}
print(set2.issuperset(set1))   # True


x = set1.pop()

print(set1,x)

set1.remove(20)    # It Gives Error if ELement is Not Found
set1.discard(20)   # It Ignores the Error if Element is Not Found
print(set1)