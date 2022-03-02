# https://www.acmicpc.net/problem/13565
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    a[i][j] = 1
    while q:
        x, y = q.popleft()
        if x == n - 1:
            return 0
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 0:
                a[nx][ny] = 1
                q.append((nx, ny))
    return -1


n, m = map(int, input().split())

a = []

for _ in range(n):
    a.append(list(map(int, input())))
result = []
for i in range(m):
    if a[0][i] == 0:
        result.append(bfs(0, i))

if 0 in result:
    print("YES")
else:
    print("NO")
