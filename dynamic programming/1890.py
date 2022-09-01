# https://www.acmicpc.net/problem/1890
import sys
input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        x = arr[i][j]
        if dp[i][j] > 0 and x > 0:
            for nx, ny in [(i + x, j), (i, j + x)]:
                if 0 <= nx < n and 0 <= ny < n:
                    dp[nx][ny] += dp[i][j]
print(dp[-1][-1])
