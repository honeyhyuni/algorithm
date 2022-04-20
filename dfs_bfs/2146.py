# https://www.acmicpc.net/problem/2146
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global cnt
    visited[i][j] = 0
    q = deque()
    q.append((i, j))
    arr[i][j] = cnt
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = 0
                    arr[nx][ny] = cnt
                    q.append((nx, ny))


def bfs2(c):
    global min_v
    visited2 = [[-1] * n for i in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j] == c:
                q.append((i, j))
                visited2[i][j] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                if visited2[nx][ny] == -1 and arr[nx][ny] == 0:
                    visited2[nx][ny] = visited2[x][y] + 1
                    q.append((nx, ny))
                elif visited2[nx][ny] == -1 and arr[nx][ny] != c:
                    min_v = min(min_v, visited2[x][y])
                    return


input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cnt = 1
min_v = sys.maxsize
visited = [[-1] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and visited[i][j] == -1:
            bfs(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs2(i)

print(min_v)
