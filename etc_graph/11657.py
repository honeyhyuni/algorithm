# https://www.acmicpc.net/problem/11657
# 벨만-포드 기본 이론 문제
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for i in range(m)]
INF = sys.maxsize
dp = [INF] * (n + 1)


def bellman_ford():
    dp[1] = 0
    for i in range(n):
        for j in range(m):
            now_node, next_node, cost = arr[j]
            if dp[now_node] != INF and dp[next_node] > dp[now_node] + cost:
                dp[next_node] = dp[now_node] + cost
                if i == n-1:
                    return False
    return True


result = bellman_ford()
if not result:
    print(-1)
else:
    for i in dp[2:]:
        print(-1 if i >= INF else i)