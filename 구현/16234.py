# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

input = sys.stdin.readline


def check(i, j):
    q = deque()
    q.append((i, j))
    xy = [[i, j]]
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    xy.append((nx, ny))
    return xy


def move():
    m = 0
    for i, j in xy:
        m += arr[i][j]
    for i, j in xy:
        arr[i][j] = int(m / len(xy))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, L, R = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

cnt = 0
while True:
    bol = False
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                xy = check(i, j)
                if len(xy) > 1:  # 두개이상의 나라가 인접한경우에 인구이동 가능
                    move()
                    bol = True
    if not bol:
        break
    cnt += 1
print(cnt)
