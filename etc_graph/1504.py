# https://www.acmicpc.net/problem/1504
from heapq import heappop, heappush

n, e = map(int, input().split())
arr = [[] for i in range(n + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

n2, n3 = map(int, input().split())
INF = 100000000


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


one = dijkstra(1)
n2_ = dijkstra(n2)
n3_ = dijkstra(n3)

result = min(one[n2] + n2_[n3] + n3_[n], one[n3] + n3_[n2] + n2_[n])
if result < INF:
    print(result)
else:
    print(-1)