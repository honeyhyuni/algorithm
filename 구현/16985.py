# https://www.acmicpc.net/problem/16985
import copy
import sys
from itertools import permutations
from collections import deque

INF = sys.maxsize
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = sys.stdin.readline
arr = [[list(map(int, input().split())) for i in range(5)] for i in range(5)]
temp = list(permutations(range(5)))


def copy_arr(a, idx):
    t = copy.deepcopy(a)
    t[0], t[1], t[2], t[3], t[4] = t[idx[0]], t[idx[1]], t[idx[2]], t[idx[3]], t[idx[4]]
    return t


def bfs(a):
    visited = [[[INF] * 5 for i in range(5)] for i in range(5)]
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 0
    while q:
        x, y, z = q.popleft()
        if x == 4 and y == 4 and z == 4:
            return visited[4][4][4]
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny][z] == INF and a[nx][ny][z] == 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
        for _ in [z - 1, z + 1]:
            nz = _
            if 0 <= nz < 5 and visited[x][y][nz] == INF and a[x][y][nz] == 1:
                visited[x][y][nz] = visited[x][y][z] + 1
                q.append((x, y, nz))
    return INF


result = INF


def back(a, c):
    global result
    if c == 5:
        if a[4][4][4]:
            result = min(result, bfs(a))
        return
    for i in range(4):
        if a[0][0][0]:
            back(copy.deepcopy(a), c + 1)
        a[c] = list(map(list, zip(*a[c][::-1])))


for i in temp:
    temp_arr = copy_arr(arr, i)
    back(temp_arr, 0)

print(result if result != INF else -1)
