# end_num = int(input("정수 입력: "))
# num = 1
# sum_num = 0

# while (num <= end_num):
#     sum_num += num
#     num += 1

# print(f"1부터 {end_num}까지의 누적합: {sum_num}")

# num = int(input("구구단 단수 입력: "))
# i = 0

# print(f"구구단 {num}단")
# print("============================")
# for i in range(1, 10):
#     print(f"{num} x {i} = {num*i}")



# line = int(input("삼각형 행 수: "))
# i = 0
# j = 0

# for i in range(0, line):
#     for j in range(0, i):
#         print(" ", end="")
#     for j in range(0, line-i):
#         print("*", end="")
#     print("")

# for i in range(1, line+1):
#     for j in range(0, line-i+1):
#         print(" ", end="")
#     for j in range(0, 2*i-1):
#         print("*", end="")
#     print("")



# s = "python"

# print(s[2:5:1])
# print(s[1:4])
# print(s[3:])
# print(s[:4])




id_num = input("주민번호: ")

print(id_num[0:6])
print(id_num[7:])
print(f"{id_num[0:2]}년도 {id_num[2:4]}월 {id_num[4:6]}일 생")

birth = int(id_num[0:2])
gender = int(id_num[7])

if gender == 3 or gender == 4:
    age = 2021 - (2000+birth) + 1
else:
    age = 2021 - (1900+birth) + 1


print(f"{age}세 ", end="")

if gender == 1 or gender == 3:
    print("남자")
else:
    print("여자")


