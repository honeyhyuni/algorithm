# https://www.acmicpc.net/problem/18405
import sys
input = sys.stdin.readline
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
S, X, Y = map(int, input().split())
virus = [deque() for i in range(k+1)]

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            virus[arr[i][j]].append((i, j))


for cnt in range(1, S+1):
    for i in range(1, k+1):
        len_ = len(virus[i])
        for j in range(len_):
            x, y = virus[i].popleft()
            for _ in range(4):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                    arr[nx][ny] = i
                    virus[i].append((nx, ny))
print(arr[X-1][Y-1])
