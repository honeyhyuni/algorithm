# https://www.acmicpc.net/problem/11404
# 플로이드-와샬 기본 이론문제
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 1e9
arr = [[INF] * (n + 1) for i in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            arr[i][j] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if arr[a][b] > c:
        arr[a][b] = c

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if arr[i][j] == INF:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
