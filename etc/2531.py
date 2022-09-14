# https://www.acmicpc.net/problem/2531
import sys
from collections import defaultdict
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
arr = [int(input()) for i in range(n)]

s = defaultdict(int)

for i in range(k):
    s[arr[i]] += 1
s[c] += 1
l, r = 0, k
result = 0
while l < n:
    result = max(result, len(s))
    nr = r % n
    s[arr[nr]] += 1
    s[arr[l]] -= 1
    if s[arr[l]] == 0:
        del s[arr[l]]
    l += 1
    r += 1
print(result)
