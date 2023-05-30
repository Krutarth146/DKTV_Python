# for(i=1;i<=50;i++)
# {
#     printf("%d",i);
# }

for t in range(10):   # Intialization -> 0, End = 10 (n-1)
    print(t,end=' ')   # 0 1 2 3 4 5 6 7 8 9 

print()
print()

for h in range(2,18):   # start -> 2, End - 17
    print(h,end=' ')   # 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17

print()

for w in range(2,18,1):    # step -> 1 (default) (n-1)
    print(w,end=' ')   # # 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
print()

for w in range(2,18,2):    # step -> 1 (default) (n-1)
    print(w,end=' ')   # 2 4 6 8 10 12 14 16

print()

for w in range(18,2,2):   
    print(w,end=' ')   # blank
print()

for w in range(18,2,-1):   
    print(w,end=' ')   # 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3

print()


for q in range(-9,-1,-3):
    print(q,end=' ')  # blank

print()

for d in range(-4,3,2):
    print(d,end=' ')   # -4 -2 0 2



# List :  Allow Duplicates, Ordered

list1 = [10,20,90.89,20,True,6+90j,"Tarjani", 'S', [10,20,30], (21,45.90,"Manoj"), {"set1", "set1"}, {"Name" : "Dhruv", "address" : {'city' : "Ahm", "state" : "Gujarat"}}]

print(list1)   # [10, 20, 90.89, 20, True, (6+90j), 'Tarjani', 'S', [10, 20, 30], (21, 45.9, 'Manoj'), {'set1'}, {'Name': 'Dhruv', 'address': {'city': 'Ahm', 'state': 'Gujarat'}}]


list2 = [10,20,30,40,50,60]

for _ in list2:
    print(_,end=' ')   # 10 20 30 40 50 60
print()

for w in range(len(list2)):
    print(list2[w])   # list1[5]

# print(len(list2))  # 6
# print(list2.__sizeof__())   # 88


list1 = [(10,20,30), (40,50,60), (90,90,89), (20,304)]


for _ in list1:
    print(_)  # (10, 20, 30)  (40, 50, 60) (90, 90, 89)  (20, 304)



for big in list1:  # (10, 20, 30)
    for small in big:
        print(small,end=' ')

    print()

# List : Allow Duplicates, Ordered, Mutable (Changeble)

list1 = [10,2,30,40,50,60]

# Indexing

print(list1[2])  # 30
print(type(list1[-1])) # <class 'int'>

# Slicing

# print(list1[start : end (n-1)])
print(list1[0:4])   # [10,2,30,40]

print(list1[-2:-1])   # # [50]
print(type(list1[-2:-1]))  # <class 'list'>