# https://www.acmicpc.net/problem/1926
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    a[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                a[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

cnt_2 = 0 # 그림의 개수
result = 0 # 가장 넓은 그림의 넓이

for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            result = max(result, bfs(i, j))
            cnt_2 += 1
print(cnt_2)
print(result)
