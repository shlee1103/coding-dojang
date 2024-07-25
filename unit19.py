# 몇줄 출력할건지 (행에 관한 부분) -> 한 행에 별이 5개 찍힐때마다 개행
for row in range(5):
    # 몇 열 출력할건지(열 순서대로 별이 찍힘)
    for col in range(5):
        print('*', end = '')
    print()


# 계단식 별 출력
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end = '')
            
    print()


for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end='')
        else:
            print(' ', end='')
    print()


# 연습문제
for i in range(5):
    for j in range(5):
        if j < i:
            print(' ', end='')
        # if j >= i:
        else:
            print('*', end = '')
    print()


# 심사문제
star_row = int(input())

for i in range(star_row):
    # 공백 출력
    for j in range(star_row):
        if j < star_row - i - 1:
            print(' ', end = '')
    # ex: 3일 때
    # 1행 2칸 공백 -> i == 0, j < 2
    # 2행 1칸 공백 -> i == 1, j < 1
    # 3행 0칸 공백 -> i == 2, j < 0

    # 별 출력
    # -> 강사님께 여쭤보기