# https://www.acmicpc.net/problem/11559
import sys
from collections import deque

input = sys.stdin.readline


def popandin(xy):
    q = deque()
    for j in range(6):
        for i in range(11, -1, -1):
            if arr[i][j] != ".":
                q.append((arr[i][j]))
        for k in range(11, -1, -1):
            if q:
                arr[k][j] = q.popleft()
            else:
                arr[k][j] = "."


def bfs(i, j, S):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    xy.append((i, j))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny]:
                if arr[nx][ny] == S:
                    q.append((nx, ny))
                    xy.append((nx, ny))
                    visited[nx][ny] = True


result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
for i in range(12):
    arr.append(list(map(str, input().rstrip())))

while True:
    bol = False
    visited = [[False] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != ".":
                xy = []
                bfs(i, j, arr[i][j])
                if len(xy) >= 4:
                    bol = True
                    for i, j in xy:
                        arr[i][j] = "."
    if not bol:
        break
    popandin(xy)
    result += 1
print(result)