# Functions

# 1. Func. Defination
# 2. Func. Calling


#include<stdio.h>
# void add();


# void add()
# {
#     int a,b;
#     printf("%d",a+b);
# }

# main()
# {
#     add();
#     varsv
#     dvdv
#     dv

# }



# Func. Types

# 1. without return Type and W/o args.
# 2. without return Type and With args.
# 3. with return Type and W/o args.
# 4. with return Type and with args.


# 1. without return Type and W/o args.


def Add():    # Func. Defination
    print(3+2)


Add()   # 5   # Func. Calling


# 2. without return Type and With args.

def dev(num1 , num2):
    print(num1 + float(num2))

dev(89.25,'90.89')   # 180.14

print(dev(90,45))   # None

# 3. with return Type and W/o args.

def krrish():
    list1 = [10,20,30,90]
    return 90/2,list1,True

# krrish()  # No answer
print(krrish())  # 45.0
x = krrish()   # (45.0, [10, 20, 30, 90], True)
print(x)       # (45.0, [10, 20, 30, 90], True)


# 4. with return Type and with args.

# def Bhatt(_, _1, _2 = None):
def Bhatt(_, _1, _2 = 0):
    # print(type(_2))   # <class 'NoneType'>
    return _ ,_1 ,_2

print(Bhatt('20','90'))   # 20


# ------------------------------------

def patel(*royal):
    print(royal)

# patel("str1", 90.90, 78, True)
patel()   # ()


def dhruv(num1, num2, *args, wala=90.89):
    for i in args:
        print(i)

    print(num1,num2)
    print(type(args))   # <class 'tuple'>
    print(args[2] + wala)


dhruv(10,20,50,90,4444,'Manoj')   # 4462


# kwargs  ---> Dictionary

def khush(*args, **rohan):
    print(type(rohan))  # <class 'dict'>
    print(rohan)
    print(rohan.keys())     # dict_keys(['name', 'roll', 'salary'])
    print(rohan.values())   # dict_values(['Dhruv', 900, 10000000000])
    print(rohan.items())   # dict_items([('name', 'Dhruv'), ('roll', 900), ('salary', 10000000000)])
    print(type(rohan.items()))   # <class 'dict_items'>

khush(90,89,67,"str1",name = "Dhruv", roll = 900, salary = 10000000000)   # {'name': 'Dhruv', 'roll': 900, 'salary': 10000000000}