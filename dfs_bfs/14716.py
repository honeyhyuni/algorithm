# https://www.acmicpc.net/problem/14716
import sys
from collections import deque

dx = [1, -1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

cnt = 0


def bfs(i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        x, y = q.popleft()
        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    q.append((nx, ny))


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)
