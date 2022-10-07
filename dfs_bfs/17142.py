# https://www.acmicpc.net/problem/17142
import sys
from collections import deque
from itertools import combinations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(dp):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    for i, j in dp:
        q.append((i, j))
        visited[i][j] = 0
    cnt = 0
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                if arr[nx][ny] == 2 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 1 and visited[i][j] == -1:
                return sys.maxsize
            if arr[i][j] == 0 and visited[i][j] != -1:
                cnt = max(cnt, visited[i][j])
    return cnt


input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

result = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            result.append((i, j))
result_arr = list(combinations(result, m))

ans = sys.maxsize


for i in result_arr:
    ans = min(ans, bfs(i))
if ans >= sys.maxsize:
    print(-1)
else:
    print(ans)
