# https://www.acmicpc.net/problem/1726
import sys

input = sys.stdin.readline
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dddd(pre, post):
    if pre == post:
        return 0
    elif (pre == 0 and post == 1) or (pre == 1 and post == 0):
        return 2
    elif (pre == 2 and post == 3) or (pre == 3 and post == 2):
        return 2
    else:
        return 1


def bfs():
    visited = set()
    while q:
        x, y, d, cnt = q.popleft()
        if x == enx - 1 and y == eny - 1:
            return cnt + dddd(d, ed - 1)
        for i in range(1, 4):
            nx = x + dx[d] * i
            ny = y + dy[d] * i
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                if (nx, ny, d, cnt + 1) not in visited:
                    q.append([nx, ny, d, cnt + 1])
                    visited.add((nx, ny, d, cnt + 1))
            else:
                break
        for _ in range(4):
            if d != _ and (x, y, _, cnt + 1) not in visited:  # 전이랑 방향이 다를시 회전수만큼 더해주고 방향값 전환한후 q에 삽입
                q.append([x, y, _, cnt + dddd(d, _)])
                visited.add((x, y, _, cnt + dddd(d, _)))


n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
stx, sty, sd = map(int, input().split())
enx, eny, ed = map(int, input().split())
q = deque()
q.append([stx - 1, sty - 1, sd - 1, 0])

print(bfs())
