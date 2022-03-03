# https://www.acmicpc.net/problem/14469
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key= lambda x : (x[0], x[1]))
result = 0

for i in arr:
    if result < i[0]:
        result = i[0] + i[1]
    else:
        result += i[1]

print(result)