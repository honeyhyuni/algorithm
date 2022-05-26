# https://www.acmicpc.net/problem/23290
import copy
import sys
from collections import deque
from itertools import product

input = sys.stdin.readline
m, s = map(int, input().split())
fish_dx, fish_dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
shark_dx, shark_dy = [-1, 0, 1, 0], [0, -1, 0, 1]
arr = [[list() for i in range(4)] for i in range(4)]
smell = [[0] * 4 for i in range(4)]
for i in range(m):
    x, y, d = map(int, input().split())
    arr[x - 1][y - 1].append(d - 1)  # 배열엔 방향만 저장
sx, sy = map(int, input().split())

# 상어 우선순위를 위한 배열
shark_xy = list(product(range(4), repeat=3))

shark_location = [[sx - 1, sy - 1]]


# 물고기 move
def move_fish():
    q = deque()
    for i in range(4):
        for j in range(4):
            if len(arr[i][j]) != 0:
                while arr[i][j]:
                    k = arr[i][j].pop()
                    q.append([i, j, k])
    while q:
        x, y, d = q.popleft()
        for _ in range(8):
            nd = (d - _) % 8  # 반시계 방향
            nx = x + fish_dx[nd]
            ny = y + fish_dy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not smell[nx][ny] and [nx, ny] != shark_location[0]:
                    arr[nx][ny].append(nd)
                    break
        else:
            arr[x][y].append(d)


# 상어 move
def move_shark():
    sorting_shark = []
    x, y = shark_location[0]
    for dd in range(len(shark_xy)):
        nx, ny = x, y
        cnt = 0
        tem = []
        for _ in range(3):
            nx += shark_dx[shark_xy[dd][_]]
            ny += shark_dy[shark_xy[dd][_]]
            if not (0 <= nx < 4 and 0 <= ny < 4):
                break
            if [nx, ny] not in tem:
                cnt += len(arr[nx][ny])
            tem.append([nx, ny])
        else:
            sorting_shark.append([cnt, dd, tem])
    sorting_shark.sort(key=lambda xxx: (-xxx[0], xxx[1]))  # 많이먹은순, 동률시 노트에 적힌 사전순
    x_y = sorting_shark[0][2]
    for _ in range(3):
        xx, yy = x_y[_]
        if len(arr[xx][yy]) > 0:
            smell[xx][yy] = 2
            arr[xx][yy].clear()
    shark_location[0] = x_y[2]


def smell_down():
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0:
                smell[i][j] -= 1


def copy_fish():
    for i in range(4):
        for j in range(4):
            arr[i][j] += temp[i][j]


for i in range(s):
    temp = copy.deepcopy(arr)
    move_fish()
    smell_down()
    move_shark()
    copy_fish()

result = 0
for i in range(4):
    for j in range(4):
        result += len(arr[i][j])
print(result)
