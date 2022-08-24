# https://www.acmicpc.net/problem/1082
import sys
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
INF = sys.maxsize
dp = [-INF] * (m+1)
for i in range(n-1, -1, -1):
    v = arr[i]
    for j in range(v, m+1):
        dp[j] = max(dp[j-v]*10+i, i, dp[j])
print(dp[m])