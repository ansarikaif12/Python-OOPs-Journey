# Conceptual Implementations in Python
# Private attributes & methods are meant to be used only within the class and re not accessible from outside the class


class Student:
    def __init__(self,name):
        self.name=name
    
s1=Student("Kaif")

print(s1.name) #public access
del s1
# print(s1.name) #error




class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account(12345,"abcde")

print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.__acc_pass) #error


class Person:
    __name="Anonymous"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1=Person()
# print(p1.__name) #error
# print(p1.__hello()) #error
print(p1.welcome())
