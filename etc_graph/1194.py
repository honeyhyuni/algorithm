# https://www.acmicpc.net/problem/1194
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]

visited = [[[0] * 64 for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == "0":
            sx, sy = i, j
            arr[i][j] = "."


def bfs():
    q = deque()
    q.append((sx, sy, 0, 0))
    visited[sx][sy][0] = True
    while q:
        x, y, c, cnt = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not not visited[nx][ny][c]:
                if arr[nx][ny] == ".":
                    visited[nx][ny][c] = 1
                    q.append((nx, ny, c, cnt+1))
                elif arr[nx][ny].isupper():
                    if c & 1 << (ord(arr[nx][ny]) - 65):
                        q.append((nx, ny, c, cnt+1))
                        visited[nx][ny][c] = 1
                elif arr[nx][ny].islower():
                    nc = c | 1 << (ord(arr[nx][ny]) - 97)
                    if not visited[nx][ny][nc]:
                        visited[nx][ny][nc] = 1
                        q.append((nx, ny, nc, cnt+1))
                elif arr[nx][ny] == "1":
                    return cnt + 1
    return -1


print(bfs())
