# https://www.acmicpc.net/problem/1135
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
tree = [[] for i in range(n)]
dp = [-1] * n

for i in range(1, len(arr)):
    tree[arr[i]].append(i)


def dfs(v):
    temp = []
    for i in tree[v]:
        dfs(i)
        temp.append(dp[i])
    if not tree[v]:
        temp.append(0)
    if len(temp) > 1:
        temp.sort(reverse=True)
    temp_ = [temp[i] + i + 1 for i in range(len(temp))]
    dp[v] = max(temp_)


dfs(0)
print(dp[0] - 1)
