# https://www.acmicpc.net/problem/15655
from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
lst = list(combinations(arr, m))
for i in lst:
    print(*i)