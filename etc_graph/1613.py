# https://www.acmicpc.net/problem/1613
import sys
input = sys.stdin.readline
n, K = map(int, input().split())

arr = [[0] * (n+1) for i in range(n+1)]

for i in range(K):
    x, y = map(int, input().split())
    arr[x][y] = -1
    arr[y][x] = 1

# 플로이드 - 와샬
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if arr[a][b] == 0:
                if arr[a][k] == -1 and arr[k][b] == -1:
                    arr[a][b] = -1
                elif arr[a][k] == 1 and arr[k][b] == 1:
                    arr[a][b] = 1

s = int(input())
result_v = []
for i in range(s):
    result_v.append(list(map(int, input().split())))
for i, j in result_v:
    print(arr[i][j])