# https://www.acmicpc.net/problem/25688
from collections import deque
import sys
input = sys.stdin.readline
arr = [list(map(int, input().split())) for i in range(5)]
x, y = map(int, input().split())
visited = [[[-1 for i in range(128)] for i in range(5)] for i in range(5)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([(x, y, 1)])

while q:
    x, y, c = q.popleft()
    if c == 127:
        print(visited[x][y][c] + 1)
        break
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] != -1:
            if arr[nx][ny] == 0:
                temp = c
            else:
                if c & c << arr[nx][ny] == c:
                    continue
                temp = c | 1 << arr[nx][ny]
            if visited[nx][ny][temp] == -1:
                visited[nx][ny][temp] = visited[x][y][c] + 1
                q.append((nx, ny, temp))
else:
    print(-1)