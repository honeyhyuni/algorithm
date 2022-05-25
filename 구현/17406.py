# https://www.acmicpc.net/problem/17406
import copy
from itertools import permutations
import sys


input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
k_list = [list(map(int, input().split())) for i in range(k)]

per = list(permutations(range(k)))
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def rotate_arr(sx, sy, ex, ey):
    tmp = temp[sx][sy]
    x, y = sx, sy
    for _ in range(4):
        while True:
            x = x + dx[_]
            y = y + dy[_]
            if not (sx <= x <= ex and sy <= y <= ey):
                x = x - dx[_]
                y = y - dy[_]
                break
            tmp, temp[x][y] = temp[x][y], tmp


result = sys.maxsize
for p in per:
    temp = copy.deepcopy(arr)
    for i in p:
        r, s, c = k_list[i]
        for j in range(c):
            sx, sy = r - c - 1 + j, s - c - 1 + j
            ex, ey = r + c - 1 - j, s + c - 1 - j
            rotate_arr(sx, sy, ex, ey)
    for t in temp:
        result = min(result, sum(t))
print(result)
