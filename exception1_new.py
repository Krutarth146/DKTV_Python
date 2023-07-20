# # import math

# # print(math.exp(10.90))  # 54176.36379669875
# # print(math.exp(1000))  # 54176.36379669875


# dict1 = {'a' : 'Akbar'}

# try:
#     print(dict1['a'])

# # except Exception as err:
# except Exception as err:
#     print(err)
# else:
#     print("successfully run")

# # def func():
# #     print(name)

# # func()



# # User Defined Exception


# class Error(Exception):
#     """Base class for other Exceptions"""
#     pass

# class DhruvZeroDivision(Error):
#     pass

# try:
#     num = int(input("Enter Number : "))
#     if num == 0:
#         # num / 0
#         raise DhruvZeroDivision


# # except ZeroDivisionError:
# #     print("Inbuilt Zero Division Error")


# except DhruvZeroDivision:
#     print("Input Value is Zero")

# # except Exception as e:
#     print("Inbilt Error: ",e)

# e1 = Error()
# print(e1.__doc__)




# def print_details(num):
#     for i in range(num):
#         yield i


# for i in print_details(5):
#     print(i)






l3 = [3,3,4,5,56,21,2,22,4,45,5,6]

dict1 = {}


unique = []

for i in l3:
    if i not in unique:
        unique.append(i)

for element in unique:   # element = 3
    temp = []
    for ind in range(len(l3)):  # j ---> 0 to 11
        if element == l3[ind]:  # 3 == 3
            temp.append(l3.index(element,ind))   # [0,1]

    dict1[element] = temp

print(dict1)   # {3: [0, 1], 4: [2, 8], 5: [3, 10], 56: [4], 21: [5], 2: [6], 22: [7], 45: [9], 6: [11]}

dict2 = {element : [ind for ind in range(len(l3)) if element == l3[ind]] for element in set(l3)}
print(dict2)
# x = 0
# c = 0.0
# temp = {}
# temp = set()
# temp = []

# {3 : [0,1], 4 : [2,8]}


# list1 = [10,20,30,10,10]

# print(list1.index(10,1))
# print(list1.index(10))


list1 = [(390,10), (32,45) ,(21,34), (33,8), (23,2)]


for i in range(len(list1)):   # i = (390,10)
    for j in range(i+1,len(list1)):
        if list1[i][1] > list1[j][1]:   # 10 > 45
            list1[i], list1[j] = list1[j], list1[i]

print(list1)   # [(23, 2), (33, 8), (390, 10), (21, 34), (32, 45)]