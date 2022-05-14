# https://www.acmicpc.net/problem/19236
import copy
import sys

input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

arr = [[] for i in range(4)]

for i in range(4):
    temp = list(map(int, input().split()))
    for _ in range(0, len(temp), 2):
        # 물고기 크기, 방향
        arr[i].append([temp[_], temp[_ + 1] - 1])
        
result = 0


def dfs(sh_x, sh_y, score, arr):
    # sh_x, sh_y = 상어의 현재 위치
    global result
    score += arr[sh_x][sh_y][0]
    result = max(result, score)
    # 물고기 먹힘
    arr[sh_x][sh_y][0] = 0
    
    # 물고기는 크기순으로 움직임
    for num in range(1, 17):
        bol = False
        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == num:
                    x, y, d = i, j, arr[i][j][1]
                    bol = True
                    break
            if bol:
                break
        if not bol:
            continue
        for _ in range(8):
            nd = (d + _) % 8
            nx = x + dx[nd]
            ny = y + dy[nd]
            if (0 <= nx < 4 and 0 <= ny < 4) and not (nx == sh_x and ny == sh_y):
                # 방향의 정보를 최신화 한뒤 위치 바꿈
                arr[x][y][1] = nd
                arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                break
    sh_d = arr[sh_x][sh_y][1]
    # 상어의 움직임은 한방향으로 이동하며 빈곳으론 이동불가능
    for i in range(1, 5):
        sh_nx = sh_x + dx[sh_d] * i
        sh_ny = sh_y + dy[sh_d] * i
        if 0 <= sh_nx < 4 and 0 <= sh_ny < 4 and arr[sh_nx][sh_ny][0] > 0:
            dfs(sh_nx, sh_ny, score, copy.deepcopy(arr))


dfs(0, 0, 0, arr)
print(result)
