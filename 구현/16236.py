# https://www.acmicpc.net/problem/16236
import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(i, j):
    visited = [[-1] * n for _ in range(n)]
    visited[i][j] = 0
    eat = []
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if arr[nx][ny] == arr[i][j] or arr[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                if arr[nx][ny] != 0 and arr[nx][ny] < arr[i][j]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    eat.append((nx, ny, visited[nx][ny]))
    if not eat:
        return -1, -1, -1
    eat.sort(key=lambda z: (z[2], z[0], z[1]))
    return eat[0][0], eat[0][1], eat[0][2]


input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            arr[i][j] = 2
            x1, y1 = i, j

cnt = 0
weight = 0
while True:
    nx_, ny_, dist = bfs(x1, y1)
    if nx_ == -1:
        break
    cnt += dist
    weight += 1
    arr[nx_][ny_] = arr[x1][y1]
    arr[x1][y1] = 0
    x1, y1 = nx_, ny_
    if arr[x1][y1] == weight:
        arr[x1][y1] += 1
        weight = 0
print(cnt)
