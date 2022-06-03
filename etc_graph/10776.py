# https://www.acmicpc.net/problem/10776
from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def dijkstra(start, k):
    dp = [[INF] * (k + 1) for i in range(n + 1)]  # 무게만큼 열 을 만들어준다.
    dp[start][k] = 0
    heap = []
    heappush(heap, [0, start, k])
    while heap:
        x, y, w = heappop(heap)
        if dp[y][w] < x:
            continue
        for n_n, n_w, nn in arr[y]:
            if w - nn <= 0:
                continue
            min_v = x + n_w
            if dp[n_n][w - nn] > min_v:
                dp[n_n][w - nn] = min_v
                heappush(heap, [min_v, n_n, w - nn])
    return dp


k, n, m = map(int, input().split())
INF = sys.maxsize
arr = [[] for i in range(n + 1)]
for i in range(m):
    a, b, t, h = map(int, input().split())
    arr[a].append([b, t, h])
    arr[b].append([a, t, h])
A, B = map(int, input().split())
result = min(dijkstra(A, k)[B])
print(result if result < sys.maxsize else -1)
