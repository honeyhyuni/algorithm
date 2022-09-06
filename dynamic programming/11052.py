# https://www.acmicpc.net/problem/11052
import sys
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(1, n+1):
    x = arr[i]
    for j in range(i, n+1):
        v, m = divmod(j, i)
        dp[j] = max(dp[j], x * v + dp[m], dp[j-i] + x)
print(dp[-1])