# https://www.acmicpc.net/problem/2573
import copy
import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    bing = copy.deepcopy(arr)
    while q:
        cnt = 0
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if arr[nx][ny] == 0:
                cnt += 1
        bing[x][y] = arr[x][y] - cnt  # 0의 개수만큼 빼주기
        if bing[x][y] <= 0:
            bing[x][y] = 0
    return bing


def check(i, j):
    dq = deque()
    dq.append((i, j))
    while dq:
        x, y = dq.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] != 0:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    return 1


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            q.append((i, j))
cnt = 1

while True:
    visited = [[False] * m for i in range(n)]
    arr = bfs()
    c = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                q.append((i, j))
            if arr[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                c += check(i, j)  # 빙산이 2개이상으로 분리되어있는지 확인
    if not q:  # 모두 녹았다면 종료
        print(0)
        break
    if c >= 2:  # 2개이상 분리되어있다면 종료
        print(cnt)
        break
    cnt += 1
