# https://www.acmicpc.net/problem/1012
import sys
from collections import deque

t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, i, j):
    q = deque()
    q.append((i, j))
    arr[i][j] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1:
                arr[nx][ny] = 0 # 방문처리
                q.append((nx, ny))


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    arr = [[0] * m for _ in range(n)]
    cnt = 0
    for i in range(k):
        a, b = map(int, sys.stdin.readline().split())
        arr[b][a] = 1
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                bfs(arr, i, j)

    print(cnt)