# https://www.acmicpc.net/problem/16681
import sys
from heapq import heappop, heappush


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
            if H[n_n] > H[y]:
                min_v = x + n_w
                if dp[n_n] >= min_v:
                    dp[n_n] = min_v
                    heappush(heap, [min_v, n_n])
    return dp


input = sys.stdin.readline
n, m, d, e = map(int, input().split())
H = [0] + list(map(int, input().split()))
INF = sys.maxsize
arr = [[] for i in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

home = dijkstra(1)
college = dijkstra(n)
result = INF * -1
for i in range(1, n + 1):
    if home[i] != INF and college[i] != INF:
        result = max(result, (H[i] * e) - (home[i] + college[i]) * d)

if result == INF * -1:
    print("Impossible")
else:
    print(result)
