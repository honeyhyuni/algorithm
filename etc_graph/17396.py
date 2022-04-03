# https://www.acmicpc.net/problem/17396
import sys
from heapq import heappop, heappush

n, m = map(int, input().split())
arr = [[] for i in range(n)]
INF = sys.maxsize
dp = [INF] * n

visited = list(map(int, input().split()))
visited[-1] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def dijkstar(start):
    heap = []
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y]:
            min_v = x + n_w
            if dp[n_n] > min_v and visited[n_n] == 0:
                dp[n_n] = min_v
                heappush(heap, [min_v, n_n])
    return dp[n - 1]


result = dijkstar(0)
print(result if result != INF else -1)

