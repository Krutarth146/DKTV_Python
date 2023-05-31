# Files ----> 1. Text File  2. Binary File

# Files Opening Modes::

# 'w' ---> Write Mode [Overwrite Data]

# 'r' ---> Read Mode [If file does not Exist then it will give Error]

# 'a' ---> Append Mode [Append Data]

# 'x' ---> If file exists then it will create an Error

# '+' ---> [Read + Write Mode]

# 't' ---> Text FIle

# 'b' ---> Binary FIle

# FILE *dev;

# dev = fopen("dhrav.txt","w");

# fp = open("dhrav.txt","at")
fp = open("dhrav.txt","wt")

fp.write("Hello Priyank! Good Afternoon!!\n")

list1 = ["Royal is Good Institute Ever.\n", "Dhrav is also good.\n", "Dev is Also Very Good Student\n"]

fp.writelines(list1)
# fp.read()  # GIves Error
fp.close()


fp = open("dhrav.txt","rt")

# x = fp.read()
# print(x)
print(fp.tell())   # 0
print(fp.readline())   # Hello Priyank! Good Afternoon!!
print(fp.tell())   # 33
print(fp.readline())   # Royal is Good Institute Ever.
print(fp.tell())   # 64
print(fp.readline())   # Dhrav is also good.
print(fp.tell())   # 85
print(fp.readline(3))   # Dev is Also Very Good Student
print(fp.tell())   # 88
print(fp.readline())   #  is Also Very Good Student
print(fp.tell())   # 116

fp.seek(64)
print(fp.readline())   #  Dhrav is also good.
print(fp.readline())   #  Dev is Also Very Good Student
print(fp.tell())       # 116
print(fp.readline())   #  

fp.seek(0)

x = fp.readlines()
print(x)   # ['Hello Priyank! Good Afternoon!!\n', 'Royal is Good Institute Ever.\n', 'Dhrav is also good.\n', 'Dev is Also Very Good Student\n']

counter = 0
chars = 0
for line in x:
    for q in line:
        chars += 1
    counter +=1
y_counter = 0

for line in x:
    words_list = line.split()
    print(words_list,"--->",len(words_list))

    for word in words_list:
        if word.endswith('y'):
            y_counter += 1

print(counter)  # 4
print(chars)    # 112

print(y_counter)   # 1
fp.close()


ph = open("dict1.png","rb")

bytes_code = ph.read()

# print(bytes_code)

ph.close()

jk = open("dict_copy.png","wb")
jk.write(bytes_code)
jk.close()


# Use Random Module  (1 to 10000) ---> Refer
# if random generated number is Prime then it must written in prime.txt
# if random generated number is Armstrong then it must written in armstrong.txt