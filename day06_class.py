# class Calculator:
    
#     def setting(self, color, n1, n2):
#         self.color = color
#         self.n1 = n1
#         self.n2 = n2

#     def add(self):
#         result = self.n1 + self.n2
#         return result

#     def sub(self):
#         result = self.n1 - self.n2
#         return result


# class Account:

#     def __init__(self, bank, owner, password):
#         #print("constructor is called")
#         self.balance = 0
#         self.bank = bank
#         self.owner = owner
#         self.pw = password

#     def set_balance(self, balance):
#         self.balance = balance

#     def get_balance(self):
#         return self.balance

#     def deposit(self, money):
#         self.balance += money

#     def withdraw(self, money):
#         if money > self.balance:
#             print("잔고가 부족합니다.")
#         else:
#             self.balance -= money

class Student:

    def __init__(self):
        self.id = None
        self.name = None
        self.kor = 0
        self.eng = 0
        self.math = 0
        self.tot = 0
        self.avg = 0.0
        self.grade = None
    
    def input_stu_info(self):
        self.id = input("student number: ")
        self.name = input("student name: ")
        self.kor = int(input("Korean point: "))
        self.eng = int(input("English point: "))
        self.math = int(input("Mathmatics point: "))
    
    def calc_tot_avg_grade(self):
        self.tot = self.kor + self.eng + self.math
        self.avg = self.tot / 3

        if self.avg >= 90:
            self.grade = 'A'
        elif self.avg >= 80:
            self.grade = 'B'
        elif self.avg >= 70:
            self.grade = 'C'
        elif self.avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def output_stu_info(self):
        print(f"{self.id:<8}{self.name:<5}{self.kor:<6}{self.eng:<6}{self.math:<6}{self.tot:<6}{self.avg:<10.2f}{self.grade:<6}")
    
    def modify_kor(self):
        self.kor = int(input(f"Input the {self.name}'s Korean record: "))
        self.calc_tot_avg_grade()

    def modify_eng(self):
        self.eng = int(input(f"Input the {self.name}'s English record: "))
        self.calc_tot_avg_grade()

    def modify_math(self):
        self.math = int(input(f"Input the {self.name}'s Mathmatics record: "))
        self.calc_tot_avg_grade()