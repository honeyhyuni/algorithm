# https://www.acmicpc.net/problem/18809
import sys
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline
n, m, g, r = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
garden = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            garden.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
ans = 0


def makeFlower():
    global cnt
    len_q = len(q)
    new_arr = defaultdict(int)
    for _ in range(len_q):
        x, y, v = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != 0:
                if not visited[nx][ny] and new_arr[(nx, ny)] != v:
                    new_arr[(nx, ny)] += v
    for i, j in new_arr.items():
        visited[i[0]][i[1]] = True
        if j >= 3:
            cnt += 1
        else:
            q.append((i[0], i[1], j))


def plus_q(v, b):
    for i in v:
        x, y = garden[i]
        q.append((x, y, b))
        visited[x][y] = True


for total in combinations(range(len(garden)), r+g):
    for g_list in combinations(total, g):
        r_list = set(total) - set(g_list)
        q = deque()
        visited = [[False] * m for i in range(n)]
        plus_q(g_list, 1)
        plus_q(r_list, 2)
        cnt = 0
        while q:
            makeFlower()
        ans = max(ans, cnt)

print(ans)