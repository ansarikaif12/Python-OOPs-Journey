
# class Student:
#     college_name="NIET College" # here college_name is called class attribute
#     # parameterized constructors
#     def __init__(self, name, marks):
#         self.name=name  # here self.name, self.marks are called instance attribute 
#         self.marks=marks
#         print("adding new student in database..")

# s1=Student("Kaif Ansari",90)
# print(s1.name,s1.marks)

# s2=Student("Maxxxx",99)
# print(s2.name,s2.marks)

# print(s2.college_name)

# print(Student.college_name)




# ===================================================================


# concept: same name ka class attribute or same name ka object attribute hota hai to object attribute ki precedence class attribute se high hoti hai

class Student:
    college_name="NIET College" # here college_name is called class attribute
    name="anonymous" #class attribute
    
    # parameterized constructors
    def __init__(self, name, marks):
        self.name=name  # here self.name, self.marks are called instance attribute 
        self.marks=marks
        print("adding new student in database..")

s1=Student("Kaif Ansari",90)
print(s1.name)