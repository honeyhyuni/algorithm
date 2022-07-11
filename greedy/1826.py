# https://www.acmicpc.net/problem/1826
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())
gas = []
[heappush(gas, list(map(int, input().split()))) for i in range(n)]

l, p = map(int, input().split())
heap = []
result = 0
while p < l:
    while gas and gas[0][0] <= p:
        x, y = heappop(gas)
        heappush(heap, [-y, x])
    if not heap:
        result = -1
        break
    y, x = heappop(heap)
    p += -y
    result += 1

print(result)