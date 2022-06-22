# https://www.acmicpc.net/problem/1240
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(n - 1):
    x, y, z = map(int, input().split())
    arr[x].append([y, z])
    arr[y].append([x, z])


def dfs(v):
    global cnt
    for i, j in arr[v]:
        if i == end:
            cnt += j
            return True
        if not visited[i]:
            visited[i] = True
            if dfs(i):
                cnt += j
                return True
    return False


for i in range(m):
    start, end = map(int, input().split())
    cnt = 0
    visited = [False] * (n+1)
    visited[start] = True
    dfs(start)
    print(cnt)
