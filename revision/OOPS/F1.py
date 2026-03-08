class student:

    def __init__(self):  #default constructor
       pass


    @staticmethod
    def yo():
        print("YO!")

     
    def __init__(self, name, age):  

        #parameterized constructor

        self.name = name
        self.age = age
        
s1 = student("Amey", 99)
print(s1.name, s1 .age)
student.yo()







# class student:
#     name = "Amey"

# s1 = student()
# print(s1.name)

# class mobile:
#     brand = "Realme"
#     model = "Realme 15 Pro"

# mobile1 = mobile()   #object
# print(mobile1.brand)
# print(mobile1.model)


