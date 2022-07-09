# https://www.acmicpc.net/problem/23801
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
INF = sys.maxsize

for i in range(m):
    u, v, w = map(int, input().split())
    arr[u].append([v, w])
    arr[v].append([u, w])


def dijkstra(start):
    dp = [INF] * (n + 1)
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
    return dp


a, b = map(int, input().split())
p = int(input())
p_arr = list(map(int, input().split()))

dp_ = dijkstra(a)
dp2 = dijkstra(b)

result = INF
for i in p_arr:
    result = min(result, dp_[i] + dp2[i])

if result >= INF:
    print(-1)
else:
    print(result)

