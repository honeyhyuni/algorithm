# https://www.acmicpc.net/problem/14284
from heapq import heappop, heappush

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
INF = 100000000
dp = [INF for i in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])
start, end = map(int, input().split())


def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])


dijkstra(start)
print(dp[end])
