# https://www.acmicpc.net/problem/1865
import sys

input = sys.stdin.readline
T = int(input())


def bellman_ford():
    dp[1] = 0
    for i in range(n):
        for j in range(m * 2 + w):
            now_node, next_node, cost = arr[j]
            if dp[next_node] > dp[now_node] + cost:
                dp[next_node] = dp[now_node] + cost
                if i == n - 1:
                    return True
    return False


for tc in range(T):
    n, m, w = map(int, input().split())
    arr = []
    for i in range(m):
        s, e, t = map(int, input().split())
        arr.append((s, e, t))
        arr.append((e, s, t))
    for i in range(w):
        s, e, t = map(int, input().split())
        arr.append((s, e, -t))
    INF = sys.maxsize
    dp = [INF] * (n + 1)
    print("YES" if bellman_ford() else "NO")
