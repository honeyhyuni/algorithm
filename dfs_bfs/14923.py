# https://www.acmicpc.net/problem/14923
import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((x_ - 1, y_ - 1, 1))
    visited[x_ - 1][y_ - 1][1] = 1
    while q:
        x, y, wall = q.popleft()
        if x == x2 - 1 and y == y2 - 1:
            return visited[x2 - 1][y2 - 1][wall] - 1
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if wall == 1 and arr[nx][ny] == 1:
                    visited[nx][ny][0] = visited[x][y][wall] + 1
                    q.append((nx, ny, 0))
                elif visited[nx][ny][wall] == 0 and arr[nx][ny] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))
    return -1


n, m = map(int, input().split())
x_, y_ = map(int, input().split())
x2, y2 = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

visited = [[[0, 0] for i in range(m)] for i in range(n)]

print(bfs())