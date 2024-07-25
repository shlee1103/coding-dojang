# 4. 변수와 입력 사용하기
# 6.1 변수 만들기
# x(변수이름) = 10(값)

# 변수명 규칙
# 영문 문자와 숫자를 사용할 수 있습니다.
# 대소문자를 구분합니다.
# 문자부터 시작해야 하며 숫자부터 시작하면 안 됩니다.
# _(밑줄 문자)로 시작할 수 있습니다.
# # 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없습니다.
# # 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없습니다.

# x = 10
# print(x)

# y = 'Hello, world!'
# print(y)

# print(type(x))

# # 파이썬에서 =는 변수에 값을 할당
# # == 등호 (같다)

# # 변수 여러개 한번에 만들기
# # 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3
# # 변수와 값의 개수 동일하게
# x, y, z = 10, 20, 30
# print(x)
# print(y)
# print(z)

# x = y = z = 10
# print(x)
# print(y)
# print(z)

# x, y = 10, 20
# x, y = y, x # 두 변수의 값 바꿈
# print(x)
# print(y)

# # 변수 삭 제
# x = 10
# del x
# # print(x)    # NameError: name 'x' is not defined
# # x를 삭제하여 변수가 없어짐 so x가 정의되지 않았다는 에러

# # 변수 연산
# # 파이썬에서는 변수를 두 번 입력하지 않도록 산술 연산 후 할당 연산자를 제공
# a = 10
# a += 20 # a와 20을 더한 후 결과를 다시 a에 저장

# # 6.3 input 함수 사용
# x = input('문자열을 입력하세요: ')
# # print(x)

# a = int(input('첫번째 숫자를 입력하세요: '))
# b = int(input('두번째 숫자를 입력하세요: '))
# # print(a+b)

# # input 한 번에 값 2개
# a, b = input('숫자 두 개를 입력하세요: ').split()
# # print(a + b)

# # map 사용하여 정수로 변환
# # 변수1, 변수2 = map(int, input().split())
# # 변수1, 변수2 = map(int, input().split('기준문자열'))
# # 변수1, 변수2 = map(int, input('문자열').split())
# # 변수1, 변수2 = map(int, input('문자열').split('기준문자열'))
# a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
# print(a + b)

a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리
print(a + b)