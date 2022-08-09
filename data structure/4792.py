# https://www.acmicpc.net/problem/4792
import sys

input = sys.stdin.readline


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a_n = find_parent(a)
    b_n = find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n


def check(node):
    t = 0
    for a, b, c in node:
        if find_parent(b) != find_parent(c):
            union(b, c)
            if a == "B":
                t += 1
    return t


while True:
    n, m, k = map(int, input().split())
    if n == 0 and m == 0 and k == 0:break
    node = []
    for i in range(m):
        x, y, z = map(str, input().split())
        node.append((x, int(y), int(z)))
    parent = [i for i in range(n + 1)]
    B_max = check(sorted(node))
    parent = [i for i in range(n + 1)]
    B_min = check(sorted(node, reverse=True))
    print(1) if B_min <= k <= B_max else print(0)