# https://www.acmicpc.net/problem/2812
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
st = list(map(str, input().rstrip()))
stack = []
for i in range(n):
    x = st[i]
    if not stack:
        stack.append(x)
        continue
    else:
        while stack and stack[-1] < x and k > 0:
            stack.pop()
            k -= 1
        stack.append(x)
while k > 0:
    stack.pop()
    k -= 1
print("".join(stack))
