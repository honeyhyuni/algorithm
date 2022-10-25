# https://www.acmicpc.net/problem/24513
import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y, z = q.popleft()
        if visited[x][y][0] == 3:
            continue
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if (0 <= nx < n and 0 <= ny < m) and arr[nx][ny] != -1:
                if visited[nx][ny][0] == 0:
                    visited[nx][ny][0] = visited[x][y][0]
                    q.append([nx, ny, z + 1])
                    visited[nx][ny][1] = z + 1
                elif visited[nx][ny][0] != visited[x][y][0] and visited[nx][ny][0] != 0 and visited[nx][ny][0] != 3:
                    if visited[nx][ny][1] == visited[x][y][1] + 1:
                        visited[nx][ny][0] = 3


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[[0, 0] for i in range(m)] for i in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j, 0])
            visited[i][j][0] = 1
        elif arr[i][j] == 2:
            q.append([i, j, 0])
            visited[i][j][0] = 2

bfs()
result = [0] * 3
for i in range(n):
    for j in range(m):
        if visited[i][j][0] == 1:
            result[0] += 1
        elif visited[i][j][0] == 2:
            result[1] += 1
        elif visited[i][j][0] == 3:
            result[2] += 1
print(" ".join(map(str, result)))
