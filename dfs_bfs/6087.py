# https://www.acmicpc.net/problem/6087
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    visited[i][j] = 0
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            while True:
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if arr[nx][ny] == "*":
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break

                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[_]
                ny += dy[_]


m, n = map(int, input().split())
arr = []
INF = sys.maxsize
visited = [[INF] * m for i in range(n)]
for i in range(n):
    arr.append(list(map(str, input())))

C_ = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == "C":
            C_.append((i, j))
(x1, y1), (x2, y2) = C_

bfs(x1, y1)
print(visited[x2][y2] - 1)
for i in visited:
    print(*i)