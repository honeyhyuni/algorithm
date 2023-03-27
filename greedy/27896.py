# https://www.acmicpc.net/problem/27896
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

total, heap = 0, []

for i in arr:
    heappush(heap, -i)
    total += i
    if total >= m:
        total += (heappop(heap) * 2)

print(n - len(heap))