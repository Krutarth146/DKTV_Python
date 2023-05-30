str1 = "Royal is Best Institute Ever123."

print(str1)
str2 = 'd'
print(str2)  # Immutable (Not Chnageble)
print(len(str1))   # 32  ---> Length starts from 1, Index starts from 0
# char arr1[10] = "Royal";  # Mutable
# arr1[2] = 'm';
print(str1.__sizeof__())   # 81
print(id(str1))

str2 = "Royal"
print(id(str2))  # 2391320638512
print(id(str2))  # 2391320638512
# str3 = "Institute"
str2 += "Ram" 
print(id(str2))  # 2391320638320
print(str2)  # RoyalRam

str1 = "Royal is Best Institute Ever123."

# Indexing And Slicing

# Indexing 
print(str1[0]) # R
print(str1[-1]) # .
print(str1[-6]) # .


# Slicing
# print(str1[start : end (n-1) : step (n-1)])
print(str1[0:])  # Royal is Best Institute Ever123.
print(str1[2:8])  # yal is
print(str1[8:2])  # blank
print(str1[8:2:1])  # blank
print(str1[::])  # Royal is Best Institute Ever123.
print(str1[:4:])  # Roya
print(str1[3::2])  # a sBs nttt vr2.
print(str1[::-1])  # .321revE etutitsnI tseB si layoR
print(str1[::-2])  # a sBs nttt vr2.
print(str1[2:7:-2])  # 
print(str1[7:2:-2])  # s a
print(str1[-1:-6:2])  # 
print(str1[-3:3:2])  # 



# string Methods

str1 = "Royal_is Best Institute Ever123."
print(str1.capitalize())  # Royal_is best institute ever123.
print(str1.title())  # Royal_Is Best Institute Ever123.
print(str1.upper())  # ROYAL_IS BEST INSTITUTE EVER123.
print(str1.lower())  # royal_is best institute ever123.
print(str1.swapcase())  # rOYAL_IS bEST iNSTITUTE eVER123.
print(str1.swapcase())  # rOYAL_IS bEST iNSTITUTE eVER123.
print(str1.isupper())  # False
print(str1.islower())  # False
print(str1.istitle())  # False
print(str1.casefold())  # royal_is best institute ever123.


print(len(str1))  # 32
print(str1.center(40,'*'))  # ****Royal_is Best Institute Ever123.****

print(str1.count('yoal'))  # 0
print(str1.count('oyal'))  # 1

print(str1.find('z'))  # -1
print(str1.find('e'))  # 10
print(str1.rfind('e'))  # 26
# print(str1.index('z'))  # Generates Error if element is Not Found


str1 = "ROyal_is Best Institute Ever123."

print(len(str1))   # 32
print(str1.center(40,'*'))  #  ****ROyal_is Best Institute Ever123.****
print(str1.encode())


str2 = "Ståle"
print(str2.encode())   # b'St\xc3\xa5le'
print(str2.encode(encoding='ascii', errors="backslashreplace"))   # b'St\\xe5le'
print(str2.encode(encoding='ascii', errors="xmlcharrefreplace"))   # b'St&#229;le'
print(str2.encode(encoding='ascii', errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding='ascii', errors="ignore"))   # b'Stle'
print(str2.encode(encoding='ascii', errors="replace"))   # b'St?le'
print()


print(str1.endswith('23.'))  # True

str1 = "ROyal_is\tBest Institute Ever123."
print(str1.expandtabs(32))  # ROyal_is                        Best Institute Ever123. 

str1 = "ROyal_is Best Institute Ever123."

str3 = "{name} is {mode} student".format(name="Dev", mode="Very Bad")
str3 = "{} is {} student".format("Dev", "Good")
str3 = "{1} is {0} student".format("Dev", "Good")   # Good is Dev student
# print(str3.format(name="Dev", mode = "Bad"))  # Dev is Bad student
# print(str3.format(name="Dev", mode = "Bad"))  # Dev is Bad student
print(str3)


name = "Dev"
mode = "Bad"
print(f"{name} is {mode} Student.")


str3 = "{Name} is {mode} student"
dict1 = {"Name" : "Krutarth", "mode" : "Good"}
print(str3.format_map(dict1))   # Krutarth is Good student

print(str3.isdecimal())   # False
print(str3.isnumeric())   # False
print(str3.isdigit())   # False


str4 = "                    "
print(str4.isalnum())   # True
print(str4.isalpha())   # False
print(str4.isidentifier())  # True
print(str4.isascii())  # True
print(str4.istitle())  # False
print(str4.isspace())  # True


print('_'.join(str1))  # R_O_y_a_l___i_s_ _B_e_s_t_ _I_n_s_t_i_t_u_t_e_ _E_v_e_r_1_2_3_.
print(str1)   # ROyal_is Best Institute Ever123.

str1 = "        ROyal_       "
print(len(str1))   # 21
# print(str1.ljust())
print(str1.rjust(30,'*'))   # *********        ROyal_
print(str1.ljust(30,'*'))   #         ROyal_       *********
print(str1.strip())   # ROyal_




