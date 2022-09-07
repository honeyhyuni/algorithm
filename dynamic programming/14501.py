# https://www.acmicpc.net/problem/14501
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    x, y = arr[i]
    if i + x > n:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(y, y + dp[i+x], dp[i+1])
print(dp[0])