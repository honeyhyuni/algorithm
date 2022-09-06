# https://www.acmicpc.net/problem/16194
import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
INF = sys.maxsize
dp = [INF] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    x = arr[i]
    for j in range(i, n+1):
        v, m = divmod(j, i)
        dp[j] = min(dp[j], v * x + dp[m], dp[j-i] + x)
print(dp[-1])