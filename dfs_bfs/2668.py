# https://www.acmicpc.net/problem/2668
import sys

input = sys.stdin.readline


def dfs(v, i):
    visited[v] = True
    for n_i in arr[v]:
        if not visited[n_i]:
            dfs(n_i, i)
        elif visited[n_i] and n_i == i:
            result.append(n_i)


result = []
n = int(input())
arr = [[] for i in range(n + 1)]
for i in range(n):
    arr[i + 1].append(int(input()))

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)
print(len(result))
for i in result:
    print(i)
