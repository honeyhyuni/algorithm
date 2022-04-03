# https://www.acmicpc.net/problem/22865
import sys
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra(start):
    dp = [INF] * (n + 1)
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        x1, y1 = heappop(heap)
        if dp[y1] < x1:
            continue
        for n_n, n_w in arr[y1]:
            min_v = x1 + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp


n = int(input())
a, b, c = map(int, input().split())
m = int(input())
arr = [[] for i in range(n + 1)]
INF = sys.maxsize
for i in range(m):
    x, y, z = map(int, input().split())
    arr[x].append([y, z])
    arr[y].append([x, z])

dp_a = dijkstra(a)
dp_b = dijkstra(b)
dp_c = dijkstra(c)

result = -1
for i in range(1, n + 1):
    if result < min(dp_a[i], dp_b[i], dp_c[i]):
        result = min(dp_a[i], dp_b[i], dp_c[i])
        idx = i

print(idx)