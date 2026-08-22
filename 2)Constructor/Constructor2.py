
class Student:
    # Deafult Constructors
    def __init__(self):
        pass

    # parameterized constructors
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("adding new student in database..")

s1=Student("Kaif Ansari",90)
print(s1.name,s1.marks)

s2=Student("Maxxxx",99)
print(s2.name,s2.marks)