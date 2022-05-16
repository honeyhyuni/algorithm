# https://www.acmicpc.net/problem/14395
import sys
from collections import deque

s, t = map(int, input().split())
if s == t:
    print(0)
else:
    q = deque()
    q.append([s, ""])
    visited = set()
    visited.add(s)
    op = ["*", "+", "/"]
    while q:
        x, st = q.popleft()
        if x == t:
            print(st)
            sys.exit()
        for i, j in [[0, x * x], [1, x + x], [2, 1]]:
            if (i == 2 and x == 0) or j in visited or j > t:
                continue
            q.append([j, st + op[i]])
            visited.add(j)
    print(-1)
