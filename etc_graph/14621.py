# https://www.acmicpc.net/problem/14621
import sys

input = sys.stdin.readline


def find_parent(var):
    if var != parent[var]:
        parent[var] = find_parent(parent[var])
    return parent[var]


def union_parent(a, b):
    a_v = find_parent(a)
    b_v = find_parent(b)
    if a_v != b_v:
        if a_v < b_v:
            parent[b_v] = a_v
        else:
            parent[a_v] = b_v


n, m = map(int, input().split())
gender = [" "] + list(map(str, input().split()))
parent = [i for i in range(n + 1)]

node = []
for i in range(m):
    a, b, c = map(int, input().split())
    node.append((c, a, b))
    node.append((c, b, a))

node.sort()
result = 0
s = set()
for cost, a, b in node:
    if gender[a] != gender[b]:
        if find_parent(a) != find_parent(b):
            s.update([a, b])
            union_parent(a, b)
            result += cost
if len(s) == n:
    print(result)
else:
    print(-1)