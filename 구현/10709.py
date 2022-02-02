# https://www.acmicpc.net/problem/10709
from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))
visited = [[0] * m for i in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            visited[i][j] = -1
        if arr[i][j] == "c":
            q.append((i, j))

while q:
    x, y = q.popleft()
    ny = y + 1
    if 0 <= ny < m:
        if arr[x][ny] == ".":
            visited[x][ny] = visited[x][y] + 1
            q.append((x, ny))

for i in visited:
    print(*i)