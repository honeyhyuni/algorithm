# https://www.acmicpc.net/problem/2606
import sys

n = int(input())
m = int(input())


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(graph, i, visited)


cnt = 0
land = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    land[a].append(b)
    land[b].append(a)

dfs(land, 1, visited)

print(cnt)
