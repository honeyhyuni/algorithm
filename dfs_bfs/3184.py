# https://www.acmicpc.net/problem/3184
import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    global v_c, o_c
    q = deque()
    q.append((i, j))
    cnt_v, cnt_o = 0, 0
    if arr[i][j] == "v":
        cnt_v += 1
    elif arr[i][j] == "o":
        cnt_o += 1
    arr[i][j] = "#"
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != "#":
                if arr[nx][ny] == "v":
                    cnt_v += 1
                if arr[nx][ny] == "o":
                    cnt_o += 1
                arr[nx][ny] = "#"
                q.append((nx, ny))
    if cnt_o > cnt_v:
        o_c += cnt_o
    else:
        v_c += cnt_v


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))

v_c, o_c = 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] != "#":
            bfs(i, j)
print(o_c, v_c)
