# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * (k+1)
dp[0] = 1
for i in arr:
    for j in range(i, k+1):
        dp[j] += dp[j-i]
print(dp[-1])