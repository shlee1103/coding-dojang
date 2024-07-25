# ## 시퀀스 자료형
# # 시퀀스 자료형(sequence types) : 연속적으로 이어진 자료형
# # 시퀀스 자료형의 가장 큰 특징은 공통된 동작과 기능을 제공

# # 특정 값 있는 지 확인
# # 리스트 a에 30과 100이 있는지 확인
# a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(30 in a)
# print(100 in a)

# # 시퀀스 객체 연결하기
# a = [0, 10, 20, 30]
# b = [9, 8, 7, 6]
# print(a + b)

# # range는 리스트 또는 튜플로 만들어서 연결
# c = list(range(0, 10)) + list(range(10, 20))
# print(c)

# # 시퀀스 객체 반복
# # 시퀀스객체 * 정수
# # 정수 * 시퀀스객체
# # 문자열도 반복 가능
# # 리스트는 리스트 또는 튜플로 만들어서 반복
# c = list(range(0, 5, 2))*3
# print(c)

# # 리스트와 튜플의 요소 개수 구하기 : len()

# # range(0, 10, 2)는 0부터 10까지 2씩 증가하므로 0, 2, 4, 6, 8. 따라서 5
# d = len(range(0, 10, 2))
# print(d)

# hello = 'Hello, world!'
# print(len(hello))   # 공백포함

# # 심사문제
# x = input().split()
# a = tuple(x[:-5])
# print(a)


# 심사문제 2
a = input()
b = input()
print(a[1:len(a):2]+b[0:len(b)])
