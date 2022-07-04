# https://www.acmicpc.net/problem/21610
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

q = deque()
q.append((n-1, 0))
q.append((n-1, 1))
q.append((n-2, 0))
q.append((n-2, 1))

for i in range(m):
    d, s = map(int, input().split())
    visited = [[0] * n for _ in range(n)]
    while q:
        x, y = q.popleft()
        nx = (x + dx[d-1]*s) % n
        ny = (y + dy[d-1]*s) % n
        visited[nx][ny] = 1

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                arr[i][j] += 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                x, y = i, j
                cnt = 0
                for k in [1, 3, 5, 7]:
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] > 0:
                            cnt += 1
                arr[x][y] += cnt
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and arr[i][j] >= 2:
                arr[i][j] -= 2
                q.append((i, j))


result = 0
for a in arr:
    result += sum(a)
print(result)