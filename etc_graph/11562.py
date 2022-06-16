# https://www.acmicpc.net/problem/11562
import sys
n, m = map(int, sys.stdin.readline().split())
INF = sys.maxsize
arr = [[INF] * (n + 1) for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if c == 1:
        arr[a][b] = 0
        arr[b][a] = 0
    else:
        arr[a][b] = 0
        arr[b][a] = 1

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            arr[i][j] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if arr[a][b] > arr[a][k] + arr[k][b]:
                arr[a][b] = arr[a][k] + arr[k][b]


k = int(input())

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    print(arr[x][y])