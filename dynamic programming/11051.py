# https://www.acmicpc.net/problem/11051
n, k = map(int, input().split())
dp = [[0] for i in range(n+2)]
dp[1].append(1)
for i in range(2, n+2):
    for j in range(1, i+1):
        if j == 0 or j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1] + dp[i-1][j])
print(dp[-1][k+1] % 10007)