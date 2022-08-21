# https://www.acmicpc.net/problem/23289
import copy
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
wall = [[[] for i in range(m)] for i in range(n)]
temperature = [[0] * m for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(int(input())):
    x, y, z = map(int, input().split())
    wall[x - 1][y - 1].append(z)

check_list, machine, idx = [], [], []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            if arr[i][j] == 5:
                check_list.append((i, j))
            else:
                machine.append((i, j, arr[i][j]))


# 온풍기에서 나오는 바람의 인덱스와 그 인덱스에 더해질 값을 idx 배열에 저장해준다.
def wind_check():
    q = deque()
    for x, y, d in machine:
        visited = [[False] * m for i in range(n)]
        if d == 1:
            idx.append((x, y + 1, 5))
            q.append((x, y + 1, 5))
            while q:
                x, y, cnt = q.popleft()
                for t, nx, ny in [(1, x - 1, y + 1), (2, x, y + 1), (3, x + 1, y + 1)]:
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if t == 1:
                            if 0 in wall[x][y] or 1 in wall[nx][y]: continue
                        elif t == 2:
                            if 1 in wall[x][y]: continue
                        elif t == 3:
                            if 0 in wall[nx][y] or 1 in wall[nx][y]: continue
                        visited[nx][ny] = True
                        if cnt - 1 != 0:
                            q.append((nx, ny, cnt - 1))
                            idx.append((nx, ny, cnt - 1))
        elif d == 2:
            idx.append((x, y - 1, 5))
            q.append((x, y - 1, 5))
            while q:
                x, y, cnt = q.popleft()
                for t, nx, ny in [(1, x - 1, y - 1), (2, x, y - 1), (3, x + 1, y - 1)]:
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if t == 1:
                            if 0 in wall[x][y] or 1 in wall[nx][ny]: continue
                        elif t == 2:
                            if 1 in wall[x][ny]: continue
                        elif t == 3:
                            if 0 in wall[nx][y] or 1 in wall[nx][ny]: continue
                        visited[nx][ny] = True
                        if cnt - 1 != 0:
                            q.append((nx, ny, cnt - 1))
                            idx.append((nx, ny, cnt - 1))
        elif d == 3:
            idx.append((x - 1, y, 5))
            q.append((x - 1, y, 5))
            while q:
                x, y, cnt = q.popleft()
                for t, nx, ny in [(1, x - 1, y + 1), (2, x - 1, y), (3, x - 1, y - 1)]:
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if t == 1:
                            if 0 in wall[x][ny] or 1 in wall[x][y]: continue
                        elif t == 2:
                            if 0 in wall[x][y]: continue
                        elif t == 3:
                            if 0 in wall[x][ny] or 1 in wall[x][ny]: continue
                        visited[nx][ny] = True
                        if cnt - 1 != 0:
                            q.append((nx, ny, cnt - 1))
                            idx.append((nx, ny, cnt - 1))
        else:
            idx.append((x + 1, y, 5))
            q.append((x + 1, y, 5))
            while q:
                x, y, cnt = q.popleft()
                for t, nx, ny in [(1, x + 1, y + 1), (2, x + 1, y), (3, x + 1, y - 1)]:
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        if t == 1:
                            if 0 in wall[nx][ny] or 1 in wall[x][y]: continue
                        elif t == 2:
                            if 0 in wall[nx][y]: continue
                        elif t == 3:
                            if 0 in wall[nx][ny] or 1 in wall[x][ny]: continue
                        visited[nx][ny] = True
                        if cnt - 1 != 0:
                            q.append((nx, ny, cnt - 1))
                            idx.append((nx, ny, cnt - 1))


# 온도 조절
def control_temperature(temp):
    for x in range(n):
        for y in range(m):
            for _ in range(4):
                nx = x + dx[_]
                ny = y + dy[_]
                if 0 <= nx < n and 0 <= ny < m:
                    if _ == 0 and 0 in wall[x][y]: continue
                    if _ == 1 and 0 in wall[nx][ny]: continue
                    if _ == 2 and 1 in wall[nx][ny]: continue
                    if _ == 3 and 1 in wall[x][y]: continue
                    if temperature[nx][ny] < temperature[x][y]:
                        t = (temperature[x][y] - temperature[nx][ny]) // 4
                        temp[nx][ny] += t
                        temp[x][y] -= t
    return temp


# 가장자리 온도 1 씩 감소
def edge_minus():
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if temperature[i][j] >= 1:
                    temperature[i][j] -= 1


# 조사해야할 칸 온도 조사
def check_temperature():
    for i, j in check_list:
        if temperature[i][j] < k:
            return False
    return True


wind_check()
cnt = 0
while True:
    for a, b, c in idx:
        temperature[a][b] += c
    temperature = control_temperature(copy.deepcopy(temperature))
    edge_minus()
    cnt += 1
    if cnt == 101 or check_temperature():
        break
print(cnt)
