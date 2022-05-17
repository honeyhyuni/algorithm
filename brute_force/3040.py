# https://www.acmicpc.net/problem/3040
from itertools import combinations
import sys
input = sys.stdin.readline
arr = [int(input()) for i in range(9)]
lst = list(combinations(arr, 7))
for i in lst:
    if sum(i) == 100:
        print("\n".join(map(str, i)))
        break
