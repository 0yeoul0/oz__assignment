#if 문법과 주의사항(콜른(:) , 들여쓰기)

#escape = input("당신이 탈출해야할곳은?")

#if escape == "escape the world!!!":
    #print("yeah!!! escape the world!!")

#else:
    #print("당신은 이세상을 탈출 할수없어!")

#2. if문 문법과 주의사함(콜론 , 들여쓰기)

#개수 = int (input("붕어빵 몇개 사실건가요?"))

#if 개수 > 3:
    #print("개당 1800원 입니다.")

#3. if문의 흐름(작동원리)
#코드는 위에서 아래 순서로 작동!

# 2)개수라는 변수에 담음 1)입력을 받음
#개수 = int(input("붕어빵 몇개 사실건가요?"))

#3)개수 변수가 있네 값이 뭐지 4>3 Ture 또는  False

#if 개수 > 3:
   # print("개당 1800원입니다.") # 조건이 True면 if문이 실행됨

#if 개수 <= 3:
   # print("개당 2000원입니다.") 
#4) if 중첩문

#의문의_숫자 = 10 

#if 의문의_숫자 > 5:
    #if 의문의_숫자 <15:
        #print("의문의 숫자는 5 보다 크고 10보다 작습니다.")

#5) if ~ else 문법과 주의사함(콜론 , 들여쓰기)


#개수 = int (input("붕어빵 몇개 사실건가요?"))

#if 개수 > 3:    #True 일경우 실행
    #print("개당 1800원 입니다.")

#else: #if문이 False 일경우 실행
#    print("개당 2000원입니다.")

#6) if ~ else문 흐름

#개수 = int (input("붕어빵 몇개 사실건가요?"))

#if 개수 > 3:    
    #print("개당 1800원 입니다.")

#else: 
 #   print("개당 2000원입니다.")

#7.조건문 조건(True , False)
#True 
#if True:
    #print(True)
#else:
    #print(False)

#False
#if False:
    #print("True")
#else:
    #print(False)

#False
#if False:
    #print(True)
#else:
    #print(False)

#None
#if None:
    #print(True)
#else:
    #print(False)

#0

#if 0:
    #print(True)
#else:
#    print(False)

#1

#if 1:
#    print(True)
#else:
#    print(False)

#1.1

#if 1.1:
#    print(True)
#else:
#    print(False)

#hello

#if "hello":
#    print(True)
#else:
#    print(False)
#""

#if "":
#    print(True)
#else:
#    print(False)

#not

#if not True:
#    print(True)
#else:
#    print(False)

#not ''

#if not '':
#    print(True)
#else:
#    print(False)

#8)조건식 여러개 설정하기

a , b = 10,30

if a==10 and b==30:
   print("동일합니다.")
    
else:
    print("동일하지 않습니다.")

if a==10 or b==30:
    print("동일합니다.")
    
else:
    print("동일하지 않습니다.")

if a>= 10 and a<20:
    print("10보다 크고 20보다 작습니다.")

#9
    
