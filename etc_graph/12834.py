# https://www.acmicpc.net/problem/12834
import sys
from heapq import heappop, heappush


def dijkstra(start):
    dp = [INF] * (v + 1)
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


input = sys.stdin.readline
n, v, e = map(int, input().split())
A, B = map(int, input().split())
H = list(map(int, input().split()))
INF = sys.maxsize
arr = [[] for i in range(v + 1)]
for i in range(e):
    a, b, l = map(int, input().split())
    arr[a].append([b, l])
    arr[b].append([a, l])
result = 0
for i in range(n):
    ar = dijkstra(H[i])
    a, b = ar[A], ar[B]
    if a == INF:
        a = -1
    if b == INF:
        b = -1
    result += a + b
print(result)
