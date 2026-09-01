# A class method is bound to the class & receives the class as an implicit fiirst argument.
# Note- static method can't access or modify class state & generally for utility.

# =====================================================================

# class Person:
#     name="anonymous"

#     def changeName(self,name):
#         self.name=name

# p1=Person()

# p1.changeName("Kaif Ansari")
# print(p1.name) # Kaif Ansari
# print(Person.name) # anonymous


# ===================================================================


# class Person:
#     name="anonymous"

#     def changeName(self,name):
#         Person.name=name

# p1=Person()

# p1.changeName("Kaif Ansari")
# print(p1.name) # Kaif Ansari
# print(Person.name) # Kaif Ansari 


# ===================================================================

# class Person:
#     name="anonymous"

#     def changeName(self,name):
#         self.__class__.name="Kaif Ansari"

# p1=Person()

# p1.changeName("Kaif Ansari")
# print(p1.name) # Kaif Ansari
# print(Person.name) # Kaif Ansari 


# ===================================================================


class Person:
    name="anonymous"

    # def changeName(obj,name):
    #     self.__class__.name="Kaif Ansari"

    @classmethod #decorator
    def changeName(cls, name):
        cls.name=name

p1=Person()
p1.changeName("Kaif Ansari")
print(p1.name) # Kaif Ansari
print(Person.name) # Kaif Ansari 