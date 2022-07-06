# https://www.acmicpc.net/problem/11437
import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

# 각 노드별 루트 까지 깊이 설정
def dfs(node, cnt):
    visited[node] = True
    depth[node] = cnt
    for nn in arr[node]:
        if not visited[nn]:
            parent[nn] = node
            dfs(nn, cnt + 1)

# 최소 공통 조상 찾기
def lca(x, y):
    if depth[x] > depth[y]:
        y, x = x, y
    while True:
        if depth[x] == depth[y]:
            break
        y = parent[y]
    for i in range(depth[x]):
        if x == y:
            return x
        x = parent[x]
        y = parent[y]
    return x


n = int(input())
parent = [i for i in range(n + 1)]
visited = [False] * (n + 1)
depth = [0] * (n + 1)
arr = [[] for i in range(n + 1)]

for i in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

dfs(1, 0)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))
