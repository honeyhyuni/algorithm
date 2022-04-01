# https://www.acmicpc.net/problem/24463
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
sys.setrecursionlimit(10 ** 5)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))

xy = []
for i in range(n):
    for j in range(m):
        if (i != 0 and i != n - 1) and (j != 0 and j != m - 1):
            continue
        else:
            if arr[i][j] == ".":
                xy.append([i, j])

(sx, sy), (ex, ey) = xy
visited = [[-1] * m for i in range(n)]
visited[sx][sy] = 0
q = deque()


def dfs(x, y):
    if x == ex and y == ey:
        return True
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
            if arr[nx][ny] == ".":
                visited[nx][ny] = visited[x][y] + 1
                if dfs(nx, ny):
                    return True
    visited[x][y] = -1
    return False


dfs(sx, sy)
for i in range(n):
    for j in range(m):
        if arr[i][j] == "+":
            print("+", end='')
        elif arr[i][j] == "." and visited[i][j] == -1:
            print("@", end='')
        else:
            print(".", end='')
    print()
