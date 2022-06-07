# https://www.acmicpc.net/problem/9370
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
            min_v = x + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp


input = sys.stdin.readline
T = int(input())
INF = sys.maxsize
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    arr = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, d = map(int, input().split())
        arr[a].append([b, d])
        arr[b].append([a, d])
    result = []
    for i in range(t):
        result.append(int(input()))
    start_v = dijkstra(s)
    g_v = dijkstra(g)
    h_v = dijkstra(h)

    total_an = []

    for i in result:
        if start_v[g] + g_v[h] + h_v[i] == start_v[i] or start_v[h] + h_v[g] + g_v[i] == start_v[i]:
            total_an.append(i)
    total_an.sort()

    for i in total_an:
        print(i, end=' ')