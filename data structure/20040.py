# https://www.acmicpc.net/problem/20040
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]


def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a_n, b_n = find_parent(a), find_parent(b)
    if a_n != b_n:
        if a_n < b_n:
            parent[b_n] = a_n
        else:
            parent[a_n] = b_n
        return True
    return False


result = []
for i in range(m):
    a, b = map(int, input().split())
    if not union(a, b):
        result.append(i + 1)
print(result[0] if result else 0)