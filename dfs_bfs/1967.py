# https://www.acmicpc.net/problem/1967
import sys

input = sys.stdin.readline
from collections import deque

n = int(input())

arr = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n + 1)
    visited[start] = True
    distance = [0] * (n + 1)
    while q:
        node, cnt = q.popleft()
        distance[node] = cnt
        for i, j in arr[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt + j))
    return distance


root_n = bfs(1)
idx = root_n.index(max(root_n))
print(max(bfs(idx)))
