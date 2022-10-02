# https://www.acmicpc.net/problem/16920
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = sys.stdin.readline
n, m, p = map(int, input().split())
cango = [0] + list(map(int, input().split()))
arr = [list(map(str, input().rstrip())) for i in range(n)]
answer = [0] * (p + 1)

idx = [deque() for _ in range(p + 1)]

for i in range(n):
    for j in range(m):
        if arr[i][j] != "." and arr[i][j] != "#":
            idx[int(arr[i][j])].append((i, j))
            answer[int(arr[i][j])] += 1


def bfs(v, t):
    cnt = 0
    for k in range(t):
        len_ = len(idx[v])
        if not idx[v]:
            return cnt
        for __ in range(len_):
            x, y = idx[v].popleft()
            for _ in range(4):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == ".":
                    arr[nx][ny] = v
                    cnt += 1
                    idx[v].append((nx, ny))
    return cnt


while True:
    bol = True
    for i in range(1, p + 1):
        if not idx[i]:
            continue
        cnt = bfs(i, cango[i])
        if cnt != 0:
            bol = False
        answer[i] += cnt
    if bol:
        break
print(*answer[1:])
