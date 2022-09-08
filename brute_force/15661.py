# https://www.acmicpc.net/problem/15661
import sys
from itertools import combinations
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
temp = set([i for i in range(n)])
result = sys.maxsize

for i in range(2, n//2+1):
    t = set(combinations(temp, i))
    for j in t:
        j = set(j)
        divide = temp - j
        start, link = 0, 0
        for _ in j:
            for __ in j:
                start += arr[_][__]
        for _ in divide:
            for __ in divide:
                link += arr[_][__]
        result = min(result, abs(start - link))
print(result)