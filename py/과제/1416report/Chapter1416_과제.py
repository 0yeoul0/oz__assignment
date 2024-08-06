print("붕어빵 주문 시스템에 오신 것을 환영합니다!")

# 붕어빵 종류와 재고
재고 = {'팥붕어빵': 10, '슈크림붕어빵': 8, '초코붕어빵': 5}

# 관리자 비밀번호 설정
관리자_비밀번호 = "admin1234"

def print_재고():
    
    #현재 남은 재고를 출력합니다.
  
    print("\n현재 남은 재고:")
    for 항목, 재고량 in 재고.items():
        print(f"{항목}: {재고량}개")

def 관리자_모드():
    
    #관리자 모드에서 재고를 추가할 수 있는 기능을 제공합니다.
   
    while True:
        관리종류 = input("\n추가할 붕어빵 종류를 입력해주세요 (종료: '종료'): ").strip()
        if 관리종류.lower() == '종료':
            break

        if 관리종류 not in 재고:
            print("존재하지 않는 붕어빵 종류입니다. 다시 입력해주세요.")
            continue

        try:
            추가수량 = int(input(f'{관리종류}의 추가할 개수를 입력해주세요: ').strip())
            if 추가수량 < 0:
                raise ValueError
        except ValueError:
            print("올바른 개수를 입력해주세요.")
            continue

        재고[관리종류] += 추가수량
        print(f"{관리종류}의 재고를 {추가수량}개 추가했습니다.")
        print_재고()

def 주문_처리(주문):
    
    #손님의 주문을 처리 및 재고를 업데이트
    
    print("\n주문 내역:")
    for 항목, 수량 in 주문.items():
        print(f"{항목}: {수량}개")

    print("\n주문 처리 시작!")
    for 항목, 수량 in 주문.items():
        if 재고.get(항목, 0) >= 수량:
            재고[항목] -= 수량
            print(f"{항목} {수량}개를 판매했습니다.")
        else:
            print(f"죄송하지만 {항목}의 재고가 부족합니다. 재고가 {재고.get(항목, 0)}개 남아 있습니다.")

    print_재고()

def 주문_모드():
    """
    손님의 주문을 받고 처리
    """
    주문 = {}
    while True:
        종류 = input("붕어빵 종류를 입력해주세요 ('입력완료' 입력시 주문종료): ").strip()
        if 종류.lower() == '입력완료':
            break

        if 종류 not in 재고:
            print("존재하지 않는 붕어빵 종류입니다. 다시 입력해주세요.")
            continue

        try:
            수량 = int(input(f'{종류}의 개수를 입력해주세요: ').strip())
            if 수량 < 0:
                print("개수는 0 이상의 자연수로 해주세요.")
                continue
        except ValueError:
            print("올바른 개수를 입력해주세요.")
            continue

        주문[종류] = 주문.get(종류, 0) + 수량

    if 주문:
        주문_처리(주문)

def main(): #가장중요!!! *******
    
    #메인 함수로, 사용자 입력을 받아 적절한 모드를 실행합니다.
   
    while True:
        모드 = input("주문을 하려면 '주문'을 입력하세요. (종료하실거면 '종료' 를 입력해주세요!): ").strip().lower() #<=히든옵션 관리자

        if 모드 == '주문':
            주문_모드()
        elif 모드 == '관리자':
            비밀번호 = input("관리자 비밀번호를 입력하세요: ").strip() #<= "admin1234"
            if 비밀번호 == 관리자_비밀번호:
                관리자_모드()
            else:
                print("잘못된 비밀번호입니다. 관리자 모드에 접근할 수 없습니다.")
        elif 모드 == '종료':
            print("\n주문 시스템을 종료합니다. 감사합니다!")
            print_재고()
            break
        else:
            print("잘못된 입력입니다. '주문' 을 입력해주세요.")

if __name__ == "__main__":
    main()
