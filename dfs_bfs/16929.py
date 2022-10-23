# https://www.acmicpc.net/problem/16929
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]
visited = [[0] * m for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dfs(x, y, cnt):
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == arr[x][y]:
            if visited[nx][ny] == 0:
                visited[nx][ny] = cnt + 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0
            elif cnt + 1 >= 4 and visited[nx][ny] == 1:
                print("Yes")
                exit()
    return


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1)

print("No")
