# https://www.acmicpc.net/problem/11779
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for i in range(n + 1)]
INF = sys.maxsize
dp = [INF] * (n + 1)
node_v = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

start, end = map(int, input().split())


def dijkstra(start, end):
    node_v[start].append(start)
    heap = []
    heappush(heap, [0, start])
    dp[start] = 0
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
                node_v[n_n] = []
                for p in node_v[y]:
                    node_v[n_n].append(p)
                node_v[n_n].append(n_n)
    return dp[end]


print(dijkstra(start, end))
print(len(node_v[end]))
for i in node_v[end]:
    print(i, end=' ')
