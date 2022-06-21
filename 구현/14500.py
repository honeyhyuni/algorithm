# https://www.acmicpc.net/problem/14500
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, idx, total):
    global result
    if result > total + (3- idx) * max_v:
        return
    if idx == 3:
        result = max(result, total)
        return
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if idx == 1:
                visited[nx][ny] = True
                dfs(x, y, idx+1, total+ arr[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            dfs(nx, ny, idx + 1, total + arr[nx][ny])
            visited[nx][ny] = False


arr = []
result = 0
for i in range(n):
    arr.append(list(map(int, input().split())))
max_v = max(map(max, arr))
visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, 0, arr[i][j])
            visited[i][j] = False


print(result)