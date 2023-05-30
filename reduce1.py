list1 = [10, 90, 56, 78, 35]

from functools import reduce

x = reduce(lambda x,y : x + y, list1)
print(x)   # 269

from itertools import accumulate

y = list(accumulate(list1, lambda x,y : x + y))
print(y)   # [10, 100, 156, 234, 269]

def max1(x,y):
    return x if x > y else y
list1 = [10, 90, 56, 78, 35]
r = reduce(lambda x, y : x if x > y else y,list1)
print(r)


l1 = [(10,3390,3787,432) , (34, 90, 42, 21), (33,99,77)]

# for i in range(len(l1)):
#     if l1[i][-2] > l1[i+1][-2]:
#         pass
        # swap

# ---------------------

# Recursion

# When Function calls Itself then it is called as Recursion

# FIbonnacci ------------

# n1 = 0
# n2 = 1

# print(n1,n2,end=' ')

# for i in range(5-2):
#     n3 = n1 + n2
#     print(n3,end= ' ')
#     n1 = n2
#     n2 = n3

# Fibonacci in Recursive
print()
print()

from functools import lru_cache
import time

t_rec = time.time()
@lru_cache(maxsize=1000)
def fibonacci_rec(num):
    if num == 0:   # Base Condition
        return num
    elif num == 1:
        return num
    
    return fibonacci_rec(num-1) + fibonacci_rec(num-2)

# print(fibonacci_rec(5))  # 5

for i in range(5):
    print(fibonacci_rec(i),end=' ')
print("Recursion Execution time: ",time.time() - t_rec)



# Reduce, Recursion (Factorial) 10 Programs


# Iterators
i_rec = time.time()
def fibonacci_iterators(num):
    list1 = [0,1]
    for i in range(num):
        list1.append(list1[-1] + list1[-2])

    return list1[-1]
# print()
# print()
# print()
print(fibonacci_iterators(4))
print("Iteration Execution time: ",time.time() - i_rec)