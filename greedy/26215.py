# https://www.acmicpc.net/problem/26215
import sys
input = sys.stdin.readline
from heapq import heappop, heappush, heapify
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] *= -1
cnt, temp = 0, 0
heapify(arr)
while len(arr) >= 2:
    x = heappop(arr)
    y = heappop(arr)
    x = -x
    y = -y
    if x == y:
        cnt += x
    else:
        cnt += y
        heappush(arr, -(x-y))
if arr:
    cnt += -arr[0]
print(cnt if cnt <= 1440 else -1)