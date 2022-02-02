# https://www.acmicpc.net/problem/11279
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
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
        heappush(heap, [-x, x])
