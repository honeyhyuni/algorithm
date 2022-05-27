# https://www.acmicpc.net/problem/16562
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]


def find_parent(var):
    if var != parent[var]:
        parent[var] = find_parent(parent[var])
    return parent[var]


for i in range(m):
    a, b = map(int, input().split())
    a_n, b_n = find_parent(a), find_parent(b)
    if a_n != b_n:
        if cost[a_n] <= cost[b_n]:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
result = 0
for i, j in enumerate(parent):
    if i == j:
        result += cost[i]

print("Oh no" if result > k else result)
