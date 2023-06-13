# class Student
# {
#     private:
#     int id;
#     char name[10];
#     float marks;


#     public:
#     void set_data(int id, char s[] ,float marks)
#     {
#         this->id = id;
#     }
# };

# self.id = id
# self.name = Authenticate_name
    # void pointer, null pointer, Dangling Pointer, Wild Pointer


# Encapsulation

class Royal:
    no_of_students = 350  # class Variable  # Public Variable
    _password = 87654321    # Protected
    __Royal_bank_ac = 90000000000  # Private

    def __init__(self,name,admit_year):  # Constructor
        self.name = name
        self.year = admit_year
        self.group_name = self.name + str(self.year)

    @classmethod
    def change_password(cls):
        cls._password = input("Enter New Password: ")

    @classmethod  # Decorator
    def show_password(cls):
        print(cls._password)
        print(cls.__Royal_bank_ac)

    @staticmethod
    def check_no_of_students():
        print("Total Number of students are",Royal.check_no_of_students)


Royal.change_password()
Royal.show_password()
# print(Royal.password) # Error
print(Royal._password) # changed Password

# print(Royal.__Royal_bank_ac)

print(Royal._Royal__Royal_bank_ac)