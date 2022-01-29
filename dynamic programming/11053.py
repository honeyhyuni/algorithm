# https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [1]

for i in range(1, n):
    d = []
    for j in range(i):
        if arr[j] < arr[i]:
            d.append(dp[j] + 1)
    if not d:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))