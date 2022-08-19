# https://www.acmicpc.net/problem/2325
import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [defaultdict(int) for i in range(n + 1)]
Inf = sys.maxsize
prev = [-1] * (n+1)
dp = [Inf] * (n + 1)


def dijkstra():
    heap = []
    heappush(heap, (0, 1))
    dp[1] = 0
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y].items():
            min_v = dp[y] + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                prev[n_n] = y
                heappush(heap, (min_v, n_n))


for i in range(m):
    x, y, z = map(int, input().split())
    arr[x][y] = z
    arr[y][x] = z
dijkstra()

n_x = n
destroy_road = []
while n_x != -1:
    destroy_road.append((n_x, prev[n_x]))
    n_x = prev[n_x]
destroy_road.pop()

result = 0

for i, j in destroy_road:
    dp = [Inf] * (n+1)
    og = arr[i][j]
    arr[i][j] = arr[j][i] = Inf
    heap = []
    heappush(heap, (0, 1))
    dp[1] = 0
    while heap:
        x, y = heappop(heap)
        if dp[y] < x:
            continue
        for n_n, n_w in arr[y].items():
            min_v = dp[y] + n_w
            if dp[n_n] > min_v:
                dp[n_n] = min_v
                heappush(heap, (min_v, n_n))
    result = max(result, dp[-1])
    arr[i][j] = arr[j][i] = og
print(result)