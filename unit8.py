# ## boolean
# print(3>1)  # True

# # is와 is not -> 객체 비교
# print(1 == 1.0)
# print(1 is 1.0)
# print(1 is not 1.0)

# # 값 비교에 is 사용하지 않기

# # 논리 연산자
# # and는 두 값이 모두 True라야 True, 하나라도 False이면 False
# # or는 두 값 중 하나라도 True이면 True, 두 값이 모두 False라야 False
# # not은 논릿값을 뒤집음. not True는 False, not False는 True
# # and, or, not 논리 연산자가 식 하나에 들어있으면 not -> and -> or 순으로 판단

# # 비교연산자 같이사용
# 10 == 10 and 10 != 5    # True and True -> True
# 10 > 5 or 10 < 3        # True or False -> True
# not 10 > 5              # not True -> False
# not 1 is 1.0            # not False -> True
# # 비교 연산자(is, is not, ==, !=, <, >, <=, >=)를 먼저 판단, 논리 연산자(not, and, or)를 판단

# # 정수 1은 True, 0은 False
# # 정수 0, 실수 0.0이외의 모든 숫자는 True
# # 빈 문자열 '', ""를 제외한 모든 문자열은 True
# bool(1)
# # True
# bool(0)
# # False
# bool(1.5)
# # True
# bool('False')
# # True


# # 단락평가
# # 첫 번째 값만으로 결과가 확실할 때 두 번째 값은 확인(평가)하지 않는 방법
# # and : 두 값이 모두 참이어야 참 -> 첫번째값 거짓이면 바로 거짓
# # 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
# print(False and True)     # False
# print(False and False)    # False

# # or : 두 값 중 하나만 참이라도 참 -> 첫번째값 참이면 바로 참
# # 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
# print(True or True)     # True
# print(True or False)    # True

# # 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환
# # 무조건 T/F를 반환하지 않음


# # 연습문제
# # 국어, 영어, 수학, 과학 점수 중 한 과목이라도 50점 미만이면 불합격. 합격이면 True, 불합격이면 False
# korean = 92
# english = 47
# mathematics = 86
# science = 81
 
# # print(?)
# # 답 : False

# print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)

# 심화퀴즈
korean, english, mathematics, science = map(int, input().split())
print(korean >= 90 and english > 80 and mathematics > 85 and science >= 80)

