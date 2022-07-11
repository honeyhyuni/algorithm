# https://www.acmicpc.net/problem/1461
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
minus, plus = [], []
max_v = 0
for i in arr:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
    max_v = max(max_v, abs(i))
result = []
minus.sort()
plus.sort(reverse=True)
for i in range(0, len(minus), m):
    if abs(minus[i]) != max_v:
        result.append(minus[i])

for i in range(0, len(plus), m):
    if abs(plus[i]) != max_v:
        result.append(plus[i])

ans = 0
for i in result:
    ans += abs(i*2)
print(ans + abs(max_v))