# https://www.acmicpc.net/problem/10026
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j, v, arr):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == v:
                arr[nx][ny] = 0
                q.append((nx, ny))


cnt = 0
cnt2 = 0
n = int(input())
arr2 = [[0] * n for _ in range(n)]
arr = []
for _ in range(n):
    arr.append(list(map(str, input())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == "R" or arr[i][j] == "G":
            arr2[i][j] = 1
        else:
            arr2[i][j] = 2

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            cnt += 1
            bfs(i, j, arr[i][j], arr)
        if arr2[i][j] != 0:
            cnt2 += 1
            bfs(i, j, arr2[i][j], arr2)

print(cnt, cnt2)
