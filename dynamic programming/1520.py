# https://www.acmicpc.net/problem/1520
# dp + dfs
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[-1] * m for i in range(n)]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] < arr[x][y]:
                visited[x][y] += dfs(nx, ny)
    return visited[x][y]


print(dfs(0, 0))
