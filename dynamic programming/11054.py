# https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
p_dp, m_dp = [1] * n, [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            p_dp[i] = max(p_dp[i], p_dp[j]+1)
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            m_dp[i] = max(m_dp[i], m_dp[j]+1)

result = 0
for i, j in zip(m_dp, p_dp):
    result = max(result, i + j)
print(result-1)