# https://www.acmicpc.net/problem/2206
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    visited[0][0][1] = 1
    q = deque()
    q.append((0, 0, 1))
    while q:
        x, y, wall = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[n - 1][m - 1][wall]
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1 and wall == 1:
                    visited[nx][ny][0] = visited[x][y][wall] + 1
                    q.append((nx, ny, 0))
                elif arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
    return -1

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().rstrip())))

visited = [[[0, 0] for i in range(m)] for i in range(n)]
print(bfs())