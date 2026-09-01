# Methods that don't use the self parameter (work at class level)
# Decorators allows us to wrap another function in order to extend the behvaiour of the wrapped function, without permannetly nodifying it.

class Student:
    def __init__(self, name,m1):
        self.name=name
        self.m1=m1

    @staticmethod   #decorator
    def hello(): #here self ka koi work nhi hai to staticmethod use krte hai
        print("Hello")

    def avgMarks(self):
        sum=0
        for i in self.m1:
            sum+=i
        print("Hi",self.name,"your avg score is:",sum/3)


s1=Student("Kaif",[10,20,30])
s1.avgMarks()

s1.name="Ansari"
s1.avgMarks()

s1.hello()