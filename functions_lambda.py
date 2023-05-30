x = 90


def demo():
    global x
    x+=90
    print(x)   # 180
demo() 

print(x)  # 180

# -------------------------

# Lambda (Anounomus Function)


def square(num, str):
    return num ** 2

print(square(str = "Ashok", num = 90))   # 8100

ans = lambda num : num ** 2
print(ans(25))  # 625


mul = lambda num1, num2, num3 : num1 * num2 * num3
mul = lambda num1, num2, num3 : 90 * 90 + 89
mul = lambda num1, num2, num3 : '_'.join(num2)
print(mul('90','Dev Bhatt',90))   # D_e_v_ _B_h_a_t_t


converter = lambda x : print(int(x))
converter("78")

# a = 90
# b = 800
# c = 78

res = lambda a,b,c: print(a) if a > c else print(c) if a > b else print(b) if b>c else print(c)

res1 = lambda a,b,c: print(a) if a > c \
    else print(c) if a > b \
        else print(b) if b>c \
            else \
                print(c)


res(10,90,890)  # 890