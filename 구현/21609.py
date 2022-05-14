# https://www.acmicpc.net/problem/21609
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 중력
def gravity():
    temp_q = deque()
    for j in range(n):
        black = 0
        for i in range(n):
            if arr[i][j] != -2 and arr[i][j] != -1:
                temp_q.appendleft(arr[i][j])
            if arr[i][j] == -1:
                block(i, j, black, temp_q)
                black = i + 1
        block(i + 1, j, black, temp_q)


def block(x, y, black, temp_q):
    for i in range(x - 1, black - 1, -1):
        if temp_q:
            arr[i][y] = temp_q.popleft()
        else:
            arr[i][y] = -2


while True:
    land = []
    visited = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                color = arr[i][j]
                rainbow, temp = [], [[i, j]]
                while q:
                    x, y = q.popleft()
                    for _ in range(4):
                        nx = x + dx[_]
                        ny = y + dy[_]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if arr[nx][ny] == 0 or arr[nx][ny] == color:
                                q.append((nx, ny))
                                visited[nx][ny] = True
                                temp.append([nx, ny])
                            if arr[nx][ny] == 0:
                                rainbow.append([nx, ny])
                if len(temp) >= 2:
                    land.append([len(temp), len(rainbow), temp])  # 크기, 무지개 블록, x, y 좌표순
                while rainbow:
                    xx, yy = rainbow.pop()
                    visited[xx][yy] = False
    if not land:
        break
    land.sort(reverse=True) # 여러개 있다면 역순
    result += land[0][0] ** 2
    for a, b in land[0][2]:
        arr[a][b] = -2

    gravity()
    arr = list(map(list, zip(*arr)))[::-1] # 반시계방향으로 90도 회전
    gravity()

print(result)