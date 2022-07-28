# https://www.acmicpc.net/problem/23288
import sys

input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
dice = [1, 2, 3, 4, 5, 6]
# 위 뒤 오 왼 앞 밑
result = 0


# 주사위 변환
def change(v):
    # 우
    if v == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    # 아래
    elif v == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    # 좌
    elif v == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    # 위
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]


# 갯수 * 보드값 return
def check(x, y, v):
    global result
    q = deque()
    q.append((x, y))
    cnt = 1
    visited = [[False] * m for i in range(n)]
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == v:
                visited[nx][ny] = True
                cnt += 1
                q.append((nx, ny))
    result += cnt * v


# 주사위 굴리고 주사위 맨밑과 보드값 차이 확인
def bfs(x, y, nd):
    nx = x + dx[nd]
    ny = y + dy[nd]
    if not (0 <= nx < n and 0 <= ny < m):
        if nd == 0 or nd == 1:
            nd += 2
        else:
            nd -= 2
        nx = x + dx[nd]
        ny = y + dy[nd]
    change(nd)
    check(nx, ny, arr[nx][ny])
    if dice[-1] > arr[nx][ny]:
        nd = (nd + 1) % 4
    elif dice[-1] < arr[nx][ny]:
        nd = (nd - 1) % 4
    return nx, ny, nd


x, y, d = 0, 0, 0
for c in range(k):
    x, y, d = bfs(x, y, d)
print(result)
