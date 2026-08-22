#  methods are functions that belong to objects.

#  class ke andar data(attributes) aur methods hota hai


class Student:
    college_name="NIET College" # here college_name is called class attribute

    # parameterized constructors
    def __init__(self, name, marks):
        self.name=name  # here self.name, self.marks are called instance attribute 
        self.marks=marks
        print("adding new student in database..")

    def welcome(self): #self parameter likhna hi hai har methods me
        print("Welcome Student!!")
s1=Student("Kaif Ansari",90)
print(s1.name,s1.marks)
s1.welcome()
