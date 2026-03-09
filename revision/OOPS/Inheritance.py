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


# class car:     #Parent class 
#     color = "Azure"
#     @staticmethod
#     def start():
#         print("Car started.")
#     @staticmethod
#     def stop():
#         print("Car stopped.")


# class electric_car(car):  #child class        
#     def __init__(self, name):
#         self.name = name


# class hybrid_car(electric_car):  #child class
#     def __init__(self, type):
#         self.type = type

# car1 = hybrid_car("Petrol")
# car1.start()  # Inherited method from car class



# multiple inheritance


# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varA)  # Inherited from class A
# print(c1.varB)  # Inherited from class B
# print(c1.varC)  # Defined in class C         

# Super Method   used to call the parent class constructor
# class car:     #Parent class 
#     color = "Azure"
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("Car started.")
#     @staticmethod
#     def stop():
#         print("Car stopped.")

#   #SUPER

# class hybrid_car(car):  #child class
#     def __init__(self, type):
#         super().__init__(type)  #calling parent class constructor
#         super().start()  #calling parent class method



#CLASS METHOD : A class method is a method that is bound to the class and not the instance of the class. It can modify a class state that applies across all instances of the class. Class methods are defined using the @classmethod decorator and take cls as the first parameter.


#static method doesn't can't access or modify class state. It is defined using the @staticmethod decorator and does not take cls or self as the first parameter. Static methods are used to perform utility functions that are related to the class but do not require access to instance or class variables.


# class Person:
#     name = "Amey"

#     def changename(self, name):
#         Person.name = name

# p1 = Person()
# p1.changename("Alice")
# print(p1.name)  # Output: Alice
# print(Person.name)  # Output: Alice (class variable is modified)

# class Person:
#     name = "Amey"

#     def changename(self, name):
#         self.__class__.name = "Alice"

# p1 = Person()
# p1.changename("Anshul") 
# print(p1.name)  # Output: Alice
# print(Person.name)  # Output: Alice (class variable is modified)

# class Person:
#     name = "Amey"
#     @classmethod      #change to amey (class att)
#     def changename(cls, name):
#         cls.name = name

# p1 = Person()
# p1.changename("Anshul")
# print(p1.name)  # Output: Anshul
# print(Person.name)  # Output: Anshul (class variable is modified)



# static no change
#class  (cls)
#instance (self) 

  #PROPERTY DECORATOR

class student:

    def __init__(self, phy, chem, math):  #default constructor
        self.phy = phy
        self.chem = chem
        self.math = math


    # def calcper(self):
    #     self.percenatge = str((self.phy + self.chem + self.math) / 3) + "%" 

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


s1 = student(90, 80, 70)
print(s1.percentage)        
s1.phy = 100
print(s1.percentage)  #percentage is not updated because it is calculated in constructor only 



#we use property decorator to make percentage as a property so that it is calculated every time we access it and not just in constructor (function itself property)