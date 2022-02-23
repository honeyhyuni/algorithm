# https://www.acmicpc.net/problem/10845
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    x = input().split()
    if x[0] == "push":
        q.append(x[1])
    elif x[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif x[0] == "size":
        print(len(q))
    elif x[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif x[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])