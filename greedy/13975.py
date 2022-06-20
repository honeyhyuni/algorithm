# https://www.acmicpc.net/problem/13975
import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    heap = list(map(int, input().split()))
    heapify(heap)
    result = 0
    while len(heap) > 1:
        x = heappop(heap)
        y = heappop(heap)
        result += (x + y)
        heappush(heap, x + y)
    print(result)