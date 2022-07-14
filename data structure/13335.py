# https://www.acmicpc.net/problem/13335
import sys
from collections import deque
input = sys.stdin.readline
n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
q = deque([0] * w)
cnt = 0
while q:
    q.popleft()
    if truck:
        if sum(q) + truck[0] <= l:
            q.append(truck.pop(0))
        else:
            q.append(0)
    cnt += 1
print(cnt)