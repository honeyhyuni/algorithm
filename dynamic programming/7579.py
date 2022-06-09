# https://www.acmicpc.net/problem/7579
# 배낭문제
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))
dp = [[0] * (sum(C)+1) for i in range(len(A))]

result = sys.maxsize
for i in range(1, len(A)):
    a, c = A[i], C[i]
    for j in range(1, sum(C)+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c] + a)
        if dp[i][j] >= m:
            result = min(result, j)
print(result)