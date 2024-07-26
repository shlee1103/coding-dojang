# # 2차원 리스트 만들고 요소에 접근하기

# # 2차원 리스트
# # 리스트 = [[값, 값], [값, 값], [값, 값]]
# # a = [[10, 20], [30, 40], [50, 60]]
# # print(a)

# # 리스트[세로인덱스][가로인덱스]
# # 리스트[세로인덱스][가로인덱스] = 값

# # for 반복문 한번만 사용하기
# a = [[10, 20], [30, 40], [50, 60]]
# for x, y in a:
#     print(x,y)

# # for 반복문 두 번 사용
# for i in a:     # a 안쪽에서 리스트 꺼냄
#     for j in i:     # 안쪽 리스트에서 요소를 하나씩 꺼냄
#         print(j, end = ' ')
#     print()
        

 
# for i in range(len(a)):            # 세로 크기
#     for j in range(len(a[i])):     # 가로 크기
#         print(a[i][j], end=' ')
#     print()




# i = 0
# while i < len(a):    # 반복할 때 리스트의 크기 활용(세로 크기)
#     x, y = a[i]      # 요소 두 개를 한꺼번에 가져오기
#     print(x, y)
#     i += 1           # 인덱스를 1 증가시킴


# # 반복문으로 리스트 만들기
# # 1차원
# a = []
# for i in range(10):
#     a.append(0)
# print(a)

# # 2차원
# a = []
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
# print(a)
# # [[0, 0], [0, 0], [0, 0]]


# a = [[i*j for j in range(2)] for i in range(3)]
# print(a)


# a = []
# for i in range(3):
#     b = []
#     for j in range(2):
#         b.append(i*j)
#     a.append(b)
# print(a)

# a = [[0] * 2 for i in range(3)]

# a = [[10, 20], [30, 40]]
# b = a
# b[0][0] = 500


# 연습문제 ---------------------------------------------
# 높이 2, 세로크기 4, 가로크기 3
c = []
for i in range(2):
    b = []
    c.append(b)
    for j in range(4):
        a = []
        for k in range(3):
            a.append(0)
        b.append(a)
print(c)


a = [[[0 for k in range(3)] for j in range(4)] for i in range(2)]
print(a)


# 심사문제 ---------------------------------------------
matrix = []
for i in range(row):
    matrix.append(list(input()))