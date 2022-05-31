# https://www.acmicpc.net/problem/1655
from heapq import heappop, heappush
import sys
input = sys.stdin.readline
n = int(input())
small, big = [], []
for i in range(n):
    x = int(input())
    if len(small) == len(big):
        heappush(small, (-x, x))
    else:
        heappush(big, x)
    if big and small[0][1] > big[0]:
        sm = heappop(small)
        b = heappop(big)
        heappush(big, sm[1])
        heappush(small, (-b, b))
    print(small[0][1])