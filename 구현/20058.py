import copy
import sys
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
input = sys.stdin.readline
n, qq = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(2 ** n)]
L = list(map(int, input().split()))


# 회전
def tornado(l):
    plus_ = 2 ** l
    for i in range(0, 2 ** n, 2 ** l):
        for j in range(0, 2 ** n, 2 ** l):
            temp = [i[j: j + plus_] for i in arr[i:i + plus_]]
            temp = list(map(list, zip(*temp[::-1])))
            for x in range(plus_):
                for y in range(plus_):
                    arr[x + i][y + j] = temp[x][y]


# 얼음 녹음
def ice_down():
    ice_check = copy.deepcopy(arr)
    for i in range(2 ** n):
        for j in range(2 ** n):
            cnt = 0
            if arr[i][j] == 0:
                continue
            for xx, yy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nx = i + xx
                ny = j + yy
                if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                    if arr[nx][ny] > 0:
                        cnt += 1
            if cnt < 3:
                ice_check[i][j] -= 1
            if ice_check[i][j] < 0:
                ice_check[i][j] = 0
    return ice_check


# 가장 큰지형 체크
def check(i, j):
    visited[i][j] = True
    q = deque()
    q.append([i, j])
    cnt = 1
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if (0 <= nx < (2 ** n)) and (0 <= ny < (2 ** n)):
                if arr[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1
    return cnt


for l in L:
    if l > 0:
        tornado(l)
    arr = ice_down()

max_v = 0
visited = [[False] * 2 ** n for i in range(2 ** n)]
for i in range(2 ** n):
    for j in range(2 ** n):
        if arr[i][j] != 0 and not visited[i][j]:
            max_v = max(max_v, check(i, j))

print(sum(map(sum, arr)))
print(max_v)
