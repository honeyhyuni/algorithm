# https://www.acmicpc.net/problem/12851
import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append((n, 0))
min_v = sys.maxsize
result = 0
while q:
    x, c = q.popleft()
    visited[x] = 1
    if x == k:
        min_v = min(min_v, c)
        if min_v == c:
            result += 1
    if 0 <= x - 1 and visited[x-1] == 0:
        q.append((x-1, c+1))
    if x + 1 < len(visited) and visited[x+1] == 0:
        q.append((x+1, c+1))
    if x * 2 < len(visited) and visited[x*2] == 0:
        q.append((x*2, c+1))

print(min_v)
print(result)

