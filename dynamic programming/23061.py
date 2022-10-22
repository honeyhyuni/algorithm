# https://www.acmicpc.net/problem/23061
import sys
import math


def lcm(a, b):
    return a * b // math.gcd(a, b)


input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
arr.insert(0, [0, 0])
result = [0]
bag_w = []
for _ in range(m):
    bag_w.append(int(input()))
bag_w_m = max(bag_w)
dp = [[0] * (bag_w_m + 1) for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, bag_w_m + 1):
        w, v = arr[i][0], arr[i][1]
        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

result = 0
for i in range(1, m):
    temp = lcm(bag_w[result], bag_w[i])
    var, var2 = dp[n][bag_w[result]] * temp // bag_w[result], dp[n][bag_w[i]] * temp // bag_w[i]
    if var2 > var:
        result = i
print(result+1)
