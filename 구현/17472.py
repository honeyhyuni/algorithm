# https://www.acmicpc.net/problem/17472
from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for i in range(n)]
cnt = 1
# 각섬의 숫자의 인덱스에 [x, y] 좌표를 저장하기 위한 deque 베열
# 섬은 최대 6개
land = [deque() for i in range(7)]

# 각 섬의 숫자를 정해줌
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append([i, j])
            visited[i][j] = True
            arr[i][j] = cnt
            land[cnt].append([i, j])
            while q:
                x, y = q.popleft()
                for _ in range(4):
                    nx = x + dx[_]
                    ny = y + dy[_]
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] != 0:
                        visited[nx][ny] = True
                        arr[nx][ny] = cnt
                        q.append([nx, ny])
                        land[cnt].append([nx, ny])
            cnt += 1

node = []
for c in range(1, cnt):
    visited = [[0] * m for i in range(n)]
    while land[c]:
        x, y = land[c].popleft()
        for _ in range(4):
            xx, yy = x, y
            while True:  # 다리는 일직선이어야 함
                nx = xx + dx[_]
                ny = yy + dy[_]
                if 0 <= nx < n and 0 <= ny < m:
                    if arr[nx][ny] == c:  # c -> 현재 land 인덱스 즉 섬의 숫자를 의미 하므로 같은 숫자를 만날경우
                        break
                    if arr[nx][ny] == 0:
                        visited[nx][ny] = visited[xx][yy] + 1
                    else:
                        if visited[xx][yy] > 1:  # 다리는 두칸 이상
                            if (visited[xx][yy], c, arr[nx][ny]) not in node and (
                                    visited[xx][yy], arr[nx][ny], c) not in node:
                                node.append((visited[xx][yy], c, arr[nx][ny]))
                        break
                else:
                    break
                xx = nx
                yy = ny
parent = [i for i in range(cnt)]


# 크루스칼
def find_parent(var):
    if var != parent[var]:
        parent[var] = find_parent(parent[var])
    return parent[var]


result, check = 0, 0
cnt -= 1
node.sort()

for c, a, b in node:
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        result += c
        check += 1

        if check == cnt - 1:
            print(result)
            break
else:
    print(-1)