str1 = "ShreeS Fam"

# print(str1.replace("S","F"))   # Fhree Fam
# print(str1.replace("S","F",1))   # Fhree Fam


table = str1.maketrans('F','R',"S")
print(table)  # {70: 82}
print(str1.translate(table))


str1 = "ROyal_is Best Institute Ever123."
print(str1)

print(str1.partition(' '))    # ('ROyal_is', ' ', 'Best Institute Ever123.')
print(str1.rpartition(' '))   # ('ROyal_is Best Institute', ' ', 'Ever123.')
 
print(str1.split('i'))   # ['ROyal_', 's Best Inst', 'tute Ever123.']
print(str1.rsplit('i'))   # ['ROyal_is', 'Best', 'Institute', 'Ever123.']

print(str1.removeprefix("ROya"))  # l_is Best Institute Ever123.
print(str1.removesuffix("23."))  # ROyal_is Best Institute Ever1

print(str1.find('z'))  # -1
print(str1.rfind('i'))  # 18
# print(str1.rindex("z"))  # Generates Error If element is Not Found

print(len(str1))   # 32 # Length starts from 1, Index starts from 0
print(str1.rjust(40,'*'))
print(str1.center(40,'*'))


str1 = "ROyal_is\nBest Instit\nute Ever123."
print(str1.lower().find('i',7,15))   # 14

print(str1.splitlines())  # ['ROyal_is', 'Best Instit', 'ute Ever123.']

print(str1.startswith("Oyal"))
str1 = "ROyal_is Best Institute Ever123."
print(str1.title())   # Royal_Is Best Institute Ever123.

str2 = '5000'
print(str2.zfill(6))   # 005000



# oye balle balle oye



# OyE BallE BallE OyE

# Is string Plindrome or not???
str1 = "Nayan"
if str1 == str1[::-1]:   # Without using this Method but Use Function with retrun type
    print("Palindrome")

# 1 to 10000 Armstrong Number Using FUnc. Type - 4


# String Programs

# 1. Write a Py program that takes your full Name and Print Like This :
# Input - Krutarth Daxeshbhai Patel
# o/p   - K.D.Patel

# 2. Find NUmber of spaces characters in a given str.
# input - Python Programming

# o/p - vowels - 4, white spaces - 1, consonents - 13

# 3. write a py program to make a new string
# input  - This is the lion in the cage.
# o/ p - This is lion in cage.

# 4. WAP:
# input - Keep yourself Mute while not speaking
# output - Keep_yourself Mute while not#speaking

# 5. Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 3 + 33 + 333 + 3333 + 33333 = ???

# (num ** 3)


# 6. Write a Python function that checks whether a passed string is palindrome or not.

# 7. Write a Py program to calculate the factorial of a number (a non-negative integer).

# 8. Python program to find second largest number in a list.  // Null


# Programming Excercises:
"""
1. Ask user for an integer & print whether it's a perfect number or not.
    eg, 56
    factors of 56: 1 + 2 + 4 + 7 + 8 + 14 + 28 = 64 != 56
    eg, 28
    factors of 28: 1 + 2 + 4 + 7 + 14 = 28
2. Ask two integers from user and print all the perfect numbers between those two numbers
3. Ask user for a 3-digit integer & print whether it's an Armstrong number or not. A 3-digit integer is an Armstrong number if sum of cubes of all of its digits equals to the number itself.
    eg, 153:
    (1^3) + (5^3) + (3^3) = 153
"""
"""
a = int(input("Enter two integers:\n"))
b = int(input())
for n in range(a, b+1):
    # n = int(input("n : "))
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if sum(factors) == n:
        # print("Perfect.")
        print(n)
    # else:
    #     print("Not Perfect.")
"""
# HW:
"""
4. Ask user for a an integer & print whether it's an Armstrong number or not. An x-digit integer is an Armstrong number if sum of x-powers of all of its digits equals to the number itself.
    eg, 1634:
    (1^4) + (6^4) + (3^4) + (4^4)
    = 1 + 1296 + 81 + 256
    = 1634
5. Ask two integers from user and print all the Armstrong numbers between those two numbers
6. Given an array of integers A, find and return the minimum elements to be removed such that in the resulting array the sum of any two adjacent values is even.

Input Format:
The only argument given is the integer array A.
Output Format:
Return the minimum number of elements to be removed.

Program Constraints:
1 <= length of the array <= 100000
-10^9 <= A[i] <= 10^9 

Examples:
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    1
"""


# if 'a' < 'b':
#     print("Big")

# chr()
# ord()


# 3 + 33 + 333 + 3333 + 33333 = ?



num = 3
sum = 0
sum += 3
safe = num
mul = 10
print(num)
for i in range(4):
    num = (num % mul) * 10 + safe   
    sum += num  # 3 + 33 + 333 + 3333 + 33333
    mul *= 10

    print(num)

print(sum)