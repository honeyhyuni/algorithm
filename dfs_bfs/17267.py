# https://www.acmicpc.net/problem/17267
import sys
input = sys.stdin.readline
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
l, r = map(int, input().split())
arr = [list(map(int, input().rstrip())) for i in range(n)]
q = deque()
visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append((i, j, l, r))
            visited[i][j] = True
            arr[i][j] = 0
total = 1
while q:
    x, y, l, r = q.popleft()
    for _ in range(2):
        for __ in range(1, n+1):
            nx = x + dx[_] * __
            if 0 <= nx < n and arr[nx][y] == 0:
                if not visited[nx][y]:
                    visited[nx][y] = True
                    q.append((nx, y, l, r))
                    total += 1
            else:
                break
    for _ in range(2, 4):
        if _ == 2 and l == 0:
            continue
        if _ == 3 and r == 0:
            continue
        ny = y + dy[_]
        if 0 <= ny < m and not visited[x][ny] and arr[x][ny] == 0:
            if _ == 2:
                q.append((x, ny, l-1, r))
            else:
                q.append((x, ny, l, r-1))
            visited[x][ny] = True
            total += 1
print(total)
