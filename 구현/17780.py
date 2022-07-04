# https://www.acmicpc.net/problem/17780
import sys

input = sys.stdin.readline
from collections import deque

dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
board = [[deque() for i in range(n)] for i in range(n)]

horse = [[]]
for i in range(1, k + 1):
    a, b, c = map(int, input().split())
    horse.append([a - 1, b - 1, c])
    board[a - 1][b - 1].append(i)


def change_xy(d):
    if d == 2 or d == 4:
        return d - 1
    else:
        return d + 1


def move_horse(v):
    x, y, d = horse[v]
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 2:
        nd = change_xy(d)
        nx = x + dx[nd]
        ny = y + dy[nd]
        if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] == 2:
            horse[v] = [x, y, nd]
            return
        horse[v][2] = nd
    temp = []
    while True:
        vv = board[x][y].popleft()
        temp.append(vv)
        if vv == v:
            break
    if arr[nx][ny] == 0:
        board[nx][ny].extendleft(temp[::-1])
    else:
        board[nx][ny].extendleft(temp)

    for i in temp:
        horse[i][0], horse[i][1] = nx, ny
        if len(board[nx][ny]) >= 4:
            return True
    return False


bol = True
for cnt in range(1, 1001):
    for v in range(1, k + 1):
        x, y, d = horse[v]
        if board[x][y][-1] == v:
            if move_horse(v):
                bol = False
                print(cnt)
                break
    if not bol:
        break
else:
    print(-1)
