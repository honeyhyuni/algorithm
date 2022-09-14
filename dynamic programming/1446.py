# https://www.acmicpc.net/problem/1446
import sys
input = sys.stdin.readline
n, d = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [i for i in range(d+1)]
for i in range(d+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    for s, e, v in arr:
        if i == s and e <= d:
            dp[e] = min(dp[e], dp[s] + v)
print(dp[-1])