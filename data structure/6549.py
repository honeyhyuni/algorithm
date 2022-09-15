# https://www.acmicpc.net/problem/6549
import sys
input = sys.stdin.readline
while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    if n == 0: break
    stack = []
    result = 0
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            temp = stack.pop()
            if not stack:
                w = i
            else:
                w = i - stack[-1] - 1
            result = max(result, w * arr[temp])
        stack.append(i)
    while stack:
        temp = stack.pop()
        if not stack:
            w = n
        else:
            w = n - stack[-1] - 1
        result = max(result, w * arr[temp])
    print(result)