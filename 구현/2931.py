# https://www.acmicpc.net/problem/2931
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(str, input().rstrip())) for i in range(n)]
visited = [[False] * m for i in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dic = {"|": [0, 1], "-": [2, 3], "+": [0, 1, 2, 3], "1": [1, 3],
       "2": [0, 3], "3": [0, 2], "4": [1, 2], "Z": []}

q = deque()
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "M":
            q.append((i, j))
            visited[i][j] = True


def around():
    x, y = q.popleft()
    for j in range(4):
        nx = x + dx[j]
        ny = y + dy[j]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != "." and not visited[nx][ny]:
            q.append((nx, ny, dic[arr[nx][ny]]))
            visited[nx][ny] = True


def check():
    re_x, re_y = 0, 0
    while q:
        x, y, d = q.popleft()
        for _ in d:
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == ".":
                    re_x, re_y = nx, ny
                    if _ == 0 or _ == 2:
                        result.append(_ + 1)
                    else:
                        result.append(_ - 1)
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny, dic[arr[nx][ny]]))
    return re_x, re_y


around()
re_x, re_y = check()
q.append((re_x, re_y))
around()
check()

result.sort()
for i, j in dic.items():
    if j == result:
        print(re_x + 1, re_y + 1, i)
        break
