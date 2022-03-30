# https://www.acmicpc.net/problem/2109
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y, x]) 
arr.sort(key=lambda x : x[0])  # 일수순으로 정렬
heap = []
for i, j in arr:
    heappush(heap, j)
    if len(heap) > i:
        heappop(heap)
print(sum(heap))
