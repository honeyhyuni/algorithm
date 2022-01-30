# https://www.acmicpc.net/problem/24313
import sys
input = sys.stdin.readline
n, n1 = map(int, input().split())
m = int(input())
c = int(input())
result = []
for i in range(c, 101):
    A = n * i + n1
    B = m * i
    if A > B:
        result.append(0)
    else:
        result.append(1)

result.sort()
print(result[0])