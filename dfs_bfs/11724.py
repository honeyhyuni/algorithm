# https://www.acmicpc.net/problem/11724
import sys
from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0


def bfs(arr, v, visited):
    visited[v] = True
    q = deque([v])
    while q:
        x = q.popleft()
        for _ in arr[x]:
            if not visited[_]:
                visited[_] = True
                q.append(_)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        bfs(arr, i, visited)

print(cnt)
