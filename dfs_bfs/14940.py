# https://www.acmicpc.net/problem/14940
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                visited[i][j] = 0
    return visited


n, m = map(int, input().split())

arr = []
visited = [[-1] * m for _ in range(n)]
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)

for i in range(n):
    print(' '.join(map(str, visited[i])))