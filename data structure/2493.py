# https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = []
result = [0] * (n+1)
for i, j in enumerate(arr, start=1):
    while stack:
        if stack[-1][1] < j:
            stack.pop()
        else:
            result[i] = stack[-1][0]
            break
    stack.append((i, j))
print(*result[1:])