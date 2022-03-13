# https://www.acmicpc.net/problem/1261
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < m and 0 <= ny < n:
                if a[nx][ny] == 0 and visited[nx][ny] == -1:  # 벽이 아니면 부실 필요가 없으므로 카운팅을 하지않고 appendleft 사용
                    visited[nx][ny] = visited[x][y]
                    q.appendleft((nx, ny))
                elif a[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    return visited[m - 1][n - 1]


n, m = map(int, input().split())

a = []
visited = [[-1] * n for _ in range(m)]
for _ in range(m):
    a.append(list(map(int, input())))

print(bfs())
