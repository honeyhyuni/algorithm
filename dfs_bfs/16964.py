# https://www.acmicpc.net/problem/16964
import sys
from collections import defaultdict


def dfs(v):
    global cnt
    cnt += 1
    visited[v] = cnt
    for i in arr[v]:
        if not visited[i]:
            dfs(i)


input = sys.stdin.readline
n = int(input())
arr = defaultdict(list)
for i in range(n - 1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
result_arr = list(map(int, input().split()))
sort_arr = [-1] * (n + 1)
for i, j in enumerate(result_arr):
    sort_arr[j] = i + 1

for i in arr.values():
    i.sort(key=lambda x: sort_arr[x])

cnt = 0
visited = [0] * (n + 1)

dfs(1)
print(1 if visited[1:] == sort_arr[1:] else 0)
