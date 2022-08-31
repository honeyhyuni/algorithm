# https://www.acmicpc.net/problem/16956
import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q.append((i, j))

while q:
    x, y = q.popleft()
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 'W':
                print(0)
                break
            elif arr[nx][ny] == '.':
                arr[nx][ny] = 'D'
else:
    print(1)
    for i in arr:
        print("".join(i))