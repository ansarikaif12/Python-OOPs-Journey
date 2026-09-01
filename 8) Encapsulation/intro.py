# Encapsulation: Wrapping data and functions into a single unit(object).

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account = BankAccount(5000)

print(account.get_balance())

account.deposit(2000)

print(account.get_balance())



# ahan __balance private variable hai:

# self.__balance

# Isliye ise directly access karne ki jagah methods ke through access kiya ja raha hai:

# account.get_balance()
# account.deposit(2000)
# Python mein access levels

# Python mein access modifiers ke liye mainly naming conventions use hoti hain.

# Public:

# class Student:

#     def __init__(self):
#         self.name = "Kaif"

# Directly access kar sakte hain:

# s = Student()
# print(s.name)

# Protected:

# class Student:

#     def __init__(self):
#         self._name = "Kaif"

# _name protected convention hai. Technically ise access kiya ja sakta hai, lekin _ indicate karta hai ki member ko class/subclass ke context mein use karna intended hai.

# Private:

# class Student:

#     def __init__(self):
#         self.__name = "Kaif"
# s = Student()

# print(s.__name)   # Error

# __name private convention hai; Python iske liye name mangling use karta hai.

# Interview definition:

# Encapsulation is the process of bundling data and methods into a single class and restricting direct access to some data.