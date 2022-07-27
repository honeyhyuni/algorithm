# https://www.acmicpc.net/problem/20057
import math
import sys

input = sys.stdin.readline
from collections import deque

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

d_dic = {0: [(-1, 0, 7), (-1, -1, 10), (-1, 1, 1), (-2, 0, 2), (0, -2, 5), (1, -1, 10), (1, 0, 7), (1, 1, 1), (2, 0, 2), (0, -1)],
         1: [(0, -1, 7), (0, -2, 2), (-1, -1, 1), (1, -1, 10), (2, 0, 5), (0, 1, 7), (-1, 1, 1), (1, 1, 10), (0, 2, 2), (1, 0)]}
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
q = deque()
q.append((n // 2, n // 2, 0, 1, 1))


def tornado():
    ans = 0
    while q:
        x, y, d, cnt, c = q.popleft()
        for _ in range(1, cnt + 1):
            nx = x + dx[d] * _
            ny = y + dy[d] * _
            if ny < 0:
                return ans
            temp = arr[nx][ny]
            if d == 0 or d == 1:nd = d
            else:nd = d - 2
            temp_v = temp
            arr[nx][ny] = 0
            for i in range(9):
                a, b, v = d_dic[nd][i]
                if d == 2:b = -b
                elif d == 3:a = -a
                nnx = nx + a
                nny = ny + b
                t = math.trunc(temp * v / 100)
                if not (0 <= nnx < n and 0 <= nny < n):
                    ans += t
                else:
                    arr[nnx][nny] += t
                temp_v -= t
            a, b = d_dic[nd][-1]
            if d == 2:b = -b
            elif d == 3:a = -a
            nnx = nx + a
            nny = ny + b
            if not (0 <= nnx < n and 0 <= nny < n):
                ans += temp_v
            else:
                arr[nnx][nny] += temp_v

        if c == 1:c += 1
        else:
            c = 1
            cnt += 1
        q.append((nx, ny, (d + 1) % 4, cnt, c))


print(tornado())
