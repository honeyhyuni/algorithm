# https://www.acmicpc.net/problem/2660
import sys
input = sys.stdin.readline

n = int(input())
INF = sys.maxsize
arr = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            arr[i][j] = 0

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    arr[x][y] = 1
    arr[y][x] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if arr[a][b] > arr[a][k] + arr[k][b]:
                arr[a][b] = arr[a][k] + arr[k][b]


result = []
for i in range(1, n + 1):
    result.append(max(arr[i][1:]))


r = min(result)
print(r, result.count(r))

for i in range(n):
    if result[i] == r:
        print(i + 1, end=' ')
