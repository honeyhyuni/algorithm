# https://www.acmicpc.net/problem/14889
from itertools import combinations
import sys
input = sys.stdin.readline
n = int(input())
arr = []
result = sys.maxsize
for i in range(n):
    arr.append(list(map(int, input().split())))
com = [i for i in range(n)]
comb = combinations(com, n//2)
for _ in comb:
    start, link = 0, 0
    temp = set(com) - set(_)
    for i, j in combinations(_, 2):
        start += (arr[i][j] + arr[j][i])
    for i, j in combinations(temp, 2):
        link += (arr[i][j] + arr[j][i])
    result = min(result, abs(start - link))
print(result)