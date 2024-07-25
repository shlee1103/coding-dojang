start, end = list(map(int, input().split()))

list = []

for i in range(start, end + 1):
    if (i == start + 1 or i == end - 1):
        continue
    else:
        list.append(2 ** i)

print(list)