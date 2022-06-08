# https://www.acmicpc.net/problem/14728
import sys
input = sys.stdin.readline
n, t = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(n)]
arr.insert(0, [0, 0])
dp = [[0] * (t+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        k, s = arr[i][0], arr[i][1]
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-k] + s)
print(dp[n][t])