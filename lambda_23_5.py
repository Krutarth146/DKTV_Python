# Quadratic Function

# (a * x ** 2) + (b * x) + c


def quadratic_fun(a,b,c):
    return lambda x : (a * x ** 2) + (b * x) + c

dhruv = quadratic_fun(10,20,30)

print(dhruv(5))  # 380
# -------------------------------------------------------
list1 = [(10,89), (333,45), (21,43), (23,4), (21, 90)]
res = []
k = 2

for i in list1:  # (10,89)
    flag = 1
    for j in i:  # j = 10
        if len(str(j)) != k:
            flag=0
            break
    if flag != 0:   
        res.append(i)

print(res)   # [(10, 89), (21, 43), (21, 90)]


print([i for i in list1 if all(len(str(j)) == k for j in i)])
   # [(10, 89), (21, 43), (21, 90)]

# l1 = [45,-90.89,True,0]
# print(all(l1))   # False

# Nested Lambda


res = lambda x = 25 : lambda y : x+y

dhruv1 = res()
print(dhruv1(40))  # 65


#-  - - - - - - - - - - -- - - - - - - 

royal = lambda n1,n2 : lambda f : (n1 **f) + n2

techno = royal(10,2)(4)
print(techno)   # 10002



l1 = [(10,20) , (34,98), (55,89)]
l2 = [(20,10) , (34,90), (89,555), (10,20), (3,4,2), (34,98)]

# FInd Common Elements