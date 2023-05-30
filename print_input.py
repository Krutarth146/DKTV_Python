print("""
    Hello, 
    This is Krutarth
    Ahm
    380001
""")

print("Hello Krutarth",end=' Royal ')
print("Tarjani")  # Hello Royal Tarjani

# Python -> Dyanamic, Interpreted Language


# Runtime Memory Allocation, Not require datatype declaration

# int x, y;

x = 90
print(type(x))   # <class 'int'>

y = 888.90
print(type(y))  # <class 'float'>


z = "T"
print(type(z))  # <class 'str'>

_ = "Tarjani"

print(_,z,sep = ' **** ')   # Tarjani **** T

# Typecasting, Datatypes, Input()

x = '90'
print(type(x))  # <class 'str'>

y = 800000000000000000000000000
print(type(y))   # <class 'int'>

g = 8923333333333332.23
print(type(g))   # <class 'float'>

j = "Krutarth"
print(type(j))  # str

e = True
print(type(e))   # <class 'bool'>

w = None
print(type(w))   # <class 'NoneType'>

d = 90+7j
print(type(d))  # <class 'complex'>  -> 90 is Real Part, 7j is Imaginary Part

w = [10,20.90,"acsdcsdc",True,89+8j,[10,20,30,[10,20,30]], (30,40,506), {30,30,303,40,30}, {"Name" : "Krutarth", 90:56.32}]

print(w)  # [10, 20.9, 'acsdcsdc', True, (89+8j), [10, 20, 30, [10, 20, 30]], (30, 40, 506), {40, 30, 303}, {'Name': 'Krutarth', 90: 56.32}]


e = (10,320,30,40)

print(type(e))  # Tuple


x = {10,20,30,40,10,10}
print(type(x))  # <class 'set'>

dict1 = {}
print(type(dict1))   # <class 'dict'>

dict1 = {"Roll" : [10,20,30,40,50], "Address" : {"Area" : ("Ahm", 'Annand'), 'state' : "Guj"}}
print(type(dict1))   # <class 'dict'>
print(dict1)   # {'Roll': [10, 20, 30, 40, 50], 'Address': {'Area': ('Ahm', 'Annand'), 'state': 'Guj'}}


# scanf("%d",&tarjani);
# print("Enter element: ")
# tarjani = input()
# print(tarjani)     # 1000
# print(type(tarjani))   # <class 'str'>

# kru = input("Enter element: ")
# kru1 = input("Enter element: ")
# print(kru)
# print(kru1)

# print(kru + kru1)  # 3311  str

# x = 90
# y = input()

# print(x+y)   # gives Error

# Typecasting -> one datatype to another datatype  1. Implicit Typecasting  2. Explicit Typecasting

# x = 67
# j = True   # 1

# print(x+j)   # 68  # Implicit Typecasting

# print(int("A"))  # Gives Error

s = "89.78"

print(int(float(s)))  # Explicit Typecsating  # 89

import math

f= 89.9999
print(math.floor(f))   # 89
print(math.ceil(f))    # 90

# Calc, 5 Areas, Simple Interest
# Take seconds as Input from User and Calculate Total Hours, minutes and Remaining seconds
# Take Days as Input from User and Calculate Total Years, months and Remaining days
# Operator Precedence andf associativity (R & D) (Image)
x = 90
y= 80
print(x,"+",y,"=",x+y)  # 90 + 80 = 170
print(x,"-",y,"=",x-y)  # 90 + 80 = 170
print(x,"+",y,"=",x*y)  # 90 + 80 = 170
print(x,"+",y,"=",x/y)  # 90 + 80 = 170    # 25 / 2 = 12.5
print(x,"+",y,"=",x//y)  # 90 + 80 = 170   # floor return in int  # 25 // 2 = 12
print(x,"+",y,"=",x%y)  # 90 + 80 = 170
print(x,"+",y,"=",x**y)  # 90 + 80 = 170   # Exponencial  # 2**3 -> 8   # 2**3**2 -> 2**9 -> 512