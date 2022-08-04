# https://www.acmicpc.net/problem/2234
import sys
input = sys.stdin.readline
from collections import deque

# x, y, bit
dd = [(0, -1, 1), (-1, 0, 2), (0, 1, 4), (1, 0, 8)]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
visited = [[False] * m for i in range(n)]

wall = deque()


# bfs 돌면서 연결되어있는 방들은 연결시켜주고
# 벽이 있다면 wall deque 에 넣어준다
def bfs(i, j, temp):
    cnt = 1
    q = deque()
    q.append((i, j))
    temp += 1
    visited[i][j] = temp
    while q:
        x, y = q.popleft()
        for _ in range(4):
            dx, dy, v = dd[_]
            nx = x + dx
            ny = y + dy
            if not arr[x][y] & v:
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = temp
                    cnt += 1
            else:
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    wall.append((x, y, nx, ny))
    return cnt


total, max_arr, break_wall = 0, [0], 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            max_arr.append(bfs(i, j, total))
            total += 1

# 벽을 하나 씩 확인해주면서 벽 을 중심으로
# visited 배열에 다른수가 들어있다면 그 크기만큼 더해준다.
while wall:
    x, y, nx, ny = wall.popleft()
    o, t = visited[x][y], visited[nx][ny]
    if o != t:
        break_wall = max(break_wall, max_arr[o] + max_arr[t])

print(total)
print(max(max_arr))
print(break_wall)