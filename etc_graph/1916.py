# https://www.acmicpc.net/problem/1916
from heapq import heappush, heappop

n = int(input())
m = int(input())

arr = [[] for i in range(n + 1)]
INF = 100000000
dp = [INF for i in range(n + 1)]
for i in range(m):
    a, b, w = map(int, input().split())
    arr[a].append([b, w])
start, end = map(int, input().split())


def dijkstra(start):
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n2, m2 in arr[y]:
            total = x + m2
            if dp[n2] > total:
                dp[n2] = total
                heappush(heap, [total, n2])


dijkstra(start)
print(dp[end])
