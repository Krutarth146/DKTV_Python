# # int x = 10;

# x = 90333333333333
# print(x)  # Int

# y = 321212121211.12
# print(y)  # 321212121211.12
# print(type(y))  # <class 'float'>

# _ = "Royal1"
# print(_)
# print(type(_))  # <class 'str'>

# _1 = "S"
# print(type(_1))  # <class 'str'>

# f1_1 = True
# print(type(f1_1))  # <class 'bool'>

# www = 89+2j  # 89 is real part, 2j is Imaginary Part 

# w1 = 6j
# print(type(w1))  # <class 'complex'>

# '''
# Multi
# Line
# Comment
# '''


# # from __future__ import print_function
# # import raw_input()


# print('''
#     Hello,
#     This is 
#     Triple quoatation
# ''')

# x = 90
# y = 70

# print("x =",x,"y =",y)   # x = 90 y = 70
# print(x,y)  # 90 70
# print(x,y,sep='\n')  # 90 
#                     #  70


# print("Hello",end=' Krutarth ')
# print("Vraj")   # Hello Krutarth Vraj


# # scanf("%d",&roll);


# # roll = int(input("Enter Number: "))
# # print(roll)   # 44

# # age = input('ENter Age: ')
# # print(age)   # 11


# # print(int(age) + roll)  # 1144   # Concat


# print(ord('Z'))  # 90
# print(ord('d'))  # 100
# print(chr(102))  # f
# print(chr(86))   # V


# num1 = int(input("Enter First number: "))
# num2 = int(input("Enter Second number: "))

# print(num1,'+',num2,'=',num1+num2)   # 200 + 100 = 300
# print(f"{num1} + {num2} = {num1 + num2}")   # fstring
# print(f"{num1} - {num2} = {num1 - num2}")   # fstring
# print(f"{num1} * {num2} = {num1 * num2}")   # fstring
# print(f"{num1} / {num2} = {num1 / num2}")   # fstring
# print(f"{num1} // {num2} = {num1 // num2}")   # fstring
# print(f"{num1} % {num2} = {num1 % num2}")   # fstring
# print(f"{num1} ** {num2} = {num1 ** num2}")   # fstring


# Task

# Calc, 5 Areas, Simple Interest
# Take seconds as Input from User and Calculate Total Hours, minutes and Remaining seconds
# Take Days as Input from User and Calculate Total Years, months and Remaining days
# Operator Precedence andf associativity (R & D) (Image)


# Take Days as Input from User and Calculate Total Years, months and Remaining days

days = int(input("ENter Total Days: "))

year = days // 365
months = (days % 365) // 30
rem_days = (days % 365) % 30

print(f"Total Years = {year}, months = {months}, remaining Days are {rem_days}")