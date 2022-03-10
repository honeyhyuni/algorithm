# https://www.acmicpc.net/problem/24480
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(v):
    global cnt
    visited[v] = cnt
    for _ in arr[v]:
        if visited[_] == 0:
            cnt += 1
            dfs(_)


n, m, r = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [0] * (n + 1)
cnt = 1
for i in arr:
    i.sort(reverse=True)
dfs(r)
print("\n".join(map(str, visited[1:])))