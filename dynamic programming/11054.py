# https://www.acmicpc.net/problem/11054
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
p_dp, m_dp = [0] * n, [0] * n
p_dp[0], m_dp[-1] = 1, 1

for i in range(1, n):
    pd = []
    for j in range(i):
        if arr[i] > arr[j]:
            pd.append(p_dp[j] + 1)
    if not pd:
        p_dp[i] = 1
    else:
        p_dp[i] = max(pd)
for i in range(n-2, -1, -1):
    md = []
    for j in range(n-1, i, -1):
        if arr[i] > arr[j]:
            md.append(m_dp[j] + 1)
    if not md:
        m_dp[i] = 1
    else:
        m_dp[i] = max(md)
result = 0
for i, j in zip(m_dp, p_dp):
    result = max(result, i + j)
print(result-1)