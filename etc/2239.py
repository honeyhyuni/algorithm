# https://www.acmicpc.net/problem/2239
import sys

input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(list(map(int, input().rstrip())))
q = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            q.append([i, j])


# 행확인
def horizontal(x, v):
    for i in range(9):
        if arr[x][i] == v:
            return False
    return True


# 열 확인
def vertical(x, v):
    for i in range(9):
        if arr[i][x] == v:
            return False
    return True


# 가로3 세로3 주변 확인
def division(x, y, v):
    x = (x // 3) * 3
    y = (y // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if arr[i][j] == v:
                return False
    return True


def dfs(idx):
    if idx == len(q):
        for i in range(9):
            print("".join(map(str, arr[i])))
        sys.exit()
    x, y = q[idx]
    for i in range(1, 10):
        if horizontal(x, i) and vertical(y, i) and division(x, y, i):
            arr[x][y] = i
            dfs(idx + 1)
            arr[x][y] = 0


dfs(0)
