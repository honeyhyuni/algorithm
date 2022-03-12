# https://www.acmicpc.net/problem/1238
from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n, m, X = map(int, input().split())
arr = [[] for i in range(n + 1)]
INF = sys.maxsize

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

                        
def dijkstra(start):  # 다익스트라 최단경로
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


result3 = 0
for i in range(1, n + 1):
    result = dijkstra(i)
    result2 = dijkstra(X)
    result3 = max(result3, result[X] + result2[i])
print(result3)
