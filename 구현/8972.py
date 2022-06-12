# https://www.acmicpc.net/problem/8972
import sys
from collections import deque

dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(str, input().rstrip())))
q = deque()
mx, my = 0, 0
ddd = list(map(int, input().rstrip()))


def me_bfs(xx):
    global mx, my
    x, y = mx, my
    arr[x][y] = 0
    nx = x + dx[xx]
    ny = y + dy[xx]
    if arr[nx][ny] > 0:
        return False
    arr[nx][ny] = -1
    mx, my = nx, ny
    return True


def robot_bfs():
    global mx, my
    len_q = len(q)
    for kk in range(len_q):
        x, y = q.popleft()
        temp = sys.maxsize
        d = 0
        for _ in range(9):
            nx = x + dx[_]
            ny = y + dy[_]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if temp > abs(nx - mx) + abs(ny - my):
                temp = abs(nx - mx) + abs(ny - my)
                d = _
        nx = x + dx[d]
        ny = y + dy[d]
        if arr[nx][ny] == -1:
            return False
        arr[nx][ny] += 1
        arr[x][y] -= 1
        q.append([nx, ny])
    new_robot()
    return True


def new_robot():
    len_q = len(q)
    dq = []
    for kk in range(len_q):
        x, y = q.popleft()
        if arr[x][y] > 1:
            dq.append((x, y))
        else:
            q.append([x, y])
    for i, j in dq:
        arr[i][j] = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == ".":
            arr[i][j] = 0
        elif arr[i][j] == "R":
            q.append([i, j])
            arr[i][j] = 1
        elif arr[i][j] == "I":
            mx, my = i, j
            arr[i][j] = -1


def result():
    for i in range(len(ddd)):
        if ddd[i] != 5:
            if not me_bfs(ddd[i] - 1):
                print("kraj %d" % (i + 1))
                return
        if not robot_bfs():
            print("kraj %d" % (i + 1))
            return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(".", end='')
            elif arr[i][j] == 1:
                print("R", end='')
            elif arr[i][j] == -1:
                print("I", end='')
        print()


result()
