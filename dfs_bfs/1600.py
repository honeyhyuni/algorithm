# https://www.acmicpc.net/problem/1600
import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ddx = [-1, -2, -2, -1, 1, 2, 2, 1]
ddy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs():
    q = deque()
    q.append((0, 0, k))  # k는 벽을 부실수 있는 횟수
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z] == 0:
                if arr[nx][ny] == 1:
                    continue
                else:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append((nx, ny, z))
        if z >= 1:  # 벽을 한번이상 부실수 있을경우만 말처럼 움직일수 있음
            for _ in range(8):
                nx = x + ddx[_]
                ny = y + ddy[_]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][z - 1] == 0:
                    if arr[nx][ny] == 1:
                        continue
                    else:
                        visited[nx][ny][z - 1] = visited[x][y][z] + 1
                        q.append((nx, ny, z - 1))
    return -1


k = int(input())
m, n = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited = [[[0 for i in range(31)] for i in range(m)] for i in range(n)]

print(bfs())
