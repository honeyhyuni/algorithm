# https://www.acmicpc.net/problem/17836
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, t = map(int, input().split())
arr = []
visited = [[0] * m for _ in range(n)]
tmp = 123456789
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def bfs():
    global tmp
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        if arr[x][y] == 2:
            tmp = abs(n - 1 - x) + abs(m - 1 - y) + visited[x][y] - 1
        if x == n - 1 and y == m - 1:
            return min(visited[x][y] - 1, tmp)
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny]:
                    if arr[nx][ny] != 1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
    return tmp


result = bfs()

if result > t:
    print("Fail")
else:
    print(result)
