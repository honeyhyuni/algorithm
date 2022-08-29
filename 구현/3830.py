# https://www.acmicpc.net/problem/16202
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())


def parent_find(v):
    if v != parent[v]:
        parent[v] = parent_find(parent[v])
    return parent[v]


def union(a, b):
    a_n = parent_find(a)
    b_n = parent_find(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        return True
    return False


node = deque()
for i in range(m):
    a, b = map(int, input().split())
    node.append((a, b, i + 1))

t = set()
for i in range(k):
    result = 0
    s = set()
    cnt = 0
    parent = [i for i in range(n + 1)]
    for a, b, c in node:
        if c in t:
            continue
        if union(a, b):
            result += c
            s.add(c)
            if cnt == 0:
                cnt += 1
                t.add(c)
    if len(s) != n-1:
        print(0, end=' ')
    else:
        print(result, end=' ')
