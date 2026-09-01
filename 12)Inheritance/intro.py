# when one class(child/derived) derives the properties & methods of another class(parent/base)

# Single Inheritance================================================

# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")


# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name

# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")

# print(car1.name)
# print(car1.start())
# print(car1.color)

#-----------------------------------------------------------------

# MULTI-LEVEL INHERITANCE=========================================


# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")


# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self,typ):
#         self.type=type


# car1=Fortuner("diesel")
# car1.start()

#---------------------------------------------------------------

# MULTIPLE INHERITANCE==========================================

# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="Welcome to class C"

# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


#--------------------------------------------------------------

# 4. Hierarchical Inheritance=======================================

# Ek parent se multiple child classes:

    #    Animal
    #    /    \
    #  Dog     Cat
# class Animal:

#     def eat(self):
#         print("Eating")


# class Dog(Animal):

#     def bark(self):
#         print("Barking")


# class Cat(Animal):

#     def meow(self):
#         print("Meowing")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()

# Dog aur Cat, dono Animal se inherit karte hain.

# ------------------------------------------------------------------

# 5. Hybrid Inheritance=============================================

# Jab inheritance ke do ya usse zyada forms combine hote hain, use hybrid inheritance kehte hain.

#        A
#       / \
#      B   C
#       \ /
#        D

# class A:

#     def show_a(self):
#         print("A")


# class B(A):

#     def show_b(self):
#         print("B")


# class C(A):

#     def show_c(self):
#         print("C")


# class D(B, C):

#     def show_d(self):
#         print("D")


# obj = D()

# obj.show_a()
# obj.show_b()
# obj.show_c()
# obj.show_d()

# Yahan hierarchical aur multiple inheritance ka combination hai.