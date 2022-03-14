# https://www.acmicpc.net/problem/1374
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x, y, z = map(int, input().split())
    heappush(heap, [y, z])
result = []
start, end = heappop(heap)
heappush(result, end)
while heap:
    start, end = heappop(heap)
    if result[0] <= start:
        heappop(result)
    heappush(result, end)
print(len(result))
