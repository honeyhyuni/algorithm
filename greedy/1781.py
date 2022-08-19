# https://www.acmicpc.net/problem/1781
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
heap = []
now_noodle = []
for i in range(n):
    x, y = map(int, input().split())
    heappush(heap, (x, -y))

while heap:
    dead, noodle = heappop(heap)
    if not now_noodle or len(now_noodle) < dead:
        heappush(now_noodle, -noodle)
    elif len(now_noodle) == dead and now_noodle[0] < -noodle:
        heappop(now_noodle)
        heappush(now_noodle, -noodle)
print(sum(now_noodle))
