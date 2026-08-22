# __init__ Function

# Constructor:
# All classes have a function called __init__(), which is always exceuted when the class is being initiated
# ye jo function hai wo object creation k time pr invoke hota hai 
# constructor hmesha ek argument leta hai that is self jo ki first parameter hota hai (jrurui nhi hai ki self hi ho isko ham apne taraf se bhi name assign kr skte hai)
# The self parameter is a reference to the current instance of the class , and is used to access variables that belongs to the class.
# variables, data are called attributes



class Student:
    name="Kaif"
    def __init__(self):
        print(self)
        print("adding new student in database..")

# creating object (instance)
s1=Student()
print(s1)
print(s1.name)

s2=Student()
print(s2.name)




# ======================================================================





class Student:
    def __init__(self, fullname):
        self.name=fullname
        print("adding new student in database..")

s1=Student("Kaif Ansari")
print(s1.name)

s2=Student("Maxxxx")
print(s2.name)



# ======================================================================




class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")

s1=Student("Kaif Ansari",90)
print(s1.name,s1.marks)

s2=Student("Maxxxx",99)
print(s2.name,s2.marks)