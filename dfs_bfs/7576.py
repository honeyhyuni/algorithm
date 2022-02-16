# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                a[nx][ny] = a[x][y] + 1
                q.append((nx, ny))


m, n = map(int, input().split())
a = []
q = deque()

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            q.append((i, j))
bfs()
result = -2
visited = False
for i in a:
    for j in i:
        if j == 0:
            visited = True
        result = max(result, j)


if visited:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)





