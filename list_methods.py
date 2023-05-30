list1 = [10,33,44,55,66]

print(list1)  # [10, 33, 44, 55, 66]

print(type(list1))  # <class 'list'>
print(list1.__sizeof__())   # 88
print(id(list1))   # 1904062093568

# Indexing and Slicing

print(list1[0])   # 10
print(list1[-2])  # 55
print(type(list1[-2]))  # <class 'int'>

# Slicing

# print(list1[start : end(n-1)]) 
list1 = [10,33,44,55,66]
print(list1[2:5])  # [44, 55, 66]
print(list1[5:2])  # []
print(type(list1[5:2]))  # <class 'list'>
print(list1[:])  # [10,33,44,55,66]
print(list1[3:])  # [55, 66]
print(list1[:2])  # [10, 33]
print(list1[-4:-1])  # [10, 33]
print(list1[-1:-4])  # []

# step value

print(list1[1:4:1])  # step - 1 (n-1) 1. Positive/ Negative  2. skip
print(list1[4:1:1])  # []

list1 = [10,33,44,55,66]
print(list1[4:1:-1])  # [66, 55, 44]
print(list1[-1:-4:-3])  # [66]
print(list1[-1:-4:])  # []
print(list1[:-3:])  # [10, 33]
print(list1[1:-4:])  # []
print(list1[-2:2:2])  # []
print(list1[-2:2:-2])  # [55]


# List Methods

list1.append(100)
print(list1)   # [10, 33, 44, 55, 66, 100]

list1.append("Dhruv")
print(list1)  # [10, 33, 44, 55, 66, 100, 'Dhruv']

# list1.extend(800)  # int Not supported

list1.extend('800')
print(list1)  # [10, 33, 44, 55, 66, 100, 'Dhruv', '8', '0', '0']   

list2 = [3,34,5,6,7,3,2]

# list1.append(list2)
# print(list1)    # [10, 33, 44, 55, 66, 100, 'Dhruv', '8', '0', '0', [3, 34, 5, 6, 7, 3, 2]]

list1.extend(list2)
print(list1)   # [10, 33, 44, 55, 66, 100, 'Dhruv', '8', '0', '0', 3, 34, 5, 6, 7, 3, 2]

print(type(list1[-2]))   # <class 'int'>


list1.insert(2,8657)
print(list1)
list1.insert(-1,8000)
print(list1)  # [10, 33, 8657, 44, 55, 66, 100, 'Dhruv', '8', '0', '0', 3, 34, 5, 6, 7, 3, 8000, 2]

list1[2] = 3300
print(list1)

list1+=list2

print(list1)  # [10, 33, 3300, 44, 55, 66, 100, 'Dhruv', '8', '0', '0', 3, 34, 5, 6, 7, 3, 8000, 2, 3, 34, 5, 6, 7, 3, 2]

# Remove Elements ----------

# list1.clear()
# print(list1)   # []

list1.pop()
print(list1)   # [10, 33, 3300, 44, 55, 66, 100, 'Dhruv', '8', '0', '0', 3, 34, 5, 6, 7, 3, 8000, 2, 3, 34, 5, 6, 7, 3]

list1.pop(3)

print(list1)  # [10, 33, 3300, 55, 66, 100, 'Dhruv', '8', '0', '0', 3, 34, 5, 6, 7, 3, 8000, 2, 3, 34, 5, 6, 7, 3]

# Colab

list1.remove("Dhruv")
print(list1)   # [10, 33, 3300, 55, 66, 100, '8', '0', '0', 3, 34, 5, 6, 7, 3, 8000, 2, 3, 34, 5, 6, 7, 3]

# del list1
del list1[6:]
print(list1)   # [10, 33, 3300, 55, 66, 100]


list2 = list1.copy()  # shallow Copy

list3 = list1   # Deep copy

list1.append(5000)
print(list2)  # [10, 33, 3300, 55, 66, 100]
print(list3)  # [10, 33, 3300, 55, 66, 100, 5000]

list3.append(3222)

print(list1)  # [10, 33, 3300, 55, 66, 100, 5000, 3222]
 
print(list1.count(3222))  # 1
print(list1.index(3222))  # 7
list1.reverse()
print(list1)   # [3222, 5000, 100, 66, 55, 3300, 33, 10]

list1.sort()
print(list1)  # [10, 33, 55, 66, 100, 3222, 3300, 5000]


list1.sort(reverse=True)
print(list1)   # [5000, 3300, 3222, 100, 66, 55, 33, 10]


# -----------


for i in list1:
    print(i,end=' ')   # 5000 3300 3222 100 66 55 33 10


for h in range(len(list1)):
    print(list1[h])

list1 = [(102,0,30,4), (30,43,50), (202,202,22,44,11)]

for i in list1:
    print(i)


for i in list1:
    for f in i:
        if f % 2 != 0:
            print(f)




'''
Task-:
1. Create a list of Fruits(15 exotic fruits)
take user input and check if the fruits are avail in the list
if available print "fruit_name is Available"


2. create a list of numbers(15 numbers (1-100))
sort that list in ascending order
search for the number in the list
take input from user and find all the occurence
print the occurence


Tasks-: 
    1. Wap to find no. of month from the given no. of days
    2. wap to scan seconds and print hour, minute and remaining seconds
    3. wap to swap 3 numbers that is scanned by the user (a->b, b->c, c->a)
    4. wap to check whether the number is odd or even
    5. wap to find out the maximum, minimum, average of the numbers that is scanned by the user
    6. wap to make any user inputted string in uppercase or lowercase
    7. wap to print the sum of user entered numbers (scan by the user)
    8. wap to find power of a number
    9. wap to print numbers between n1 and n2 (n1, n2 are scanned by the user)
    
    Finale-: Make a Python program that generates a list of powers of base that is given by user upto the power given by user.    
    eg: base = 2, power=10
    output: [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

    list programs
    1. add 5 numbers into the list and print the list
    2. add 10 numbers into the list, reverse that list, store the list into another list and print the list
    3. add 10 numbers into the list, sort that list and print the list
    4. add 10 numbers into the list, remove the duplicates and print the list
    5. add 10 numbers into the list, print the maximum and minimum number from the list
    6. add 10 numbers into the list, print the average of the list
    7. add 10 numbers into the list, print the sum of the list
    8. scan 5 numbers from the user and store it into the list, check if both the lists are same or not
    9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
    # Ask user for quantity
    # Assume each unit's cost is 100.
    # Judge and print total cost for user. 

    10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

    11. A school has following rules for grading system:
    # a. Below 25 - F
    # b. 25 to 45 - E
    # c. 45 to 50 - D
    # d. 50 to 60 - C
    # e. 60 to 80 - B
    # f. Above 80 - A
    # Ask user to enter marks and print the corresponding grade.

    12. A student will not be allowed to sit in exam if his/her attendance is less than 75%.
    # Take following input from user:
    # Number of classes held
    # Number of classes attended.
    # And print:
    # percentage of class attended
    # Is student is allowed to sit in exam or not.

'''


a = 90

b = a



print(id(a))
print(id(b))

if a is b:
    print("Same")
else:
    print("Not Same")


# 1. Create a list of Fruits(15 exotic fruits)
# take user input and check if the fruits are avail in the list
# if available print "fruit_name is Available"

