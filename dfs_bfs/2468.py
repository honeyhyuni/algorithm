# https://www.acmicpc.net/problem/2468
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] > cnt:
                q.append((nx, ny))
                visited[nx][ny] = True
    return 1


cnt = max(map(max, arr))

result = []

while cnt >= 0:
    visited = [[False] * n for i in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] > cnt:
                temp += bfs(i, j)
    result.append(temp)
    cnt -= 1

print(max(result))
