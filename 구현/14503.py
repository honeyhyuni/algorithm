# https://www.acmicpc.net/problem/14503
import sys

input = sys.stdin.readline


def bfs(x, y, d):
    global cnt
    if arr[x][y] == 0:
        arr[x][y] = 2
        cnt += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0:
            bfs(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    bfs(nx, ny, d)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
cnt = 0
bfs(r, c, d)
print(cnt)
