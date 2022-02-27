# https://www.acmicpc.net/problem/11659
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = [0]

temp = 0
for i in a:
    temp += i
    a_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(a_sum[b]-a_sum[a-1])
