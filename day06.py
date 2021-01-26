from day06_class import Student

# red_calc = Calculator()
# blue_calc = Calculator()

# red_calc.setting('red', 15, 5)
# blue_calc.setting('blue', 20, 15)

# print(f"color of the red calculator: {red_calc.color}")
# print(f"color of the blue calculator: {blue_calc.color}")

# print(f"add result of the red calculator: {red_calc.add()}")
# print(f"add result of the blue calculator: {blue_calc.add()}")


# def menu_info():

#     print("")
#     print("*** 계좌 관리 프로그램 ***")
#     print("1. 계좌 정보 조회")
#     print("2. 입금하기")
#     print("3. 출금하기")
#     print("4. 잔액 조회")
#     print("5. 프로그램 종료")


# def reg_account():
#     bank_name = input("은행명: ")
#     owner_name = input("예금주명: ")
#     password = int(input("비밀번호: "))

#     acc = Account(bank_name, owner_name, password)
#     print(f"{acc.owner} 님의 계좌가 생성 되었습니다.")

#     return acc


# def account_info():
#     print("account information")
#     print(f"Bank: {acc.bank}")
#     print(f"Owner: {acc.owner}")
#     print(f"Balance: {acc.get_balance()}")
    
# def deposit_acc():
#     #use password
#     pw = int(input("Please input the password: "))
#     if pw == acc.pw:
#         money = int(input("Please input the money to deposit: "))
#         acc.deposit(money)
#     else:
#         print("Wrong Password. Process is exterminated.")

# def withdraw_acc():
#     #use password
#     pw = int(input("Please input the password: "))
#     if pw == acc.pw:
#         money = int(input("Please input the money to withdraw: "))
#         acc.withdraw(money)
#     else:
#         print("Wrong Password. Process is exterminated.")

# def check_balance():
#     print(f"Your balance is now: {acc.get_balance()}")


# acc = reg_account()
# sel = 0

# while sel != 5:
    
#     menu_info()
#     sel = int(input("Please input your order: "))

#     if sel == 1:
#         account_info()
#     elif sel == 2:
#         deposit_acc()
#     elif sel == 3:
#         withdraw_acc()
#     elif sel == 4:
#         check_balance()
#     elif sel == 5:
#         print("프로그램을 종료합니다.")
#     else:
#         print("잘못된 입력입니다.")

def show_point_ui():
    print("")
    print(" "*18, "*** Report Card ***")
    print("=" * 55)
    print("ID   Name   Kor   Eng   Math   Total   Average   Grade")
    print("=" * 55)

# stu = Student()
# stu.input_stu_info()
# stu.calc_tot_avg_grade()
# show_point_ui()
# stu.output_stu_info()

def get_record_everyone():
    show_point_ui()
    
    class_avg = 0
    class_num = 0
    for stu in student:        
        stu.output_stu_info()
        class_avg += stu.avg
        class_num += 1
    print(f"The average of my class: {class_avg/class_num:.2f}")


def input_record():
    if not student: #Is the list empty?
        print("=========")
        print("no record")
        print("=========")
    else:
        get_record_everyone()
    
    stu = Student()
    stu.input_stu_info()
    stu.calc_tot_avg_grade()
    for who in student:
        if stu.id == who.id:
            print("ID is duplicated. Please check again.")
            break
    else:
        student.append(stu)  
    
    print("Record creating is complete.")


def get_record_individual():
    stu_num = input("Input the Student ID to check: ")
    for stu in student:
        if stu.id == stu_num:
            show_point_ui()
            stu.output_stu_info()
            break
        else:
            continue
    else:
        print("There is no ID in this class. Please check again.")


def modify_record():
    stu_num = input("Input the Student ID to modify: ")
    for stu in student:
        if stu.id == stu_num:
            show_point_ui()
            stu.output_stu_info()
            print(f"Start to modifying {stu.name}'s record'.")
            modify_record_indivisual(stu)
            break
        else:
            continue
    else:
        print("There is no ID in this class. Please check again.")

def modify_record_indivisual(stu):
    sel = 0
    while sel != 4:
        print("")
        print("Select the class to modify")
        print("1. Korean")
        print("2. English")
        print("3. Mathmatics")
        print("4. Stop modifying")
        print("")
        sel = int(input("Please select: "))

        if sel == 1:
            stu.modify_kor()
            show_point_ui()
            stu.output_stu_info()
        elif sel == 2:
            stu.modify_eng()
            show_point_ui()
            stu.output_stu_info()
        elif sel == 3:
            stu.modify_math()
            show_point_ui()
            stu.output_stu_info()
        elif sel == 4:
            print("Stop modifying.")
        else:
            print("Wrong number.")

def delete_record():
    get_record_everyone()
    
    stu_num = input("Please input the Student ID to delete: ")
    for who in student:
        if stu_num == who.id:
            student.remove(who)
            break
    else:
        print("There is no ID in this class. Please check again.")
    
    print("Record deletion is complete.")


def menu_info():
    print("")
    print("Grade mangement program")
    print("1. Input the record")
    print("2. Check records of everyone")
    print("3. Check indivisual record")
    print("4. Modify the record")
    print("5. Delete the record")
    print("6. Stop the program")
    print("")

sel = 0
student = []

while sel != 6:
    menu_info()
    sel = int(input("Please input the menu number: "))

    if sel == 1:
        input_record()
    elif sel == 2:
        get_record_everyone()
    elif sel == 3:
        get_record_individual()
    elif sel == 4:
        modify_record()
    elif sel == 5:
        delete_record()
    elif sel == 6:
        print("Stop the program. Bye.")
    else:
        print("Wrong selection.")