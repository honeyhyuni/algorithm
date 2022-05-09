# https://www.acmicpc.net/problem/14888
from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
lst = ["+", "-", "*", "/"]
d = list(map(int, input().split()))
op = []
for i, j in zip(lst, d):
    for k in range(j):
        op += i
operator = list(permutations(op))


result = []
for p in operator:
    stack = [arr[0]]
    for i, j in zip(arr[1:], p):
        if j == "*":
            stack.append(stack[-1] * i)
        elif j == "+":
            stack.append(stack[-1] + i)
        elif j == "/":
            if stack[-1] < 0:
                stack.append(-(abs(stack[-1]) // i))
            else:
                stack.append(stack[-1] // i)
        else:
            stack.append(stack[-1] - i)
    result.append(stack[-1])
print(max(result))
print(min(result))
