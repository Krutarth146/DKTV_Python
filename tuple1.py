# Tuple = ()

tup1 = ()  # Imutable, Ordered (Indexed), Allow's Duplicates
print(type(tup1))  # <class 'tuple'>

tup2 = (10,20,30,10,10)
list2 = [10,20,30,10,10]
print(tup2)  # (10, 20, 30, 10, 10)
print(list2)  # (10, 20, 30, 10, 10)
print(list2.__sizeof__())  # 88
print(tup2.__sizeof__())   # 64

print(tup2[-2])  # 10
print(tup2[-4])  # 20
print(tup2[2:])  # (30, 10, 10)
print(tup2[-1:-3:-2])  # (10,)

tup2 = (90, 89.89 , True, 89 + 7j, [10,20,3], ((21),(89)), {89}, {"Name" : ['Dhruv','Nilay','Dev','Krishh']})
print(tup2)

print(tup2[-1]['Name'][1])   # Nilay
print(tup2[-1].get('Name')[1])   # Nilay

print(tup2.count({89}))  # 1

print(tup2.index(True))  # 2

tup3 = (10,20,30,10,10)
print(sum(tup3)// len(tup3))  # 16

print(max(tup3))  # 30

print(sorted(tup3))  # [10, 10, 10, 20, 30]


tup3 = list(tup3)
tup3.append("Hello")
# print(tuple(tup3))  # (10, 20, 30, 10, 10, 'Hello')
tup3 = tuple(tup3)
# print(type(tup3))


# tup3[2] = 900  # Error
print(id(tup3))   # 2225358320544
tup4 = (90,89)
tup3 += tup4   # (10, 20, 30, 10, 10, 'Hello', 90, 89)

print(id(tup3))  # 2225358738752
print(id(tup4))  # 2225358246912
print(tup3)


t1 = (10,20,30,40,50)

# user_need = int(input())

# for i in t1:
#     if i==user_need:
#         print("Element is Found")
#         break
# else:
#     print("Elemnet is Not Found")


t1 = (10,20,30,40,50,90,90)

list1 = sorted(t1)
print(list1)  # [10, 20, 30, 40, 50, 90, 90]

list1 = [i for i in range(1,101)]
need = int(input())

length = len(list1)  # 7
print(length,"-----")
start = 0
end = length-1   # End = 6

binary_counter = 0
while start <= end:
    mid = (start + end) // 2  # mid = 3
    if need == list1[mid]:
        print("Element is Found1")
        break
    elif need < list1[mid]:
        end = mid-1
    elif need > list1[mid]:
        start = mid+1
    binary_counter += 1
else:
    print("Fail")

# --------------------------
linear_counter = 0

for i in list1:
    if i == need:
        print("Element is Found2")
        break
    linear_counter += 1

print(linear_counter)
print(binary_counter)