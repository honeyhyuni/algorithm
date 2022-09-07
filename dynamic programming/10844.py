# https://www.acmicpc.net/problem/10844
n = int(input())
dp = [[0] * 10 for i in range(n+1)]
dp[1][1:] = [1] * 9

for i in range(2, n+1):
    for j in range(10):
        if j == 0 or j == 9:
            dp[i][j] = dp[i-1][abs(1-j)]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)