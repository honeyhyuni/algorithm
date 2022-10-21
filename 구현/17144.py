# https://www.acmicpc.net/problem/17144
import copy
import sys

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


def bfs():
    visited = [[0] * m for i in range(n)]
    visited[a1][a2], visited[b1][b2] = -1, -1
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt = 0
                for _ in range(4):
                    nx = i + dx[_]
                    ny = j + dy[_]
                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != -1:
                        visited[nx][ny] += arr[i][j] // 5
                        cnt += 1
                visited[i][j] += arr[i][j] - (arr[i][j] // 5 * cnt)
    return visited


def rotate(x, y, d):
    temp = copy.deepcopy(arr)
    cx, cy = x, y - 1
    arr[x][y] = 0
    for i in range(4):
        while True:
            nx = x + dx[d[i]]
            ny = y + dy[d[i]]
            if nx == cx and ny == cy:
                return
            if 0 <= nx < n and 0 <= ny < m:
                arr[nx][ny] = temp[x][y]
            else:
                break
            x, y = nx, ny


input = sys.stdin.readline
n, m, T = map(int, input().split())
arr = []
for i in range(n):
    arr.append((list(map(int, input().split()))))

air_m = []
for i in range(n):
    if arr[i][0] == -1:
        air_m.append((i, 0))
        air_m.append((i + 1, 0))
        break

a1, a2 = air_m[0][0], air_m[0][1]
b1, b2 = air_m[1][0], air_m[1][1]

for t in range(T):
    arr = bfs()
    rotate(a1, a2 + 1, [0, 1, 2, 3])
    rotate(b1, b2 + 1, [0, 3, 2, 1])

result = 0
for a in arr:
    result += sum(a)
print(result + 2)
