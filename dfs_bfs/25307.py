# https://www.acmicpc.net/problem/25307
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def dont_go():
    maq_q = deque(mannequin)
    while maq_q:
        x, y, cnt = maq_q.popleft()
        if cnt < k:
            for _ in range(4):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    maq_q.append((nx, ny, cnt+1))


input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
q = deque()
mannequin = []
visited = [[False] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 4:
            q.append((i, j, 0))
        elif arr[i][j] == 3:
            mannequin.append((i, j, 0))
            visited[i][j] = True

dont_go()
while q:
    x, y, cnt = q.popleft()
    if arr[x][y] == 2:
        print(cnt)
        break
    for _ in range(4):
        nx = x + dx[_]
        ny = y + dy[_]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny, cnt + 1))
else:
    print(-1)