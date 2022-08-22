# https://www.acmicpc.net/problem/13016
import sys

input = sys.stdin.readline


def dfs(v, c):
    visited[v] = c
    result[v] = max(result[v], c)
    for i, j in tree[v]:
        if visited[i] == -1:
            dfs(i, c + j)


n = int(input())
tree = [[] for i in range(n + 1)]
for i in range(n - 1):
    x, y, z = map(int, input().split())
    tree[x].append((y, z))
    tree[y].append((x, z))

node, result = [], [0] * (n+1)
t = 1

while True:
    visited = [-1] * (n + 1)
    dfs(t, 0)
    max_v = visited.index(max(visited))
    if node and max_v == node[-1][0]:
        break
    node.append((t, max_v))
    t = max_v

print("\n".join(map(str, result[1:])))