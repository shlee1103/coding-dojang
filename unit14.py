# # if에 else 사용하면 조건식이 만족할 때와 만족하지 않을 대 각각 다른 코드 실행할 수 있다

# x = 5
# if x == 10:
#     print('10입니다.')
# else:
#     print('10이 아닙니다.')

    

# x = ''
# y = 20

# if 20 :
#     print('참')
# else:
#     print('거짓')



# # 연습문제
# written_test = 75
# coding_test = True

# if written_test  >= 80 and coding_test == True:
#     print('합격')
# else:
#     print('불합격')


# 심사문제
# korean, english, mathematics, science = map(int, input().split())
# avg_score = (korean + english + mathematics + science)//4
# if 0 < korean + english + mathematics + science < 400:
#     print('잘못된 점수')
# elif avg_score >= 80 and 0 < korean + english + mathematics + science < 400:
#     print('합격')
# elif 0 < korean + english + mathematics + science < 400:
#     print('잘못된 점수')
# else:
#     print('불합격')

# korean, english, mathematics, science = map(int, input().split())

# if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= science <= 100:
#     avg_score = (korean + english + mathematics + science) / 4
#     if avg_score >= 80:
#         print('합격')
#     else:
#         print('불합격')
# else:
#     print('잘못된 점수')

