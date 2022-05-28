# https://www.acmicpc.net/problem/15664
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = []
per = set(combinations(arr, m))
for i in sorted(list(per)):
    print(*i)
