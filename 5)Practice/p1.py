# create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average.

# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3

#     def avgMarks(self):
#         total=self.m1+self.m2+self.m3
#         return total/3


# s1=Student("Kaif",10,20,30)
# print(s1.avgMarks())

# ==============================================OR===============================


class Student:
    def __init__(self, name,m1):
        self.name=name
        self.m1=m1
        

    def avgMarks(self):
        sum=0
        for i in self.m1:
            sum+=i
        print("Hi",self.name,"your avg score is:",sum/3)


s1=Student("Kaif",[10,20,30])
s1.avgMarks()

s1.name="Ansari"
s1.avgMarks()