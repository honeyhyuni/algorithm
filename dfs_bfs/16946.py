# https://www.acmicpc.net/problem/16946
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for i in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j]: result[i][j] = 1


def bfs(i, j):
    visited[i][j] = True
    cnt = 1
    q = deque()
    q.append((i, j))
    temp = []
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if not arr[nx][ny]:
                    q.append((nx, ny))
                    cnt += 1
                    visited[nx][ny] = True
                else:
                    temp.append((nx, ny))
                    visited[nx][ny] = True
    for x, y in temp:
        visited[x][y] = False
        result[x][y] += cnt
        result[x][y] %= 10


visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)

for i in result:
    print("".join(map(str, i)))
