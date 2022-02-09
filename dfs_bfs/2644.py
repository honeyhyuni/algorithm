# https://www.acmicpc.net/problem/2644
import sys

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())

visited = [0] * (n + 1)
arr = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(start):
    for k in arr[start]:
        if visited[k] == 0:
            visited[k] = visited[start] + 1
            dfs(k)


dfs(a)
print(visited[b] if visited[b] > 0 else -1)
