# https://www.acmicpc.net/problem/6198
import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
stack = []
result = 0
for i in range(n):
    while stack and arr[stack[-1]] <= arr[i]:
        stack.pop()
    stack.append(i)
    result += len(stack) - 1

print(result)