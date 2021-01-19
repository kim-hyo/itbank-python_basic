# li = ['11', '22', '33']
# mp = map(int, li)

# print(type(mp))

# mp_li = list(mp)
# print(mp_li)





# def max_of_three(n1, n2, n3):
#     li = [n1, n2, n3]
#     return max(li)

# def min_of_three(n1, n2, n3):
#     li = [n1, n2, n3]
#     return min(li)

# num1, num2, num3 = map(int, input("3개의 정수를 입력하세요: ").split())
# print(f"{num1}, {num2}, {num3} 중 최대값: {max_of_three(num1, num2, num3)}")
# print(f"{num1}, {num2}, {num3} 중 최소값: {min_of_three(num1, num2, num3)}")





# def Calc_BMI(height, weight):
#     return (weight / ((height/100)*(height/100)))

# height = float(input("키(cm)를 입력하세요: "))
# weight = float(input("몸무게(kg)를 입력하세요: "))

# print(f"키 -> {height}cm, 체중 -> {weight}kg의 체질량지수는: {Calc_BMI(height, weight):.2f}입니다.")
# if Calc_BMI(height, weight) >= 25.0:
#     print("당신은 과체중입니다.")
# elif Calc_BMI(height, weight) <= 18.5:
#     print("당신은 저체중입니다.")
# else:
#     print("당신은 정상 체중입니다.")


# def get_avg(tu):
#     sum = 0
#     for i in tu:
#         sum += i
#     return sum / len(tu)

# int_tu = tuple(map(int, input("평균을 구할 정수값을 입력하세요: ").split()))

# print(f"{int_tu}의 평균값은 {get_avg(int_tu):.2f}입니다.")



# def get_max(tu):
#     return max(tu)

# int_tu = tuple(map(int, input("최대값을 구할 정수값을 입력하세요: ").split()))

# print(f"{int_tu}의 최대값은 {get_max(int_tu)}입니다.")


# def food_name(**foods):
#     print(type(foods))
#     print(foods)

# food_name(chicken='통닭', ramen='라면', gimbab='김밥')


sel = 0
while sel != 4:
    print("\n\n*** 구구단을 외우자 ***")
    print("1. 홀수 구구단 보기")
    print("2. 짝수 구구단 보기")
    print("3. 특정 구구단 보기")
    print("4. 프로그램 종료")
    print("*" * 23, "\n")
    sel = int(input("메뉴를 선택하세요: "))

    if sel == 1:
        for i in range(2, 10):
            if i % 2 == 1:
                for j in range(1, 10):
                    print(f"{i} x {j} = {i*j}")
    elif sel == 2:
        for i in range(2, 10):
            if i % 2 == 0:
                for j in range(1, 10):
                    print(f"{i} x {j} = {i*j}")
    elif sel == 3:
        choice = int(input("보고 싶은 구구단수를 입력하세요: "))
        for i in range(1, 10):
            print(f"{choice} x {i} = {choice*i}")
    elif sel == 4:
        break
    else:
        print("잘못된 선택입니다.\n\n")

    