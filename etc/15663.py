# https://www.acmicpc.net/problem/15663
import sys
from itertools import permutations
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
combo = set(permutations(sorted(arr), m))
for i in sorted(combo):
    print(*i)
