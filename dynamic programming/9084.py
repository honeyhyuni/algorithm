# https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    dp = [0] * (m+1)
    dp[0] = 1
    for i in money:
        for j in range(1, m+1):
            if j - i >= 0:
                dp[j] += dp[j-i]
    print(dp[-1])