# 제품 1개당 정보
# [제품번호, 제품명, 단가, 수량, 제품총액]

# product_list = []

# def find_product(product_id):
#     for i in range(0, len(product_list)):
#         if product_list[i]['id'] == product_id:
#             return i
#             break
#     else:
#         return -1


# def regist_product():
#     product = {}

#     print("제품 등록을 시작합니다.")
#     product['id'] = input("제품번호: ")
#     product['name'] = input("제품명: ")
#     product['cost'] = int(input("제품단가: "))
#     product['amount'] = int(input("제품수량: "))
#     product['total_cost'] = product['cost'] * product['amount']

#     product_list.append(product)    


# def remove_product(product_id):
#     product_index = find_product(product_id)
#     print(f"선택하신 제품은 {product_list[product_index]['name']}입니다. ")
#     show_product(product_index)
#     sel = int(input("삭제(1) / 취소(2) ==> "))
#     if sel == 1:
#         del(product_list[product_index])
#     elif sel == 2:
#         print("취소되었습니다.")
#     else:
#         print("잘못된 선택으로 취소되었습니다.")
    


# def modify_product(product_id):
#     product_index = find_product(product_id)
#     print(f"선택하신 제품은 {product_list[product_index]['name']}입니다. ")

#     sel = 0
#     while sel != 4:
#         show_product(product_index)
#         print("어떤 항목을 수정하시겠습니까?")
#         sel = int(input("제품명(1) / 제품단가(2) / 제품수량(3) / 수정종료(4) ==> "))

#         if sel == 1:
#             product_list[product_index]['name'] = input("제품명을 입력해주세요: ")
#         elif sel == 2:
#             product_list[product_index]['cost'] = input("단가를 입력해주세요: ")
#         elif sel == 3:
#             product_list[product_index]['amount'] = input("수량을 입력해주세요: ")
#         else:
#             print("잘못된 입력입니다.")



# def show_product(product_index=-1):
#     # index가 -1이면 전체 제품 출력
#     # index가 0 이상이면 해당 index 제품 출력
#     total_all_cost = 0
#     if product_index == -1:
#         print("=" * 60)
#         print(f"제품ID     제품명      제품단가      제품수량      총가격")
#         print("=" * 60)
#         for i in range(0, len(product_list)):
#             print(f"{product_list[i]['id']:<12}{product_list[i]['name']:<12}{product_list[i]['cost']:<12}{product_list[i]['amount']:<12}{product_list[i]['total_cost']}")
#             total_all_cost += product_list[i]['total_cost']
#         print("=" * 60)
#         print(" "*32, f"총 합계 금액: {total_all_cost} 원")
#     else:
#         print("=" * 60)
#         print(f"제품ID     제품명      제품단가      제품수량      총가격")
#         print("=" * 60)
#         print(f"{product_list[product_index]['id']:<12}{product_list[product_index]['name']:<12}{product_list[product_index]['cost']:<15}{product_list[product_index]['amount']:<14}{product_list[product_index]['total_cost']}")    
#         print("=" * 60)


# select = 0

# while select != 5:
#     print("")
#     print("=" * 8, "창고 물류 관리 프로그램", "=" * 8)
#     print("1. 제품 등록하기")
#     print("2. 등록된 전체 제품 조회하기")
#     print("3. 등록된 개별 제품 조회하기")
#     print("4. 등록된 제품 수정하기")
#     print("5. 등록된 제품 삭제하기")
#     print("6. 종료")
#     print("=" * 41)

#     select = int(input("메뉴를 선택하세요: "))

#     if select == 1:
#         regist_product()
#     elif select == 2:
#         show_product()
#     elif select == 3:
#         product_id = input("조회할 제품의 ID를 입력하세요: ")
#         if find_product(product_id) >= 0:
#             show_product(find_product(product_id))
#         else:
#             print("잘못된 ID입니다.")
#     elif select == 4:
#         sel = input("수정할 제품의 ID를 입력하세요: ")
#         if find_product(sel) >= 0:
#             modify_product(sel)
#         else:
#             print("존재하지 않는 ID입니다.")
#     elif select == 5:
#         sel = input("삭제할 제품의 ID를 입력하세요: ")
#         if find_product(sel) >= 0:
#             remove_product(sel)
#         else:
#             print("존재하지 않는 ID입니다.")        
#     elif select == 6:
#         print("프로그램을 종료합니다.")
#     else:
#         print("잘못된 선택입니다.")


import random

lotto = []
num = 0
count = 0

while count != 6:
    num = random.randint(1, 45)
    if num in lotto:
        continue
    else:
        lotto.append(num)
        count += 1
    
lotto.sort()
print(f"로또 번호는 {lotto}")