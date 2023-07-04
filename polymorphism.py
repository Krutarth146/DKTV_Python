# Poly---> Many, Morph ---> forms

# Having Same Name but Different Types (Signature)
# Ex. Right ---> r-wrong, left - right
# Ex. who ----> kon, who - k j

print(len("Kruatrth"))  # 8

print(len([10,20,30]))   # 3


# UDF

def fun(a,b,c=0):
    print(a)
    print(b)


# def fun(a,b,c):
#     print(a,b,c)


# fun(10,20,90)   # 10 20 90

fun(10,20)
fun("Dhruv", "Krrish")

def fun(l):
    for x in l:
        print(x)

fun([10,20,30,40,50,60,70])  # 10 20


'''
Dhruv's Code

# Poly--->Many, Morph--->forms

# Having same name but different types(Signature)
# Ex Right--->r-wrong,left-right
#ex who---> kon,who--->KJ

# print(len("Krutarth"))
# print(len([10,20,30]))

# UDF
# def fun(a,b,c=0):
#     print(a,b)

# def fun(a,b,c):
#     print(a,b,c)

# fun(10,20,30)
# fun(10,20)
# fun("Dhruv","Krrish")

# def fun(l):
#     for x in l:
#         print(x)
# fun([10,20,30,40])

# class polymorph:
#     def meth(self):
#         print("Meth withour arg in polymorph")
    # def meth(self,a):
    #     print(a," Meth with one arg in polymorph")

# class subpolymorph(polymorph):
#     def _init_(self) -> None:
#         print("")
#     def meth(self):
#         print("Meth without arg in subpolymorph")
    # def meth(self,a):
    #     print(a," Meth with one arg in polymorph")
    # def meth(self,a,b):
    #     print(a,b,"Meth with 2 arg in subpolymorph")

# class child(polymorph):
#     def meth(self):
#         print("Meth withour arg in Child")

# list1=[subpolymorph(),child(),polymorph()]
# for i in list1:
    # print(i)
    # i.meth()

# p1=subpolymorph()
# p1.meth()
# p1.meth(10)
# p1.meth(10,11)
class cls1:
    def method1(self):
        print("Method in cls1")

class cls2:
    def method1(self):
        print("Method in cls2")

def meth1(obj):
    obj.method1()

# list1=[cls1(),cls2()]
# for i in list1:
#     i.method1()
#     meth1(i)


class polymorph:
    def meth(self):
        print("Meth without arg in polymorph")
    # def meth(self,a):
    #     print(a," Meth with one arg in polymorph")
    def meth1(self):
        print("Meth1 in polymorph")

class subpolymorph(polymorph):
    def _init_(self) -> None:
        print("")
    def meth(self):
        print("Meth without arg in subpolymorph")
    # def meth(self,a):
    #     print(a," Meth with one arg in polymorph")
    # def meth(self,a,b):
    #     print(a,b,"Meth with 2 arg in subpolymorph")

class child(polymorph):
    def meth(self):
        print("Meth withour arg in Child")
p1=child()
p1.meth1()
'''