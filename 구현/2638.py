# https://www.acmicpc.net/problem/2638
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited = [[-1] * m for i in range(n)]
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1:
                    if arr[nx][ny] >= 1:
                        arr[nx][ny] += 1
                    else:
                        visited[nx][ny] = 0
                        q.append((nx, ny))


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append((list(map(int, input().split()))))

cnt = 0
while True:
    bfs()
    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
                c = 1
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if c == 1:
        cnt += 1
    else:
        break

print(cnt)
