# https://www.acmicpc.net/problem/13398
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
INF = sys.maxsize
dp = [[-INF] * n for i in range(2)]
dp[0][0] = arr[0]
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

print(max(map(max, dp)))