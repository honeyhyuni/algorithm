# https://www.acmicpc.net/problem/17070
import sys
input = sys.stdin.readline
n = int(input())
dp = [[[0] * 3 for i in range(n)] for i in range(n)]

arr = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n):
    if arr[0][i] == 1:
        break
    dp[0][i][0] = 1

# [0, 0, 0] 순서대로 가로, 대각선, 세로

for i in range(1, n):
    for j in range(1, n):
        if arr[i][j] == 0:
            dp[i][j][0] += dp[i][j-1][0] + dp[i][j-1][1]
            dp[i][j][2] += dp[i-1][j][1] + dp[i-1][j][2]
            if arr[i][j-1] == arr[i-1][j] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))