# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations

input = sys.stdin.readline
l, c = map(int, input().split())
arr = sorted(list(map(str, input().split())))
comb = list(combinations(arr, l))

for i in comb:
    cc = 0
    for j in ['a', 'i', 'o', 'u', 'e']:
        if j in i:
            cc += 1
    if 0 < cc <= l-2:
        print("".join(i))
