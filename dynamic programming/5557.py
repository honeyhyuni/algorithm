# https://www.acmicpc.net/problem/5557
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [[0] * 21 for i in range(n-1)]
dp[0][arr[0]] = 1
for i in range(1, n-1):
    x = arr[i]
    for j in range(21):
        if dp[i-1][j] > 0:
            for _ in [j + x, j - x]:
                if 0 <= _ <= 20:
                    dp[i][_] += dp[i-1][j]
print(dp[-1][arr[-1]])