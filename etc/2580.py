# https://www.acmicpc.net/problem/2580
import sys

input = sys.stdin.readline


def horizontal(x, target):
    for i in range(9):
        if arr[x][i] == target:
            return False
    return True


def vertical(y, target):
    for i in range(9):
        if arr[i][y] == target:
            return False
    return True


def division(x, y, target):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if arr[nx + i][ny + j] == target:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in arr:
            print(*i)
        sys.exit()
    for i in range(1, 10):
        x = blank[idx][0]
        y = blank[idx][1]

        if horizontal(x, i) and vertical(y, i) and division(x, y, i):
            arr[x][y] = i
            dfs(idx + 1)
            arr[x][y] = 0


arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))
blank = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            blank.append([i, j])

dfs(0)
