# https://www.acmicpc.net/problem/14497
import sys
from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False] * m for _ in range(n)]
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == "0" and not visited[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = True
                elif arr[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    arr[nx][ny] = "0"
                elif arr[nx][ny] == "#":
                    arr[nx][ny] = 2


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))
cnt = 0
while True:
    bfs(x1 - 1, y1 - 1)
    cnt += 1
    if arr[x2 - 1][y2 - 1] == 2:
        print(cnt)
        break
