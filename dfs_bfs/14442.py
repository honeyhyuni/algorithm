# https://www.acmicpc.net/problem/14442
import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m, k = map(int, input().split())
arr = [list(map(int, input().rstrip())) for i in range(n)]


def bfs():
    visited = [[[0] * (k + 1) for i in range(m)] for i in range(n)]
    q = deque()
    q.append((0, 0, k))
    visited[0][0][k] = 1
    while q:
        x, y, wall = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and not visited[nx][ny][wall]:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
                elif arr[nx][ny] == 1:
                    if wall and not visited[nx][ny][wall - 1]:
                        visited[nx][ny][wall - 1] = visited[x][y][wall] + 1
                        q.append((nx, ny, wall - 1))

    return visited[n-1][m-1]


min_v = bfs()
result = sys.maxsize
for i in min_v:
    if i and result > i:
        result = i

print(-1 if result >= sys.maxsize else result)
