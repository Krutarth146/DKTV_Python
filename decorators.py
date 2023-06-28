# Decorators is First Class Object

# Function can have Inner Functions

# It Takes Another Function as an Argument

def fun1():
    print("Inside Fun1")


def fun2(f):
    print("Inside fun2")
    f()


# fun2(fun1)

f = fun1
f()   # Inside Fun1
print()
print(type(f))   # <class 'function'>
fun2(f)

# Inside fun2
# Inside Fun1


# ---------------------------------------

def fun5(f):
    def innerfun():
        print("Dhruv")
        f()

    return innerfun


@fun5
def fun():
    print("Krutarth")

# fun = fun5(fun)
fun()