# Single Inheritance  ---> Inherits the Property from another class

class Father():
    ROI = 9000   # class variable

    def __init__(self, car, house_name):
        self.car = car
        self.house = house_name

    def show_property(self):   #  Instance Method
        print(self.car, self.house)
        # print(Father.ROI)
        # print("Hello")

# class Dhrav : public Father
class Dhrav(Father):
    def __init__(self, car_name, house_name):  
        super().__init__(car_name, house_name)
        self.bag = "sdvsdvsdv"
        self.laptop = None

    def show_details(self):
        print(self.bag, self.laptop)


# f1 = Father()
d1 = Dhrav("Creta", "Dhrav_delux")
d1.show_details()
d1.show_property()



num1 = 9


if num1 % 2 == 0:
    i = num1  # i = 9

    while i < num1 * 3:   # 9 < 27
        print(i,end=' ')
        i+=2
else:
    i = num1  # i = 9

    while i < num1 * 3:   # 9 < 27
        print(i,end=' ')
        i+=2


str1 = '( ()) ((()()())) (()) ()'      
str2 = ""
l1 = []
for i in str1.replace(' ',''):
    # print(i)
    str2 += i

    if str2.count('(') == str2.count(')'):
        l1.append(str2)
        str2 = ""

print(l1)  # ['(())', '((()()()))', '(())', '()']