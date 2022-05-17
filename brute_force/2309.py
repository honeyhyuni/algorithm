# https://www.acmicpc.net/problem/2309
from itertools import combinations

arr = sorted([int(input()) for i in range(9)])
lst = list(combinations(arr, 7))
for i in lst:
    if sum(i) == 100:
        print("\n".join(map(str, i)))
        break
