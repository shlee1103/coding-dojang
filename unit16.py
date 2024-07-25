## for과 range 사용하기

# range에 반복할 횟수를 지정하고 앞에 in과 변수를 입력
# for i in range(100):
#                print('Hello, world!')

# range에서 in으로 숫자를 하나하나 꺼내서 반복하는 방식
# for 반복문은 반복 횟수가 정해져 있을 때 주로 사용
# range 안에는 무조건 숫자

# for 변수 i in range(시작, 끝)

# range(10, 0)은 실행X
# range는 숫자가 증가하는 기본값이 양수 1
# for i in range(10, 0, -1):
#         print('Hello, world!', i)

# reversed 사용하면 숫자의 순서를 반대로 뒤집기 가능
# for 변수 in reversed(range(횟수))
# for 변수 in reversed(range(시작, 끝))
# for 변수 in reversed(range(시작, 끝, 증가폭))
# for i in reversed(range(10)):
#         print('Hello, world!', i)
    

# 변수 i 변경
# for i in range(10):
#         print(i, end='')
#         i = 10

# # 입력한 횟수대로 반복하기
# count = int(input('반복할 횟수를 입력하세요: '))

# for i in range(count):
#         print('Hello, world!', i)


# for문으로 시퀀스 객체 꺼내기
# a = [10, 20, 30, 40, 50]
# for i in a:
#     print(i)


# fruits = ('apple', 'orange', 'grape')
# for fruit in fruits:
#     print(fruit)


# # Python 뒤집어서 출력하기
# for letter in reversed('Python'):
#     print(letter, end=' ')

# 연습문제 -------------------
# x = [49, -17, 25, 102, 8, 62, 21]

# for i in x:
#     value = i*10
#     print(value, end = ' ')


# 심사문제 -------------------
num = int(input())

for i in range(1,10):
    # print(num,'*',i, '=', (num*i))
    print(f'{num} * {i} = {num*i}')

