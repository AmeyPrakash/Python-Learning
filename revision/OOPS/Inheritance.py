# class student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno

# s1 = student("Alice", 123)
# print(s1.name)  # Output: Alice
# del s1.name

class account:
    def __init__(self, acc_no, ac_pass):
        self.__account_number = acc_no   #private
        self.__account_password = ac_pass  #private

    def reset_pass(self):
        print(self.__account_password)  #can access (private)

ac1 = account("23456", "xyz") 

ac1.reset_pass() 