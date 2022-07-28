# https://www.acmicpc.net/problem/15683
import copy
import sys


def check(x, y, d, temp):
    for _ in d:
        nx = x
        ny = y
        while True:
            nx += dx[_]
            ny += dy[_]
            if not (0 <= nx < n and 0 <= ny < m) or temp[nx][ny] == 6:
                break
            if temp[nx][ny] == 0:
                temp[nx][ny] = "#"


def dfs(arr, cnt):
    global result
    temp = copy.deepcopy(arr)
    if cnt == cctv:
        c = 0
        for i in temp:
            c += i.count(0)
        result = min(result, c)
        return
    x, y, cc = q[cnt]
    for _ in dd[cc]:
        check(x, y, _, temp)
        dfs(temp, cnt + 1)
        temp = copy.deepcopy(arr)


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]
dd = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 3], [3, 1], [1, 2], [2, 0]],
      [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]], [[0, 1, 2, 3]]]
for i in range(n):
    arr.append(list(map(int, input().split())))

q = []
cctv = 0
for i in range(n):
    for j in range(m):
        if 0 < arr[i][j] < 6:
            cctv += 1
            q.append([i, j, arr[i][j]])

result = sys.maxsize
dfs(arr, 0)
print(result)
