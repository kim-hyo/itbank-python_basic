# a = 1234

# print(type(a))
# print(bin(a))
# print(oct(a))
# print(hex(a))


# file2 = r"c:\temp\abc\new.jpg"
# file3 = "c:\\temp\\abc\\new.jpg"

# print(f"file2 = {file2}, file3 = {file3}")

# lyrics = """링딩동
# 링딩동
# 링딩동"""

# print(f"lyrics={lyrics}")


# print("배고파 " * 3)



# dog = "멍멍이"
# cat = "야옹이"
# print(dog, cat, 23, sep=" ")
# print(dog, cat, 23, sep=", ")
# print(dog, cat, 23, sep="")

# THIS_YEAR = 2021

# name = input("이름: ")
# gender = input("성별: ")
# age = int(input("나이: "))
# birth = THIS_YEAR - age + 1

# print(f"이름은 {name}, 성별은 {gender}, 나이는 {age}세, 출생년도는 {birth}")





# height = int(input("키를 입력해주세요: "))
# age = int(input("나이를 입력해주세요: "))

# if (height >= 140) and (age >= 8):
#     print("놀이기구에 탑승 할 수 있습니다.")
# else:
#     print("놀이기구에 탐승 할 수 없습니다.")

# print("오늘 하루 즐거운 시간 되세요.")




# number = int(input("정수를 입력하세요: "))

# if (number == 0):
#     print("입력하신 숫자는 0입니다.")
# elif (number%5 == 0):
#     print("입력하신 숫자는 5의 배수입니다.")
# else:
#     print("입력하신 숫자는 5의 배수가 아닙니다.")




score = int(input("점수를 입력하세요: "))

if (score >= 90):
    if (score > 100):
        print("점수를 잘 못 입력했습니다.")
    elif (score >= 95):
        print("당신의 학점은 A+입니다.")
    else:
        print("당신의 학점은 A입니다.")
elif (score >= 80):
    print("당신의 학점은 B입니다.")
elif (score >= 70):
    print("당신의 학점은 C입니다.")
elif (score >= 60):
    print("당신의 학점은 D입니다.")
else:
    print("당신의 학점은 F입니다.")
