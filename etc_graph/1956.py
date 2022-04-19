# https://www.acmicpc.net/problem/1956
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
INF = sys.maxsize
arr = [[INF] * (v + 1) for i in range(v + 1)]

for i in range(v + 1):
    for j in range(v + 1):
        if i == j:
            arr[i][j] = 0

for i in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])
result = INF
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if i != j:
            result = min(result, arr[i][j] + arr[j][i])
print(result if result < INF else -1)
