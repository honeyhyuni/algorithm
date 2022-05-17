# https://www.acmicpc.net/problem/13023
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

result = False


def dfs(v, cnt):
    global result
    if cnt == 4:
        result = True
        return
    for i in arr[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False
    return


visited = [False] * n
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0 if not result else 1)
