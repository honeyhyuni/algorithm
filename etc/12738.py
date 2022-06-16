# https://www.acmicpc.net/problem/12738
import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lis = []
for a in arr:
    k = bisect_left(lis, a)
    if len(lis) <= k:
        lis.append(a)
    else:
        lis[k] = a
print(len(lis))