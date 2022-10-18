# https://www.acmicpc.net/problem/20007
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
n, m, x, y = map(int, input().split())
arr = [[] for i in range(n)]
INF = sys.maxsize
dp = [INF] * n

for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])

dp[y] = 0
heap = []
heappush(heap, [0, y])
while heap:
    nx, ny = heappop(heap)
    if dp[ny] < nx:
        continue
    for n_n, n_w in arr[ny]:
        min_v = nx + n_w
        if dp[n_n] > min_v:
            dp[n_n] = min_v
            heappush(heap, [min_v, n_n])

dp.sort()

total = 0
day = 1
for i in range(len(dp)):
    if dp[i] * 2 > x:
        day = -1
        break
    total += dp[i] * 2
    if total > x:
        day += 1
        total = dp[i] * 2
print(day)



