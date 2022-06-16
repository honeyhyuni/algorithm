# https://www.acmicpc.net/problem/10159
import sys
n = int(input())
m = int(input())
arr = [[0] * (n + 1) for i in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if arr[a][k] == 1 and arr[k][b] == 1:
                arr[a][b] = 1

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if arr[i][j] == 0 and arr[j][i] == 0:
            cnt += 1
    print(cnt - 1)