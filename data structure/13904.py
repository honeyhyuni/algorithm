# https://www.acmicpc.net/problem/13904
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
heap = []
for i in range(n):
    heappush(heap, arr[i][1])
    if len(heap) > arr[i][0]:
        heappop(heap)
print(sum(heap))