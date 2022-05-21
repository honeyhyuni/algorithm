# https://www.acmicpc.net/problem/17143
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [[0] * m for i in range(n)]
shark = {}
temp = []
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
for i in range(k):
    r, c, s, d, z = map(int, input().split())
    arr[r - 1][c - 1] = z
    temp.append([z, r - 1, c - 1, s, d])

for z, r, c, s, d in sorted(temp):
    shark[z] = [r, c, s, d]


# 상어 위치 재정의
def shark_xy():
    for i, j in shark.items():
        if not j:
            continue
        x, y, s, d = j
        for _ in range(s):
            nx = x + dx[d - 1]
            ny = y + dy[d - 1]
            if 0 <= nx < n and 0 <= ny < m:
                x, y = nx, ny
            else:
                if d == 1:
                    d = 2
                elif d == 2:
                    d = 1
                elif d == 3:
                    d = 4
                else:
                    d = 3
                x, y = x + dx[d - 1], y + dy[d - 1]
        shark[i] = [x, y, s, d]


# 상어 움직임, 만약 여러마리가 한칸에 있다면 큰 상어가 작은상어를 먹음
def move_shark():
    new_arr = [[0] * m for i in range(n)]
    for i, j in shark.items():
        if shark[i]:
            x, y, s, d = j
            if new_arr[x][y] == 0:
                new_arr[x][y] = i
                continue
            elif new_arr[x][y] < i:
                shark[new_arr[x][y]] = []
                new_arr[x][y] = i
    return new_arr


result = 0
# 낚시자는 한칸씩 이동하며 땅에서 가장 가까운(y 좌표가 0에 가까운) 상어를 잡음
for i in range(m):
    for j in range(n):
        if arr[j][i] != 0:
            result += arr[j][i]
            shark[arr[j][i]] = []
            arr[j][i] = 0
            break
    shark_xy()
    arr = move_shark()

print(result)
