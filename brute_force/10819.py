# https://www.acmicpc.net/problem/10819
from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
per = list(permutations(arr, n))
max_v = -1
for i in per:
    sum_v = 0
    for j in range(len(i)-1):
        sum_v += abs(i[j] - i[j+1])
    max_v = max(max_v, sum_v)
print(max_v)