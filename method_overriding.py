class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def print_details(self):
        print(self.id, self.name)

class SalesEmployee(Employee):
    def __init__(self, id, name, si):
        super().__init__(id, name)
        self.si = si

    def print_details(self):
        super().print_details()
        print(self.si)


el = [Employee(101,"Dhruv"), SalesEmployee(102,"Krrish", 700)]

for x in el:
    x.print_details()