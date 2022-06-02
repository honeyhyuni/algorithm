# https://www.acmicpc.net/problem/5582
str1 = input().rstrip()
str2 = input().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
answer = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(max(map(max, dp)))