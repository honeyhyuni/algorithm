# https://www.acmicpc.net/problem/17178
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    st = list(map(str, input().split()))
    arr.extend(st)
stack = deque()
ans = [[] for i in range(26)]
bol = True
while arr:
    al, num = arr.pop(0).split('-')
    num = int(num)
    while stack and (stack[-1][0] < al or (stack[-1][0] == al and stack[-1][1] < num)):
        x, y = stack.pop()
        x_ = ord(x) - 65
        for i in range(25, x_, -1):
            if ans[i]:
                bol = False
        if ans[x_]:
            if max(ans[x_]) > y:
                bol = False
        ans[x_].append(y)
    stack.append((al, num))

while stack:
    x, y = stack.pop()
    x_ = ord(x) - 65
    for i in range(25, x_, -1):
        if ans[i]:
            bol = False
    if ans[x_]:
        if max(ans[x_]) > y:
            bol = False
    ans[x_].append(y)

print("GOOD" if bol else "BAD")