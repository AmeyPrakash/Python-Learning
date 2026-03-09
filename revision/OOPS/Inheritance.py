# class student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno

# s1 = student("Alice", 123)
# print(s1.name)  # Output: Alice
# del s1.name

# class account:
#     def __init__(self, acc_no, ac_pass):
#         self.__account_number = acc_no   #private
#         self.__account_password = ac_pass  #private

#     def reset_pass(self):
#         print(self.__account_password)  #can access (private)

# ac1 = account("23456", "xyz") 

# ac1.reset_pass() 


# same can be done with variables and methods of parent class in child class using inheritance


                # INHERITANCE
#when a class is derived from another class, it is called inheritance. The derived class inherits all the features of the base class and can have additional features of its own. Inheritance provides code reusability and establishes a natural hierarchical relationship between classes.


class car:     #Parent class 
    color = "Azure"
    @staticmethod
    def start():
        print("Car started.")
    @staticmethod
    def stop():
        print("Car stopped.")


class electric_car(car):  #child class        
    def __init__(self, name):
        self.name = name


class hybrid_car(electric_car):  #child class
    def __init__(self, type):
        self.type = type

car1 = hybrid_car("Petrol")
car1.start()  # Inherited method from car class