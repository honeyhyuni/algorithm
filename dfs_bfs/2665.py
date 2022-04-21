# https://www.acmicpc.net/problem/2665
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                elif a[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited[n - 1][n - 1]


n = int(input())

a = []

visited = [[-1] * n for _ in range(n)]

for _ in range(n):
    a.append(list(map(int, input())))

print(bfs())

