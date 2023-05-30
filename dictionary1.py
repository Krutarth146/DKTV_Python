dict1 = {}
print(type(dict1))  # <class 'dict'>

set1 = {}
print(type(set1))   # <class 'dict'>

# set2 = {10}
# print(type(set2))   # <class 'set'>

# # dict2 = {key : Value}  # Dict: ordered, Don't Allow Duplicates, Mutable (Changeble)

# dict2 = {"Name" : "Krutarth", "Roll":7008, 'Name' : "Manoj"}
# print(dict2)  # Key -> Unique

# # key -> Unique
# # values -> Allow's Duplicates


# print(dict2["Roll"])
# print(dict2["Name"])


# key1 = input("Enter any str value inform of key: ")
# value = input("Enter value: ")

# dict2.update({key1 : value})
# print(dict2)

# print(dict2['Name'])   # Manoj
# # print(dict2['Manoj']) 


# print(dict2.get('Roll'))   # 7008

dict3 = {'1001' : {'pName' : "5 Star", 'qn' : 340, 'price' : 10},
         '1002' : {'pName' : "Parle G", 'qn' : 200, 'price' : 5},
         '1003' : {'pName' : "Oats", 'qn' : 140, 'price' : 30},
         '1004' : {'pName' : "Oreo", 'qn' : 90, 'price' : 50}}

print(dict3)   # {'1001': {'pName': '5 Star', 'qn': 340, 'price': 10}, '1002': {'pName': 'Parle G', 'qn': 200, 'price': 5}, '1003': {'pName': 'Oats', 'qn': 140, 'price': 30}, '1004': {'pName': 'Oreo', 'qn': 90, 'price': 50}}

print(dict3['1002'])  # {'pName': 'Parle G', 'qn': 200, 'price': 5}
print(dict3['1002']['price'])  # 5
print(dict3['1002']['qn'])  # 5


# print(dict3.keys())

for h in dict3.keys():
    print(h)

for h in dict3.values():
    print(h)

for h,p in dict3.items():
    print(h,p)

for w in dict3:
    x = dict3[w]
    print(x.keys())
    print(w, dict3[w]['pName'], dict3[w]['price'])


# dict3.clear()
# print(dict3) # {}

# del dict3['1004']

print(dict3) 
    
list1 = ('str1', 'str2', 'str3')
val = 0
dict4 = dict.fromkeys(list1,val)
print(dict4)


temp = dict3.pop("1001")
print(temp)
print(dict3)


dict3.popitem()
print(dict3)

print(dict3.values())


car = {'Model' : 'ALto', 'price' : 900, 'Date' : '990000'}

car['Model'] = "BMW"
print(car)

# dict6 = ('Model')
y = car.setdefault('Date','20230202')
print(y)

print(car)

'''
1. Check if a Given Key Already Exists in Dictionary
-> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

D1 = {'first_name' : 'Krutarth', 'age' : 22, 'height' : 5.0 , 'job' : 'Developer', 'company': 'Google'}

2. Handle Missing Keys in Dictionary
-> Dictionary is a collection in python, where the data is stored in the form of a key-value pair, that is, it maps key to its value. Often, you will not know all the keys present in the dictionary and you might end up with a typing error which may lead to runtime error due to missing keys in the dictionary.

D1 = {'first_name' : 'Zafar', 'age' : 21, 'height' : 4.8 , 'job' : 'Engineer', 'company': 'Microsoft'}

3. Extract Unique Values in a Given Dictionary
-> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

D1 = {	'list1': [4, 7, 10, 20], 
      	'list2': [7, 16, 9, 10], 
     	'list3': [13, 10, 4, 8], 
     	'list4': [7, 20, 6, 11]
         }

Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]

4. Print the Sum of Key Value Pairs in a Given Dictionary
-> You need to create a list which has the sum of key-value pairs of a given dictionary. 

D1 = {2: 8, 5: 20, 3: 15}

HINT-> This can be done using a for loop and append() function. 

5. Replace Dictionary Values From Other Dictionary
-> Let’s say you are given two dictionaries. You need to write a python program that will replace the values in the first dictionary with the values from the second dictionary if the key is present in the second dictionary. 

# initializing D1 - first dictionary
D1 = {'first_name' : 'Rutvi', 'age' : 21, 'height' : 4.0 , 'job' : 'Software Engineer', 'company': 'Uber'}
 
# initializing D2 - - first dictionary
D2 = {'age' : 35, 'job' : 'senior data analyst'}

6. Update or Change the Keys in a Given Dictionary
-> try these 2 ways
i)  Using assignment operator
ii) Using pop() method

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

7. Delete a List of Keys in a Given Dictionary 

8. Count the Frequency of List Items Using a Dictionary
-> You can solve this in many ways. Any ideas? Well, you can just use looping constructs or use the list() count method or you can start with an empty dictionary and use the dict.get() method. Probably many other ways!

D1 = {'Niraj': 23, 'Krutarth': 29, 'Pushpa': 33, 'Sures': 40}

9. Change the Value of a Key in Nested Dictionary
-> Given a nested dictionary, you need to write a program demonstrating how to change the value associated with a particular key of that dictionary. 

#change the value of a key in nested dictionary
#Initializing Dictionary
D1 = {'emp1': {'name' : 'Niraj', 'age' : 21, 'job' : 'developer'}, 
      'emp2': {'name' : 'Zafar', 'age' : 22, 'job' : 'data analyst'}, 
      'emp3': {'name' : 'Rutvi', 'age' : 22, 'job' : 'data scientist'}, 
      'emp4': {'name' : 'Krutarth', 'age' : 60, 'job' : 'python developer'}}

11. Check if the Given Dictionary Is Empty or Not
-> One way to check this using the len() function, which you can try coding; we will achieve this using the bool() function. The bool() function evaluates to standard true or false and is used to return or convert a value to Boolean type. If you pass an empty dictionary, the bool() evaluates to False, as failure to convert something that is empty.

14. Get a Key From Value in a Dictionary
-> You need to write a program, which returns the key for a given value. This can be done in multiple ways. Try doing it using dict.items() function.

#get key for a given value using dict.items()
# Dictionary Initialization
D1 = {'Priyanka Chopra': 23, 'Alia Bhatt': 29, 'Hritik Roshan': 45, 'Ranbir Kapoor': 40}

15. Sort a Given Dictionary by Key
-> You know this so, you got this...

D1 = {'Niraj': 23, 'Jaynam': 29, 'Rutvi': 40, 'Zafar': 45, 'Obama': 34}
'''