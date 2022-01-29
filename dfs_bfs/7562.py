# https://www.acmicpc.net/problem/7562
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]


def bfs(a, b, x, y):
    q = deque()
    q.append((a, b))
    if a == x and b == y:
        return 0
    while q:
        x2, y2 = q.popleft()
        for _ in range(8):
            nx = x2 + dx[_]
            ny = y2 + dy[_]
            if 0 <= nx < L and 0 <= ny < L and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x2][y2] + 1
                if nx == x and ny == y:
                    return arr[nx][ny]
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    arr = []
    L = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    arr = [[0] * L for _ in range(L)]
    print(bfs(a, b, x, y))
