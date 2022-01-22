# https://www.acmicpc.net/problem/1743
# bfs 이론 문제
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    cnt = 1
    a[i][j] = 0
    while q:
        v, c = q.popleft()
        for _ in range(4):
            nx = v + dx[_]
            ny = c + dy[_]
            if 0 <= nx <= n and 0 <= ny <= m and a[nx][ny] == 1:
                cnt += 1
                a[nx][ny] = 0 # 방문한곳 방문처리
                q.append((nx, ny))
    return cnt


n, m, k = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]
result = 0

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    a[x][y] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == 1:
            result = max(result, bfs(i, j))
print(result)

