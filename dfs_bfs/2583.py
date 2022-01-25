# https://www.acmicpc.net/problem/2583
import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    arr[i][j] = 1
    q = deque()
    q.append((i, j))
    cnt_ = 1
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1 #방문 처리
                    q.append((nx, ny))
                    cnt_ += 1
    return cnt_


n, m, k = map(int, input().split())
arr = [[0] * m for i in range(n)] # 가로 세로 크기만큼 0 으로 초기화
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2): # 들어온 좌표안은 1 로 지정
        for j in range(y1, y2):
            arr[i][j] = 1
cnt = 0
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result.append(bfs(i, j))
            cnt += 1
result.sort()
print(cnt)
print(*result)
