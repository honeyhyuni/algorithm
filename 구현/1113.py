# https://www.acmicpc.net/problem/1113
import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for i in range(n)]

result = 0


def check(i, j, v):
    visited = [[False] * m for i in range(n)]
    visited[i][j] = True
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] <= v and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
            else:
                return False
    return True


for i in range(1, n - 1):
    for j in range(1, m - 1):
        v = arr[i][j]
        while check(i, j, v):
            v += 1
        result += v - arr[i][j]
print(result)
