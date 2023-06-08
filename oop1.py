# class , Object

# class Student
# {
#     int id; 
#     string name;
#     float marks;

#     void set_data(int id, string name, float marks)
#     {   
#         this->id = id;
        # name = name;
        # marks = marks;
#     }

#     void display()
#     {
#         cout<<id<<name<<marks;
#     }
# };




# # Structure ---> User DEfined Datatype


# class Student
# {
#     int a;  # 2 byte
#     char name[10]; # 10 Bytes
#     float marks; # 4 Bytes

    # student()  # Autocalling
    # {
            # a = 90;
    # }
# };

# main()
# {
#              int      a;
#     struct Student  Dhrav;
#            Student  s1;

# }

# Constructor-----> Special Type of Method


# Self == this Pointer

# Class - Blueprint 
# object - isinstanceof class


class Bank:
    ROI = 5   # Class Member Variable

    def __init__(self):   # Constructor
        self.name = None   # Instance Member Variable
        self.balance = 0   # Instance Member Variable

    def deposit(self, money):  # Instance Method
        if money > 0:
            self.balance += money

    def withdraw(self,money):
        if money < 0 or (self.balance - money) < 5000:
            print("Not Allowed")
        else:
            self.balance -= money

    def check_bal(self):
        print(f"Your Ac. Bal is {self.balance}")

    @classmethod
    def increse_ROI(cls):
        cls.ROI += 2

    def calc_money(self):
        self.balance += (self.balance * Bank.ROI) / 100
        


# Bank b1;  In CPP
dhruv = Bank()
dhrav = Bank()
krrish = Bank()

dhruv.deposit(10000)
dhruv.check_bal()
dhruv.withdraw(8000)
dhruv.withdraw(2000)
dhruv.check_bal()
dhruv.increse_ROI()
dhruv.calc_money()
dhruv.check_bal()

dhruv.address = "India"
print(dhruv.address)  # India
# print(dhrav.address)  # India


print(dhrav.ROI)  # 7
print(dhruv.ROI)  # 7
print(krrish.ROI)  # 7

Bank.ROI = 20

print(dhrav.ROI)  # 7
print(dhruv.ROI)  # 7
print(krrish.ROI)  # 7

dhruv.ROI = 78

print(dhrav.ROI)  # 20
print(dhruv.ROI)  # 78
print(krrish.ROI)  # 20