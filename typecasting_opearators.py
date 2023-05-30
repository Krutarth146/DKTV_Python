# To convert One Datatype into another Datatype

# 1. Implicit TYpecasting
# 2. Explicit Typecasting


v = False
w = 56

print(v+w)   # 56   # IMplicit

x = '34.90'
print(int(float(x)))   # 34  # Explicit Typecasting

q = 34.99
print(int(q))   # 34


import math
print(math.ceil(q))   # 35
print(math.floor(q))  # 34

str1 = '23'
print(int(str1))  # 23

print(type(str1))   # <class 'str'>

s = 90j
print(34 + s)   # (34+90j)


# Operators

# 1. Arithmetic O/p
# 2. Assignment O/p -> Priority Low
# 3. Logical o/p
# 4. Comparison O/p  (Relational)
# 5. Bitwise O/p
# 6. Identity o/p
# 7. Membership o/p


# 1. 23 + 90  -> 90 is Opearand, + is Opearator
# Arithmetic O/p + - * / // % **

# 2. Assignment O/p
# = += -= /= *= //= <<= >>= &= |= ^=

x = 10

y = 90
y += 1   # y = y + 1   # y = 91
y /= 3   # 30.33333
y -= 21  # 9.33333
y %= 2   # 1.33333333

print(y)   # 1.33333333


# Bitwise O/p  & | ^ << >>

# & Table  (A * B)

# I/p 1     I/p 2     RES
#  0         0         0
#  0         1         0
#  1         0         0
#  1         1         1

# Or Table (A + B)

# I/p 1     I/p 2     RES
#  0         0         0
#  0         1         1
#  1         0         1
#  1         1         1

# ^ Table (Same = 0)

# I/p 1     I/p 2     RES
#  0         0         0
#  0         1         1
#  1         0         1
#  1         1         0


print(45 & 21)   # 5    
# 101101
# 010101
# ---------
# & 000101

# 000101

print(45 | 89)
print(452 & 9012)
print(422 ^ 1242)
print(422 << 5)
print(422 >> 3)


