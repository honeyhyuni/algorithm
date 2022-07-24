# https://www.acmicpc.net/problem/15644
import sys

input = sys.stdin.readline
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dd = ["U", "D", "L", "R"]
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]

visited = set()
len_ = max(n, m)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j
        elif arr[i][j] == 'O':
            ex, ey = i, j
q = deque()

q.append((rx, ry, bx, by, 0, ""))
visited.add((rx, ry, bx, by))


def bfs():
    while q:
        rx, ry, bx, by, cnt, temp = q.popleft()
        if cnt > 10:
            return -1, -1
        if rx == ex and ry == ey:
            return cnt, temp
        for _ in range(4):
            bol = False
            red, blue = [rx, ry], [bx, by]
            for __ in range(1, len_):
                nrx = rx + dx[_] * __
                nry = ry + dy[_] * __
                if arr[nrx][nry] == 'O':
                    red = [nrx, nry]
                    break
                if arr[nrx][nry] != "#":
                    red = [nrx, nry]
                else:
                    break
            for __ in range(1, len_):
                nbx = bx + dx[_] * __
                nby = by + dy[_] * __
                if arr[nbx][nby] == 'O':
                    bol = True
                    break
                elif arr[nbx][nby] != '#':
                    blue = [nbx, nby]
                else:
                    break
            if bol:
                continue
            if red == blue:
                if abs(red[0] - rx) + abs(red[1] - ry) > abs(blue[0] - bx) + abs(blue[1] - by):
                    red[0] -= dx[_]
                    red[1] -= dy[_]
                else:
                    blue[0] -= dx[_]
                    blue[1] -= dy[_]
            if (red[0], red[1], blue[0], blue[1]) not in visited:
                visited.add((red[0], red[1], blue[0], blue[1]))
                q.append((red[0], red[1], blue[0], blue[1], cnt + 1, temp + dd[_]))
    return -1, -1


c, t = bfs()
if c == -1:
    print(t)
else:
    print(c)
    print(t)
