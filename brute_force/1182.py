# https://www.acmicpc.net/problem/1182
from itertools import combinations
import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    result_arr = list(combinations(arr, i))
    for re in result_arr:
        if sum(re) == s:
            cnt += 1
print(cnt)
