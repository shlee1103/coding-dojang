# # elif(else if)
# # elif는 else인 상태에서 조건식을 지정할 때 사용

# # x가 10인지 검사하고 참이면 10입니다 출력
# # x가 20인지 검사하고 거짓이면 20인지 검사
# x = 20

# if x == 10:
#     print('10입니다.')
# elif x == 20:
#     print('20입니다.')

# # x가 10도 아니고, 20도 아니면
# x = 30

# if x == 10:
#     print('10입니다.')
# elif x == 20:
#     print('20입니다.')
# else:
#     print('10도 20도 아닙니다.')


# # 음료수 자판기
# button = int(input())

# if button == 1:
#     print('콜라')
# elif button == 2:
#     print('사이다')
# elif button == 3:
#     print('환타')
# else:
#     print('제공하지 않는 메뉴')


# 연습문제
# x = int(input())
# if 11 <= x <= 20:
#     print('11~20')
# elif 21 <= x <= 30:
#     print('21~30')
# else:
#     print('아무것도 해당하지 않음')


# 심사문제
age = int(input())
balance = 9000

if 7 <= age <= 12:
    balance = 9000 - 650
elif 13 <= age <= 18:
    balance = 9000-1050
elif age >= 19:
    balance = 9000-1250 

print(balance)
