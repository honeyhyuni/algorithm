# https://www.acmicpc.net/problem/3197
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

water = deque()
swan = deque()


def move_water():
    len_ = len(water)
    for i in range(len_):
        x, y = water.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == "X":
                arr[nx][ny] = '.'
                water.append((nx, ny))


def move_swan():
    temp = deque()
    while swan:
        x, y = swan.popleft()
        if x == end_x and y == end_y:
            return True, None
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == "X":
                    temp.append((nx, ny))
                else:
                    swan.append((nx, ny))
                visited[nx][ny] = True
    return False, temp


for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            water.append((i, j))
        elif arr[i][j] == 'L':
            arr[i][j] = '.'
            water.append((i, j))
            swan.append((i, j))
cnt = -1
end_x, end_y = swan.pop()
visited = [[False] * m for i in range(n)]
visited[swan[0][0]][swan[0][1]] = True
while True:
    cnt += 1
    bol, swan = move_swan()
    if bol:
        break
    move_water()

print(cnt)
