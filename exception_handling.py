# printa(89/0)

# print("Hello")

# IOError
# AttributeError
# Import Error
# Value Error
# Type Error  # 5 + "Dhruv"
# Name Error
# Syntax Error
# Zero Division
# Index Error

# Exception: when program is syntatically correct but code results in Error.


num = 90
name = "Dhruv"

try:
    ans = num + name
except TypeError:
    print("Error: can not add int + str")


print("Hello")


# ----------------------

list1 = [10,900,89]

try:
    # print("%d" %(list1[1]/0))
    # print("%d" %(list1[8]))
    print("%d" %(list1[-1]//0))
# except ValueError:
#     print("Value Error")
except IndexError:
    print("Index Error")
except ZeroDivisionError:
    print("Not Divisible By 0")
except:
    print("Error Generated")
else:
    print("Dhruv Panwala")

finally:
    print("Always Executed")

# print("Hello")


# try:
    # raise NameError("Name Errrorrrrrrrrrrrrrrr")
# except NameError:
    # print("An Exception")
    # raise


# ------------------------------------------------


# Built-in Exceptions

# def factorial(num):
#     mul = 1
#     for i in range(1,num+1):
#         mul = mul * i
#         yield mul   # Generator

# for j in factorial(5):
#     print(j)



def gener1():
    try:
        for i in range(5):
            print("yeilding", i)
            yield i
    except GeneratorExit:
        print("Exiting Early")

g1 = gener1()

print(type(g1))  # <class 'generator'>
print (g1.__next__())
print (g1.__next__())
print (g1.__next__())
g1.close()


# In file 
import os

def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write("Hello World")
    except IOError:
        print("Could not create a file")


def read_file(filename):
    try:
        with open(filename,'r') as f1:
            x = f1.read()
            print(x)
    except IOError:
        print("Could Not Read a File")

def deletefile(old_file_name, new_file_name):
    try:
        # os.remove(filename)
        os.rename(old_file_name, new_file_name)
        print("File successfully Deleted.")
    except IOError:
        print("Could not Delete a File")

if __name__ == '__main__':
    filename = "dhruv.txt"
    create_file(filename)
    read_file(filename)
    deletefile(filename)


def indexing(list1):

    try:
        print(list1[21])
    except LookupError:
        print("Index out of Range")
    else:
        print("success")

indexing([10,20,30])


# Inbulit, User Defined, nzec Error

