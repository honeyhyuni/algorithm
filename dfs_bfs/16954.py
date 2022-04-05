# https://www.acmicpc.net/problem/16954
from collections import deque

dx = [0, -1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 0, -1, 1, -1, 1, -1, 1]


def bfs():
    q = deque()
    q.append((7, 0))
    while q:
        visited = [[False] * 8 for j in range(8)]
        for i in range(len(q)):
            x, y = q.popleft()
            if x == 0 and y == 7:
                return 1
            if arr[x][y] == "#":
                continue
            for _ in range(9):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not visited[nx][ny] and arr[nx][ny] == '.':
                        visited[nx][ny] = True
                        q.append((nx, ny))
        arr.pop()
        arr.insert(0, ['.', '.', '.', '.', '.', '.', '.', '.'])
    return 0


arr = []
for _ in range(8):
    arr.append(list(map(str, input())))

print(bfs())
