# https://www.acmicpc.net/problem/1106
import sys
input = sys.stdin.readline
c, n = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
INF = sys.maxsize
dp = [INF] * (c+100)
dp[0] = 0

for p, co in arr:
    for j in range(co, c+100):
        dp[j] = min(dp[j-co] + p, dp[j])
print(min(dp[c:]))