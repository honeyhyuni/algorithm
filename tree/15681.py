# https://www.acmicpc.net/problem/15681
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(node):
    visited[node] = True
    for i in arr[node]:
        if not visited[i]:
            dfs(i)
            result[node] += result[i]


n, r, q = map(int, input().split())
arr = [[] for i in range(n+1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (n+1)
result = [1] * (n+1)
dfs(r)

for i in range(q):
    print(result[int(input())])
