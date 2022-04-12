import sys
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if x == E:
            return visited[x]
        for _ in arr[x]:
            if visited[_] == -1:
                visited[_] = visited[x] + 1
                q.append(_)
        for _ in [x + 1, x - 1]:
            if 0 <= _ < n + 1 and visited[_] == -1:
                visited[_] = visited[x] + 1
                q.append(_)


input = sys.stdin.readline
n, m = map(int, input().split())
S, E = map(int, input().split())
arr = [[] for i in range(n + 1)]
visited = [-1] * (n + 1)
visited[S] = 0
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
print(bfs(S))
