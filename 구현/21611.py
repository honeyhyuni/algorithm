# https://www.acmicpc.net/problem/21611
import sys
from collections import deque

result = [0] * 4

input = sys.stdin.readline

idx = []

ice_dx, ice_dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

ice = []
for i in range(m):
    d, s = map(int, input().split())
    ice.append((d, s))


# 얼음 던지기
def throw_ice(d, s):
    x, y = n // 2, n // 2
    for _ in range(1, s + 1):
        nx = x + ice_dx[d] * _
        ny = y + ice_dy[d] * _
        arr[nx][ny] = 0


# 회전 하는 방향으로 인덱스 저장
def make_idx():
    q = deque()
    q.append((n // 2, n // 2, 0, 1, 1))
    while q:
        x, y, d, cnt, c = q.popleft()
        for _ in range(1, cnt + 1):
            nx = x + dx[d] * _
            ny = y + dy[d] * _
            if not (0 <= nx < n and 0 <= ny < n):
                return
            idx.append((nx, ny))
        if c == 1:
            c += 1
        else:
            c = 1
            cnt += 1
        q.append((nx, ny, (d + 1) % 4, cnt, c))


# 배열 정리
def move_arr():
    q = deque()
    for x, y in idx:
        if arr[x][y] != 0:
            q.append(arr[x][y])
    for x, y in idx:
        if q:
            arr[x][y] = q.popleft()
        else:
            arr[x][y] = 0


# 같은 숫자 4개이상 있을시 터트리고 크기, 숫자 순으로
# count_q 에 저장
def boom_arr():
    temp_q = deque()
    count_q = deque()
    bol = False
    for x, y in idx:
        if temp_q and temp_q[-1][-1] != arr[x][y]:
            if len(temp_q) < 4:
                count_q.append(len(temp_q))
                count_q.append(temp_q[-1][-1])
                temp_q.clear()
            else:
                bol = True
                while temp_q:
                    xx, yy, v = temp_q.popleft()
                    result[v] += 1
                    arr[xx][yy] = 0
        temp_q.append((x, y, arr[x][y]))
    return bol, count_q


# 크기, 숫자 순으로 다시 배열에 정리
def fill(co):
    for x, y in idx:
        if co:
            arr[x][y] = co.popleft()
        else:
            arr[x][y] = 0


make_idx()
for i in range(m):
    throw_ice(ice[i][0], ice[i][1])
    move_arr()
    while True:
        bol, co = boom_arr()
        if not bol:
            break
        move_arr()
    fill(co)
ans = 0
for i in range(1, 4):
    ans += result[i] * i
print(ans)
