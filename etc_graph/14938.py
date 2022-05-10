# https://www.acmicpc.net/problem/14938
from heapq import heappop, heappush

n, m, r = map(int, input().split())

item = list(map(int, input().split()))
arr = [[] for i in range(n + 1)]

for i in range(r):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def dijkstra(start):
    heap = []
    INF = 100000000
    dp = [INF for i in range(n + 1)]
    dp[start] = 0
    heappush(heap, [0, start])
    item_sum = 0
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    for i in range(1, n + 1):
        if dp[i] <= m:
            item_sum += item[i - 1]
    return item_sum


result = 0
for i in range(1, n + 1):
    result = (max(result, dijkstra(i)))

print(result)
