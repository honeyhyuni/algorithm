# https://www.acmicpc.net/problem/17135
import copy
from itertools import combinations
import sys

input = sys.stdin.readline
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]

lst = [[n, i] for i in range(m)]
archer = list(combinations(lst, 3))  # 궁수 위치
ans = 0


def attack(arc, arr, cnt):
    global ans
    kill = []
    bol = False  # 적 확인 변수
    for a in arc:
        temp = []
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1:
                    bol = True
                    dd = abs(a[0] - i) + abs(a[1] - j)
                    if dd <= d:
                        temp.append((dd, j, i))
        if not bol:
            return False
        temp.sort()
        if temp:
            kill.append(temp[0])
    while kill:
        dd, y, x = kill.pop()
        if arr[x][y] == 1:
            cnt += 1
        arr[x][y] = 0
    arr.pop()  # 적 이동
    arr.insert(0, [0] * m)
    if not attack(arc, arr, cnt):
        ans = max(ans, cnt)
        return False


for i in archer:
    attack(i, copy.deepcopy(board), 0)

print(ans)
