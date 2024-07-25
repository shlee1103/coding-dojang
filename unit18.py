# # break, continue : 반복문 제어
# # break: 제어흐름 중단
# # continue: 제어흐름(반복) 유지, 코드 실행만 건너뜀

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i == 100:
#         break


# for i in range(10000):
#     print(i)
#     if i == 100:
#         break


# # 홀수만 출력 -> 짝수 건너뛰기
# for i in range(100):
#     if i % 2 == 0:
#         continue
#     print(i)


# # while - 건너뛰기
# i = 0
# while i < 100:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)



# 연습문제
# i = 0
# while True:
#     if i > 73:
#         break
#     if i % 10 == 3:
#         print(i, end = ' ')
#     i += 1

# # 정답
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue

#     if i > 73:
#         break


# 심사문제
start, stop = map(int, input().split())
 
i = start
 
while True:
    if i > stop:
        break

    if i % 10 != 3:
        print(i, end=' ')
    i += 1


    if i % 10 == 3:
        i += 1
        continue
    if i > stop:
        break
    print(i, end = ' ')
    i+=1
