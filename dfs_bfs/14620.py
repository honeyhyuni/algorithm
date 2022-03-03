# https://www.acmicpc.net/problem/14620
import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def check(nodes):
    visited = []
    q = deque()
    flower = 0
    for i, j in nodes:
        q.append((i, j))
        visited.append((i, j))
        flower += arr[i][j]
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if (nx, ny) in visited:
                return INF
            else:
                flower += arr[nx][ny]
                visited.append((nx, ny))
    return flower


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

a = [(i, j) for i in range(1, n - 1) for j in range(1, n - 1)]
INF = sys.maxsize
min_v = INF
comb = list(combinations(a, 3))
for i in comb:
    min_v = min(min_v, check(i))
print(min_v)
