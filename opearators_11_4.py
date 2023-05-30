# Logical Operators    # and or not
# Comparison Operator  -> == < > <= >= != (Relational O/p)

# and or not

# print(56 and 100)  # 100
# print(56 or 100)  # 56

# age = int(input())
# name = input()

# if age > 18:
#     print(name,"is Eligible for Voting")
#     print(f"{name} is Eligible for Voting")   # fstring
# elif age == 0 or age < 0:
#     print("Please Enter Valid Age")
# else:
#     print(f"{name} is not Eligible for Voting, Need {18-age} Years.")

# Loop -> Entry Control Loops  1. For      2. While
# While Loop

x = 22    # Intialization

while x <= 44:   # Condition
    print(x,end=' ')
    x += 1   # 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 

print()
print()
_ = 100
while _ >= 25:
    if _ % 5 == 0 and (_ % 7 == 0 or _ % 10 == 0):
        print(_,end=' ')   # 100 90 80 70 60 50 40 35 30
    _-=1

print()
# print(_1)  # 24


num1 = 900
num2 = 800
num3 = 5600

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Greater")
    else:
        print(f"{num3} is Greater")
else:
    if num2 > num3:
        print(f"{num2} is Greater")
    else:
        print(f"{num3} is Greater")


print(num1 if num1 > num2 else num2)   # Hw 3 Variables Match

a = 90

if not(a < 100):
    print(True)
else:
    print(False)



# For Loop 

# while -3:   # True
#     print("Ram")
#     break

x = 33
while x<=50:
    x+=1
    if x % 3 == 0:
        continue
    print(x)


list1 = [10,20,390,490,89]
user_need = int(input("Enter any Number: "))



# Linear Search
for w in list1:   # # Membership O/p   in    not in
    if w == user_need:
        print(f"{user_need} is Found")
        break


if user_need not in list1:    # Membership O/p
    print(f"{user_need} is Found")
else:
    print(f"{user_need} is not Found")

tup1 = (10,20,30,40,(10,20,30))

for dhruv in tup1:
    print(dhruv,end=' ')
print(dhruv)


x = 9000
y = 9000


if x == y:
    print("x same as Y")
else:
    print(False)


if x is y:   # Identity O/p   is   is not
    print("x is Y")
else:
    print("Not")


list1 = [10,20,30]
list2 = [10,20,30]

if list1 == list2:   # Match Elements
    print("list1 same as list2")
else:
    print(False)


if list1 is list2:   # Identity O/p   is   is not   # MAtch Reference
    print("list1 is List2")
else:
    print("Not")



# ------------------
list3 = list2

if list3 is list2:
    print("list3 is List2")



# While -> Sum of Digits, Sum of Numbers, Find Power, Reverse Number Print, Palindrome (1 to 10000), Armstrong (1 to 10000), Prime (1 to 10000) All Methods, Perfect Number, Twin Number