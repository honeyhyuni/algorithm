# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))


chicken_com = list(combinations(chicken, m))
result = [0] * len(chicken_com)

for i in home:
    for j in range(len(chicken_com)):
        min_v = sys.maxsize
        for k in chicken_com[j]:
            sum_v = abs(i[0] - k[0]) + abs(i[1] - k[1])
            min_v = min(min_v, sum_v)
        result[j] += min_v
print(min(result))
