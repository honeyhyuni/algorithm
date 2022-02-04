# https://www.acmicpc.net/problem/1303
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(W, i, j):
    cnt = 1
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if arr[nx][ny] == W and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt


n, m = map(int, input().split())
arr = []
b_sum = 0
w_sum = 0
visited = [[False] * n for _ in range(m)]
for i in range(m):
    arr.append(list(map(str, input())))

for i in range(m):  # 방문한적이 없는 W or B
    for j in range(n):
        if arr[i][j] == 'W' and not visited[i][j]: # bfs 리턴할때마다 제곱값을 더해준다
            w_sum += pow(bfs('W', i, j), 2)
        elif arr[i][j] == 'B' and not visited[i][j]:
            b_sum += pow(bfs('B', i, j), 2)
print(w_sum, b_sum)
