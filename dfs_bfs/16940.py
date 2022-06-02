# https://www.acmicpc.net/problem/16940
import sys
from collections import defaultdict, deque


def bfs(v):
    global cnt
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        for i in arr[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                q.append(i)


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

cnt = 1
visited = [0] * (n + 1)
visited[1] = 1
bfs(1)

print(1 if visited[1:] == sort_arr[1:] else 0)
