# https://www.acmicpc.net/problem/2589
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    result2 = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] != "W" and visited[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                visited[nx][ny] = 1
                result2 = max(result2, arr[nx][ny])
                q.append((nx, ny))
    return result2


n, m = map(int, input().split())
arr = []
result = 0

for _ in range(n):
    arr.append(list(map(str, input())))

for i in range(n):
    for j in range(m):
        if arr[i][j] != "W":
            visited = [[0] * m for _ in range(n)]
            visited[i][j] = 1
            arr[i][j] = 0
            result = max(result, bfs(i, j))
print(result)