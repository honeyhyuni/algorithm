import sys
from collections import deque
# bfs_dfs 이론문제

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if not visited[i] and arr[x][i] == 1:
                visited[i] = True
                q.append(i)


def dfs(v):
    visited2[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited2[i] and arr[v][i] == 1:
            dfs(i)


n, m, v = map(int, sys.stdin.readline().split())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1) # bfs 방문처리 배열
visited2 = [False] * (n + 1) # dfs 방문처리 배열

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a][b] = arr[b][a] = 1
dfs(v)
print()
bfs(v)
