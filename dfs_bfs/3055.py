# https://www.acmicpc.net/problem/3055
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]
visited = [[-1] * m for _ in range(n)]
q = deque()

# 고슴도치 먼저 돌고 물이 돌게
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            q.appendleft((i, j))
            visited[i][j] = 0
        elif arr[i][j] == "*":
            q.append((i, j))
        elif arr[i][j] == "D":
            ex, ey = i, j


def bfs(ex, ey):
    while q:
        if arr[ex][ey] == "S":
            return visited[ex][ey]
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                # 고슴도치의 위치가 물한테 잠식당하지 않았다면
                if arr[x][y] == "S":
                    if visited[nx][ny] == -1 and (arr[nx][ny] == "." or arr[nx][ny] == "D"):
                        arr[nx][ny] = "S"
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                else:
                    if arr[nx][ny] == "." or arr[nx][ny] == "S":
                        arr[nx][ny] = "*"
                        q.append((nx, ny))
    return "KAKTUS"


print(bfs(ex, ey))
