#list

#리스트란? 원소들이 연속적으로 저장되는 형태의 자료형을 말합니다.
#시퀀스 자료형!!
    #str, list, tuple,dict,set

리스트 = []
print(리스트)

리스트 = [23,"이게리스트다",3,23,True,False]
print(리스트)

#리스트 다시 한번 선언해 보자

리스트 = ["이" ,"렇" ,"게", "만", "들" , "어", "요"]
리스트
리스트2 = list()
리스트2

#range? 연속된 숫자를 생산하는 기능이다.

range(10)

#list(range(시작,끝))

#리스트_매직_들어간다 = list(range(0,20))
#print(리스트_매직_들어간다)

#list(range(시작 , 끝 , 증가))

리스트_매직2 = list(range(0,20,2))#2의 약수
print(리스트_매직2)

리스트_매직3 = list(range(20,0,-1))#20~1
print(리스트_매직3)

리스트_매직4 = list(range(0,20))#0~19
print(리스트_매직4)

#리스트를 이용 변수에 값넣기

a , b , c = ["들", "어", "가"]
print(a , b , c )

d , e, f = [7 , 7 , 8]
print(d , e , f)

지갑 = [10000, 5000, 1000]
만원 , 오천원 ,천원 = 지갑
print(f'{만원} 2장 , {오천원} 3장 , {천원} 1장')

#리스트 패킹, 리스트 언패킹 ******

input() .split()
print("기억?" "나요?")

#슬라이싱

로또 = [3 , 5 , 15 , 33 , 41 , 44]
#로또 변수에 있는 리스트의 인덱스 1번부터 2번까지의 값을 출력해보자!

print(로또[1:3])

#로또변수의 마지막위치 출력해줘

print(로또[-1])

#반대로 출력 해보자!

print(로또[::-1])

#로또번호에 33이 있는지 확인

print(33 in 로또)

#로또와 로또2 리스트와 합치기

로또2 = [2 , 12 , 15 , 24 , 33 , 39]
print(로또+로또2)

#range 를 이용해서 1부터 10사이에 짝수만 들어있는 짝수 리스트를 만들어 주세요

짝수 = list(range(2, 12 , 2))
print(짝수)

#짝수 리스트에 들어있는 값을 2배 늘리고 다시 짝수 변수에 담아줘

짝수 = 짝수 * 2
print(짝수)

#짝수 리스트에 들어있는 요소의 개수를 구해 주세요

print(len(짝수))

# 리스트의 평균!

nums = [1 , 2 , 3 , 4 , 5]

numsavg = sum(nums) / len(nums)

#짝수 리스트에 3번째 인덱스를 출력해주세요.

print(짝수[3])

#len()함수를 이용해 인덱스 마지막 값 출력

print(짝수[len(짝수)-1])

#list 값 널고, 바꾸고, 지우고

mzfood = ["숙주" , "분모자" , "마라", "소세지", "소고기", "옥수수면" ]

#값을 넣는 방법 : append():마지막 요소에 값을 넣음, insert():원하는 곳에 값을 넣음

mzfood.append("고수")
print(mzfood)

mzfood.insert(0,"탕후루")
print(mzfood)

# 값지우기

del mzfood[-1]
print(mzfood)

#값 바꾸기

mzfood[-2] = "양고기" 
print(mzfood)

#문자열 시퀀스 아니냐 그럼 저거다 될듯
#문자열은 시퀀스여도 기능이용 불가
#인사 = "반가워"
#인사[2] = "웡"

#list의 기능 확인
print(dir(list))

print(mzfood)

#list 순서 거꾸로
mzfood.reverse()
print(mzfood)

#문자별 순서대로
mzfood.sort()
print(mzfood)

#none 왜 논이 나올까?

print(mzfood)
print(mzfood.reverse())
print(mzfood.sort())

