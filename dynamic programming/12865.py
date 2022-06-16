# https://www.acmicpc.net/problem/12865
# 기본 냅색문제
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
dp = [[0] * (k+1) for i in range(n+1)]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w, v = arr[i-1][0], arr[i-1][1]
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])