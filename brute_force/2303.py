# https://www.acmicpc.net/problem/2303
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
result = []
for i in range(n):
    arr = list(map(int, input().split()))
    com = list(combinations(arr, 3))
    num = 0
    for c in com:
        temp = int(str(sum(c))[-1])
        num = max(num, temp)
    result.append([num, i + 1])
print(sorted(result, key=lambda x: (-x[0], -x[1]))[0][1])