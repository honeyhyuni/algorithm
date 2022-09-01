# https://www.acmicpc.net/problem/2156
import sys
input = sys.stdin.readline
n = int(input())
arr = [0] * 10001
dp = [0] * 10001
for i in range(n):
    arr[i] = int(input())
dp[0], dp[1] = arr[0], arr[0] + arr[1]
for i in range(2, n):
    dp[i] = max(dp[i-3] + arr[i] + arr[i-1], dp[i-2] + arr[i], dp[i-1])
print(dp[n-1])