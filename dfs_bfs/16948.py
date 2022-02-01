# https://www.acmicpc.net/problem/16948
import sys
from collections import deque
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

input = sys.stdin.readline
n = int(input())
arr = [[-1] * n for i in range(n)]

r1, c1, r2, c2 = map(int, input().split())

arr[r1][c1] = 0
q = deque()
q.append((r1, c1))
while q:
    x, y = q.popleft()
    for _ in range(6):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == -1:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

print(arr[r2][c2])
