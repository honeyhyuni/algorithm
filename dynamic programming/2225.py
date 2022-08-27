# https://www.acmicpc.net/problem/2225
n, k = map(int, input().split())
dp = [[0] * (n+1) for i in range(k)]
dp[0] = [1] * (n+1)
for i in range(1, k):
    for j in range(1, n+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[-1][-1] % 1000000000)