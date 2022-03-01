# https://www.acmicpc.net/problem/11725
import sys

input = sys.stdin.readline
from collections import deque


def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        x = q.popleft()
        for _ in arr[x]:
            if not visited[_]:
                visited[_] = True
                result[_] = x
                q.append(_)


n = int(input())
arr = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
for i in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

result = [0] * (n + 1)
bfs()
print("\n".join(map(str, result[2:])))
