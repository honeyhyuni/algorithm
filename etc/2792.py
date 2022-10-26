# https://www.acmicpc.net/problem/2792
import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for i in range(m)]

start, end = 1, max(arr)
result = []
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += math.ceil(i / mid)

    if cnt > n:
        start = mid + 1

    else:
        end = mid - 1
        result.append(mid)
print(min(result))