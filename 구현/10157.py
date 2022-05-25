# https://www.acmicpc.net/problem/10157
from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

m, n = map(int, input().split())
k = int(input())
if k > m*n:
    print(0)
else:
    arr = [[0] * m for i in range(n)]
    q = deque()
    q.append([n-1, 0, 0])
    arr[n-1][0] = 1
    while q:
        x, y, d = q.popleft()
        if arr[x][y] == k:
            print(y+1, n-x)
            break
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            q.append([nx, ny, d])
            arr[nx][ny] = arr[x][y] + 1
        else:
            q.append([x, y, (d+1) % 4])