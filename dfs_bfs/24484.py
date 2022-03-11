# https://www.acmicpc.net/problem/24484
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(v):
    global cnt
    global sum_
    sum_ += cnt * visited[v]
    for _ in arr[v]:
        if visited[_] == -1:
            cnt += 1
            visited[_] = visited[v] + 1
            dfs(_)


n, m, r = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
visited = [-1] * (n + 1)
visited[r], cnt, sum_ = 0, 1, 0
for i in arr:
    i.sort(reverse=True)
dfs(r)
print(sum_)