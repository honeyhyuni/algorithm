# https://www.acmicpc.net/problem/1753
# 다익스트라 기본 이론 문제
from heapq import heappop, heappush

v, e = map(int, input().split())
start = int(input())

arr = [[] for i in range(v + 1)]
INF = 100000000
dp = [INF for i in range(v + 1)]
for i in range(e):
    a, b, w = map(int, input().split())
    arr[a].append([b, w])


def dijkstra(start):
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for x2, y2 in arr[y]:
            min_v = x + y2
            if dp[x2] > min_v:
                dp[x2] = min_v
                heappush(heap, [min_v, x2])


dijkstra(start)
for i in dp[1:]:
    print(i if i != INF else "INF")