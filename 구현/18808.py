# https://www.acmicpc.net/problem/18808
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
sticker = []
arr = [[0] * m for i in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(a)]
    sticker.append(temp)


def stech(a, x, y):
    global result
    idx = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if arr[i + x][j + y] == 1 and a[i][j] == 1:
                return False
            if a[i][j] == 1:
                idx.append((i + x, j + y))
    for i, j in idx:
        arr[i][j] = 1
    result += len(idx)
    return True


def check(a):
    for i in range(n - len(a) + 1):
        for j in range(m - len(a[0]) + 1):
            if stech(a, i, j):
                return True
    return False


result = 0
for i in sticker:
    a = i
    if check(a):
        continue
    for _ in range(3):
        a = list(map(list, zip(*a[::-1])))
        if check(a):
            break
print(result)