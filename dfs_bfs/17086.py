# https://www.acmicpc.net/problem/17086
import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def bfs(q):
    while q:
        x, y = q.popleft()
        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

bfs_arr = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs_arr.append((i, j))

bfs(bfs_arr)
result = 0

for i in range(n):
    for j in range(m):
        result = max(result, arr[i][j])
print(result - 1)
