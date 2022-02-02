# https://www.acmicpc.net/problem/11286
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, [abs(x), x])