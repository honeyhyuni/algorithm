# https://www.acmicpc.net/problem/12875
# 플로이드-와샬 기본 이론문제
import sys
input = sys.stdin.readline
n = int(input())
d = int(input())
INF = sys.maxsize
arr = []
for i in range(n):
    arr.append(list(map(str, input().strip())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'N':
            arr[i][j] = INF
        else:
            arr[i][j] = 1


for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            if arr[a][b] > arr[a][k] + arr[k][b]:
                arr[a][b] = arr[a][k] + arr[k][b]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, arr[i][j])

if result > 1e9:
    print(-1)
else:
    print(result * d)