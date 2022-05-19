# https://www.acmicpc.net/problem/19237
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
arr = [list(map(int, input().split())) for i in range(n)]
start = [0] + list(map(int, input().split()))
ddd = [[]]
for i in range(m):
    temp = [list(map(int, input().split())) for _ in range(4)]
    ddd.append(temp)
shark = [[] for i in range(m + 1)]  # 상어 좌표, 방향 배열

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            shark[arr[i][j]] = [i, j, start[arr[i][j]]]
            arr[i][j] = [arr[i][j], k]
        else:
            arr[i][j] = [0, 0]


# 냄새 1씩 감소한후 가장 최신 상어 좌표 최신화
def smell_down():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == [0, 0]:
                continue
            arr[i][j][1] -= 1
            if arr[i][j][1] == 0:
                arr[i][j] = [0, 0]
    for i in range(m, 0, -1):  # 크기가 작은 상어가 내쫓음
        if shark[i]:
            x, y, d = shark[i]
            if arr[x][y] == [0, 0]:
                arr[x][y] = [i, k]
                continue
            if arr[x][y][0] > i:
                die_shark.add(arr[x][y][0])
                shark[arr[x][y][0]] = []
                arr[x][y] = [i, k]
            else:
                arr[x][y] = [i, k]


die_shark = set()
for cnt in range(1, 1001):
    for i in range(1, m + 1):
        if shark[i]:
            x, y, d = shark[i]
            temp = []
            for _ in range(4):
                nd = ddd[i][d - 1][_]
                nx = x + dx[nd]
                ny = y + dy[nd]
                if 0 <= nx < n and 0 <= ny < n:
                    if arr[nx][ny] == [0, 0]:
                        shark[i] = [nx, ny, nd]
                        break
                    elif arr[nx][ny][0] == i:
                        temp.append([nx, ny, nd])
            else:
                shark[i] = temp[0]
    smell_down()
    if len(die_shark) == m - 1:
        print(cnt)
        break
else:
    print(-1)
