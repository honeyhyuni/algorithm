# https://www.acmicpc.net/problem/5427
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = sys.maxsize


def bfs_fire():
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == "#":
                continue
            if arr[nx][ny] != "#" and visited[nx][ny] == INF:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


def bfs_people():
    while pq:
        x, y = pq.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == "#":
                continue
            elif arr[nx][ny] == "." and visited2[nx][ny] == INF:
                visited2[nx][ny] = visited2[x][y] + 1
                pq.append((nx, ny))


T = int(input())
for t in range(T):
    m, n = map(int, input().split())
    arr = []
    q = deque()
    pq = deque()
    visited = [[INF] * m for _ in range(n)]
    visited2 = [[INF] * m for _ in range(n)]
    for i in range(n):
        arr.append(list(map(str, input().rstrip())))
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "*":
                q.append((i, j))
                visited[i][j] = 0
            elif arr[i][j] == "@":
                pq.append((i, j))
                visited2[i][j] = 0
    bfs_fire()
    bfs_people()
    result = INF
    for i in range(n):
        for j in range(m):
            if i != 0 and i != n - 1 and j != 0 and j != m - 1:
                continue
            if visited[i][j] > visited2[i][j]:
                result = min(result, visited2[i][j] + 1)
    if result >= INF:
        print("IMPOSSIBLE")
    else:
        print(result)
