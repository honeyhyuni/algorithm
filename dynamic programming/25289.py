# https://www.acmicpc.net/problem/25289
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

ans = 1

for t in range(-100, 101):
    dp = [0] * 101
    for i in range(n):
        if arr[i] - t < 1 or arr[i] - t > 100:
            dp[arr[i]] = 1
        else:
            dp[arr[i]] = dp[arr[i]- t] + 1
        ans = max(ans, dp[arr[i]])
print(ans)