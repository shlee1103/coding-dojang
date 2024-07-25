# while 반복문
# 조건식으로만 동작, 반복할 코드 안에 조건식에 영향을 주는 변화식
# i = 0                # 초기식
# while i < 100:        # while 조건식
#     print('Hello, world!')    # 반복할 코드
#     i += 1                    # 변화식


# 조건식을 판별 -> 조건식이 참이면 반복할 코드와 변화식 수행
# # 다시 조건식 판별 -> 참이면 코드 계속 반복, 거짓이면 반복문 끝냄
# i = 0
# while i < 100:
#     print('Hello, world!')
#     i += 1


# 초기값 1 할당, 100번 출력
# i = 1
# while i <= 100:
#     print('Hello, world!', i)
#     i += 1

# 초깃값 감소
# i = 100
# while i > 0:
#     print('Hello, world!', i)
#     i -= 1


# count = int(input('반복할 횟수를 입력하세요: '))
# i = 0
# while i < count:
#     print('Hello, world!', i)
#     i += 1


# count = int(input('반복할 횟수를 입력하세요: '))
# while count > 0:
#     print('Hello, world!', count)
#     count += 1


# 반복 횟수가 정해지지 않은 경우
# 난수 생성 : import random

# import random
# i = 0
# while i != 3:
#     i = random.randint(1, 6)
#     print(i)

# while에 True 지정하면 무한 루프
# while에 조건식 대신 True 지정하면 무한히 반복하는 무한 루프 만들어짐



# 연습문제
# i = 2
# j = 5

# while i <= 32 or j >= 1:
#     print(i, j)
#     i *= 2
#     j -= 1


# 심사문제
traffic_card_fee = int(input())

while traffic_card_fee >= 1350 :
    traffic_card_fee = traffic_card_fee - 1350
    print(traffic_card_fee)