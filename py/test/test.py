잔액 = {"잔액": 0}
영수증 = []

입금_금액 = int(input("입금 금액을 입력하세요: "))
잔액["잔액"] += 입금_금액
print(f'현재 {잔액["잔액"]}원입니다.')
영수증.append(("입금", 입금_금액, 잔액["잔액"]))

출금_금액 = int(input("출금 금액을 입력하세요: "))

if 출금_금액 > 잔액["잔액"]:
    출금_금액 = 잔액["잔액"]

잔액["잔액"] -= 출금_금액
print(f'현재 {잔액["잔액"]}원입니다.')

영수증.append(("출금", 출금_금액, 잔액["잔액"]))

print("모든 거래 내역(영수증):")
for 거래_유형, 금액, 현재_잔액 in 영수증:
    print(f'{거래_유형} - {금액}원, 현재 잔액: {현재_잔액}원')
