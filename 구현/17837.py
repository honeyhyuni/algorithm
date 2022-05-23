# https://www.acmicpc.net/problem/17837
from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
n, k = map(int, input().split())
locate = [[]]
board = [list(map(int, input().split())) for i in range(n)]
arr = [[deque() for i in range(n)] for i in range(n)]
for i in range(1, k + 1):
    x, y, d = map(int, input().split())
    arr[x - 1][y - 1].append(i)
    locate.append([x - 1, y - 1, d])


def move_horse(idx):
    x, y, d = locate[idx]
    nx = x + dx[d]
    ny = y + dy[d]
    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
        if d == 2 or d == 4:
            d -= 1
        else:
            d += 1
        nx = x + dx[d]
        ny = y + dy[d]
        locate[idx] = [x, y, d]
        if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
            return False
    temp = []
    while True:
        v = arr[x][y].popleft()
        temp.append(v)
        if v == idx:
            break
    if board[nx][ny] == 0:
        arr[nx][ny].extendleft(temp[::-1])
    else:
        arr[nx][ny].extendleft(temp)
    if len(arr[nx][ny]) >= 4:
        return True
    for i in temp:
        locate[i][0], locate[i][1] = nx, ny


for cnt in range(1, 1001):
    for idx in range(1, k + 1):
        if move_horse(idx):
            print(cnt)
            sys.exit()


print(-1)
