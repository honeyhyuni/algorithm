import copy
from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_result = 0


def bfs():
    global max_result
    visited = copy.deepcopy(arr)
    q = deque()
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 2:
                q.append((i, j))
    result = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 2
                    q.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                result += 1
    max_result = max(max_result, result)


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


def wall(value):
    if value == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(value + 1)
                arr[i][j] = 0


wall(0)
print(max_result)
