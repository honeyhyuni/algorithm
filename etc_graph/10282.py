# https://www.acmicpc.net/problem/10282
from heapq import heappop, heappush

t = int(input())


def dijkstra(start):
    dp = [INF for i in range(n + 1)]
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
    return dp


for i in range(t):
    n, d, c = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    INF = 100000000
    cnt = 0
    sum_ = 0
    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append([a, s])
    result = dijkstra(c)
    for j in result:
        if j != INF:
            if sum_ < j:
                sum_ = j
            cnt += 1
    print(cnt, sum_)
