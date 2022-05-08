# https://www.acmicpc.net/problem/5972
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra():
    dp[1] = 0
    heap = []
    heappush(heap, [0, 1])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp[n]


n, m = map(int, input().split())

arr = [[] for i in range(n + 1)]
INF = sys.maxsize
dp = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

print(dijkstra())


