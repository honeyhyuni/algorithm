# https://www.acmicpc.net/problem/16724
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]

dd = {"D": (1, 0), "L": (0, -1), "U": (-1, 0), "R": (0, 1)}
visited = [[0] * m for i in range(n)]

ans = 0


def dfs(x, y, idx):
    global ans
    visited[x][y] = idx
    d = arr[x][y]
    nx = x + dd[d][0]
    ny = y + dd[d][1]
    if visited[nx][ny] == 0:
        dfs(nx, ny, idx)
    else:
        if visited[nx][ny] == visited[x][y]:
            ans += 1
        return


idx = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, idx)
            idx += 1
print(ans)