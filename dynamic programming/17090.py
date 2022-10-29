# https://www.acmicpc.net/problem/17090
import sys
sys.setrecursionlimit(10 ** 5 + 300000)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().rstrip()) for i in range(n)]
dd = {"D": (1, 0), "U": (-1, 0), "L": (0, -1), "R": (0, 1)}
visited = [[-1] * m for i in range(n)]
ans = 0


def dfs(x, y, v, c):
    global ans
    d = dd[v]
    visited[x][y] = 0
    nx = x + d[0]
    ny = y + d[1]
    if not (0 <= nx < n and 0 <= ny < m):
        ans += c
        visited[x][y] = 1
        return True
    else:
        if visited[nx][ny] != -1:
            if visited[nx][ny] == 0:
                visited[x][y] = -1
                return False
            else:
                ans += c
                visited[x][y] = 1
                return True
        else:
            if dfs(nx, ny, arr[nx][ny], c+1):
                visited[x][y] = 1
                return True
            else:
                visited[x][y] = -1
                return False


for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            dfs(i, j, arr[i][j], 1)

print(ans)