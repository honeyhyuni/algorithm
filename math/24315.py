# https://www.acmicpc.net/problem/24315
import sys
input = sys.stdin.readline
n, n1 = map(int, input().split())
m, m1 = map(int, input().split())
c = int(input())
result = []
for i in range(c, 101):
    A = n * i + n1
    B = m * i
    C = m1 * i
    if B <= A <= C:
        result.append(1)
    else:
        result.append(0)
result.sort()
print(result[0])