list1 = [[10,20,30,40,50], 
         [60,70,80,90,100]]

print(list1[1][2])   # 80


for i in list1:   # i = [10,20,30,40,50]
    for g in i:   # g = 10
        print(g,end=' ')
    print()

print()
print()
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(list1[i][j],end=' ')
    print()

list2 = [[10,20,30],
         [40,50,60],
         [70,80,90]]

print()
print()
for i in range(len(list2)):   # 0 to 2     i = 0
    if i % 2 != 0:
        for j in range(len(list2[i])-1,-1,-1):  # 0 to 2   j = 0
            print(list2[i][j],end=' ')
        print()
    else:
        for j in range(0,len(list2[i])):
            print(list2[i][j],end=' ')
        print()

# 1. 10 20 30 60 90 80 70 40 50


# 2. 30 + 50 + 70 = sum

# 3. Palindrome

str1 = "Tarjani"
rev = "inajraT"

if str1 == str1[::-1]:
    print("Palindrome")

# 4. Matrix Identical or not???
# 5. Matrix Transpose