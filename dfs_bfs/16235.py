# https://www.acmicpc.net/problem/16235
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def spring():
    for i in range(n):
        for j in range(n):
            len_ = len(tree_age[i][j])
            for k in range(len_):
                if arr[i][j] < tree_age[i][j][k]:
                    for _ in range(k, len_):
                        dead_trees[i][j].append(tree_age[i][j].pop())
                    break
                else:
                    arr[i][j] -= tree_age[i][j][k]
                    tree_age[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while dead_trees[i][j]:
                arr[i][j] += dead_trees[i][j].pop() // 2


def fall():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree_age[i][j])):
                if tree_age[i][j][k] % 5 == 0:
                    for _ in range(8):
                        nx, ny, = i + dx[_], j + dy[_]

                        if 0 <= nx < n and 0 <= ny < n:
                            tree_age[nx][ny].appendleft(1)

            arr[i][j] += sd[i][j]


n, m, k = map(int, input().split())
sd = []
for i in range(n):
    sd.append(list(map(int, input().split())))
arr = [[5] * n for i in range(n)]
tree_age = [[deque() for _ in range(n)] for _ in range(n)]
dead_trees = [[list() for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, z = map(int, input().split())
    tree_age[x-1][y-1].append(z)

result = 0

for i in range(k):
    spring()
    fall()

for i in range(n):
    for j in range(n):
        result += len(tree_age[i][j])
print(result)
