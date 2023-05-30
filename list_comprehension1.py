list1 = [10,20,30,41,61]

res = [i for i in list1 if i % 2 != 0]
print(res)

ans = [j for j in list1 if j > 20]
print(ans)

list1 = [10,20,30,40,50]

for u in list1:
    for h in list1:
        print(u,h)

jk = [(d,h) for d in list1 for h in list1]
print(jk)  # [(10, 10), (10, 20), (10, 30), (10, 40), (10, 50), (20, 10), (20, 20), (20, 30), (20, 40), (20, 50), (30, 10), (30, 20), (30, 30), (30, 40), (30, 50), (40, 10), (40, 20), (40, 30), (40, 40), (40, 50), (50, 10), (50, 20), (50, 30), (50, 40), (50, 50)]


lst4 = [10,33,44,22,12,56]

print()
res1 = [(i,j) for i,j in enumerate(lst4,5)]
print(res1)

tup1 = (10,20,30,40,50,88)
tup2 = (40,60,80,60,33)

v1 = [i for i in zip(tup1,tup2)]

print(v1)

task = [[1,2,3],
        [5,6,7],
        [9,8,7]]



freq = int(input())

main = []
temp = []

for i in range(3):
    temp = [int(x) for x in input().split()]
    main.append(temp)

print(main)

# ----------------------------------------

# 10 20 30 
# 40 50 60 
# 70 80 90