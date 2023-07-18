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