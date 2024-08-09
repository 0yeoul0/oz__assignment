#붕어빵 재고 확인
stock = {
    '팥붕어빵': 10,
    '슈크림붕어빵': 8,
    '초코붕어빵': 5    
}

for item, 재고 in stock.items():
    print(f"{item}: {재고}개")



order = {}
bread_type, bread_count = input("붕어빵 종류와 개수 입력해주세요!")
bread_count = int(bread_count)
order


주문 = {}


#붕어빵 재고 확인
stock = {
    '팥붕어빵': 10,
    '슈크림붕어빵': 8,
    '초코붕어빵': 5    
}

for item, 재고 in stock.items():
    print(f"{item}: {재고}개")


#주문
order = {}
bread_type, bread_count = input("붕어빵 종류와 개수 입력해주세요!(한칸 띄어서 입력해주세요 예시: 팥붕어빵3)").split('')
bread_count = int(bread_count)

order["팥붕어빵"] = 3 #order[팥붕어빵]
print(f"주문내역 {order}")


#첫번쨰는 재고가 충분
#두번째는 재고가 충분하지 않음
if stock[bread_type] >= order[bread_count]:
    stock[bread_type] = stock[bread_type] - order[bread_type]
    print(f"{bread_type} {order[bread_type]}개를 판매 했습니다.")


else:
    print("죄송하지만 재고가 없어요.")







#주문 종료

while True:
    if bread_type == "종료":
        break

    bread_count = int(input("주문할 붕어빵의 개수를 입력해주세요."))

    if stock[bread_type] >= order[bread_count]:
    stock[bread_type] = stock[bread_type] - order[bread_type]
    print(f"{bread_type} {order[bread_type]}개를 판매 했습니다.")
    
    else:
        print("죄송하지만 재고가 없어요.")
    
    print("현재 붕어빵 재고")
    for bread_type, bread_count in stock.items:
        print(f"{bread_type} : {bread_count}")

#팥붕어빵 : 10
# 초코붕어빵 : 5