# https://www.acmicpc.net/problem/1806
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = sys.maxsize
i, nxi = 0, 0
sum_v = 0
while nxi < n:
    if sum_v < m:
        sum_v += arr[nxi]
        nxi += 1
    else:
        sum_v -= arr[i]
        i += 1
    if sum_v >= m:
        result = min(result, nxi-i)
while i < n:
    sum_v -= arr[i]
    i += 1
    if sum_v >= m:
        result = min(result, nxi - i)

if result == sys.maxsize:
    print(0)
else:
    print(result)
