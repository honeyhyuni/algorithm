# https://www.acmicpc.net/problem/23793
from heapq import heappop, heappush
import sys


def dijkistra(start, bol):
    dp = [INF] * (n + 1)
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            if bol:
                if n_n == v:
                    continue
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp


input = sys.stdin.readline
n, m = map(int, input().split())
INF = sys.maxsize
arr = [[] for i in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
u, v, w = map(int, input().split())

bol = False

result = dijkistra(u, bol)
result2 = dijkistra(v, bol)
result3 = result[v] + result2[w]
if result3 >= INF:
    print(-1, end=' ')
else:
    print(result3, end=' ')

bol = True
result = dijkistra(u, bol)
if result[w] >= INF:
    print(-1, end=' ')
else:
    print(result[w], end=' ')
