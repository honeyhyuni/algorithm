# https://www.acmicpc.net/problem/16197
import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    while q:
        x, y, x1, y1, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            nx2 = x1 + dx[_]
            ny2 = y1 + dy[_]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if arr[nx][ny] == "#":
                    nx = x
                    ny = y
                if arr[nx2][ny2] == "#":
                    nx2 = x1
                    ny2 = y1
                q.append((nx, ny, nx2, ny2, cnt + 1))
            elif 0 <= nx < n and 0 <= ny < m:
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
            else:
                continue
    return -1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))

q = deque()
a = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "o":
            a.append([i, j])
q.append((a[0][0], a[0][1], a[1][0], a[1][1], 0))

print(bfs())
