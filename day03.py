# s1 = "떡볶이 김말이 닭강정"
# s2 = s1.split()

# print(s2)


# idol = "방탄소년단, 아이즈원, 샤이니"
# idol_list = idol.split(", ")

# for i in idol_list:
#     print(i+" 사랑해!!")


# a = 3
# b = 1

# print(f"a = {a}")
# print(f"b = {b}")
# print(f"b/a = {b/a:.3}")


# a = 12345

# print(f"~~{a:<16}~~")


# nums = [1, 2, 4, 5]

# nums[2:3] = [9, 10, 11]

# print(nums)

# nums[:] = []
# print(nums)




# contact_name = []
# contact_tel = []

# menu = 0
# while menu != 5:
#     print("")
#     print("-" * 8, "연락처 관리 프로그램", "-" * 8)
#     print("1. 연락처 등록")
#     print("2. 연락처 검색")
#     print("3. 연락처 삭제")
#     print("4. 모든 연락처 조회")
#     print("5. 프로그램 종료")
#     print("-" * 38)

#     menu = int(input("메뉴 입력: "))

#     if menu == 1:
#         print("-" * 25)
#         print("연락처 등록을 시작합니다.")
#         name = input("이름: ")
#         tel = input("전화번호: ")

#         contact_name.append(name)
#         contact_tel.append(tel)
#     elif menu == 2:
#         search_name = input("찾을 이름을 입력하세요: ")
#         if search_name in contact_name:            
#             print(f"{search_name}님의 연락처는 {contact_tel[contact_name.index(search_name)]}입니다.")
#         else:
#             print(f"{search_name}님은 연락처 목록에 없습니다.")
#     elif menu == 3:
#         search_name = input("삭제할 이름을 입력하세요: ")
#         if search_name in contact_name:
#             search_index = contact_name.index(search_name)
#             del(contact_name[search_index])
#             del(contact_tel[search_index])
#             print(f"{search_name}님의 연락처가 정상적으로 삭제 되었습니다.")
#         else:
#             print(f"{search_name}님은 연락처 목록에 없습니다.")
#     elif menu == 4:
#         print("=" * 8, "전체 연락처 조회", "=" * 8)
#         for i in range(0, len(contact_name)):
#             print(f"{contact_name[i]}: {contact_tel[i]}")
#     else:
#         print("프로그램을 종료합니다.")


# user = {'kim1234': 'kkk1234',
#         'lee4567': 'lll4567', 
#         'park9876': 'ppp9876'}
# login_success = False

# while not login_success:
#     user_id = input("아이디: ")
#     # if user_id in user:
#     #     user_pw = input("비밀번호: ")
#     #     if user_pw == user[user_id]:
#     #         print("로그인 성공")
#     #         break
            
#     # else:
#     #     print("존재하지 않는 회원입니다.")
#     if user_id not in user:
#         print("존재하지 않는 회원입니다.")
#     while user_id in user:
#         user_pw = input("비밀번호: ")
#         if user_pw == user[user_id]:
#             print("로그인 성공")
#             login_success = True
#             break
#         else:
#             print("비밀번호가 틀렸습니다.")
    

# food menu

# select = 0
# menu = {}

# while select != 3:
#     print("")
#     print("=" * 8, "음식점 메뉴 관리 프로그램", "=" * 8)
#     print("1. 신규 메뉴 등록하기")
#     print("2. 메뉴판 전체 보기")
#     print("3. 프로그램 종료하기")
#     print("=" * 41)

#     select = int(input("=> "))
#     if select == 1:
#         menu_name = input("메뉴명: ")
#         if menu_name in menu:
#             print("이미 등록된 메뉴입니다.")
#         else:
#             menu_price = input("가격: ")
#             menu[menu_name] = menu_price
#             print(f"신규 메뉴 {menu_name}(이)가 등록 되었습니다.")
#     elif select == 2:
#         for i in menu:
#             print(f"{i}: {menu[i]}")
#     elif select == 3:
#         print("프로그램을 종료합니다.")
#         break
#     else:
#         print("잘못된 선택입니다.")


# a = {'t', 'l', 'd', 'c', 'h', 'cat'}
# b = {'d', 'cat', 'h'}


# print(a >= b)
# print(b >= b)

# print(a > b)
# print(b > b)


def calc_rangesum(start, end):
    sum_num = 0
    for i in range(start, end+1):
        sum_num += i
    return sum_num

start = int(input("덧셈 시작값: "))
end = int(input("덧셈 끝값: "))
print(f"{start} ~ {end}의 누적합: {calc_rangesum(start, end)}")