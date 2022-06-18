# https://www.acmicpc.net/problem/13549
n, k = map(int, input().split())
from collections import deque
visited = [0] * 100001
q = deque()
cnt = 0
q.append((n, cnt))
while q:
    x, c = q.popleft()
    if x == k:
        print(c)
        break
    visited[x] = 1
    if 0 <= x-1 and visited[x-1] == 0:
        q.append((x-1, c+1))
    if x + 1 < len(visited) and visited[x+1] == 0:
        q.append((x+1, c+1))
    if x * 2 < len(visited) and visited[x*2] == 0:
        q.appendleft((x*2, c))