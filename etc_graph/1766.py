# https://www.acmicpc.net/problem/1766
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, m = map(int, input().split())
degree = [0] * (n+1)

arr = [[] for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    degree[y] += 1
    arr[x].append(y)

heap = []

for i in range(1, n+1):
    if degree[i] == 0:
        heappush(heap, i)
while heap:
    x = heappop(heap)
    if degree[x] == 0:
        print(x, end=' ')
    for n_n in arr[x]:
        degree[n_n] -= 1
        if degree[n_n] == 0:
            heappush(heap, n_n)