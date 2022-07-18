# https://www.acmicpc.net/problem/1938
import sys

input = sys.stdin.readline
from collections import deque

dx, dy = [-1, 1, 0, 0, -1, -1, 1, 1], [0, 0, -1, 1, -1, 1, -1, 1]

n = int(input())
arr = [list(map(str, input().rstrip())) for i in range(n)]

b_list, e_list = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "B":
            b_list.append((i, j))
        if arr[i][j] == "E":
            e_list.append((i, j))
if b_list[1][0] - b_list[0][0] == 1:
    d = 1
else:
    d = 0
if e_list[1][0] - e_list[0][0] == 1:
    ed = 1
else:
    ed = 0
ex, ey = e_list[1][0], e_list[1][1]
q = deque()
q.append((b_list[1][0], b_list[1][1], d, 0))
visited = set()
visited.add((b_list[1][0], b_list[1][1], d))


def rotate_tree(x, y, d):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == '1':
            return False, False
    if d == 1:
        return True, 0
    else:
        return True, 1


def bfs():
    while q:
        x, y, d, cnt = q.popleft()
        if x == ex and y == ey and d == ed:
            return cnt
        bol, nd = rotate_tree(x, y, d)
        if bol and (x, y, nd) not in visited:
            q.append((x, y, nd, cnt + 1))
            visited.add((x, y, nd))
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != '1':
                if d == 1:
                    if 0 <= nx - 1 < n and 0 <= nx + 1 < n and (nx, ny, d) not in visited:
                        if arr[nx - 1][ny] != '1' and arr[nx + 1][ny] != '1':
                            visited.add((nx, ny, 1))
                            q.append((nx, ny, 1, cnt + 1))
                else:
                    if 0 <= ny - 1 < n and 0 <= ny + 1 < n and (nx, ny, d) not in visited:
                        if arr[nx][ny - 1] != '1' and arr[nx][ny + 1] != '1':
                            visited.add((nx, ny, 0))
                            q.append((nx, ny, 0, cnt + 1))

    return 0


print(bfs())
