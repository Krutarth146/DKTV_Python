class Car:
    seating_capacity = 5        # class variable
    allCars = []                # class variable

    def __init__(self, name, price, fuel):
        self.name = name   # Instance Variable
        self.price = price  # Instance Variable
        self.fuel = fuel    # Instance Variable
        Car.allCars.append(self)

    # creating a method
    def displayDetails(self):  # Instance Method
        print(Car.allCars)  # [<__main__.Car object at 0x000001B93C07BEB0>, <__main__.Car object at 0x000001B93C07BE20>, <__main__.Car object at 0x000001B93C07BDC0>]
        print(f"---------- Details of {self.name} ----------")
        print("Model Name:", self.name)
        print("Price:", self.price)
        print("Fuel:", self.fuel)
        print("Seating Capacity:", self.seating_capacity)
        print()

    def displayallCars(cls):
        for i in range(len(cls.allCars)):
            print(cls.allCars[i].name)

    def changeDetails(self):  # Instance Method
        print("Enter new details (just press Enter if you want to keep that detail same):")
        self.name = input("Name: ")
        self.price = int(input("Price: "))
        self.fuel = input("Fuel: ")

    # static methods
    @staticmethod
    def showAllCars():
        print("Sr.No.\tName")
        for i in range(len(Car.allCars)):
            print(f"{i}\t{Car.allCars[i].name}")

    # class method:
    @classmethod
    def addNewCar(cls):
        print("Enter the following details:")
        name = input("Name: ")
        price = int(input("Price: "))
        fuel = input("Fuel: ")
        # Car.allCars.append(cls(name, price, fuel))
        return cls(name, price, fuel)
    
    @classmethod
    def deletecar(cls,carname):
        for i in range(len(Car.allCars)):
            print(Car.allCars[i].name)
            if Car.allCars[i].name == carname:
                Car.allCars[i].displayDetails()
                Car.allCars.remove(Car.allCars[i])
                # Car.displayallCars()
                break

  
        
                


c1 = Car("Elantra", 2500000, "Petrol")
# c1.displayDetails("Nothing")
# Car.allCars.append(c1)

c2 = Car("Verna", 1200000, "Petrol")
# Car.allCars.append(c2)
# c1.changeDetails()
# c1.displayDetails()
c3 = Car("Fortuner", 3500000, "Diesel")
# Car.allCars.append(c3)

"""
Press 1 - to add a new car
2 - display details of an existing car
3 - change details of an existing car
4 - delete a car
5 - exit
"""

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to display details of an exisiting car")
    print("3 to change details of an exisiting car")
    print("4 to delete an exisiting car")
    print("5 to exit")
    op = int(input())
    if op == 1:
        Car.addNewCar()

    elif op == 2:
        """
        Sr.No.  Name
        0       Elantra
        1       Verna
        2       Fortuner
        """
        Car.showAllCars()
        c = int(input("Sr.No:"))
        Car.allCars[c].displayDetails()


    elif op == 4:
        Car.showAllCars()
        carname=input("car name you want to remove:")
        Car.deletecar(carname)
        
    elif op == 3:
        Car.addNewCar()
        pass

    elif op == 5:
        exit()

# Car.allCars[0].displayDetails()
# Car.allCars[1].displayDetails()